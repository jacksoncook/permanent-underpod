#!/usr/bin/env python3
"""Gate a clips.json BEFORE rendering (and the .mp4s after). Catches the two
defects that shipped on Ep 8 and were found by a human watching, not by tooling:

  1. a `face_crops` key that GLIDES between panels -> the "boomerang" artifact
  2. an in/out point that lands mid-word -> a clip that cuts someone off

usage:
  <venv>/bin/python verify_clips.py <clips.json> [options]      # needs numpy + ffmpeg
    --clip NAME       only this clip (repeatable)
    --whisper         also run word-level whisper at each boundary (slow, 2nd opinion)
    --rendered        also measure the finished mp4s in out_dir
    --envelope B      dump the raw 10 ms envelope around one boundary time and exit
                      (use this to calibrate --thr, or to eyeball a marginal call)
    --thr DB          override the silence threshold (default: -55, or -45 for a
                      mastered source — see "Thresholds" below)
    --lead S          silence wanted before an in-point   (default 0.20)
    --tail S          silence wanted after  an out-point  (default 0.10)

Exit code is 1 if anything FAILs, so this works as a pre-render gate:
  verify_clips.py clips.json && clipify.py clips.json

Thresholds
----------
FIXED thresholds only. Do NOT derive one from a percentile of the window: a window
containing digital silence gives a baseline near -174 dB and then EVERY frame reads
as speech. Defaults: -55 dB for an unmastered source (an episode's `edited_raw.mov`),
-45 dB for a mastered one (the final mp4 / `audio_chain: "anull"` / `style: "plain"`),
picked per clip. `--envelope` + `--thr` are the escape hatch for an odd source.

What "in a gap" means
---------------------
Speech-band RMS (highpass=200, lowpass=3500) in 10 ms frames; a "quiet run" is
>=80 ms continuously below the threshold. A boundary is OK only if it sits inside
one. Whisper CANNOT answer this question: its segments tile contiguously ACROSS
real pauses, so a cue edge is not a speech edge (on Ep 8 they were off by up to
6 s). `--whisper` uses word-level output (`--max-len 1 -sow`) as a second opinion;
where the two disagree the ENVELOPE wins — but read it raw before overriding, since
a stop consonant's closure looks like a short gap (Ep 8's short5: the dip at
2617.74 was the /p/ of "up"; the real gap was 2618.35).
"""
import json, os, subprocess, sys, wave

try:
    import numpy as np
except ImportError:
    sys.exit("verify_clips.py needs numpy — run it with a venv python "
             "(e.g. media/epN/work/.venv/bin/python), not bare system python3.")

ARGV = sys.argv[1:]
if not ARGV:
    sys.exit(__doc__)
SPEC_PATH = ARGV[0]
SPEC = json.load(open(SPEC_PATH))


def opt(flag, default=None, cast=str):
    return cast(ARGV[ARGV.index(flag) + 1]) if flag in ARGV else default


ONLY = [ARGV[i + 1] for i, a in enumerate(ARGV) if a == "--clip"]
DO_WHISPER = "--whisper" in ARGV
DO_RENDERED = "--rendered" in ARGV
ENVELOPE_AT = opt("--envelope", None, float)
THR_OVERRIDE = opt("--thr", None, float)
LEAD = opt("--lead", 0.20, float)
TAIL = opt("--tail", 0.10, float)

FPS, CW, FRAME_W = 30, 406, 1280
X_MAX = FRAME_W - CW                 # 874
SEAM_DX = 40                         # a move bigger than this leaves the panel
TRAIL_GUARD = 0.5                    # no crop switch in the last 0.5 s
MIN_QUIET = 8                        # frames (10 ms each) => 80 ms
WIN = 2.5                            # analysis half-window around a boundary
RENDER_EDGE_DB = 8.0                 # edge must sit this far below the clip body

OUTDIR = SPEC.get("out_dir", os.path.join(os.getcwd(), "clips"))
DEF_SRC = SPEC.get("source")
DEF_CHAIN = SPEC.get("audio_chain")
WHISPER = "/opt/homebrew/bin/whisper-cli"
MODEL = os.path.expanduser("~/.cache/whisper/ggml-small.en.bin")
SCRATCH = os.environ.get("TMPDIR", "/tmp").rstrip("/")

fails, warns = [], []


