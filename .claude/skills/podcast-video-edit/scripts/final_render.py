#!/usr/bin/env python3
"""Phase 5 (automatic): final encode — overlays + logo bug + audio chain + SFX.
Reads clips.json / overlays.json from cut_render.py and a render.json config.

usage: python3 final_render.py <workdir> <render.json> [--test=75]

render.json schema:
{
  "out": "/path/Final Cut.mp4",
  "chain": "highpass=f=70,afftdn=nr=22:nf=-52:tn=1,dynaudnorm=f=200:g=11:m=30:p=0.95:t=0.0065",
  "target_lufs": -16, "limit": 0.84,
  "logo": {"file": "logo.png", "width": 170, "alpha": 0.8,
            "hide_during": ["CARD_TITLE", "CARD_END"]},
  "reframe_presets": {            # OPTIONAL; punch-in/push presets used by reframes.json
    "jackson": {"zoom": 1.85, "cx": 285, "cy": 285},   # crop center in source 1280x720 px
    "center":  {"zoom": 1.5,  "cx": 640, "cy": 400},
    "push":    {"zoom": 1.12, "cx": 640, "cy": 360}},  # "push" eases zoom across the window
  "sfx": [{"file": "sfx_whoosh.wav", "block": "CARD_TITLE", "offset": -0.45},
           {"file": "sfx_sting.wav",  "block": "CARD_END",   "offset": 0}]
}

Notes baked in from hard experience:
- every -loop 1 image input gets a finite -t (else the encode NEVER terminates)
- every overlay uses eof_action=pass
- output gets -t <timeline> -shortest as a belt-and-braces cap
- loudness: measure post-chain LUFS first, apply linear volume + alimiter
  (loudnorm linear=true silently under-gains when input TP is hot)
"""
import json, os, re, subprocess, sys

WORK = sys.argv[1]
CFG = json.load(open(sys.argv[2]))
TEST_T = next((float(a.split("=")[1]) for a in sys.argv if a.startswith("--test=")), None)

clips = json.load(open(os.path.join(WORK, "clips.json")))
overlays = json.load(open(os.path.join(WORK, "overlays.json")))
# optional video picture-in-picture windows (screen recordings etc.) written by
# remote_cut.py: [{file, mode: corner|full, crop:[w,h,x,y]|null, t0, start, end}]
pfile = os.path.join(WORK, "pip.json")
pips = json.load(open(pfile)) if os.path.exists(pfile) else []
raw = os.path.join(WORK, "edited_raw.mov")
CHAIN = CFG["chain"]
total = clips[-1]["final_start"] + clips[-1]["dur"]

def blk_start(bid):
    return next(c["final_start"] for c in clips if c["block"] == bid)

# measure post-chain loudness (audio-only decode: fast)
mfile = os.path.join(WORK, "loudmeas.json")
if not os.path.exists(mfile):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", raw, "-map", "0:a", "-af",
                        CHAIN + ",loudnorm=print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    # loudnorm prints its JSON summary somewhere in stderr, often with ffmpeg
    # progress/footer lines after it — so grab the LAST {...} block, not an
    # end-anchored match (the anchor was fragile and returned None mid-run).
    blocks = re.findall(r"\{[^{}]*\}", r.stderr, re.S)
    if not blocks:
        sys.exit("loudnorm measurement failed:\n" + r.stderr[-800:])
    json.dump(json.loads(blocks[-1]), open(mfile, "w"))
meas = json.load(open(mfile))
gain = CFG.get("target_lufs", -16) - float(meas["input_i"])
lim = CFG.get("limit", 0.84)
print(f"post-chain {meas['input_i']} LUFS -> gain {gain:+.2f} dB, limiter {lim}")

# test mode: drop overlay/pip/sfx entries outside the test window — their looped
# far-future inputs can deadlock the filtergraph against a short output -t
if TEST_T:
    overlays = [o for o in overlays if o["start"] < TEST_T]
    pips = [p for p in pips if p["start"] < TEST_T]
    CFG["sfx"] = [s for s in CFG.get("sfx", [])
                  if blk_start(s["block"]) + s.get("offset", 0) < TEST_T]
    CFG["anim"] = [a for a in CFG.get("anim", []) if a["start"] < TEST_T]
    CFG["aux_audio"] = [a for a in CFG.get("aux_audio", []) if a["at"] < TEST_T]

