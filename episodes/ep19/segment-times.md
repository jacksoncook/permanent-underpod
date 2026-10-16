# Permanent Underpod — Ep 19 — Segment Times

**Final cut: 1:00:39 · fully-remote episode, three StreamYard cams (offsets 0 / +0.015 / −0.011
from the filename deltas) plus Chris's screen share of the Perp of Fortune dashboard as a
top-right PiP wherever the share has content · three-beat 35 s cold open · title card · end card ·
whoosh + gold wipe on all 7 transitions · three LIKE + SUBSCRIBE pop-ups · Jackson's track
dereverbed (WPE + expander, Ep 18 recipe), Jackson's and Chris's earbud mics EQ'd at source ·
topics reordered per Jackson (Ledger first) · ~7.5 min of content removed, 27 dead-air pauses
trimmed (34 s).**

## Episode video

- **URL:** https://youtu.be/gBkEBCNJfPU — live 2026-10-16 as "They Hid a SIM Card Inside a Crypto Wallet. $102M Gone."
  (Jackson's manual upload, description = the sheet's draft). API-patched 2026-10-16: standard caption track
  from the final-cut SRT, 15 tags (the force-ssl token was revoked by the manual upload again; re-authed).
- **File:** `media/ep19/Permanent Underpod - Ep 19 (Final Cut).mp4`
- **Thumbnail:** `media/ep19/ep19-thumbnail.png` — "THEY BUGGED THE WALLET" (Jackson center,
  Tyler left, Chris right; passed the 320×180 shrink test).
- **Loudness:** delivered −15.7 LUFS integrated, −2.7 dBTP, LRA 4.2 (chain in `render.json`:
  Ep 18 front-end with the 6.8 kHz dynamic de-esser, target_lufs −11.8 / limit 0.7).
- **Sync check:** final audio cross-correlated against `edited_raw.mov` at 1:40, 10:00, 25:00,
  40:00, 55:00 and 1:00:00 — lag a constant 35 ms at every point (same as Ep 15–18; no drift).
- **LIKE + SUBSCRIBE:** pop-up on frame at 2:00.0, 30:19.4 and 57:18.8, SFX paired in each window.
  PiP dashboard on frame in the perp windows (3:30–5:43) and the perp wrap (59:26 onward).
- **Captions:** `episodes/ep19/transcript-attributed.srt` — regenerated from the FINAL cut.

## Title (drafts)

1. **They Hid a SIM Card Inside the Hardware Wallet ($102M Gone)**
2. The Ledger Implant: A Modem That Texted Your Seed Phrase to the Hacker
3. Is Self-Custody Dead? Another Hardware Wallet Bites the Dust
4. An AI Split Itself Across 15 Android TV Boxes (and Lightning, Roasted)

## YouTube description (paste-ready draft)

