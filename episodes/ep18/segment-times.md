# Permanent Underpod — Ep 18 — Segment Times

**Final cut: 1:01:31 · fully-remote episode, three StreamYard cams (offsets 0 / +0.016 / +0.017
from the filename deltas) plus Chris's screen share of the Perp of Fortune dashboard as a
top-right PiP wherever the share has content (it is black elsewhere) · three-beat 44 s cold
open · title card · end card · whoosh + gold wipe on all 9 transitions · three LIKE + SUBSCRIBE
pop-ups · Jackson's and Chris's earbud mics EQ'd at source (Ep 16 recipe) · 4:20 of content
removed, 25 dead-air pauses trimmed (39 s).**

## Episode video

- **URL:** (Jackson uploads manually; backfill from `yt_fetch.py` after publish)
- **File:** `media/ep18/Permanent Underpod - Ep 18 (Final Cut).mp4`
- **Thumbnail:** `media/ep18/ep18-thumbnail.png` — "AI BREAKS BITCOIN?" (Jackson center, Tyler
  left, Chris right; passed the 320×180 shrink test).
- **Loudness:** delivered −15.5 LUFS integrated, −2.5 dBTP, LRA 4.0 (chain in `render.json`:
  Ep 16 front-end with the 6.8 kHz dynamic de-esser, target_lufs −11.8 / limit 0.7; post-chain
  measured −17.38 LUFS → +5.58 dB make-up).
- **Sync check:** final audio cross-correlated against `edited_raw.mov` at 1:40, 10:00, 25:00,
  40:00, 55:00 and 1:00:50 — lag a constant 35 ms at every point (same as Ep 15/16; no drift).
  A/V stream durations match to 4 ms (3691.067 / 3691.063 s).
- **LIKE + SUBSCRIBE:** all three windows verified in the final MP4: pop-up on frame at 2:16.5 /
  2:18.9, 30:57.5 / 30:59.9, 59:57.5 / 59:59.9, and the SFX cross-correlates at 0.17–0.20 against
  `sfx_likesub.wav` in each window vs 0.002 in the pre-mix audio. Wipes spot-checked at 0:18, 7:54,
  28:42 and 1:00:08; PiP dashboard on frame at 6:20, 29:40 and 1:00:50.
- **Captions:** `episodes/ep18/transcript-attributed.srt` — regenerated from the FINAL cut.

## Title (drafts)

1. **Did OpenAI Just Break Cryptography? (Bitcoin, Banks, Your Browser History)**
2. If AI Breaks Encryption, Your Bitcoin Is Worth Half a Cigarette
3. Would OpenAI Tell Us If It Broke Bitcoin?
4. Who Goes to Jail When Your AI Agent Breaks the Law?

## YouTube description (paste-ready draft)

