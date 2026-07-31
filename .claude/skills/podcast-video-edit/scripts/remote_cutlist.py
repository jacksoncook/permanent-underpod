#!/usr/bin/env python3
"""Fully-remote episodes, phase 3: turn the LLM-authored remote_plan.json into
a multicam cutlist. Dead-air removal on the union VAD, boundary snapping to
all-silent gaps, active-speaker camera assignment with split-screen composites
(duo halves / trio thirds) replacing punch-ins, churn-killer shot merging, and
per-clip audio-mix specs (all covering mics, idle attenuation, equalized).

usage: <venv>/bin/python remote_cutlist.py <workdir> <remote_plan.json>

remote_plan.json (LLM judgment lives here):
{
  "blocks": [                       # FINAL order; m0/m1 are REFERENCE-clock secs
    {"id": "COLD1", "m0": 231.5, "m1": 250.0, "cam": "tyler"},   # fixed solo cam
    {"id": "CARD_TITLE", "card": "card_title.mov"},
    {"id": "AI", "insert": "/abs/final_ai.mp4"},                 # conformed insert
    {"id": "MAIN", "m0": 59.3, "m1": 258.8},                     # auto multicam
    {"id": "SOLO", "m0": -134.2, "m1": -107.5, "cam": "jackson",
     "mics": ["jackson"]},           # mics: person whitelist — OMIT other mics
    {"id": "DUOZONE", "m0": 59.5, "m1": 93.5,                    # entirely (kills parallel-
     "mics": ["chris", "tyler"], "cams": ["chris", "tyler"]},    # conversation bleed)
    {"id": "X", "m0": 300, "m1": 800,
     "mute": [["tyler", 324.4, 330.6]]}   # mute: force-silence one person's mic
  ],                                      # for a master-time span (stray meta lines)
  "protect": [[1388, 1400]],        # never dead-air-cut here (claps etc.)
  "face_cx": {"jackson": 620, "chris": 600, "tyler": 660},   # panel crop centers
  "panel_order": ["jackson", "chris", "tyler"],
  "params": {"idle_gain": 0.12, "group_thresh": 0.48, "min_shot": 3.5,
             "gain_target": 0.028}   # 0.028 ~ -31 dBFS speech RMS per track:
}                                    # 3 mics sum + crest => peaks ~-8 dBFS.
                                     # 0.055 CLIPPED on Ep 5 — don't raise it.
"""
import json, sys, wave
import numpy as np

WORK, PLAN_PATH = sys.argv[1], sys.argv[2]
PLAN = json.load(open(PLAN_PATH))
OFF = json.load(open(f"{WORK}/offsets.json"))
SRC = json.load(open(f"{WORK}/sources.json"))
P = PLAN.get('params', {})
IDLE_GAIN = P.get('idle_gain', 0.12)
GROUP_TH = P.get('group_thresh', 0.48)
MIN_SHOT = P.get('min_shot', 3.5)
GAIN_TGT = P.get('gain_target', 0.028)
PORDER = PLAN.get('panel_order', ['jackson', 'chris', 'tyler'])
FACE_CX = PLAN.get('face_cx', {})
PROTECT = [tuple(p) for p in PLAN.get('protect', [])]
SWITCH_HOLD = 2.0

SR, HOP, FPS_V = 16000, 160, 100
FILES = {nm: t['file'] for nm, t in SRC['tracks'].items()}
PERSON = {nm: t['person'] for nm, t in SRC['tracks'].items()}

