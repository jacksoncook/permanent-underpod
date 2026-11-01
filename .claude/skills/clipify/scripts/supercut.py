#!/usr/bin/env python3
"""Stitch many short pieces of one episode into a single vertical short (a word or
phrase montage: every "billion" in the show, three hosts saying the same thing).

usage: python3 supercut.py <supercut.json>

spec: {"source", "out_dir", "logo", "audio_chain", "workdir", "name", "caption",
       "pieces": [{"start", "end"}, ...], "snap": 0.2, "pad": 0.06}

Each piece boundary is snapped to the quietest 10 ms of the speech-band envelope
within +-snap s (the same measurement verify_clips.py gates on), the active face is
located with remote_face_crops.py over the piece, every piece is rendered through
clipify.py as a face-crop vertical (shared caption, no ender), the pieces are
concatenated with the concat demuxer, and the montage is run through clipify.py once
more for the ender. The gate's silence rule cannot hold between words, so the result
must be watched before it is scheduled."""
import json, os, subprocess, sys, tempfile, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPIFY = os.path.join(HERE, "clipify.py")
FACE = os.path.normpath(os.path.join(HERE, "..", "..", "podcast-video-edit", "scripts", "remote_face_crops.py"))
SPEC = json.load(open(sys.argv[1]))
SRC, OUT, NAME = SPEC["source"], SPEC["out_dir"], SPEC["name"]
SNAP, PAD = SPEC.get("snap", 0.2), SPEC.get("pad", 0.06)
PIECES = os.path.join(OUT, f"_{NAME}_pieces")
os.makedirs(PIECES, exist_ok=True)


def envelope(t0, dur):
    wav = os.path.join(PIECES, "_env.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-t", f"{dur:.3f}", "-i", SRC,
                    "-vn", "-ac", "1", "-ar", "16000", "-af", "highpass=f=200,lowpass=f=3500", wav], check=True)
    with wave.open(wav) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    n = len(x) // 160
    rms = np.sqrt((x[: n * 160].reshape(n, 160) ** 2).mean(axis=1)) + 1e-9
    return 20 * np.log10(rms)


def quietest(t, lo, hi):
    """Time of the quietest 10 ms window in [t+lo, t+hi]."""
    db = envelope(t + lo, hi - lo)
    return t + lo + (int(np.argmin(db)) + 0.5) * 0.01


def face_x(a, b):
    out = subprocess.run([sys.executable, FACE, SPEC["workdir"], f"{a:.3f}", f"{b:.3f}"],
                         capture_output=True, text=True).stdout.strip().splitlines()
    keys = json.loads(out[-1])
    return keys[0][1]


clips = []
for i, p in enumerate(SPEC["pieces"]):
    a = quietest(p["start"], -SNAP, PAD)
    b = quietest(p["end"], -PAD, SNAP)
    if b - a < 0.25:
        sys.exit(f"piece {i} collapsed to {b - a:.2f}s ({a:.2f}-{b:.2f}); widen it")
    clips.append({"name": f"p{i:02d}", "start": round(a, 3), "end": round(b, 3), "vertical": True,
                  "ender": False, "caption": SPEC.get("caption"), "face_crops": [[0.0, face_x(a, b), "cut"]]})
    print(f"  piece {i:2d}  {p['start']:.2f}-{p['end']:.2f} -> {a:.2f}-{b:.2f}  ({b - a:.2f}s)  x={clips[-1]['face_crops'][0][1]}")

piece_spec = {"source": SRC, "out_dir": PIECES, "logo": SPEC["logo"], "audio_chain": SPEC["audio_chain"],
              "ender": False, "clips": clips}
json.dump(piece_spec, open(os.path.join(PIECES, "pieces.json"), "w"), indent=1)
subprocess.run([sys.executable, CLIPIFY, os.path.join(PIECES, "pieces.json")], check=True)

lst = os.path.join(PIECES, "concat.txt")
open(lst, "w").write("".join(f"file '{os.path.join(PIECES, c['name'])}.mp4'\n" for c in clips))
body = os.path.join(PIECES, "body.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", body], check=True)

dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", body],
                           capture_output=True, text=True).stdout)
final_spec = {"source": body, "out_dir": OUT, "logo": SPEC["logo"], "ender": True,
              "clips": [{"name": NAME, "start": 0.0, "end": round(dur, 3), "vertical": True,
                         "audio_chain": "anull", "logo": False}]}
json.dump(final_spec, open(os.path.join(PIECES, "final.json"), "w"), indent=1)
subprocess.run([sys.executable, CLIPIFY, os.path.join(PIECES, "final.json")], check=True)
json.dump({"pieces": clips, "body_seconds": dur}, open(os.path.join(OUT, f"{NAME}.pieces.json"), "w"), indent=1)
print(f"supercut -> {os.path.join(OUT, NAME)}.mp4  ({dur:.1f}s + ender, {len(clips)} pieces)")
