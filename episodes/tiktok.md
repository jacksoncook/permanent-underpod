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

## Ep 18 clips — 4 PM PT daily (19:00 ET)

| Day | Clip | TikTok |
|---|---|---|
| Sat Oct 10 | short6-half-a-cigarette | https://www.tiktok.com/@permanentunderpod/video/7694712381988982038 (scheduled 19:00 ET) |
| Sun Oct 11 | short4-economy-crash-bro | https://www.tiktok.com/@permanentunderpod/video/7694712584733429015 (scheduled 19:00 ET) |
| Mon Oct 12 | short9-unemployed-brother | https://www.tiktok.com/@permanentunderpod/video/7694712743399673110 (scheduled 19:00 ET) |
| Tue Oct 13 | short1-36-doubles | https://www.tiktok.com/@permanentunderpod/video/7694713001366097175 (scheduled 19:00 ET) |
| Wed Oct 14 | short2-kendrick-on-drake | https://www.tiktok.com/@permanentunderpod/video/7694713295663680790 (scheduled 19:00 ET) |
| Thu Oct 15 | short11-bank-history-slack | https://www.tiktok.com/@permanentunderpod/video/7694713478187093270 (scheduled 19:00 ET) |
| Fri Oct 16 | short3-one-guy-at-cloudflare | https://www.tiktok.com/@permanentunderpod/video/7694713716922797334 (scheduled 19:00 ET) |
| Sat Oct 17 | short8-drool-and-youtube | https://www.tiktok.com/@permanentunderpod/video/7694714253617401110 (scheduled 19:00 ET) |
| Sun Oct 18 | short10-gpu-farm | https://www.tiktok.com/@permanentunderpod/video/7694714508736154902 (scheduled 19:00 ET) |
| Mon Oct 19 | short5-browser-history | not yet scheduled: beyond Studio's 10-day window on Oct 9; rerun `tt_upload.py` on/after Oct 10 |
| Tue Oct 20 | short7-feudal-salesforce | not yet scheduled: beyond Studio's 10-day window on Oct 9; rerun `tt_upload.py` on/after Oct 10 |

Same eleven as the YouTube release, same order, two hours after the 2 PM PT YouTube slot. Nine
scheduled 2026-10-09; the last two sit outside TikTok Studio's 10-day scheduling window and need a
rerun of `tt_upload.py media/clips/tiktok/queue.json` once inside it (the script skips them as
"later" and picks them up unchanged).

## Ep 19 clips — two a day, 6 PM + 8 PM PT (21:00 / 23:00 ET), Oct 16–21

Jackson: "start today, double up … lets see if we get banned again." Per-item `postHourLocal` (new) puts
them beside Ep 18's 19:00 slot (through Oct 20). All twelve fit TikTok's 10-day window in one pass. The
two Ep 18 stragglers (short5-browser-history Oct 19, short7-feudal-salesforce Oct 20) ride the same run.

| Slot | Clip | TikTok |
|---|---|---|
| Fri Oct 16 21:00 ET | short9-horcruxing-himself | https://www.tiktok.com/@permanentunderpod/video/7697169698907065622 (scheduled 21:00 ET) |
| Fri Oct 16 23:00 ET | short10-butter-hostage | https://www.tiktok.com/@permanentunderpod/video/7697171283305352470 (scheduled 23:00 ET) |
| Sat Oct 17 21:00 ET | short8-goblin-in-my-toaster | https://www.tiktok.com/@permanentunderpod (row link not found yet) (scheduled 21:00 ET) |
| Sat Oct 17 23:00 ET | short4-chris-wallet | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Sun Oct 18 21:00 ET | short3-talking-like-cockroach | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Sun Oct 18 23:00 ET | short7-not-good-buddy | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Mon Oct 19 21:00 ET | short12-ken-griffin-took-us-out | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Mon Oct 19 23:00 ET | short5-store-sells-the-scales | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Tue Oct 20 21:00 ET | short1-haiku-or-fable | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Tue Oct 20 23:00 ET | short2-perp-of-fortune-index | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Wed Oct 21 21:00 ET | short6-saasless-dude | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |
| Wed Oct 21 23:00 ET | short11-half-a-token-a-second | PENDING — session logged out mid-run; re-clone cookies and rerun `tt_upload.py` |

- Run 1 (03:49 ET): item 1 scheduled, but Studio listed its row late and the 120 s row check aborted
  the run; URL recovered from the list. `wait_for_posts_list` now reloads the list every 30 s.
- Run 2 (03:53 ET): items 2–3 scheduled (item 3's row link not found yet), then the session was
  logged out server-side on item 4 (`/login` redirect; Chrome Profile 1 holds the same Oct 3
  sessionid, so it is logged out too). Owed: Jackson logs into TikTok in Chrome, re-clone the Cookies
  file, rerun `tt_upload.py media/clips/tiktok/queue.json` for the remaining 9 + the 2 Ep 18 items.

## Ep 20 clips — 4 PM PT daily (19:00 ET, the queue default), Oct 24 – Nov 5

Enqueued 2026-10-24 from `media/clips/ep20/upload-manifest.json` (13 items, one per day, same day as the
YouTube release). Session: the clone was logged out again (server-side, 10/16); cookie cloning from Chrome is blocked by
macOS TCC for this process, Finder and Terminal alike, and Chrome 155 refuses a DevTools port on the
default profile. Fix that worked: open the clone profile headful on the login page and have Jackson log in
there. Scheduling run 2026-10-24 ~04:30 ET: `tt_upload.py queue.json --headful --slow 3 --pause 900`, one
browser session, 15–30 min between clips (Jackson: "be careful not to trigger bot detection", "go a little
slower", "we don't gotta close the browser after each vid"). Nov 3–5 fall outside the 10-day window
until Oct 26; rerun then. Log: `media/clips/ep20/_tiktok.log`; URLs land in `queue.json.results.json`.

The 11 Ep 18/19 items that never got scheduled (Oct 17–21) are retired in `queue.json.results.json`
(`dropped: true`; Jackson 10/24: "lets just do ep 20").
