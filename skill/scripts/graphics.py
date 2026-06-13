#!/usr/bin/env python3
"""Phase 3 (automatic, driven by LLM-authored brand.json): logo, title/end
cards (PNG + .mov), lower thirds, stat callouts.

usage: <workdir>/.venv/bin/python graphics.py <workdir> <brand.json>

brand.json schema (all text decided by the LLM):
{
  "show": "PERMANENT UNDERPOD", "show_kicker": "PERMANENT",
  "show_main": "UNDERPOD",                  # logo text lines
  "accent": [255, 210, 74],
  "source": "/path/raw.mov",
  "title_card": {"bg_frame": 2410, "line": "EPISODE 1 · Bitcoin · Stablecoins · AI", "dur": 4.5},
  "end_card":   {"bg_frame": 5165, "kicker": "NEXT WEEK ON", "lines": ["..."],
                  "cta": "LIKE + SUBSCRIBE", "dur": 7},
  "lower_thirds": [{"name": "meet", "kicker": "EPISODE 1", "title": "MEET THE HOSTS"}],
  "stats":        [{"name": "loop", "kicker": "JACKSON'S FUMBLE", "main": "$20,000 -> $10,000"}]
}
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import json, os, subprocess, sys

WORK, BRAND = sys.argv[1], json.load(open(sys.argv[2]))
W, H = 1280, 720
ACC = tuple(BRAND.get("accent", [255, 210, 74])) + (255,)
WHITE = (255, 255, 255, 255)
BLACK_F = os.path.join(WORK, "arialblack.ttf")
BOLD_F = os.path.join(WORK, "arialbold.ttf")
for src, dst in [("Arial Black.ttf", BLACK_F), ("Arial Bold.ttf", BOLD_F)]:
    if not os.path.exists(dst):
        subprocess.run(["cp", f"/System/Library/Fonts/Supplemental/{src}", dst])

font = lambda p, s: ImageFont.truetype(p, s)

def center(d, y, text, f, fill):
    bb = d.textbbox((0, 0), text, font=f)
    d.text(((W - bb[2] + bb[0]) / 2, y), text, font=f, fill=fill)

def grab_frame(t, out):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(t),
                    "-i", BRAND["source"], "-frames:v", "1", out])

def blurred_bg(path):
    img = Image.open(path).convert("RGB").resize((W, H)).filter(ImageFilter.GaussianBlur(22))
    return Image.blend(img, Image.new("RGB", (W, H), (10, 10, 14)), 0.55).convert("RGBA")

def make_logo():
    S = 480
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([(8, 8), (S - 9, S - 9)], radius=86, fill=(14, 14, 19, 240),
                        outline=ACC, width=7)
    dark = (14, 14, 19, 255)
    d.rounded_rectangle([(118, 108), (362, 218)], radius=26, fill=ACC)   # couch back
    d.rounded_rectangle([(78, 152), (138, 268)], radius=22, fill=ACC)    # arms
    d.rounded_rectangle([(342, 152), (402, 268)], radius=22, fill=ACC)
    d.rounded_rectangle([(130, 196), (238, 262)], radius=14, fill=ACC, outline=dark, width=6)
    d.rounded_rectangle([(242, 196), (350, 262)], radius=14, fill=ACC, outline=dark, width=6)
    d.rounded_rectangle([(96, 258), (384, 282)], radius=10, fill=ACC)    # base
    d.rectangle([(120, 282), (146, 306)], fill=ACC); d.rectangle([(334, 282), (360, 306)], fill=ACC)
    k = " ".join(BRAND.get("show_kicker", "")) or None
    if k:
        center(d, 322, k, font(BOLD_F, 27), WHITE)
    center(d, 358, BRAND.get("show_main", BRAND["show"]), font(BLACK_F, 56), ACC)
    img.save(os.path.join(WORK, "logo.png"))
    return img

logo = make_logo()

def card_video(png, dur, out):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                    "-loop", "1", "-t", str(dur), "-i", png,
                    "-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=mono",
                    "-filter_complex",
                    f"[0:v]fps=30,format=yuv420p,fade=t=in:st=0:d=0.5,"
                    f"fade=t=out:st={dur-0.6}:d=0.6[v]",
                    "-map", "[v]", "-map", "1:a", "-c:v", "h264_videotoolbox",
                    "-b:v", "10M", "-c:a", "pcm_s16le", "-shortest",
                    os.path.join(WORK, out)], check=True)

# title card
tc = BRAND["title_card"]
grab_frame(tc["bg_frame"], os.path.join(WORK, "bg_title.png"))
img = blurred_bg(os.path.join(WORK, "bg_title.png"))
img.alpha_composite(logo.resize((300, 300), Image.LANCZOS), ((W - 300) // 2, 92))
d = ImageDraw.Draw(img)
d.line([(W/2 - 200, 452), (W/2 + 200, 452)], fill=ACC, width=3)
center(d, 482, tc["line"], font(BOLD_F, 32), (235, 235, 235, 255))
img.convert("RGB").save(os.path.join(WORK, "png_title.png"))
card_video(os.path.join(WORK, "png_title.png"), tc.get("dur", 4.5), "card_title.mov")

# end card
ec = BRAND["end_card"]
grab_frame(ec["bg_frame"], os.path.join(WORK, "bg_end.png"))
img = blurred_bg(os.path.join(WORK, "bg_end.png"))
img.alpha_composite(logo.resize((150, 150), Image.LANCZOS), ((W - 150) // 2, 36))
d = ImageDraw.Draw(img)
center(d, 212, " ".join(ec.get("kicker", "NEXT TIME ON")), font(BOLD_F, 26), ACC)
center(d, 252, BRAND["show"], font(BLACK_F, 50), WHITE)
y = 360
for ln in ec.get("lines", []):
    center(d, y, f"·  {ln}  ·", font(BOLD_F, 33), (235, 235, 235, 255)); y += 58
center(d, 562, ec.get("cta", "LIKE + SUBSCRIBE"), font(BLACK_F, 38), ACC)
img.convert("RGB").save(os.path.join(WORK, "png_end.png"))
card_video(os.path.join(WORK, "png_end.png"), ec.get("dur", 7), "card_end.mov")

def boxed(name, kicker, title, fk_s, ft_s, h, prefix, accent_bar):
    fk, ft = font(BOLD_F, fk_s), font(BLACK_F, ft_s)
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    w = max(tmp.textbbox((0, 0), kicker, font=fk)[2],
            tmp.textbbox((0, 0), title, font=ft)[2]) + 52 + (18 if accent_bar else 0)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([(0, 0), (w - 1, h - 1)], radius=14, fill=(12, 12, 16, 202))
    x = 26
    if accent_bar:
        d.rounded_rectangle([(0, 0), (10, h - 1)], radius=5, fill=ACC); x = 44
    else:
        d.rounded_rectangle([(0, h - 8), (w - 1, h - 1)], radius=4, fill=ACC)
    d.text((x, 16 if accent_bar else 14), kicker, font=fk, fill=ACC)
    d.text((x, 52 if accent_bar else 46), title, font=ft, fill=WHITE)
    img.save(os.path.join(WORK, f"{prefix}_{name}.png"))

for lt in BRAND.get("lower_thirds", []):
    boxed(lt["name"], lt["kicker"], lt["title"], 24, 38, 118, "lt", True)
for st in BRAND.get("stats", []):
    boxed(st["name"], st["kicker"], st["main"], 22, 34, 104, "st", False)

print("graphics done:", len(BRAND.get("lower_thirds", [])), "lower thirds,",
      len(BRAND.get("stats", [])), "stats, logo + 2 cards")
