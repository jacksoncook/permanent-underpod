"""Backend contract: face image + audio -> talking-head video clip.

To add a backend, subclass TalkingHeadBackend, implement check_available()
and generate(), and register it in backends/__init__.py. The pipeline
normalizes whatever generate() returns (resolution / fps / loudness), so
backends only need to produce *some* mp4 with the mouth synced to the audio.
"""

from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod
from pathlib import Path


class BackendError(RuntimeError):
    """Backend unavailable or generation failed."""


class TalkingHeadBackend(ABC):
    #: registry key, e.g. "musetalk"
    name: str = "?"

    @abstractmethod
    def check_available(self) -> None:
        """Raise BackendError (with install/setup hints) if this backend
        cannot run on this machine right now."""

    @abstractmethod
    def generate(self, face_image: Path, audio_file: Path,
                 out_path: Path, workdir: Path) -> Path:
        """Produce a talking-head mp4 at out_path from one face image and
        one audio file. workdir is a scratch dir this backend may use for
        job files. Returns out_path. Raises BackendError on failure."""

    # ---- shared helper for subprocess-wrapping backends ----
    @staticmethod
    def _run(cmd: list, cwd: Path | None, what: str,
             env: dict | None = None) -> None:
        cmd = [str(c) for c in cmd]
        try:
            proc = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, text=True, env=env)
        except OSError as e:
            raise BackendError(f"{what}: could not launch {cmd[0]!r}: {e}") from e
        if proc.returncode != 0:
            tail = "\n".join(proc.stdout.strip().splitlines()[-25:])
            raise BackendError(
                f"{what} failed (exit {proc.returncode}).\n"
                f"  command: {' '.join(cmd)}\n"
                f"  output tail:\n{tail}"
            )

    @staticmethod
    def _newest_mp4(root: Path, what: str) -> Path:
        vids = sorted(root.rglob("*.mp4"), key=lambda p: p.stat().st_mtime)
        if not vids:
            raise BackendError(
                f"{what}: run finished but produced no .mp4 under {root}"
            )
        return vids[-1]