def ts(v):
    """Seconds from a number or 'H:MM:SS' / 'MM:SS' string (same as clipify.py)."""
    if isinstance(v, (int, float)):
        return float(v)
    s = 0.0
    for p in str(v).split(":"):
        s = s * 60 + float(p)
    return s


def envelope(src, t0, dur):
    """10 ms speech-band RMS envelope in dB. Returns (db array, actual t0)."""
    t0 = max(0.0, t0)
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", f"{t0:.3f}", "-t", f"{dur:.3f}", "-i", src,
         "-vn", "-ac", "1", "-ar", "16000",
         "-af", "highpass=f=200,lowpass=f=3500", "-f", "s16le", "-"],
        capture_output=True)
    x = np.frombuffer(p.stdout, dtype=np.int16).astype(np.float32) / 32768.0
    n = len(x) // 160
    if n == 0:
        return np.zeros(0), t0
    e = np.sqrt(np.mean(x[:n * 160].reshape(n, 160) ** 2, axis=1))
    return 20 * np.log10(np.maximum(e, 1e-9)), t0


def quiet_runs(db, thr):
    """[(start_frame, end_frame_exclusive)] for runs >= MIN_QUIET below thr."""
    runs, i, n = [], 0, len(db)
    while i < n:
        if db[i] < thr:
            j = i
            while j < n and db[j] < thr:
                j += 1
            if j - i >= MIN_QUIET:
                runs.append((i, j))
            i = j
        else:
            i += 1
    return runs


def word_at(src, b):
    """Word-level whisper around b -> the word straddling it, or None."""
    if not (os.path.exists(WHISPER) and os.path.exists(MODEL)):
        warns.append(f"--whisper asked for but {WHISPER} or the model is missing")
        return None
    base = f"{SCRATCH}/_vc_{b:.2f}".replace("-", "n")
    t0 = max(0.0, b - WIN)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.3f}",
                    "-t", f"{WIN * 2:.3f}", "-i", src, "-vn", "-ac", "1",
                    "-ar", "16000", base + ".wav"], check=True)
    subprocess.run([WHISPER, "-m", MODEL, "-f", base + ".wav", "--max-len", "1",
                    "-sow", "-ocsv", "-of", base],
                   capture_output=True, check=False)
    hit = None
    if os.path.exists(base + ".csv"):
        for line in open(base + ".csv").read().splitlines()[1:]:
            parts = line.split(",", 3)
            if len(parts) < 3:
                continue
            try:
                s, e = t0 + float(parts[0]) / 1000, t0 + float(parts[1]) / 1000
            except ValueError:
                continue
            txt = parts[-1].strip().strip('"')
            if s < b < e and txt:
                hit = (s, e, txt)
    for ext in (".wav", ".csv"):
        if os.path.exists(base + ext):
            os.remove(base + ext)
    return hit


