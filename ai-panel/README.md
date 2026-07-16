# ai-panel — local AI-clone talking-head panel

One-shot local pipeline: **N face images + voice audio → per-speaker
lip-synced talking-head clips → one composed multi-person video.**

```
python3 make_panel.py --config script.json --layout panel          --out final.mp4
python3 make_panel.py --config script.json --layout active-speaker --out final.mp4
```

- `panel` — everyone on screen in a horizontal row; the active speaker's
  tile gets a highlight border while the others play subtle idle loops
  (no frozen faces).
- `active-speaker` — hard cut to whoever is talking, full frame, with a
  name lower-third.

The pipeline itself is **stdlib-only Python + ffmpeg**. The talking-head
model runs in its *own* checkout/env and is invoked via subprocess, so
swapping models never touches this code's dependencies.

## Quick smoke test (no models needed, ~30 s)

```bash
bash sample/make_demo_assets.sh          # placeholder faces + `say` audio
python3 make_panel.py --config sample/demo/script.json \
    --backend static --layout panel --out outputs/demo_panel.mp4
```

The `static` backend is ffmpeg-only (still face + audio, no lip sync) —
it exists to prove config → generation → normalization → idle loops →
composition → concat end-to-end before you install any model.

## script.json

Per-speaker audio (speakers talk in listed order):

```json
{
  "speakers": [
    {"name": "jackson", "display_name": "Jackson",
     "face_image": "faces/jackson.jpg", "audio_file": "audio/jackson.wav"},
    {"name": "chris",  "face_image": "faces/chris.jpg",  "audio_file": "audio/chris.wav"},
    {"name": "tyler",  "face_image": "faces/tyler.jpg",  "audio_file": "audio/tyler.wav"}
  ]
}
```

