"""SadTalker backend (https://github.com/OpenTalker/SadTalker).

Image + audio -> talking head WITH generated head pose/nodding (unlike
MuseTalk-from-a-still, which only animates the mouth). Configure with:

  SADTALKER_DIR         path to the cloned SadTalker repo (required)
  SADTALKER_PYTHON      python of SadTalker's env
                        (default: $SADTALKER_DIR/.venv/bin/python if present,
                         else "python3")
  SADTALKER_PREPROCESS  crop (default; face-only, most reliable) or
                        full (keeps the whole source frame)
  SADTALKER_EXTRA_ARGS  extra CLI args, e.g. "--enhancer gfpgan" for face
                        quality, "--still" to damp head motion, "--size 512",
                        "--cpu" to force CPU (shlex-split)

Verified working on Apple Silicon (M5, torch 2.13 + MPS): the wrapper sets
TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1 (SadTalker's pickled checkpoints predate
torch 2.6's weights_only default) and PYTORCH_ENABLE_MPS_FALLBACK=1 (a few
ops fall back to CPU).
"""

from __future__ import annotations

import os
import shlex
import shutil
from pathlib import Path

from .base import BackendError, TalkingHeadBackend


class SadTalkerBackend(TalkingHeadBackend):
    name = "sadtalker"

    def __init__(self) -> None:
        self.repo = Path(os.environ["SADTALKER_DIR"]).expanduser() \
            if os.environ.get("SADTALKER_DIR") else None
        py = os.environ.get("SADTALKER_PYTHON")
        if not py and self.repo and (self.repo / ".venv/bin/python").exists():
            py = str(self.repo / ".venv/bin/python")
        self.python = py or "python3"
        self.preprocess = os.environ.get("SADTALKER_PREPROCESS", "crop")
        self.extra_args = shlex.split(os.environ.get("SADTALKER_EXTRA_ARGS", ""))

    def check_available(self) -> None:
        if self.repo is None:
            raise BackendError(
                "SADTALKER_DIR is not set. Clone and set up SadTalker "
                "(see README.md → 'SadTalker setup'), then:\n"
                "  export SADTALKER_DIR=~/models/SadTalker"
            )
        if not (self.repo / "inference.py").exists():
            raise BackendError(
                f"{self.repo} doesn't look like a SadTalker checkout "
                "(missing inference.py)"
            )
        ckpt = self.repo / "checkpoints"
        if not ckpt.is_dir() or not any(ckpt.iterdir()):
            raise BackendError(
                f"SadTalker checkpoints missing under {ckpt}; run "
                "`bash scripts/download_models.sh` in the SadTalker repo"
            )
        if shutil.which(self.python) is None and not Path(self.python).exists():
            raise BackendError(
                f"SadTalker python not found: {self.python!r} "
                "(set SADTALKER_PYTHON)"
            )

    def generate(self, face_image: Path, audio_file: Path,
                 out_path: Path, workdir: Path) -> Path:
        result_dir = workdir / f"sadtalker_{out_path.stem}"
        result_dir.mkdir(parents=True, exist_ok=True)

        cmd = [self.python, "inference.py",
               "--source_image", face_image.resolve(),
               "--driven_audio", audio_file.resolve(),
               "--result_dir", result_dir.resolve(),
               "--preprocess", self.preprocess,
               *self.extra_args]
        env = {**os.environ,
               # pickled checkpoints predate torch 2.6's weights_only default
               "TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD": "1",
               # a few facerender ops still fall back to CPU on Apple Silicon
               "PYTORCH_ENABLE_MPS_FALLBACK": "1"}
        self._run(cmd, cwd=self.repo, env=env,
                  what=f"SadTalker inference for {face_image.name}")

        produced = self._newest_mp4(result_dir, "SadTalker")
        shutil.copy2(produced, out_path)
        return out_path
