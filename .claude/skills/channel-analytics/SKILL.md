---
name: channel-analytics
description: Pull YouTube channel + per-video performance data (views, watch time, retention curves, traffic sources, daily timeseries) and build a branded HTML report with improvement insights for the channel and the pod. Use when asked to analyze the channel, review video performance, check retention/stats, or figure out how to improve the show.
---

# channel-analytics — how is the show doing, and what do we change?

Three steps: **pull data → write insights → render report**. The scripts do 1 and 3;
the analysis in step 2 is yours (the LLM/human) — that's the point of the skill.

## 0. Prereqs
Same OAuth client as clipify (`~/.config/clipify-youtube/client_secret.json`), run
scripts with the uploader venv's python: `~/.config/clipify-youtube/.venv/bin/python`.
This skill uses its own token (`token_analytics.json`, scopes: `youtube.readonly` +
`yt-analytics.readonly`). First run opens a browser — **the user must pick the
Permanent Underpod BRAND channel on the channel-selection screen**, not the personal
account. Always pass `--expect-channel "Permanent Underpod"` so a wrong pick fails
loudly (token auto-deleted) instead of silently reading the wrong channel.

## 1. Pull
```bash
~/.config/clipify-youtube/.venv/bin/python \
  .claude/skills/channel-analytics/scripts/yt_pull.py \
  analytics/channel-data.json --expect-channel "Permanent Underpod"
```
Produces one JSON: channel totals, every video (metadata + public stats + lifetime
analytics: watch min, avg view duration/%, shares, subs gained), **audience-retention
curves for long-form videos**, daily views/subs timeseries, traffic-source breakdown.
Quota cost is trivial (all reads); no upload-quota impact.

## 2. Analyze → write `analytics/insights.json`
Read the pulled JSON and write insights per `examples/insights.example.json`:
`headline`, `channel[]` (packaging/distribution: titles, thumbnails, shorts strategy,
cadence, SEO), `pod[]` (the show itself: length, segment order, hooks, pacing), and
optional `experiments[]`. Every item needs `evidence` citing actual numbers/videos.

The highest-value move: **map retention-curve drop-offs to segments** using the
episode's `episodes/epN/segment-times.md` chapter timestamps — "viewers bail at 38%
of Ep 4" becomes "viewers bail when segment X starts". Do this for every episode
that has a retention curve.

## 3. Render + open
```bash
python3 .claude/skills/channel-analytics/scripts/report.py \
  analytics/channel-data.json analytics/insights.json analytics/report.html \
  --logo brand/logo-480.png
open analytics/report.html
```
Self-contained dark-brand HTML (logo embedded; Chart.js from CDN, so viewing needs
network). Charts: views per video, daily views + net subs, traffic sources,
retention curves overlaid per episode; then the insight cards and a full video table.

## Gotchas
- **Scheduled/private videos** appear in the table (flagged) but have ~no analytics
  yet — don't read their zeros as failure.
- **Retention needs views**: low-view videos may return no curve (script skips
  gracefully). `relativeRetentionPerformance` (vs-typical) is fetched when the API
  allows, else curve-only.
- **Shorts detection is a heuristic** (≤183 s ⇒ short); a genuinely short landscape
  clip would be mislabeled.
- **Impressions/CTR** come from the **YouTube Reporting API** (added Jan 2026;
  report type `channel_reach_basic_a1` — they are NOT in the Analytics query API).
  `yt_pull.py` handles it: first run creates the report job, later runs download the
  daily CSVs and merge per-video `reach: {impressions, ctr_pct}`. Expect ~48 h before
  the first reports exist (with ~30-day backfill); until then reach is null — say
  "no CTR data yet", don't invent numbers. Requires `youtubereporting.googleapis.com`
  enabled in the Cloud project (the script prints the enable URL on 403).
- Token expiry: if the OAuth consent screen is still in Testing mode, refresh tokens
  die after 7 days — re-auth or publish the app (see memory / clipify youtube-setup.md).
- Data lands in `analytics/` (committable — it's our own channel's data; no secrets).
