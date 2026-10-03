#!/usr/bin/env python3
"""Render a frame-exact gallery clip source with hard-cut vertical crop keys."""

import argparse
import json
import math
import os
import subprocess
import sys

import numpy as np

FPS = 30
SR = 48000
SPF = 1600
STEP = 0.01
WIDE = "wide"
WIDE_X = 437


def runs_of(tl):
    """Return contiguous timeline runs as start, end, value triples."""
    if len(tl) == 0:
        return []
    out = []
    start = 0
    for i in range(1, len(tl) + 1):
        if i == len(tl) or tl[i] != tl[start]:
            out.append([start, i, int(tl[start])])
            start = i
    return out


def sticky(acts):
    """Select an active person while retaining the current person when possible."""
    first = np.flatnonzero(acts.any(axis=0))
    person = int(np.flatnonzero(acts[:, first[0]])[0]) if len(first) else 0
    timeline = np.empty(acts.shape[1], dtype=int)
    for i in range(acts.shape[1]):
        if not acts[person, i]:
            others = np.flatnonzero(acts[:, i])
            if len(others):
                person = int(others[0])
        timeline[i] = person
    return timeline


def enforce_min(tl, acts, min_steps):
    """Absorb timeline runs without enough active speech into a neighbor."""
    timeline = tl.copy()
    while True:
        runs = runs_of(timeline)
        if len(runs) < 2:
            return timeline
        short = [
            (j, run)
            for j, run in enumerate(runs)
            if min(run[1] - run[0], int(acts[run[2], run[0]:run[1]].sum())) < min_steps
        ]
        if not short:
            return timeline
        j, (start, end, _) = min(short, key=lambda item: item[1][1] - item[1][0])
        timeline[start:end] = runs[j + 1][2] if j == 0 else runs[j - 1][2]


def keyed_timeline(keys, persons, lo, n, step):
    """Build a person-index timeline from absolute source-time keys."""
    parsed = sorted((float(t), person) for t, person in keys)
    timeline = np.zeros(n, dtype=int)
    for i, (time, person) in enumerate(parsed):
        start = max(0, int((time - lo) / step))
        end = n if i + 1 == len(parsed) else int((parsed[i + 1][0] - lo) / step)
        timeline[start:end] = persons.index(person)
    if parsed and parsed[0][0] > lo:
        timeline[:int((parsed[0][0] - lo) / step)] = persons.index(parsed[0][1])
    return timeline


def pieces_from_timeline(tl, persons, lo, hi, step):
    """Convert a person-index timeline to absolute source-time pieces."""
    pieces = [[lo + start * step, lo + end * step, persons[index]] for start, end, index in runs_of(tl)]
    if pieces:
        pieces[0][0] = lo
        pieces[-1][1] = hi
    return pieces


def snap_pieces(pieces, lo, hi, fps):
    """Snap interior piece boundaries to the frame grid anchored at lo."""
    if not pieces:
        return []
    edges = [lo]
    edges.extend(lo + round((piece[1] - lo) * fps) / fps for piece in pieces[:-1])
    edges.append(hi)
    return [[edges[i], edges[i + 1], piece[2]] for i, piece in enumerate(pieces) if edges[i + 1] > edges[i]]


