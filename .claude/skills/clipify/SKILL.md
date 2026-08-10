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
# 1. GATE FIRST — always. Needs numpy + ffmpeg, so use a venv python
#    (an episode workdir has one: media/epN/work/.venv/bin/python)
<venv>/bin/python scripts/verify_clips.py <clips.json>      # exit 1 = do not render
# 2. render
python3 scripts/clipify.py <clips.json> [--no-logo]
# captions need Pillow: pip install pillow (or use a venv that has it)
# 3. confirm the finished files
<venv>/bin/python scripts/verify_clips.py <clips.json> --rendered
```

Times accept seconds (`3207.4`) or clock strings (`"58:01"`, `"1:11:31"`) — so
you can paste timestamps straight off a chapter list.

**`verify_clips.py` is not optional, and neither is reading its output.** Ep 8
shipped 8 clips with a crop artifact and 10 truncated boundaries; every one was
invisible in the JSON, passed a bracket-window transcript check, and was caught by
Jackson *watching them*. The gate checks what only eyes caught before:

- every in/out point lands in a **measured ≥80 ms silence** (10 ms speech-band RMS
  envelope), and prints a suggested corrected time when it doesn't;
- every `face_crops` switch is a hard cut, in range, in order, and not inside the
  last 0.5 s of the clip;
- with `--rendered`, each finished clip's first/last 100 ms sits ≥8 dB below its
  own body level.

Extra flags: `--whisper` adds word-level whisper as a second opinion (it names the
word being cut); `--envelope T --src FILE` dumps the raw envelope around one time
when a call is marginal; `--thr`/`--lead`/`--tail` tune it; `--clip NAME` narrows the
run. `clipify.py` itself hard-exits on a seam-crossing swipe or a trailing crop key
as a backstop, but it cannot check audio — skip the gate and truncation ships.

**Overriding a boundary FAIL** (rare, and it has to be earned): sometimes no gap
exists — the clip ends on a decaying consonant and the next word starts 10 ms later.
That's a real judgement call, so it's allowed only as a *declared* override carrying
a reason, which downgrades it to a WARN and leaves a trail:

```json
{"name": "short3-…", "verify_override":
  {"out": "no gap exists: ends on the decaying /f/ of 'wife', next word 0.01s later"}}
