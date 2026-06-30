#!/usr/bin/env bash
# One-time setup to reproduce the Permanent Underpod editing toolkit on a new Mac.
# The skills themselves auto-load from .claude/skills/ when you open this repo in
# Claude Code — this script just installs the external tools the pipeline shells out to.
set -euo pipefail

echo "==> Checking Homebrew"
command -v brew >/dev/null || { echo "Install Homebrew first: https://brew.sh" >&2; exit 1; }

echo "==> Installing ffmpeg + whisper-cpp"
brew install ffmpeg whisper-cpp

echo "==> Fetching whisper model (small.en) -> ~/.cache/whisper/"
mkdir -p "$HOME/.cache/whisper"
if [ ! -f "$HOME/.cache/whisper/ggml-small.en.bin" ]; then
  curl -L --fail -o "$HOME/.cache/whisper/ggml-small.en.bin" \
    "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.en.bin"
fi

echo "==> Installing Pillow (graphics + captions)"
python3 -m pip install --user --quiet pillow

read -r -p "==> Set up the YouTube upload venv too? [y/N] " yn
if [[ "${yn:-}" =~ ^[Yy] ]]; then
  python3 -m venv "$HOME/.config/clipify-youtube/.venv"
  "$HOME/.config/clipify-youtube/.venv/bin/pip" install -q \
    google-api-python-client google-auth-oauthlib google-auth-httplib2
  echo "    Done. Next: follow .claude/skills/clipify/youtube-setup.md to add client_secret.json"
fi

echo ""
echo "==> Setup complete."
echo "    Skills auto-load from .claude/skills/ when you open this repo in Claude Code."
echo "    Raw .mov / final .mp4 are NOT in git (gitignored under media/) — copy them in to re-render."
