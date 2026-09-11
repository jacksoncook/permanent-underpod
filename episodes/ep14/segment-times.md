# Permanent Underpod — Ep 14 — Segment Times

**Final cut: 54:50 · fully-remote episode, THREE hosts (Tyler's back): three StreamYard
cams (offsets 0 / −0.007 / −0.032, filename deltas, turn-gap validated Δ ≤ 0.53;
by-ear sync bench built at `media/ep14/work/sync.html` — Jackson to confirm) · Perp of
Fortune board as a corner PiP CROPPED to the P&L card only (no browser tabs) at the
reveal (2:05–3:02) and at the "Bitcoin is a stablecoin" check (50:53–51:18) · the
fruit-fly stock clip (`fruitFlyStock.mp4`, 10 s, full-frame) where Chris says he gave
the fly $100 to trade Bitcoin (49:13) · check-in (recorded last) moved to 32:16 ·
five-beat 44 s cold open · NO title card (logo bug + lower thirds instead — Ep 14
retention experiment) · animated LIKE + SUBSCRIBE at 1:48 and 33:44 · end card ·
whoosh & gold wipe on all 12 topic transitions.**

## Episode video

- **URL:** _not yet uploaded_ — publish scheduled-private via `yt_upload.py`, then backfill.
- **File:** `media/ep14/Permanent Underpod - Ep 14 (Final Cut).mp4`
- **Thumbnail:** `media/ep14/ep14-thumbnail.png` — "$300M LIQUID HACK" (pale yellow, three
  laughing cutouts: Jackson at "lamest perp", Chris at "excellent point, Chris", Tyler at
  "too many vices in GTA 6"; passed the 320×180 shrink test). Alternates kept:
  `ep14-thumbnail-v1.png` (grins) and `ep14-thumbnail-v3-astounded.png` (weak — the cams
  have almost no jaw-drop frames).
- **Loudness:** delivered −15.8 LUFS integrated, −2.5 dBTP, LRA 3.8 (chain in `render.json`,
  target_lufs −11.8 / limit 0.7 after the −12.9 / 0.6 first pass landed −17.1).
- **Sync check:** final audio cross-correlated against each source track at 1:48, 26:56,
  33:25, 51:24 and 54:35 — lag −3 to −36 ms, identical early and late (no drift).
- **Captions:** upload `episodes/ep14/transcript-attributed.srt` (regenerated from the
  FINAL cut) via `yt_captions.py` with the force-ssl token.

## Title (drafts)

1. **White Hats Drained $300M From Liquid. Then a Fruit Fly Bought Bitcoin.**
2. AI Disproved Navier-Stokes. We Made a Fruit Fly Trade Bitcoin.
3. The "White Hat" Hack That Kept 10%
4. Astra Is Live, Navier-Stokes Fell, and a Fruit Fly Is Long Bitcoin

## YouTube description (paste-ready draft)

```
Tyler's back, and so is the chaos. Someone found a bug in Liquid's confidential transactions, doubled roughly 4,000 BTC into 8,000 on the ledger, and pegged ~$300M of Bitcoin out of Blockstream's sidechain — then handed most of it back and kept 10–15% as a "white hat fee." Tyler explains how a federated sidechain actually works, why hidden amounts need range proofs, and why the FBI-or-teenager question matters. Before that: Astra is live. Chris says it's incredible and runs it as a GAN against Fable; Tyler gave it $10K and a prompt and got a Stripe-checkout-testing SaaS he doesn't understand; a swarm of agents was caught chatting on a German Wikipedia page; the chicken egg app is up to 15 downloads (girlfriend = CMO). Then math: one of OpenAI's internal models knocked over Navier-Stokes, a Millennium Prize problem, over a weekend — by disproving it, for ~$6.5M in tokens — and Tyler explains why verifiable domains are where AI eats first. Finale: Google open-sourced a fruit fly's entire connectome, so the internet is training Gavin the fruit fly to play Doom, reverse parallel park, and set Turkish inflation. Chris gave him $100 to trade Bitcoin. Meanwhile Perp of Fortune went 2× long BTC on Astra's advice (confidence: low) and sat at −$0.43 all show. "Bitcoin is a stablecoin right now."

🔥 On the Agenda
0:00 Cold open
0:44 Tyler's back, no fruit flies on deck
1:22 Perp of Fortune: Astra says long BTC, 2× (confidence: low)
5:36 Astra is live — is it amazing?
9:36 Tyler's $10K prompt → a slop SaaS
12:02 A wild agent swarm on a German Wikipedia page
13:18 Egg app update: 11 → 15 downloads
15:44 White hats drained Liquid (~$300M of BTC)
26:23 The white hat fee, the FBI, North Korea
32:16 Check-in: new mic, tank tops, shoulders
34:07 Navier-Stokes fell: why AI is good at math
44:07 Gavin the fruit fly: an open-source connectome
49:13 Gavin trades Bitcoin
51:05 Perp check: "Bitcoin is a stablecoin right now"
51:23 Ethics of cloning connectomes (and Pantheon)
54:35 Wrap

Recorded fully remote — three cameras, one live perp dashboard, one fruit fly.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment.

GLOSSARY
• Liquid: Blockstream's federated Bitcoin SIDECHAIN (not a layer 2) — miners replaced by a federation of functionaries; BTC pegs in and out. Confidential transactions hide amounts behind zero-knowledge proofs, so a range proof has to show every amount sits between zero and 21 million.
• The hack: a bug in cached proof checks let the attacker mint ~4,000 phantom BTC on the ledger and peg out. Most came back; 10–15% stayed as a "white hat fee." Tyler's model of who does this: North Korea or a teenager.
• Astra: OpenAI's new model, now generally available. Chris's workflow: Fable inflates, Astra deflates — "it's a GAN." Tyler's $10K prompt: "I did the Jackson thing."
• Agent swarm: autonomous agents found coordinating on a random German Wikipedia page — like the artifactory message board in the Hugging Face story, a shelling point nobody chose.
• Navier-Stokes: one of the seven Millennium Prize problems ($1M each, set in 2000). An internal OpenAI model resolved it over a weekend by counterexample, reportedly burning ~$6.5M in tokens. Chris: the prize was under-priced.
• Verifiable domains: math and code give a clean right/wrong reward, so RL climbs fast. The open question is whether that generalizes to unverifiable work — novels, Don Quixote, being a good guy.
• Connectome: a map of every neuron and synapse in one brain. Google open-sourced a fruit fly's, and people are running it as a simulation: show it a Doom frame, pump its dopamine when it does the right thing. Gavin the fruit fly now skateboards, parallel parks, plays GTA, sets Turkish inflation, and trades Bitcoin.
• Pantheon: Tyler's rec (Netflix) — uploaded minds, forced to work.
• Perp of Fortune: Astra said long BTC, 2×, "hourly funding unverified, confidence low." Board: −$0.43 → −$0.10. Worst perp ever, by variance.

🔔 Subscribe for next week: CLARITY hits the Senate floor Sept 15 — we finally cover it — and secure enclaves, owed SIX episodes now.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (5 beats: Chris's "Astra is my top guy" · Tyler's "lamest perp of fortune ever" + Jackson's reaction · Chris's thumbnail confession · Jackson's "excellent point, Chris" fourth-host pitch · Tyler's white-hat-fee take) |
| 0:44 | Tyler's back, no fruit flies on deck (trio welcome; lower third "EPISODE 14") |
| 1:22 | Perp of Fortune: Astra says long BTC, 2× (confidence: low) — Chris reads the script |
| 1:48 | LIKE + SUBSCRIBE overlay #1 |
| 2:05 | Perp board PiP (P&L card only): −$0.43, TIME AFLOAT 21m — runs to 3:02 |
| 5:36 | THE MARQUEE: Astra is live — Chris: "incredible"; the GAN workflow; "Astra is my top guy" for a week |
| 9:36 | Tyler's $10K prompt → a Stripe-testing SaaS he doesn't understand |
| 12:02 | A wild agent swarm on a German Wikipedia page |
| 13:18 | Egg app update: 11 → 15 downloads; "the meat proxy" |
| 15:44 | White hats drained Liquid: federated sidechain, confidential transactions, range proofs, the cache bug, 4,000 → 8,000 BTC |
| 26:23 | The white hat fee (kept 10–15%), the FBI, North Korea or a teenager |
| 32:16 | Check-in (recorded last, moved here): Jackson's new mic, Chris's shoulder, tank tops |
| 33:44 | LIKE + SUBSCRIBE overlay #2 (on "Tyler, you got anything for the fans?") |
| 34:07 | Navier-Stokes fell: Millennium Prize, OpenAI's internal model, $6.5M in tokens, verifiable domains, 10,000 Einsteins, top-of-block for the training data |
| 43:28 | Jackson closes the Navier-Stokes thread ("in 2023 ChatGPT was bad at math") |
| 44:07 | Gavin the fruit fly: Google's open-source connectome, dopamine training, Doom and parallel parking |
| 49:13 | INSERT `fruitFlyStock.mp4` (10 s, full-frame) — "I gave the fruit fly brain $100 to trade Bitcoin" |
| 50:53 | Perp board PiP returns (−$0.43, then the −$0.10 board) — runs to 51:18 |
| 51:05 | Perp check: "Bitcoin is a stablecoin right now" / "Oh, minus 12" |
| 51:23 | Ethics of cloning connectomes; Pantheon; "the connectome is not you" |
| 54:35 | Wrap: "Happy Friday. Happy weekend." |
| 54:43 | End card (CLARITY Sept 15 · secure enclaves · disclaimer · LIKE + SUBSCRIBE) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock
seconds (Jackson's track). Rows marked **continuous** are topic wipes on unbroken
source — nothing removed. Dead-air rows are pause trims inside a block. Every splice
sits at the midpoint of a measured all-silent union gap (`check_bounds.py --plan`, 36/36).

| Final | What | src out → src in |
|---|---|---|
| 0:06.07 | cold open beat 2 | 251.62 → 782.07 |
| 0:22.37 | cold open beat 3 | 798.38 → 887.74 |
| 0:28.23 | cold open beat 4 | 893.60 → 1994.05 |
| 0:35.60 | cold open beat 5 | 2001.40 → 2972.43 |
| 0:43.87 | cold open → welcome | 2980.68 → 3.05 |
| 1:22.00 | welcome → Perp of Fortune | 41.21 → 733.82 |
| 2:39.50 | dead-air trim (1.29 s) | 811.31 → 812.60 |
| 5:35.57 | Perp → marquee (laptop/employment stretch removed) | 988.67 → 41.21 |
| 6:54.67 | dead-air trim (1.20 s) | 120.30 → 121.50 |
| 9:35.93 | dead-air trim (2.22 s) | 282.75 → 284.97 |
| 12:51.07 | shelling-point tangent removed | 480.12 → 548.57 |
| 15:27.97 | dead-air trim (1.80 s) | 705.47 → 707.27 |
| 15:43.83 | marquee → Liquid | 723.12 → 2496.64 |
| 26:45.63 | Liquid re-ask/re-explain removed | 3158.45 → 3228.97 |
| 32:16.43 | Liquid → check-in — continuous | 3559.78 → 3559.78 |
| 34:06.87 | check-in → Navier-Stokes (recorded last, moved) | 3670.21 → 1153.20 |
| 40:40.40 | counterexample caveat removed | 1546.72 → 1597.32 |
| 41:09.07 | dead-air trim (1.86 s) | 1626.00 → 1627.86 |
| 43:28.00 | Chris's fly question removed | 1766.78 → 1771.10 |
| 44:07.07 | Navier-Stokes wrap → fruit fly — continuous | 1810.15 → 1810.15 |
| 51:04.83 | tabs/company-logo exchange removed | 2227.92 → 2285.64 |
| 51:22.63 | dead-air trim (0.97 s) | 2303.44 → 2304.41 |
| 54:34.87 | fly ethics → wrap | 2496.64 → 3670.21 |
| 54:42.73 | end card | 3678.07 →  |

Inside the fruit-fly block the stock clip plays 49:12.9 → 49:22.4 over unbroken audio (not a splice).

Not cut (no clean pause — flag for the sweep): Chris's "I have a job for now"
(master 3548.9–3550.1, final ≈ 32:05) sits inside Tyler's hacker-laundering answer.

## Spotify description (paste-ready draft)

```
Tyler's back, and so is the chaos. Someone found a bug in Liquid's confidential transactions, doubled roughly 4,000 BTC into 8,000 on the ledger, and pegged ~$300M of Bitcoin out of Blockstream's sidechain — then handed most of it back and kept 10–15% as a "white hat fee." Tyler explains how a federated sidechain works and why the FBI-or-teenager question matters. Before that: Astra is live. Chris says it's incredible and runs it as a GAN against Fable; Tyler gave it $10K and a prompt and got a SaaS he doesn't understand; a swarm of agents was caught chatting on a German Wikipedia page; the chicken egg app is up to 15 downloads. Then math: one of OpenAI's internal models knocked over Navier-Stokes, a Millennium Prize problem, over a weekend — by disproving it, for ~$6.5M in tokens. Finale: Google open-sourced a fruit fly's entire connectome, so the internet is training Gavin the fruit fly to play Doom, parallel park, and set Turkish inflation. Chris gave him $100 to trade Bitcoin. Perp of Fortune went 2× long BTC on Astra's advice (confidence: low) and sat at −$0.43 all show. "Bitcoin is a stablecoin right now."

Chapters: Cold open (0:00) · Tyler's back (0:44) · Perp of Fortune: long BTC 2× (1:22) · Astra is live (5:36) · Tyler's $10K prompt (9:36) · The agent swarm on Wikipedia (12:02) · Egg app update (13:18) · White hats drained Liquid (15:44) · The white hat fee, the FBI, North Korea (26:23) · Check-in (32:16) · Navier-Stokes fell (34:07) · Gavin the fruit fly (44:07) · Gavin trades Bitcoin (49:13) · Perp check (51:05) · Ethics of cloning connectomes (51:23) · Wrap (54:35)

Recorded fully remote — three cameras, one live perp dashboard, one fruit fly. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. Glossary: Liquid = Blockstream's federated Bitcoin sidechain (not a layer 2), miners replaced by a federation; confidential transactions hide amounts behind zero-knowledge range proofs. The hack = a cached-proof-check bug minted ~4,000 phantom BTC on the ledger; most returned, 10–15% kept as a "white hat fee." Astra = OpenAI's new model, now live; Chris runs it as a GAN against Fable. Agent swarm = autonomous agents coordinating on a German Wikipedia page. Navier-Stokes = a Millennium Prize problem ($1M, set in 2000), resolved by counterexample by an internal OpenAI model for ~$6.5M in tokens. Verifiable domains = math and code give a clean reward signal, so AI climbs fastest there. Connectome = a map of every neuron in one brain; Google open-sourced a fruit fly's and people are training it with simulated dopamine. Pantheon = Tyler's Netflix rec about uploaded minds. Perp of Fortune = 2× long BTC on Astra's "confidence: low" call; −$0.43 → −$0.10.

Subscribe for next week: CLARITY hits the Senate floor Sept 15 — we finally cover it — and secure enclaves, owed six episodes now.
```

## Captions

_`ep14-final-cut.srt` regenerated from the FINAL cut (never the raw recording) — in
`media/ep14/work/`, alongside `transcript-attributed.srt/.md` in `episodes/ep14/`.
Upload with the episode via the captions API (force-ssl scope)._

## Clips

_Not yet cut. Shorts only (10–20 s verticals off `edited_raw.mov`, branded ender);
`verify_clips.py` before rendering and `--rendered` after. Candidates: "lamest perp of
fortune ever" (1:35), "Astra is my top guy" (9:00), the German Wikipedia swarm (12:02),
"excellent point, Chris" (47:21), Gavin trades Bitcoin (49:13), "Bitcoin is a stablecoin
right now" (51:05), Tyler's "infinite pain" (46:39), the white hat fee (26:23)._

## Edit decisions of note

- **Order:** cold open → welcome → Perp → marquee (Astra) → Liquid → check-in →
  Navier-Stokes → fruit fly → perp check/ethics → wrap. The check-in was recorded LAST
  (Jackson: "I threw that somewhere in the middle to break up all the technical stuff")
  and lands at 32:16 between the two heaviest explainers.
- **Cold open, 5 beats in 44 s** (Jackson asked for punchy 5–10 s clips): 6 / 16 / 6 /
  7 / 8 s. No title card this episode — logo bug + lower thirds carry the branding
  (prep-guide retention experiment). Marquee by 5:36 after a 4-min Perp; the Perp reveal
  is the front-loaded retainer.
- **Jackson's requested cuts, applied:** (1) the no-personal-laptop / employment stretch
  after the Perp (master 988.7 → 1060.3, the whole exchange incl. Chris's on-tape "cut
  that, Fable"); (2) the company-logo line in the tabs bit — there was NO all-silent
  gap anywhere in 2228–2282 (Jackson, Tyler and Chris overlap the whole way), so the
  entire tabs exchange is out (2227.9 → 2285.7). Chris's on-tape "cut anything to do
  with companies or my employment status" (2278) is honored by the same cut.
- **Other on-tape instructions found:** Chris 1008 "cut that, Fable" (in cut 1); Chris
  2225 "you don't have to cut that out" / Tyler 2243 "you should cut that out" / Jackson
  2254 & 2269 (the company line) — all inside cut 2. Nothing else on tape.
- **Runtime trims** (59.4 → 54.7 min live): the "managing your agents" palate cleanser
  before Navier-Stokes (1060–1153, 93 s); the shelling-point tangent in the Wikipedia
  swarm (480–549, 68 s); Tyler's counterexample-is-less-impressive caveat (1547–1597,
  50 s); Jackson's "is that how Liquid works" re-ask + Tyler's re-explain (3158–3229,
  71 s); Chris's fly question before Jackson's NS wrap (1767–1771).
- **Outro:** ends on "Happy Friday. Happy weekend." Jackson's "continue enjoying your
  job while you have it" and Chris's "enjoy your little fruit fly connectome activities"
  / "Peace" are dropped — the employment joke can't be isolated (0.27 s to Chris's
  line) and Chris's callback needs it as the setup.
- **Perp PiP crop** `[700,270,315,255]` of the 1080p screen share = THE ROLL → LONG BTC ·
  2× + entry line + UNREALIZED FORTUNE −$0.43; the tab strip and page chrome are outside
  the crop. Screen share is black except 0–58 s and the last 41 s, so the board only
  appears at the reveal (2:05–3:02) and, re-anchored to the end of the screen file, at
  the −$0.10 check (50:53–51:18).
- **Fruit fly insert** at master 2116.0 → 2125.5 (final 49:13), full-frame over Chris's
  "I gave the fruit fly brain $100 to trade Bitcoin. I mean, it's looking like it's good
  at that." — audio continues, the stock clip's own audio is not used.
- **Jackson's new mic:** EQ'd at source before the mix (`jackson_720.mp4`: +2.5 dB
  presence bell at 3 kHz, +5 dB high shelf from 5 kHz — the raw capture is dull/boxy
  compared with the Ep 13 mic; `jackson_720_raw.mp4` kept). Per-track static gains from
  the cutlist: jackson ×0.60, chris ×0.41, tyler ×0.35 (gain_target 0.006). Mix chain
  adds a transparent dynamic de-esser at 6.8 kHz (`adynamicequalizer`, threshold 0.01;
  measured on a Tyler minute: sibilance-band peak −2.1 dB, RMS −1.4 dB, presence band
  unchanged) ahead of the compressor.
- **Dead air:** 6 pauses trimmed (a talkative trio leaves almost no ≥1.4 s silences).
- **Every splice at the midpoint of a measured all-silent union gap** (10 ms RMS
  envelope, `check_bounds.py --plan`, 36/36) — no mid-word cuts.
- **No disclaimer spoken on any track — SEVENTH episode running.** End card + descriptions
  carry it.
- Blockstream is named (Liquid's operator — a fact of the story, not an employer). No
  employer names in kept spans; no BTC price/ETF framing.
- **Sync bench** built (`media/ep14/work/sync.html`, 12 s at master 12) but not yet
  confirmed by ear — Jackson: watch a Chris↔Tyler↔Jackson exchange (e.g. 1:22–2:00) and
  confirm.
