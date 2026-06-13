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
SKILL=skill/scripts
# 1. Probe, extract audio, transcribe, find silences, measure loudness (automatic)
bash $SKILL/analyze.sh <raw.mov> <workdir>
# 2. Verify silence candidates by speech-band RMS so quiet speakers aren't cut
python3 $SKILL/verify_silences.py <workdir>
#    >>> read <workdir>/transcript.csv, design the episode ->
#        write plan.json, brand.json, render.json (see skill/examples/)
# 3. Logo, title/end cards, lower thirds, stat callouts
<workdir>/.venv/bin/python $SKILL/graphics.py <workdir> brand.json
# 4. Cut + render clips, concat, map overlay times, write chapter sheet
python3 $SKILL/cut_render.py <workdir> plan.json
# 5. Final encode (test the head first!) — overlays, logo bug, audio chain, SFX
python3 $SKILL/final_render.py <workdir> render.json --test=75
python3 $SKILL/final_render.py <workdir> render.json
```

The LLM judgment lives in: segment order & boundaries (from the transcript),
teaser clip picks, protect/pause zones, overlay titles & timing, card copy,
and chapter labels. Everything else is the scripts' job.

## Clips & teasers

```bash
# captions need Pillow; use a venv that has it
python3 skills/clipify/scripts/clipify.py episodes/ep1/clips.json
```

`episodes/ep1/clips.json` defines the three cold-open **teasers** (branded, pulled
from the raw footage → `media/clips/`) plus a **long-form** "Contrarian Corner"
pull from the finished cut (`style: plain`). The long-form entry is skipped until
`media/ep1-final-cut.mp4` exists, and its timestamps should be refreshed from
`episodes/ep1/segment-times.md` after a re-render.

## Brand

Accent yellow `#FFD24A`, badge dark `#0E0E13`, Arial Black wordmark. The couch
logo is drawn procedurally — regenerate at any size from `make_logo()` in
`skill/scripts/graphics.py`. Cover art for Spotify/Apple: `brand/logo-3000-cover.png`.

## Episode 1

First episode (recorded 2026-06-12): two-host-on-couch + Tyler remote (his dog
Pico was sick). Final cut ~1:24, 16 chapters. Teases for Ep 2: Pico's recovery,
saved contrarian takes, and whether Chris's lottery ticket paid out.

## Changelog

- **A/V drift fixed.** The first Ep 1 render drifted ~2.4s (picture ahead of
  sound) because `fps=30` rounded each clip's video up ~1 frame while audio was
  cut exact, accumulating across 63 clips. `cut_render.py` now renders an exact
  frame count per clip and pads/trims audio to the matching sample count
  (`n*1600`), so every clip has `video_len == audio_len` and concat stays
  locked; the final pass also forces `-r 30 -fps_mode cfr`. See
  `skills/podcast-video-edit/SKILL.md` → Gotchas for the full writeup.
- **Ep 1 v2 re-rendered & verified.** +0.010s A/V delta across 84 min (was
  +2.4s), true 30fps CFR, −16.6 LUFS / −1.14 dBTP. Three teasers + a 15-min
  Contrarian Corner pull exported to `media/clips/`.
