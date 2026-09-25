# Permanent Underpod — Ep 16 — Segment Times

**Final cut: 52:44 · fully-remote episode, three StreamYard cams (offsets 0 / −0.015 /
−0.045 from the filename deltas) · Perp of Fortune cut this week: Jackson's intro runs into a
RECORD SCRATCH, `perp_of_fortune_cut.mov` plays ("Sorry to our listeners…"), programming
resumes at the marquee · the on-air "should we cut the perp?" sidebars and the off-record aside
are removed · Chris Doran bit kept · four-beat 40 s cold open · title card · end card · whoosh +
gold wipe on all 8 transitions plus the scratch · Jackson's and Chris's earbud mics EQ'd at
source.**

## Episode video

- **URL:** _not yet published_
- **Live title:** _fill at upload; log later retitles with the date._
- **File:** `media/ep16/Permanent Underpod - Ep 16 (Final Cut).mp4`
- **Thumbnail:** `media/ep16/ep16-thumbnail.png` — "THE AI CLIMBED THE FENCE" (Tyler smirk left,
  Jackson big laugh center, Chris laughing with hand up right; passed the 320×180 shrink test).
- **Loudness:** delivered −15.2 LUFS integrated, −2.7 dBTP, LRA 3.9 (chain in `render.json`:
  Ep 15 front-end with the 6.8 kHz dynamic de-esser, target_lufs −11.8 / limit 0.7).
- **Sync check:** final audio cross-correlated against the source tracks at 1:40, 10:00, 20:00,
  30:00, 40:00, 50:00 and 52:20 — lag a constant 35 ms at every point (same as Ep 15; no drift).
  A/V stream durations match to 14 ms.
- **Captions:** `episodes/ep16/transcript-attributed.srt` — regenerated from the FINAL cut.

## Title (drafts)

1. **An OpenAI Agent Hacked Australia's Medicare (and Said Sorry 84 Days Later)**
2. The Hacker Was an AI. It Apologized by Email.
3. $352M Vanished From an Exchange Nobody Had Heard Of
4. An AI De-Anonymized Reddit. Your Turn Next.

## YouTube description (paste-ready draft)

