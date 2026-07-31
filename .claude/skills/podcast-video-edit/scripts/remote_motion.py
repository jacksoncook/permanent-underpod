#!/usr/bin/env python3
"""Fully-remote episodes: per-host VISUAL reaction detector -> motion.json

Why this exists: the split-screen planner in remote_cutlist.py decides who is
"hot" from VAD alone, so it can only see people who make NOISE. A host who
laughs silently, nods hard, throws their hands up or pulls a face never gets on
screen — exactly the reaction shots that make a panel feel live. This measures
per-frame visual change in a box around each host's face and reports, per track,
the spans where they are visibly animated *while not speaking*.

Judging "animated" against a per-track baseline is the whole trick: webcams
differ wildly in noise, exposure and how much the person fidgets at rest, so a
single absolute threshold would fire constantly on one host and never on
another. Baseline = that host's own motion during their own SILENT frames.

usage: python3 remote_motion.py <workdir> [--pct 85] [--fps 10]
writes <workdir>/motion.json  {track: {"spans": [[m0,m1],...], "pct": .., "thr": ..}}
Spans are in MASTER time (offsets applied), so the cutlist can use them directly.

remote_cutlist.py picks this up automatically IF present and IF the plan sets
params.react_thresh -- so it is purely additive and cannot change an episode
that was cut before it existed.
"""
import json, os, subprocess, sys, wave
import numpy as np

WORK = sys.argv[1]
PCT = float(sys.argv[sys.argv.index('--pct') + 1]) if '--pct' in sys.argv else 85.0
FPS = float(sys.argv[sys.argv.index('--fps') + 1]) if '--fps' in sys.argv else 10.0

SRC = json.load(open(f'{WORK}/sources.json'))
OFF = json.load(open(f'{WORK}/offsets.json'))
PLAN_P = f'{WORK}/remote_plan.json'
FACE_CX = json.load(open(PLAN_P)).get('face_cx', {}) if os.path.exists(PLAN_P) else {}

W, H = 64, 36          # diff resolution; big enough for a head, cheap to decode
BOX_W = 520            # crop width around the face centre (source is 1280 wide)


def vad(nm):
    """same energy VAD the cutlist uses, at FPS resolution, in TRACK time"""
    w = wave.open(f'{WORK}/audio/{nm}_16k.wav', 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    hop = int(16000 / FPS)
    n = len(x) // hop
    e = np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, axis=1))
    thr = max(np.percentile(e, 10) * 6, 0.004)
    k = max(1, int(FPS * 0.45))
    return np.convolve((e > thr).astype(np.float32), np.ones(k), 'same') > 0


def motion(nm, path, cx):
    x0 = int(max(0, min(1280 - BOX_W, cx - BOX_W // 2)))
    vf = f'fps={FPS},crop={BOX_W}:720:{x0}:0,scale={W}:{H},format=gray'
    p = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-an', '-vf', vf,
                        '-f', 'rawvideo', '-'], capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f'{nm}: ffmpeg failed: {p.stderr.decode()[:300]}')
    fr = np.frombuffer(p.stdout, dtype=np.uint8).reshape(-1, H, W).astype(np.float32)
    if len(fr) < 3:
        raise RuntimeError(f'{nm}: only {len(fr)} frames decoded')
    d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
    return np.concatenate([[0.0], d])          # align to frame index


out = {}
for nm, t in SRC['tracks'].items():
    person = t['person']
    cx = FACE_CX.get(person, 640)
    m = motion(nm, t['file'], cx)
    v = vad(nm)
    n = min(len(m), len(v))
    m, v = m[:n], v[:n]

    quiet = m[~v]
    if len(quiet) < FPS * 30:                  # not enough silent footage to calibrate
        print(f'{nm}: WARNING only {len(quiet)/FPS:.0f}s of silence; using all frames')
        quiet = m
    thr = float(np.percentile(quiet, PCT))
    # only claim a REACTION where they are animated AND not talking: while
    # speaking, motion is just their mouth/head and tells us nothing new.
    hot = (m > thr) & (~v)
    # close 0.3 s holes, then drop blips under 0.4 s (a real reaction is not 2 frames)
    k = max(1, int(FPS * 0.3))
    hot = np.convolve(hot.astype(np.float32), np.ones(k), 'same') > 0
    spans, s = [], None
    for i, b in enumerate(hot):
        if b and s is None:
            s = i
        if (not b or i == len(hot) - 1) and s is not None:
            if (i - s) / FPS >= 0.4:
                spans.append([round(s / FPS + OFF[nm], 2), round(i / FPS + OFF[nm], 2)])
            s = None
    tot = sum(b - a for a, b in spans)
    out[nm] = {'spans': spans, 'pct': PCT, 'thr': thr, 'fps': FPS}
    print(f'{nm}: {len(spans)} reaction spans, {tot/60:.1f} min '
          f'({100*tot/(n/FPS):.1f}% of track), thr={thr:.3f}')

json.dump(out, open(f'{WORK}/motion.json', 'w'), indent=1)
print(f'wrote {WORK}/motion.json')
