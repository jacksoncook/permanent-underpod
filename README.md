# Permanent Underpod

A podcast about **Bitcoin, stablecoins, and AI**, hosted by Jackson (Korea
markets), Chris (stablecoins / DEXs), and Tyler (Bitcoin & Lightning data).
The name riffs on "permanent underclass." Not affiliated with any employer.

This repo is the **source of truth for producing the show**: the editing
toolkit, the brand assets, and per-episode production files (transcripts,
segment maps, prep guides, render configs).

## Layout

```
skills/
  podcast-video-edit/   Make the full episode: reorder, cut, brand, master
    SKILL.md              Full workflow + gotchas
    scripts/              The automated pipeline (analyze → verify → graphics → cut → final)
    examples/             Schema-documented example configs (Ep 1's real decisions)
  clipify/              Carve shareable clips out of a recording
    SKILL.md              Teasers/shorts (branded) + long-form chapter pulls (plain)
    scripts/clipify.py
brand/                Logo masters (480 / 1920 / 3000px cover) + brand spec
episodes/
  ep1/                  Transcript (csv/srt/words), segment-times, prep guide,
                        and the plan/brand/render/clips JSON for the episode
media/                (gitignored) raw recording, final cuts, exported clips
```

All media — raw recordings, final `.mp4`s, exported clips — lives in `media/`
and is **gitignored**. It's large and regenerable from the configs above.

## Skills

Two companion agent skills (canonical copies also installed under `~/.claude/skills`):

- **`podcast-video-edit`** — turns a raw recording into a polished episode.
- **`clipify`** — cuts standalone clips: short **branded** teasers/shorts from raw
  footage (logo bug + caption, 16:9 or vertical 9:16), or **plain** long-form
  chapter pulls sliced out of the finished cut. Both share the frame-aligned
  anti-drift recipe.

## Producing an episode (the scripted pipeline)

The mechanical work is automated; a human (or LLM) makes the creative calls
via three JSON files. From a working directory:

```bash
SKILL=skills/podcast-video-edit/scripts
# 1. Probe, extract audio, transcribe, find silences, measure loudness (automatic)
bash $SKILL/analyze.sh <raw.mov> <workdir>
# 2. Verify silence candidates by speech-band RMS so quiet speakers aren't cut
python3 $SKILL/verify_silences.py <workdir>
#    >>> read <workdir>/transcript.csv, design the episode ->
#        write plan.json, brand.json, render.json (see skills/podcast-video-edit/examples/)
# 3. Logo, title/end cards, lower thirds, stat callouts
<workdir>/.venv/bin/python $SKILL/graphics.py <workdir> brand.json
# 4. Cut + render clips, concat (sync-safe), map overlay times, write chapter sheet
#    (sheet.md gets a YouTube + a Spotify chapter block automatically)
python3 $SKILL/cut_render.py <workdir> plan.json
# 5. Final encode (test the head first!) — overlays, logo bug, audio leveling, SFX
python3 $SKILL/final_render.py <workdir> render.json --test=75
python3 $SKILL/final_render.py <workdir> render.json
```

The LLM judgment lives in: segment order & boundaries (from the transcript),
teaser clip picks, protect/pause zones, overlay titles & timing, card copy,
and chapter labels. Everything else is the scripts' job.

The **audio chain** (in `render.json`) cleans + levels every speaker to a stable,
equal loudness: `highpass → afftdn → acompressor → loudnorm (dynamic, LRA=5)`.
Don't use `dynaudnorm` — it pumps on a single mixed track. (Details in SKILL.md.)

### Verify before publishing (don't skip — this caught real bugs)

```bash
F=media/<episode>.mp4
# A/V sync — video PTS must be perfectly even (drift hides if you only check total length):
ffprobe -v error -select_streams v:0 -show_entries packet=pts_time -of csv=p=0 "$F" \
  | python3 -c "import sys;t=[float(x) for x in sys.stdin if x.strip()];print('irregular gaps:',sum(1 for i in range(len(t)-1) if abs(t[i+1]-t[i]-1/30)>0.005))"   # want 0
# Loudness + leveling — integrated ~-16 LUFS, TP <= -1, LRA ~5-6:
ffmpeg -hide_banner -i "$F" -map 0:a -af loudnorm=print_format=json -f null - 2>&1 | tail -12
```
Also eyeball a frame from a **late** segment (overlays + lip sync), not just the top.

