#!/usr/bin/env python3
"""Cut standalone clips out of a longer video — short teasers/shorts AND
long-form segment extractions (e.g. pull one chapter out as its own video).
Each clip is independent and upload-ready.

usage: python3 clipify.py <clips.json> [--no-logo]
       (needs Pillow only if a clip has a caption — pip install pillow)

Times accept seconds (3207.4) or clock strings ("58:01", "1:11:31").

clips.json:
{
  "source":   "/path/video.mov",        # default source; per-clip can override
  "out_dir":  "/path/out",              # default ./clips
  "logo":     "/path/logo.png",         # optional corner bug (branded clips)
  "fonts_dir":"/path",                  # dir w/ arialblack.ttf+arialbold.ttf (auto-copied on macOS)
  "audio_chain": "<ffmpeg -af chain>",  # optional; default cleanup + 1-pass loudnorm
  "clips": [
    # short branded teaser pulled from RAW footage:
    {"name": "hook-1", "start": 3207.0, "end": 3215.4,
     "caption": {"kicker": "BIGGEST FUMBLES", "title": "$20K -> $100K -> $0"},
     "vertical": false},
    # long-form chapter pulled from the FINISHED cut (already branded+mastered):
    {"name": "contrarian-corner", "source": "/path/ep1-final.mp4",
     "start": "58:01", "end": "1:11:31", "style": "plain"}
  ]
}

style: "branded" (default) adds logo bug + optional caption + audio cleanup &
loudnorm — for clips cut from raw footage. "plain" does a clean, frame-accurate
re-encode with NO overlays and NO audio processing — for slicing a segment out
of an already-finished video.

All clips are frame-aligned (video_len == audio_len), h264 + aac + faststart.
"""
import json, os, subprocess, sys

SPEC = json.load(open(sys.argv[1]))
NO_LOGO = "--no-logo" in sys.argv
FPS, SR, SPF = 30, 48000, 1600  # 1600 = 48000/30 samples per video frame
ACC, WHITE = (255, 210, 74, 255), (255, 255, 255, 255)

OUTDIR = SPEC.get("out_dir", os.path.join(os.getcwd(), "clips"))
os.makedirs(OUTDIR, exist_ok=True)
LOGO = SPEC.get("logo")
DEF_SRC = SPEC.get("source")
CHAIN = SPEC.get("audio_chain",
    "highpass=f=70,afftdn=nr=22:nf=-52:tn=1,"
    "acompressor=threshold=-20dB:ratio=3:attack=15:release=250:knee=6,"
    "loudnorm=I=-16:TP=-1.5:LRA=5")

FONTS = SPEC.get("fonts_dir", OUTDIR)
BLACK_F, BOLD_F = os.path.join(FONTS, "arialblack.ttf"), os.path.join(FONTS, "arialbold.ttf")
for sysname, dst in [("Arial Black.ttf", BLACK_F), ("Arial Bold.ttf", BOLD_F)]:
    sp = f"/System/Library/Fonts/Supplemental/{sysname}"
    if not os.path.exists(dst) and os.path.exists(sp):
        subprocess.run(["cp", sp, dst])

def ts(v):
    """Seconds from a number or 'H:MM:SS' / 'MM:SS' string."""
    if isinstance(v, (int, float)):
        return float(v)
    s = 0.0
    for p in str(v).split(":"):
        s = s * 60 + float(p)
    return s

def caption_png(kicker, title, path, big=False):
    from PIL import Image, ImageDraw, ImageFont
    ks, ts_ = (30, 48) if big else (24, 38)
    fk, ft = ImageFont.truetype(BOLD_F, ks), ImageFont.truetype(BLACK_F, ts_)
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    w = max(tmp.textbbox((0, 0), kicker, font=fk)[2],
            tmp.textbbox((0, 0), title, font=ft)[2]) + 62
    h = ks + ts_ + 56
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([(0, 0), (w - 1, h - 1)], radius=14, fill=(12, 12, 16, 205))
    d.rounded_rectangle([(0, 0), (10, h - 1)], radius=5, fill=ACC)
    d.text((44, 16), kicker, font=fk, fill=ACC)
    d.text((44, 16 + ks + 8), title, font=ft, fill=WHITE)
    img.save(path)