def face_key_x(cx, frame_w=1280, col_w=406):
    """Center and clamp a vertical crop column around a face center."""
    return int(min(frame_w - col_w, max(0, cx - col_w // 2)))


def face_keys(files, start):
    """Build hard-cut face crop keys from rendered file records."""
    keys = []
    cumulative_frames = 0
    for record in files:
        x_left = record[5]
        time = round(max(0, cumulative_frames / FPS - start), 3)
        if not keys or keys[-1][1] != x_left:
            keys.append([time, x_left, "cut"])
        cumulative_frames += record[1]
    return keys


def nongrid_mask(src, badges, t0, nf, fps=30, blue_min=50):
    """Decode a window and return frames where any gallery badge is absent."""
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", src],
        capture_output=True,
        check=True,
        text=True,
    )
    width, height = map(int, probe.stdout.strip().split(","))
    decoded = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", f"{t0:.4f}", "-i", src, "-vf", f"fps={fps},scale=192:108", "-frames:v", str(nf), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True,
        check=True,
    ).stdout
    frame_bytes = 192 * 108 * 3
    if len(decoded) != nf * frame_bytes:
        raise RuntimeError(f"badge decode returned {len(decoded) // frame_bytes} of {nf} frames")
    frames = np.frombuffer(decoded, np.uint8).reshape(nf, 108, 192, 3)
    nongrid = np.zeros(nf, dtype=bool)
    sx, sy = 192 / width, 108 / height
    for x, y, w, h in badges.values():
        x0, y0 = int(x * sx), int(y * sy)
        x1, y1 = max(x0 + 1, int((x + w) * sx)), max(y0 + 1, int((y + h) * sy))
        patch = frames[:, y0:y1, x0:x1, :]
        blue = patch[..., 2].mean(axis=(1, 2)) - patch[..., 0].mean(axis=(1, 2))
        nongrid |= blue <= blue_min
    return nongrid


def refine_spans(coarse, lo, hi, mask_fn, fps=30, slack=0.75):
    """Refine coarse spans on the frame grid anchored at lo."""
    refined = []
    for start, end in coarse:
        if end <= lo or start >= hi:
            continue
        k0 = math.floor((max(lo, start - slack) - lo) * fps)
        k1 = math.ceil((min(hi, end + slack) - lo) * fps)
        t0 = lo + k0 / fps
        nf = k1 - k0
        mask = np.asarray(mask_fn(t0, nf), dtype=bool)
        if len(mask) != nf:
            raise ValueError(f"mask returned {len(mask)} values for {nf} frames")
        found = np.flatnonzero(mask)
        if not len(found):
            continue
        a = max(lo, lo + (k0 + int(found[0])) / fps)
        b = min(hi, lo + (k0 + int(found[-1]) + 1) / fps)
        if b > a:
            refined.append([a, b])
    return refined


def pad_span_leads(spans, lo, lead_frames, fps=30):
    """Move span starts earlier by whole frames without crossing the lower bound."""
    return [[max(lo, start - lead_frames / fps), end] for start, end in spans]


def split_at_spans(pieces, spans):
    """Split pieces at span edges and label intersecting intervals wide."""
    if not spans:
        return [list(piece) for piece in pieces if piece[1] > piece[0]]
    edges = sorted({edge for piece in pieces for edge in piece[:2]} | {edge for span in spans for edge in span})
    out = []
    for piece_start, piece_end, who in pieces:
        local = [piece_start] + [edge for edge in edges if piece_start < edge < piece_end] + [piece_end]
        for start, end in zip(local, local[1:]):
            if end <= start:
                continue
            label = WIDE if any(min(end, b) > max(start, a) for a, b in spans) else who
            if out and label == WIDE and out[-1][2] == WIDE and out[-1][1] == start:
                out[-1][1] = end
            else:
                out.append([start, end, label])
    return out


def tile_overlaps(pieces, spans, fps):
    """Return the first non-wide span overlap of at least one frame."""
    for piece_start, piece_end, who in pieces:
        if who == WIDE:
            continue
        for span_start, span_end in spans:
            overlap = min(piece_end, span_end) - max(piece_start, span_start)
            if overlap * fps >= 1 - 1e-9:
                return [piece_start, piece_end, who, span_start, span_end]
    return None


def _parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("work")
    parser.add_argument("plan")
    parser.add_argument("name")
    parser.add_argument("src_start", type=float)
    parser.add_argument("src_end", type=float)
    parser.add_argument("--pad", type=float, default=1.0)
    parser.add_argument("--min-shot", type=float, default=1.5)
    parser.add_argument("--keys")
    parser.add_argument("--start", type=float)
    parser.add_argument("--end", type=float)
    parser.add_argument("--wide-hold", action="store_true")
    parser.add_argument("--lead-frames", type=int, default=0)
    args = parser.parse_args(argv)
    if args.lead_frames < 0:
        parser.error("--lead-frames must be nonnegative")
    return args


def main(argv=None):
    """Render one gallery clip source and print its clips.json entry."""
    args = _parse_args(argv)
    plan = json.load(open(args.plan))
    src = plan["source"]
    gallery = plan["gallery"]
    tiles = gallery["tiles"]
    speech = json.load(open(os.path.join(args.work, "speech.json")))
    lo, hi = args.src_start - args.pad, args.src_end + args.pad
    actual_start = args.pad if args.start is None else args.start
    actual_end = args.pad + args.src_end - args.src_start if args.end is None else args.end
    persons = [person for person in tiles if person in speech["spans"]]
    nsteps = int(round((hi - lo) / STEP))
    acts = np.zeros((len(persons), nsteps), dtype=bool)
    for k, person in enumerate(persons):
        for start, end in speech["spans"][person]:
            s, e = int((start - lo) / STEP), int((end - lo) / STEP)
            if e > 0 and s < nsteps:
                acts[k, max(0, s):min(nsteps, e)] = True
    if args.keys:
        keys = [item.split(":", 1) for item in args.keys.split(",")]
        timeline = keyed_timeline(keys, persons, lo, nsteps, STEP)
    else:
        timeline = enforce_min(sticky(acts), acts, int(args.min_shot / STEP))
    pieces = snap_pieces(pieces_from_timeline(timeline, persons, lo, hi, STEP), lo, hi, FPS)
    speaker_pieces = [list(piece) for piece in pieces]
    badges = gallery.get("badges")
    spans = []
    if badges:
        layout_path = os.path.join(args.work, "layout.json")
        if not os.path.exists(layout_path):
            raise SystemExit("gallery.badges is set but layout.json is missing: run gallery_layout.py first")
        coarse = json.load(open(layout_path))["other_spans"]
        spans = refine_spans(coarse, lo, hi, lambda t0, nf: nongrid_mask(src, badges, t0, nf, FPS, gallery.get("blue_min", 50)))
        spans = pad_span_leads(spans, lo, args.lead_frames, FPS)
        pieces = split_at_spans(pieces, spans)
        offender = tile_overlaps(pieces, spans, FPS)
        if offender is not None:
            raise SystemExit(f"tile crop overlaps non-grid span: {offender}")
    out_dir = os.path.join(args.work, "clipsrc")
    os.makedirs(out_dir, exist_ok=True)
    facex = os.path.join(args.work, "facex")
    if any(piece[2] != WIDE for piece in pieces) and not os.path.exists(facex):
        subprocess.run(["swiftc", "-O", os.path.join(os.path.dirname(os.path.abspath(__file__)), "facex.swift"), "-o", facex], check=True)
    defaults = {"chris": 420, "jackson": 600, "tyler": 700}
    files = []
    for i, (pa, pz, who) in enumerate(pieces):
        nframes = max(1, round((pz - pa) * FPS))
        path = os.path.join(out_dir, f"_{args.name}_{i:02d}.mov")
        if who == WIDE:
            if args.wide_hold:
                vf = f"fps={FPS},select=eq(n\\,{nframes // 2}),setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={nframes / FPS:.4f},scale=1280:720:flags=lanczos,format=yuv420p"
            else:
                vf = f"fps={FPS},scale=1280:720:flags=lanczos,format=yuv420p"
        else:
            x, y, w, h = tiles[who]
            vf = f"fps={FPS},crop={w}:{h}:{x}:{y},scale=1280:720:flags=lanczos,format=yuv420p"
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{pa:.4f}", "-i", src, "-vf", vf, "-frames:v", str(nframes), "-af", f"aresample={SR},apad,atrim=end_sample={nframes * SPF}", "-video_track_timescale", "30000", "-c:v", "h264_videotoolbox", "-b:v", "12M", "-c:a", "pcm_s16le", "-ar", str(SR), "-ac", "1", path], check=True)
        if who == WIDE:
            x_left = WIDE_X
        else:
            png = os.path.join(out_dir, f"_{args.name}_face_{i:02d}.png")
            original = next(piece for piece in speaker_pieces if piece[0] <= pa < piece[1] and piece[2] == who)
            x, y, w, h = tiles[who]
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{(original[0] + original[1]) / 2:.4f}", "-i", src, "-vf", f"crop={w}:{h}:{x}:{y},scale=1280:720:flags=lanczos", "-frames:v", "1", png], check=True)
            result = subprocess.run([facex, png], capture_output=True, text=True, check=True).stdout.split()
            cx = int(result[0]) if result else defaults.get(who, 640)
            x_left = face_key_x(cx)
            os.remove(png)
        files.append((path, nframes, who, pa, pz, x_left))
    concat_txt = os.path.join(out_dir, f"_{args.name}_concat.txt")
    with open(concat_txt, "w") as handle:
        for path, *_ in files:
            handle.write(f"file '{os.path.abspath(path)}'\n")
    raw = os.path.join(out_dir, f"_{args.name}_audio.raw")
    with open(raw, "wb") as output:
        for path, nframes, *_ in files:
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-map", "0:a", "-af", f"apad,atrim=end_sample={nframes * SPF}", "-f", "s16le", "-acodec", "pcm_s16le", "-ar", str(SR), "-ac", "1", "-"], stdout=output, check=True)
    video = os.path.join(out_dir, f"_{args.name}_video.mov")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", concat_txt, "-an", "-vf", f"setpts=N/{FPS}/TB", "-fps_mode", "passthrough", "-video_track_timescale", "30000", "-c:v", "h264_videotoolbox", "-b:v", "12M", video], check=True)
    out_mov = os.path.join(out_dir, f"{args.name}.mov")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", raw, "-c:v", "copy", "-c:a", "pcm_s16le", out_mov], check=True)
    for path, *_ in files:
        os.remove(path)
    for path in (concat_txt, raw, video):
        if os.path.exists(path):
            os.remove(path)
    entry = {"name": args.name, "source": out_mov, "start": actual_start, "end": actual_end, "vertical": True, "face_crops": face_keys(files, actual_start)}
    print(json.dumps(entry))
    print("pieces:", " | ".join(f"{pa:.2f}-{pz:.2f} {who}" for _, _, who, pa, pz, _ in files), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
