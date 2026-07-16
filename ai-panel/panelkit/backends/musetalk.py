"""MuseTalk backend (https://github.com/TMElyralab/MuseTalk).

Wraps a separate MuseTalk checkout via subprocess so its heavy torch
environment stays isolated from this tool. Configure with env vars:

  MUSETALK_DIR         path to the cloned MuseTalk repo (required)
  MUSETALK_PYTHON      python interpreter of MuseTalk's env
                       (default: $MUSETALK_DIR/.venv/bin/python if present,
                        else "python3")
  MUSETALK_VERSION     "v15" (default, MuseTalk 1.5) or "v1"
  MUSETALK_EXTRA_ARGS  extra CLI args appended verbatim, e.g.
                       "--bbox_shift -7" (shlex-split)

MuseTalk lip-syncs a source image/video; from a still image the head itself
stays static (mouth-only motion) — the pipeline's idle/still handling and
SadTalker (which generates head pose) cover the "natural head movement" case.
"""

from __future__ import annotations

import os
import shlex
import shutil
from pathlib import Path

from .base import BackendError, TalkingHeadBackend

_WEIGHT_HINT = (
    "download weights per the MuseTalk README (sh ./download_weights.sh) — "
    "expects models/musetalkV15/unet.pth (v15) or models/musetalk/"
    "pytorch_model.bin (v1), plus whisper/vae/dwpose under models/"
)


class MuseTalkBackend(TalkingHeadBackend):
    name = "musetalk"

    def __init__(self) -> None:
        self.repo = Path(os.environ["MUSETALK_DIR"]).expanduser() \
            if os.environ.get("MUSETALK_DIR") else None
        self.version = os.environ.get("MUSETALK_VERSION", "v15")
        py = os.environ.get("MUSETALK_PYTHON")
        if not py and self.repo and (self.repo / ".venv/bin/python").exists():
            py = str(self.repo / ".venv/bin/python")
        self.python = py or "python3"
        self.extra_args = shlex.split(os.environ.get("MUSETALK_EXTRA_ARGS", ""))

    def _model_args(self) -> list:
        if self.version == "v15":
            return ["--version", "v15",
                    "--unet_model_path", "models/musetalkV15/unet.pth",
                    "--unet_config", "models/musetalkV15/musetalk.json"]
        if self.version == "v1":
            return ["--version", "v1",
                    "--unet_model_path", "models/musetalk/pytorch_model.bin",
                    "--unet_config", "models/musetalk/musetalk.json"]
        raise BackendError(f"MUSETALK_VERSION must be 'v15' or 'v1', got {self.version!r}")

    def check_available(self) -> None:
        if self.repo is None:
            raise BackendError(
                "MUSETALK_DIR is not set. Clone and set up MuseTalk "
                "(see README.md → 'MuseTalk setup'), then:\n"
                "  export MUSETALK_DIR=~/models/MuseTalk"
            )
        if not (self.repo / "scripts" / "inference.py").exists():
            raise BackendError(
                f"{self.repo} doesn't look like a MuseTalk checkout "
                "(missing scripts/inference.py)"
            )
        weight = self.repo / ("models/musetalkV15/unet.pth" if self.version == "v15"
                              else "models/musetalk/pytorch_model.bin")
        if not weight.exists():
            raise BackendError(f"MuseTalk weights missing ({weight}); {_WEIGHT_HINT}")
        if shutil.which(self.python) is None and not Path(self.python).exists():
            raise BackendError(
                f"MuseTalk python not found: {self.python!r} "
                "(set MUSETALK_PYTHON to the interpreter of MuseTalk's venv/conda env)"
            )

    def generate(self, face_image: Path, audio_file: Path,
                 out_path: Path, workdir: Path) -> Path:
        job = workdir / f"musetalk_{out_path.stem}"
        result_dir = job / "results"
        result_dir.mkdir(parents=True, exist_ok=True)

        # Inference config is a trivial YAML mapping; write it by hand to
        # avoid a pyyaml dependency.
        cfg = job / "inference.yaml"
        cfg.write_text(
            "task_0:\n"
            f'  video_path: "{face_image.resolve()}"\n'
            f'  audio_path: "{audio_file.resolve()}"\n'
        )

        cmd = [self.python, "-m", "scripts.inference",
               "--inference_config", cfg.resolve(),
               "--result_dir", result_dir.resolve(),
               *self._model_args(), *self.extra_args]
        self._run(cmd, cwd=self.repo,
                  what=f"MuseTalk inference for {face_image.name}")

        produced = self._newest_mp4(result_dir, "MuseTalk")
        shutil.copy2(produced, out_path)
        return out_path
