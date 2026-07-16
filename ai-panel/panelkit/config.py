"""Load and validate script.json.

Two supported shapes:

1. Per-speaker audio (simplest — each speaker's full speech in one file;
   speakers talk in listed order):

   {
     "speakers": [
       {"name": "jackson", "display_name": "Jackson",
        "face_image": "faces/jackson.jpg", "audio_file": "audio/jackson.wav"},
       ...
     ]
   }

2. One master audio file + a timed timeline of speaking turns
   (script + single audio + person assignments):

   {
     "audio_file": "audio/full_conversation.wav",
     "speakers": [
       {"name": "jackson", "face_image": "faces/jackson.jpg"},
       ...
     ],
     "timeline": [
       {"speaker": "jackson", "start": 0.0,  "end": 12.5},
       {"speaker": "chris",   "start": 12.5, "end": 31.0},
       ...
     ]
   }

Timeline entries may also carry their own "audio_file" (with optional
start/end) to override both of the above per turn.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

MAX_SPEAKERS = 4  # panel layout is a single row of tiles


class ConfigError(ValueError):
    pass


@dataclass
class Speaker:
    name: str
    display_name: str
    face_image: Path
    audio_file: Path | None = None


@dataclass
class Turn:
    index: int
    speaker: Speaker
    audio_source: Path
    start: float | None = None
    end: float | None = None


@dataclass
class Script:
    speakers: list = field(default_factory=list)
    turns: list = field(default_factory=list)
    base_dir: Path = Path(".")

    def speaker_index(self, speaker: Speaker) -> int:
        return self.speakers.index(speaker)


def _resolve(base: Path, p) -> Path:
    p = Path(str(p)).expanduser()
    return p if p.is_absolute() else (base / p).resolve()


def _parse_time(entry: dict, key: str, where: str) -> float | None:
    if key not in entry:
        return None
    try:
        val = float(entry[key])
    except (TypeError, ValueError):
        raise ConfigError(f"{where}: '{key}' must be a number, got {entry[key]!r}")
    if val < 0:
        raise ConfigError(f"{where}: '{key}' must be >= 0")
    return val


def load_script(config_path: Path) -> Script:
    config_path = Path(config_path)
    if not config_path.is_file():
        raise ConfigError(f"config file not found: {config_path}")
    try:
        raw = json.loads(config_path.read_text())
    except json.JSONDecodeError as e:
        raise ConfigError(f"{config_path} is not valid JSON: {e}")
    if not isinstance(raw, dict):
        raise ConfigError(f"{config_path}: top level must be a JSON object")

    base = config_path.parent.resolve()

    speakers_raw = raw.get("speakers")
    if not isinstance(speakers_raw, list) or not speakers_raw:
        raise ConfigError(f"{config_path}: 'speakers' must be a non-empty list")
    if len(speakers_raw) > MAX_SPEAKERS:
        raise ConfigError(
            f"{config_path}: at most {MAX_SPEAKERS} speakers supported "
            f"(got {len(speakers_raw)})"
        )

    speakers: list[Speaker] = []
    by_name: dict[str, Speaker] = {}
    for i, s in enumerate(speakers_raw):
        where = f"speakers[{i}]"
        if not isinstance(s, dict):
            raise ConfigError(f"{where}: must be an object")
        name = str(s.get("name", "")).strip()
        if not name:
            raise ConfigError(f"{where}: 'name' is required")
        if name in by_name:
            raise ConfigError(f"{where}: duplicate speaker name {name!r}")
        if "face_image" not in s:
            raise ConfigError(f"{where} ({name}): 'face_image' is required")
        sp = Speaker(
            name=name,
            display_name=str(s.get("display_name") or name.title()),
            face_image=_resolve(base, s["face_image"]),
            audio_file=_resolve(base, s["audio_file"]) if s.get("audio_file") else None,
        )
        speakers.append(sp)
        by_name[name] = sp

    master_audio = _resolve(base, raw["audio_file"]) if raw.get("audio_file") else None

    timeline_raw = raw.get("timeline")
    turns: list[Turn] = []

    if timeline_raw is None:
        # Default: one turn per speaker, in listed order, whole audio file.
        for sp in speakers:
            if sp.audio_file is None:
                raise ConfigError(
                    f"speaker {sp.name!r} has no 'audio_file' and no 'timeline' "
                    "was given — either give every speaker an audio_file, or "
                    "provide a top-level audio_file + timed timeline"
                )
            turns.append(Turn(index=len(turns), speaker=sp,
                              audio_source=sp.audio_file))
    else:
        if not isinstance(timeline_raw, list) or not timeline_raw:
            raise ConfigError("'timeline' must be a non-empty list")
        for i, t in enumerate(timeline_raw):
            where = f"timeline[{i}]"
            if not isinstance(t, dict):
                raise ConfigError(f"{where}: must be an object")
            sp = by_name.get(str(t.get("speaker", "")).strip())
            if sp is None:
                raise ConfigError(
                    f"{where}: 'speaker' must be one of "
                    f"{sorted(by_name)} (got {t.get('speaker')!r})"
                )
            start = _parse_time(t, "start", where)
            end = _parse_time(t, "end", where)
            if (start is None) != (end is None):
                raise ConfigError(f"{where}: give both 'start' and 'end', or neither")
            if start is not None and end <= start:
                raise ConfigError(f"{where}: 'end' must be greater than 'start'")

            if t.get("audio_file"):
                src = _resolve(base, t["audio_file"])
            elif master_audio is not None:
                if start is None:
                    raise ConfigError(
                        f"{where}: turns over the master audio_file need "
                        "'start' and 'end'"
                    )
                src = master_audio
            elif sp.audio_file is not None:
                src = sp.audio_file
            else:
                raise ConfigError(
                    f"{where}: no audio for this turn — give the turn an "
                    f"'audio_file', or speaker {sp.name!r} an 'audio_file', "
                    "or a top-level master 'audio_file'"
                )
            turns.append(Turn(index=i, speaker=sp, audio_source=src,
                              start=start, end=end))

    return Script(speakers=speakers, turns=turns, base_dir=base)
