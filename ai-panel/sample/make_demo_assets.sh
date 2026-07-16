#!/usr/bin/env bash
# Generate synthetic demo assets (placeholder faces + spoken/tone audio)
# under sample/demo/, for smoke-testing the pipeline with --backend static.
#
# NOTE: the placeholder "faces" are colored initials — real backends
# (musetalk/sadtalker) need actual face photos and will fail face detection
# on these. They exist only to prove the pipeline end-to-end.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p demo/faces demo/audio

font=""
if ffmpeg -hide_banner -filters 2>/dev/null | grep -q ' drawtext '; then
  for f in "/System/Library/Fonts/Helvetica.ttc" \
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" \
           "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"; do
    [ -f "$f" ] && font="$f" && break
  done
fi

make_face() { # name initial color
  local vf="format=yuv420p"
  if [ -n "$font" ]; then
    vf="drawtext=fontfile='$font':text='$2':fontsize=300:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-30,format=yuv420p"
  fi
  ffmpeg -y -v error -f lavfi -i "color=c=$3:s=720x900" -vf "$vf" \
    -frames:v 1 "demo/faces/$1.png"
}
make_face alice A 0x2E5E4E
make_face bob   B 0x33415C
make_face cara  C 0x6E3B3B

make_audio() { # name voice freq text
  if command -v say >/dev/null 2>&1; then
    say -v "$2" -o "demo/audio/$1.aiff" "$4"
    ffmpeg -y -v error -i "demo/audio/$1.aiff" -ar 48000 -ac 2 "demo/audio/$1.wav"
    rm -f "demo/audio/$1.aiff"
  else
    ffmpeg -y -v error -f lavfi -i "sine=frequency=$3:duration=5" \
      -af "volume=0.3" -ar 48000 -ac 2 "demo/audio/$1.wav"
  fi
}
make_audio alice Samantha 300 "Welcome back to the show. Today we are testing the AI clone panel pipeline, end to end, on this very machine."
make_audio bob   Daniel   220 "Thanks Alice. I am a placeholder face, but my audio is real, and my tile should light up right now."
make_audio cara  Karen    260 "And when neither of us is talking, our tiles should keep moving subtly instead of freezing. That is the whole trick."

cat > demo/script.json <<'EOF'
{
  "speakers": [
    {"name": "alice", "display_name": "Alice", "face_image": "faces/alice.png", "audio_file": "audio/alice.wav"},
    {"name": "bob",   "display_name": "Bob",   "face_image": "faces/bob.png",   "audio_file": "audio/bob.wav"},
    {"name": "cara",  "display_name": "Cara",  "face_image": "faces/cara.png",  "audio_file": "audio/cara.wav"}
  ]
}
EOF

echo "demo assets ready under $(pwd)/demo"
echo "smoke test:"
echo "  python3 ../make_panel.py --config demo/script.json --backend static --layout panel --out ../outputs/demo_panel.mp4"