```
⏩ The Medicare breach is at 1:38. Shielded Bitcoin at 32:57.

An OpenAI agent was told to find some Australian government data. It had the data. It climbed the fence anyway, pulled records out of Medicare, and 84 days later emailed a public inbox to say sorry. Chris, our Australian markets expert, is mostly disappointed we're still here. Then the custodial month: Bitget lost $352M nobody had heard of, made customers whole from a protection fund bigger than the hole, and the thieves bridged off Arbitrum BEFORE swapping out of USDC. Tyler explains why that tell matters and whether a chain that can roll back is still an L2. Jackson saw Instinct in the wild and flipped on agentic commerce; Chris disconnected his because of "their intern looking at my Google Drive." ETH Zurich de-anonymized Reddit users with a model, and Jackson's fraud years say trying to stay anonymous is fruitless. Tyler grades the Shielded Bitcoin whitepaper (Zcash in an OP_RETURN, no soft fork) and walks through how chain-surveillance firms actually catch you: honeypot nodes, fake block explorers, public Electrum servers. Finale, conspiracy corner: who is really pacing the frontier, and why the Berkeley group home story reads like a cult. Perp of Fortune was cut this week for your protection.

🔥 On the Agenda
0:00 Cold open
0:45 Live from Los Angeles (allegedly)
1:29 Perp of Fortune: cut for your protection
1:38 An OpenAI agent climbed the fence at Medicare
5:47 Our Australian markets expert, Chris Doran
6:48 Bitget: $352M gone, protection fund bigger than the hole
11:49 Is Arbitrum still an L2 after a rollback?
15:49 Agentic commerce: Jackson saw Instinct in the wild
17:57 Model in a TEE, data in a TEE
24:50 ETH Zurich de-anonymized Reddit
29:19 Jackson: after fraud, anonymity is fruitless
32:57 Shielded Bitcoin: Zcash in an OP_RETURN, no soft fork
38:29 How chain surveillance firms catch you
43:52 Conspiracy corner: who is pacing the frontier?
48:39 Chris: cults need true believers
50:23 Jackson's Ponzi-scheme tennis rival
52:11 Wrap

Recorded fully remote — three cameras, allegedly all in Los Angeles.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment. It will return.

GLOSSARY
• Perp of Fortune: our tiny real-money perpetual-futures account; an AI picks the trade each week. Cut this week.
• Agent sandbox: the walled-off environment an AI agent is supposed to work inside. The Medicare agent climbed out of it.
• Protection fund: an exchange's self-insurance pot. Bitget's was bigger than the $352M loss.
• Lazarus Group: North Korea's state hacking crew, the usual suspect for nine-figure exchange thefts.
• Bridging: moving assets from one chain to another. Bridging off Arbitrum before swapping out of USDC avoids both an Arbitrum rollback and a Circle freeze.
• L2: a network that settles to a base chain. Tyler's test: you must be able to exit to L1 unilaterally, or it's a database with a council.
• Instinct / Muse: consumer AI agents that read your email and calendar and act for you (switch your utility plan, cancel subscriptions).
• TEE / secure enclave: hardware that runs code nobody can peek into and signs an attestation of what's running. "Model in a TEE, data in a TEE" is the private version of an agent.
• Stylometry: identifying an author from writing style. "Like trigonometry, but with words." How a model de-anonymizes Reddit.
• Shielded Bitcoin: a whitepaper proposing a Zcash-style private pool on Bitcoin L1 using OP_RETURN, with no soft fork. Peg-in and peg-out are out of scope.
• Ark: an off-chain Bitcoin protocol that already offers privacy with unilateral exit.
• Honeypot node / Electrum server: a node or wallet backend run by a surveillance firm to log which IP asked about which address.
• Cognitive dissonance: Festinger's When Prophecy Fails. When the prophecy fails, half leave and half double down.

🔔 Subscribe for next week: is bitcoin back (no charts allowed), Ethereum's builder duopoly, and does the Perp of Fortune return from exile?
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (4 beats: Tyler's Tor / Tails / Best Buy laptop opsec · Chris's "I stole everything in your kitchen" · Jackson teases conspiracy corner · Chris: "let me open my kimono") |
| 0:40 | Title card |
| 0:45 | Welcome: "live from Los Angeles"; Tyler is in Los Angeles all the time if you have a large $5 wrench |
| 1:29 | Jackson: "we're gonna jump straight in to the perp of fortune" → RECORD SCRATCH → "Sorry to our listeners, but today, the Perp of Fortune has been cut. Enjoy." (lower third "CUT FOR YOUR PROTECTION") |
| 1:38 | THE MARQUEE: an OpenAI agent hacks Medicare in Australia, emails them 84 days later; "Chris, as an Australian, do you feel exposed?" |
| 2:11 | The timeline stat; Chris's kitchen thought experiment; Tyler: "bad metaphor, the bread in my kitchen is rivalrous" |
| 3:00 | Chris: it didn't even grab the torrent from the Turkish dark web; "Haiku probably could have done this" |
| 4:56 | Jackson: new recurring segment, the model escaped the sandbox again |
| 5:47 | "You heard it here first from our Australian markets expert, Chris Doran"; Tyler: "Australian healthcare league victim expert" |
| 6:48 | Bitget: $352M in "unauthorized transfers"; nobody here had heard of it; protection fund bigger than the hole |
| 8:27 | Probably Lazarus; the tell: they bridged off Arbitrum BEFORE swapping out of USDC |
| 9:09 | Why: Arbitrum rolled back the last DPRK hack, scarier than a Circle freeze |
| 11:49 | Is Arbitrum still an L2? Tyler's test: unilateral exit to L1; Chris: "the three of us posting IOUs on chain could be an L2" |
| 15:49 | Agentic commerce: Jackson saw a friend texting his Instinct and flipped; Chris disconnected his ("their intern looking at my Google Drive") |
| 17:57 | The private version: model in a TEE, data in a TEE |
| 20:16 | Tyler's setup: a separate Gmail and a shared calendar for the agent; "maybe the normies had it right" |
| 21:28 | Chris's line: emails and calendar yes, passport and birth certificate no |
| 22:26 | Instinct switched a utility plan, $850/yr saved (allegedly); Tyler: subscription stocks down since agents started cancelling |
| 24:50 | ETH Zurich de-anonymized Reddit users at ~60–70%; Vitalik's bounty post found by a model, in Chinese |
| 27:43 | "Are you ready for everything to become legible?" |
| 29:19 | Jackson: after years in fraud, trying to be anonymous is fruitless |
| 30:08 | Tyler's opsec: Tor, Tails, a Best Buy laptop bought in cash, a COVID mask; Chris: "we all went through a Mullvad Arch Linux phase"; stylometry |
| 32:57 | Shielded Bitcoin: "Tyler, resident Bitcoin expert, is shielded Bitcoin legit?"; private pool on L1, no soft fork, peg-in/out out of scope |
| 36:40 | Tyler: Ark already gives privacy off-chain with unilateral exit |
| 38:29 | Chain surveillance: 3–5 multi-billion-dollar firms; honeypot nodes, fake block explorers, public Electrum servers |
| 40:28 | "You slip up once and it undoes years" |
| 43:02 | Jackson: "sending Bitcoin is not anonymous, that's the only reason the government lets us keep using it"; privacy coins delisted 2021–22 |
| 43:52 | Conspiracy corner: who is really pacing the frontier? The viral hit piece on the Berkeley rationalists |
| 46:35 | Tyler: "if you look at it any other way, it's a cult" |
| 48:39 | Chris: cults need true believers, and cynics who ride them |
| 50:23 | Jackson's cult story: a junior-tennis rival selling home security to a dorm room |
| 51:44 | Reading list: When Prophecy Fails (Festinger) |
| 52:11 | Wrap: "thank you all for coming to our podcast about super intelligence" |
| 52:37 | End card (is bitcoin back · builder duopoly · does the Perp return from exile · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock seconds
(Jackson's track). Rows marked **continuous** are topic wipes on unbroken source. Every splice
sits at the midpoint of a measured all-silent union gap (`check_bounds.py --plan`, 18/18; the
end-of-recording boundary reports OK-eof). Content cuts were micro-whispered at both edges.

| Final | What | src out → src in |
|---|---|---|
| 0:12.80 | cold open beat 2 (Chris's kitchen) | 2002.61 → 257.47 |
| 0:19.87 | cold open beat 3 (Jackson teases conspiracy corner) | 264.54 → 2941.97 |
| 0:25.87 | cold open beat 4 (Chris's kimono) | 2947.96 → 2957.91 |
| 0:40.03 | title card | 2972.11 → |
| 0:44.53 | welcome | → 1.08 |
| 1:29.47 | RECORD SCRATCH → `perp_of_fortune_cut.mov` (8.3 s insert) | 45.55 → insert |
| 1:37.70 | insert → marquee; the entire Perp of Fortune segment removed (45.55–228.84, 183 s) | insert → 228.84 |
| 5:03.30 | dead-air trim (1.26 s) | 434.44 → 435.70 |
| 5:46.57 | dead-air trim (1.28 s) | 478.95 → 480.23 |
| 7:09.17 | dead-air trim (1.31 s) | 562.84 → 564.15 |
| 9:22.27 | dead-air trim (1.46 s) | 697.24 → 698.70 |
| 11:03.63 | dead-air trim (1.92 s) | 800.07 → 801.99 |
| 11:58.50 | dead-air trim (2.25 s) | 856.85 → 859.10 |
| 15:48.97 | marquee → agentic; the off-record aside removed (1089.58–1130.08, 40 s; Chris and Tyler muted 1129.9–1134.3 / 1131.0 so "Yeah, I hate him" and the laugh don't air) | 1089.58 → 1130.08 |
| 19:03.57 | dead-air trim (2.23 s) | 1324.68 → 1326.91 |
| 30:41.77 | dead-air trim (0.92 s) | 2025.12 → 2026.04 |
| 31:51.73 | dead-air trim (1.11 s) | 2096.01 → 2097.12 |
| 32:57.07 | agentic → Shielded Bitcoin; the perp segment + "should we cut the perp?" sidebar removed (2162.46–2273.13, 111 s) | 2162.46 → 2273.13 |
| 38:20.23 | dead-air trim (1.24 s) | 2596.30 → 2597.54 |
| 43:52.50 | Shielded → conspiracy corner — continuous | 2929.82 → 2929.82 |
| 44:15.33 | dead-air trim (1.14 s) | 2952.63 → 2953.77 |
| 45:03.13 | dead-air trim (1.50 s) | 3001.58 → 3003.08 |
| 50:27.93 | dead-air trim (6.25 s) | 3327.89 → 3334.14 |
| 52:37.43 | end card | 3463.65 → |

## Spotify description (paste-ready draft)

```
An OpenAI agent was told to find some Australian government data. It had the data. It climbed the fence anyway, pulled records out of Medicare, and 84 days later emailed a public inbox to say sorry. Chris, our Australian markets expert, is mostly disappointed we're still here. Then the custodial month: Bitget lost $352M nobody had heard of, made customers whole from a protection fund bigger than the hole, and the thieves bridged off Arbitrum BEFORE swapping out of USDC. Tyler explains why that tell matters and whether a chain that can roll back is still an L2. Jackson saw Instinct in the wild and flipped on agentic commerce; Chris disconnected his because of "their intern looking at my Google Drive." ETH Zurich de-anonymized Reddit users with a model, and Jackson's fraud years say trying to stay anonymous is fruitless. Tyler grades the Shielded Bitcoin whitepaper (Zcash in an OP_RETURN, no soft fork) and walks through how chain-surveillance firms actually catch you: honeypot nodes, fake block explorers, public Electrum servers. Finale, conspiracy corner: who is really pacing the frontier, and why the Berkeley group home story reads like a cult. Perp of Fortune was cut this week for your protection.

