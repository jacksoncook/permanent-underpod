---
name: clipify
description: Cut standalone, upload-ready clips out of a longer video — short branded teasers/shorts (with logo bug + caption, 16:9 or vertical 9:16) AND long-form segment extractions (pull one chapter out of a finished cut as its own file). Use when asked to clip, extract, cut out, make a teaser/short/highlight, grab a segment, or split a portion of a video/recording into separate file(s).
---

# Clipify

Turn a long video into standalone clips with ffmpeg (+ Pillow for captions). Two
modes, one tool — every clip comes out frame-aligned, h264 + aac + faststart,
safe to upload directly.

## Usage

```bash
python3 scripts/clipify.py <clips.json> [--no-logo]
# captions need Pillow: pip install pillow (or use a venv that has it)
```

Times accept seconds (`3207.4`) or clock strings (`"58:01"`, `"1:11:31"`) — so
you can paste timestamps straight off a chapter list.

## Two modes (the `style` field)

- **`branded`** (default) — for clips cut from RAW footage. Adds the logo bug,
  an optional lower-third caption, and cleans + loudness-normalizes the audio.
  Supports `"vertical": true` for a 1080×1920 short (blurred-fill background with
  the source centered — the standard Shorts/Reels/TikTok look).
- **`plain`** — for slicing a segment out of an ALREADY-finished cut (already
  branded + mastered). Does a clean, frame-accurate re-encode with NO overlays
  and NO audio processing. This is the long-form path: e.g. pull "Contrarian
  Corner, 58:01–1:11:31" out of the final episode as its own video.

## clips.json

```json
{
  "source":   "/path/video.mov",
  "out_dir":  "/path/out",
  "logo":     "/path/logo.png",
  "audio_chain": "<optional ffmpeg -af chain>",
  "clips": [
    {"name": "hook-options", "start": 3207.0, "end": 3215.4,
     "caption": {"kicker": "BIGGEST FUMBLES", "title": "$20K -> $100K -> $0"}},
    {"name": "hook-options-vertical", "start": 3207.0, "end": 3215.4, "vertical": true,
     "caption": {"kicker": "BIGGEST FUMBLES", "title": "$20K -> $100K -> $0"}},
    {"name": "contrarian-corner", "source": "/path/ep1-final.mp4",
     "start": "58:01", "end": "1:11:31", "style": "plain"}
  ]
}
```

Per-clip overrides: `source`, `logo` (bool), `caption`, `vertical`, `style`.

## Notes / gotchas

- **A/V sync:** clips are frame-aligned the same way `podcast-video-edit` cuts —
  exact `-frames:v round(dur*30)` video + audio padded/trimmed to `n*1600`
  samples — so video_len == audio_len and there's no drift even on long pulls.
- **Long-form from the finished cut, not raw:** when extracting a chapter, point
  `source` at the FINAL mp4 and use the final-cut chapter timestamps (the polished
  version already has overlays + mastered audio). Use `style: "plain"` so clipify
  doesn't double-process it.
- **Captions** reuse the project's lower-third look (dark box, accent side-bar,
  yellow kicker + white title). Needs the Arial Black/Bold fonts — auto-copied
  from `/System/Library/Fonts/Supplemental` on macOS, or point `fonts_dir` at them.
- **Vertical** uses a blurred-background center layout so couch/two-shot framings
  aren't cropped through faces. Logo moves to a safe top-left inset; caption sits
  above the lower third of the 9:16 frame.
- Homebrew ffmpeg may lack `drawtext` — captions are rendered as PNG overlays
  (via Pillow), not drawtext, on purpose.

## Relationship to podcast-video-edit

`podcast-video-edit` produces the full episode (reorder, cut, brand, master).
`clipify` is the downstream/companion tool that carves shareable pieces out of
either the raw recording (teasers) or the finished episode (chapter pulls). They
share the frame-aligned anti-drift recipe and the same logo/lower-third styling.
