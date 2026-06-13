---
name: podcast-video-edit
description: Edit a raw podcast video recording into a polished episode — reorder segments, cut dead air safely, normalize/level audio, add title cards, lower thirds, stat callouts, a logo bug, and SFX. Use when editing, cutting, swagifying, reordering, or polishing a podcast/interview/panel recording (video or audio), or when asked to "make a podcast" from a raw recording.
---

# Podcast Video Edit

Turn a single raw recording (e.g. `.mov` from a camera) into a polished, reordered,
branded episode using only ffmpeg + whisper-cpp + Python/Pillow. No NLE needed.

> **Companion skill — `clipify`:** to carve shareable pieces out of a recording
> (short branded teasers/shorts, or long-form chapter pulls from the finished
> cut), use the `clipify` skill. It shares this skill's frame-aligned anti-drift
> recipe and logo/lower-third styling. This skill makes the episode; clipify
> slices it.

## Scripted pipeline (use this — scripts in `scripts/`, examples in `examples/`)

The mechanical work is automated; your job is the three JSON decision documents.

```
1. bash scripts/analyze.sh <raw.mov> <workdir>      # probe, audio, transcript, silence candidates, loudness
2. python3 scripts/verify_silences.py <workdir>      # band-RMS-verified dead air -> verified_cuts.json
       (run --calibrate first on a known silence + faintest speech if levels look unusual)
   >>> YOU: read transcript.csv, design the episode -> write plan.json, brand.json, render.json
       (see examples/ep1_*.json for the schemas and a real episode's decisions)
3. <workdir>/.venv/bin/python scripts/graphics.py <workdir> brand.json   # logo, cards, lower thirds, stats
4. python3 scripts/cut_render.py <workdir> plan.json # clips -> concat -> edited_raw.mov + overlays.json + sheet.md
5. python3 scripts/final_render.py <workdir> render.json --test=75   # ALWAYS test-render the head first
   # verify frames of test_head.mp4 (title card, lower third, logo bug), then run without --test
```

The LLM judgment lives in: segment order + boundaries (from the transcript), teaser
clip picks, protect zones (visual moments), pause-keep zones, overlay titles/timing,
card copy, chapter labels. Everything else is the scripts' problem.

After the full render: spot-check frames at overlay windows (`overlays.json` has
exact final times), confirm A/V durations match, loudnorm-measure the result
(target ≈ -16 LUFS, TP ≤ -1 dBTP). If peaks are hot, re-render AUDIO ONLY from
edited_raw.mov and remux with `-c:v copy` — never re-encode video for an audio fix.

## Pipeline overview (what the scripts do, for debugging or extending)

