#!/usr/bin/env python3
"""Boundary gate for splice points: every cut must sit in a MEASURED all-silent
union gap across every track, never on a whisper timestamp (whisper times tile
across real pauses and land cuts mid-word).

VAD = 10 ms RMS envelope per track, threshold max(p10*6, 0.004), 41-frame
dilation (~±0.2 s), evaluated in master time via offsets.json. A boundary is
safe only when NO track is active there.

usage:
  check_bounds.py <work> --plan <remote_plan.json>   # gate every block m0/m1; exit 1 on any failure
  check_bounds.py <work> <t> [t ...]                 # check individual boundaries
  check_bounds.py <work> --spans <m0> <m1> [track ...]   # per-track speech spans + all-silent gaps in a window

Expects <work>/audio/<track>_16k.wav per track in <work>/offsets.json.
Works for single-cam plans too (one track, offset 0).
"""
import json, os, sys, wave
import numpy as np

WORK = sys.argv[1]
OFF = json.load(open(os.path.join(WORK, "offsets.json")))
SR, HOP, FPS_V = 16000, 160, 100

VAD = {}
for nm in OFF:
    w = wave.open(os.path.join(WORK, "audio", f"{nm}_16k.wav"), 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    n = len(x) // HOP
    e = np.sqrt(np.mean(x[:n * HOP].reshape(n, HOP) ** 2, axis=1))
    thr = max(np.percentile(e, 10) * 6, 0.004)
    VAD[nm] = np.convolve((e > thr).astype(np.float32), np.ones(41), 'same') > 0


def union_act(t):
    for nm in OFF:
        i = int((t - OFF[nm]) * FPS_V)
        if 0 <= i < len(VAD[nm]) and VAD[nm][i]:
            return True
    return False


def check(m):
    grid = np.arange(m - 2.5, m + 2.5, 0.01)
    silent = np.array([not union_act(t) for t in grid])
    runs, s = [], None
    for i, v in enumerate(silent):
        if v and s is None:
            s = i
        if (not v or i == len(silent) - 1) and s is not None:
            if i - s >= 20:
                runs.append((grid[s], grid[i]))
            s = None
    inside = any(a <= m <= b for a, b in runs)
    near = min(runs, key=lambda r: abs((r[0] + r[1]) / 2 - m)) if runs else None
    return inside, near


if len(sys.argv) > 2 and sys.argv[2] == "--spans":
    m0, m1 = float(sys.argv[3]), float(sys.argv[4])
    want = sys.argv[5:] or list(OFF)
    for nm in want:
        print(f"\n{nm.upper()}:")
        i0, i1 = int((m0 - OFF[nm]) * FPS_V), int((m1 - OFF[nm]) * FPS_V)
        v = VAD[nm][max(0, i0):i1]
        s = None
        for i, on in enumerate(v):
            if on and s is None:
                s = i
            if (not on or i == len(v) - 1) and s is not None:
                a, z = m0 + s / FPS_V, m0 + (i + 1) / FPS_V
                if z - a > 0.25:
                    print(f"   {a:8.2f} -> {z:8.2f}  ({z-a:5.2f}s)")
                s = None
    grid = np.arange(m0, m1, 0.02)
    act = np.zeros(len(grid), bool)
    for nm in OFF:
        idx = ((grid - OFF[nm]) * FPS_V).astype(int)
        ok = (idx >= 0) & (idx < len(VAD[nm]))
        act[ok] |= VAD[nm][idx[ok]]
    print("\nALL-SILENT GAPS (safe cut points):")
    s = None
    for i, a in enumerate(act):
        if not a and s is None:
            s = i
        if (a or i == len(act) - 1) and s is not None:
            if grid[i] - grid[s] >= 0.30:
                mid = (grid[s] + grid[i]) / 2
                print(f"   {grid[s]:8.2f} -> {grid[i]:8.2f}  ({grid[i]-grid[s]:5.2f}s)   mid={mid:.2f}")
            s = None
    sys.exit(0)

if len(sys.argv) > 2 and sys.argv[2] == "--plan":
    plan = json.load(open(sys.argv[3]))
    bounds = []
    for b in plan.get("blocks", []):
        if "m0" not in b:
            continue
        bounds += [(b["id"] + ".m0", b["m0"]), (b["id"] + ".m1", b["m1"])]
    bad = 0
    for label, m in bounds:
        inside, near = check(m)
        if inside:
            print(f"{m:9.2f}  OK-in-gap   {label}")
        else:
            bad += 1
            hint = (f"snap->{(near[0]+near[1])/2:.2f} (gap {near[0]:.2f}-{near[1]:.2f})"
                    if near else "NO GAP +-2.5s  <<<< DANGER")
            print(f"{m:9.2f}  ON SPEECH   {label}  {hint}")
    print(f"\n{len(bounds)-bad}/{len(bounds)} boundaries in verified silence")
    sys.exit(1 if bad else 0)

bad = 0
for tok in sys.argv[2:]:
    m = float(tok)
    inside, near = check(m)
    if inside:
        print(f"{m:9.2f}  OK-in-gap")
    else:
        bad += 1
        print(f"{m:9.2f}  " + (f"snap->{(near[0]+near[1])/2:.2f} (gap {near[0]:.2f}-{near[1]:.2f})"
                               if near else "NO GAP +-2.5s  <<<< DANGER"))
sys.exit(1 if bad else 0)
