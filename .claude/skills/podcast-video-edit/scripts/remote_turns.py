#!/usr/bin/env python3
"""Turn-based rebuild, step 1: extract conversational TURNS per speaker.
A turn = a run of one person's speech (VAD spans merged across gaps < 1.2s),
with the whisper text whose lines overlap it. Cuts will use the ENERGY
boundaries (+pads), never whisper timestamps (they tile).

Writes turns.json + turns.md (readable script for curation).
"""
import csv, json, wave
import numpy as np

SR = 16000
HOP = 160
FPS = 100
OFF = json.load(open('offsets.json'))
PERSON = {'chris': 'chris', 'jackson1': 'jackson', 'jackson2': 'jackson',
          'tyler1': 'tyler', 'tyler2': 'tyler', 'tyler3': 'tyler'}
MERGE_GAP = 1.2     # merge speech spans within a turn
MIN_TURN = 1.0      # drop shorter (pure backchannels)

def load(p):
    w = wave.open(p, 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    return x

# text lines per track (for labeling only)
lines = {nm: [] for nm in PERSON}
for nm in PERSON:
    with open(f'tx/{nm}.csv') as f:
        for r in csv.DictReader(f):
            txt = r['text'].strip()
            if not txt or txt == '[BLANK_AUDIO]':
                continue
            lines[nm].append((float(r['start']) / 1000, float(r['end']) / 1000, txt))

turns = []
for nm in PERSON:
    x = load(f'audio/{nm}_16k.wav')
    n = len(x) // HOP
    e = np.sqrt(np.mean(x[:n * HOP].reshape(n, HOP) ** 2, axis=1))
    thr = max(np.percentile(e, 10) * 6, 0.004)
    act = e > thr
    spans, s = [], None
    for i, v in enumerate(act):
        if v and s is None: s = i
        if (not v or i == n - 1) and s is not None:
            spans.append([s / FPS, (i + 1) / FPS]); s = None
    merged = []
    for sp in spans:
        if merged and sp[0] - merged[-1][1] < MERGE_GAP:
            merged[-1][1] = sp[1]
        else:
            merged.append(list(sp))
    for l0, l1 in merged:
        if l1 - l0 < MIN_TURN:
            continue
        # collect text lines overlapping [l0,l1] (whisper starts tile early, so
        # accept lines whose start is within [l0-8, l1])
        txt = " ".join(t for (s0, e0, t) in lines[nm] if l0 - 8 <= s0 <= l1)
        turns.append(dict(person=PERSON[nm], track=nm,
                          m0=round(l0 + OFF[nm], 2), m1=round(l1 + OFF[nm], 2),
                          text=txt[:400]))
turns.sort(key=lambda t: t['m0'])
json.dump(turns, open('turns.json', 'w'), indent=1)

def fmt(t):
    t = int(t); h, r = divmod(abs(t), 3600); m, s = divmod(r, 60)
    return ('-' if t < 0 else '') + (f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}")

with open('turns.md', 'w') as f:
    for i, t in enumerate(turns):
        f.write(f"[{i:4d}] {t['person']:8s} {fmt(t['m0'])}-{fmt(t['m1'])} "
                f"({t['m0']:7.1f}-{t['m1']:7.1f}, {t['m1']-t['m0']:5.1f}s): {t['text']}\n")
print(f"{len(turns)} turns -> turns.json / turns.md")
