#!/usr/bin/env python3
"""Fully-remote episodes: generate a face-crop schedule for a clipify vertical
short. Tracks the ACTIVE speaker: solo shots crop around that person's face;
split-screen shots crop the speaking panel.

Crop-switch rules (the subtle part):
- At a SHOT-LAYOUT boundary (solo->duo etc.) the crop switches IMMEDIATELY and
  exactly at the boundary — carrying the old x into a new layout shows the seam
  between panels (half of two people, i.e. nobody on screen).
- WITHIN a constant layout, speaker switches use 1.5s hysteresis so the crop
  doesn't twitch on backchannels.

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
            keys.append([round(max(0.0, lo - A), 2), x])
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
            # layout boundary: switch EXACTLY here, no hysteresis
            if x != cur_x:
                keys.append([round(max(0.0, lo - A), 2), x])
                cur_x = x
            hold_x, hold_since, first = x, t, False
        elif x != cur_x:
            if hold_x != x:
                hold_x, hold_since = x, t
            elif t - hold_since >= 1.5:
                keys.append([round(t - A, 2), x])
                cur_x = x
        else:
            hold_x = x
        t += 0.25
if not keys:
    keys = [[0.0, 437]]
elif keys[0][0] > 0.0:
    keys.insert(0, [0.0, keys[0][1]])
print(json.dumps(keys))
