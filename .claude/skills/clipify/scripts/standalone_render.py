#!/usr/bin/env python3
"""Cut search-intent standalone videos out of finished episode masters.

A standalone = optional hook (one line) -> 3 s title card -> one or more parts spliced from
the published final cuts (same or different episodes). Parts are re-encoded frame-exact with
the clipify `plain` recipe (no overlays, no audio processing: the masters are already
mastered). A 0.4 s dip to black separates parts that come from different episodes.

usage:
  standalone_render.py <standalones.json> --emit-clips <clips.json>   # for verify_clips.py
  standalone_render.py <standalones.json> [--only NAME ...]           # render mp4 + srt

standalones.json:
{
  "out_dir": "media/standalones",
  "logo": "brand/logo-1920.png",
  "items": [
    {"name": "lightning", "title": "How the Lightning Network actually works",
     "hook":  {"source": "media/ep19/....mp4", "start": "44:09.8", "end": "44:24.9"},
     "parts": [{"source": "...", "srt": "episodes/ep19/transcript-attributed.srt",
                "start": "34:35.0", "end": "41:41.2"}, ...]}
  ]
}

Every boundary must pass `verify_clips.py` on the emitted clips.json BEFORE rendering
(never cut mid-word). Captions come from the source SRTs, offset into standalone time.
"""
import argparse
import json
import os
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS, SR = 1280, 720, 30, 48000
SPF = SR // FPS
CARD_S = 3.0
GAP_S = 0.4
ACCENT = (255, 210, 74, 255)
FONT_DIR = "/System/Library/Fonts/Supplemental"


def tsec(v):
    if isinstance(v, (int, float)):
        return float(v)
    parts = v.split(":")
    return sum(float(p) * m for p, m in zip(reversed(parts), (1, 60, 3600)))


def run(cmd):
    subprocess.run(cmd, check=True)


def ffmpeg(*args):
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args])


def frames(dur):
    return int(round(dur * FPS))


def encode_part(src, start, end, out):
    n = frames(end - start)
    ffmpeg("-ss", f"{start:.3f}", "-i", src, "-t", f"{n / FPS:.4f}",
           "-filter_complex",
           f"[0:v]fps={FPS},format=yuv420p[v];"
           f"[0:a]aresample={SR},aformat=channel_layouts=mono,apad,atrim=end_sample={n * SPF},"
           f"afade=t=in:d=0.03,afade=t=out:st={n / FPS - 0.03:.3f}:d=0.03[a]",
           "-map", "[v]", "-map", "[a]", "-frames:v", str(n),
           "-c:v", "h264_videotoolbox", "-b:v", "8M", "-c:a", "pcm_s16le", out)
    return n / FPS


def black(out, dur=GAP_S):
    ffmpeg("-f", "lavfi", "-t", str(dur), "-i", f"color=c=black:s={W}x{H}:r={FPS}",
           "-f", "lavfi", "-t", str(dur), "-i", f"anullsrc=r={SR}:cl=mono",
           "-c:v", "h264_videotoolbox", "-b:v", "8M", "-c:a", "pcm_s16le", "-shortest", out)
    return dur


