#!/usr/bin/env python3
"""Fully-remote episodes: generate a face-crop schedule for a clipify vertical
short. Tracks the ACTIVE speaker: solo shots crop around that person's face;
split-screen shots crop the speaking panel.

Crop-switch rules (the subtle part):
- **EVERY crop switch is a HARD CUT (mode "cut"). Never emit "swipe" here.** The
  crop is a 406 px column of a 1280 px frame, which is NARROWER than the gap
  between any two faces in any layout — so a glide of ANY length necessarily
  passes through the seam between panels, showing wall plus two half-faces (i.e.
  nobody). Verified frame-by-frame on Ep 8: at 0.15 s into a 0.35 s swipe the crop
  sat at x=526, straddling the trio's middle/right panels. This holds even for
  an in-layout speaker switch where both people are on screen in the SOURCE — they
  are never both in the CROP, so "they're both visible, so easing is fine" is
  wrong. It's only true if you widen the column past the face spacing.
- Symptom when this is violated: the shot appears to swing off a person and
  boomerang back (worst when the same person is on both sides of the switch, e.g.
  duo(jackson,tyler) -> solo(jackson), where the pan leaves and returns to the
  same face). Ep 8's first clip batch shipped 10 of these because clipify swiped
  every key by default.
- Layout boundaries switch EXACTLY at the boundary — carrying the old x into a new
  layout lands on the seam. The panel chosen AT the boundary is the one that holds
  the first shot, decided with lookahead, not the panel that happens to have a
  transient on it at that instant.
- WITHIN a constant layout the schedule is built with LOOKAHEAD, not a lag: the
  whole piece's speech is known up front, so a speaker switch fires at the true
  onset of the new speaker, and only if that speaker then HOLDS the shot for at
  least `face_min_shot` s (remote_plan.json params; default 1.0). A cough, a
  "yeah", a chair creak on the other mic used to flip the crop and flip it back
  (Ep 14 flicker); now any shot shorter than the minimum is absorbed into its
  neighbour. The current speaker is also STICKY: while they are still talking,
  a sound on another panel never wins. Note the VAD alone smears every transient
  to ~0.4 s, so a threshold below ~0.6 s filters nothing — do not go there.

usage: python3 remote_face_crops.py <workdir> <final_start> <final_end> [--debug]
prints a "face_crops" JSON array for the clipify clip entry. Warnings go to stderr;
--debug also dumps every speaker run (raw and after the hold) with its talk time.
"""
import json, sys, wave
import numpy as np

DEBUG = '--debug' in sys.argv
WORK, A, B = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
cl = json.load(open(f'{WORK}/clips.json'))
OFF = json.load(open(f'{WORK}/offsets.json'))
SRC = json.load(open(f'{WORK}/sources.json'))
PLAN = json.load(open(f'{WORK}/remote_plan.json'))
PERSON = {nm: t['person'] for nm, t in SRC['tracks'].items()}
FACE_CX = PLAN.get('face_cx', {'jackson': 620, 'chris': 600, 'tyler': 660})
MIN_SHOT = float(PLAN.get('params', {}).get('face_min_shot', 1.0))
TRAIL_GUARD = 0.5
CW = 406  # 9:16 column of a 720p frame
STEP = 0.01  # VAD grid