```
⏩ The Ledger implant is at 5:43. The self-replicating model at 52:03.

Someone opened a brand-new Ledger from a third-party retailer and found an LTE modem, a SIM card and an antenna soldered under the board. The secure element never leaks the seed, so the implant read it off the display and texted it to the attacker, who sat on hundreds of seed phrases and drained them all at once: ~$102M in Bitcoin. A second implant turned up at a big German electronics retailer, so this is not one dodgy shop. Tyler tells his Cold Card tamper-bag story, Chris wants to weigh every hardware wallet on a microscale, and we revisit Tyler's Ep 1 call that self-custody doesn't scale past the early adopters. Fixes on the table: multi-vendor multisig and Bitcoin vaults. Then: Anthropic left GitHub after going from 2,500 to 30,000 code changes a day. Is SaaS dead? Tyler's agent built an entire SaaS business (Billing Proof, $250/mo, zero customers) and Chris vibe-coded a DoorDash shame tracker instead of paying for one. Layer-2 series, part two: Tyler explains the Lightning Network, channels, HTLCs, inbound liquidity, and why 7 billion channels won't fit in the blocks. Finally, a research paper split an open-weight model across 15 Android TV boxes and it kept thinking at half a token a second. Chris wants a goblin in his toaster. Perp of Fortune: the model picked a 3× long on STBL; we lost $9.

🔥 On the Agenda
0:00 Cold open
0:39 Welcome, live from the moon (fully human)
1:15 Perp of Fortune: the model picks a 3× long on STBL
5:43 The Ledger implant that read the seed off the screen
7:40 Tyler's Cold Card tamper-bag story
9:11 Inside the box: a SIM card, an antenna, and your 24 words
12:58 Is self-custody dead? Tyler's Ep 1 call, revisited
17:14 Fixes: multi-vendor multisig and Bitcoin vaults
20:42 The death of SaaS: Anthropic leaves GitHub
22:01 Tyler's agent built a SaaS nobody bought: Billing Proof
31:01 Chris vibe-coded his DoorDash shame tracker
34:26 Layer-2 series: the Lightning Network, explained by Tyler
37:24 How a Lightning channel works: the 2-of-2 pot and HTLCs
43:13 The downsides: inbound liquidity and always-on nodes
47:25 Why Lightning can't onboard 7 billion people
52:03 Self-replicating AI: a model living on 15 Android TV boxes
59:26 Perp final: −$9, and the portafilter tattled

Recorded fully remote, three cameras, one dashboard.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment.

GLOSSARY
• Perp of Fortune: our tiny real-money perpetual-futures account; an AI picks the trade each week. This week: a 3× long on STBL.
• STBL: governance token of a protocol that splits a tokenized Treasury into a principal token and a yield token. Thin, volatile, hard to market-make.
• Hardware wallet: a device that keeps your private keys offline. Ledger and Cold Card are two of the big names.
• Seed phrase: the 24 words that back up a wallet's keys. Anyone who reads them owns the coins.
• Secure element: the tamper-resistant chip that holds the seed. The implant never touched it; it read the screen instead.
• Supply-chain attack: tampering with a product between the factory and the buyer. Tamper seals and shrink wrap are the defense, and both can be faked.
• Multi-vendor multisig: a 2-of-3 or 3-of-5 wallet whose keys live on devices from different companies, so one bad vendor can't drain it.
• Bitcoin vaults: proposed covenant-style constructs that add a delay and a veto to withdrawals, so a stolen key still can't move coins instantly.
• SaaS: software as a service, the subscription model agents may be undercutting when a $100 token bill builds the product.
• Layer two: a protocol that moves transactions off the Bitcoin chain and settles back to it, ideally with a unilateral exit.
• Lightning channel: a 2-of-2 multisig "pot" two parties update off-chain; opening or closing it is an on-chain transaction.
• HTLC: hash time-locked contract, the trick that routes a payment across several channels so everyone gets paid or no one does.
• Inbound liquidity: to receive on Lightning, someone else's coins must sit on their side of your channel. You usually pay for that.
• LSP: Lightning service provider, the intermediary most mobile wallets route through. Phoenix is the canonical self-custody example.
• Pipeline parallelism: splitting a model's layers across machines so each box runs a slice and passes the activations on.

🔔 Subscribe for next week: Poppy, Meta and Sierra's protocol for letting your agent act for you without your password; OUSD week two; the npm worm that holds packages hostage; Perp of Fortune rides again.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (3 beats: Chris on the implant texting the seed to the hacker · Tyler: "Claude's just becoming Voldemort and Horcrux-ing himself" · Chris: "an email from my smart fridge holding all of my butter hostage") |
| 0:35 | Title card |
| 0:39 | Welcome, live from the moon; "never are we AI, we are fully humid, flesh and blood" |
| 1:15 | Perp of Fortune: Chris condensed the pick to the most volatile perps of the last 72 h and let the model choose; it picked a 3× long on STBL; dashboard PiP; "which model? a Haiku pick?" "it was Fable" |
| 4:20 | Tyler: the Perp of Fortune index is the best bear/bull indicator in crypto |
| 5:43 | THE MARQUEE: the Ledger wallet hack; $102M in Bitcoin, a physical implant, not an AI story; "I'm talking like cockroach" |
| 7:40 | Tyler's Cold Card tamper-bag story: it arrived torn open; they sent a new one |
| 9:11 | Inside the box: an ESP32-class chip, an LTE receiver, a SIM card and an antenna; the seed read off the display; a second unit found at a German retailer |
| 12:58 | Is self-custody dead? Tyler's revised take: it needs a belief system that doesn't scale past early adopters; Jackson: "hardware wallets are failing their customers" |
| 14:33 | Chris wants to build a hardware wallet; "not Phoenix Wallet. Chris Wallet."; the store that also sells the scales |
| 17:14 | Fixes: multi-vendor multisig, Bitcoin vaults; a call for enterprising Bitcoiners |
| 20:42 | The death of SaaS: Anthropic leaves GitHub, 2,500 → 30,000 code changes a day |
| 22:01 | Tyler's agent built a SaaS nobody bought: Billing Proof, Stripe checkout tests, $250/mo, zero customers, a second eSIM |
| 26:00 | Is SaaS still viable when the build costs $100 in tokens? GitHub as infrastructure, not SaaS |
| 31:01 | Chris vibe-coded his DoorDash shame tracker; circular revenue until a Series A; "not good, buddy" |
| 34:26 | Layer-2 series: the Lightning Network; Tyler, "please roast the hell out of it like you did Spark" |
| 37:24 | How a Lightning channel works: the 2-of-2 pot, the abacus, HTLCs; ~5,000 BTC in public channels, ~20,000 nodes |
| 41:41 | Chris: "I could blow up the pod"; Jackson compares the unilateral exit to Spark's 80% haircut |
| 43:13 | The downsides: inbound liquidity ("your homies hook you up"), always-on nodes, locked capital |
| 47:25 | Why Lightning can't onboard 7 billion people; Chris's two big ones; Phoenix as the self-custody wallet done right |
| 52:03 | Self-replicating AI: the paper that split GLM across 15 Android TV boxes with pipeline parallelism; "a dumb little goblin in my toaster" |
| 55:53 | "Half a token a second across the global fleet of Huawei smart TVs"; local inference, DoorDash burritos vs a GPU |
| 58:43 | Did GLM get into the Ledger wallets? Negotiating with a model for your seed phrase |
| 59:26 | Perp of Fortune final: −$9; "the portafilter tattled on us"; Ken Griffin took us out; buy Tyler's t-shirt on eBay |
| 1:00:32 | End card (Poppy · OUSD week two · the npm worm · Perp of Fortune rides again · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock seconds
(Jackson's track). Rows marked **continuous** are topic wipes on unbroken source. Every splice sits
at the midpoint of a measured all-silent union gap (`check_bounds.py --plan`) except the edges pinned
with `hard_m0`/`hard_m1` (crosstalk removals, with the overlapping mic muted for the edge); content
cuts were micro-whispered at both edges (`mw.sh`).

| Final | What | src out → src in |
|---|---|---|
| 0:23.20 | cold open beat 2 (Voldemort / Horcrux) | 2932.50 → 3681.30 |
| 0:29.13 | cold open beat 3 (butter hostage) | 3687.25 → 3915.10 |
| 0:34.63 | title card | 3920.60 → |
| 0:39.13 | welcome; 0.55 s of pre-roll dropped | → 0.55 |
| 1:14.80 | welcome → Perp of Fortune — continuous | 36.20 → 36.20 |
| 3:35.23 | 31 s of crosstalk over the dashboard share removed (Tyler's "why split the yield" question lands, Chris's answer resumes) | 176.64 → 207.21 |
| 4:12.53 | dead-air trim (1.09 s) | 244.50 → 245.59 |
| 4:30.17 | dead-air trim (0.84 s) | 263.22 → 264.06 |
| 5:42.77 | REORDER: perp → Ledger marquee ("Something interesting this week") | 336.65 → 2622.62 |
| 5:48.73 | Tyler's "I've talked a lot already" and the reply removed (out of order after the reorder; Jackson's note); Chris's "most Tyler episode" kept | 2628.57 → 2638.00 |
| 5:56.13 | hard edges: remainder of the out-of-order exchange removed | 2645.40 → 2650.55 |
| 6:25.97 | dead-air trim (0.95 s) | 2680.40 → 2681.35 |
| 6:51.57 | 7 s of three-way crosstalk removed (hard edge, Jackson muted on the in) | 2706.96 → 2714.08 |
| 10:55.53 | dead-air trim (1.30 s) | 2958.03 → 2959.33 |
| 13:10.17 | dead-air trim (2.95 s) | 3093.96 → 3096.91 |
| 15:55.20 | dead-air trim (0.96 s) | 3261.94 → 3262.90 |
| 20:17.47 | dead-air trim (0.81 s) | 3525.18 → 3525.99 |
| 20:42.37 | REORDER: Ledger → death of SaaS (back to the recording's first topic) | 3550.89 → 340.61 |
| 20:46.63 | dead-air trim (1.04 s) | 344.89 → 345.93 |
| 21:41.30 | dead-air trim (2.44 s) | 400.61 → 403.05 |
| 21:56.03 | dead-air trim (0.87 s) | 417.80 → 418.67 |
| 24:18.47 | dead-air trim (0.86 s) | 561.09 → 561.95 |
| 25:16.50 | dead-air trim (1.00 s) | 619.99 → 620.99 |
| 25:51.37 | dead-air trim (0.93 s) | 655.85 → 656.78 |
| 27:51.30 | 34 s of the Billing Proof back-and-forth removed | 776.72 → 811.06 |
| 28:31.40 | dead-air trim (1.63 s) | 851.17 → 852.80 |
| 28:59.77 | dead-air trim (0.81 s) | 881.17 → 881.98 |
| 29:16.43 | dead-air trim (1.07 s) | 898.65 → 899.72 |
| 34:26.50 | SaaS → Lightning — continuous | 1209.79 → 1209.79 |
| 34:36.17 | dead-air trim (0.86 s) | 1219.47 → 1220.33 |
| 37:06.37 | dead-air trim (1.07 s) | 1370.53 → 1371.60 |
| 37:24.27 | 19 s removed ahead of the channel explainer (hard edge, Jackson muted on the in) | 1389.51 → 1408.40 |
| 41:41.37 | dead-air trim (0.89 s) | 1665.49 → 1666.38 |
| 42:52.53 | dead-air trim (1.38 s) | 1737.55 → 1738.93 |
| 43:12.67 | Lightning privacy tangent removed (1:50); in on "the downsides of Lightning" | 1759.08 → 1868.65 |
| 45:05.27 | Lightning tangent removed (0:55) | 1981.25 → 2036.16 |
| 47:29.37 | dead-air trim (0.81 s) | 2180.25 → 2181.06 |
| 48:46.43 | Lightning tangent removed (1:10); in on Chris's HTLC question | 2258.14 → 2327.68 |
| 49:12.13 | Lightning tangent removed (1:08); in on Chris's "two big ones" | 2353.37 → 2421.08 |
| 51:53.43 | 28 s removed; in on "we're going to throw a wrap on the Lightning Network" (hard edge, Chris muted) | 2582.39 → 2610.50 |
| 52:02.93 | REORDER: Lightning wrap → self-replicating AI (skips the Ledger block, already aired) | 2620.00 → 3561.28 |
| 52:33.90 | dead-air trim (1.86 s) | 3592.25 → 3594.11 |
| 53:08.10 | dead-air trim (1.80 s) | 3628.31 → 3630.11 |
| 56:37.33 | dead-air trim (1.34 s) | 3839.33 → 3840.67 |
| 56:41.50 | dead-air trim (2.01 s) | 3844.85 → 3846.86 |
| 58:29.67 | dead-air trim (1.21 s) | 3955.01 → 3956.22 |
| 59:26.07 | dead-air trim (1.08 s) | 4012.61 → 4013.69 |
| 1:00:31.77 | end card; "Have a lovely week" is the last line | 4079.39 → |

## Spotify description (paste-ready draft)

```
Someone opened a brand-new Ledger from a third-party retailer and found an LTE modem, a SIM card and an antenna soldered under the board. The secure element never leaks the seed, so the implant read it off the display and texted it to the attacker, who sat on hundreds of seed phrases and drained them all at once: ~$102M in Bitcoin. A second implant turned up at a big German electronics retailer, so this is not one dodgy shop. Tyler tells his Cold Card tamper-bag story, Chris wants to weigh every hardware wallet on a microscale, and we revisit Tyler's Ep 1 call that self-custody doesn't scale past the early adopters. Fixes on the table: multi-vendor multisig and Bitcoin vaults. Then: Anthropic left GitHub after going from 2,500 to 30,000 code changes a day. Is SaaS dead? Tyler's agent built an entire SaaS business (Billing Proof, $250/mo, zero customers) and Chris vibe-coded a DoorDash shame tracker instead of paying for one. Layer-2 series, part two: Tyler explains the Lightning Network, channels, HTLCs, inbound liquidity, and why 7 billion channels won't fit in the blocks. Finally, a research paper split an open-weight model across 15 Android TV boxes and it kept thinking at half a token a second. Chris wants a goblin in his toaster. Perp of Fortune: the model picked a 3× long on STBL; we lost $9.

