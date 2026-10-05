# Permanent Underpod — Ep 17 — Segment Times

**Final cut: 1:00:20 · FIRST GALLERY-RECORDING EPISODE: one video of the call grid (three tiles,
one mixed track) instead of three cams. Speaker-following edit: every shot is a static crop of the
active speaker's tile (or a tighter face crop on long runs), the grid on crosstalk and on the
two Perp dashboard screen shares, hard cuts only · four-beat 48 s cold open · title card · the
fumbled "we'll just cut all this" handoff into the slop auction, the Nitro-enclave digression and the
federation-size/Tempo aside removed · end card · whoosh +
gold wipe on all 6 transitions.**

## Episode video

- **Upload:** Jackson confirmed uploaded on 2026-10-01. Do not re-render or re-upload.
- **URL:** https://youtu.be/Wuyi6fwVtJA (public; verified via API 2026-10-02).
- **Published:** 2026-10-01 13:45 Pacific. YouTube reports 1:00:21; local master is 1:00:20.47.
- **File:** `media/ep17/Permanent Underpod - Ep 17 (Final Cut).mp4`
- **Thumbnail:** `media/ep17/ep17-thumbnail.png` — "THE AI CAN'T EVEN TALK" (Tyler smirk left,
  Jackson mid-laugh with hand up center, Chris grin right; tile crops trimmed above the name
  badges; passed the 320×180 shrink test).
- **Loudness:** delivered −15.8 LUFS integrated, −2.7 dBTP, LRA 3.5 (chain in `render.json`: `adeclip`, no
  denoiser (floor −67 to −80 dB), −3 dB at 250 Hz, +2 dB at 2.8 kHz, 6.8 kHz dynamic de-esser (range 5), +3 dB air
  at 9.5 kHz, loudnorm LRA 5; target_lufs −11.8 / limit 0.7).
- **Sync check:** final audio cross-correlated against `edited_raw.mov` at 1:40, 30:00, 50:00 and 59:50: lag a
  constant 10 ms at every point (no drift). Each clip's audio correlates to the source at 0 ms. A/V stream
  durations match to 17 ms; 108,614 frames × 1600 samples exactly.
- **Captions:** `episodes/ep17/transcript.srt` — regenerated from the FINAL cut.

## Title (published)

**Korea Turned Crypto Trading Into a Spectator Sport** — Jackson's manual retitle, seen live
2026-10-05 (launched 2026-10-01 as "An AI That Can’t Talk Picked Our Trade"). Thumbnail still reads
"THE AI CAN'T EVEN TALK". Description opener rewritten to lead with Seoul to match
(`episodes/ep17/description.txt`; live via `yt_update.py --set-description`).

### Earlier title drafts

1. The AI That Can't Talk Picked Our Trade
2. It Cost 80,000 Sats to Get 20,000 Out of Spark
3. Korea Made Gambling a Spectator Sport
4. Your Agent Will Outbid Mine for Dinner

## YouTube description (published; API readback 2026-10-02; opener rewritten 2026-10-05 for the retitle)