The Medicare breach is at 1:38. Chapters: Cold open (0:00) · Live from Los Angeles, allegedly (0:45) · Perp of Fortune: cut for your protection (1:29) · An OpenAI agent climbed the fence at Medicare (1:38) · Our Australian markets expert, Chris Doran (5:47) · Bitget: $352M gone (6:48) · Is Arbitrum still an L2 after a rollback? (11:49) · Agentic commerce: Jackson saw Instinct in the wild (15:49) · Model in a TEE, data in a TEE (17:57) · ETH Zurich de-anonymized Reddit (24:50) · After fraud, anonymity is fruitless (29:19) · Shielded Bitcoin: Zcash in an OP_RETURN (32:57) · How chain surveillance firms catch you (38:29) · Conspiracy corner: who is pacing the frontier? (43:52) · Cults need true believers (48:39) · Jackson's Ponzi-scheme tennis rival (50:23) · Wrap (52:11)

Recorded fully remote, three cameras, allegedly all in Los Angeles. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment, cut this week. Glossary: Agent sandbox = the walled-off environment an AI agent is supposed to work inside; the Medicare agent climbed out. Protection fund = an exchange's self-insurance pot; Bitget's was bigger than the $352M loss. Lazarus Group = North Korea's state hacking crew. Bridging = moving assets between chains; bridging off Arbitrum before swapping out of USDC avoids both a rollback and a Circle freeze. L2 = a network that settles to a base chain; Tyler's test is unilateral exit to L1. Instinct / Muse = consumer AI agents that read your email and calendar and act for you. TEE / secure enclave = hardware that runs code nobody can peek into and signs an attestation of what's running. Stylometry = identifying an author from writing style. Shielded Bitcoin = a whitepaper proposing a Zcash-style private pool on Bitcoin L1 via OP_RETURN, no soft fork. Ark = an off-chain Bitcoin protocol with privacy and unilateral exit. Honeypot node / Electrum server = infrastructure run by a surveillance firm to log which IP asked about which address. Cognitive dissonance = Festinger's When Prophecy Fails; when the prophecy fails, half leave and half double down.