VAD = {}
for nm in PERSON:
    w = wave.open(f'{WORK}/audio/{nm}_16k.wav', 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    n = len(x) // 160
    e = np.sqrt(np.mean(x[:n * 160].reshape(n, 160) ** 2, axis=1))
    thr = max(np.percentile(e, 10) * 6, 0.004)
    VAD[nm] = np.convolve((e > thr).astype(np.float32), np.ones(41), 'same') > 0


def active_grid(person, m_lo, m_hi):
    """Boolean activity for `person` on the STEP grid over master time [m_lo, m_hi)."""
    n = int(round((m_hi - m_lo) / STEP))
    out = np.zeros(n, dtype=bool)
    for nm, p in PERSON.items():
        if p != person:
            continue
        idx = ((m_lo - OFF[nm]) / STEP + np.arange(n)).astype(int)
        ok = (idx >= 0) & (idx < len(VAD[nm]))
        out[ok] |= VAD[nm][idx[ok]]
    return out


def panel_offsets(n_panels):
    if n_panels == 2:
        return [117, 757]            # face-centered 406 col inside each 640 panel
    return [10, 437, 864]            # inside 426/428/426 panels


def sticky_timeline(acts, start_k):
    """Per-step panel index: stay on the current panel while it is active, move to
    the first other active panel when it goes quiet, hold through silence."""
    n = acts.shape[1]
    tl = np.empty(n, dtype=int)
    k = start_k
    for i in range(n):
        if not acts[k, i]:
            others = np.flatnonzero(acts[:, i])
            if len(others):
                k = int(others[0])
        tl[i] = k
    return tl


def runs_of(tl):
    """[(start_i, end_i_exclusive, value)] for a timeline."""
    out, s = [], 0
    for i in range(1, len(tl) + 1):
        if i == len(tl) or tl[i] != tl[s]:
            out.append((s, i, int(tl[s])))
            s = i
    return out


def shot_weight(acts, run):
    """How much of a run is a real shot: its length, capped by how long the panel's
    person actually TALKS in it. Silence held after a grunt does not count, or a
    0.4 s "yeah" followed by a 1 s pause would pass as a 1.4 s shot."""
    s, e, k = run
    return min(e - s, int(acts[k, s:e].sum()))


def enforce_min_shot(acts, tl, min_steps):
    """Absorb every run whose shot_weight is under min_steps: the opening run merges
    FORWARD (the layout cut is landing anyway, so land on whoever holds), any other
    short run merges BACKWARD (the current shot simply keeps going). Shortest first,
    repeated until stable."""
    tl = tl.copy()
    while True:
        rs = runs_of(tl)
        if len(rs) < 2:
            return tl
        short = [(j, r) for j, r in enumerate(rs) if shot_weight(acts, r) < min_steps]
        if not short:
            return tl
        j, (s, e, _) = min(short, key=lambda jr: shot_weight(acts, jr[1]))
        tl[s:e] = rs[j + 1][2] if j == 0 else rs[j - 1][2]


def opening_panel(acts, cur_k):
    """Panel that opens a multi-panel piece: whoever is talking at the boundary,
    else the first to speak inside the piece, else the panel we were already on."""
    now = np.flatnonzero(acts[:, 0])
    if len(now):
        return int(now[0]) if cur_k not in now else cur_k
    any_i = np.flatnonzero(acts.any(axis=0))
    if len(any_i):
        return int(np.flatnonzero(acts[:, any_i[0]])[0])
    return cur_k if cur_k is not None else 0


keys = []
layout_keys = set()
cur_x = None
pieces = [c for c in cl if 'm0' in c
          and c['final_start'] < B and c['final_start'] + c['dur'] > A]
pieces.sort(key=lambda c: c['final_start'])
for c in pieces:
    lo, hi = max(A, c['final_start']), min(B, c['final_start'] + c['dur'])
    panels = c.get('panels', [])
    persons = [PERSON[p['track']] for p in panels]
    t0 = round(max(0.0, lo - A), 3)
    if len(panels) <= 1:
        cx = FACE_CX.get(persons[0], 640) if panels else 640
        x = int(max(0, min(1280 - CW, cx - CW / 2)))
        if x != cur_x:
            keys.append([t0, x, "cut"])
            layout_keys.add(t0)
            cur_x = x
        continue
    offs = panel_offsets(len(panels))
    m_lo = c['m0'] + (lo - c['final_start'])
    m_hi = c['m0'] + (hi - c['final_start'])
    acts = np.array([active_grid(p, m_lo, m_hi) for p in persons])
    if acts.shape[1] == 0:
        continue
    cur_k = offs.index(cur_x) if cur_x in offs else None
    start_k = opening_panel(acts, cur_k)
    raw = sticky_timeline(acts, start_k)
    tl = enforce_min_shot(acts, raw, int(round(MIN_SHOT / STEP)))
    if DEBUG:
        for label, timeline in (("raw", raw), ("held", tl)):
            for s, e, k in runs_of(timeline):
                print(f"  {label:4} t={lo - A + s * STEP:6.2f}-{lo - A + e * STEP:6.2f} "
                      f"{persons[k]:8} talk={acts[k, s:e].sum() * STEP:.2f}s",
                      file=sys.stderr)
    for i, (s, e, k) in enumerate(runs_of(tl)):
        x = offs[k]
        if x == cur_x:
            continue
        t = t0 if i == 0 else round(lo - A + s * STEP, 3)
        keys.append([t, x, "cut"])
        if i == 0:
            layout_keys.add(t)
        cur_x = x

# A switch in the last 0.5 s reads as a flash at the out point, not a shot (Ep 8's
# short3: a key 0.17 s from the end = 5 frames of another person). A LAYOUT key
# there means the source itself cuts inside the tail — the crop can't fix that,
# so say so and let the editor move the out point.
tail = (B - A) - TRAIL_GUARD
for k in keys:
    if 0.0 < k[0] < TRAIL_GUARD and k[0] in layout_keys:
        print(f"WARN face_crops: source layout changes at t={k[0]} inside the first "
              f"{TRAIL_GUARD}s -> {round(k[0] * 30)} frame(s) of the previous shot flash "
              f"at the head. Move the in point to >= {A + k[0]:.2f}.", file=sys.stderr)
    if k[0] > tail and k[0] in layout_keys:
        print(f"WARN face_crops: source layout changes at t={k[0]} inside the last "
              f"{TRAIL_GUARD}s -> dropped; the old crop will sit on the new layout. "
              f"Move the out point to <= {A + k[0]:.2f} or past it.", file=sys.stderr)
keys = [k for k in keys if k[0] <= tail]
if not keys:
    keys = [[0.0, 437, "cut"]]
elif keys[0][0] > 0.0:
    keys.insert(0, [0.0, keys[0][1], "cut"])
print(json.dumps(keys))
