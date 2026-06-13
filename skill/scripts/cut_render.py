#!/usr/bin/env python3
"""Phase 4 (automatic, driven by LLM-authored plan.json): build the cut list
from blocks + verified dead-air, render clips in parallel, concat, map overlay
times, and write the segment sheet.

usage: python3 cut_render.py <workdir> <plan.json>

plan.json schema (the LLM's creative decisions live here):
{
  "source": "/path/raw.mov",
  "pause_keep_default": 0.7,
  "pause_zones": [{"start": 4591, "end": 5173, "keep": 1.2}],
  "protect": [[3597, 3630]],
  "blocks": [                                # FINAL order; times are SOURCE secs
    {"id": "T2", "start": 3207.0, "end": 3215.4, "cut_silences": false},
    {"id": "CARD_TITLE", "card": "card_title.mov"},
    {"id": "A",  "start": 2404.9, "end": 2993.88, "cut_silences": true}
  ],
  "overlays": [   # src_time anchors inside a block; mapped to final time
    {"name": "lt_meet", "block": "A", "src_time": 2406.5, "dur": 6, "kind": "lt"}
  ],
  "sheet": [      # chapter rows: block start or {block, src_time}
    {"label": "Welcome + meet the hosts", "block": "A"},
    {"label": "First crypto", "block": "A", "src_time": 2645.6}
  ]
}
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

WORK = sys.argv[1]
PLAN = json.load(open(sys.argv[2]))
SRC = PLAN["source"]
CLIPDIR = os.path.join(WORK, "clips")
os.makedirs(CLIPDIR, exist_ok=True)

cuts = json.load(open(os.path.join(WORK, "verified_cuts.json")))
KEEP = PLAN.get("pause_keep_default", 0.7)
ZONES = PLAN.get("pause_zones", [])
PROTECT = PLAN.get("protect", [])

removals = []
for c in cuts:
    s, e = c["start"], c["end"]
    if any(p[0] < e and p[1] > s for p in PROTECT):
        continue
    keep = next((z["keep"] for z in ZONES if s >= z["start"] and e <= z["end"]), KEEP)
    rs, re_ = s + keep / 2, e - keep / 2
    if re_ - rs >= 1.0:
        removals.append((rs, re_))
removals.sort()

clips, idx = [], 0
for b in PLAN["blocks"]:
    if "card" in b:
        clips.append({"file": b["card"], "block": b["id"], "src_start": None, "src_end": None})
        continue
    bs, be = b["start"], b["end"]
    segs = [(bs, be)]
    if b.get("cut_silences", True):
        segs, cur = [], bs
        for rs, re_ in removals:
            rs2, re2 = max(rs, bs + 0.5), min(re_, be - 0.5)
            if re2 - rs2 < 0.8 or rs2 >= be or re2 <= bs:
                continue
            if rs2 > cur:
                segs.append((cur, rs2))
            cur = max(cur, re2)
        if cur < be:
            segs.append((cur, be))
    for a, z in segs:
        idx += 1
        clips.append({"file": f"clips/c{idx:03d}.mov", "block": b["id"],
                      "src_start": round(a, 3), "src_end": round(z, 3)})

print(f"{idx} clips to render, {sum(e-s for s,e in removals)/60:.1f} min dead air removed")

def render(c):
    if c["src_start"] is None:
        return True
    out = os.path.join(WORK, c["file"])
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                        "-ss", f"{c['src_start']:.3f}",
                        "-t", f"{c['src_end']-c['src_start']:.3f}", "-i", SRC,
                        "-vf", "fps=30,format=yuv420p",
                        "-c:v", "h264_videotoolbox", "-b:v", "10M",
                        "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "1", out],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("FAIL", c["file"], r.stderr[-200:])
    return r.returncode == 0

with ThreadPoolExecutor(max_workers=3) as ex:
    if not all(ex.map(render, clips)):
        sys.exit(1)

cum = 0.0
for c in clips:
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", os.path.join(WORK, c["file"])],
                             capture_output=True, text=True).stdout.strip())
    c["final_start"], c["dur"] = round(cum, 3), round(d, 3)
    cum += d
print(f"final runtime: {cum/60:.2f} min")

with open(os.path.join(WORK, "concat.txt"), "w") as f:
    for c in clips:
        f.write(f"file '{os.path.join(WORK, c['file'])}'\n")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat",
                "-safe", "0", "-i", os.path.join(WORK, "concat.txt"), "-c", "copy",
                os.path.join(WORK, "edited_raw.mov")], check=True)
json.dump(clips, open(os.path.join(WORK, "clips.json"), "w"), indent=1)

def s2f(block, t):
    for c in clips:
        if c["block"] != block or c["src_start"] is None:
            continue
        if c["src_start"] <= t <= c["src_end"]:
            return c["final_start"] + (t - c["src_start"])
        if t < c["src_start"]:
            return c["final_start"]
    return None

omap = []
for o in PLAN.get("overlays", []):
    ft = s2f(o["block"], o["src_time"])
    if ft is None:
        print("WARN overlay unmapped:", o["name"]); continue
    omap.append({"name": o["name"], "kind": o.get("kind", "lt"),
                 "start": round(ft, 2), "end": round(ft + o.get("dur", 6), 2)})
json.dump(omap, open(os.path.join(WORK, "overlays.json"), "w"), indent=1)

def fmt(s):
    s = int(round(s)); h, r = divmod(s, 3600); m, sec = divmod(r, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"

rows = []
for r in PLAN.get("sheet", []):
    t = (s2f(r["block"], r["src_time"]) if "src_time" in r
         else next(c["final_start"] for c in clips if c["block"] == r["block"]))
    rows.append((r["label"], t))
with open(os.path.join(WORK, "sheet.md"), "w") as f:
    f.write("| Time | Segment |\n|---|---|\n")
    for label, t in rows:
        f.write(f"| {fmt(t)} | {label} |\n")
    f.write("\n```\n" + "\n".join(f"{fmt(t)} {l}" for l, t in rows) + "\n```\n")
print("wrote clips.json, overlays.json, sheet.md, edited_raw.mov")
