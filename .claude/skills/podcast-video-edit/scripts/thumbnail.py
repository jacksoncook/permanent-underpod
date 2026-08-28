#!/usr/bin/env python3
"""Episode thumbnail — house recipe (Ep 10/11/12): pale yellow bg, white-outlined
person cutouts, logo badge top-left, big black/white-outlined text at the bottom.

Driven by brand.json's "thumbnail" key (the LLM picks the frames + text):

  "thumbnail": {
    "text": "AI AGENTS FORMED A CULT",       # ALL-CAPS hook, ~18-28 chars; NOT the episode title
    "out":  "/abs/path/epN-thumbnail.png",
    "faces": [                                # paste order = back-to-front
      {"track": "chris",   "t": 2155,  "cx": 640,  "top": 130, "h": 580},
      {"track": "jackson", "t": 531.5, "cx": 265,  "top": 110, "h": 600},
      {"track": "tyler1",  "t": 526.5, "cx": 1010, "top": 120, "h": 590}
    ]
  }

"track" resolves to <work>/src/<track>_720.mp4 (remote eps); use "file" (path
relative to <work>) for single-cam episodes. "t" is SOURCE-file seconds — pick
expressive frames (shock/laugh beats a neutral face; extract a candidate contact
sheet and LOOK first). Cutouts use macOS Vision via scripts/cutout.swift,
compiled on demand to <work>/cutout.

usage: python3 thumbnail.py <workdir> <brand.json>
After rendering: ALWAYS shrink-test to 320x180 and eyeball — text must stay
legible at feed size (the Ep 11 gate).
"""
import json, os, subprocess, sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

WORK, BRAND = sys.argv[1], sys.argv[2]
cfg = json.load(open(BRAND))["thumbnail"]

W, H = 1280, 720
BG = (255, 231, 158)

cutout_bin = os.path.join(WORK, "cutout")
if not os.path.exists(cutout_bin):
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cutout.swift")
    subprocess.run(["swiftc", "-O", src, "-o", cutout_bin], check=True)

frames_dir = os.path.join(WORK, "frames")
os.makedirs(frames_dir, exist_ok=True)


def face_png(i, f):
    vid = os.path.join(WORK, f["file"]) if "file" in f else \
        os.path.join(WORK, "src", f'{f["track"]}_720.mp4')
    raw = os.path.join(frames_dir, f"thumb_face{i}.png")
    cut = os.path.join(frames_dir, f"thumb_face{i}_cut.png")
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(f["t"]), "-i", vid,
                    "-frames:v", "1", "-y", raw], check=True)
    subprocess.run([cutout_bin, raw, cut], check=True)
    return cut


def outlined(cut, target_h, outline=10):
    bbox = cut.split()[3].getbbox()
    cut = cut.crop(bbox)
    scale = target_h / cut.height
    img = cut.resize((int(cut.width * scale), int(cut.height * scale)), Image.LANCZOS)
    grown = img.split()[3].filter(ImageFilter.MaxFilter(outline * 2 + 1)) \
                          .filter(ImageFilter.GaussianBlur(1.2))
    white = Image.new("RGBA", img.size, (255, 255, 255, 255))
    out = Image.composite(white, Image.new("RGBA", img.size, (0, 0, 0, 0)), grown)
    out.alpha_composite(img)
    return out


canvas = Image.new("RGB", (W, H), BG)
for i, f in enumerate(cfg["faces"]):
    img = outlined(Image.open(face_png(i, f)).convert("RGBA"), f.get("h", 590))
    canvas.paste(img, (f["cx"] - img.width // 2, f["top"]), img)

logo = Image.open(os.path.join(WORK, "logo.png")).convert("RGBA")
logo = logo.resize((210, int(logo.height * 210 / logo.width)), Image.LANCZOS)
canvas.paste(logo, (28, 24), logo)

font_path = os.path.join(WORK, "arialblack.ttf")
font = ImageFont.truetype(font_path, 86)
d = ImageDraw.Draw(canvas)
while d.textbbox((0, 0), cfg["text"], font=font)[2] > W - 50:
    font = ImageFont.truetype(font_path, font.size - 2)
bb = d.textbbox((0, 0), cfg["text"], font=font)
d.text(((W - bb[2]) // 2, H - (bb[3] - bb[1]) - 58), cfg["text"], font=font,
       fill=(10, 10, 10), stroke_width=12, stroke_fill=(255, 255, 255))

canvas.save(cfg["out"])
feed = canvas.resize((320, 180), Image.LANCZOS)
feed_path = os.path.join(frames_dir, "thumb_feed.png")
feed.save(feed_path)
print(f'OK {cfg["out"]}  shrink-test: {feed_path} — LOOK at it before shipping')