```
⏩ The cryptography scare is at 7:55. The agent liability bill at 36:15.

OpenAI dropped a paper on 377 families of open math problems and within a day the timeline decided AI was about to break cryptography. Justin Drake told Ethereum holders to go "bunker mode." Matthew Green said we might lose public-key crypto, full stop. Tyler separates Q-Day from a classical break and explains why the real exposure is address reuse, not the curve. Then the harder question: if a lab actually found it, would they tell anyone? Chris walks through Dankrad Feist's take that the internet just goes back to cleartext (Gmail had no TLS until ~2010), and the three of us rank what we'd delete first: browser history, bank logins, or the Bitcoin that would be worth half a cigarette. Open USD is live at $700M issued, and the yield goes to partners, not holders. Chris flags the suspect wallets behind Tempo's $2B. The Hawley/Murphy bill makes the "operator" of an AI agent liable, and the Roman Storm precedent says tokens flowing back and forth may not count as speech. Tyler takes it to the 90s crypto wars and the feudal estate of Salesforce. Jackson's Instinct booked him a tennis tournament every week in six hours; someone else's posted their bank history to work Slack. Perp of Fortune: Tyler's 15-minute coin flips vs the OG perp, with a live dashboard, start to finish.

🔥 On the Agenda
0:00 Cold open
0:49 Welcome back, all three of us
1:38 Perp of Fortune: Tyler's 15-minute coin flips vs the OG perp
6:03 The little man in the computer shorted Circle
7:55 Did OpenAI's math drop just threaten cryptography?
9:08 Justin Drake says go bunker mode
14:38 Q-Day vs a classical break
17:47 Matthew Green and the FUD contagion
19:26 If a lab found it, would they tell us?
22:45 How do you responsibly disclose a broken curve?
24:06 Dankrad: the internet goes back to cleartext
25:16 Open kimono, nude beach, browser history
28:43 Perp halftime: who's winning?
30:06 Open USD is live: $700M issued, who gets the yield
32:51 Tempo's $2B of suspect volume
36:15 The Hawley/Murphy bill: who's liable for your agent?
40:30 Open weights, speech, and Roman Storm
48:23 How crypto got legalized, and what that means for AI
49:46 The cop model and the 90s crypto wars
51:11 Death of IP, death of owning software
54:07 Instinct update: a tennis tournament every week
57:26 The guy whose agent posted his bank history to Slack
1:00:08 Perp of Fortune: final numbers

Recorded fully remote, three cameras, one dashboard.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment.

GLOSSARY
• Perp of Fortune: our tiny real-money perpetual-futures account; an AI picks the trade each week. This week Tyler ran a $25 side bet against it.
• 15-minute markets: prediction-market contracts that resolve every 15 minutes on whether bitcoin went up or down. All-or-nothing by design.
• Q-Day: the hypothetical day a quantum computer can break today's public-key cryptography. Still orders of magnitude short on qubits.
• Classical break: a mathematical shortcut that breaks a curve on ordinary hardware. The scarier, less likely scenario the math paper stirred up.
• Bunker mode: Justin Drake's advice to rotate coins to addresses whose public key has never been revealed on chain.
• Address reuse: spending from an address exposes its public key. Bitcoin wallets rotate addresses; Ethereum reuses one by default.
• Responsible disclosure: telling the affected parties before the public. There is no process for "the curve is broken."
• Cleartext: unencrypted traffic. Dankrad's point: most of the internet ran that way until the 2010s.
• Open USD (OUSD): a new bank-backed stablecoin; $700M issued, yield paid to partner banks prorated, not to holders.
• Tempo: a payments-focused chain reporting $2B of stablecoin volume; Chris says the wallets doing it look like a handful of insiders.
• Hawley/Murphy bill: October 1 Senate bill on AI agent accountability; the loosely defined "operator" carries liability.
• Roman Storm: Tornado Cash developer convicted on a money-transmitter theory for publishing code.
• Crypto wars: the 1990s fight over whether encryption counted as a munition. Open weights are the sequel.
• Instinct: a consumer AI agent that reads your email and calendar and acts for you. Books tennis. Sometimes posts to Slack.

🔔 Subscribe for next week: Tyler's rebuilt Perp of Fortune goes live (the most volatile gambling on the pod), does OpenAI restart training, and does Instinct buy itself a GPU farm?
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (3 beats: Tyler's "they let Claude choose the most conservative trades… the full hero's journey" · Tyler: "your physical Bitcoin will get you half a cigarette" · Jackson: Instinct is "my brother that is unemployed and does whatever I want") |
| 0:44 | Title card |
| 0:49 | Welcome back, all three of us; Chris apologizes for the solo episode |
| 1:38 | Perp of Fortune: Tyler rebuilds the concept as 15-minute bitcoin up/down bets, $25 stake, resolution before the pod ends; Chris: "36 doubles is 1.7 trillion dollars from $25" |
| 6:03 | The OG perp: "the little man in the computer" shorted Circle; dashboard PiP |
| 7:55 | THE MARQUEE: OpenAI's paper on 377 families of open math problems, and the "AI breaks cryptography" day that followed |
| 9:08 | Justin Drake: anyone with coins on chain should go bunker mode; "you gonna go Kendrick on Drake?" |
| 14:38 | Q-Day vs a classical break: Tyler explains; the real exposure is address reuse, and Ethereum reuses by default |
| 17:47 | Matthew Green: "we might lose public-key crypto, full stop"; Tyler on knee-jerking between chicken-little crises |
| 19:26 | If a lab found it, would they tell us? Tyler: they'd withhold it, quietly; Chris: "there's one guy at Cloudflare who knows" |
| 22:45 | How do you responsibly disclose a broken curve? |
| 24:06 | Dankrad Feist: the internet goes back to cleartext; Gmail had no TLS until ~2010 |
| 25:16 | What would you delete first? Open kimono, nude beach, Jackson's browser history, every bank door wide open |
| 28:43 | Perp halftime: Tyler $25 → $40, "more than your perp ever made" |
| 30:06 | Open USD is live: $700M issued (started at $500M); the yield goes to partners, prorated, not holders; dashboard PiP |
| 32:51 | Tempo's $2B of volume came from suspect wallets; correction: Visa + Mastercard do tens of billions a day |
| 36:15 | The Hawley/Murphy AI agent accountability bill (Oct 1): the "operator" is liable, loosely defined |
| 40:30 | Are tokens speech? Roman Storm, Tornado Cash, open weights; Jackson's "really nice kitchen knives" |
| 48:23 | How crypto got legalized, and what that means for AI |
| 49:46 | The cop model, Inglourious Basterds ("a GPU running DeepSeek Flash in this house?"), the 90s crypto wars, RSA as a munition |
| 51:11 | Chris: "it's the death of IP"; Tyler: "peasants on the feudal estate of Salesforce" |
| 54:07 | Instinct update: a tennis tournament every week, booked in 6 hours; "I let it rip while I drool and watch YouTube" |
| 57:26 | Cautionary tale: the guy whose Instinct posted his bank history to work Slack; Tyler: "it bought itself a GPU farm on your dime" |
| 1:00:08 | Perp of Fortune final numbers: Tyler $25 → $10 → $50 → $25, the OG perp down $2 on $100; dashboard PiP; next week the rebuilt perp goes live |
| 1:01:24 | End card (Tyler's rebuilt Perp goes live · does OpenAI restart training · does Instinct buy a GPU farm · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock seconds
(Jackson's track). Rows marked **continuous** are topic wipes on unbroken source. Every splice
sits at the midpoint of a measured all-silent union gap (`check_bounds.py --plan`); content
cuts were micro-whispered at both edges (`mw.sh`).

| Final | What | src out → src in |
|---|---|---|
| 0:18.37 | cold open beat 2 (half a cigarette) | 86.01 → 1856.62 |
| 0:28.10 | cold open beat 3 (unemployed brother) | 1866.34 → 3680.37 |
| 0:44.23 | title card | 3696.50 → |
| 0:48.73 | welcome; 1.9 s of pre-roll dropped | → 1.87 |
| 1:37.53 | welcome → Perp of Fortune — continuous | 50.66 → 50.66 |
| 4:57.33 | dead-air trim (1.14 s) | 250.46 → 251.60 |
| 6:30.03 | dead-air trim (1.14 s) | 344.30 → 345.44 |
| 7:54.63 | perp → marquee — continuous | 430.04 → 430.04 |
| 8:32.53 | dead-air trim (0.92 s) | 467.94 → 468.86 |
| 9:04.53 | dead-air trim (3.40 s) | 500.87 → 504.27 |
| 13:54.53 | dead-air trim (0.97 s) | 794.28 → 795.25 |
| 16:19.40 | post-quantum trade-offs tangent removed (940.18–1051.35, 1:51) | 940.11 → 1051.35 |
| 18:30.77 | Tyler's probability ramble removed (1182.71–1268.51, 1:26) | 1182.70 → 1268.50 |
| 24:27.93 | dead-air trim (3.40 s) | 1625.67 → 1629.07 |
| 24:54.80 | dead-air trim (1.82 s) | 1655.95 → 1657.77 |
| 25:16.30 | dead-air trim (1.59 s) | 1679.27 → 1680.86 |
| 28:42.63 | marquee → perp halftime / OUSD — continuous | 1887.18 → 1887.18 |
| 30:05.73 | dead-air trim (2.57 s) | 1970.28 → 1972.85 |
| 30:08.17 | dead-air trim (1.18 s) | 1975.28 → 1976.46 |
| 30:10.83 | dead-air trim (1.08 s) | 1979.12 → 1980.20 |
| 31:29.20 | dead-air trim (1.40 s) | 2058.55 → 2059.95 |
| 32:32.27 | dead-air trim (1.48 s) | 2123.01 → 2124.49 |
| 35:57.67 | PYUSD sidebar removed (2329.91–2380.60, 0:51) | 2329.90 → 2380.59 |
| 36:15.10 | OUSD → liability bill — continuous | 2398.04 → 2398.04 |
| 36:24.27 | Jackson's "resave" glitch removed (2407.22–2419.19, 0:12) | 2407.20 → 2419.17 |
| 38:42.43 | dead-air trim (2.98 s) | 2557.33 → 2560.31 |
| 40:20.53 | dead-air trim (1.43 s) | 2658.40 → 2659.83 |
| 40:35.77 | dead-air trim (1.03 s) | 2675.06 → 2676.09 |
| 42:07.87 | dead-air trim (1.09 s) | 2768.19 → 2769.28 |
| 46:51.47 | dead-air trim (1.05 s) | 3052.89 → 3053.94 |
| 46:55.93 | dead-air trim (1.10 s) | 3058.42 → 3059.52 |
| 47:06.53 | dead-air trim (1.51 s) | 3070.11 → 3071.62 |
| 48:06.80 | dead-air trim (1.85 s) | 3131.88 → 3133.73 |
| 49:24.47 | dead-air trim (1.39 s) | 3211.39 → 3212.78 |
| 54:06.60 | liability → Instinct — continuous | 3494.92 → 3494.92 |
| 59:15.57 | dead-air trim (0.98 s) | 3803.90 → 3804.88 |
| 59:38.60 | dead-air trim (1.07 s) | 3827.93 → 3829.00 |
| 1:00:07.93 | Instinct → perp wrap — continuous | 3858.32 → 3858.32 |
| 1:00:54.40 | dead-air trim (1.16 s) | 3904.79 → 3905.95 |
| 1:01:24.07 | end card; "Have a good weekend" is the last line | 3935.60 → |

## Spotify description (paste-ready draft)

```
OpenAI dropped a paper on 377 families of open math problems and within a day the timeline decided AI was about to break cryptography. Justin Drake told Ethereum holders to go "bunker mode." Matthew Green said we might lose public-key crypto, full stop. Tyler separates Q-Day from a classical break and explains why the real exposure is address reuse, not the curve. Then the harder question: if a lab actually found it, would they tell anyone? Chris walks through Dankrad Feist's take that the internet just goes back to cleartext (Gmail had no TLS until ~2010), and the three of us rank what we'd delete first: browser history, bank logins, or the Bitcoin that would be worth half a cigarette. Open USD is live at $700M issued, and the yield goes to partners, not holders. Chris flags the suspect wallets behind Tempo's $2B. The Hawley/Murphy bill makes the "operator" of an AI agent liable, and the Roman Storm precedent says tokens flowing back and forth may not count as speech. Tyler takes it to the 90s crypto wars and the feudal estate of Salesforce. Jackson's Instinct booked him a tennis tournament every week in six hours; someone else's posted their bank history to work Slack. Perp of Fortune: Tyler's 15-minute coin flips vs the OG perp, with a live dashboard, start to finish.

