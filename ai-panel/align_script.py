#!/usr/bin/env python3
"""Build a timed script.json from a speaker-labeled script + one audio file.

Pipeline: whisper-cli gives word-level timestamps for the audio; this aligns
those words against the script text (which the TTS read near-verbatim) and
derives start/end for every speaking turn.

Usage:
  ffmpeg -i talk.m4a -ar 16000 -ac 1 words.wav
  whisper-cli -m <ggml model> -f words.wav -ml 1 -sow -oj -of words
  python3 align_script.py --script script.md --words words.json \
      --audio talk.m4a --faces-dir faces/ --out script.json

Script format: turns as `**NAME:** text...` (markdown transcript style).
Face images are found as <faces-dir>/<name lowercased>.<png|jpg|jpeg|webp>.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

TURN_RE = re.compile(r"\*\*([A-Za-z ]+):\*\*(.*?)(?=\n\*\*[A-Za-z ]+:\*\*|\Z)",
                     re.S)


def tokens(text: str) -> list:
    return re.findall(r"[a-z0-9']+", text.lower())


def load_turns(script_path: Path) -> list:
    turns = [(m.group(1).strip().lower(), m.group(2).strip())
             for m in TURN_RE.finditer(script_path.read_text())]
    if not turns:
        sys.exit(f"error: no '**NAME:** text' turns found in {script_path}")
    return turns


def load_words(words_json: Path) -> list:
    """-> [(token, start_s, end_s)] from whisper-cli -ml 1 -sow -oj output."""
    data = json.loads(words_json.read_text())
    out = []
    for seg in data["transcription"]:
        t0 = seg["offsets"]["from"] / 1000.0
        t1 = seg["offsets"]["to"] / 1000.0
        for tok in tokens(seg["text"]):
            out.append((tok, t0, t1))
    if not out:
        sys.exit(f"error: no words in {words_json}")
    return out


def audio_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def align(turns: list, words: list, total: float) -> list:
    """-> [(speaker, start, end, coverage)] with contiguous boundaries."""
    script_tok, turn_of = [], []
    for i, (_, text) in enumerate(turns):
        for tok in tokens(text):
            script_tok.append(tok)
            turn_of.append(i)

    sm = difflib.SequenceMatcher(None, script_tok, [w for w, _, _ in words],
                                 autojunk=False)
    first = [None] * len(turns)
    last = [None] * len(turns)
    matched = [0] * len(turns)
    for a, b, size in sm.get_matching_blocks():
        for k in range(size):
            ti = turn_of[a + k]
            _, w0, w1 = words[b + k]
            if first[ti] is None or w0 < first[ti]:
                first[ti] = w0
            if last[ti] is None or w1 > last[ti]:
                last[ti] = w1
            matched[ti] += 1

    for i, (spk, text) in enumerate(turns):
        cov = matched[i] / max(1, len(tokens(text)))
        if first[i] is None:
            sys.exit(f"error: turn {i} ({spk}) matched no words — check that "
                     "the audio actually contains this script")
        if cov < 0.5:
            print(f"warning: turn {i} ({spk}) only {cov:.0%} matched",
                  file=sys.stderr)

    result = []
    for i, (spk, text) in enumerate(turns):
        start = 0.0 if i == 0 else (last[i - 1] + first[i]) / 2
        end = total if i == len(turns) - 1 else (last[i] + first[i + 1]) / 2
        if end <= start:
            sys.exit(f"error: turn {i} ({spk}) got non-positive duration "
                     f"[{start:.2f}, {end:.2f}] — alignment failed")
        result.append((spk, round(start, 3), round(end, 3),
                       matched[i] / max(1, len(tokens(text)))))
    return result


def find_face(faces_dir: Path, name: str) -> Path:
    for ext in ("png", "jpg", "jpeg", "webp"):
        p = faces_dir / f"{name}.{ext}"
        if p.exists():
            return p
    sys.exit(f"error: no face image for {name!r} in {faces_dir} "
             f"(looked for {name}.png/.jpg/.jpeg/.webp)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script", required=True, type=Path)
    ap.add_argument("--words", required=True, type=Path,
                    help="whisper-cli JSON (-ml 1 -sow -oj)")
    ap.add_argument("--audio", required=True, type=Path,
                    help="the master audio file (goes into script.json)")
    ap.add_argument("--faces-dir", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    turns = load_turns(args.script)
    words = load_words(args.words)
    total = audio_duration(args.audio)
    timeline = align(turns, words, total)

    base = args.out.parent.resolve()

    def rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(base))
        except ValueError:
            return str(p.resolve())

    speakers = []
    for name in dict.fromkeys(spk for spk, *_ in timeline):
        speakers.append({"name": name, "display_name": name.title(),
                         "face_image": rel(find_face(args.faces_dir, name))})

    cfg = {
        "audio_file": rel(args.audio),
        "speakers": speakers,
        "timeline": [{"speaker": spk, "start": s, "end": e}
                     for spk, s, e, _ in timeline],
    }
    args.out.write_text(json.dumps(cfg, indent=2) + "\n")

    print(f"{len(timeline)} turns over {total:.1f}s -> {args.out}")
    for i, (spk, s, e, cov) in enumerate(timeline):
        print(f"  {i:2d} {spk:<8s} {s:7.2f} - {e:7.2f}  ({e - s:5.1f}s, "
              f"{cov:.0%} matched)")


if __name__ == "__main__":
    main()
