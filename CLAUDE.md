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
- **clipify**: `clipify.py` cuts clips; `yt_upload.py` publishes (scheduled-private,
  auto-publish at a `publishAt`); `yt_fetch.py` reads back live video metadata. One-time
  OAuth setup is in `.claude/skills/clipify/youtube-setup.md`.

## Conventions / gotchas
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
