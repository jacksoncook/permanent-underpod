#!/usr/bin/env python3
"""Gallery recordings (one video of a video-call grid, one mixed audio track):
attribute every speech span to a host from the voice alone -> speech.json.

Why: a Meet/Zoom-style grid recording has no per-host audio track and no
active-speaker border, so the speaker-following edit (gallery_shots.py) needs a
diarization. Each host is ENROLLED from a few seconds of known speech (the intro
roll call is ideal), then every VAD window is scored by cosine similarity of its
ECAPA speaker embedding against the enrollment centroids. Two self-training
rounds re-enroll from the most confident long windows, which fixes the usual
problem that the roll-call lines are short and read in a "radio voice".

usage: gallery_diarize.py <workdir> <enroll.json> [--win 1.5] [--hop 0.5]
  enroll.json: {"jackson": [[6.1, 9.2]], "tyler": [[11.9, 21.4]], "chris": [[22.9, 25.4]]}
  reads  <workdir>/audio16k.wav (from analyze.sh)
  writes <workdir>/speech.json  {"persons": [...], "spans": {person: [[s, e], ...]},
                                 "windows": [[s, e, person, margin], ...]}

Requires torch + speechbrain (model speechbrain/spkrec-ecapa-voxceleb, cached by
huggingface). Run with the diarization venv, not the Pillow venv.
"""
import json, os, sys, wave
import numpy as np
import torch
from speechbrain.inference.speaker import EncoderClassifier

WORK = sys.argv[1]
ENROLL = json.load(open(sys.argv[2]))
WIN = float(sys.argv[sys.argv.index('--win') + 1]) if '--win' in sys.argv else 1.5
HOP = float(sys.argv[sys.argv.index('--hop') + 1]) if '--hop' in sys.argv else 0.5
SR = 16000

w = wave.open(os.path.join(WORK, 'audio16k.wav'), 'rb')
assert w.getframerate() == SR and w.getnchannels() == 1
x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
w.close()
dur = len(x) / SR

HOP_E = 160
n = len(x) // HOP_E
e = np.sqrt(np.mean(x[:n * HOP_E].reshape(n, HOP_E) ** 2, axis=1))
thr = max(np.percentile(e, 10) * 6, 0.004)
vad = np.convolve((e > thr).astype(np.float32), np.ones(41), 'same') > 0

spans, s = [], None
for i, b in enumerate(vad):
    if b and s is None:
        s = i
    if (not b or i == len(vad) - 1) and s is not None:
        spans.append([s / 100.0, i / 100.0]); s = None
merged = []
for a, b in spans:
    if merged and a - merged[-1][1] < 0.3:
        merged[-1][1] = b
    else:
        merged.append([a, b])
spans = [sp for sp in merged if sp[1] - sp[0] >= 0.3]
print(f'{len(spans)} speech spans, {sum(b - a for a, b in spans) / 60:.1f} min of speech, vad thr {thr:.4f}')

device = 'mps' if torch.backends.mps.is_available() else 'cpu'
enc = EncoderClassifier.from_hparams(source='speechbrain/spkrec-ecapa-voxceleb',
                                     savedir=os.path.join(WORK, '.ecapa'),
                                     run_opts={'device': device})


def embed_batch(segs):
    out = []
    B = 64
    for i in range(0, len(segs), B):
        chunk = segs[i:i + B]
        L = max(len(c) for c in chunk)
        batch = np.zeros((len(chunk), L), dtype=np.float32)
        lens = np.zeros(len(chunk), dtype=np.float32)
        for j, c in enumerate(chunk):
            batch[j, :len(c)] = c
            lens[j] = len(c) / L
        with torch.no_grad():
            emb = enc.encode_batch(torch.from_numpy(batch).to(device),
                                   torch.from_numpy(lens).to(device))
        emb = emb.squeeze(1).cpu().numpy()
        out.append(emb / np.linalg.norm(emb, axis=1, keepdims=True))
    return np.concatenate(out)


windows = []
for a, b in spans:
    t = a
    while True:
        t2 = min(b, t + WIN)
        if t2 - t >= 0.6 or t == a:
            windows.append([t, max(t2, min(b, t + 0.6))])
        if t2 >= b:
            break
        t += HOP
wsegs = [x[int(a * SR):int(b * SR)] for a, b in windows]
print(f'{len(windows)} windows -> embedding on {device} ...')
W_EMB = embed_batch(wsegs)

persons = list(ENROLL)


def centroids(labels_segs):
    cs = []
    for p in persons:
        segs = [x[int(a * SR):int(b * SR)] for a, b in labels_segs[p]]
        emb = embed_batch(segs)
        c = emb.mean(axis=0)
        cs.append(c / np.linalg.norm(c))
    return np.stack(cs)


def classify(C):
    sims = W_EMB @ C.T
    order = np.argsort(-sims, axis=1)
    best = order[:, 0]
    margin = sims[np.arange(len(sims)), order[:, 0]] - sims[np.arange(len(sims)), order[:, 1]]
    return best, margin, sims


C = centroids(ENROLL)
best, margin, sims = classify(C)
for rnd in range(2):
    relabel = {p: [] for p in persons}
    for k, p in enumerate(persons):
        idx = np.flatnonzero(best == k)
        if len(idx) == 0:
            relabel[p] = ENROLL[p]; continue
        conf = idx[np.argsort(-margin[idx])][:max(20, len(idx) // 3)]
        relabel[p] = [windows[i] for i in conf]
    C = centroids(relabel)
    best, margin, sims = classify(C)
    counts = {p: int((best == k).sum()) for k, p in enumerate(persons)}
    print(f'round {rnd + 1}: {counts}, median margin {np.median(margin):.3f}')

wins_out = []
for (a, b), k, m in zip(windows, best, margin):
    wins_out.append([round(a, 2), round(b, 2), persons[int(k)], round(float(m), 3)])

# per-span attribution on a 10 ms grid: each grid cell takes the vote of the windows
# covering it, weighted by margin, so a 1.5 s window straddling a speaker change
# is outvoted by its neighbours instead of smearing the first speaker over the second
grid = np.zeros((len(persons), n), dtype=np.float32)
for (a, b), k, m in zip(windows, best, margin):
    grid[int(k), int(a * 100):int(b * 100)] += max(0.05, float(m))
lab = np.where(vad, grid.argmax(axis=0), -1)
lab[(grid.max(axis=0) == 0) & vad] = -1
out_spans = {p: [] for p in persons}
s = None
for i in range(n + 1):
    v = lab[i] if i < n else -2
    if s is None:
        if v >= 0:
            s = i
    elif v != lab[s]:
        out_spans[persons[lab[s]]].append([round(s / 100, 2), round(i / 100, 2)])
        s = i if v >= 0 else None
for p in persons:
    merged = []
    for a, b in out_spans[p]:
        if merged and a - merged[-1][1] < 0.25:
            merged[-1][1] = b
        else:
            merged.append([a, b])
    out_spans[p] = [sp for sp in merged if sp[1] - sp[0] >= 0.25]
    tot = sum(b - a for a, b in out_spans[p])
    print(f'{p:8} {len(out_spans[p]):4d} spans  {tot / 60:5.1f} min  ({100 * tot / dur:.0f}% of runtime)')

json.dump({'persons': persons, 'duration': round(dur, 2), 'spans': out_spans, 'windows': wins_out},
          open(os.path.join(WORK, 'speech.json'), 'w'))
print(f"wrote {WORK}/speech.json")
