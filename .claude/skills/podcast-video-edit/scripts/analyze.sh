#!/bin/bash
# Phase 1 (fully automatic): probe, extract audio, transcribe, find silence
# candidates, measure loudness. Everything the LLM needs to plan the edit.
#
# usage: analyze.sh <input-video> <workdir>
set -euo pipefail
SRC="$1"; WORK="$2"
mkdir -p "$WORK"
cd "$WORK"

echo "== probe =="
ffprobe -v error -show_format -show_streams -of json "$SRC" > probe.json
python3 -c "
import json; d=json.load(open('probe.json'))
v=[s for s in d['streams'] if s['codec_type']=='video'][0]
a=[s for s in d['streams'] if s['codec_type']=='audio'][0]
print(f\"  {v['width']}x{v['height']} {v['codec_name']}, audio {a['codec_name']} {a.get('channels')}ch, {float(d['format']['duration'])/60:.1f} min\")"

echo "== audio extract =="
[ -f audio.m4a ] || ffmpeg -hide_banner -loglevel error -i "$SRC" -vn -c:a copy audio.m4a 2>/dev/null \
  || ffmpeg -hide_banner -loglevel error -i "$SRC" -vn -c:a aac -b:a 256k audio.m4a
[ -f audio16k.wav ] || ffmpeg -hide_banner -loglevel error -i audio.m4a -ar 16000 -ac 1 -c:a pcm_s16le audio16k.wav

echo "== whisper =="
command -v whisper-cli >/dev/null || brew install whisper-cpp
MODEL="$HOME/.cache/whisper/ggml-small.en.bin"
mkdir -p "$(dirname "$MODEL")"
[ -f "$MODEL" ] || curl -sL -o "$MODEL" \
  "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.en.bin"
[ -f transcript.csv ] || whisper-cli -m "$MODEL" -f audio16k.wav -t 8 -ocsv -osrt -of transcript >/dev/null 2>&1
echo "  $(wc -l < transcript.csv) transcript rows"

echo "== silence candidates (-38dB, >=2s) =="
[ -f silences.txt ] || ffmpeg -hide_banner -i audio.m4a -af silencedetect=noise=-38dB:d=2.0 -f null - 2>&1 \
  | grep -E "silence_(start|end)" | sed 's/.*] //' > silences.txt
echo "  $(grep -c silence_start silences.txt) candidates"

echo "== input loudness =="
[ -f loudness_input.json ] || ffmpeg -hide_banner -i audio.m4a \
  -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 \
  | python3 -c "import sys,re,json; m=re.search(r'\{[^{}]*\}', sys.stdin.read()[-2000:], re.S); print(m.group(0))" \
  > loudness_input.json
python3 -c "import json; d=json.load(open('loudness_input.json')); print(f\"  {d['input_i']} LUFS, TP {d['input_tp']} dB\")"

echo "== python env (Pillow for graphics) =="
[ -d .venv ] || { python3 -m venv .venv && .venv/bin/pip -q install pillow; }

echo "DONE. Next: read transcript.csv to plan the edit, then verify_silences.py."