```
⏩ Seoul's live perp-trading competition is at 5:52. Jev, the AI that can't talk, 11:53. Spark's trust model 23:06.

Korea made eSports a national pastime; now it's perps. Aster sponsored a live perp-trading competition in Seoul, and a Korean streamer trades Trump speeches at 50x. Someone said it was paper trading. Chris is crushed. This week's thesis (long Aster: perps are becoming spectator entertainment) came from Jev, a model that never writes a sentence: you hand it a question and a set of boxes and it hands back probabilities. Tyler explains what Jev actually is (a classifier layer on an open-weights model, no moat, but a form factor that struck a nerve), Chris wants to vibe-vacuum his house with it, and Jackson's AI notes claim Jev beat Pokémon Red for $1.65, with Claude's help. Headline inflation is out of control. Then the Bitcoin topic: Spark, the Lightning-without-channels layer two. Tyler's teardown: security rests on the operators deleting their keys ("point your Claude at the code"), it's proof of authority with extra steps, one tester spent 80,000 sats to unilaterally exit 20,000, and the operators see every transaction. Finale: Chris's slop auction. Flashbots found L2s full of fizzling MEV orders, EIP-1559 taxed them, and the same Tullock-contest math says the bot internet gets fixed by an auction or a wall. https://cdrn.xyz/blog/slop-auction/ We're getting the wall. Plus: what happens when everyone's agent wants the same reservation. Perp of Fortune finishes +$3.72. One of the few.

🔥 On the Agenda
0:00 Cold open
0:53 Talking into chopsticks
1:57 Perp of Fortune: long Aster, perps as spectator sport
3:30 Who sponsors a cigarette-smoking competition?
5:52 Seoul's live perp-trading competition
10:34 Tyler's conspiracy: the pot doesn't exist
11:53 The marquee: Jev, the AI that can't talk
18:29 Headline inflation: Jev beat Pokémon (with Claude)
23:06 Spark: Lightning without channels
24:46 Tyler explains: what is a Bitcoin layer two?
29:04 The trust model: they have to delete the keys
32:04 Chris: proof of authority, a multisig between friends
34:05 Unilateral exit: 80,000 sats to recover 20,000
36:58 Privacy: Spark sees everything
41:06 Ark vs Spark, and some nice things
44:00 The slop auction: Chris Doran's blog
49:28 Tullock contests: the auction or the wall
54:52 Agent congestion: everyone's bot wants the same table
58:02 Chris's strategy: like what other people don't
59:22 Perp of Fortune result
1:00:13 End card / next week

Recorded fully remote, three tiles on one call.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment. Not a recommendation to long Aster, or anything else.

GLOSSARY
• Perp of Fortune: our tiny real-money perpetual-futures account; an AI picks the trade each week. This week Jev picked it.
• Aster: a perps exchange. Sorry, Aster.
• Jev: a model trained to answer only in typed structures with probabilities, never prose. Fast, cheap, good at "which bucket is this?" questions.
• Transfer learning: taking a pre-trained model and training a new head on your own data. What you used to need a data scientist for; Jev sells it as an API.
• Headline inflation: "Jev beat Pokémon Red in 37 hours for $1.65 using Claude Opus 5." Claude built the harness.
• Spark: a Bitcoin L2 run by a federation (Lightspark, Flashnet, Breez). Payments inside the Spark are cheap; Spark Service Providers swap in and out to Lightning and on-chain.
• Delete-the-keys trust model: every Spark payment is a 2-of-2 between you and the operators; it's non-custodial only if they really delete the old key.
• Proof of authority: a network run by a known set of trusted parties.
• Unilateral exit: leaving an L2 with only your own keys. On Spark your balance is split into many "leaves," and each one costs an on-chain fee to exit.
• Ark: an off-chain Bitcoin protocol with a stronger trust model than Spark's; Tyler expects it to "L2-mog" Spark.
• MEV: maximal extractable value, the profit from ordering and inserting transactions in a block.
• Fizzling orders: speculative on-chain orders that fail when the preconditions aren't met. Spamming them is positive EV, so L2s fill up with them.
• EIP-1559: Ethereum's fee change; the price of block space rises as it gets congested. An auction against spam.
• Tullock contest: the game theory of a raffle. The more tickets (spam posts) you buy, the better your odds, until the tickets cost what the prize is worth.
• The auction vs the wall: the two ways to fix a Tullock contest. Price the slot, or gatekeep who gets one. Subscriptions and KYC are walls.
• Instinct / Muse: consumer agents that book, buy, and cancel for you. The congestion pricing on your Valentine's reservation is coming from them.

🔔 Subscribe for next week: enclaves III (a $200 board forges the attestation), agent week two, is bitcoin back (still no charts), and Korea's 4× yen stablecoin.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (4 beats: Jackson's "Man Gambles Child's College Education Fund for Perpetual Fortune… you're in trouble with the wife" · Tyler's "point your Claude at the code, ask Claude if we delete the keys" · the delete-the-keys bool · "proof of fun to post" / "Jev can do that for one cent, it's so over") |
| 0:48 | Title card |
| 0:53 | Welcome: Jackson talks into a chopstick, Tyler into a sushi microphone holder, Chris ends his turn |
| 1:57 | Perp of Fortune: long Aster, "perps becoming spectator entertainment, not long on Korea" |
| 3:30 | Who sponsors a cigarette-smoking competition? The two Rubik's cubes, two beers, two cigarettes challenge |
| 5:52 | Seoul's live perp-trading competition; the Korean streamer who perps Trump speeches |
| 8:58 | "Someone said it was paper trading" |
| 10:34 | Tyler's conspiracy: the Perp of Fortune pot doesn't exist; "Man Gambles Child's College Education Fund" |
| 11:53 | THE MARQUEE: Jev, discovered by scientists with a telescope; Tyler's breakdown of structured-output probability models |
| 16:06 | "I don't think Jev has any moat"; how does Jev play Doom with no image input? |
| 18:29 | Headline inflation: Jev beat Pokémon Red for $1.65 "using Claude Opus 5" |
| 20:39 | The vibe problem: P(rain) + P(no rain) ≠ 1; Chris wants to vibe-vacuum |
| 23:06 | Spark: Lightning without channels, "created by a dude who created Libra" |
| 24:46 | Tyler explains what a Bitcoin L2 is: Lightning, Spark, Ark, statechains |
| 26:56 | How Spark works: the federation, Spark Bitcoin, Spark Service Providers |
| 29:04 | The trust model: they have to delete the keys; point your Claude at the code |
| 31:24 | "Delete the key material: true" |
| 32:04 | Chris: proof of authority, a multisig between friends; Ronin and Wormhole |
| 34:05 | Unilateral exit: leaves, and the tester who spent 80,000 sats to recover 20,000 |
| 36:58 | Privacy: Spark operators see everything; transactions were public by default |
| 41:06 | Ark vs Spark, "L2-mog," and some nice things about the SDK |
| 44:00 | The slop auction: Chris's blog; Flashbots and MEV-filled L2s |
| 46:43 | Fizzling orders: positive EV to spam; EIP-1559 as the auction |
| 49:28 | Tullock contests: the auction or the wall; "we're going to get the wall" |
| 51:00 | How would an auction for posts even work? The ad-auction dystopia |
| 54:52 | Agent congestion: proof of fun, CAPTCHAs, Instinct and Muse fighting for the same table |
| 57:23 | Valentine's Day congestion pricing |
| 58:02 | Chris's strategy: like what other people don't; the anointed Mission taqueria |
| 59:22 | Perp of Fortune result: +$3.72 on Aster, "one of the few"; the pod needs more volatility |
| 1:00:13 | End card (enclaves III · agent week two · is bitcoin back · Korea's yen stablecoin · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts; `src out → src in` are source seconds. Every
content splice sits at the midpoint of a measured all-silent gap (`check_bounds.py --plan` on the
mix, 10 ms RMS envelope, 14/14) and both edges were micro-whispered. Shot changes (~285)
are not splices: the source is continuous across them.

| Final | What | src out → src in |
|---|---|---|
| 0:17.10 | cold open beat 2 (point your Claude at the code) | 636.00 → 1770.50 |
| 0:23.90 | cold open beat 3 (delete the key material: true) | 1777.30 → 1896.14 |
| 0:34.27 | cold open beat 4 (proof of fun / Jev for one cent) | 1906.49 → 3425.93 |
| 0:48.43 | title card | 3440.11 → |
| 0:52.93 | welcome | → 2.00 |
| 3:05.40 | dead-air trim (1.75 s) | 134.44 → 136.19 |
| 9:56.83 | dead-air trim (1.35 s) | 547.64 → 548.99 |
| 15:24.60 | dead-air trim (1.75 s) | 876.73 → 878.48 |
| 18:33.87 | dead-air trim (1.51 s) | 1067.76 → 1069.27 |
| 23:05.30 | dead-air trim (1.34 s) | 1340.69 → 1342.03 |
| 24:07.87 | dead-air trim (1.34 s) | 1404.59 → 1405.93 |
| 30:21.97 | Nitro-enclave digression removed (1780.10–1811.10, 31 s): "…the software they're running." → "So at the end of the day…" | 1780.10 → 1811.10 |
| 38:54.67 | dead-air trim (1.92 s) | 2323.76 → 2325.68 |
| 41:01.53 | dead-air trim (1.50 s) | 2452.53 → 2454.03 |
| 41:03.00 | federation-size / Tempo aside removed (2455.50–2538.00, 83 s): "…decentralization schemes. Yeah." → "Yeah, totally. It makes a lot of sense." | 2455.50 → 2538.00 |
| 43:28.43 | dead-air trim (3.29 s) | 2683.46 → 2686.75 |
| 43:59.47 | Spark → slop auction; the fumbled handoff removed ("I don't remember what it is… we'll just cut all this", 2717.77–2757.77, 40 s) | 2717.77 → 2757.77 |
| 48:43.60 | dead-air trim (3.47 s) | 3041.92 → 3045.39 |
| 48:44.90 | dead-air trim (1.62 s) | 3046.67 → 3048.30 |
| 57:44.07 | dead-air trim (2.80 s) | 3587.48 → 3590.28 |
| 59:43.87 | dead-air trim (1.64 s) | 3710.07 → 3711.70 |
| 1:00:13.47 | end card | 3741.30 → |

## Spotify description (paste-ready draft)

```
Jev is a new kind of model: it never writes a sentence. You hand it a question and a set of boxes and it hands back probabilities. It also picked this week's Perp of Fortune (long Aster: perps are becoming spectator entertainment, and Seoul is running a live perp-trading competition with a Korean streamer who trades Trump speeches at 50x). Tyler explains what Jev actually is (a classifier layer on an open-weights model, no moat, but a form factor that struck a nerve), Chris wants to vibe-vacuum his house with it, and Jackson's AI notes claim Jev beat Pokémon Red for $1.65, with Claude's help. Headline inflation is out of control. Then the Bitcoin topic: Spark, the Lightning-without-channels layer two. Tyler's teardown: security rests on the operators deleting their keys ("point your Claude at the code"), it's proof of authority with extra steps, one tester spent 80,000 sats to unilaterally exit 20,000, and the operators see every transaction. Some nice things are said at the end. Finale: Chris's slop auction. Flashbots found L2s full of fizzling MEV orders, EIP-1559 taxed them, and the same Tullock-contest math says the bot internet gets fixed by an auction or a wall. We're getting the wall. Plus: what happens when everyone's agent wants the same reservation. Perp of Fortune finishes +$3.72. One of the few.

