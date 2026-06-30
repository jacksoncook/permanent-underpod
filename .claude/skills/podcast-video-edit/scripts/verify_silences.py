#!/usr/bin/env python3
"""Phase 2 (fully automatic): verify silence candidates by speech-band RMS so
quiet speakers never get cut. Writes verified_cuts.json.

usage: verify_silences.py <workdir> [--dead-db -62] [--min-dur 2.0]
       verify_silences.py <workdir> --calibrate 570.7-576.7 1850.6-1872 2410-2415

Calibrate first when unsure: pass a known true silence, the faintest real
speech you can find in the transcript, and normal speech; pick a threshold
between silence and faint speech (default -62 works for far-mic rooms).
"""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

WORK = sys.argv[1]
AUDIO = os.path.join(WORK, "audio.m4a")

def arg(flag, default):
    return float(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default

DEAD = arg("--dead-db", -62.0)
MIN_DUR = arg("--min-dur", 2.0)

def band_rms(s, e):
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-ss", f"{s:.3f}", "-t", f"{e-s:.3f}", "-i", AUDIO,
         "-af", "highpass=f=200,lowpass=f=3500,"
                "astats=measure_overall=RMS_level:measure_perchannel=none",
         "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"RMS level dB: (-?[\d.]+|-inf)", r.stderr)
    return float("-inf") if (m and m.group(1) == "-inf") else (float(m.group(1)) if m else 0.0)

if "--calibrate" in sys.argv:
    for spec in sys.argv[sys.argv.index("--calibrate") + 1:]:
        if not re.match(r"[\d.]+-[\d.]+$", spec):
            break
        a, b = map(float, spec.split("-"))
        print(f"  {a}-{b}: band RMS {band_rms(a, b):.1f} dB")
    sys.exit(0)

txt = open(os.path.join(WORK, "silences.txt")).read()
cands = [(s, e) for s, e in zip(
    (float(x) for x in re.findall(r"silence_start: ([\d.]+)", txt)),
    (float(x) for x in re.findall(r"silence_end: ([\d.]+)", txt))) if e - s >= MIN_DUR]

with ThreadPoolExecutor(max_workers=8) as ex:
    levels = list(ex.map(lambda c: band_rms(c[0] + 0.3, c[1] - 0.3), cands))

out = [{"start": round(s, 3), "end": round(e, 3), "band_rms": round(l, 1)}
       for (s, e), l in zip(cands, levels) if l < DEAD]
json.dump(out, open(os.path.join(WORK, "verified_cuts.json"), "w"), indent=1)
print(f"{len(cands)} candidates -> {len(out)} verified dead-air regions "
      f"({sum(c['end']-c['start'] for c in out)/60:.1f} min), "
      f"{len(cands)-len(out)} rejected as faint speech")
