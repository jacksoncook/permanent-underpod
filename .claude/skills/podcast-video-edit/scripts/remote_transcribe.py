#!/usr/bin/env python3
"""Fully-remote episodes, phase 2: transcribe every track separately and merge
onto the reference clock with speaker attribution FOR FREE (each track is one
person — no diarization needed).

usage: remote_transcribe.py <workdir>     # needs offsets.json + audio/*_16k.wav

Writes tx/<track>.csv, session.md (human-readable merged transcript with
[mm:ss] + raw seconds), session.json (line records for the planner).

Gotcha (Ep 5): whisper hallucinates REPEATED LINES on long near-silent
stretches of an own-voice track ("...like I said, like I said", "Thank you.
Thank you.") — read the merged transcript with that in mind, and use VAD (not
transcript density) for activity decisions.
"""
import csv, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

WORK = sys.argv[1]
MODEL = os.path.expanduser("~/.cache/whisper/ggml-small.en.bin")
OFF = json.load(open(f"{WORK}/offsets.json"))
SRC = json.load(open(f"{WORK}/sources.json"))
os.makedirs(f"{WORK}/tx", exist_ok=True)


def tx(nm):
    out = f"{WORK}/tx/{nm}"
    if not os.path.exists(out + ".csv"):
        subprocess.run(["whisper-cli", "-m", MODEL, "-f", f"{WORK}/audio/{nm}_16k.wav",
                        "-t", "4", "-ocsv", "-of", out],
                       check=True, capture_output=True)
    return nm

with ThreadPoolExecutor(3) as ex:
    list(ex.map(tx, OFF))

rows = []
for nm in OFF:
    person = SRC['tracks'][nm]['person'].upper()
    with open(f"{WORK}/tx/{nm}.csv") as f:
        for r in csv.DictReader(f):
            txt = r['text'].strip()
            if not txt or txt == '[BLANK_AUDIO]':
                continue
            s = float(r['start']) / 1000 + OFF[nm]
            rows.append({'t': round(s, 2), 'end': round(float(r['end']) / 1000 + OFF[nm], 2),
                         'spk': person, 'track': nm, 'text': txt})
rows.sort(key=lambda r: r['t'])

def fmt(t):
    t = int(t); h, r = divmod(abs(t), 3600); m, s = divmod(r, 60)
    sign = '-' if t < 0 else ''
    return f"{sign}{h}:{m:02d}:{s:02d}" if h else f"{sign}{m:02d}:{s:02d}"

with open(f"{WORK}/session.md", 'w') as f:
    f.write("# merged session transcript (reference clock)\n")
    cur = None
    for r in rows:
        tag = f"[{fmt(r['t'])}] ({r['t']:.0f}s)"
        if r['spk'] != cur:
            f.write(f"\n**{r['spk']}** {tag}: {r['text']}\n")
            cur = r['spk']
        else:
            f.write(f"  {tag} {r['text']}\n")
json.dump(rows, open(f"{WORK}/session.json", 'w'), indent=1)
print(f"wrote session.md / session.json ({len(rows)} lines)")
print("NOW: run remote_sync.py --validate and hand-correct offsets.json if needed")
