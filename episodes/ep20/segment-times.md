# Permanent Underpod — Ep 20 — Segment Times

**Final cut: 52:52 · fully-remote episode, three StreamYard cams (offsets 0 / −0.021 / +0.030
from the filename deltas) plus Chris's screen share of the Perp of Fortune 2.0 dashboard: full-frame
at the reveal, then a persistent top-right PiP of the two position cards for the rest of the show ·
three-beat 36 s cold open · title card · end card · whoosh + gold wipe on all 9 transitions · three
LIKE + SUBSCRIBE pop-ups · Jackson's track dereverbed (WPE + expander, Ep 18 recipe), Chris's mic
EQ'd at source · ~8.7 min of content removed, 21 dead-air pauses trimmed (29 s).**

## Episode video

- **URL:** https://youtu.be/MdZKvp8GZkE — live 2026-10-23 as "A Certificate Authority Used ‘4’ as Its "Private Key""
  (Jackson's manual upload, description = the sheet's draft). API-patched 2026-10-24: `standard` caption track
  from the final-cut SRT, 15 tags (force-ssl token survived).
- **File:** `media/ep20/Permanent Underpod - Ep 20 (Final Cut).mp4`
- **Thumbnail:** `media/ep20/ep20-thumbnail.png` — "THE KEY WAS 4" (Chris center with his hands on
  his head at the countdown, Tyler left, Jackson right; passed the 320×180 shrink test).
