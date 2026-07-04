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

## Posting copy (ALWAYS produce this alongside the clips)

The clips are only half the deliverable — every run also writes a
**`posting-copy.md`** in `out_dir` so the clips are ready to upload, not just ready
to watch. This is LLM-authored judgment (hooks/hashtags), the same way the JSON
decision docs are in `podcast-video-edit`. For **each** clip include:

- **Title** — platform-ready, with the hook **front-loaded in the first ~40 chars**
  (that's all the Shorts/Reels player shows). **NO `#Shorts` in the title** (house
  style, set by Jackson's Ep 4 edits) — routing comes from a `#shorts` hashtag in
  the description instead. Long-form pulls get a **"Highlights: " title prefix**.
- **Caption** — one punchy sentence of context (assume the viewer has zero episode
  context; the clip must stand alone), ending with the live episode link
  ("Full episode: https://youtu.be/…").
- **Hashtags** — the description's LAST line: 2–3 lowercase topical tags plus
  `#shorts` for verticals (e.g. `#shorts #ai #conquistador`). Keep the `tags`
  manifest field for the 5–8 plain keywords.

Shape (one block per clip):

```
**<clip-name>** (9:16 | 16:9)
- Title:   <hook front-loaded> 🤖
- Caption: <one standalone sentence>
- Tags:    #Shorts #Topic1 #Topic2 …
```

If these clips belong to an episode that already has a `segment-times.md` (the
`podcast-video-edit` sheet), also append the same per-clip copy there so all the
publishing text lives in one place. Long-form pulls get a title + 1–2 line
description + the segment's hashtags (no `#Shorts`).

## Publish to YouTube (`scripts/yt_upload.py`)

Once the clips + posting copy exist, `yt_upload.py` uploads them via the YouTube
Data API v3. **Default flow: scheduled-private — each video uploads private with a
`publishAt` time and YouTube flips it public automatically at release.** This is the
shared uploader for *both* this skill and `podcast-video-edit` — a full episode is
just another upload entry (16:9, no `#Shorts`).

**One-time setup:** see [`youtube-setup.md`](youtube-setup.md) — make a Google Cloud
project, enable *YouTube Data API v3*, create a **Desktop** OAuth client, download
`client_secret.json` to `~/.config/clipify-youtube/`, and install the libs into a venv.
Secrets live OUTSIDE the repo; never commit `client_secret.json` / `token.json`.

**The flow (what you, the agent, do):**

1. Build an **upload manifest** from the posting copy you already authored — one
   entry per file, reusing its title/description/tags. Map markdown → JSON:
   `Title → title`, `Caption → description` (or a fuller description), `Tags → tags`
   (strip the `#` — the `tags` field is plain keywords; keep `#Shorts` in the *title*
   so YouTube still routes verticals to the Shorts shelf).
2. **Ask the user for the release date/time** (their local Pacific time), then
   convert to RFC3339 **UTC** and set `publishAt` per entry. Ask whether they want
   everything at one time or a stagger (e.g. one short every few days). Use
   `AskUserQuestion`. This is the "ask me for release date/time" step.
3. Run it with the setup venv's python:
   ```bash
   ~/.config/clipify-youtube/.venv/bin/python scripts/yt_upload.py <manifest>.json --dry-run  # verify first
   ~/.config/clipify-youtube/.venv/bin/python scripts/yt_upload.py <manifest>.json            # upload
   ```
   The first real run opens a browser once to authorize; the token is cached after.
4. Report the resulting URLs. Scheduled clips stay **private** until `publishAt`,
   then auto-publish.

**Show conventions (learned Ep 4 — follow by default):**

- **The episode publishes BEFORE its clips.** Schedule the full episode first;
  clips start after it's live. Every clip description links the live episode
  ("Full episode: https://youtu.be/…") — never "drops soon".
- **Playlists:** every vertical short gets `"playlist": "Underpod Shorts"`; every
  16:9 clip/highlight gets `"playlist": "Underpod Clips"` (both exist on the
  channel). The uploader resolves playlist names case-insensitively and adds each
  video right after upload. This needs the broad `youtube` OAuth scope (the script
  requests it; an old upload-only token triggers a one-time re-auth).
- **Shorts "related video"** (the Studio button that points a Short at its source
  episode) is NOT settable via the Data API — flag it in the run summary as a
  ~10-second-per-short manual step in YouTube Studio → Content → (short) →
  Related video. The description link is the automated fallback.
- **Browser auth gotcha:** on the OAuth channel-picker screen, choose the
  **Permanent Underpod brand channel**, not the personal account — the flow
  defaults to personal, and a token is channel-bound (Ep 4's first batch landed
  on the wrong channel and had to be re-uploaded).

**Manifest** (`publishAt` is RFC3339 UTC; omit it to just use `privacyStatus`;
`playlist` is a playlist name or PL… id, per-entry or in `defaults`):

```json
{
  "client_secret": "~/.config/clipify-youtube/client_secret.json",
  "token":         "~/.config/clipify-youtube/token.json",
  "defaults": {"categoryId": "22", "privacyStatus": "private", "madeForKids": false},
  "uploads": [
    {"file": "/path/clips/ep3/short5-monster-energy.mp4",
     "title": "Roasted for grinding Halo 3 as a fully-grown adult 🎮 #Shorts",
     "description": "Chris cops to needing 200mg of caffeine to game… Full episode: https://youtu.be/…",
     "tags": ["Halo3", "gaming", "podcast", "MonsterEnergy"],
     "playlist": "Underpod Shorts",
     "publishAt": "2026-07-01T17:00:00Z"}
  ]
}
```

Notes: `--publish-at` / `--privacy` override every entry; uploaded files are tracked
in `<manifest>.results.json` and skipped on re-run (`--force` to re-upload).
`categoryId` "22" = People & Blogs. A video insert costs ~1600 of the default
10,000/day API quota (~6 uploads/day). A brand-new channel locks API uploads to
private until you verify it by phone in YouTube Studio.

**Reading back what's live (`scripts/yt_fetch.py`).** Companion fetcher — pulls every
published video's title/description/tags for the authed channel (scope
`youtube.readonly`, same `client_secret.json`, cached to `token_readonly.json`). Use it
to backfill each episode's `segment-times.md` from the *actual published* copy instead
of drafts: `~/.config/clipify-youtube/.venv/bin/python scripts/yt_fetch.py` → writes
`channel_dump.json`. (YouTube only returns a video's real `tags` to the channel owner.)

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
