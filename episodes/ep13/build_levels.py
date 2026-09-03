#!/usr/bin/env python3
"""Ep 13: the DeepMind "Levels of AGI" table (media/ep13/aiLevels.png) as a
document-over-video overlay — dimmed frame, the paper's table at 0.9x, a gold
highlight that moves to the cell the hosts are talking about. One alpha .mov per
window, scheduled in render.json `anim` (with hide_logo so the bug stays clear).

usage: media/ep12/work/.venv/bin/python episodes/ep13/build_levels.py media/ep13/work media/ep13/aiLevels.png
prints the render.json anim entries.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

WORK, SRC = sys.argv[1], sys.argv[2]
W, H, FPS = 1280, 720, 30
ACC = (255, 210, 74)
SCALE = 0.9
CROP_TOP = 200                      # drop the header + Level 0 rows
TX, TY = 40, 64                     # table origin in the frame
FADE = 0.3

COLS = {"perf": (0, 450), "narrow": (450, 880), "general": (880, 1334)}
ROWS = {1: (200, 312), 2: (312, 525), 3: (525, 685), 4: (685, 765), 5: (765, 888)}

# windows in FINAL time; highlights = [(t_switch_final, (col or None, row))]
WINDOWS = [
    {"name": "W1", "start": 479.68, "end": 497.68,
     "hl": [(479.68, ("general", 1))]},
    {"name": "W2", "start": 508.68, "end": 528.68,
     "hl": [(508.68, (None, 2))]},
    {"name": "W3", "start": 566.66, "end": 587.66,
     "hl": [(566.66, (None, 5)), (574.66, (None, 4))]},
    {"name": "W4", "start": 626.66, "end": 668.66,
     "hl": [(626.66, ("narrow", 5)), (642.66, ("general", 4)), (662.66, (None, 3))]},
    {"name": "W5", "start": 2094.83, "end": 2102.5,
     "hl": [(2094.83, ("general", 3))]},
]

BLACK_F = os.path.join(WORK, "arialblack.ttf")
BOLD_F = os.path.join(WORK, "arialbold.ttf")
for src, dst in [("Arial Black.ttf", BLACK_F), ("Arial Bold.ttf", BOLD_F)]:
    if not os.path.exists(dst):
        subprocess.run(["cp", f"/System/Library/Fonts/Supplemental/{src}", dst])

table = Image.open(SRC).convert("RGB")
table = table.crop((0, CROP_TOP, table.width, table.height))
tw, th = round(table.width * SCALE), round(table.height * SCALE)
table = table.resize((tw, th), Image.LANCZOS)


def cell_box(col, row):
    x0, x1 = COLS[col] if col else (0, 1334)
    y0, y1 = ROWS[row]
    return (TX + round(x0 * SCALE), TY + round((y0 - CROP_TOP) * SCALE),
            TX + round(x1 * SCALE), TY + round((y1 - CROP_TOP) * SCALE))


def base_frame():
    """Everything that never changes: scrim, labels, table with shadow, source line."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 240))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rectangle([TX + 6, TY + 8, TX + tw + 6, TY + th + 8], fill=(0, 0, 0, 200))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(10)))
    img.paste(table, (TX, TY))
    d = ImageDraw.Draw(img)
    d.rectangle([TX - 2, TY - 2, TX + tw + 1, TY + th + 1], outline=ACC + (255,), width=2)
    f_t = ImageFont.truetype(BLACK_F, 22)
    d.text((TX, 12), "GOOGLE DEEPMIND  ·  LEVELS OF AGI  (NOV 2023)", font=f_t, fill=ACC + (255,))
    f_c = ImageFont.truetype(BOLD_F, 15)
    for col, label in [("narrow", "NARROW  —  one scoped task"), ("general", "GENERAL  —  wide range of tasks")]:
        x0, x1 = COLS[col]
        cx = TX + round((x0 + x1) / 2 * SCALE)
        bb = d.textbbox((0, 0), label, font=f_c)
        d.text((cx - (bb[2] - bb[0]) / 2, 44), label, font=f_c, fill=(235, 235, 240, 255))
    f_u = ImageFont.truetype(BOLD_F, 15)
    d.text((TX, TY + th + 8), "Morris et al., \"Levels of AGI\"  ·  arxiv.org/pdf/2311.02462",
           font=f_u, fill=(170, 170, 178, 255))
    return img


def highlight_layer(box, alpha):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle([box[0] - 4, box[1] - 4, box[2] + 4, box[3] + 4], radius=8,
                        fill=ACC + (int(46 * alpha),), outline=ACC + (int(255 * alpha),), width=4)
    return lay


def ease(u):
    u = max(0.0, min(1.0, u))
    return u * u * (3 - 2 * u)


BASE = base_frame()
entries = []
for w in WINDOWS:
    dur = round(w["end"] - w["start"], 3)
    n = round(dur * FPS)
    out = os.path.join(WORK, f"levels_{w['name']}.mov")
    boxes = [(t - w["start"], cell_box(*c)) for t, c in w["hl"]]
    proc = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                             "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS),
                             "-i", "-", "-c:v", "qtrle", "-pix_fmt", "argb", out], stdin=subprocess.PIPE)
    for i in range(n):
        t = i / FPS
        fr = BASE.copy()
        for k, (t0, box) in enumerate(boxes):
            t1 = boxes[k + 1][0] if k + 1 < len(boxes) else 1e9
            a = ease((t - t0) / 0.25) * (1 - ease((t - t1) / 0.25))
            if a > 0:
                fr.alpha_composite(highlight_layer(box, a))
        g = min(ease(t / FADE), ease((dur - t) / FADE))
        if g < 1:
            r, gg, b, al = fr.split()
            fr = Image.merge("RGBA", (r, gg, b, al.point(lambda v: int(v * g))))
        proc.stdin.write(fr.tobytes())
    proc.stdin.close(); proc.wait()
    entries.append({"file": os.path.basename(out), "start": w["start"], "end": w["end"],
                    "x": 0, "y": 0, "hide_logo": True})
    print("wrote", out, dur, "s")
print(json.dumps(entries))
json.dump(entries, open(os.path.join(WORK, "levels_anim.json"), "w"))
