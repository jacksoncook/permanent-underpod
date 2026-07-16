"""End-to-end orchestration: config -> per-turn clips -> composed final.mp4.

Intermediates land in <workdir>/intermediate/:
  audio/   per-turn wavs (sliced/converted, 48 kHz stereo)
  talk/    raw backend output, cached by content hash of (face, audio, backend)
  norm/    normalized clips (fps/height/loudness uniform)
  idle/    per-speaker idle loops
  turns/   per-turn composed segments
  jobs/    backend scratch (model configs, raw result dirs)
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from . import compose
from .backends import get_backend
from .config import Script, Turn, load_script
from .media import (MediaError, duration, extract_audio_wav,
                    make_silence_wav, require_tools, validate_audio,
                    validate_image)

LAYOUTS = ("panel", "active-speaker")


def _hash_inputs(face: Path, audio: Path, backend_name: str) -> str:
    h = hashlib.sha1()
    h.update(backend_name.encode())
    for p in (face, audio):
        h.update(p.read_bytes())
    return h.hexdigest()[:10]


def _log(msg: str) -> None:
    print(msg, flush=True)


def build(config_path: Path, layout: str, out_path: Path, workdir: Path,
          backend_name: str = "musetalk", idle_mode: str = "loop",
          force: bool = False) -> Path:
    if layout not in LAYOUTS:
        raise ValueError(f"layout must be one of {LAYOUTS}, got {layout!r}")
    if idle_mode not in ("silence", "loop", "still"):
        raise ValueError(
            f"idle_mode must be 'silence', 'loop' or 'still', got {idle_mode!r}")

    require_tools()
    script: Script = load_script(config_path)
    backend = get_backend(backend_name)
    backend.check_available()

    inter = Path(workdir) / "intermediate"
    dirs = {name: inter / name
            for name in ("audio", "talk", "norm", "idle", "turns", "jobs")}
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # ---- validate all inputs up front, so failures are early and clear ----
    _log(f"[1/5] validating inputs ({len(script.speakers)} speakers, "
         f"{len(script.turns)} turns)")
    for sp in script.speakers:
        validate_image(sp.face_image, f"speaker {sp.name!r}")
    for t in script.turns:
        validate_audio(t.audio_source, f"turn {t.index} ({t.speaker.name})")

    spoken = {t.speaker.name for t in script.turns}
    silent = [sp.name for sp in script.speakers if sp.name not in spoken]
    if silent and layout == "panel":
        _log(f"      note: {', '.join(silent)} never speak(s); "
             "their tile will use a still-image idle")

    # ---- per-turn audio + talking-head generation ----
    _log(f"[2/5] generating talking heads (backend: {backend.name})")
    norm_clips: dict[int, Path] = {}          # turn index -> normalized clip
    first_norm_by_speaker: dict[str, Path] = {}
    for t in script.turns:
        tag = f"turn{t.index:02d}_{t.speaker.name}"
        wav = extract_audio_wav(t.audio_source, dirs["audio"] / f"{tag}.wav",
                                t.start, t.end)
        key = _hash_inputs(t.speaker.face_image, wav, backend.name)
        raw = dirs["talk"] / f"{tag}_{key}.mp4"
        if raw.exists() and not force:
            _log(f"      {tag}: cached ({raw.name})")
        else:
            _log(f"      {tag}: {duration(wav):.1f}s of audio -> {raw.name}")
            try:
                backend.generate(t.speaker.face_image, wav, raw, dirs["jobs"])
            except Exception:
                raw.unlink(missing_ok=True)  # never leave a half-written cache hit
                raise
        norm = compose.normalize_clip(raw, wav, dirs["norm"] / f"{tag}.mp4")
        norm_clips[t.index] = norm
        first_norm_by_speaker.setdefault(t.speaker.name, norm)

    # ---- idle loops (panel layout only) ----
    idle_by_speaker: dict[str, Path] = {}
    if layout == "panel":
        _log(f"[3/5] building idle loops (mode: {idle_mode})")
        silence_wav = None
        for sp in script.speakers:
            idle = dirs["idle"] / f"{sp.name}_{idle_mode}.mp4"
            src_clip = first_norm_by_speaker.get(sp.name)
            if idle_mode == "silence":
                # Generate a real not-talking clip: run the backend on
                # near-silence so the mouth stays neutral but the head still
                # moves naturally. Boomeranging a *talking* clip (old 'loop'
                # mode) makes everyone's mouth flap while others speak.
                if silence_wav is None:
                    silence_wav = make_silence_wav(
                        dirs["audio"] / "_idle_silence.wav", seconds=4.0)
                key = _hash_inputs(sp.face_image, silence_wav, backend.name)
                raw = dirs["talk"] / f"idle_{sp.name}_{key}.mp4"
                if raw.exists() and not force:
                    _log(f"      idle {sp.name}: cached ({raw.name})")
                else:
                    _log(f"      idle {sp.name}: generating from silence")
                    try:
                        backend.generate(sp.face_image, silence_wav, raw,
                                         dirs["jobs"])
                    except Exception:
                        raw.unlink(missing_ok=True)
                        raise
                compose.idle_from_clip(raw, idle, seg=3.8)
            elif idle_mode == "loop" and src_clip is not None:
                compose.idle_from_clip(src_clip, idle, seg=1.6)
            else:
                compose.idle_from_image(src_clip or sp.face_image, idle,
                                        dirs["jobs"])
            idle_by_speaker[sp.name] = idle
    else:
        _log("[3/5] idle loops: skipped (active-speaker layout)")

    # ---- compose each turn ----
    _log(f"[4/5] composing turns ({layout})")
    turn_files: list[Path] = []
    for t in script.turns:
        seg = dirs["turns"] / f"{layout}_turn{t.index:02d}.mp4"
        if layout == "panel":
            compose.compose_panel_turn(
                active_clip=norm_clips[t.index],
                active_pos=script.speaker_index(t.speaker),
                idle_clips=[idle_by_speaker[sp.name] for sp in script.speakers],
                display_names=[sp.display_name for sp in script.speakers],
                out=seg)
        else:
            compose.compose_active_turn(norm_clips[t.index],
                                        t.speaker.display_name, seg)
        turn_files.append(seg)

    # ---- final concat ----
    _log("[5/5] concatenating final video")
    compose.concat(turn_files, out_path, inter)
    total = duration(out_path)
    _log(f"done: {out_path} ({total:.1f}s, {len(turn_files)} turns)")
    _log(f"intermediates kept in {inter}")
    return out_path