cmd = ["ffmpeg", "-hide_banner", "-loglevel", "warning", "-stats", "-y", "-i", raw]
for o in overlays:
    cmd += ["-loop", "1", "-t", f"{o['end']+0.5:.2f}", "-i",
            os.path.join(WORK, o["name"] + ".png")]
logo = CFG.get("logo")
i_next = 1 + len(overlays)
if logo:
    cmd += ["-loop", "1", "-t", f"{total:.2f}", "-i", os.path.join(WORK, logo["file"])]
    i_logo = i_next; i_next += 1
sfx_idx = []
for s in CFG.get("sfx", []):
    cmd += ["-i", os.path.join(WORK, s["file"])]
    sfx_idx.append(i_next); i_next += 1
# animated overlays: short looping alpha movs (e.g. qtrle) shown during [start,end]
# windows in FINAL time. -stream_loop -1 + a finite input -t cap (same runaway-
# encode guard as the -loop 1 images).
anims = CFG.get("anim", [])
anim_idx = []
for a in anims:
    cmd += ["-stream_loop", "-1", "-t", f"{a['end']+0.5:.2f}",
            "-i", os.path.join(WORK, a["file"])]
    anim_idx.append(i_next); i_next += 1
# aux audio beds: clean external audio (e.g. a screen-share/playback source)
# mixed UNDER the room capture at exact FINAL-time positions. Each entry places
# file[src_start,src_end] at final time `at`, with a constant gain and edge fades.
# Mixed post-chain (like sfx) so the voice chain doesn't re-process clean audio.
auxes = CFG.get("aux_audio", [])
aux_idx = []
for a in auxes:
    cmd += ["-i", os.path.join(WORK, a["file"])]
    aux_idx.append(i_next); i_next += 1
pip_idx = []
for p in pips:
    cmd += ["-ss", f"{max(0, p['t0']):.2f}", "-t", f"{p['end']-p['start']+1.0:.2f}",
            "-i", p["file"]]
    pip_idx.append(i_next); i_next += 1

f = []
# --- creative reframes: punch-ins / slow pushes, applied UNDER the overlays ---
# A single static camera (couch wide) gets monotonous; reframes simulate cutting
# to a tighter shot of the active speaker (or a slow push for emphasis). We do
# the WHOLE schedule in ONE zoompan pass driven by piecewise expressions of the
# output time (on/30), so it costs one scaler pass — not N crop/scale branches —
# and stays frame-exact (1280x720 CFR in, 1:1 out), leaving the anti-drift work
# untouched. Outside every window z=1 -> the crop is the full frame (no zoom).
# Lower-thirds/logo composite on top afterwards, so captions stay full-frame/sharp.
rfile = os.path.join(WORK, "reframes.json")
reframes = json.load(open(rfile)) if os.path.exists(rfile) else []
# Each preset has a START (zoom,cx,cy) and OPTIONAL END (zoom2,cx2,cy2). When an end
# value differs it EASES across the window -> pushes (zoom moves) and pans (center
# moves) fall out of the same machinery; static "face-cut" presets just omit the *2.
DEF = {"jackson": {"zoom": 1.85, "cx": 285, "cy": 285},
       "tyler":   {"zoom": 1.85, "cx": 975, "cy": 270},
       "center":  {"zoom": 1.5,  "cx": 640, "cy": 460},
       "push":    {"zoom": 1.0,  "cx": 640, "cy": 360, "zoom2": 1.12},
       "pushin":  {"zoom": 1.25, "cx": 640, "cy": 430, "zoom2": 1.65, "cy2": 465},
       "pan_lr":  {"zoom": 1.6,  "cx": 400, "cy": 290, "cx2": 880},
       "pan_rl":  {"zoom": 1.6,  "cx": 880, "cy": 290, "cx2": 400}}
PRESETS = CFG.get("reframe_presets", {})
def preset(name):
    p = dict(DEF.get(name, DEF["center"])); p.update(PRESETS.get(name, {})); return p

