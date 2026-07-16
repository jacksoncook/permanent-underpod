"""LivePortrait backend — stub.

LivePortrait (https://github.com/KwaiVGI/LivePortrait) is a *reenactment*
model: it animates a source image from a DRIVING VIDEO (or a pre-extracted
motion template), not directly from audio. Wiring it in means pairing it
with an audio-to-motion stage, e.g.:

  1. generate mouth/head motion from audio with a cheap model
     (SadTalker's coefficients, or a recorded "driving" clip of yourself
     talking), then
  2. run LivePortrait: `python inference.py -s face.png -d driving.mp4`
     inside LIVEPORTRAIT_DIR and pick up the output mp4.

The subclass below keeps the registry slot and shows exactly what to
implement — mirror sadtalker.py's subprocess pattern.
"""

from __future__ import annotations

from pathlib import Path

from .base import BackendError, TalkingHeadBackend


class LivePortraitBackend(TalkingHeadBackend):
    name = "liveportrait"

    def check_available(self) -> None:
        raise BackendError(
            "the LivePortrait backend is a stub: LivePortrait is driven by "
            "a motion video, not audio, so it needs an audio-to-motion "
            "front end first. Use --backend musetalk or --backend sadtalker, "
            "or implement generate() in panelkit/backends/liveportrait.py "
            "(see the module docstring for the plan)."
        )

    def generate(self, face_image: Path, audio_file: Path,
                 out_path: Path, workdir: Path) -> Path:
        raise BackendError("LivePortrait backend not implemented")
