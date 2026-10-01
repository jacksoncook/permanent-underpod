#!/usr/bin/env python3
"""Gallery recordings: build the speaker-following shot schedule -> shots.json.

The source is ONE video of a video-call grid (every host in a fixed tile) with one
mixed audio track. The edit simulates a multicam: a solo shot is the active
speaker's tile cropped and scaled to full frame, a reaction/crosstalk beat is the
whole grid ("wide"), and long monologues alternate between the tile and a tighter
face crop ("<person>_tight") so a 40 s answer is not one static frame.

EVERY shot change is a HARD CUT. The tiles are separated by black gutters, so any
eased move between them would glide across the seam (the same boomerang failure
the vertical face crops had on Ep 8). The cut lands on the new speaker's onset,
with lookahead: a switch only fires if that speaker then holds the shot for at
least `min_shot` s of actual talk, and the current speaker is sticky while
talking, so a "yeah" or a laugh on another tile never flips the shot.

usage: gallery_shots.py <workdir> <plan.json>
  plan.json["gallery"] = {
    "tiles": {"chris": [x, y, w, h], ...},        # source-pixel tile rects (even w/h)
    "tight": {"chris": [x, y, w, h], ...},        # optional tighter 16:9 crops per person
    "min_shot": 2.0,          # s of talk a new speaker must hold to win the cut
    "wide_overlap": 1.0,      # s of >=2 simultaneous speakers that cuts to the grid
    "wide_min": 2.5,          # minimum wide shot length
    "punch_after": 24,        # s on one solo tile before alternating to its tight crop
    "punch_dur": 9            # s the tight crop holds before cutting back
  }
  reads  <workdir>/speech.json (gallery_diarize.py)
  writes <workdir>/shots.json  [{"start", "end", "shot"}, ...] covering the whole source
"""
import json, os, sys
import numpy as np

WORK = sys.argv[1]
PLAN = json.load(open(sys.argv[2]))
G = PLAN["gallery"]
SP = json.load(open(os.path.join(WORK, "speech.json")))
persons = [p for p in G["tiles"] if p in SP["spans"]]
STEP = 0.01
MIN_SHOT = int(round(float(G.get("min_shot", 2.0)) / STEP))
WIDE_OVL = int(round(float(G.get("wide_overlap", 1.0)) / STEP))
WIDE_MIN = int(round(float(G.get("wide_min", 2.5)) / STEP))
PUNCH_AFTER = int(round(float(G.get("punch_after", 24)) / STEP))
PUNCH_DUR = int(round(float(G.get("punch_dur", 9)) / STEP))
DUR = float(SP["duration"])
N = int(DUR / STEP) + 1
WIDE = len(persons)

acts = np.zeros((len(persons), N), dtype=bool)
for k, p in enumerate(persons):
    for a, b in SP["spans"][p]:
        acts[k, int(a / STEP):int(b / STEP)] = True


def dilate(v, steps):
    return np.convolve(v.astype(np.float32), np.ones(2 * steps + 1), "same") > 0


def runs_of(tl):
    out, s = [], 0
    for i in range(1, len(tl) + 1):
        if i == len(tl) or tl[i] != tl[s]:
            out.append((s, i, int(tl[s])))
            s = i
    return out


def sticky(acts):
    first = np.flatnonzero(acts.any(axis=0))
    k = int(np.flatnonzero(acts[:, first[0]])[0]) if len(first) else 0
    tl = np.empty(acts.shape[1], dtype=int)
    for i in range(acts.shape[1]):
        if not acts[k, i]:
            others = np.flatnonzero(acts[:, i])
            if len(others):
                k = int(others[0])
        tl[i] = k
    return tl


def weight(run):
    s, e, k = run
    if k == WIDE:
        return e - s
    return min(e - s, int(acts[k, s:e].sum()))