DUR, VAD, GAIN = {}, {}, {}
for nm in FILES:
    w = wave.open(f"{WORK}/audio/{nm}_16k.wav", 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    DUR[nm] = len(x) / SR
    n = len(x) // HOP
    e = np.sqrt(np.mean(x[:n * HOP].reshape(n, HOP) ** 2, axis=1))
    thr = max(np.percentile(e, 10) * 6, 0.004)
    VAD[nm] = (np.convolve((e > thr).astype(np.float32), np.ones(41), 'same') > 0)
    sp = e[VAD[nm][:len(e)]]
    rms = float(np.median(sp)) if len(sp) else 0.02
    # Floor must stay well below any sane GAIN_TGT/rms or the clamp BINDS and
    # silently destroys the per-speaker equalization this function exists for
    # (Ep 8 at gain_target 0.006: chris 0.36 and tyler 0.39 both pinned to the
    # old 0.5 floor, leaving them ~1-3 dB hot relative to jackson).
    GAIN[nm] = float(np.clip(GAIN_TGT / rms, 0.05, 5.0))
    print(f"{nm}: dur={DUR[nm]:.1f} speech_rms={rms:.4f} gain=x{GAIN[nm]:.2f}")

def covers(nm, m0, m1, slack=0.05):
    return OFF[nm] - slack <= m0 and m1 <= OFF[nm] + DUR[nm] + slack

def act_at(nm, m):
    i = int((m - OFF[nm]) * FPS_V)
    return bool(VAD[nm][i]) if 0 <= i < len(VAD[nm]) else False

def union_act(m):
    return any(act_at(nm, m) for nm in FILES)

def person_act(p, m):
    return any(act_at(nm, m) for nm in FILES if PERSON[nm] == p)

def person_track(p, m0, m1):
    for nm in FILES:
        if PERSON[nm] == p and covers(nm, m0, m1):
            return nm
    return None

def snap(m, radius=2.0):
    grid = np.arange(m - radius, m + radius, 0.01)
    silent = np.array([not union_act(t) for t in grid])
    runs, s = [], None
    for i, v in enumerate(silent):
        if v and s is None: s = i
        if (not v or i == len(silent) - 1) and s is not None:
            e = i if not v else i + 1
            if e - s >= 20:
                runs.append((s, e))
            s = None
    if not runs:
        return m
    best = min(runs, key=lambda r: abs(grid[(r[0] + r[1]) // 2] - m))
    return float(grid[(best[0] + best[1]) // 2])

def dominant(m, win=2.4):
    return {p: float(np.mean([person_act(p, t)
                              for t in np.arange(m - win / 2, m + win / 2, 0.05)]))
            for p in PORDER}

def shot_key(sh):
    return sh['type'] + ':' + ','.join(sh.get('panels', [sh.get('cam', '')]))

def plan_block(b):
    m0, m1 = snap(b['m0']), snap(b['m1'])
    grid = np.arange(m0, m1, 0.01)
    silent = np.array([not union_act(t) for t in grid])
    keeps, cur, s = [], m0, None
    for i, v in enumerate(silent):
        t = grid[i]
        if v and s is None: s = t
        if (not v or i == len(silent) - 1) and s is not None:
            if t - s >= 2.0 and not any(p0 < t and p1 > s for p0, p1 in PROTECT):
                rs, re_ = s + 0.35, t - 0.35
                if re_ - rs >= 1.0:
                    if rs > cur: keeps.append((cur, rs))
                    cur = re_
            s = None
    if cur < m1: keeps.append((cur, m1))

    def desired(t, a, z):
        sc = dominant(t)
        allowed = b.get('cams', PORDER)
        muted_now = {mp for mp, mm0, mm1 in (b.get('mute') or [])
                     if mm0 - 1.0 < t < mm1 + 1.0}   # never show a muted mouth
        avail = [p for p in PORDER if p in allowed and p not in muted_now
                 and person_track(p, max(a, t - 1), min(z, t + 1))]
        hot = [p for p in avail if sc[p] >= GROUP_TH]
        if len(hot) >= 2:
            return dict(type='trio' if len(hot) >= 3 else 'duo',
                        panels=[person_track(p, t - 1, t + 1) for p in PORDER if p in hot])
        p = max(hot or avail, key=lambda q: sc[q]) if (hot or avail) else PORDER[0]
        return dict(type='solo', cam=person_track(p, t - 1, t + 1) or
                    next(iter(FILES)))

    pieces = []
    fixed = b.get('cam')
    for (a, z) in keeps:
        if fixed:
            tr = person_track(fixed, a, z)
            if tr is None:
                raise ValueError(f"{b['id']}: cam {fixed} not covering {a:.1f}-{z:.1f}")
            pieces.append([a, z, dict(type='solo', cam=tr)])
            continue
        ts = np.arange(a + 0.25, z, 0.5)
        if not len(ts):
            pieces.append([a, z, desired((a + z) / 2, a, z)]); continue
        wants = [desired(t, a, z) for t in ts]
        cur_s, start, cand, cand_since = wants[0], a, None, None
        for t, wnt in zip(ts, wants):
            if shot_key(wnt) != shot_key(cur_s):
                if cand is None or shot_key(cand) != shot_key(wnt):
                    cand, cand_since = wnt, t
                hold = SWITCH_HOLD if wnt['type'] == 'solo' else 1.2
                if t - cand_since >= hold - 0.001 and t - start >= MIN_SHOT:
                    cut = cand_since - 0.25
                    if cut > start:
                        pieces.append([start, cut, cur_s])
                        cur_s, start = wnt, cut
                    cand = None
            else:
                cand = None
        pieces.append([start, z, cur_s])
    # coverage repair
    out = []
    for a, z, sh in pieces:
        if sh['type'] == 'solo':
            if not covers(sh['cam'], a, z):
                alt = person_track(PERSON[sh['cam']], a, z)
                sh = dict(type='solo', cam=alt or next(nm for nm in FILES if covers(nm, a, z)))
        else:
            panels = [tr for tr in sh['panels'] if tr and covers(tr, a, z)]
            sh = (dict(type='trio' if len(panels) == 3 else 'duo', panels=panels)
                  if len(panels) >= 2 else
                  dict(type='solo', cam=panels[0] if panels else
                       next(nm for nm in FILES if covers(nm, a, z))))
        out.append((a, z, sh))
    # merge identical neighbors, absorb <3.5s churn, drop stranded slivers
    merged = []
    for a, z, sh in out:
        if merged and merged[-1][1] == a and shot_key(merged[-1][2]) == shot_key(sh):
            merged[-1] = (merged[-1][0], z, sh)
        else:
            merged.append((a, z, sh))
    changed = True
    while changed:
        changed = False
        for i, (a, z, sh) in enumerate(merged):
            if z - a >= 3.5:
                continue
            prev = merged[i - 1] if i > 0 and abs(merged[i - 1][1] - a) < 0.02 else None
            nxt = (merged[i + 1] if i + 1 < len(merged)
                   and abs(merged[i + 1][0] - z) < 0.02 else None)
            if prev is None and nxt is None:
                continue
            if nxt is None or (prev is not None and prev[1] - prev[0] >= nxt[1] - nxt[0]):
                merged[i - 1] = (prev[0], z, prev[2]); del merged[i]
            else:
                merged[i + 1] = (a, nxt[1], nxt[2]); del merged[i]
            changed = True
            break
    final = []
    for a, z, sh in merged:
        if final and abs(final[-1][1] - a) < 0.02 and shot_key(final[-1][2]) == shot_key(sh):
            final[-1] = (final[-1][0], z, sh)
        else:
            final.append((a, z, sh))
    return [(a, z, sh) for a, z, sh in final if z - a >= 1.5]

def audio_spec(a, z, mics=None, mute=None):
    spec = []
    for nm in FILES:
        if mics is not None and PERSON[nm] not in mics:
            continue
        la, lz = max(a, OFF[nm]), min(z, OFF[nm] + DUR[nm])
        if lz - la < 0.2:
            continue
        v = VAD[nm][int((la - OFF[nm]) * FPS_V):int((lz - OFF[nm]) * FPS_V)]
        spans, s = [], None
        for i, on in enumerate(v):
            if on and s is None: s = i
            if (not on or i == len(v) - 1) and s is not None:
                spans.append([s / FPS_V, (i + 1) / FPS_V]); s = None
        merged = []
        for sp in spans:
            sp = [max(0, sp[0] - 0.5), min(lz - la, sp[1] + 0.5)]
            if merged and sp[0] - merged[-1][1] < 1.5:
                merged[-1][1] = sp[1]
            else:
                merged.append(sp)
        for mp, mm0, mm1 in (mute or []):   # forced-mute spans (master-time)
            if PERSON[nm] != mp:
                continue
            u0, u1 = mm0 - la, mm1 - la
            nx = []
            for s0, s1 in merged:
                if s1 <= u0 or s0 >= u1:
                    nx.append([s0, s1]); continue
                if s0 < u0: nx.append([s0, u0])
                if s1 > u1: nx.append([u1, s1])
            merged = nx
        spec.append(dict(track=nm, file=FILES[nm], src_start=round(la - OFF[nm], 3),
                         pad_head=round(la - a, 3), dur=round(lz - la, 3),
                         gain=round(GAIN[nm], 2),
                         active=[[round(x, 2), round(y, 2)] for x, y in merged[:70]]))
    return spec

cutlist = []
for b in PLAN['blocks']:
    if 'card' in b or 'insert' in b:
        cutlist.append({k: b[k] for k in ('id', 'card', 'insert') if k in b} |
                       {'block': b['id']})
        continue
    for (a, z, sh) in plan_block(b):
        c = dict(block=b['id'], m0=round(a, 3), m1=round(z, 3), shot=sh['type'],
                 audio=audio_spec(a, z, b.get('mics'), b.get('mute')))
        panels = sh.get('panels', [sh.get('cam')])
        c['panels'] = [dict(track=tr, file=FILES[tr], src_start=round(a - OFF[tr], 3),
                            cx=FACE_CX.get(PERSON[tr], 640)) for tr in panels]
        cutlist.append(c)

from collections import Counter
sh = [c for c in cutlist if 'shot' in c]
tot = sum(c['m1'] - c['m0'] for c in sh)
print(f"{len(sh)} pieces, {tot/60:.1f} min live content,",
      dict(Counter(c['shot'] for c in sh)))
json.dump(cutlist, open(f"{WORK}/cutlist.json", 'w'), indent=1)
print("wrote cutlist.json")
