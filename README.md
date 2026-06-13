# Permanent Underpod

A podcast about **Bitcoin, stablecoins, and AI**, hosted by Jackson (Korea
markets), Chris (stablecoins / DEXs), and Tyler (Bitcoin & Lightning data).
The name riffs on "permanent underclass." Not affiliated with any employer.

This repo is the **source of truth for producing the show**: the editing
toolkit, the brand assets, and per-episode production files (transcripts,
segment maps, prep guides, render configs).

## Layout

```
skill/            The "podcast-video-edit" agent skill (canonical copy)
  SKILL.md          Full workflow + gotchas
  scripts/          The automated pipeline (see below)
  examples/         Schema-documented example configs (Ep 1's real decisions)
brand/            Logo masters (480 / 1920 / 3000px cover) + brand spec
episodes/
  ep1/              Transcript (csv/srt/words), segment-times, prep guide,
                    and the plan/brand/render JSON used to cut the episode
```

Large media (raw recordings, final `.mp4`s) are **gitignored** — they live on
the Desktop / external storage, not in git.

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
  locked; the final pass also forces `-r 30 -fps_mode cfr`. Re-cut episodes to
  pick up the fix. See `skill/SKILL.md` → Gotchas for the full writeup.
