"""Static test backend — ffmpeg only, no ML.

Produces a video of the still face image with the audio muxed in (no lip
sync). Exists so the whole pipeline — config, slicing, normalization,
idle loops, panel/active-speaker composition — can be exercised end-to-end
in seconds on any machine, before any model weights are installed.
"""

from __future__ import annotations

from pathlib import Path

from .base import TalkingHeadBackend
from ..media import ENC_AUDIO, ENC_VIDEO, FFMPEG, FPS, duration, run


class StaticBackend(TalkingHeadBackend):
    name = "static"

    def check_available(self) -> None:
        pass  # only needs ffmpeg, which the pipeline already requires

    def generate(self, face_image: Path, audio_file: Path,
                 out_path: Path, workdir: Path) -> Path:
        dur = duration(audio_file)
        cmd = [FFMPEG, "-y",
               "-loop", "1", "-framerate", str(FPS), "-i", face_image,
               "-i", audio_file,
               "-t", f"{dur:.3f}",
               "-vf", ("scale=720:720:force_original_aspect_ratio=increase,"
                       f"crop=720:720,fps={FPS}"),
               *ENC_VIDEO, *ENC_AUDIO,
               out_path]
        run(cmd, f"static backend render for {face_image.name}")
        return out_path