def build(c):
    src = c.get("source", DEF_SRC)
    if not src:
        print("SKIP", c["name"], "(no source)"); return None
    if not os.path.exists(src):
        print("SKIP", c["name"], f"(source not found: {src})"); return None
    start, end = ts(c["start"]), ts(c["end"])
    n = max(1, round((end - start) * FPS))
    dur = n / FPS
    out = os.path.join(OUTDIR, c["name"] + ".mp4")
    style = c.get("style", "branded")
    inputs = ["-ss", f"{start:.3f}", "-i", src]
    fg = []

    if style == "plain":
        # slice a finished, already-branded+mastered video: clean accurate cut only
        fg.append("[0:v]fps=30,format=yuv420p[vout]")
        fg.append(f"[0:a]aresample={SR},apad,atrim=end_sample={n*SPF}[aout]")
    else:
        vertical = c.get("vertical", False)
        if vertical:
            fg.append("[0:v]fps=30,format=yuv420p,split=2[bg][fg]")
            fg.append("[bg]scale=1080:1920:force_original_aspect_ratio=increase,"
                      "crop=1080:1920,gblur=sigma=22,eq=brightness=-0.22[bgb]")
            fg.append("[fg]scale=1080:-2[fgs]")
            fg.append("[bgb][fgs]overlay=(W-w)/2:(H-h)/2[base]")
            logo_pos, cap_pos, lsz = "x=40:y=120", "x=(W-w)/2:y=H-h-360", 220
        else:
            fg.append("[0:v]fps=30,format=yuv420p[base]")
            logo_pos, cap_pos, lsz = "x=36:y=28", "x=60:y=H-h-46", 170
        last, idx = "[base]", 1
        if c.get("logo", True) and not NO_LOGO and LOGO and os.path.exists(LOGO):
            inputs += ["-loop", "1", "-t", f"{dur:.3f}", "-i", LOGO]
            fg.append(f"[{idx}:v]format=rgba,scale={lsz}:-1,colorchannelmixer=aa=0.85[bug]")
            fg.append(f"{last}[bug]overlay={logo_pos}:eof_action=pass[v{idx}]")
            last = f"[v{idx}]"; idx += 1
        if c.get("caption"):
            cp = os.path.join(OUTDIR, "_cap_" + c["name"] + ".png")
            caption_png(c["caption"]["kicker"], c["caption"]["title"], cp, big=vertical)
            inputs += ["-loop", "1", "-t", f"{dur:.3f}", "-i", cp]
            fg.append(f"{last}[{idx}:v]overlay={cap_pos}:eof_action=pass[v{idx}]")
            last = f"[v{idx}]"; idx += 1
        fg.append(f"{last}null[vout]")
        fg.append(f"[0:a]aresample={SR}:async=1:first_pts=0,{CHAIN},"
                  f"aresample={SR},apad,atrim=end_sample={n*SPF}[aout]")

    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"] + inputs + [
        "-filter_complex", ";".join(fg), "-map", "[vout]", "-map", "[aout]",
        "-frames:v", str(n), "-r", "30", "-fps_mode", "cfr",
        "-video_track_timescale", "30000",
        "-c:v", "h264_videotoolbox", "-b:v", "8M", "-profile:v", "high",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAIL", c["name"], r.stderr[-300:]); return None
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of", "csv=p=0", out],
                             capture_output=True, text=True).stdout.strip())
    tag = style if style == "plain" else ("9:16" if c.get("vertical") else "16:9")
    print(f"  {c['name']}.mp4  {d:.1f}s  [{tag}]")
    return out

made = [build(c) for c in SPEC.get("clips", [])]
print(f"clipified {len([m for m in made if m])}/{len(SPEC.get('clips', []))} -> {OUTDIR}")