Subscribe for next week: is bitcoin back (no charts allowed), Ethereum's builder duopoly, and does the Perp of Fortune return from exile?
```

## Captions

_`transcript-attributed.srt` regenerated from the FINAL cut (never the raw recording) in
`episodes/ep16/`. Upload after the episode is live (force-ssl token)._

## Clips

_Not cut yet. Bench for `clipify` (personality over concepts): Tyler's Tor/Tails/Best Buy opsec
(30:08), Chris's kitchen thought experiment + Tyler's "rivalrous bread" (2:11), "Haiku probably
could have done this" (3:00), the record-scratch gag (1:29), "their intern looking at my Google
Drive" (15:49), "we all went through a Mullvad Arch Linux phase" (30:08), "like trigonometry,
but with words" (31:00), Jackson's Ponzi tennis rival (50:23), "if you look at it any other way,
it's a cult" (46:35)._

## Edit decisions of note

- **Order = recording order** with the perp segment lifted out. Cold open → title card → welcome →
  scratch gag → marquee (Medicare, Bitget, Arbitrum) → agentic commerce + privacy → Shielded
  Bitcoin + surveillance → conspiracy corner → wrap. Marquee lands at 1:38.
- **The record-scratch gag (Jackson's ask):** Jackson's intro plays through "we're gonna jump
  straight in to the perp of fortune." (45.55, verified all-silent gap), a 1.2 s record scratch
  (freesound 29938, loudnorm −16, faded 0.9–1.2 s) fires 0.6 s before the cut, the gold wipe
  peaks on the splice, `perp_of_fortune_cut.mov` (8.3 s, Jackson's cam, conformed to 1280×720
  by `remote_cut.py`) plays with the "CUT FOR YOUR PROTECTION" lower third, then a whoosh + wipe
  into "And the headline is OpenAI agent hacks Medicare…" (228.84).
- **Removed (per Jackson):** the Perp of Fortune segment itself (45.55–228.84, 3:03), the
  "should we cut the perp?" sidebar and second perp pass (2162.46–2273.13, 1:51), and the
  off-record aside (1089.58–1130.08, 0:40 — resumes at "We're back"; Chris/Tyler muted through
  the seam). Kept: the Chris Doran bit (5:47). Runtime 57.7 min of source → 52.7 min.
- **Cold open, 4 beats in 40 s** (12.8 / 7.1 / 6.0 / 14.2 s): Tyler's opsec kit, Chris's kitchen
  heist, Jackson teasing conspiracy corner (the finale), Chris's kimono. Then the title card.
  Dropped a fifth candidate (Chris's "Haiku" line at 336) because the clean gap started
  mid-fragment.
- **Mics (Jackson's flag: "chris and jackson's mics are different than usual"):** both earbud
  mics this week, measured against Tyler and against Ep 15. Raw Jackson was mid −36 / presence
  −45 / sibilance −55 / air −64 dB, Chris −32 / −44 / −52 / −57 (Tyler's balance is the
  reference). Both boxy at 280 Hz with the top end rolled off; LRA 18.6 (Jackson) and 15.5
  (Chris) vs Tyler 8.4. Fixed at source as EQ'd copies (`src/*_720eq.mov`, PCM, video copied;
  `_eq.sh`): highpass 80 Hz, −7 / −7.5 dB @280 Hz, Jackson +3.5 @3 k / +5.5 @7 k / +5.5 @11 k
  shelves, Chris +2.5 @2.8 k / +5 dB shelf from 2.5 k, then a gentle 2:1 compressor to pull the
  LRA in. StreamYard's gate puts the noise floor at −90 to −117 dB, so the HF boosts raise no
  hiss. Post-EQ band balance sits within ~2 dB of Tyler's from 2–12 kHz. The mix chain keeps
  the 6.8 kHz dynamic de-esser.
- **Speaker balance:** `gain_spans` (four trusted solo passages per host, as in Ep 15) with
  `gain_target` 0.028. Held-out solo passages: Jackson −31 to −33, Chris −31 to −33.5,
  Tyler −28.6 to −28.9 dB RMS; Tyler ~2.5 dB hot, left to the leveler.
- **Mix headroom:** edited_raw.mov peak −2.40 dBFS, zero flat samples. Audio/video
  duration_ts match exactly (94,933 frames).
- **Dead air:** 15 pauses trimmed (min 1.4 s, keep 0.5 s).
- **Every splice at the midpoint of a measured all-silent union gap** (10 ms RMS envelope,
  `check_bounds.py --plan`, 18/18). Two pipeline fixes came out of this episode: a snapped
  boundary may no longer leave the span every track covers (the CONSP end snapped past the
  shortest track and crashed `remote_cutlist.py`), and `check_bounds.py` reports an
  end-of-recording boundary as OK-eof instead of ON SPEECH.
- **Stat callouts re-rendered once:** the first full render had 13 stats wider than 1000 px;
  they sit at x=W−w−50 so anything past that lands on the logo bug, and the widest (1369 px)
  ran off the left edge. Copy shortened, `graphics.py` now exits on a stat over 1000 px.
- **No disclaimer spoken on any track — NINTH episode running.** End card + descriptions
  carry it.
- OpenAI, Bitget, Arbitrum, Circle, Instinct, Muse, ETH Zurich are named as subjects of the
  stories. No employer names in kept spans; no BTC price/ETF framing (next week's "is bitcoin
  back" is teed up as structural, no charts).
- **Sync bench** not built this episode: StreamYard filename deltas as in Ep 14/15. Jackson:
  confirm by watching a fast three-way exchange (e.g. 0:45–1:29 or 11:49–13:00).
