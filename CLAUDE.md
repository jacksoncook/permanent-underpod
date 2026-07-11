# CLAUDE.md — Permanent Underpod

Quick orientation for agents. Full details are in `README.md` (pipeline + publishing)
and the two skills under `.claude/skills/`.

## What this is
A Bitcoin / stablecoins / AI podcast (hosts: Jackson, Chris, Tyler). This repo is the
**source of truth for producing the show** — editing toolkit, brand, and per-episode
production files. Not affiliated with any employer.

## Where things live
- `.claude/skills/podcast-video-edit/` — make the full episode (auto-loads in this repo)
- `.claude/skills/clipify/` — cut shareable clips; publish/read YouTube
- `brand/` — logo masters + brand spec
- `episodes/epN/` — transcript(s), `segment-times.md` (the publishing sheet), and the
  `plan/brand/render/clips/reframes` JSON decision docs
- `media/` — raw recordings, final cuts, exported clips. **GITIGNORED — not in the repo.**

## Skills (auto-loaded from `.claude/skills/`)
- **podcast-video-edit**: `analyze.sh → verify_silences.py → graphics.py → cut_render.py
  → final_render.py`. The human/LLM writes `plan.json`, `brand.json`, `render.json`.
  **Fully-remote episodes** (each host records their own cam, à la Ep 5):
  `remote_sync.py → remote_sync_bench.py (a HOST aligns by ear — ALWAYS; never trust
  file metadata) → remote_transcribe.py → graphics.py → remote_cutlist.py → remote_cut.py
  → final_render.py → remote_attribute.py`, driven by `sources.json` + `remote_plan.json`
  (see SKILL.md → "Fully-remote episodes").
- **clipify**: `clipify.py` cuts clips; `yt_upload.py` publishes (scheduled-private,
  auto-publish at a `publishAt`); `yt_fetch.py` reads back live video metadata. One-time
  OAuth setup is in `.claude/skills/clipify/youtube-setup.md`.
- **channel-analytics**: `yt_pull.py` pulls channel/video stats + retention curves +
  traffic sources + impressions/CTR; LLM writes `analytics/insights.json`; `report.py`
  renders a branded HTML report. Always `--expect-channel "Permanent Underpod"`.

## Managing the pod (the weekly cycle, across the three skills)
1. **Record** (hosts — not automatable, but remind them): check-in ≤60 s, one
   retainer bit (Perp of Fortune / confession / AI bit) in the first 10 min,
   explainers ≤8 min and tied to live stakes. Rationale: `analytics/report.html`.
2. **Edit** with `podcast-video-edit` (remote pipeline for fully-remote eps).
   Apply its "Retention-informed edit defaults": cold open = the episode's best
   60–90 s + tease the finale, first real segment by ~2 min, 45–55 min target.
3. **Publish the episode FIRST** (`yt_upload.py`, scheduled-private), then backfill
   `episodes/epN/segment-times.md` from the live copy (`yt_fetch.py`).
4. **Clip** with `clipify`: personality/one-liner picks over concepts, 10–20 s
   verticals, long pulls titled `<Hook> - Ep N Clip` (never "Highlight -").
   Upload staggered (house pattern: daily 2 PM PT = 21:00 UTC), then work the
   FUNNEL CHECKLIST the uploader prints — related video, pinned comment with
   episode link + timestamp, end screens. That checklist is manual and is the
   channel's weakest metric; don't let it slide.
5. **Weekly review** with `channel-analytics` (SKILL.md → "Weekly review"):
   pull → update insights (deltas, ✓/◐ statuses, experiments) → render → publish
   to https://jacksoncook.github.io/pod-analytics-latest/ (sibling repo) → commit
   both repos. Run it after each episode drops; light mid-week pulls are fine when
   fresh data lands (e.g. first impressions/CTR backfill).

## Conventions / gotchas
- **Clip titles:** hook first, `- Ep N Clip` suffix — the "Highlight -" prefix is
  banned (data-backed; `yt_upload.py` lints for it). No `#Shorts` in titles; the
  `#shorts` hashtag goes on the description's last line.
- **`segment-times.md` reflects the ACTUAL published YouTube copy** (pulled via
  `yt_fetch.py`), in one consistent template across episodes — not pre-pro drafts.
- **Captions:** upload the SRT regenerated from the FINAL cut, never the raw recording
  (raw order/timing predates the reorder — caused the Ep 1 caption desync).
- **A/V drift:** use the frame-exact `-frames:v` + PTS-restamp recipe (podcast-video-edit
  SKILL.md → Gotchas). Always verify sync at a LATE point, not just total duration.
- **Secrets** live in `~/.config/clipify-youtube/` (client_secret.json, tokens) — NEVER
  commit them; `.gitignore` guards `client_secret*.json` / `token.json` / `*.results.json`.
- **Commits:** solo repo, direct to `main`.

## New machine
`git clone` → `bash setup.sh` (ffmpeg + whisper-cpp + model + Pillow) → copy `media/`
back from backup → re-do the OAuth (youtube-setup.md). See README → "Moving off this
machine" for the full checklist.
