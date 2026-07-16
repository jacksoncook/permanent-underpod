#!/usr/bin/env bash
# One-shot SadTalker setup, verified on Apple Silicon (M5 Max, 2026-07-16).
# Produces a working checkout at $SADTALKER_DIR (default ~/models/SadTalker):
# Python 3.11 env via uv, torch 2.13 + MPS, all legacy-dep fixes applied,
# ~2.5 GB of weights downloaded.
#
# After it finishes:   export SADTALKER_DIR=~/models/SadTalker
set -euo pipefail

DIR="${SADTALKER_DIR:-$HOME/models/SadTalker}"
command -v uv >/dev/null || { echo "need uv: brew install uv"; exit 1; }
command -v git >/dev/null || { echo "need git"; exit 1; }

[ -d "$DIR/.git" ] || git clone --depth 1 https://github.com/OpenTalker/SadTalker "$DIR"
cd "$DIR"

uv venv --python 3.11 .venv
PY=.venv/bin/python

# setuptools<81: librosa 0.9.2 needs pkg_resources (removed in 82+);
# basicsr's setup.py also imports setuptools+torch (hence no-build-isolation).
uv pip install --python $PY 'setuptools<81' wheel
uv pip install --python $PY torch torchvision torchaudio

# Relax pins that predate py3.11 arm64 wheels; drop gradio (webui only).
sed -E -e 's/scikit-image==0.19.3/scikit-image>=0.21/' \
       -e 's/imageio==2.19.3/imageio>=2.27,<3/' \
       -e '/^gradio/d' requirements.txt > /tmp/sadtalker_req.txt
uv pip install --python $PY --no-build-isolation -r /tmp/sadtalker_req.txt
# the requirements resolve can shuffle setuptools — re-pin
uv pip install --python $PY 'setuptools<81'

# --- source patches for modern torch / MPS ---
# 1) basicsr: torchvision removed transforms.functional_tensor in 0.17
grep -rl 'torchvision.transforms.functional_tensor' .venv/lib/python3.11/site-packages/basicsr/ 2>/dev/null | \
  xargs -I{} sed -i.bak 's/torchvision.transforms.functional_tensor/torchvision.transforms.functional/' {}
# 2) legacy .type(x.type()) API breaks on MPS ('torch.mps.FloatTensor' is not
#    constructible) — modernize to .to(x), and make arange() device-aware
$PY - <<'EOF'
import re
from pathlib import Path

root = Path("src")
pat = re.compile(r"\.type\((\w[\w\.]*?)\.type\(\)\)")
for f in root.rglob("*.py"):
    s = f.read_text()
    s2 = pat.sub(r".to(\1)", s)
    if s2 != s:
        f.write_text(s2)
        print("patched .type():", f)

util = root / "facerender/modules/util.py"
s = util.read_text()
if "_mps_safe_arange" not in s:
    helper = '''
def _mps_safe_arange(n, type):
    # legacy FOMM API passes tensor.type() strings; 'torch.mps.FloatTensor'
    # is not a constructible type name, so build on mps explicitly
    if isinstance(type, str) and "mps" in type:
        return torch.arange(n, dtype=torch.float32, device="mps")
    return torch.arange(n).type(type)

'''
    s = s.replace("def make_coordinate_grid_2d(spatial_size, type):",
                  helper + "def make_coordinate_grid_2d(spatial_size, type):")
    for axis, n in (("x", "w"), ("y", "h"), ("z", "d")):
        s = s.replace(f"{axis} = torch.arange({n}).type(type)",
                      f"{axis} = _mps_safe_arange({n}, type)")
    util.write_text(s)
    print("patched arange:", util)

inf = Path("inference.py")
s = inf.read_text()
if 'args.device = "mps"' not in s:
    s = s.replace(
        '''    if torch.cuda.is_available() and not args.cpu:
        args.device = "cuda"
''',
        '''    if torch.cuda.is_available() and not args.cpu:
        args.device = "cuda"
    elif torch.backends.mps.is_available() and not args.cpu:
        args.device = "mps"
''')
    inf.write_text(s)
    print("patched device:", inf)
EOF

# --- weights (~2.5 GB) ---
mkdir -p checkpoints gfpgan/weights
dl() { [ -s "$2" ] || curl -fL --retry 3 -o "$2" "$1"; }
dl https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00109-model.pth.tar checkpoints/mapping_00109-model.pth.tar
dl https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/mapping_00229-model.pth.tar checkpoints/mapping_00229-model.pth.tar
dl https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_256.safetensors checkpoints/SadTalker_V0.0.2_256.safetensors
dl https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2-rc/SadTalker_V0.0.2_512.safetensors checkpoints/SadTalker_V0.0.2_512.safetensors
dl https://github.com/xinntao/facexlib/releases/download/v0.1.0/alignment_WFLW_4HG.pth gfpgan/weights/alignment_WFLW_4HG.pth
dl https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth gfpgan/weights/detection_Resnet50_Final.pth
dl https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth gfpgan/weights/GFPGANv1.4.pth
dl https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth gfpgan/weights/parsing_parsenet.pth

$PY -c "import torch, basicsr, facexlib, gfpgan, pkg_resources; \
print('SadTalker ready | torch', torch.__version__, '| mps:', torch.backends.mps.is_available())"
echo "now:  export SADTALKER_DIR=$DIR"