cur = "[0:v]"
if reframes:
    # Build each expression as a FLAT SUM of per-window terms, not nested if()s:
    # ffmpeg's expression parser recurses per nesting level and hard-fails past
    # ~60-70 nested ifs ("Missing ')' or too many args"), so a season-length
    # schedule (100+ reframes) can't compile the nested form. With windows
    # non-overlapping (cut_render sorts them), z = 1 + sum(Bi*(zi-1)) and
    # x = sum(Bi*xi) are equivalent: outside every window all Bi=0 -> z=1 and
    # x=y=0, which at zoom=1 is exactly the full-frame crop. Bi uses
    # gte*lt (half-open) so back-to-back windows can't double-count a frame.
    # The parser ALSO fails (ENOMEM) on very long expressions (~100 summed
    # terms), so the schedule is CHUNKED across chained zoompan passes of <=40
    # windows each. Disjoint windows make chaining safe: while one pass is
    # inside a window, every other pass is identity (z=1 full frame), and each
    # pass is 1:1 in/out (d=1, fps=30) so frame-exactness is preserved.
    CHUNK = 40
    for ci in range(0, len(reframes), CHUNK):
        zterms, xterms, yterms = [], [], []
        for r in reframes[ci:ci + CHUNK]:
            s, e = r["start"], r["end"]; dur = max(0.1, e - s)
            if "rect" in r:                   # explicit [x,y,w,h] -> static crop
                x, y, w, h = r["rect"]
                z0 = z1 = 1280.0 / w; cx0 = cx1 = x + w / 2; cy0 = cy1 = y + h / 2
            else:
                p = preset(r["preset"])
                z0, cx0, cy0 = p["zoom"], p["cx"], p["cy"]
                z1, cx1, cy1 = p.get("zoom2", z0), p.get("cx2", cx0), p.get("cy2", cy0)
            u = f"max(0,min(1,(on/30-{s})/{dur:.3f}))"  # 0->1 ramp across the window
            zt  = f"{z0}" if z1 == z0 else f"({z0}+{z1-z0:.4f}*{u})"
            cxt = f"{cx0}" if cx1 == cx0 else f"({cx0}+{cx1-cx0:.2f}*{u})"
            cyt = f"{cy0}" if cy1 == cy0 else f"({cy0}+{cy1-cy0:.2f}*{u})"
            xt = f"max(0,min(iw-iw/zoom,{cxt}-(iw/zoom)/2))"  # x/y use current 'zoom' var
            yt = f"max(0,min(ih-ih/zoom,{cyt}-(ih/zoom)/2))"
            B = f"(gte(on/30,{s})*lt(on/30,{e}))"
            zterms.append(f"{B}*({zt}-1)")
            xterms.append(f"{B}*{xt}")
            yterms.append(f"{B}*{yt}")
        zx = "1+" + "+".join(zterms)
        xx = "+".join(xterms)
        yy = "+".join(yterms)
        f.append(f"{cur}zoompan=z='{zx}':x='{xx}':y='{yy}'"
                 f":d=1:s=1280x720:fps=30,setsar=1[zp{ci}]")
        cur = f"[zp{ci}]"

# PiP video windows composite UNDER lower thirds / logo. setpts shifts the
# trimmed input to its window; eof_action=pass + finite input -t keep it safe.
for k, (i, p) in enumerate(zip(pip_idx, pips)):
    if p["mode"] == "full":
        proc, pos = "scale=1280:720", "x=0:y=0"
    else:
        cw, ch, cx0, cy0 = p.get("crop") or [1100, 550, 410, 130]
        proc = f"crop={cw}:{ch}:{cx0}:{cy0},scale=430:-2"
        pos = "x=W-w-30:y=24"
    f.append(f"[{i}:v]fps=30,setpts=PTS-STARTPTS+{p['start']:.2f}/TB,{proc},"
             f"format=yuv420p[pp{k}]")
    f.append(f"{cur}[pp{k}]overlay={pos}:eof_action=pass"
             f":enable='between(t,{p['start']},{p['end']})'[vp{k}]")
    cur = f"[vp{k}]"
for k, o in enumerate(overlays):
    pos = {"lt": "x=60:y=H-h-46", "st2": "x=W-w-50:y=H-h-46"}.get(o["kind"], "x=W-w-50:y=64")
    f.append(f"{cur}[{k+1}:v]overlay={pos}:eof_action=pass"
             f":enable='between(t,{o['start']},{o['end']})'[v{k}]")
    cur = f"[v{k}]"
