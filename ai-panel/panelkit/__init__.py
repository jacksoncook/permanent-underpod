"""panelkit — local talking-head panel pipeline.

Turns face images + voice audio into per-speaker lip-synced clips
(via a pluggable backend: MuseTalk / SadTalker / static test backend)
and composes them into a single multi-person panel video with ffmpeg.
"""

__version__ = "0.1.0"