The cryptography scare is at 7:55. Chapters: Cold open (0:00) · Welcome back, all three of us (0:49) · Perp of Fortune: 15-minute coin flips vs the OG perp (1:38) · The little man in the computer shorted Circle (6:03) · Did OpenAI's math drop just threaten cryptography? (7:55) · Justin Drake says go bunker mode (9:08) · Q-Day vs a classical break (14:38) · Matthew Green and the FUD contagion (17:47) · If a lab found it, would they tell us? (19:26) · How do you responsibly disclose a broken curve? (22:45) · The internet goes back to cleartext (24:06) · Open kimono, nude beach, browser history (25:16) · Perp halftime (28:43) · Open USD is live: $700M issued (30:06) · Tempo's $2B of suspect volume (32:51) · The Hawley/Murphy bill: who's liable for your agent? (36:15) · Open weights, speech, and Roman Storm (40:30) · How crypto got legalized (48:23) · The cop model and the 90s crypto wars (49:46) · Death of IP, death of owning software (51:11) · Instinct update: a tennis tournament every week (54:07) · The agent that posted a bank history to Slack (57:26) · Perp of Fortune: final numbers (1:00:08)

Recorded fully remote, three cameras, one dashboard. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. Glossary: 15-minute markets = prediction-market contracts that resolve every 15 minutes on whether bitcoin went up or down. Q-Day = the hypothetical day a quantum computer can break today's public-key cryptography; still orders of magnitude short on qubits. Classical break = a mathematical shortcut that breaks a curve on ordinary hardware. Bunker mode = Justin Drake's advice to rotate coins to addresses whose public key has never been revealed. Address reuse = spending from an address exposes its public key; Bitcoin wallets rotate, Ethereum reuses by default. Cleartext = unencrypted traffic; most of the internet ran that way until the 2010s. Open USD = a new bank-backed stablecoin, $700M issued, yield paid to partner banks, not holders. Tempo = a payments chain reporting $2B of stablecoin volume from a handful of suspect wallets. Hawley/Murphy bill = October 1 Senate bill on AI agent accountability; the "operator" carries liability. Roman Storm = Tornado Cash developer convicted on a money-transmitter theory for publishing code. Crypto wars = the 1990s fight over whether encryption counted as a munition. Instinct = a consumer AI agent that reads your email and calendar and acts for you.

