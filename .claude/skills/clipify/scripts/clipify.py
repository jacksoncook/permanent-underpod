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
                                        # per-clip override too ("anull" for a mastered source)
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

ender: spec-level `"ender": true` (or `{"duration": 1.0, "sting": path,
"text": "PERMANENT UNDERPOD"}`) appends a ~1 s branded end card to every
branded VERTICAL clip: dark card, logo pops to center on the sting hit,
wordmark + gold underline settle in. Funnel branding for shorts — the swipe
moment shows the channel, and on Shorts it doubles as the loop seam.
Per-clip `"ender": false` opts out; per-clip `"ender": true` forces it on a
non-vertical branded clip. Never applied to "plain" clips. The sting defaults
to ender-sting.wav next to the spec logo (brand/ender-sting.wav). The ender
is APPENDED — content length is unchanged; reported duration grows by ~1 s.

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

ENDER = SPEC.get("ender")

def ender_cfg(c):
    """Resolve the ender for one clip: dict when active, else None."""
    e = c.get("ender")
    if e is False or c.get("style", "branded") == "plain":
        return None
    base = ENDER if isinstance(ENDER, dict) else ({} if ENDER else None)
    if e is None and (base is None or not c.get("vertical")):
        return None
    cfg = dict(base or {})
    if isinstance(e, dict):
        cfg.update(e)
    cfg.setdefault("duration", 1.0)
    cfg.setdefault("text", "PERMANENT UNDERPOD")
    cfg.setdefault("sting", os.path.join(os.path.dirname(LOGO or ""), "ender-sting.wav"))
    return cfg

def ease_out_back(p):
    c1 = 1.70158
    return 1 + (c1 + 1) * (p - 1) ** 3 + c1 * (p - 1) ** 2