Jev is at 11:53. Chapters: Cold open (0:00) · Talking into chopsticks (0:53) · Perp of Fortune: long Aster (1:57) · Who sponsors a cigarette-smoking competition? (3:30) · Seoul's live perp-trading competition (5:52) · Tyler's conspiracy: the pot doesn't exist (10:34) · The marquee: Jev, the AI that can't talk (11:53) · Headline inflation: Jev beat Pokémon, with Claude (18:29) · Spark: Lightning without channels (23:06) · What is a Bitcoin layer two? (24:46) · The trust model: they have to delete the keys (29:04) · Proof of authority, a multisig between friends (32:04) · Unilateral exit: 80,000 sats to recover 20,000 (34:05) · Privacy: Spark sees everything (36:58) · Ark vs Spark, and some nice things (41:06) · The slop auction (44:00) · Tullock contests: the auction or the wall (49:28) · Agent congestion (54:52) · Like what other people don't (58:02) · Perp of Fortune result (59:22)

Recorded fully remote, three tiles on one call. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment, not a recommendation to long Aster or anything else. Glossary: Jev = a model trained to answer only in typed structures with probabilities, never prose. Transfer learning = training a new head on a pre-trained model with your own data; Jev sells that as an API. Layer two = a network that settles to Bitcoin; Tyler's test is unilateral exit. Spark = a Bitcoin L2 run by a federation (Lightspark, Flashnet, Breez); Spark Service Providers swap in and out to Lightning and on-chain. Delete-the-keys trust model = every Spark payment is a 2-of-2 with the operators; non-custodial only if they really delete the old key. Proof of authority = a network run by a known set of trusted parties, like the Ronin and Wormhole bridges. Unilateral exit = leaving an L2 with only your own keys; on Spark each "leaf" of your balance costs an on-chain fee. Ark = an off-chain Bitcoin protocol with a stronger trust model. MEV = profit from ordering and inserting transactions in a block. Fizzling orders = speculative on-chain orders that fail if the preconditions aren't met; spamming them is positive EV. EIP-1559 = Ethereum's congestion-priced block space, an auction against spam. Tullock contest = the game theory of a raffle; buy tickets until they cost what the prize is worth. The auction vs the wall = price the slot, or gatekeep who gets one. Instinct / Muse = consumer agents that book, buy, and cancel for you.

