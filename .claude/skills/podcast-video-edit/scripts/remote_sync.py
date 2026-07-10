#!/usr/bin/env python3
"""Fully-remote episodes, phase 1: sync per-host recordings onto one timeline.

Each host records LOCALLY (QuickTime) while on a call. With headphones there
is NO shared audio between tracks — envelope cross-correlation FAILS (learned
on Ep 5). What works:

  1. `com.apple.quicktime.creationdate` = capture START (1 s resolution,
     NTP-synced Macs => +-0.6 s). `creation_time` is the SAVE time — ignore.
  2. Refine/validate via turn-taking: merged-transcript handoff gaps per
     incoming track should share one median (+-0.3 s estimator).
  3. Counted group claps ("3-2-1-clap") validate to +-0.4 s — human/call-latency
     skew means claps CONFIRM but can't give sample-exact alignment.

usage:
  remote_sync.py <workdir> <sources.json>            # extract wavs + metadata offsets
  remote_sync.py <workdir> --validate                # turn-gap medians (needs tx/*.csv)
  remote_sync.py <workdir> --claps <m0> <m1>         # clap-cluster check in a window

sources.json: {"reference": "chris",
               "tracks": {"chris": {"file": "/abs/pod.mov", "person": "chris"},
                          "jackson1": {"file": "/abs/part1.mov", "person": "jackson"}}}

Writes <workdir>/offsets.json {track: seconds-on-reference-clock} and
<workdir>/sources.json (a copy, used by later phases).
"""
import json, os, subprocess, sys, wave
from concurrent.futures import ThreadPoolExecutor

WORK = sys.argv[1]
SR = 16000


def creationdate(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format_tags=com.apple.quicktime.creationdate",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    s = r.stdout.strip()
    if not s:
        return None
    from datetime import datetime
    return datetime.fromisoformat(s).timestamp()


def extract(nm, path):
    out = f"{WORK}/audio/{nm}_16k.wav"
    if not os.path.exists(out):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vn", "-ac", "1",
                        "-ar", str(SR), "-c:a", "pcm_s16le", out], check=True)
    return out


def load(nm):
    w = wave.open(f"{WORK}/audio/{nm}_16k.wav", 'rb')
    import numpy as np
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    return x


def main_sync(srcs):
    os.makedirs(f"{WORK}/audio", exist_ok=True)
    with ThreadPoolExecutor(3) as ex:
        list(ex.map(lambda kv: extract(kv[0], kv[1]['file']), srcs['tracks'].items()))
    ref = srcs['reference']
    t_ref = creationdate(srcs['tracks'][ref]['file'])
    if t_ref is None:
        sys.exit("reference file has no com.apple.quicktime.creationdate tag")
    offsets = {}
    for nm, tr in srcs['tracks'].items():
        t = creationdate(tr['file'])
        if t is None:
            print(f"WARN {nm}: no creationdate tag — offset unknown, set manually")
            continue
        offsets[nm] = round(t - t_ref, 3)
        print(f"{nm}: {offsets[nm]:+9.3f}s")
    json.dump(offsets, open(f"{WORK}/offsets.json", 'w'), indent=2)
    json.dump(srcs, open(f"{WORK}/sources.json", 'w'), indent=2)
    print("wrote offsets.json (metadata; run --validate after transcription,"
          " then hand-correct offsets.json if a track's median is off)")


def main_validate():
    import csv
    import numpy as np
    off = json.load(open(f"{WORK}/offsets.json"))
    rows = []
    for nm in off:
        with open(f"{WORK}/tx/{nm}.csv") as f:
            for r in csv.DictReader(f):
                txt = r['text'].strip()
                if not txt or txt == '[BLANK_AUDIO]':
                    continue
                rows.append((float(r['start']) / 1000 + off[nm],
                             float(r['end']) / 1000 + off[nm], nm))
    rows.sort()
    gaps = {nm: [] for nm in off}
    for a, b in zip(rows, rows[1:]):
        if a[2] != b[2] and -6 < b[0] - a[1] < 6:
            gaps[b[2]].append(b[0] - a[1])
    med = {nm: float(np.median(g)) for nm, g in gaps.items() if g}
    gm = float(np.median(sum(gaps.values(), [])))
    print(f"global median handoff gap {gm:+.2f}s (whisper end-inflation is normal)")
    for nm, m in med.items():
        flag = " <-- shift track by this delta" if abs(m - gm) > 0.6 else ""
        print(f"  {nm}: median={m:+.2f} delta={m-gm:+.2f}{flag}")


def main_claps(m0, m1):
    import numpy as np
    off = json.load(open(f"{WORK}/offsets.json"))
    for nm in off:
        x = load(nm)
        l0, l1 = max(0, m0 - off[nm]), min(len(x) / SR, m1 - off[nm])
        if l1 <= l0:
            continue
        seg = x[int(l0 * SR):int(l1 * SR)]
        H = 16
        n = len(seg) // H
        e = np.abs(seg[:n * H]).reshape(n, H).max(axis=1)
        onset = e[30:] - e[:-30]
        o = onset.copy()
        peaks = []
        for _ in range(8):
            i = int(np.argmax(o))
            if o[i] < 0.08:
                break
            peaks.append((l0 + (i + 30) * H / SR + off[nm], float(o[i])))
            o[max(0, i - 250):i + 250] = -1
        print(f"{nm}:", " ".join(f"{t:.2f}({s:.2f})" for t, s in sorted(peaks)))
    print("claps from different rooms cluster within ~0.4s at correct offsets")


if '--validate' in sys.argv:
    main_validate()
elif '--claps' in sys.argv:
    i = sys.argv.index('--claps')
    main_claps(float(sys.argv[i + 1]), float(sys.argv[i + 2]))
else:
    main_sync(json.load(open(sys.argv[2])))