## Clips & teasers

```bash
# captions need Pillow; use a venv that has it
python3 skills/clipify/scripts/clipify.py episodes/ep1/clips.json
```

`episodes/ep1/clips.json` defines the cold-open **teasers** — each in **16:9** and
a **9:16 vertical** twin for Shorts/Reels/TikTok (blurred-bg center layout) — plus
a **long-form** "Contrarian Corner" pull from the finished cut (`style: plain`,
trimmed to end before the Vitalik tangent). Branded clips get the logo bug + a
caption; `plain` pulls are a clean slice of the already-mastered episode. Times
accept clock strings (`"58:00"`). The `plain` entry is skipped until the final cut
exists; refresh its timestamps from `segment-times.md` after a re-render. clipify
auto-cleans its caption scratch PNGs.

## Publishing

- **Final video** → YouTube and Spotify (Spotify for Creators takes the same MP4).
- **Chapters** → `episodes/ep1/segment-times.md` has a ready-to-paste block for
  **each** platform: YouTube (≥10s spacing) and Spotify (≥30s spacing). Paste the
  matching one into the description; both auto-create clickable chapters.
- **Captions** → upload `episodes/ep1/transcript.srt` as the subtitle file.
- **Cover art** → `brand/logo-3000-cover.png` (3000×3000, meets Apple/Spotify spec).
- **Promo** → `media/clips/`: 16:9 teasers for YouTube, 9:16 verticals for
  Shorts/Reels/TikTok, the long-form segment as its own upload.

## Brand

Accent yellow `#FFD24A`, badge dark `#0E0E13`, Arial Black wordmark. The couch
logo is drawn procedurally — regenerate at any size from `make_logo()` in
`skills/podcast-video-edit/scripts/graphics.py`. Cover art: `brand/logo-3000-cover.png`.

## Episode 1

First episode (recorded 2026-06-12): two-host-on-couch + Tyler remote (his dog
Pico was sick). Final cut **1:24:17**, 15 chapters. Teases for Ep 2: Pico's
recovery, saved contrarian takes, and whether Chris's lottery ticket paid out.

## Changelog

- **Speaker loudness stabilized & equalized.** Voices fluctuated (quiet
  remote/far mic vs loud in-room) — a 10 LU loudness range. The old
  `dynaudnorm` was *pumping* on the single mixed track and making it worse.
  New chain: `acompressor` (within-speaker peaks) + `loudnorm` dynamic at
  **LRA=5** (between-speaker macro leveling). Result: final-cut LRA 8.6 → **6.0**,
  short-term loudness std ~halved, speakers within ~1 LU. Clips regenerated with
  the leveled audio. See `skills/podcast-video-edit/SKILL.md` → Audio chain.

- **A/V drift fixed (two root causes).** The first Ep 1 renders drifted (picture
  progressively ahead of sound). Two independent bugs, both now fixed in
  `cut_render.py`:
  1. *Per-clip frame rounding* — `fps=30` rounded each clip's video up ~1 frame
     while audio was cut exact. Fixed by rendering an exact `-frames:v` count and
     padding/trimming audio to the matching `n*1600` samples.
  2. *Concat-demuxer PTS corruption* — `-f concat -c copy` mangled video PTS at
     clip boundaries (frames piling on one timestamp), so video drifted even with
     matched clips. Fixed by re-stamping video PTS by frame index
     (`setpts=N/30/TB`) and byte-concatenating raw PCM audio, assembled as
     separate tracks then muxed.
  See `skills/podcast-video-edit/SKILL.md` → Gotchas for the full writeup.
- **Ep 1 final re-rendered & verified the right way.** Across the whole 84 min:
  **0 irregular video PTS gaps** (was 381), `frames×1600 == audio samples`
  (delta +0.0003s, ~16 AAC samples — non-progressive), true 30fps CFR,
  −16.6 LUFS / −1.14 dBTP. Verified by PTS regularity + frame↔sample match across
  the entire file, not just total duration (which had masked the drift). Three
  teasers + a 15-min Contrarian Corner pull in `media/clips/`.