def enforce_min(tl, min_steps):
    tl = tl.copy()
    while True:
        rs = runs_of(tl)
        if len(rs) < 2:
            return tl
        short = [(j, r) for j, r in enumerate(rs)
                 if weight(r) < (WIDE_MIN if r[2] == WIDE else min_steps)]
        if not short:
            return tl
        j, (s, e, _) = min(short, key=lambda jr: weight(jr[1]))
        tl[s:e] = rs[j + 1][2] if j == 0 else rs[j - 1][2]


tl = sticky(acts)

# crosstalk / shared laughs -> the grid. A single mixed track gives every instant
# to exactly one voice, so simultaneous speech is invisible; what IS visible is
# churn: several speaker changes inside a few seconds. `wide_overlap` is the
# window (s) in which >= 3 changes of voice mark a group beat.
onsets = []
for k in range(len(persons)):
    a = acts[k]
    onsets.extend(np.flatnonzero(a[1:] & ~a[:-1]) + 1)
onsets = np.sort(np.array(onsets))
WIN = max(WIDE_OVL, int(round(4.0 / STEP)))
for j in range(len(onsets) - 2):
    if onsets[j + 2] - onsets[j] <= WIN:
        who = {int(np.flatnonzero(acts[:, i])[0]) for i in onsets[j:j + 3] if acts[:, i].any()}
        if len(who) >= 2:
            lo, hi = max(0, onsets[j] - 30), min(N, onsets[j + 2] + WIDE_MIN)
            tl[lo:hi] = WIDE

tl = enforce_min(tl, MIN_SHOT)

# where the grid is not on screen (screen share, spotlight) the tiles do not
# exist: hold the full frame and let the share be the shot (gallery_layout.py)
lay_p = os.path.join(WORK, "layout.json")
if os.path.exists(lay_p):
    for a, b in json.load(open(lay_p))["other_spans"]:
        tl[max(0, int(a / STEP) - 25):min(N, int(b / STEP) + 25)] = WIDE
elif G.get("badges"):
    sys.exit("gallery.badges is set but layout.json is missing: run gallery_layout.py first")

# forcing wide can leave a sliver of the old shot on either side; absorb anything
# under 0.5 s into the longer neighbour
SLIVER = int(round(0.5 / STEP))
while True:
    rs = runs_of(tl)
    short = [j for j, r in enumerate(rs) if r[1] - r[0] < SLIVER]
    if len(rs) < 2 or not short:
        break
    j = short[0]; s, e, _ = rs[j]
    tl[s:e] = rs[j + 1][2] if j == 0 else rs[j - 1][2]

# punch-ins: alternate a long solo run between the tile and its tight crop
names = persons + ["wide"]
shots = []
for s, e, k in runs_of(tl):
    nm = names[k]
    if k == WIDE or nm not in G.get("tight", {}) or e - s < PUNCH_AFTER + PUNCH_DUR + MIN_SHOT:
        shots.append([s, e, nm]); continue
    i, tight = s, False
    while i < e:
        L = PUNCH_DUR if tight else PUNCH_AFTER
        j = min(e, i + L)
        if e - j < MIN_SHOT:
            j = e
        shots.append([i, j, nm + "_tight" if tight else nm])
        i, tight = j, not tight

out = [{"start": round(s * STEP, 2), "end": round(e * STEP, 2), "shot": nm} for s, e, nm in shots]
out[-1]["end"] = round(DUR, 2)
json.dump(out, open(os.path.join(WORK, "shots.json"), "w"), indent=0)

tot = {nm: 0.0 for nm in names + [p + "_tight" for p in persons]}
for o in out:
    tot[o["shot"]] = tot.get(o["shot"], 0.0) + o["end"] - o["start"]
print(f"{len(out)} shots, median {np.median([o['end']-o['start'] for o in out]):.1f} s, "
      f"min {min(o['end']-o['start'] for o in out):.2f} s")
for nm, t in sorted(tot.items(), key=lambda x: -x[1]):
    if t:
        print(f"  {nm:16} {t/60:5.1f} min  {100*t/DUR:4.1f}%")
print(f"wrote {WORK}/shots.json")