Subscribe for next week: enclaves III (a $200 board forges the attestation), agent week two, is bitcoin back (still no charts), and Korea's 4× yen stablecoin.
```

## Captions

`transcript.srt` regenerated from the FINAL cut (never the raw recording) in `episodes/ep17/`.
YouTube's caption flag is false at API readback 2026-10-02; no caption-track upload performed in this session.

## Clips

Seven Shorts uploaded and scheduled on 2026-10-02: 1, 3, 5, 6, 10, 7, 2. YouTube
readback confirms all seven processed, private until release, with matching copy and
Underpod Shorts playlist entries. Shorts 8 and 9 remain alternates; 4 and 11 are held.

QA passed 2026-10-01: 9 helper tests, full decodes and rendered speech-edge checks.
All 11 pre/post-render gates rechecked 2026-10-02: zero failures, warnings or seam flashes.
The full episode is live at https://youtu.be/Wuyi6fwVtJA. No episode re-render or re-upload.

| Release (Pacific) | Short | URL |
|---|---|---|
| Oct 2, 6 PM | Fish microphone | https://youtu.be/xvb5mJkinNc |
| Oct 3, 6 PM | Résumé roast | https://youtu.be/Ls7plYeMeSo |
| Oct 4, 6 PM | Kids' savings joke | https://youtu.be/VWakrvUAe_Y |
| Oct 5, 6 PM | Telescope joke | https://youtu.be/RF5_D-GqxFE |
| Oct 6, 6 PM | CAPTCHA pep talk | https://youtu.be/LphRdqj4dQg |
| Oct 7, 2 PM | Pokémon headline | https://youtu.be/AgbkXiCqkwQ |
| Oct 8, 2 PM | Cigarette challenge order | https://youtu.be/ccGALj-8JWw |

Jackson approved a four-hour offset on overlap days only: Ep 16 occupies 2 PM through
October 6. October 7–8 return to the standard 2 PM slot. UTC values and upload receipts
are in `media/clips/ep17/upload-manifest.json` and its `.results.json`.

Funnel comments are queued in `media/clips/ep17/pin-comments.json`; the existing LaunchAgent
now includes Ep 17 alongside Ep 16/15 and runs at 17:10/21:10 Eastern. Comments wait until
public; dry-run confirmed all seven currently private. Related video and comment pinning
are manual Studio steps; their status is not API-verifiable.

`clips.json` is the render specification; `clip-sources.json` records raw bounds and
speaker keys for rebuilding the gitignored sources. Gallery Shorts use per-clip tile
sources from `gallery_clip_source.py`, not the full episode's grid shots. Every switch is a hard cut.
The same posting copy is saved in `media/clips/ep17/posting-copy.md`.

Rebuild the résumé source with raw bounds `303.8 323.8`, `--keys
302.8:jackson,310.2:chris,320.7:jackson`, `--start 0.6333 --end 20.28`,
`--lead-frames 1 --wide-hold`. The share insert covers the call app's animated
layout change; the original mixed audio is preserved. Re-gate after any rebuild.

### short1-chopstick

- Title: A Microphone That Smells Like Fish - Ep 17 Clip
- Description: Tyler wonders whether his microphone holder could pick up sushi, and Jackson spots the obvious problem.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #comedy #podcast #shorts
- Tags: microphone, sushi, podcast banter, mic setup, host introductions, comedy podcast

### short2-cig-order

- Title: Two Cubes, Two Beers, One Terrible Game Plan - Ep 17 Clip
- Description: Tyler has a suspiciously detailed game plan for the two-cube, two-beer, two-cigarette challenge.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #rubikscube #comedy #shorts
- Tags: Rubik's cube, challenge, beer, cigarettes, podcast banter, comedy podcast

### short3-resume

- Title: Cigarettes and Gambling: Quite a Résumé - Ep 17 Clip
- Description: Chris objects to being named the resident expert in both cigarettes and gambling.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #comedy #podcast #shorts
- Tags: resume, gambling, cigarettes, podcast banter, host roast, comedy podcast

### short4-college-fund (HOLD)

- Hold: the audio uses a house segment name and depends on the preceding exchange. Do not upload this draft.
- Title: Gambling the College Fund Is a Bad Rebrand - Ep 17 Clip
- Description: A hypothetical college-fund gamble becomes Jackson's pitch for the worst possible podcast name.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #comedy #gambling #shorts
- Tags: college fund, podcast name, gambling joke, leveraged trading, finance satire, podcast banter

### short5-trump-account

- Title: A Kid's Savings at 100x Leverage - Ep 17 Clip
- Description: Tyler jokes about putting his daughter's Trump account into a 100x leveraged trade, and the business pitch only gets worse.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #finance #comedy #shorts
- Tags: Trump account, perpetual futures, leverage, Aster, finance satire, podcast comedy

### short6-telescope

- Title: They Found an AI With a Telescope? - Ep 17 Clip
- Description: Jackson gives AI model Jev a completely unserious origin story involving scientists and a telescope in space.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #ai #comedy #shorts
- Tags: Jev, artificial intelligence, language models, tech satire, space joke, podcast comedy

### short7-headline-inflation

- Title: Pokémon for $1.65? Read the AI Fine Print - Ep 17 Clip
- Description: Jackson reads a claim that Jev beat Pokémon Red for $1.65, and Chris immediately roasts the headline.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #ai #pokemon #shorts
- Tags: Jev, Pokémon Red, AI headlines, Claude, gaming, tech humor, headline inflation
- Copy constraint: this quotes a headline, not a verified benchmark; the clarification appears later in the episode.

### short8-ask-claude

- Title: Claude Read the Code. That's Not Proof. - Ep 17 Clip
- Description: Tyler explains why an AI review of Spark's public code cannot prove which software its operators actually run.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #bitcoin #ai #shorts
- Tags: Spark, Bitcoin, Claude, source code, trust model, AI code review

### short9-proof-of-fun

- Title: Make Bots Play a Game Before Posting? - Ep 17 Clip
- Description: A joke about stopping spam with a ten-second browser game collapses when Tyler points out AI could play it too.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #ai #bots #shorts
- Tags: AI spam, bots, social media, Jev, browser games, proof of fun

### short10-captcha

- Title: An AI Hits a CAPTCHA. Cue the Pep Talk. - Ep 17 Clip
- Description: Tyler recounts an AI agent's CAPTCHA hesitation turning into a “you can do it, buddy” pep talk.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #ai #captcha #shorts
- Tags: AI agents, CAPTCHA, browser automation, tech humor, podcast comedy, permission prompts

### short11-korean-lady (HOLD)

- Hold: the earlier Korean trading-streamer reference is absent. The description cannot repair the unexplained audio callback. Do not upload this draft.
- Title: This Podcast Needs More Screaming - Ep 17 Clip
- Description: Chris wants the podcast to borrow a Korean trading streamer's yelling-and-screaming energy.
- Full episode: https://youtu.be/Wuyi6fwVtJA
- Hashtags: #comedy #podcast #shorts
- Tags: podcast banter, trading streams, Korean streamer, show format, host reactions, comedy podcast

## Edit decisions of note

- **New form factor, new pipeline.** One 1920×1080 recording of the call grid (Chris top-left,
  Jackson top-right, Tyler bottom-center) with one mixed track and an unattributed VTT. Edit =
  simulated multicam: `gallery_diarize.py` (ECAPA voice embeddings against enrolled centroids,
  verified by eye on frame strips) → `gallery_layout.py` (blue name badges detect where the grid
  is replaced by a screen share: two 2–3 s Perp dashboard shares at 310.5 and 577.5) →
  `gallery_shots.py` (sticky, lookahead scheduler: min shot 2 s of talk, grid on churn ≥3 voice
  changes in 4 s, tile ↔ tight-crop alternation after 24 s solo) → `cut_render.py` crops each
  piece statically. 285 shots, 24 wide. Hard cuts only: the black gutters make any glide read
  as the Ep 8 boomerang. Documented in `podcast-video-edit/SKILL.md` → "Gallery recordings".
- **Order = recording order.** Cold open → title card → welcome → Perp of Fortune (Korea) →
  Jev → Spark → slop auction → agent congestion → wrap. Perp lands at 1:57, marquee at 11:53.
- **Removed:** the fumbled handoff into the final topic (2717.77–2757.77, 40 s, "we'll just
  cut all this"). 15 dead-air pauses trimmed (min 2.0 s, keep 0.7 s), 0.5 min. Per Jackson (10/1):
  the Nitro-enclave digression (1780.10–1811.10, 31 s) and the federation-size/Tempo aside
  (2455.50–2538.00, 83 s; `st_operators` dropped with it) removed from the Spark block, which stays
  otherwise whole. Runtime 62.4 min of source → 60.3 min, still above the 45–55 target by choice.
- **Cold open, 4 beats in 48 s** (17.1 / 6.8 / 10.4 / 14.2 s), teasing the finale with beat 4. Beat 1
  first ended at the only all-silent gap in the line, which fell after "Child's" (Jackson caught it);
  it now runs through "in trouble with the wife" and the laugh, ending at 636.0 in the 100 ms dip
  before Tyler's next line (no all-silent gap exists there; the whoosh covers it).
- **Mix:** single track, so no per-host gain. Source peaks at −0.05 dBFS (call-client AGC), which
  clipped a handful of samples in the 16-bit intermediate; `adeclip` leads the chain. All three mics
  measure within 2 dB of each other per band and the floor is −67 to −80 dB, so (per Jackson, "everyone
  has a good mic") the denoiser is gone and the chain is tonal: 150–400 Hz −0.7 dB, 5–9 kHz +1.4 dB,
  9–16 kHz +2.9 dB relative to 1–4 kHz on a 2-min Tyler passage. Stereo channels are identical (L−R −65 dB).
- **Same-speaker splices are punch-ins:** when the shot before and after a splice is the same tile,
  `cut_render.py` renders the post-splice piece in that person's tight crop (or back to the tile), so
  a dead-air trim or a content cut inside one speaker's run reads as a cut, not a jump. Audio/video duration_ts
  match exactly.
- **`verify_silences.py` fix:** silencedetect's first candidate started at −0.000167 s and the
  regex dropped the sign, misaligning every start/end pair → 0 cuts. Both regexes now accept
  negatives.
- Aster, Lightspark, Flashnet, Breez, Tempo, Flashbots, Instinct, Muse named as subjects. No
  employer names in kept spans. The Aster P&L is the show's own account; no price/ETF framing.
- **No disclaimer spoken — TENTH episode running.** End card + descriptions carry it.
