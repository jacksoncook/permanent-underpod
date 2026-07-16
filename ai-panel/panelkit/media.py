"""ffmpeg / ffprobe helpers shared by the whole pipeline."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

FFMPEG = "ffmpeg"
FFPROBE = "ffprobe"

# One consistent encode everywhere so the final concat never has to fight
# mismatched codec parameters.
ENC_VIDEO = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
             "-pix_fmt", "yuv420p"]
ENC_AUDIO = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

FPS = 25


class MediaError(RuntimeError):
    """An ffmpeg/ffprobe invocation or media validation failed."""


def require_tools() -> None:
    missing = [t for t in (FFMPEG, FFPROBE) if shutil.which(t) is None]
    if missing:
        raise MediaError(
            f"required tool(s) not on PATH: {', '.join(missing)}. "
            "Install ffmpeg — macOS: `brew install ffmpeg`, "
            "Debian/Ubuntu: `sudo apt install ffmpeg`."
        )


def run(cmd: list, what: str) -> subprocess.CompletedProcess:
    """Run a command, raising MediaError with the stderr tail on failure."""
    cmd = [str(c) for c in cmd]
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, text=True)
    except OSError as e:
        raise MediaError(f"{what}: could not launch {cmd[0]!r}: {e}") from e
    if proc.returncode != 0:
        tail = "\n".join(proc.stderr.strip().splitlines()[-15:])
        raise MediaError(
            f"{what} failed (exit {proc.returncode}).\n"
            f"  command: {' '.join(cmd)}\n"
            f"  stderr tail:\n{tail}"
        )
    return proc


_FILTERS: set | None = None


def has_filter(name: str) -> bool:
    """Some builds (e.g. Homebrew's default ffmpeg) omit filters like
    drawtext (needs libfreetype) — degrade instead of failing."""
    global _FILTERS
    if _FILTERS is None:
        proc = run([FFMPEG, "-hide_banner", "-filters"], "listing ffmpeg filters")
        _FILTERS = {line.split()[1] for line in proc.stdout.splitlines()
                    if len(line.split()) > 2 and line.startswith(" ")}
    return name in _FILTERS


def probe(path: Path) -> dict:
    proc = run([FFPROBE, "-v", "error", "-print_format", "json",
                "-show_format", "-show_streams", path],
               f"probing {path}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise MediaError(f"ffprobe returned unparseable JSON for {path}") from e


def duration(path: Path) -> float:
    info = probe(path)
    dur = info.get("format", {}).get("duration")
    if dur is None:
        # Fall back to the longest stream duration (e.g. some containers).
        durs = [float(s["duration"]) for s in info.get("streams", [])
                if "duration" in s]
        if not durs:
            raise MediaError(f"could not determine duration of {path}")
        return max(durs)
    return float(dur)


def has_stream(path: Path, kind: str) -> bool:
    info = probe(path)
    return any(s.get("codec_type") == kind for s in info.get("streams", []))


def validate_image(path: Path, label: str) -> None:
    if not path.is_file():
        raise MediaError(f"{label}: face image not found: {path}")
    if not has_stream(path, "video"):
        raise MediaError(f"{label}: {path} is not a decodable image")


def validate_audio(path: Path, label: str) -> None:
    if not path.is_file():
        raise MediaError(f"{label}: audio file not found: {path}")
    if not has_stream(path, "audio"):
        raise MediaError(
            f"{label}: {path} has no decodable audio stream "
            "(bad/unsupported format?)"
        )
    if duration(path) < 0.2:
        raise MediaError(f"{label}: {path} is shorter than 0.2s")


def make_silence_wav(out: Path, seconds: float = 4.0) -> Path:
    """Near-silence for generating idle (not-talking) clips. Very quiet pink
    noise rather than digital zeros so mel/log audio pipelines stay finite."""
    run([FFMPEG, "-y", "-f", "lavfi",
         "-i", f"anoisesrc=color=pink:amplitude=0.0005:duration={seconds}",
         "-ar", "48000", "-ac", "2", "-acodec", "pcm_s16le", out],
        "generating idle silence wav")
    return out


def extract_audio_wav(src: Path, out: Path,
                      start: float | None = None,
                      end: float | None = None) -> Path:
    """Slice/convert any audio source to a 48 kHz stereo PCM wav."""
    cmd = [FFMPEG, "-y", "-i", src]
    if start is not None:
        cmd += ["-ss", f"{start:.3f}"]  # after -i => sample-accurate
    if end is not None:
        cmd += ["-to", f"{end:.3f}"]
    cmd += ["-vn", "-acodec", "pcm_s16le", "-ar", "48000", "-ac", "2", out]
    run(cmd, f"extracting audio to {out.name}")
    return out