The Ledger implant is at 5:43. Chapters: Cold open (0:00) · Welcome, live from the moon (0:39) · Perp of Fortune: a 3× long on STBL (1:15) · The Ledger implant that read the seed off the screen (5:43) · Tyler's Cold Card tamper-bag story (7:40) · Inside the box: a SIM card, an antenna, and your 24 words (9:11) · Is self-custody dead? (12:58) · Fixes: multi-vendor multisig and Bitcoin vaults (17:14) · The death of SaaS: Anthropic leaves GitHub (20:42) · Tyler's agent built a SaaS nobody bought (22:01) · Chris vibe-coded his DoorDash shame tracker (31:01) · Layer-2 series: the Lightning Network (34:26) · How a Lightning channel works (37:24) · The downsides: inbound liquidity and always-on nodes (43:13) · Why Lightning can't onboard 7 billion people (47:25) · Self-replicating AI on 15 Android TV boxes (52:03) · Perp final: −$9 (59:26)

Recorded fully remote, three cameras, one dashboard. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. Glossary: STBL = governance token of a protocol that splits a tokenized Treasury into a principal token and a yield token. Seed phrase = the 24 words that back up a wallet's keys. Secure element = the tamper-resistant chip that holds the seed; the implant read the screen instead. Supply-chain attack = tampering with a product between the factory and the buyer. Multi-vendor multisig = a 2-of-3 wallet whose keys live on devices from different companies. Bitcoin vaults = proposed constructs that add a delay and a veto to withdrawals. Layer two = a protocol that moves transactions off the Bitcoin chain and settles back to it. Lightning channel = a 2-of-2 multisig pot two parties update off-chain. HTLC = hash time-locked contract, the trick that routes a payment across channels so everyone gets paid or no one does. Inbound liquidity = to receive on Lightning, someone else's coins must sit on their side of your channel. LSP = Lightning service provider, the intermediary most mobile wallets route through. Pipeline parallelism = splitting a model's layers across machines so each runs a slice.