def check_boundary(clip, kind, b, src, thr, clip_spec):
    """kind is 'in' or 'out'. Reports whether b lands in measured silence."""
    db, t0 = envelope(src, b - WIN, WIN * 2)
    if len(db) == 0:
        fails.append(f"{clip}: {kind}-point {b:.2f} — no audio decoded from {src}")
        return
    runs = quiet_runs(db, thr)
    i = int(round((b - t0) / 0.01))
    inside = next(((a, z) for a, z in runs if a - 1 <= i <= z + 1), None)
    at = db[min(max(i, 0), len(db) - 1)]

    if inside:
        a, z = inside
        margin = min(i - a, z - i) * 0.01
        print(f"  ok   {kind:3} {b:8.2f}  in a {(z-a)*0.01:.2f}s gap "
              f"({t0+a*0.01:.2f}-{t0+z*0.01:.2f}), {margin:.2f}s of room, "
              f"{at:.0f} dB")
        return

    # mid-speech: suggest the nearest usable gap
    if kind == "in":
        # want the gap that ENDS just before speech resumes
        cands = sorted(runs, key=lambda r: abs((t0 + r[1] * 0.01) - b))
        sug = (max(t0 + cands[0][0] * 0.01, t0 + cands[0][1] * 0.01 - LEAD)
               if cands else None)
    else:
        # want the gap that STARTS just after speech stops
        cands = sorted(runs, key=lambda r: abs((t0 + r[0] * 0.01) - b))
        sug = (min(t0 + cands[0][1] * 0.01, t0 + cands[0][0] * 0.01 + TAIL)
               if cands else None)
    # Diagnostics that let a human tell a chopped vowel from a word-complete
    # consonant tail: the 100 ms trend into the boundary, and the next onset.
    lo = max(0, i - 10)
    slope = at - float(db[lo]) if i > lo else 0.0
    nxt = next((t0 + j * 0.01 for j in range(i + 1, len(db)) if db[j] > thr + 15), None)
    trend = ("falling" if slope < -4 else "rising" if slope > 4 else "flat")
    msg = (f"{clip}: {kind}-point {b:.2f} is MID-SPEECH ({at:.0f} dB, thr {thr:.0f}; "
           f"{trend} {slope:+.0f} dB over the prior 100ms"
           + (f", next onset {nxt:.2f}" if nxt else "") + ")")
    msg += f" — try {sug:.2f}" if sug else " — no gap within ±2.5 s; widen the clip"
    if DO_WHISPER:
        w = word_at(src, b)
        if w:
            msg += f'  [whisper: cuts "{w[2]}" ({w[0]:.2f}-{w[1]:.2f})]'
    # A FALLING tail with no gap anywhere near can still be word-complete (the clip
    # ends on a decaying fricative and the next word starts immediately). That is a
    # real judgement call, so it is allowed — but only as a DECLARED override with a
    # written reason, so the next person sees it was decided, not missed:
    #   "verify_override": {"out": "ends on the decaying /f/ of 'wife'"}
    ov = (clip_spec.get("verify_override") or {}).get(kind)
    if ov and str(ov).strip():
        warns.append(msg + f"\n     OVERRIDDEN: {ov}")
        print(f"  WARN {kind:3} {b:8.2f}  mid-speech at {at:.0f} dB, overridden")
        return
    fails.append(msg)
    print(f"  FAIL {kind:3} {b:8.2f}  mid-speech at {at:.0f} dB ({trend} tail)")


def check_crops(clip, fcs, dur, swipe_set):
    """The boomerang gate. EVERY panel switch must be a hard cut."""
    if swipe_set:
        warns.append(f"{clip}: has a `swipe` duration set — it only affects "
                     f'"swipe" keys, which should not exist for panel switches')
    if float(fcs[0][0]) != 0.0:
        fails.append(f"{clip}: first face_crops key is at t={fcs[0][0]}, must be 0.0 "
                     f"(clipify uses key 0's x as the base, so a late first key "
                     f"silently shifts the whole schedule)")
    prev_t, prev_x = -1.0, None
    for k in fcs:
        t, x = float(k[0]), int(k[1])
        mode = (k[2] if len(k) > 2 else "cut").lower()
        if t <= prev_t:
            fails.append(f"{clip}: face_crops key t={t} is not after {prev_t} — "
                         f"clipify builds the x expression by walking keys in order")
        if not (0 <= x <= X_MAX):
            fails.append(f"{clip}: face_crops x={x} is outside 0..{X_MAX} "
                         f"(a {CW}px column of a {FRAME_W}px frame) — ffmpeg will clamp "
                         f"and the crop won't be where you think")
        dx = 0 if prev_x is None else x - prev_x
        if mode not in ("cut", "swipe"):
            fails.append(f"{clip}: face_crops mode {mode!r} at t={t} is neither "
                         f'"cut" nor "swipe" — clipify treats anything unknown as a cut')
        if mode == "swipe" and abs(dx) >= SEAM_DX:
            fails.append(
                f"{clip}: face_crops t={t} SWIPES {abs(dx)}px — that crosses a panel "
                f"seam and is the Ep 8 boomerang. A {CW}px column is narrower than "
                f'the gap between any two faces, so use "cut". ("swipe" is legal only '
                f"for a hand-authored drift WITHIN one panel, i.e. |dx| < {SEAM_DX}.)")
        if dx and t > dur - TRAIL_GUARD:
            fails.append(
                f"{clip}: face_crops switch at t={t} is inside the last "
                f"{TRAIL_GUARD}s of a {dur:.2f}s clip — {round((dur-t)*FPS)} frames of "
                f"another shot reads as a flash at the out point, not a cut")
        if prev_x is not None and dx == 0:
            warns.append(f"{clip}: face_crops key at t={t} repeats x={x} (no-op)")
        prev_t, prev_x = t, x
    print(f"  ok   crops  {len(fcs)} keys, "
          f"{sum(1 for i,k in enumerate(fcs) if i and int(k[1])!=int(fcs[i-1][1]))} "
          f"switches, all hard cuts")