for k, (i, a) in enumerate(zip(anim_idx, anims)):
    f.append(f"{cur}[{i}:v]overlay=x={a['x']}:y={a['y']}:eof_action=pass"
             f":enable='between(t,{a['start']},{a['end']})'[va{k}]")
    cur = f"[va{k}]"
if logo:
    hide = "*".join(
        f"not(between(t,{blk_start(b):.2f},{blk_start(b)+next(c['dur'] for c in clips if c['block']==b):.2f}))"
        for b in logo.get("hide_during", []))
    f.append(f"[{i_logo}:v]format=rgba,scale={logo.get('width',170)}:-1,"
             f"colorchannelmixer=aa={logo.get('alpha',0.8)}[bug]")
    f.append(f"{cur}[bug]overlay=x=36:y=28:eof_action=pass"
             + (f":enable='{hide}'" if hide else "") + "[vout]")
    cur = "[vout]"
else:
    f.append(f"{cur}null[vout]")

# aresample=async=1:first_pts=0 locks audio to the video clock from t=0 so the
# final mux can't reintroduce an offset.
f.append(f"[0:a]aresample=async=1:first_pts=0,{CHAIN},"
         f"volume={gain:.2f}dB,alimiter=limit={lim}:level=false[sp]")
amix_in = "[sp]"
for j, (i, s) in enumerate(zip(sfx_idx, CFG.get("sfx", []))):
    ms = int(max(0, blk_start(s["block"]) + s.get("offset", 0)) * 1000)
    f.append(f"[{i}:a]adelay={ms}:all=1[sx{j}]")
    amix_in += f"[sx{j}]"
for j, (i, a) in enumerate(zip(aux_idx, auxes)):
    dur = a["src_end"] - a["src_start"]
    fd = a.get("fade", 0.4)
    ms = int(a["at"] * 1000)
    f.append(f"[{i}:a]atrim={a['src_start']}:{a['src_end']},asetpts=PTS-STARTPTS,"
             f"aresample=48000,volume={a.get('gain_db', 0):.2f}dB,"
             f"afade=t=in:st=0:d={fd},afade=t=out:st={dur-fd:.3f}:d={fd},"
             f"adelay={ms}:all=1[ax{j}]")
    amix_in += f"[ax{j}]"
# The FINAL limiter runs 4x-oversampled. alimiter caps SAMPLE peak, but AAC
# encodes the continuous waveform, so a sample-limited master can decode a few
# dB HOT (inter-sample peaks become real samples at the new phase). Limiting at
# 192 kHz catches those. This is cheap insurance, NOT a fix for a hot master:
# on Ep 8 it produced a BIT-IDENTICAL file, because the overage had already been
# clipped INTO edited_raw.mov upstream (gain_target too high -> the 16-bit PCM
# intermediate hit 0 dBFS, which is destructive and permanent). If you measure a
# hot true peak, astats the INTERMEDIATE first: "Flat factor > 0" there means the
# damage predates this stage and no amount of limiting here will undo it.
TP_LIM = f"aresample=192000,alimiter=limit={lim}:level=false,aresample=48000"
n_mix = 1 + len(sfx_idx) + len(aux_idx)
if n_mix > 1:
    f.append(f"{amix_in}amix=inputs={n_mix}:duration=first:normalize=0,"
             f"{TP_LIM}[aout]")
else:
    f.append(f"[sp]{TP_LIM}[aout]")

out = CFG["out"] if not TEST_T else os.path.join(WORK, "test_head.mp4")
cmd += ["-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[aout]",
        "-t", f"{(TEST_T or total + 0.2):.2f}", "-shortest",
        "-r", "30", "-fps_mode", "cfr", "-video_track_timescale", "30000",
        "-c:v", "h264_videotoolbox", "-b:v", "7500k", "-profile:v", "high",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart", out]
print("rendering...", "(test)" if TEST_T else "")
r = subprocess.run(cmd)
if r.returncode == 0:
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of", "csv=p=0", out],
                             capture_output=True, text=True).stdout.strip())
    print(f"OK {out}  {d/60:.2f} min  {os.path.getsize(out)/(1<<30):.2f} GB")
sys.exit(r.returncode)