def grab_frame(src, t, out):
    ffmpeg("-ss", f"{t:.3f}", "-i", src, "-frames:v", "1", out)


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    for w in words:
        trial = (cur + " " + w).strip()
        if probe.textbbox((0, 0), trial, font=font)[2] <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def title_card(bg_png, logo_png, title, out_png, out_mov):
    img = Image.open(bg_png).convert("RGBA").resize((W, H), Image.LANCZOS)
    img = img.filter(ImageFilter.GaussianBlur(28))
    img = Image.alpha_composite(img, Image.new("RGBA", (W, H), (10, 10, 16, 190)))
    logo = Image.open(logo_png).convert("RGBA")
    logo = logo.resize((220, int(logo.height * 220 / logo.width)), Image.LANCZOS)
    img.alpha_composite(logo, ((W - logo.width) // 2, 70))
    d = ImageDraw.Draw(img)
    kicker = ImageFont.truetype(f"{FONT_DIR}/Arial Bold.ttf", 22)
    size = 46
    while True:
        tf = ImageFont.truetype(f"{FONT_DIR}/Arial Black.ttf", size)
        lines = wrap(title, tf, W - 220)
        if len(lines) <= 2 or size <= 30:
            break
        size -= 2
    y0 = 70 + logo.height + 28
    d.line([(W / 2 - 180, y0), (W / 2 + 180, y0)], fill=ACCENT, width=3)
    y = y0 + 26
    kt = "EXPLAINER"
    kw = d.textbbox((0, 0), kt, font=kicker)[2]
    d.text(((W - kw) / 2, y), kt, font=kicker, fill=(200, 200, 205, 255))
    y += 44
    for ln in lines:
        lw = d.textbbox((0, 0), ln, font=tf)[2]
        d.text(((W - lw) / 2, y), ln, font=tf, fill=(255, 255, 255, 255))
        y += int(size * 1.3)
    img.convert("RGB").save(out_png)
    ffmpeg("-loop", "1", "-t", str(CARD_S), "-i", out_png,
           "-f", "lavfi", "-t", str(CARD_S), "-i", f"anullsrc=r={SR}:cl=mono",
           "-filter_complex",
           f"[0:v]fps={FPS},format=yuv420p,fade=t=in:st=0:d=0.4,fade=t=out:st={CARD_S - 0.5}:d=0.5[v]",
           "-map", "[v]", "-map", "1:a", "-c:v", "h264_videotoolbox", "-b:v", "8M",
           "-c:a", "pcm_s16le", "-shortest", out_mov)
    return CARD_S


def read_srt(path):
    cues = []
    for blk in open(path, encoding="utf-8", errors="ignore").read().strip().split("\n\n"):
        L = blk.split("\n")
        if len(L) >= 3 and "-->" in L[1]:
            a, b = L[1].split(" --> ")
            text = re.sub(r"^(Jackson|Chris|Tyler|Insert|Gemini|AI [A-Za-z]+):\s*", "",
                          " ".join(L[2:]).strip())
            cues.append((tsec(a.replace(",", ".")), tsec(b.replace(",", ".")), text))
    return cues


def fmt_srt(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def collect_cues(srt, start, end, offset):
    out = []
    for a, b, text in read_srt(srt):
        if b <= start or a >= end or not text:
            continue
        out.append((max(a, start) - start + offset, min(b, end) - start + offset, text))
    return out


def emit_clips(spec, path):
    clips = []
    for it in spec["items"]:
        segs = ([("hook", it["hook"])] if it.get("hook") else []) + \
               [(f"p{i + 1}", p) for i, p in enumerate(it["parts"])]
        for tag, s in segs:
            clips.append({"name": f"{it['name']}-{tag}", "source": os.path.abspath(s["source"]),
                          "start": tsec(s["start"]), "end": tsec(s["end"]), "style": "plain"})
    json.dump({"source": clips[0]["source"], "out_dir": os.path.abspath(spec["out_dir"]),
               "clips": clips}, open(path, "w"), indent=1)
    print(f"wrote {len(clips)} boundary clips -> {path}")


def render_item(spec, it):
    out_dir = spec["out_dir"]
    work = os.path.join(out_dir, "work", it["name"])
    os.makedirs(work, exist_ok=True)
    seq, cues, t = [], [], 0.0
    if it.get("hook"):
        h = it["hook"]
        f = os.path.join(work, "hook.mov")
        d = encode_part(h["source"], tsec(h["start"]), tsec(h["end"]), f)
        if h.get("srt"):
            cues += collect_cues(h["srt"], tsec(h["start"]), tsec(h["end"]), t)
        seq.append(f)
        t += d
    first = it["parts"][0]
    bg = os.path.join(work, "bg.png")
    grab_frame(first["source"], tsec(first["start"]) + 2.0, bg)
    card = os.path.join(work, "card.mov")
    t += title_card(bg, spec["logo"], it.get("card_line", it["title"]), os.path.join(work, "card.png"), card)
    seq.append(card)
    prev_src = None
    for i, p in enumerate(it["parts"]):
        if prev_src and p["source"] != prev_src:
            g = os.path.join(work, f"gap{i}.mov")
            t += black(g)
            seq.append(g)
        f = os.path.join(work, f"part{i + 1}.mov")
        a, b = tsec(p["start"]), tsec(p["end"])
        d = encode_part(p["source"], a, b, f)
        if p.get("srt"):
            cues += collect_cues(p["srt"], a, b, t)
        seq.append(f)
        t += d
        prev_src = p["source"]
    lst = os.path.join(work, "concat.txt")
    with open(lst, "w") as fh:
        for f in seq:
            fh.write(f"file '{os.path.abspath(f)}'\n")
    final = os.path.join(out_dir, f"{it['name']}.mp4")
    ffmpeg("-f", "concat", "-safe", "0", "-i", lst, "-c:v", "h264_videotoolbox", "-b:v", "8M",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", final)
    with open(os.path.join(out_dir, f"{it['name']}.srt"), "w") as fh:
        for n, (a, b, text) in enumerate(cues, 1):
            fh.write(f"{n}\n{fmt_srt(a)} --> {fmt_srt(b)}\n{text}\n\n")
    print(f"{it['name']}: {t / 60:.1f} min, {len(cues)} cues -> {final}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--emit-clips")
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    spec = json.load(open(a.spec))
    if a.emit_clips:
        emit_clips(spec, a.emit_clips)
        return
    os.makedirs(spec["out_dir"], exist_ok=True)
    for it in spec["items"]:
        if a.only and it["name"] not in a.only:
            continue
        render_item(spec, it)


if __name__ == "__main__":
    main()
