# TikTok — @permanentunderpod

Posting sheet for TikTok. Every clip goes to TikTok (house rule since 2026-10-03):
`tt_enqueue.py` adds an episode's YouTube manifest to `media/clips/tiktok/queue.json`, and
LaunchAgent `com.jcook.underpod.tiktok-daily` posts one queue item per day at 4 PM PT
(`postHourLocal` 19 ET). The one-off top-7 batch below runs from `manifest.json` at 2 PM PT.

## Batch 1 — top 7 YouTube Shorts by lifetime views (pulled 2026-10-03)

| Day | Short (YT rank · views) | File | TikTok |
|---|---|---|---|
| Fri Oct 3 | Claude helps decipher lottery ticket (1 · 1,304) | ep1/short-lottery-ticket | https://www.tiktok.com/@permanentunderpod/video/7692560210329701634 (posted 5:42 PM ET) |
| Sat Oct 4 | Make me a millionaire (2 · 1,216) | ep9/short1-make-me-a-millionaire | scheduled |
| Sun Oct 5 | Name one programmer better than Fable (3 · 1,168) | ep13/short1-i-know-zero | scheduled |
| Mon Oct 6 | Baby egg allergy test (4 · 1,152) | ep8/short3-seven-times-one-evening | scheduled |
| Tue Oct 7 | AI 25x long the yen, R-E-K-T (5 · 1,087) | ep15/short1-rekt-25x | scheduled |
| Wed Oct 8 | "Astra is my top guy" (6 · 1,051) | ep14/short2-top-guy | scheduled |
| Thu Oct 9 | Rolled dice 100 times (7 · 1,011) | ep9/short3-rolled-dice-100-times | scheduled |

- Captions live in the manifest: hook + "Full episode: Permanent Underpod" + 3–4 hashtags.
- The Ep 1 short had no local master; it was pulled from YouTube with yt-dlp (1080x1920 h264).
- Live state after each post: `media/clips/tiktok/manifest.json.results.json` and `tt_upload.log`.
- Owed (manual, Jackson): YouTube channel link in the TikTok bio; check Oct 4 post landed.

## Ep 17 clips — standing queue, 4 PM PT daily (two hours after the top-7 slot)

| Day | Clip | TikTok |
|---|---|---|
| Fri Oct 3 | short1-chopstick | queued |
| Sat Oct 4 | short3-resume | queued |
| Sun Oct 5 | short5-trump-account | queued |
| Mon Oct 6 | short6-telescope | queued |
| Tue Oct 7 | short10-captcha | queued |
| Wed Oct 8 | short7-headline-inflation | queued |
| Thu Oct 9 | short2-cig-order | queued |

Same seven as the YouTube release, same order. Holds (short4, short11) stay held.
