"""Normalization, idle loops, and ffmpeg composition (panel / active-speaker)."""

from __future__ import annotations

from pathlib import Path

from .media import (ENC_AUDIO, ENC_VIDEO, FFMPEG, FPS, MediaError, duration,
                    has_filter, has_stream, run)

CANVAS_W, CANVAS_H = 1920, 1080
TILE_H = 720
BG = "0x0E0E14"
ACTIVE_BORDER = "0x4FD1C5"

_FONT_CANDIDATES = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
]


_warned_no_labels = False


def find_font() -> str | None:
    """Font for name labels, or None (label-less) if this ffmpeg build has
    no drawtext filter or no known font exists."""
    global _warned_no_labels
    if not has_filter("drawtext"):
        if not _warned_no_labels:
            print("      note: this ffmpeg build has no drawtext filter — "
                  "skipping name labels (brew: try ffmpeg with libfreetype, "
                  "e.g. `brew install ffmpeg` full build)", flush=True)
            _warned_no_labels = True
        return None
    for f in _FONT_CANDIDATES:
        if Path(f).exists():
            return f
    if not _warned_no_labels:
        print("      note: no usable font found — skipping name labels "
              "(see _FONT_CANDIDATES in panelkit/compose.py)", flush=True)
        _warned_no_labels = True
    return None


def _esc_drawtext(text: str) -> str:
    for ch in ("\\", ":", "'", "%"):
        text = text.replace(ch, "\\" + ch)
    return text


def _label_filter(font: str | None, text: str, fontsize: int, y: str) -> str:
    if not font:
        return ""
    return (f",drawtext=fontfile='{font}':text='{_esc_drawtext(text)}':"
            f"x=(w-text_w)/2:y={y}:fontsize={fontsize}:fontcolor=white:"
            "box=1:boxcolor=black@0.45:boxborderw=10")


def normalize_clip(raw_clip: Path, audio_wav: Path, out: Path) -> Path:
    """Uniform fps / height / codecs, and audio remuxed from the original
    turn wav (backends sometimes downsample audio) with loudness normalized
    to -16 LUFS."""
    cmd = [FFMPEG, "-y", "-i", raw_clip, "-i", audio_wav,
           "-map", "0:v:0", "-map", "1:a:0",
           "-vf", f"fps={FPS},scale=-2:{TILE_H}",
           "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000",
           "-shortest",
           *ENC_VIDEO, *ENC_AUDIO, out]
    run(cmd, f"normalizing {raw_clip.name}")
    return out


def idle_from_clip(clip: Path, out: Path, seg: float = 1.6) -> Path:
    """Boomerang (forward+reverse) loop of the clip's first `seg` seconds —
    keeps whatever natural head motion the backend generated, without a seam
    when stream-looped. Also normalizes fps/height so raw backend output can
    be fed directly (used for generated-from-silence idle clips)."""
    seg = max(0.4, min(seg, duration(clip) - 0.05))
    fc = (f"[0:v]trim=0:{seg:.3f},setpts=PTS-STARTPTS,fps={FPS},"
          f"scale=-2:{TILE_H},split[f][g];"
          "[g]reverse[r];[f][r]concat=n=2:v=1:a=0[v]")
    cmd = [FFMPEG, "-y", "-i", clip, "-filter_complex", fc,
           "-map", "[v]", "-an", *ENC_VIDEO, out]
    run(cmd, f"building idle loop from {clip.name}")
    return out


