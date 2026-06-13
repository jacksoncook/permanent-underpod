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

f, cur = [], "[0:v]"
for k, o in enumerate(overlays):
    pos = "x=60:y=H-h-46" if o["kind"] == "lt" else "x=W-w-50:y=64"
    f.append(f"{cur}[{k+1}:v]overlay={pos}:eof_action=pass"
             f":enable='between(t,{o['start']},{o['end']})'[v{k}]")
    cur = f"[v{k}]"
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
if sfx_idx:
    f.append(f"{amix_in}amix=inputs={1+len(sfx_idx)}:duration=first:normalize=0,"
             f"alimiter=limit={lim}:level=false[aout]")
else:
    f.append("[sp]anull[aout]")

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