def ender_frames(w, h, nf, text):
    """Render the end-card frames once per aspect; return the frame dir."""
    from PIL import Image, ImageDraw, ImageFont
    dst = os.path.join(OUTDIR, f"_ender_{w}x{h}")
    if os.path.exists(os.path.join(dst, f"f_{nf-1:03d}.png")):
        return dst
    os.makedirs(dst, exist_ok=True)
    m = min(w, h)
    logo = Image.open(LOGO).convert("RGBA")
    lw = int(m * 0.46)
    lh = int(logo.height * lw / logo.width)
    fsz = int(m * 0.058)
    font = ImageFont.truetype(BLACK_F, fsz)
    tb = ImageDraw.Draw(Image.new("RGBA", (1, 1))).textbbox((0, 0), text, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    while tw > w * 0.88:
        fsz -= 2
        font = ImageFont.truetype(BLACK_F, fsz)
        tb = ImageDraw.Draw(Image.new("RGBA", (1, 1))).textbbox((0, 0), text, font=font)
        tw, th = tb[2] - tb[0], tb[3] - tb[1]
    bar_w, bar_h, gap = int(tw * 0.6), max(6, m // 150), int(m * 0.045)
    block = lh + gap + th + gap + bar_h
    top = (h - block) // 2
    lcx, lcy = w // 2, top + lh // 2
    ty = top + lh + gap
    by = ty + th + gap
    # hit lands ~frame 7 of the sting; logo pop peaks there via ease_out_back
    for f in range(nf):
        img = Image.new("RGBA", (w, h), (12, 12, 16, 255))
        p = min(1.0, f / 13.0)
        s = 0.4 + 0.6 * ease_out_back(p)
        a = min(1.0, f / 5.0)
        sw, sh = max(1, int(lw * s)), max(1, int(lh * s))
        li = logo.resize((sw, sh), Image.LANCZOS)
        if a < 1.0:
            alpha = li.getchannel("A").point(lambda v: int(v * a))
            li.putalpha(alpha)
        img.alpha_composite(li, (lcx - sw // 2, lcy - sh // 2))
        d = ImageDraw.Draw(img)
        if f >= 6:
            q = min(1.0, (f - 6) / 10.0)
            qe = 1 - (1 - q) ** 3
            d.text(((w - tw) // 2 - tb[0], ty - tb[1] + int((1 - qe) * m * 0.05)),
                   text, font=font, fill=(255, 255, 255, int(255 * q)))
        if f >= 10:
            r = min(1.0, (f - 10) / 10.0)
            re_ = 1 - (1 - r) ** 3
            hw = int(bar_w * re_ / 2)
            if hw > 2:
                d.rounded_rectangle([(w // 2 - hw, by), (w // 2 + hw, by + bar_h)],
                                    radius=bar_h // 2, fill=ACC)
        img.convert("RGB").save(os.path.join(dst, f"f_{f:03d}.png"))
    return dst

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
    cap_tmp = None

    if style == "plain":
        # slice a finished, already-branded+mastered video: clean accurate cut only
        fg.append("[0:v]fps=30,format=yuv420p[vout]")
        fg.append(f"[0:a]aresample={SR},apad,atrim=end_sample={n*SPF}[aout]")
    else:
        vertical = c.get("vertical", False)
        if vertical and c.get("face_crops"):
            # full-bleed speaker crop (digital/remote episodes): a 406x720
            # column tracking the active face -> 1080x1920, no blur bars.
            # face_crops = [[t_rel, x_left], ...] or [[t_rel, x_left, mode], ...]
            # where mode is "cut" (default) or "swipe":
            #   "cut"   -> the crop STEPS to the new x on one frame.
            #   "swipe" -> the crop eases (smoothstep) across over `swipe` s.
            # For multicam panel switches "cut" is the ONLY correct mode, which is
            # why it's the default: this 406-wide column is narrower than the gap
            # between any two faces, so a glide always spends its middle frames on
            # the seam -- wall plus two half-faces. Ep 8's first clip batch swiped
            # every key and read as the shot swinging off a person and boomeranging
            # back. remote_face_crops.py therefore emits "cut" for every key.
            # "swipe" is retained only for a hand-authored move WITHIN one panel
            # (e.g. drifting across a wide solo shot), where there's no seam to hit.
            SWIPE_S = float(c.get("swipe", 0.35))
            fcs = c["face_crops"]
            expr = f"{int(fcs[0][1])}"
            for i in range(1, len(fcs)):
                dx = int(fcs[i][1]) - int(fcs[i - 1][1])
                if not dx:
                    continue
                t_i = float(fcs[i][0])
                mode = (fcs[i][2] if len(fcs[i]) > 2 else "cut").lower()
                # Hard guards, not warnings: both of these are invisible in the JSON
                # and glaring on screen, and Ep 8 shipped 8 clips with them because
                # nothing checked. scripts/verify_clips.py reports them with
                # suggested fixes; this is the backstop if that gate is skipped.
                if mode == "swipe" and abs(dx) >= 40:
                    sys.exit(f"{c['name']}: face_crops t={t_i} swipes {abs(dx)}px, "
                             "which crosses a panel seam (the Ep 8 boomerang). Use "
                             '"cut". A swipe is only legal within one panel (<40px).')
                if t_i > dur - 0.5:
                    sys.exit(f"{c['name']}: face_crops switch at t={t_i} is in the "
                             f"last 0.5s of a {dur:.2f}s clip -> "
                             f"{round((dur - t_i) * FPS)} frames of another shot, "
                             "which reads as a flash at the out point. Drop the key.")
                if mode == "swipe":
                    # smoothstep p^2*(3-2p): st(0,p) stores AND returns p, so one
                    # extra ld(0) gives p^2 -- three of them would give p^3, which
                    # is what this used to do (a late, lurching ramp).
                    p = f"clip((t-{t_i:.3f})/{SWIPE_S:.2f},0,1)"
                    expr += f"+{dx}*(st(0,{p})*ld(0)*(3-2*ld(0)))"
                else:
                    expr += f"+{dx}*gte(t,{t_i:.3f})"
            fg.append("[0:v]fps=30,format=yuv420p,"
                      f"crop=w=406:h=720:x='{expr}':y=0,"
                      "scale=1080:1920,setsar=1[base]")
            logo_pos, cap_pos, lsz = "x=40:y=120", "x=(W-w)/2:y=H-h-360", 220
        elif vertical:
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
            cap_tmp = os.path.join(OUTDIR, "_cap_" + c["name"] + ".png")
            caption_png(c["caption"]["kicker"], c["caption"]["title"], cap_tmp, big=vertical)
            inputs += ["-loop", "1", "-t", f"{dur:.3f}", "-i", cap_tmp]
            fg.append(f"{last}[{idx}:v]overlay={cap_pos}:eof_action=pass[v{idx}]")
            last = f"[v{idx}]"; idx += 1
        # per-clip audio_chain: a batch can mix sources with different needs --
        # face-crop shorts come off the episode's edited_raw.mov (UNmastered, so
        # they want the episode chain) while a clip that needs a baked-in graphic
        # must come off the FINAL mp4, which is already mastered and only wants
        # "anull". Applying the episode chain twice re-runs a big pre-gain into
        # the compressor/limiter; loudnorm hides it in the level but not the sound.
        chain = c.get("audio_chain", CHAIN)
        ecfg = ender_cfg(c)
        if ecfg and (NO_LOGO or not LOGO or not os.path.exists(LOGO)
                     or not os.path.exists(ecfg["sting"])):
            print(f"  {c['name']}: ender skipped (logo or sting missing)")
            ecfg = None
        if ecfg:
            ne = max(1, round(float(ecfg["duration"]) * FPS))
            if vertical:
                ew, eh = 1080, 1920
            else:
                p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                                    "-show_entries", "stream=width,height",
                                    "-of", "csv=p=0", src],
                                   capture_output=True, text=True).stdout.strip()
                ew, eh = (int(x) for x in p.split(","))
            edir = ender_frames(ew, eh, ne, ecfg["text"])
            inputs[2:2] = ["-t", f"{dur + 1.0:.3f}"]
            c["_ender_applied"] = True
            fg.append(f"{last}trim=end_frame={n},setpts=N/{FPS}/TB,setsar=1[vmain]")
            fg.append(f"[0:a]aresample={SR}:async=1:first_pts=0,{chain},"
                      f"aresample={SR},aformat=channel_layouts=stereo,"
                      f"apad,atrim=end_sample={n*SPF}[amain]")
            ei = len([x for x in inputs if x == "-i"])
            inputs += ["-framerate", str(FPS), "-i", os.path.join(edir, "f_%03d.png"),
                       "-i", ecfg["sting"]]
            fg.append(f"[{ei}:v]fps={FPS},format=yuv420p,setsar=1[vend]")
            fg.append(f"[{ei+1}:a]aresample={SR},aformat=channel_layouts=stereo,"
                      f"apad,atrim=end_sample={ne*SPF}[aend]")
            fg.append("[vmain][amain][vend][aend]concat=n=2:v=1:a=1[vout][aout]")
            n += ne
        else:
            fg.append(f"{last}null[vout]")
            fg.append(f"[0:a]aresample={SR}:async=1:first_pts=0,{chain},"
                      f"aresample={SR},apad,atrim=end_sample={n*SPF}[aout]")

    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"] + inputs + [
        "-filter_complex", ";".join(fg), "-map", "[vout]", "-map", "[aout]",
        "-frames:v", str(n), "-r", "30", "-fps_mode", "cfr",
        "-video_track_timescale", "30000",
        "-c:v", "h264_videotoolbox", "-b:v", "8M", "-profile:v", "high",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if cap_tmp and os.path.exists(cap_tmp):
        os.remove(cap_tmp)  # caption is burned into the mp4; PNG is scratch
    if r.returncode != 0:
        print("FAIL", c["name"], r.stderr[-3000:]); return None
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of", "csv=p=0", out],
                             capture_output=True, text=True).stdout.strip())
    tag = style if style == "plain" else ("9:16" if c.get("vertical") else "16:9")
    if c.get("_ender_applied"):
        tag += "+ender"
    print(f"  {c['name']}.mp4  {d:.1f}s  [{tag}]")
    return out

made = [build(c) for c in SPEC.get("clips", [])]
import glob, shutil
for e in glob.glob(os.path.join(OUTDIR, "_ender_*x*")):
    shutil.rmtree(e, ignore_errors=True)  # frames are burned in; dir is scratch
print(f"clipified {len([m for m in made if m])}/{len(SPEC.get('clips', []))} -> {OUTDIR}")