Or **one master audio file + person assignments** (the "script + single
audio + who-says-what" workflow) — turns can repeat speakers freely:

```json
{
  "audio_file": "audio/full_conversation.wav",
  "speakers": [
    {"name": "jackson", "face_image": "faces/jackson.jpg"},
    {"name": "chris",   "face_image": "faces/chris.jpg"},
    {"name": "tyler",   "face_image": "faces/tyler.jpg"}
  ],
  "timeline": [
    {"speaker": "jackson", "start": 0.0,  "end": 12.5},
    {"speaker": "chris",   "start": 12.5, "end": 31.0},
    {"speaker": "jackson", "start": 31.0, "end": 40.2},
    {"speaker": "tyler",   "start": 40.2, "end": 55.0}
  ]
}
```

Notes:
- Paths are relative to the config file. `display_name` is optional
  (defaults to `name` title-cased).
- Timeline entries may also carry their own `"audio_file"` (plus optional
  `start`/`end`) to override per turn.
- 1–4 speakers supported. Face images: clear, front-facing, one face,
  ideally ≥512 px on the short side.

## CLI

```
--config PATH        script.json
--layout             panel | active-speaker        (default: panel)
--out PATH           final mp4
--backend            musetalk | sadtalker | liveportrait | static
                                                   (default: musetalk)
--idle-mode          silence | loop | still        (default: silence)
--workdir PATH       intermediates go to <workdir>/intermediate/
                                                   (default: ./outputs)
--force              regenerate cached talking-head clips
```

`--idle-mode`: `silence` (default) runs the backend once per speaker on
near-silent audio, producing a genuine not-talking clip — neutral mouth,
natural head motion — that loops in their tile while others speak. `loop`
boomerangs the speaker's own *talking* clip, which keeps motion but makes
idle mouths flap; `still` is a subtle breathing zoom on a frozen frame
(safest for MuseTalk, which doesn't move the head anyway).

Talking-head generation is cached in `outputs/intermediate/talk/` keyed by
a content hash of (face image, turn audio, backend) — re-running with a
tweaked layout or idle mode does **not** re-run the model. `--force`
busts the cache.

## Setup

### Base (macOS / Linux)

```bash
# macOS
brew install ffmpeg
# Debian/Ubuntu
sudo apt install ffmpeg python3
```

Python ≥3.10, no pip packages required for the pipeline itself.

### MuseTalk setup (default backend, best lip-sync quality)

Realistically needs an **NVIDIA GPU (CUDA)**; CPU works but is extremely
slow, and Apple-Silicon MPS support is not reliable. On a Mac, either run
MuseTalk on a Linux/GPU box (this tool only needs the checkout reachable
via `MUSETALK_DIR`, so you can also just generate the talk clips remotely
and rsync them into `outputs/intermediate/talk/`), or use SadTalker below.

```bash
git clone https://github.com/TMElyralab/MuseTalk ~/models/MuseTalk
cd ~/models/MuseTalk
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# torch: follow https://pytorch.org for your CUDA version, e.g.
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install --no-cache-dir -U openmim && mim install mmengine "mmcv>=2.0.1" "mmdet>=3.1.0" "mmpose>=1.1.0"
sh ./download_weights.sh          # unet, vae, whisper, dwpose → models/

export MUSETALK_DIR=~/models/MuseTalk        # required
# optional: MUSETALK_PYTHON (defaults to $MUSETALK_DIR/.venv/bin/python),
#           MUSETALK_VERSION=v15|v1, MUSETALK_EXTRA_ARGS="--bbox_shift -7"
```

MuseTalk animates the *mouth region* of the source image; from a still
photo the head won't move — pair it with `--idle-mode still`, or feed a
short looping video of the person as `face_image`-quality improvement
later. If MuseTalk's CLI flags drift between releases, pin the invocation
with `MUSETALK_EXTRA_ARGS` or adjust `panelkit/backends/musetalk.py`
(one command list).

### SadTalker setup (head motion + nodding — VERIFIED on Apple Silicon)

```bash
brew install uv                    # once
bash setup_sadtalker.sh            # clone + env + patches + ~2.5 GB weights
export SADTALKER_DIR=~/models/SadTalker
# quality/motion knobs: SADTALKER_EXTRA_ARGS="--enhancer gfpgan" (sharper),
#   "--still" (damp head motion), "--size 512"; SADTALKER_PREPROCESS=full
#   keeps the whole source frame instead of the face crop
```

`setup_sadtalker.sh` encodes everything a 2023-era repo needs to run on a
2026 stack: Python 3.11 (numpy 1.23 pin), `setuptools<81` (librosa needs
`pkg_resources`), relaxed `scikit-image`/`imageio` pins, the `basicsr`
torchvision-import fix, and two small source patches that replace the legacy
`.type(x.type())` tensor API so the renderer runs on **MPS (Apple GPU)**.
The panelkit backend sets `TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1` and
`PYTORCH_ENABLE_MPS_FALLBACK=1` automatically.

Measured on an M5 Max (128 GB), 10 s clip, 256 px, `--preprocess crop`:
**~55 s on MPS** (face renderer 125 frames @ 2.95 it/s) vs **~11 min on
CPU** (5.2 s/frame). SadTalker generates natural head pose from the audio,
which is also what makes the default `--idle-mode silence` idles look alive.

### LivePortrait

`panelkit/backends/liveportrait.py` is a documented stub: LivePortrait is
driven by a motion video rather than audio, so it needs an audio-to-motion
front end. The backend interface (`panelkit/backends/base.py`) is three
methods; mirror `sadtalker.py` when wiring it in.

### GPU / CPU summary

| Backend   | NVIDIA GPU | Apple Silicon (MPS)              | CPU |
|-----------|------------|----------------------------------|-----|
| sadtalker | ✅ fast    | ✅ **verified, ~5× real-time** (M5 Max) | 🐢 ~65× real-time |
| musetalk  | ✅ fast    | ⚠️ untried (mmcv/mmpose are CUDA-centric) | 🐢 very slow |
| static    | n/a        | ✅ instant                       | ✅ instant |

## How it works

```
script.json ─► validate ─► per-turn wav (slice/convert, 48 kHz)
        ─► backend.generate(face, wav) per turn   [cached by content hash]
        ─► normalize (25 fps, 720 px tall, -16 LUFS loudnorm, h264/aac)
        ─► idle loops per speaker (boomerang or breathing-zoom still)
        ─► compose each turn (hstack panel + highlight, or full-frame cut)
        ─► concat ─► final.mp4  (1920×1080, 25 fps)
```

Intermediates are kept in `outputs/intermediate/{audio,talk,norm,idle,turns,jobs}`
for inspection/reuse. `outputs/` is gitignored.

## Troubleshooting

- **`error: ... face image not found / no decodable audio stream`** — all
  inputs are validated up front; fix the path or re-export the audio
  (`ffmpeg -i in.m4a out.wav` accepts almost anything).
- **Backend fails mid-run** — the last ~25 lines of the model's output are
  included in the error; the raw job dir survives under
  `outputs/intermediate/jobs/` for digging.
- **No face detected** (MuseTalk/SadTalker) — use a real, front-facing,
  single-face photo; the demo's placeholder initials will not work.
- **Name labels missing** — no usable font found; install
  `fonts-dejavu-core` (Linux) or check `_FONT_CANDIDATES` in
  `panelkit/compose.py`.
- **Audio pops at turn boundaries** — expected at this prototype stage;
  trim your per-turn boundaries at silences (or ask for crossfades to be
  added in `compose.concat`).
