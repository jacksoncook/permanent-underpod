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
- Layout boundaries switch EXACTLY at the boundary, no hysteresis — carrying the
  old x into a new layout lands on the seam. WITHIN a constant layout, speaker
  switches still get 1.5 s hysteresis so the crop doesn't twitch on backchannels;
  they just cut rather than glide when they do fire.

usage: python3 remote_face_crops.py <workdir> <final_start> <final_end>
prints a "face_crops" JSON array for the clipify clip entry.
"""
import json, sys, wave
import numpy as np

WORK, A, B = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
cl = json.load(open(f'{WORK}/clips.json'))
OFF = json.load(open(f'{WORK}/offsets.json'))
SRC = json.load(open(f'{WORK}/sources.json'))
PERSON = {nm: t['person'] for nm, t in SRC['tracks'].items()}
FACE_CX = json.load(open(f'{WORK}/remote_plan.json')).get(
    'face_cx', {'jackson': 620, 'chris': 600, 'tyler': 660})
CW = 406  # 9:16 column of a 720p frame

VAD = {}
for nm in PERSON:
    w = wave.open(f'{WORK}/audio/{nm}_16k.wav', 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    n = len(x) // 160
    e = np.sqrt(np.mean(x[:n * 160].reshape(n, 160) ** 2, axis=1))
    thr = max(np.percentile(e, 10) * 6, 0.004)
    VAD[nm] = np.convolve((e > thr).astype(np.float32), np.ones(41), 'same') > 0

def act(person, m):
    for nm, p in PERSON.items():
        if p != person:
            continue
        i = int((m - OFF[nm]) * 100)
        if 0 <= i < len(VAD[nm]) and VAD[nm][i]:
            return True
    return False

def panel_offsets(n_panels):
    if n_panels == 2:
        return [117, 757]            # face-centered 406 col inside each 640 panel
    return [10, 437, 864]            # inside 426/428/426 panels

keys = []
cur_x = None
pieces = [c for c in cl if 'm0' in c
          and c['final_start'] < B and c['final_start'] + c['dur'] > A]
pieces.sort(key=lambda c: c['final_start'])
for c in pieces:
    lo, hi = max(A, c['final_start']), min(B, c['final_start'] + c['dur'])
    panels = c.get('panels', [])
    persons = [PERSON[p['track']] for p in panels]
    if len(panels) <= 1:
        # solo (or insert): one x for the whole piece — nothing to track
        cx = FACE_CX.get(persons[0], 640) if panels else 640
        x = int(max(0, min(1280 - CW, cx - CW / 2)))
        if x != cur_x:
            keys.append([round(max(0.0, lo - A), 2), x, "cut"])
            cur_x = x
        continue
    offs = panel_offsets(len(panels))
    hold_x, hold_since = None, lo
    t, first = lo, True
    while t < hi:
        m = c['m0'] + (t - c['final_start'])
        x = None
        for k, p in enumerate(persons):
            if act(p, m):
                x = offs[k]
                break
        if x is None:                      # nobody talking: keep current if valid
            x = cur_x if cur_x in offs else offs[0]
        if first:
            # layout boundary: switch EXACTLY here, no hysteresis, HARD CUT
            if x != cur_x:
                keys.append([round(max(0.0, lo - A), 2), x, "cut"])
                cur_x = x
            hold_x, hold_since, first = x, t, False
        elif x != cur_x:
            if hold_x != x:
                hold_x, hold_since = x, t
            elif t - hold_since >= 1.5:
                # same layout, but a 406 col still can't hold two faces -> cut
                keys.append([round(t - A, 2), x, "cut"])
                cur_x = x
        else:
            hold_x = x
        t += 0.25
# Drop switches in the last 0.5s: a crop change with only a few frames left to
# run reads as a flash/glitch at the out point, not a shot. (Ep 8's short3 ended
# up with a key 0.17s before the end -> 5 frames of a different person.)
keys = [k for k in keys if k[0] <= (B - A) - 0.5]
if not keys:
    keys = [[0.0, 437, "cut"]]
elif keys[0][0] > 0.0:
    keys.insert(0, [0.0, keys[0][1], "cut"])
print(json.dumps(keys))