Subscribe for next week: Tyler's rebuilt Perp of Fortune goes live, does OpenAI restart training, and does Instinct buy itself a GPU farm?
```

## Captions

`transcript-attributed.srt` regenerated from the FINAL cut (never the raw recording) in
`episodes/ep18/`. Upload as the `standard` track after the episode is live.

## Clips

Not cut yet. Shorts picks from this edit, in rough order of personality: "your physical Bitcoin
will get you half a cigarette" (0:18 / 30:50 src), "the economy is going to crash, bro" (≈24:00;
no clean gap for the cold open, fine as a short with its own edges), "36 doubles is 1.7 trillion
dollars from $25" (≈2:40), "you gonna go Kendrick on Drake?" (≈9:40), "there's one guy at
Cloudflare who knows" (≈21:00), "would my browser history be legible?" (≈26:30), "my unemployed
brother who does what I want" (57:00), "it bought itself a GPU farm on your dime" (≈58:30),
"peasants on the feudal estate of Salesforce" (≈52:00). Bench: anything that says "Perp of
Fortune" in the audio (house jargon).

## Edit decisions of note

- **Order = recording order.** Cold open → title card → welcome → Perp of Fortune → marquee →
  perp halftime → Open USD → liability bill → Instinct → perp wrap → end card. The perp opens
  at 1:38 and its three dashboard beats (6:03, 30:06, 1:00:08) ride the whole show, so no
  reorder beat it. Marquee lands at 7:55: later than the ~2 min default, but the perp rebuild is
  the retainer and it opens at 1:38.
- **Runtime 61.5 min, above the 45–55 target.** 4:20 of content came out (post-quantum
  trade-offs 1:51, Tyler's probability ramble 1:26, PYUSD sidebar 0:51, the "resave" glitch
  0:12) plus 39 s of dead air across 25 pauses. Four more candidates were dropped because no
  all-silent gap or a mid-sentence edge: the Coinbase-cryptographer thread (1412–1477), the
  Gemini aside (2945–2990), the Privy sidebar (2197–2250), and the cold-open beat "the economy
  is going to crash, bro" (1626–1642). The next 5 min would come out of the liability block
  (36:15–54:07, 18 min) if Jackson wants it tighter; every join there crosses a crosstalk edge.
- **Cold open, 3 beats in 44 s** (18.4 / 9.7 / 16.1 s): Tyler's "they let Claude choose the most
  conservative trades" perp rebuild pitch, Tyler's half-a-cigarette line (the marquee payoff),
  Jackson's unemployed-brother Instinct line (the finale tease). Under the 60 s hard cap.
- **Perp of Fortune dashboard as PiP:** Chris's screen share (`chris-screen-00h_05m_29s_469ms`)
  is anchored to the session clock at master 329.127 (filename offset 329.469 minus Jackson's
  0.342). The share is black except at screen-file 0–29 s, 1612–1623 s and 3560–3607.5 s, so the
  PiP is up only for those three windows (final 6:15–6:42, 29:36–29:47, 1:00:39–1:01:24; crop
  `[936,212,484,356]`, top-right corner). Jackson's "perp ends with the video" note checks out:
  the share's last frame lands on the webcams' end.
- **Three LIKE + SUBSCRIBE pop-ups** at 2:15 (PERP +37.467), 30:56 (OUSD +133.367) and 59:56
  (INSTINCT +349.4): 6 s windows clear of cards, wipes, lower thirds, stats and PiP entrances.
- **Mics:** Jackson and Chris on earbud mics again, same signature as Ep 16 (presence −11/−13 dB
  and sibilance −21/−23 dB relative to full-band vs Tyler −7/−12). Ep 16 EQ chains applied at
  source (`src/*_720eq.mov`, PCM, video copied; `_eq.sh`). Mix chain = Ep 16 (6.8 kHz dynamic
  de-esser, target_lufs −11.8 / limit 0.7).
- **Speaker balance:** `gain_spans` (four trusted solo passages per host) with `gain_target`
  0.028. Held-out solo RMS: Jackson −30.7/−31.1, Chris −29.9/−31.7, Tyler −27.9/−27.2 dB.
  Tyler ~3 dB hot, left to the leveler as in Ep 16.
- **Mix headroom:** edited_raw.mov peak −1.95 dBFS, zero flat samples. Audio/video duration_ts
  match exactly (110,732 frames = 177,171,200 samples).
- **Split-screen framing:** `face_cx` measured with the Vision tool (`facex.swift`) every 60 s
  (medians jackson 644, chris 613, tyler 662) after a first test render clipped Tyler's face at
  the right edge of his trio panel with an eyeballed 500. Duo/trio clips re-rendered.
- **Stat callouts and lower thirds** shortened once: `graphics.py` caught a 1075 px stat and two
  lower thirds (1308 / 1403 px) that overflowed the 1280 frame.
- **Sync bench not built**: StreamYard filename deltas as in Ep 14–16. The turn-gap validator
  reported Tyler +0.90 s (Ep 16 showed ±0.35 with correct offsets, so the estimator is noisy),
  and no slip is visible on the test frames. Jackson to confirm by ear on the live copy; if
  Tyler reads late, `offsets.json` tyler is the one knob.
- **No disclaimer spoken on any track — TENTH episode running.** End card + descriptions carry it.
- OpenAI, Justin Drake, Matthew Green, Dankrad Feist, Cloudflare, Circle, Tempo, Open USD,
  Instinct, Roman Storm, Salesforce, DeepSeek are named as subjects of the stories. No employer
  names in kept spans; no BTC price/ETF framing (Tyler's 15-minute bets are framed as the
  gambling product, not as a price call).