```

Use it only when the envelope shows a **falling** tail (the gate reports the trend);
**rising** or flat at the boundary means you cut into a word — move the boundary.

## Two modes (the `style` field)

- **`branded`** (default) — for clips cut from RAW footage. Adds the logo bug,
  an optional lower-third caption, and cleans + loudness-normalizes the audio.
  Supports `"vertical": true` for a 1080×1920 short (blurred-fill background with
  the source centered — the standard Shorts/Reels/TikTok look).
- **`plain`** — for slicing a segment out of an ALREADY-finished cut (already
  branded + mastered). Does a clean, frame-accurate re-encode with NO overlays
  and NO audio processing. This is the long-form path: e.g. pull "Contrarian
  Corner, 58:01–1:11:31" out of the final episode as its own video.

## The ender (HOUSE DEFAULT for shorts — put `"ender": true` in every clips.json)

A 1 s branded end card APPENDED to every branded vertical: dark card, logo pops
to center on the sting hit (ease-out-back, peak on the transient at ~0.24 s),
"PERMANENT UNDERPOD" wordmark + gold underline settle in. Funnel branding — the
swipe-away moment shows the channel name, and since Shorts loop it also plays as
the loop seam into the hook. Added 2026-08-10 after the 8/10 analytics review
(14k shorts views → 1 sub).

- Spec-level `"ender": true` (house default) or `{"duration": 1.0, "sting": path,
  "text": "..."}`. Per-clip `"ender": false` opts out; per-clip `"ender": true`
  forces it onto a non-vertical branded clip. Never applies to `plain`.
- Sting: `brand/ender-sting.wav` (1 s, peak −3 dB, faded tail). CC0 alternates +
  provenance in `media/ender-candidates/README.md`; to change the sound, replace
  the brand wav — transient at ~0.24 s, ≤1 s, peak ≈ −3 dB.
- The ender is appended AFTER the content: in/out bounds, face_crops, and clip
  length guidance (10–20 s) are unchanged; reported duration grows ~1 s.
- `verify_clips.py --rendered` knows: it bounds the edge check to the spec-side
  content length (`note ender` line) so the sting doesn't read as a hot tail.

## Face-crop verticals (digital / fully-remote episodes)

For episodes shot as per-host webcams (solo shots + split-screen panels), vertical
shorts should be a FULL-BLEED face crop of the active speaker — not the blurred
letterbox layout. Add `"face_crops": [[t_rel, x_left], ...]` to a vertical clip:
a 406x720 column tracked piecewise across the clip, scaled to 1080x1920.

**Every crop switch is a HARD CUT, and that is not a style choice.** A key may be
`[t_rel, x_left]` or `[t_rel, x_left, "cut"|"swipe"]`; bare keys cut. Do NOT swipe
between panels: the 406 px column is narrower than the gap between any two faces,
so an eased move always spends its middle frames on the panel seam — wall plus two
half-faces. Ep 8's first clip batch swiped every key and the shot appeared to swing
off a person and **boomerang** back (worst when the same person was on both sides of
the switch, e.g. duo(jackson,tyler) → solo(jackson)). "Both faces are on screen so
easing is fine" is wrong — they're both in the SOURCE, never both in the CROP.
`"swipe"` survives only for a hand-authored drift WITHIN one panel, where there is
no seam to cross. This is **enforced, not advised**: `verify_clips.py` FAILs any
swipe of ≥40 px (plus out-of-range x, unordered keys, a first key not at t=0, and a
switch inside the last 0.5 s — Ep 8's short3 had a key 0.17 s from the end, i.e. a
5-frame flash of another person), and `clipify.py` hard-exits on the same two rather
than render them.

Generate the schedule from the episode workdir (shot layout + VAD pick the
active speaker; solo shots crop around the face, splits crop the speaking panel).
Schedules switch EXACTLY at shot-layout boundaries — hysteresis only applies to
speaker changes within a constant layout (a lagged switch across a layout cut
parks the crop on the seam between panels and shows "no one"):

```bash
python3 ../podcast-video-edit/scripts/remote_face_crops.py <workdir> <final_start> <final_end>
```

**Source rule:** cut face-crop shorts from the episode's `edited_raw.mov`
(pre-overlay master — same timeline as the final cut) with the episode's audio
chain as `audio_chain`, and let clipify add the logo + caption. Cutting from the
final mp4 works but left-edge crops catch the BAKED logo (double bug) and
stat callouts can be sliced mid-graphic.

## What to clip & how long (data-backed — channel analytics, Jul 2026)

Selection and length rules, from `analytics/report.html` (refresh with the
`channel-analytics` skill):

- **Pick by personality, not topic importance.** Every top short is a host being
  a character or a quotable one-liner (lottery ticket 1,273 views, Halo 3 roast
  986, skipped-his-party 674, dog food 469); every abstract-concept short flopped
  (4–24 views). Clip the human moments first, concepts last.
- **Default a short to 10–20 s, one punchline.** Sub-15 s shorts loop (>100% avg
  viewed — Dimon 145%, Bitcoin Bankruptcy 130%), which feeds the Shorts algorithm;
  25–60 s cuts hold only 30–48%. Go 25 s+ only when the bit genuinely needs setup.
- **Length yields to word boundaries, not the reverse.** "Start mid-laugh" means open
  on a *reaction*, never mid-syllable: pick the beat you want, then let
  `verify_clips.py` move each end out to the nearest real gap and accept the length
  that falls out. Ep 8's short3 landed at 21.7 s that way — over guidance, and correct,
  because the alternative was clipping a word. If honoring the boundaries pushes a clip
  well past ~25 s, that's the signal the pick needs a tighter beat, not a tighter trim.
- **End-of-show bits are shorts gold** — they air where only 3–5% of episode
  viewers remain, but the lottery-ticket finale became the channel's #1 video.
  Clip them within 24 h of the episode going live.

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

Per-clip overrides: `source`, `logo` (bool), `caption`, `vertical`, `style`,
`audio_chain`, `face_crops`, `swipe`, `verify_override` (see Usage — a declared,
reasoned exception to a boundary FAIL; `clipify.py` ignores it).

**Mixed-source batches need a per-clip `audio_chain`.** A fully-remote episode's
face-crop shorts come off `edited_raw.mov`, which is UNmastered and wants the
episode chain — but any clip that needs a baked-in graphic (the Perp of Fortune
dashboard PiP, a stat callout) has to come off the FINAL mp4, which is already
mastered and wants `"audio_chain": "anull"` plus `"logo": false`. Set the episode
chain at the top level and override those clips individually; running the episode
chain twice re-drives a big pre-gain into the compressor and limiter, and the
trailing `loudnorm` hides it in the measured level but not in the sound.

## Posting copy (ALWAYS produce this alongside the clips)

The clips are only half the deliverable — every run also writes a
**`posting-copy.md`** in `out_dir` so the clips are ready to upload, not just ready
to watch. This is LLM-authored judgment (hooks/hashtags), the same way the JSON
decision docs are in `podcast-video-edit`. For **each** clip include:

- **Title** — platform-ready, with the hook **front-loaded in the first ~40 chars**
  (that's all the Shorts/Reels player shows). **NO `#Shorts` in the title** (house
  style, set by Jackson's Ep 4 edits) — routing comes from a `#shorts` hashtag in
  the description instead. Long-form pulls: hook first, provenance as a **suffix**
  — **house convention: `<Hook> - Ep N Clip`** (e.g. "The US Government AI Rugged
  Us - Ep 2 Clip"). **NEVER a "Highlight -"/"Highlights:" prefix**:
  the five Ep 1–4 clips that shipped with it did 5–92 views with bottom-decile
  retention (retitled Jul 2026; `yt_upload.py` lints for this).
- **Caption** — one punchy sentence of context (assume the viewer has zero episode
  context; the clip must stand alone), ending with the live episode link
  ("Full episode: https://youtu.be/…"). Long-form pulls instead put the funnel
  line FIRST in the description: "Clip from Episode N — full episode: <link>".
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
   (strip the `#` — the `tags` field is plain keywords). Per house style the title
   carries NO `#Shorts`; the `#shorts` hashtag on the description's last line is
   what routes verticals to the Shorts shelf.
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
- **The funnel is the point** (channel analytics, Jul 2026: shorts = 81% of views
  but ~0 subscribers — episodes convert). After every clip batch, work the
  checklist `yt_upload.py` prints:
  1. **Related video** (Studio button pointing a Short at its source episode) —
     NOT settable via the Data API; ~10 s per short in YouTube Studio → Content →
     (short) → Related video. The description link is the automated fallback.
  2. **Pinned comment** once each clip is public: episode link + the timestamp
     where the full segment starts (pinning isn't in the API either).
  3. **End screens** on episodes and 16:9 clips → next episode / subscribe.
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
- **Whisper cue times cannot place an in/out point — run `verify_clips.py`.** Whisper
  segments tile contiguously *across* real pauses, so a cue boundary is not a speech
  boundary; on Ep 8 they were off by up to 6 s and most hand-picked boundaries sat
  mid-word ("Close it!" — the literal caption of its clip — was truncated). The gate
  measures a 10 ms speech-band RMS envelope (`highpass=200,lowpass=3500`) and requires
  a ≥80 ms quiet run at each boundary; `--whisper` adds word-level whisper
  (`--max-len 1 -sow`) as a second opinion. Things it encodes, worth knowing when a
  call is close:
  - **FIXED thresholds only** (−55 dB unmastered / −45 dB mastered, auto-picked per
    clip). Never percentile-derived: windows containing digital silence gave baselines
    of −174 dB and flagged everything as speech.
  - **Where envelope and whisper disagree, the envelope wins** — but read it with
    `--envelope` before acting, because a stop consonant's closure looks like a gap
    (Ep 8's short5: the dip at 2617.74 was the /p/ of "up"; the real gap was 2618.35).
  - Aim in-points ~0.15–0.25 s before speech resumes and out-points just after it
    stops — that's what the suggested times it prints are computed for.
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