- **Loudness:** delivered −15.5 LUFS integrated, −2.3 dBTP, LRA 4.1 (chain in `render.json`: Ep 19 front-end with the 6.8 kHz dynamic de-esser, target_lufs −11.8 / limit 0.7). (chain in `render.json`: Ep 19 front-end with the 6.8 kHz dynamic de-esser, target_lufs −11.8 / limit 0.7).
- **Sync check:** final audio cross-correlated against `edited_raw.mov` at 1:40, 10:00, 25:00, 40:00, 50:00 and 52:20 — lag a constant 35 ms at every point (same as Ep 15–19; no drift). Pop-up SFX cross-correlated at each LIKE + SUBSCRIBE window: peak within 22 ms of the animation start.
- **LIKE + SUBSCRIBE:** pop-up on frame at 2:02.3, 30:57.0 (on Jackson's spoken "viewer, please like
  and subscribe") and 50:46.8, SFX paired in each window. Dashboard PiP on frame from 29:00 to the
  end card.
- **Captions:** `episodes/ep20/transcript-attributed.srt` — regenerated from the FINAL cut.

## Title (drafts)

1. **A Root Certificate Authority Picked the Number 4 as Its Private Key**
2. The Key Was 4: Trusted by Your OS for 17 Months
3. 67% of the Web Had Remote Code Execution This Week (PHP2Shell)
4. Is the Future of Finance on Hyperliquid?

## YouTube description (paste-ready draft)

```
⏩ The key of 4 is at 2:30. PHP2Shell at 12:58. Perp of Fortune 2.0 at 27:22.

A root certificate authority, the kind your Linux distro ships trust for, generated its 256-bit private key by picking a number between 0 and 256. It was 4. Tyler walks through what that does to a key that needed 384 bits of entropy, Chris explains why Cloudflare points cameras at lava lamps, and the cert stayed live and trusted for 17 months. Then PHP2Shell: two CVEs, CVSS 9.2, unauthenticated remote code execution on roughly two thirds of the web, Wikipedia down, and Chris offering to remote-execute into your server and hotfix it for you. Jackson's side project got poked by white hats the same week. Then the leak: three months of secret coordination before the patch, and who gets told first. Perp of Fortune 2.0: two bets on Tyler's money, an hourly Bitcoin binary and a 25× long on ETH, with the dashboard on screen all episode and a 45-second countdown nobody could read. Vitalik's paranoid mode: a five-layer private AI stack (local model, offline Wikipedia, sandbox, zkAPI) to find a vegan restaurant. The models refuse to help with cryptography. Chris rooted his Samsung TV and found out who it was talking to. Railway got popped through its build pipeline. The marquee: Jeff Yan says the future financial system runs on Hyperliquid. Is that bonkers, or BitMEX → FTX → Binance → Hyperliquid, the same trade again? Final numbers: the binary went to zero, the ETH long bled, we lost $29.

🔥 On the Agenda
0:00 Cold open
0:41 Welcome: chamomile, toasted coffee, no Cheez-Its
1:23 A root certificate authority used a private key of 4
8:17 Less than a PIN: live for 17 months, trusted by your OS
12:58 PHP2Shell: remote code execution on 67% of the web
17:05 A DeepSeek swarm patching PHP servers for you
20:09 White hats are prodding Jackson's MotivateMe.io
22:15 The PHP leak: three months of secret coordination, and who gets told first
24:44 Quest got hacked: is privacy already gone?
26:15 Contrarian corner: nobody cares about privacy
27:22 Perp of Fortune 2.0: hourly Bitcoin binary vs LONG ETH 25×
31:20 Vitalik's paranoid mode: five layers to find a vegan restaurant
36:35 Refusals: the models won't touch cryptography
37:58 He rooted his Samsung TV and found it listening
40:40 Bitcoin UP is winning: "Guess who's out of the underclass"
41:13 Railway got popped: CI keys and a staker's time lock
43:27 We have a TikTok. The binary has 45 seconds left.
44:55 Is the future of finance on Hyperliquid?
47:10 "The nodes are in various corners of his basement"
49:28 BitMEX, FTX, Binance, Hyperliquid: the same trade
51:46 Perp final: the binary went to zero

Recorded fully remote, three cameras, one dashboard.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment.

GLOSSARY
• Root certificate authority (CA): one of the ~150 organizations whose signing keys your OS and browser trust by default. Everything below it inherits that trust.
• Entropy: the unpredictability in a key, measured in bits. A 256-bit key chosen from 0–256 has 8 bits; 384 were needed.
• CVE / CVSS: the public ID for a vulnerability and its 0–10 severity score. PHP2Shell's two CVEs scored 9.2.
• Remote code execution (RCE): a bug that lets an attacker run their own code on your server. The worst class there is.
• IDOR: insecure direct object reference, changing an ID in a URL and getting someone else's data back. What the white hats found on MotivateMe.
• Responsible disclosure / embargo: telling the vendor first and holding the details until a patch ships. PHP2Shell's lasted three months.
• Perp of Fortune 2.0: our tiny real-money account; this week two bets on Tyler's money, an hourly Bitcoin binary and a 25× ETH long, picked by a model.
• Binary option: a bet that pays out fixed money if a condition is true at settlement (Bitcoin UP in the next hour) and zero if not.
• 25× leverage: borrowing to open a position 25 times your margin. A 4% move the wrong way wipes it.
• zkAPI: Vitalik's proposal to pay for inference from an on-chain vault via a zero-knowledge proof so the lab can't tie the bill to you.
• Rooting: taking admin control of a device the maker locked down, here a Samsung TV.
• CI / build pipeline: the servers that compile and ship a company's code. Railway's were the way in.
• Hyperliquid: an exchange that runs as its own chain with the order book on the ledger. Jeff Yan is its founder.

🔔 Subscribe for next week: Poppy 0.2 vs Claude Duet, who gets to shop for you; Liquid, the layer two that isn't one; the fake adoption numbers (8 million payments for $648 of fees); Perp of Fortune 2.0 rides again.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (3 beats: Tyler on the 256-bit key picked between 0 and 256, "ten to the 250 less secure" · Tyler: "Wow, long ETH 25×, and we're losing money on both" · the 45-second binary countdown, "negative 25 or positive 25… who coded this crap?") |
| 0:36 | Title card |
| 0:41 | Welcome: chamomile tea, toasted coffee, zero Cheez-Its; the week's three extreme vulnerabilities; "is the cert being a four extremely real?" |
| 1:23 | The root CA that used a private key of 4; Tyler out of his depth on the maths; "001 and then 253 zeros?" |
| 8:17 | Less than a PIN: live and trusted for 17 months; Cloudflare's lava lamps; recursive trust |
| 12:58 | PHP2Shell: two CVEs, CVSS 9.2 ("like the Richter scale"), remote code execution on 67% of the web, Wikipedia down |
| 17:05 | A DeepSeek swarm patching PHP servers for you; "is Chris's toaster using PHP?"; "the perfect swarm" |
| 20:09 | White hats are prodding Jackson's MotivateMe.io: a shredded photo of you every workout day |
| 22:15 | The PHP leak: three months of secret coordination before the patch, who gets told first; Anthropic's CISO: expect 18 months of this |
| 24:44 | Quest got hacked: is privacy already gone? |
| 26:15 | Contrarian corner: nobody cares about privacy; "a super spreader of instinct" |
| 27:22 | Perp of Fortune 2.0: dashboard reveal, then PiP; an hourly Bitcoin binary and a 25× ETH long on Tyler's money; Opus 5.5 "a modern day poet"; "viewer, please like and subscribe if you love watching us lose money" |
| 31:20 | Vitalik's paranoid mode: local Qwen, offline Wikipedia, a sandbox and zkAPI to find a vegan restaurant; "there's no way this is practical"; "Plato's cave, but for agents" |
| 36:35 | Refusals: the models won't touch cryptography; "find people encrypting with the number four" |
| 37:58 | Chris rooted his Samsung TV: always listening, sent to Samsung for ads; "how many mics are in this room? eight" |
| 40:40 | Bitcoin UP is winning: "+$14.91, out of the permanent underclass" |
| 41:13 | Railway got popped: the build pipeline, CI keys, a staker's time lock, 24 h before disclosure |
| 43:27 | We have a TikTok (one follower, an egg app). The binary has 45 seconds left: the countdown nobody could read |
| 44:55 | THE MARQUEE: is the future of finance on Hyperliquid? Jeff Yan's interview; Tyler: "quite comical" |
| 47:10 | "The nodes are in various corners of his basement"; all of finance on one ledger is a giant data center |
| 49:28 | BitMEX → FTX → Binance → Hyperliquid, the same trade; "a year in jail for $100 million?" |
| 51:46 | Perp final: the binary went to zero (−$23.49), the ETH long −$3.85; "do not counterparty Wintermute"; "please patch yourself" |
| 52:45 | End card (Poppy 0.2 vs Claude Duet · Liquid · fake adoption numbers · Perp of Fortune 2.0 · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock seconds
(Jackson's track). Rows marked **continuous** are topic wipes on unbroken source. Every splice sits
at the midpoint of a measured all-silent union gap (`check_bounds.py --plan`) except the edges pinned
with `hard_m0`/`hard_m1` (crosstalk removals, with the overlapping mic muted for the edge); content
cuts were micro-whispered at both edges (`mw.sh`).

| Final | What | src out → src in |
|---|---|---|
| 0:00.00 | cold open beat 1 (the key picked from 0–256) | → 227.60 |
| 0:19.40 | cold open beat 2 (long ETH 25×) | 247.00 → 1954.24 |
| 0:23.57 | cold open beat 3 (the countdown) | 1958.40 → 3085.62 |
| 0:36.43 | title card | 3098.5 → |
| 0:40.93 | welcome | → 0.00 |
| 1:27.07 | dead-air trim (1.63 s) | 46.12 → 47.75 |
| 2:30.17 | 26 s of intro crosstalk removed; in on Tyler's cert explainer | 110.86 → 136.76 |
| 3:41.37 | dead-air trim (0.82 s) | 207.97 → 208.79 |
| 9:13.10 | dead-air trim (1.56 s) | 540.54 → 542.10 |
| 9:55.63 | dead-air trim (1.09 s) | 584.65 → 585.74 |
| 11:34.10 | 43 s removed around the cert wrap; out after "it remains to be seen" (hard edge) | 684.22 → 726.91 |
| 12:58.33 | 43 s removed; out after "maybe the people who did it screwed you" (hard edge, Tyler muted), in on "Speaking of vulnerabilities" | 811.15 → 854.01 |
| 15:50.73 | dead-air trim (0.93 s) | 1026.41 → 1027.34 |
| 16:14.60 | dead-air trim (1.31 s) | 1051.22 → 1052.53 |
| 17:01.13 | dead-air trim (1.38 s) | 1099.06 → 1100.44 |
| 18:00.87 | dead-air trim (1.25 s) | 1160.16 → 1161.41 |
| 18:11.30 | dead-air trim (0.97 s) | 1171.84 → 1172.81 |
| 22:11.40 | dead-air trim (2.37 s) | 1412.92 → 1415.29 |
| 22:14.67 | Patch the Planet / Glasswing explainer removed (74 s); out after "less itchy", in on Tyler's "one interesting detail of the PHP one" | 1418.55 → 1492.18 |
| 24:11.60 | 38 s removed; in on Tyler's CISO line (Jackson muted on the in) | 1609.10 → 1647.06 |
| 25:44.77 | dead-air trim (0.99 s) | 1740.23 → 1741.22 |
| 25:46.70 | dead-air trim (1.54 s) | 1743.14 → 1744.68 |
| 27:21.73 | PHP block → Perp of Fortune — continuous | 1839.71 → 1839.71 |
| 29:44.83 | dead-air trim (1.15 s) | 1982.80 → 1983.95 |
| 30:47.67 | dead-air trim (1.38 s) | 2046.77 → 2048.15 |
| 34:31.57 | 53 s of perp crosstalk removed; in on Jackson's Vitalik setup (Chris muted on the in) | 2272.05 → 2325.13 |
| 37:19.03 | Vitalik tangent removed (1:30); in on the Samsung TV (hard edge, Chris muted) | 2492.60 → 2583.08 |
| 39:31.10 | dead-air trim (1.58 s) | 2715.14 → 2716.72 |
| 39:56.70 | dead-air trim (1.39 s) | 2742.32 → 2743.71 |
| 40:18.63 | 41 s removed; in on Bitcoin UP winning | 2765.65 → 2806.35 |
| 40:37.47 | dead-air trim (2.09 s) | 2825.20 → 2827.29 |
| 43:04.27 | dead-air trim (2.23 s) | 2974.08 → 2976.31 |
| 43:17.03 | 51 s removed; out after "Vitalik is losing his mind right now" (hard edge, Jackson muted), in on "Well, that's an action item on Chris" (Chris muted) | 2989.07 → 3039.70 |
| 45:33.97 | dead-air trim (1.58 s) | 3176.62 → 3178.20 |
| 46:29.13 | dead-air trim (0.91 s) | 3233.36 → 3234.27 |
| 49:11.70 | 57 s removed; out after "didn't sound that cool to me, or novel" (Chris muted), in on the Hyperliquid marquee (hard edge) | 3396.85 → 3453.90 |
| 51:07.23 | dead-air trim (1.22 s) | 3569.43 → 3570.65 |
| 51:22.47 | 43 s removed; in on the perp final (hard edges, Chris muted) | 3585.87 → 3629.20 |
| 52:45.37 | end card; "farewells" is the last line | 3712.1 → |

## Spotify description (paste-ready draft)

```
A root certificate authority, the kind your Linux distro ships trust for, generated its 256-bit private key by picking a number between 0 and 256. It was 4. Tyler walks through what that does to a key that needed 384 bits of entropy, Chris explains why Cloudflare points cameras at lava lamps, and the cert stayed live and trusted for 17 months. Then PHP2Shell: two CVEs, CVSS 9.2, unauthenticated remote code execution on roughly two thirds of the web, Wikipedia down, and Chris offering to remote-execute into your server and hotfix it for you. Jackson's side project got poked by white hats the same week. Then the leak: three months of secret coordination before the patch, and who gets told first. Perp of Fortune 2.0: two bets on Tyler's money, an hourly Bitcoin binary and a 25× long on ETH, with a 45-second countdown nobody could read. Vitalik's paranoid mode: a five-layer private AI stack to find a vegan restaurant. The models refuse to help with cryptography. Chris rooted his Samsung TV and found out who it was talking to. Railway got popped through its build pipeline. The marquee: Jeff Yan says the future financial system runs on Hyperliquid. Is that bonkers, or BitMEX → FTX → Binance → Hyperliquid, the same trade again? Final numbers: the binary went to zero, the ETH long bled, we lost $29.

The key of 4 is at 2:30. Chapters: Cold open (0:00) · Welcome: no Cheez-Its (0:41) · A root CA used a private key of 4 (1:23) · Live for 17 months, trusted by your OS (8:17) · PHP2Shell: remote code execution on 67% of the web (12:58) · A DeepSeek swarm patching PHP for you (17:05) · White hats prodding MotivateMe.io (20:09) · The PHP leak: three months of secret coordination, and who gets told first (22:15) · Quest got hacked: is privacy already gone? (24:44) · Contrarian corner: nobody cares about privacy (26:15) · Perp of Fortune 2.0: hourly Bitcoin binary vs LONG ETH 25× (27:22) · Vitalik's paranoid mode (31:20) · Refusals: the models won't touch cryptography (36:35) · He rooted his Samsung TV (37:58) · Bitcoin UP is winning (40:40) · Railway got popped (41:13) · We have a TikTok; 45 seconds left (43:27) · Is the future of finance on Hyperliquid? (44:55) · The nodes are in his basement (47:10) · BitMEX, FTX, Binance, Hyperliquid: the same trade (49:28) · Perp final: the binary went to zero (51:46)

Recorded fully remote, three cameras, one dashboard. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. Glossary: Root CA = one of the ~150 organizations whose signing keys your OS and browser trust by default. Entropy = the unpredictability in a key, in bits; a key chosen from 0–256 has 8, 384 were needed. CVE / CVSS = a vulnerability's public ID and its 0–10 severity score. RCE = remote code execution, running attacker code on your server. IDOR = changing an ID in a URL and getting someone else's data back. Embargo = holding vulnerability details until the patch ships. Binary option = a fixed payout if a condition is true at settlement, zero if not. 25× leverage = a position 25 times your margin; a 4% move wipes it. zkAPI = paying for inference from an on-chain vault via a zero-knowledge proof so the lab can't tie the bill to you. Rooting = taking admin control of a locked-down device. CI pipeline = the servers that build and ship a company's code. Hyperliquid = an exchange that runs as its own chain with the order book on the ledger.

Subscribe for next week: Poppy 0.2 vs Claude Duet, who gets to shop for you; Liquid, the layer two that isn't one; the fake adoption numbers; Perp of Fortune 2.0 rides again.
```

## Captions

`transcript-attributed.srt` regenerated from the FINAL cut (never the raw recording) in
`episodes/ep20/`. Uploaded as the `standard` track 2026-10-24 (`yt_captions.py`).

## Clips

Thirteen vertical Shorts cut 2026-10-24 from `edited_raw.mov` with the episode audio chain, face-crop
hard cuts, branded ender. `verify_clips.py --whisper` pre and `--rendered` post: 0 failures (short5's
tail warning is a declared override: whisper puts "patched." complete at 1082.65, 80 ms gap, next word
at 1082.74). Uploaded scheduled-private to Underpod Shorts, one a day at 2 PM PT from Oct 24 to Nov 5
(21:00 UTC, 22:00 UTC from Nov 1). Spec `media/clips/ep20/clips.json` (built from `picks.json`), copy in
`media/clips/ep20/posting-copy.md`, receipts in `media/clips/ep20/upload-manifest.json.results.json`.

| Release | Clip | Final-cut in–out | Title | URL |
|---|---|---|---|---|
| 2026-10-24 2 PM PT | `short4-hotfix-it-for-you` | 1009.4000–1021.1000 (11.7 s) | I'll Remote-Execute Into Your Server and Fix It for You | https://youtu.be/qXPoBBtMT4A |
| 2026-10-25 2 PM PT | `short9-egg-tracking-follower` | 2612.6400–2628.8000 (16.2 s) | Our Only TikTok Follower Is an Egg Tracking App | https://youtu.be/DqGMG3r0v2Y |
| 2026-10-26 2 PM PT | `short10-who-coded-this-crap` | 2634.7700–2654.9000 (20.1 s) | 40 Seconds Left on a $25 Bitcoin Coin Flip | https://youtu.be/jL1Yu4w5TIE |
| 2026-10-27 2 PM PT | `short1-five-is-legit` | 303.7000–322.5000 (18.8 s) | A Certificate Authority's Private Key Was 4 | https://youtu.be/ohDSZRkqoUQ |
| 2026-10-28 2 PM PT | `short7-eight-microphones` | 2354.1900–2370.7900 (16.6 s) | It Was the TV Listening the Whole Time | https://youtu.be/SXQctwfUdLk |
| 2026-10-29 2 PM PT | `short12-jail-for-a-year` | 3033.0300–3056.6000 (23.6 s) | Would You Do a Year in Jail for $100M? | https://youtu.be/RAY1vqA7T0M |
| 2026-10-30 2 PM PT | `short5-dont-tell-claude` | 1060.5100–1082.7000 (22.2 s) | Don't Tell Claude About the PHP Bug | https://youtu.be/wdwzrDv3-qc |
| 2026-10-31 2 PM PT | `short2-less-than-a-pin` | 510.6400–522.8700 (12.2 s) | Your iPhone PIN Is More Secure Than This Root CA | https://youtu.be/LKDFWThMz_g |
| 2026-11-01 2 PM PT | `short11-his-basement` | 2849.1300–2866.6000 (17.5 s) | Hyperliquid's Nodes Are in His Basement | https://youtu.be/1JuONDn5OvY |
| 2026-11-02 2 PM PT | `short8-dumb-contract` | 2486.3200–2500.9500 (14.6 s) | "So It Was a Dumb Contract" | https://youtu.be/Nk-IBj6qzhA |
| 2026-11-03 2 PM PT | `short3-test-answers` | 571.6000–586.3200 (14.7 s) | Hack the University for the Test Answers | https://youtu.be/mCinQ5Vyh8A |
| 2026-11-04 2 PM PT | `short13-permanent-underclass` | 2452.9900–2469.7500 (16.8 s) | "Guess Who's Out of the Permanent Underclass" | https://youtu.be/9Lo_kdlrK3w |
| 2026-11-05 2 PM PT | `short6-platos-cave` | 2109.9000–2135.5200 (25.6 s) | Vitalik Built Plato's Cave for AI Agents | https://youtu.be/0yeLOhi8akQ |

Funnel comments: `media/clips/ep20/pin-comments.json` added to the pin-comments LaunchAgent; pinning and
the related-video button stay manual. TikTok: same thirteen enqueued at 4 PM PT daily in
`media/clips/tiktok/queue.json`, scheduled 2026-10-24 in one slow-paced Studio session (Nov 3–5 rerun on/after
Oct 26); URLs in `episodes/tiktok.md`.

## Edit decisions of note

- **Order: recording order kept.** Cold open → title card → welcome → the key of 4 → PHP2Shell →
  the PHP leak / privacy → Perp of Fortune 2.0 → Vitalik's paranoid mode → Samsung TV → Railway →
  Hyperliquid marquee → perp final → end card. The perp lands at 27:22 (retainer rule missed; the
  cert story is the strongest material and fills the first 13 min). Marquee at 44:55.
- **Jackson's brief:** snappy, no mid-word cuts, drop discussions that add neither entertainment nor
  information, like-and-subscribe reminders. ~8.7 min removed: 26 s of intro crosstalk, 43 s and
  43 s around the cert wrap, Jackson's Patch the Planet / Glasswing explainer (74 s, Jackson's note
  after v1), 38 s before Tyler's CISO line, 53 s of perp crosstalk before Vitalik, 90 s and 41 s of
  Vitalik tangents, 51 s before Railway, 57 s before Hyperliquid, 43 s before the perp final, the
  tail after "farewells", plus 29 s of dead air across 21 pauses.
- **v1 → v2 (Jackson's review of v1):** 12:30 cut Jackson mid-sentence, 22:02 kept the Glasswing
  explainer, 43:56 and 52:05 had a faintly audible muted mic. Sweep found the same whisper
  line-timestamp trap at three more edges (11:31 mid-word, 43:56 in-point mid-sentence, 49:54
  mid-sentence); every content edge was re-measured with word-level micro-whisper + the 10 ms
  envelope. Two pipeline bugs fixed: (1) `remote_cut.py` consumes `cutlist.json`, which had been
  built before `sources.json` was repointed, so v1 rendered the raw (non-dereverbed) Jackson/Chris
  audio; cutlist is now regenerated after any plan or source change. (2) Forced `mute` spans only
  dropped the mic to idle gain (−18 dB), so muted words still played under pauses ("supposedly"
  at 52:05); `remote_cutlist.py` now emits hard mute spans and `remote_cut.py` gates them to zero.
- **Perp of Fortune 2.0 overlay (Jackson's note: the dashboard changed).** Chris's share anchored at
  master 1938.363 (filename delta). Full-frame for the reveal (29:00–29:11), then a persistent
  top-right corner PiP of the two position cards: crop `[840,290,532,95]` until Chris scrolls,
  `[840,290,532,40]` after (30:42), held through the countdown, the marquee and the final numbers
  to the end card (Ep 8 house rule: once the dashboard is up it stays up). Stats from the reveal
  onward are bottom-right (`st2`) so the P&L cards are never hole-punched; lower thirds still punch.
- **Cold open, 3 beats in 36.4 s** (19.4 / 4.2 / 12.9 s): Tyler on the 256-bit key picked from 0–256,
  Tyler's "long ETH 25×, and we're losing money on both," the binary countdown panic. Under the
  60 s hard cap.
- **Three LIKE + SUBSCRIBE pop-ups** at 2:02 (INTRO +81.4, over Tyler's and Chris's laughs), 30:57
  (PERP, on Jackson's own "viewer, please like and subscribe if you love watching us lose money")
  and 50:47 (HL, the jail-for-$100M banter): 6 s windows clear of cards, wipes, lower thirds, stats
  and PiP entrances.
- **Jackson's echo:** Ep 18/19 recipe reused as-is: WPE (nara_wpe, 48 kHz, 40 taps, delay 2, 120 s
  chunks) → `agate` expander → EQ, built as `src/jackson_720dr.mov`. Chris on the Ep 18 EQ chain
  (`src/chris_720eq.mov`). Tyler untouched. Mic band signatures matched Ep 19 within 1 dB.
- **Speaker balance:** `gain_spans` per host with `gain_target` 0.028; edited_raw.mov peak
  −1.30 dBFS, zero flat samples.
- **Split-screen framing:** `face_cx` measured with the Vision tool (jackson 666, chris 694,
  tyler 655).
- **`remote_cut.py` changes:** adjacent PiP windows merge only when the crop matches too (the
  scroll change was being flattened into one crop); `st2` overlays no longer punch PiP holes.
- **Sync bench not built**: StreamYard filename deltas as in Ep 14–19; `remote_sync.py --validate`
  handoff deltas within ±0.4 s. Jackson to confirm by ear on the live copy; `offsets.json` is the
  knob.
- **No disclaimer spoken on any track — TWELFTH episode running.** End card + descriptions carry it.
- Cloudflare, OpenAI, Anthropic, DeepSeek, Samsung, Railway, Hyperliquid, Jeff Yan, Vitalik, BitMEX,
  FTX, Binance, Wintermute, Quest are named as subjects of the stories. No employer names in kept
  spans; the perp's −$29 is the only money number, framed as the gag.