def idle_from_image(image_or_clip: Path, out: Path, workdir: Path) -> Path:
    """Subtle 'breathing' zoom on a still frame — used when a speaker has no
    generated clip yet, or with --idle-mode still (never shows silent lip
    movement)."""
    src = image_or_clip
    if src.suffix.lower() in (".mp4", ".mov", ".mkv", ".webm"):
        frame = workdir / f"{out.stem}_frame.png"
        run([FFMPEG, "-y", "-i", src, "-frames:v", "1", frame],
            f"extracting idle frame from {src.name}")
        src = frame
    vf = ("scale=1600:1600:force_original_aspect_ratio=increase,"
          "crop=1600:1600,"
          "zoompan=z='1.03+0.02*sin(2*PI*on/150)':"
          "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
          f"d=1:s={TILE_H}x{TILE_H}:fps={FPS}")
    cmd = [FFMPEG, "-y", "-loop", "1", "-framerate", str(FPS), "-t", "6",
           "-i", src, "-vf", vf, "-an", *ENC_VIDEO, out]
    run(cmd, f"building still idle from {src.name}")
    return out


def compose_panel_turn(active_clip: Path, active_pos: int,
                       idle_clips: list, display_names: list,
                       out: Path) -> Path:
    """One speaking turn on the full panel: the active speaker's clip in
    their tile (highlighted), everyone else's idle loop, single audio track
    from the active clip."""
    n = len(idle_clips)
    dur = duration(active_clip)
    tile_w = (CANVAS_W // n) & ~1  # even
    font = find_font()

    cmd = [FFMPEG, "-y"]
    for j in range(n):
        if j == active_pos:
            cmd += ["-i", active_clip]
        else:
            cmd += ["-stream_loop", "-1", "-i", idle_clips[j]]

    parts = []
    for j in range(n):
        chain = (f"[{j}:v]scale={tile_w}:{TILE_H}:"
                 f"force_original_aspect_ratio=increase,"
                 f"crop={tile_w}:{TILE_H},fps={FPS}")
        if j == active_pos:
            chain += (f",drawbox=x=3:y=3:w=iw-6:h=ih-6:"
                      f"color={ACTIVE_BORDER}@0.85:t=5")
        chain += _label_filter(font, display_names[j], 32, "h-58")
        parts.append(chain + f"[v{j}]")

    stack_in = "".join(f"[v{j}]" for j in range(n))
    if n > 1:
        parts.append(f"{stack_in}hstack=inputs={n}[row]")
    else:
        parts.append(f"{stack_in}null[row]")
    parts.append(f"[row]pad={CANVAS_W}:{CANVAS_H}:(ow-iw)/2:(oh-ih)/2:"
                 f"color={BG}[vout]")

    cmd += ["-filter_complex", ";".join(parts),
            "-map", "[vout]", "-map", f"{active_pos}:a:0",
            "-t", f"{dur:.3f}",
            *ENC_VIDEO, *ENC_AUDIO, out]
    run(cmd, f"composing panel turn -> {out.name}")
    return out


def compose_active_turn(active_clip: Path, display_name: str,
                        out: Path) -> Path:
    """One speaking turn, full frame, with a name lower-third."""
    font = find_font()
    vf = (f"scale={CANVAS_W}:{CANVAS_H}:force_original_aspect_ratio=decrease,"
          f"pad={CANVAS_W}:{CANVAS_H}:(ow-iw)/2:(oh-ih)/2:color={BG},"
          f"fps={FPS}")
    vf += _label_filter(font, display_name, 46, "h-120")
    cmd = [FFMPEG, "-y", "-i", active_clip, "-vf", vf,
           *ENC_VIDEO, *ENC_AUDIO, out]
    run(cmd, f"composing active-speaker turn -> {out.name}")
    return out


def concat(turn_files: list, out: Path, workdir: Path) -> Path:
    """Concat the per-turn segments. All segments come from the same encoder
    settings, so stream-copy first; fall back to a re-encode if the muxer
    objects."""
    listing = workdir / "concat.txt"
    listing.write_text("".join(
        "file '{}'\n".format(str(p.resolve()).replace("'", r"'\''"))
        for p in turn_files))
    base = [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", listing]
    try:
        run([*base, "-c", "copy", out], "concatenating turns (stream copy)")
    except MediaError:
        run([*base, *ENC_VIDEO, *ENC_AUDIO, out],
            "concatenating turns (re-encode)")
    if not has_stream(out, "video"):
        raise MediaError(f"concat produced no video stream in {out}")
    return out