def check_rendered(clip, path):
    """Post-render: the clip's own edges must be quiet relative to its body."""
    if not os.path.exists(path):
        warns.append(f"{clip}: --rendered but {path} does not exist")
        return
    db, _ = envelope(path, 0.0, 3600.0)
    if len(db) < 40:
        warns.append(f"{clip}: rendered clip too short to measure")
        return
    body = float(np.percentile(db[10:-10], 75))
    head, tail = float(np.max(db[:10])), float(np.max(db[-10:]))
    hot = []
    for name, v in (("head", head), ("tail", tail)):
        if body - v < RENDER_EDGE_DB:
            hot.append(name)
            warns.append(
                f"{clip}: rendered {name} 100ms is only {body-v:.1f} dB below the "
                f"body ({v:.0f} vs {body:.0f}) — expected >={RENDER_EDGE_DB:.0f}. "
                f"Listen: a decaying final consonant can be word-complete and still "
                f"read hot, but a truncation looks exactly like this too")
    print(f"  {'WARN' if hot else 'ok  '} render head {body-head:+.1f} dB / "
          f"tail {body-tail:+.1f} dB vs body {body:.0f}"
          + (f"  ({'/'.join(hot)} hot)" if hot else ""))


# ---------------------------------------------------------------- main

if ENVELOPE_AT is not None:
    src = SPEC["clips"][0].get("source", DEF_SRC) if SPEC.get("clips") else DEF_SRC
    src = opt("--src", src)
    db, t0 = envelope(src, ENVELOPE_AT - WIN, WIN * 2)
    thr = THR_OVERRIDE if THR_OVERRIDE is not None else -55.0
    print(f"# {src}\n# 10ms speech-band RMS, thr {thr:.0f} dB, '.' = quiet")
    for i, v in enumerate(db):
        mark = "." if v < thr else "#"
        star = "  <-- boundary" if abs((t0 + i * 0.01) - ENVELOPE_AT) < 0.005 else ""
        print(f"{t0+i*0.01:8.2f}  {v:7.1f}  {mark}{star}")
    for a, z in quiet_runs(db, thr):
        print(f"# quiet run {t0+a*0.01:.2f}-{t0+z*0.01:.2f} ({(z-a)*0.01:.2f}s)")
    sys.exit(0)

clips = [c for c in SPEC.get("clips", []) if not ONLY or c["name"] in ONLY]
print(f"verify_clips: {len(clips)} clip(s) from {SPEC_PATH}")
for c in clips:
    src = c.get("source", DEF_SRC)
    start, end = ts(c["start"]), ts(c["end"])
    dur = max(1, round((end - start) * FPS)) / FPS
    chain = c.get("audio_chain", DEF_CHAIN)
    mastered = c.get("style") == "plain" or (chain or "").strip() == "anull"
    thr = THR_OVERRIDE if THR_OVERRIDE is not None else (-45.0 if mastered else -55.0)
    print(f"\n{c['name']}  {start:.2f}-{end:.2f}  ({dur:.2f}s, thr {thr:.0f} dB"
          f"{', mastered' if mastered else ''})")
    if not src or not os.path.exists(src or ""):
        fails.append(f"{c['name']}: source not found: {src}")
        continue
    check_boundary(c["name"], "in", start, src, thr, c)
    check_boundary(c["name"], "out", end, src, thr, c)
    if c.get("face_crops"):
        check_crops(c["name"], c["face_crops"], dur,
                    "swipe" in c or "swipe" in SPEC)
    if DO_RENDERED:
        check_rendered(c["name"], os.path.join(OUTDIR, c["name"] + ".mp4"))

print()
for w in warns:
    print("WARN", w)
for f in fails:
    print("FAIL", f)
print(f"\n{len(fails)} failure(s), {len(warns)} warning(s)")
if fails:
    print("Fix clips.json and re-run. Do NOT render over a FAIL — both Ep 8 defects "
          "were invisible in the JSON and obvious on screen.")
sys.exit(1 if fails else 0)
