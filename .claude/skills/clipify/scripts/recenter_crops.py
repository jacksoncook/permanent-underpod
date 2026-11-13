#!/usr/bin/env python3
"""Re-center every face_crops segment on the detected face.

remote_face_crops.py centers the 406 px column on the PANEL, which clips a host
who leans inside their panel (Ep 23: Tyler and Chris both drifted to a panel
edge). This samples the source every 0.5 s per segment, finds the face nearest
the current column with facex (Vision), and moves x to the median face center,
clamped to the panel so the column never crosses a seam. A face the panel
itself cuts is reported as CUT so the segment can be pointed at someone else.

usage: python3 recenter_crops.py <clips.json> <workdir> [--write]
"""
import json, os, statistics, subprocess, sys, tempfile

SPEC, WORK = sys.argv[1], sys.argv[2]
WRITE = "--write" in sys.argv
W, COL = 1280, 406
FACEX = os.path.join(WORK, "facex")
FACEX_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "podcast-video-edit", "scripts", "facex.swift")
if not os.path.exists(FACEX):
    subprocess.run(["swiftc", "-O", FACEX_SRC, "-o", FACEX], check=True)
d = json.load(open(SPEC))
tmp = tempfile.mkdtemp()


def faces(src, t):
    png = os.path.join(tmp, "f.png")
    subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", src, "-frames:v", "1", "-y", png], check=True)
    out = subprocess.run([FACEX, png], capture_output=True, text=True).stdout.split("\n")
    return [tuple(map(float, l.split())) for l in out if l.strip()]


def panel(n, cx):
    n = max(1, min(n, 3))
    w = W / n
    i = min(int(cx // w), n - 1)
    return i * w, (i + 1) * w


for c in d["clips"]:
    src = c.get("source", d["source"])
    keys = c.get("face_crops")
    if not keys:
        continue
    dur = c["end"] - c["start"]
    for i, k in enumerate(keys):
        t0 = k[0]
        t1 = keys[i + 1][0] if i + 1 < len(keys) else dur
        seen, n = [], 1
        t = t0 + 0.15
        while t < t1 - 0.05:
            fs = faces(src, c["start"] + t)
            n = max(n, len(fs))
            near = [f for f in fs if abs(f[0] - (k[1] + COL / 2)) < 260]
            if near:
                seen.append(min(near, key=lambda f: abs(f[0] - (k[1] + COL / 2))))
            t += 0.5
        if not seen:
            print(f"{c['name']} key {i} t={t0}: NO FACE near x={k[1]}")
            continue
        cx = statistics.median(f[0] for f in seen)
        lo, hi = panel(n, cx)
        cut = any(f[0] - f[2] / 2 < lo + 4 or f[0] + f[2] / 2 > hi - 4 for f in seen)
        x = int(round(max(lo, min(cx - COL / 2, hi - COL))))
        flag = " CUT by panel" if cut else ""
        print(f"{c['name']} key {i} t={t0}: x {k[1]} -> {x}  (face cx {cx:.0f}, panel {lo:.0f}-{hi:.0f}){flag}")
        k[1] = x
if WRITE:
    json.dump(d, open(SPEC, "w"), indent=1)
