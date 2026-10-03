# TikTok — @permanentunderpod

Posting sheet for TikTok. Every clip goes to TikTok (house rule since 2026-10-03):
`tt_enqueue.py` adds an episode's YouTube manifest to `media/clips/tiktok/queue.json`, and
`tt_upload.py` schedules every pending item in TikTok Studio in one pass (clipify step 5).
Live state: `media/clips/tiktok/*.results.json`.

## Batch 1 — top 7 YouTube Shorts by lifetime views (pulled 2026-10-03)

| Day | Short (YT rank · views) | File | TikTok |
|---|---|---|---|
| Fri Oct 3 | Claude helps decipher lottery ticket (1 · 1,304) | ep1/short-lottery-ticket | https://www.tiktok.com/@permanentunderpod/video/7692560210329701634 (posted 5:42 PM ET) |
| Sat Oct 4 | Make me a millionaire (2 · 1,216) | ep9/short1-make-me-a-millionaire | https://www.tiktok.com/@permanentunderpod/video/7692590170503122198 (scheduled 17:00 ET) |
| Sun Oct 5 | Name one programmer better than Fable (3 · 1,168) | ep13/short1-i-know-zero | https://www.tiktok.com/@permanentunderpod/video/7692590318918700310 (scheduled 17:00 ET) |
| Mon Oct 6 | Baby egg allergy test (4 · 1,152) | ep8/short3-seven-times-one-evening | https://www.tiktok.com/@permanentunderpod/video/7692590462128934166 (scheduled 17:00 ET) |
| Tue Oct 7 | AI 25x long the yen, R-E-K-T (5 · 1,087) | ep15/short1-rekt-25x | https://www.tiktok.com/@permanentunderpod/video/7692590659961752854 (scheduled 17:00 ET) |
| Wed Oct 8 | "Astra is my top guy" (6 · 1,051) | ep14/short2-top-guy | https://www.tiktok.com/@permanentunderpod/video/7692590859979722006 (scheduled 17:00 ET) |
| Thu Oct 9 | Rolled dice 100 times (7 · 1,011) | ep9/short3-rolled-dice-100-times | https://www.tiktok.com/@permanentunderpod/video/7692591063843802390 (scheduled 17:00 ET) |

- Captions live in the manifest: hook + "Full episode: Permanent Underpod" + 3–4 hashtags.
- The Ep 1 short had no local master; it was pulled from YouTube with yt-dlp (1080x1920 h264).
- Live state after each post: `media/clips/tiktok/manifest.json.results.json` and `tt_upload.log`.
- Owed (manual, Jackson): YouTube channel link in the TikTok bio.

## Ep 17 clips — 4 PM PT daily (two hours after the top-7 slot)

| Day | Clip | TikTok |
|---|---|---|
| Fri Oct 3 | short1-chopstick | https://www.tiktok.com/@permanentunderpod/video/7692580371065539862 (posted 7:00 PM ET) |
| Sat Oct 4 | short3-resume | https://www.tiktok.com/@permanentunderpod/video/7692591257998216470 (scheduled 19:00 ET) |
| Sun Oct 5 | short5-trump-account | https://www.tiktok.com/@permanentunderpod/video/7692591528853736726 (scheduled 19:00 ET) |
| Mon Oct 6 | short6-telescope | https://www.tiktok.com/@permanentunderpod/video/7692591710354066710 (scheduled 19:00 ET) |
| Tue Oct 7 | short10-captcha | https://www.tiktok.com/@permanentunderpod/video/7692591864586800406 (scheduled 19:00 ET) |
| Wed Oct 8 | short7-headline-inflation | https://www.tiktok.com/@permanentunderpod/video/7692592071126928643 (scheduled 19:00 ET) |
| Thu Oct 9 | short2-cig-order | https://www.tiktok.com/@permanentunderpod/video/7692592282758810902 (scheduled 19:00 ET) |

Same seven as the YouTube release, same order. Holds (short4, short11) stay held.