1. **Probe & context** — `ffprobe` the file (duration, streams, fps, loudness).
   Look for a prep doc / rundown near the file (e.g. `*prep*.md` on the Desktop):
   it tells you the intended segments AND production intent (e.g. "record the cold
   open last, cut it to the front").
2. **Extract audio** — `ffmpeg -vn -c:a copy` to m4a; also a 16 kHz mono WAV for whisper.
3. **Transcribe** — `brew install whisper-cpp`, download `ggml-small.en.bin` from
   huggingface ggerganov/whisper.cpp, run `whisper-cli -m model -f audio16k.wav -ocsv`.
   The CSV (start ms, end ms, text) is the map for everything: real segment
   boundaries, reorder anchors, overlay timing, teaser quotes.
4. **Plan the order** — find structural lines in the transcript ("welcome to the show",
   "let's transition", "our last segment"). Classic shape: cold-open teaser clips →
   title card → official intro (often recorded mid/late!) → segments → outro →
   bloopers/meta as post-credits stinger → end card. Segment boundaries usually land
   where blocks are *contiguous* in the source — exploit that to minimize cuts.
5. **Cut dead air SAFELY** (see below — naive silencedetect WILL cut quiet speakers).
6. **Graphics with Pillow** (homebrew ffmpeg often lacks drawtext!): title card and
   end card (blurred video frame + text), lower-third PNGs per segment, stat-callout
   PNGs, logo badge. Copy system fonts (e.g. `/System/Library/Fonts/Supplemental/Arial
   Black.ttf`) to a path without spaces.
7. **Render clips** — one ffmpeg per keep-interval: `-ss S -t D -i src -vf
   fps=30,format=yuv420p -c:v h264_videotoolbox -b:v 10M -c:a pcm_s16le -ac 1`
   into `.mov`. PCM audio makes concat gapless (AAC priming causes clicks at joins).
   Parallelize with ~3 workers. Re-encoding per clip keeps every cut frame-accurate
   and avoids cumulative A/V drift (never use one giant select= graph for 50+ cuts).
8. **Concat** — concat demuxer with `-c copy`. ffprobe each clip's *actual* duration and
   build a source-time → final-time map for overlay scheduling and the segment sheet.
9. **Final pass** — single re-encode: overlay chain (looped PNG inputs with
   `enable='between(t,a,b)'`), logo bug (`format=rgba,scale=170:-1,
   colorchannelmixer=aa=0.8`, disabled during cards), audio chain + SFX mix,
   `h264_videotoolbox -b:v 7500k`, `-movflags +faststart`.
10. **Deliverables** — final mp4 + a segment-times markdown sheet (chapter list with
    final timestamps, YouTube-chapter friendly).

## The dead-air trap (critical)

Far-mic / laptop-speaker participants can speak at **−55 dB RMS** while normal speech
is −37 dB. `silencedetect` at any sane threshold flags their speech as silence, and
whisper word timestamps tile contiguously (words stretch across real pauses), so
transcript gaps can't verify either. The fix that works:

- Get candidates: `silencedetect=noise=-38dB:d=2.0`.
- Verify each candidate by measuring speech-band RMS of its interior
  (`highpass=f=200,lowpass=f=3500,astats=measure_overall=RMS_level`, on
  `[start+0.3, end-0.3]`). Only cut if RMS < **−62 dB** (calibrate: measure a known
  true silence and the faintest real speech first).
- Keep ~0.7 s of each cut pause (1.2 s where pauses are content, e.g. on-camera
  business); skip protected zones (visual moments). Require ≥1 s net removal.
- Expect to reject ~60% of candidates. ~2–3 min of true dead air per 90 min is normal.

## Audio chain for uneven multi-mic recordings

```
highpass=f=70, afftdn=nr=22:nf=-52:tn=1,
dynaudnorm=f=200:g=11:m=30:p=0.95:t=0.0065,
loudnorm=I=-16:TP=-1.5:LRA=11:linear=true:measured_*=<2-pass values>
```

- `dynaudnorm` with a tuned `t` (threshold) is the key: it lifts faint speakers
  (+25 dB) but leaves true silence un-amplified (no noise pumping). Tune `t` between
  noise peaks and faint-speech peaks (~0.006–0.01); verify on three slices: faint
  speech, normal speech, true silence. Target: speech within ~5 dB, silence < −60.
- Two-pass loudnorm: measure with the chain applied, then render with `measured_*`
  values and `linear=true`. −16 LUFS integrated / −1.5 dBTP is the podcast standard.
- Mix SFX *after* loudnorm: `adelay=<ms>:all=1` + `amix=normalize=0` + alimiter.
  Pre-normalize SFX to ~−20 LUFS so they sit under speech.

## SFX & music

freesound.org preview MP3s are fetchable without auth: scrape
`https://freesound.org/search/?q=<query>` for `cdn.freesound.org/previews/*.mp3`
(use a browser User-Agent). Good queries: "whoosh transition", "logo sting".
Trim/fade and loudnorm before mixing.

## Branding quickly with Pillow

- Logo badge: rounded-rect dark card + flat icon drawn from rounded rectangles +
  show name in Arial Black; export PNG with alpha, reuse at 3 sizes (card centerpiece,
  end-card mark, 170 px corner bug at ~0.8 alpha).
- Lower thirds: dark rounded box, accent side-bar, yellow kicker line + white title,
  auto-width from `textbbox`. Show each for ~6 s at segment starts.
- Stat callouts (top-right) for "numbers" moments (confessions, prices) ~10–12 s.
- Cards: grab a frame (`-ss T -frames:v 1`), GaussianBlur(22) + 55% black blend.

## Gotchas

- **Progressive A/V drift (THE big one — bit Ep 1 TWICE).** There are two
  independent causes; you must fix BOTH or the picture drifts ahead of the sound,
  worsening through the episode. Always verify by checking sync at a LATE point —
  matching total durations does NOT prove internal sync.
  1. *Per-clip frame rounding.* `-t <dur> ... -vf fps=30` rounds each clip's video
     up to a whole frame (~+33 ms) while audio is cut exact. FIX: render an EXACT
     frame count + matching sample count — `-frames:v round(dur*30)` and
     `-af aresample=48000,apad,atrim=end_sample=round(dur*30)*1600`
     (1600 = 48000/30 samples/frame), so video_len == audio_len per clip.
  2. *Concat-demuxer PTS corruption (the subtle one).* Even with perfectly
     matched clips, `ffmpeg -f concat -c copy` MANGLES video PTS at every clip
     boundary — piles of frames land on a single timestamp, others get double
     gaps (`ffprobe -show_entries packet=pts_time` reveals 0 ms and 66 ms gaps).
     The PCM audio concatenates cleanly, so video drifts. The concat *filter*
     isn't a fix either — it pads audio ~1 frame per join. RELIABLE FIX, done in
     `cut_render.py`: assemble the two tracks separately —
       • VIDEO: concat-demuxer (keeps every frame) then **re-stamp PTS by frame
         index**: `-vf setpts=N/30/TB -fps_mode passthrough` → perfectly even CFR.
       • AUDIO: **byte-concatenate raw PCM** (`-f s16le` per clip, `cat` the
         bytes) → exact sample sum, zero padding/resample.
       • mux the clean video + raw audio.
     Verify: `ffprobe -show_entries packet=pts_time` shows ZERO gaps off 1/30,
     and `nb_read_frames*1600 == audio duration_ts` to the sample.
  The final pass also forces `-fps_mode cfr` + `aresample=async=1:first_pts=0`,
  but those only hold if the concat feeding them is already clean (cfr will
  drop/dup frames trying to conform corrupt PTS, spreading the drift around).
- **Runaway encode:** `-loop 1` image inputs NEVER signal EOF. Without a finite
  input `-t` on every looped image, `eof_action=pass` on overlays, and an output
  `-t <timeline>` cap, the final render encodes static frames forever and the MP4
  never gets its moov atom (file unplayable, high CPU, slow growth). All three
  guards are baked into `scripts/final_render.py`.
- `loudnorm=linear=true` silently under-gains when input TP is hot (it protects
  the ceiling by reducing the gain). For speech with rare hot transients, apply
  plain `volume=<gain>dB` + `alimiter` instead.
- Homebrew ffmpeg may lack `drawtext` — render ALL text as PNG overlays instead.
- whisper word-level mode (`-ml 1 -sow`): words absorb silence; never infer pauses.
- `-ss` before `-i` + re-encode is frame-accurate; with `-c copy` it is not.
- Title/teaser quote boundaries: pull exact ms from the transcript CSV, pad ±0.15 s.
- Check `input_tp` from a loudnorm measure early: far-mic recordings can hide +5 dB
  clipped transients (mic bumps) — the limiter at the end of the chain catches them.
- Verify the final A/V sync by spot-checking a LATE segment, not just the start —
  drift is invisible at the top and only obvious near the end.