Subscribe for next week: Poppy, Meta and Sierra's protocol for letting your agent act for you without your password; OUSD week two; the npm worm that holds packages hostage; Perp of Fortune rides again.
```

## Captions

`transcript-attributed.srt` regenerated from the FINAL cut (never the raw recording) in
`episodes/ep19/`. Upload as the `standard` track after the episode is live.

## Clips

Twelve vertical Shorts cut 2026-10-16 from `edited_raw.mov` with the episode audio chain, face-crop
hard cuts, branded ender. `verify_clips.py` pre and `--rendered`: 0 failures (short1/short9 tail
warnings are decaying final words, confirmed by whisper). Every rendered head and tail whispered: no
clipped words. Uploaded scheduled-private to Underpod Shorts, two a day (Jackson: "start today, double
up"): 6 PM + 10 PM PT while Ep 18 holds 2 PM PT through Oct 20, then 2 PM + 6 PM PT on Oct 21.
Receipts in `media/clips/ep19/upload-manifest.json.results.json`.

| Release | Clip | Final-cut in–out | Title | URL |
|---|---|---|---|---|
| 2026-10-16 6 PM PT | `short9-horcruxing-himself` | 3239.1333–3253.0900 (14.0 s) | Claude Just Horcruxed Himself - Ep 19 Clip | https://youtu.be/dCFxmfWl2j8 |
| 2026-10-16 10 PM PT | `short10-butter-hostage` | 3450.5000–3474.9600 (24.5 s) | My Smart Fridge Is Holding My Butter Hostage - Ep 19 Clip | https://youtu.be/BSnekJhe0bE |
| 2026-10-17 6 PM PT | `short8-goblin-in-my-toaster` | 3155.9000–3167.0400 (11.1 s) | I Want a Goblin in My Toaster - Ep 19 Clip | https://youtu.be/-b7Ih8Gwfx0 |
| 2026-10-17 10 PM PT | `short4-chris-wallet` | 924.9000–938.0800 (13.2 s) | Forget Phoenix Wallet. Chris Wallet. - Ep 19 Clip | https://youtu.be/6pmsUijzjhA |
| 2026-10-18 6 PM PT | `short3-talking-like-cockroach` | 370.6667–400.9000 (30.2 s) | $102M Lost to a Bug Inside a Hardware Wallet - Ep 19 Clip | https://youtu.be/ALvnhtHhXJU |
| 2026-10-18 10 PM PT | `short7-not-good-buddy` | 2031.2333–2051.6800 (20.4 s) | My Finance Agent Says "Not Good, Buddy" - Ep 19 Clip | https://youtu.be/fkWnZETzf80 |
| 2026-10-19 6 PM PT | `short12-ken-griffin-took-us-out` | 3584.9000–3598.3000 (13.4 s) | Ken Griffin Took Us Out (We Lost $9) - Ep 19 Clip | https://youtu.be/AHT6yw9yjUk |
| 2026-10-19 10 PM PT | `short5-store-sells-the-scales` | 981.9000–1015.0500 (33.1 s) | The Store That Sold the Bugged Wallet Also Sells the Scale - Ep 19 Clip | https://youtu.be/F3JzqYKo6_k |
| 2026-10-20 6 PM PT | `short1-haiku-or-fable` | 249.0667–258.9000 (9.8 s) | Which AI Picked Our Trade? - Ep 19 Clip | https://youtu.be/qhzeGR3WrmY |
| 2026-10-20 10 PM PT | `short2-perp-of-fortune-index` | 260.0000–277.2000 (17.2 s) | Our Gambling Account Is the Best Bear Market Indicator - Ep 19 Clip | https://youtu.be/X22OMRuXpOU |
| 2026-10-21 2 PM PT | `short6-saasless-dude` | 1303.5000–1316.0000 (12.5 s) | "I'm SaaS-less, Dude" - Ep 19 Clip | https://youtu.be/mPyBs9vOga8 |
| 2026-10-21 6 PM PT | `short11-half-a-token-a-second` | 3351.6000–3372.8500 (21.2 s) | Half a Token a Second on Every Smart TV - Ep 19 Clip | https://youtu.be/sTaOA9dTdVY |

Funnel comments: `media/clips/ep19/pin-comments.json` added to the pin-comments LaunchAgent (now also
fires at 01:10 ET for the 10 PM PT slot); pinning stays manual. TikTok: same twelve scheduled via
`tt_upload.py`, two a day at 6 PM + 8 PM PT (21:00/23:00 ET) Oct 16–21 (per-item `postHourLocal`,
new), URLs in `episodes/tiktok.md`.

## Edit decisions of note

- **Order (Jackson's note): Ledger first.** Cold open → title card → welcome → Perp of Fortune →
  Ledger implant → death of SaaS → Lightning Network → self-replicating AI → perp wrap → end card.
  Jackson allowed SaaS and the AI paper to swap; the paper stayed last because its Ledger callback
  ("did GLM get into the ledger wallets?") and the fridge gag flow straight into the perp wrap, and
  it was recorded last so the wrap needs no splice. Recording order was SaaS → Lightning → Ledger
  → AI paper. Marquee lands at 5:43 (perp is the retainer at 1:15).
- **Jackson's cut:** Tyler's "I've talked a lot already" at the top of the Ledger block (out of
  order once Ledger leads) is gone; LEDGER_A/B/C stitch Jackson's intro, Chris's "most Tyler
  episode" and Jackson's "this hack isn't even technical" with hard edges and mutes on the
  overlapping mic.
- **Runtime 60.6 min, above the 45–55 target.** ~7.5 min of content came out: the four Lightning
  tangents (1:50 privacy, 0:55, 1:10, 1:08) plus 28 s before the wrap, 34 s of Billing Proof
  back-and-forth, 31 s of perp crosstalk, 19 s before the channel explainer, the out-of-order Ledger
  exchange, and 34 s of dead air across 27 pauses. Every remaining Lightning join crosses a
  crosstalk edge; the next 5 min would come out of the SaaS block (20:42–34:26) if Jackson wants
  it tighter.
- **Cold open, 3 beats in 34.6 s** (23.2 / 5.9 / 5.5 s): Chris explaining the implant texting the
  seed to the hacker (the marquee), Tyler's Horcrux line and Chris's butter-hostage fridge (the
  finale tease). Under the 60 s hard cap.
- **Perp of Fortune dashboard as PiP:** Chris's screen share anchored at master 169.945 (filename
  delta). PiP windows: master 171–176.64 and 207.21–336.65 (final 3:30–5:43) and 4013.5–4060.5
  (final 59:26–60:13); crop `[1000,470,460,355]`, top-right corner.
- **Three LIKE + SUBSCRIBE pop-ups** at 2:00 (PERP +45.2), 30:19 (SAAS_B +148.083) and 57:19
  (REPL +315.833): 6 s windows clear of cards, wipes, lower thirds, stats and PiP entrances.
- **Jackson's echo:** Ep 18 recipe reused as-is: WPE (nara_wpe, 48 kHz, 40 taps, delay 2, 120 s
  chunks) → `agate` expander (threshold 0.02, ratio 2.5, range 0.15) → Ep 16/18 EQ, built as
  `src/jackson_720dr.mov`. Chris on the Ep 18 EQ chain (`src/chris_720eq.mov`). Tyler untouched.
- **Speaker balance:** `gain_spans` per host with `gain_target` 0.028; edited_raw.mov peak
  −1.88 dBFS, zero flat samples.
- **Split-screen framing:** `face_cx` measured with the Vision tool (jackson 671, chris 632,
  tyler 730).
- **Lower thirds** shortened once after the first full render: `lt_ledger.png` (1319 px) clipped at
  the right edge; `lt_lndown.png` (1276) also trimmed. Both ≤1130 px now; full re-render.
- **Sync bench not built**: StreamYard filename deltas as in Ep 14–18. No slip visible on the test
  frames. Jackson to confirm by ear on the live copy; if Tyler reads late, `offsets.json` tyler is
  the one knob.
- **No disclaimer spoken on any track — ELEVENTH episode running.** End card + descriptions carry it.
- Ledger, Cold Card, Phoenix, Anthropic, GitHub, Hyperliquid, Tether, Stripe, DoorDash, Plaid,
  Huawei, Samsung, GLM, Vitalik, Ken Griffin are named as subjects of the stories. No employer names
  in kept spans; the perp's −$9 is the only money number, framed as the gag.
