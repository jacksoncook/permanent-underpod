#!/usr/bin/env python3
"""Gallery recordings: find where the call grid is NOT on screen -> layout.json.

A grid recording is only a grid most of the time: a screen share (the Perp of
Fortune dashboard on Ep 17), a host dropping, or a spotlight view swaps the tile
layout for the whole span, and a tile crop over that span shows a slice of
someone's screen. Rather than modelling the other layouts, this marks every
instant where the grid is absent so gallery_shots.py can hold the full frame
("wide") there and let the share be the shot.

The grid signature is the per-tile name badge (the blue pill in each tile's
bottom-left corner), which is drawn by the call client at a fixed position only
in the grid layout. "badges" in the plan give one small [x, y, w, h] patch per
host in SOURCE pixels; a frame is "grid" iff every patch is blue (mean B - mean R
above `blue_min`, default 50).

usage: gallery_layout.py <workdir> <plan.json> [--fps 2]
  plan.json["gallery"]["badges"] = {"chris": [56, 464, 114, 48], ...}
  writes <workdir>/layout.json  {"other_spans": [[s, e], ...], "grid_pct": ..}
"""
import json, os, subprocess, sys
import numpy as np

WORK = sys.argv[1]
PLAN = json.load(open(sys.argv[2]))
FPS = float(sys.argv[sys.argv.index("--fps") + 1]) if "--fps" in sys.argv else 2.0
G = PLAN["gallery"]
BADGES = G["badges"]
BLUE_MIN = float(G.get("blue_min", 50))
SW, SH = 192, 108

r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                    "stream=width,height", "-of", "csv=p=0", PLAN["source"]],
                   capture_output=True, text=True)
W, H = map(int, r.stdout.strip().split(",")[:2])
sx, sy = SW / W, SH / H

p = subprocess.run(["ffmpeg", "-v", "error", "-i", PLAN["source"], "-an",
                    "-vf", f"fps={FPS},scale={SW}:{SH}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                   capture_output=True)
if p.returncode != 0:
    sys.exit(p.stderr.decode()[-400:])
fr = np.frombuffer(p.stdout, dtype=np.uint8).reshape(-1, SH, SW, 3).astype(np.float32)
n = len(fr)

grid = np.ones(n, dtype=bool)
for nm, (x, y, w, h) in BADGES.items():
    x0, y0 = int(x * sx), int(y * sy)
    x1, y1 = max(x0 + 1, int((x + w) * sx)), max(y0 + 1, int((y + h) * sy))
    patch = fr[:, y0:y1, x0:x1, :]
    blue = patch[..., 2].mean(axis=(1, 2)) - patch[..., 0].mean(axis=(1, 2))
    ok = blue > BLUE_MIN
    print(f"{nm:8} badge blue in {100 * ok.mean():.1f}% of frames (median B-R {np.median(blue):.0f})")
    grid &= ok

# a badge can flicker for a frame on a scene change; hold the grid state unless
# it is gone for >= 1 s
k = max(1, int(FPS * 1.0))
other = ~grid
other = np.convolve(other.astype(np.float32), np.ones(k), "same") >= k
spans, s = [], None
for i in range(n + 1):
    v = other[i] if i < n else False
    if v and s is None:
        s = i
    if not v and s is not None:
        spans.append([round(s / FPS, 2), round(i / FPS, 2)])
        s = None
tot = sum(b - a for a, b in spans)
json.dump({"other_spans": spans, "grid_pct": round(100 * grid.mean(), 2), "fps": FPS},
          open(os.path.join(WORK, "layout.json"), "w"), indent=1)
print(f"grid on screen {100 * grid.mean():.1f}% · {len(spans)} non-grid spans, {tot / 60:.1f} min:")
for a, b in spans:
    print(f"  {a:8.2f} -> {b:8.2f}  ({b - a:5.1f}s)")
print(f"wrote {WORK}/layout.json")
