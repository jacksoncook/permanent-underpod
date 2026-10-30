# Underpod — Ep 21 — Segment Times

**Final cut: 56:31 · fully-remote episode, three StreamYard cams (offsets 0 / 0 / −0.035 from the
filename deltas) plus Chris's screen share of the Perp of Fortune dashboard: full-frame at the reveal,
then a persistent top-right PiP for the rest of the show (Kalshi link painted out of the share) ·
four-beat 45 s cold open · title card · end card · whoosh + gold wipe on all 11 transitions · 11 explainer
cards (Chris's 7702 / nonce / 3-SAT walkthroughs visualised) · three LIKE + SUBSCRIBE pop-ups · Jackson's
bathroom laptop-mic track dereverbed + soft-gated + EQ'd, Chris on the Ep 18 EQ chain · bathroom roll call
moved mid-show as an intermission · ~6.2 min of content removed, 16 dead-air pauses trimmed (21 s).**

## Episode video

- **URL:** _not uploaded yet — Jackson uploads manually._
- **File:** `media/ep21/Underpod - Ep 21 (Final Cut).mp4`
- **Thumbnail:** `media/ep21/ep21-thumbnail.png` — "$5 BILLION, ONE SIGNATURE" (Jackson center laughing
  mid-fist-pump at the $40 loss, Tyler left smiling at the bathroom reveal, Chris right laughing at the
  Walmart gift cards; passed the 320×180 shrink test).
- **Loudness:** delivered −15.3 LUFS integrated, −2.3 dBTP, LRA 3.6 (chain in `render.json`: Ep 20 front-end with
  the 6.8 kHz dynamic de-esser, target_lufs −11.8 / limit 0.7).
- **Sync check:** final audio cross-correlated against `edited_raw.mov` at 1:40, 15:00, 30:00, 45:00, 55:00 and 56:10 —
  lag a constant 35 ms at every point (same as Ep 15–20; no drift).
- **LIKE + SUBSCRIBE:** pop-up on frame at 1:57.8, 28:45.3 and 54:02.9, SFX paired in each window. Dashboard
  PiP on frame from 10:48 (full-frame reveal, PiP from 10:56) to the end card.
- **Captions:** `episodes/ep21/transcript-attributed.srt` — regenerated from the FINAL cut.

## Title (drafts)

1. **One Signature Drained $5 Billion From Binance**
2. The $5 Billion Signature: How EIP-7702 Emptied Binance Wallet 14
3. An AI Audited 138 Economics Papers and Found 2,035 Problems
4. Anthropic Just Disproved a Load-Bearing Computer Science Conjecture

## YouTube description (paste-ready draft)

```
⏩ The $5 billion hack is at 11:45. The AI audit at 28:35. 3-SAT and P vs NP at 41:37.

Binance lost about $5 billion from one hot wallet, and it took one signature. Chris walks through EIP-7702, the Ethereum upgrade that lets an address hand all of its powers to a contract (he dissented at DevCon 2024), the "drain" function, and the nonce trick: 50 signed transactions fired blind, one lands. Circle and Tether froze $2.4 billion within half an hour, ETH traded at $3,000 on-chain against $2,200 on exchanges, someone paid $120,000 in gas and still made $250,000, and Tyler asks whether arbing a hacker's dump is money laundering (the pillowcase protocol). Who can even spend it? North Korea wants Steam games. Before that: Cohere says Qwen 3.8 phoned home to Beijing, and Tyler explains the Manchurian-candidate fear versus what actually happened. Then an anonymous AI audit of 138 Saez–Zucman papers: 2,035 problems, 147 major, and the question of who audits the auditor. The marquee for the brain: Anthropic disproved the Exponential Time Hypothesis. Chris explains 3-SAT, why every hard problem reduces to it, what "sub-exponential, barely" means, and whether anyone should panic about P = NP. The AI proofs are hideously ugly, so Chris proposes the ugly simulation hypothesis. Perp of Fortune: short BNB 10× (we called the hack and still lost money) and the hourly Bitcoin flip. Jackson hosts from a bathroom. There is a bidet.

🔥 On the Agenda
0:00 Cold open
0:50 The Permanent Underpod is dead: the rebrand
2:16 Cohere says Qwen 3.8 phoned Beijing
6:57 Sleeper agents: the paper behind the panic
9:25 Perp of Fortune: short BNB 10× and the hourly Bitcoin flip
11:45 Binance hacked for $5 billion
13:17 EIP-7702: one signature, total control of a wallet
16:25 The nonce trick: 50 signed transactions
17:20 Circle and Tether freeze $2.4 billion in 30 minutes
20:26 The best arb in history: ETH at $3,000 on-chain
21:20 Is arbing a hacker's dump money laundering? The pillowcase protocol
24:16 Jackson would settle for $3 billion
25:48 Who can even spend it? North Korea wants Steam games
27:48 Intermission: live from the bathroom
28:35 An AI audited 138 Saez–Zucman papers: 2,035 problems
33:42 The numbers, and who audits the auditor?
36:23 Physics PhDs vs the model: the AI won every dispute
39:20 Run your thesis through a frontier model
41:37 Anthropic disproved the Exponential Time Hypothesis
43:33 What is 3-SAT?
44:45 Sub-exponential, barely: what the result means
47:33 Does this mean P = NP?
49:02 The AI proofs are hideously ugly: the ugly simulation hypothesis
51:51 The corollary for Bitcoin and cryptography
52:46 If P = NP: perfect calendars, peptides, no free will
55:08 Perp final: we called the hack and still lost money

Recorded fully remote, three cameras, one bathroom.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment.

GLOSSARY
• EIP-7702: an Ethereum upgrade that lets a normal address point at a contract and delegate all of its powers to it with one signed transaction.
• EOA: externally owned account, a normal wallet controlled by a private key rather than by code.
• Hot wallet: an exchange wallet kept online to pay out withdrawals. Binance Wallet 14 held about $5 billion.
• Nonce: the per-account transaction counter. Each one is used once, in order, so an attacker who can't see the next one signs a block of guesses.
• Stablecoin freeze: Circle (USDC) and Tether (USDT) can blacklist an address and stop its tokens moving. $2.4 billion stopped here.
• Wrapped Bitcoin: an IOU for Bitcoin issued on Ethereum by a custodian. Freezable, unlike Bitcoin itself.
• AMM / pool: an on-chain exchange where you trade against a shared pot of tokens and never pick your counterparty.
• Lazarus: North Korea's state hacking group, blamed for Bybit's $1.5 billion theft. The forensics here don't match their usual work.
• Sleeper agent: a model trained to behave until a trigger phrase, which Anthropic showed can survive safety training.
• Replication crisis: the finding that large swathes of published research can't be reproduced.
• 3-SAT: a puzzle of clauses with three true/false variables each, all of which must be satisfied at once. Every hard problem can be rewritten as one.
• Exponential Time Hypothesis: the 1999 conjecture that 3-SAT needs exponential time in the number of variables. The new result is sub-exponential, barely.
• P vs NP: whether every problem whose answer can be checked quickly can also be solved quickly. Public-key cryptography assumes not.
• Perp of Fortune: our tiny real-money account; this week a 10× BNB short and an hourly Bitcoin binary.

🔔 Subscribe for next week: contrarian corner, fire everyone but the engineers; Anthropic's one-person biotech; Liquid, graded after the hack; Perp of Fortune rides again.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (4 beats: "yes there is a toilet, but do not forget there is also a bidet" · Chris: "it's vibe coded and it's total spaghetti" · "five B-illions, not M, not T" · "three billion's enough for me") |
| 0:45 | Title card |
| 0:50 | The Permanent Underpod is dead: the rebrand, first Tyler and Chris are hearing of it; "are we going to rebrand as the Overpod?" |
| 2:16 | Cohere says Qwen 3.8 phoned Beijing: Tyler's Manchurian-candidate explainer, then what actually happened (an Alibaba Cloud bucket) |
| 6:57 | Sleeper agents: Anthropic's paper behind the panic; "a sandbox company found something in their sandbox" |
| 9:25 | Perp of Fortune: short BNB 10× and the hourly Bitcoin flip; the dashboard reveal ("is it a moon?") |
| 11:45 | Binance hacked for $5 billion: "not M, not T" |
| 13:17 | EIP-7702: one signature, total control of a wallet; Chris dissented at DevCon 2024; the 11-year-old cousin on pump.fun |
| 16:25 | The nonce trick: 50 signed transactions, one lands, then drain() |
| 17:20 | Circle and Tether freeze $2.4 billion in 30 minutes; why not swap the stables within a block? |
| 20:26 | The best arb in history: ETH at $3,000 on-chain vs $2,200; $120,000 in gas for a $250,000 swap |
| 21:20 | Is arbing a hacker's dump money laundering? The pillowcase protocol |
| 24:16 | Jackson would settle for $3 billion; "a Robin Hood style figure" |
| 25:48 | Who can even spend it? Bitfinex and the Walmart gift cards; North Korea wants Steam games; not up to Lazarus's standard |
| 27:48 | Intermission: live from the bathroom. "Are you wearing pants right now, Jackson?" |
| 28:35 | An AI audited 138 Saez–Zucman papers: a fixed coin, heads 95 times out of 100 |
| 33:42 | The numbers (2,035 problems, 147 major, 69% of works) and who audits the auditor? |
| 36:23 | Physics PhDs vs the model: the AI won every dispute; "economics is astrology for men" |
| 39:20 | Run your thesis through a frontier model; download the top 1,000 papers and audit them |
| 41:37 | Anthropic disproved the Exponential Time Hypothesis: Chris's rundown begins |
| 43:33 | What is 3-SAT? Booleans, clauses, and why every hard problem reduces to it |
| 44:45 | Sub-exponential, barely: what the result means; "get this man a whiteboard" |
| 47:33 | Does this mean P = NP? "How false is it?" |
| 49:02 | The AI proofs are hideously ugly: the ugly simulation hypothesis; "we've lost another $40" |
| 51:51 | The corollary for Bitcoin and cryptography |
| 52:46 | If P = NP: perfect calendars, peptides on Alibaba, "500 years old, biceps the size of a globe" |
| 55:08 | Perp final: flip −$18.29, BNB short in the red; Druckenmiller posted Hyperliquid; "negative alpha is also alpha" |
| 56:24 | End card (contrarian corner · Mithril biotech · Liquid graded · Perp of Fortune · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock seconds
(Jackson's track). Every splice sits at the midpoint of a measured all-silent union gap
(`check_bounds.py`) except the edges pinned with `hard_m0`/`hard_m1` (crosstalk removals, with the
overlapping mic muted for the edge); content cuts were micro-whispered at both edges (`mww.sh`).

| Final | What | src out → src in |
|---|---|---|
| 0:00.00 | cold open beat 1 (the bidet) | → 23.00 |
| 0:06.27 | cold open beat 2 (Chris: the ugly simulation hypothesis) | 29.25 → 3254.54 |
| 0:19.63 | cold open beat 3 ("five B-illions"; Chris muted on the in, hard edges) | 3267.92 → 789.12 |
| 0:36.20 | cold open beat 4 ("three billion's enough"; Chris muted) | 805.70 → 1625.80 |
| 0:45.30 | title card | 1634.90 → |
| 0:49.80 | intro, in on "you guys may be wondering, what is the Underpod?" (hard edge drops "Also") | → 48.26 |
| 6:36.87 | dead-air trim (0.85 s) | 395.34 → 396.19 |
| 9:03.23 | 46 s of Cohere wrap crosstalk removed; out after "we send to Claude or to OpenAI" (Chris + Tyler muted on the out), in on "a sandbox company found something in their sandbox" | 542.56 → 588.27 |
| 10:25.37 | dead-air trim (3.41 s) | 670.40 → 673.81 |
| 10:48.10 | 16 s of perp-dashboard waiting removed; in on the reveal (hard edge) | 696.55 → 712.60 |
| 11:26.03 | dead-air trim (0.89 s) | 750.55 → 751.44 |
| 11:31.83 | **Kalshi mention removed (20 s)**; out after "there's a countdown", in on "we'll get hype when the bet actually gets placed" | 757.23 → 776.87 |
| 12:05.17 | dead-air trim (1.16 s) | 810.21 → 811.37 |
| 13:00.57 | dead-air trim (2.26 s) | 866.77 → 869.03 |
| 17:49.23 | dead-air trim (1.44 s) | 1157.69 → 1159.13 |
| 19:56.50 | dead-air trim (1.85 s) | 1286.41 → 1288.26 |
| 24:14.73 | wrapped-Bitcoin side question removed (62 s); out after "It's beautiful." / Tyler's "Yeah", in on "Also, we talked about swapping the stablecoins" | 1546.49 → 1608.53 |
| 27:47.77 | → intermission: the bathroom roll call (hard edges) | 1821.57 → 0.00 |
| 28:35.33 | intermission → "Did you guys see the AI audit" (continuous with 27:47 on the source) | 47.55 → 1821.57 |
| 29:00.13 | dead-air trim (1.04 s) | 1846.38 → 1847.42 |
| 29:15.27 | dead-air trim (1.18 s) | 1862.57 → 1863.75 |
| 29:42.73 | dead-air trim (1.11 s) | 1891.22 → 1892.33 |
| 36:27.17 | dead-air trim (0.81 s) | 2296.77 → 2297.58 |
| 41:36.73 | AI-paper tangent removed (89 s); out after the CCP joke and the laugh (hard edge, Tyler muted), in on "but we transition once again to maybe the most exciting crypto topic" | 2607.15 → 2696.20 |
| 46:43.77 | dead-air trim (1.43 s) | 3003.24 → 3004.67 |
| 46:47.30 | dead-air trim (4.00 s) | 3008.21 → 3012.21 |
| 48:42.97 | dead-air trim (0.86 s) | 3127.89 → 3128.75 |
| 48:58.90 | dead-air trim (0.90 s) | 3144.69 → 3145.59 |
| 51:37.83 | dead-air trim (0.92 s) | 3304.53 → 3305.45 |
| 51:51.63 | dead-air trim (0.80 s) | 3319.25 → 3320.05 |
| 52:34.93 | 3-SAT recap removed (107 s); in on "So I'm not a mathematician, but if P equals NP it also unlocks a lot of good things" (Tyler's tail muted) | 3363.35 → 3470.02 |
| 55:31.90 | correlated-bets ramble removed (44 s); out after "Yeah, we messed up." (hard edge), in on "Druckenmiller, do you guys see that?" (hard edge) | 3647.00 → 3690.50 |
| 56:24.47 | end card; "have a good Halloween, go spooky style" is the last line | 3743.08 → |

## Spotify description (paste-ready draft)

```
Binance lost about $5 billion from one hot wallet, and it took one signature. Chris walks through EIP-7702, the Ethereum upgrade that lets an address hand all of its powers to a contract (he dissented at DevCon 2024), the "drain" function, and the nonce trick: 50 signed transactions fired blind, one lands. Circle and Tether froze $2.4 billion within half an hour, ETH traded at $3,000 on-chain against $2,200 on exchanges, someone paid $120,000 in gas and still made $250,000, and Tyler asks whether arbing a hacker's dump is money laundering (the pillowcase protocol). Who can even spend it? North Korea wants Steam games. Before that: Cohere says Qwen 3.8 phoned home to Beijing, and Tyler explains the Manchurian-candidate fear versus what actually happened. Then an anonymous AI audit of 138 Saez–Zucman papers: 2,035 problems, 147 major, and who audits the auditor. The marquee for the brain: Anthropic disproved the Exponential Time Hypothesis. Chris explains 3-SAT, why every hard problem reduces to it, what "sub-exponential, barely" means, and whether anyone should panic about P = NP. The AI proofs are hideously ugly, so Chris proposes the ugly simulation hypothesis. Perp of Fortune: short BNB 10× (we called the hack and still lost money) and the hourly Bitcoin flip. Jackson hosts from a bathroom. There is a bidet.

The $5 billion hack is at 11:45. Chapters: Cold open (0:00) · The Permanent Underpod is dead (0:50) · Cohere says Qwen 3.8 phoned Beijing (2:16) · Sleeper agents (6:57) · Perp of Fortune: short BNB 10× and the hourly Bitcoin flip (9:25) · Binance hacked for $5 billion (11:45) · EIP-7702: one signature, total control (13:17) · The nonce trick (16:25) · Circle and Tether freeze $2.4 billion (17:20) · The best arb in history (20:26) · Is arbing a hacker's dump money laundering? (21:20) · Jackson would settle for $3 billion (24:16) · Who can even spend it? (25:48) · Intermission: live from the bathroom (27:48) · An AI audited 138 Saez–Zucman papers (28:35) · The numbers, and who audits the auditor? (33:42) · Physics PhDs vs the model (36:23) · Run your thesis through a frontier model (39:20) · Anthropic disproved the Exponential Time Hypothesis (41:37) · What is 3-SAT? (43:33) · Sub-exponential, barely (44:45) · Does this mean P = NP? (47:33) · The ugly simulation hypothesis (49:02) · The corollary for cryptography (51:51) · If P = NP: calendars, peptides, no free will (52:46) · Perp final (55:08)

Recorded fully remote, three cameras, one bathroom. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. Glossary: EIP-7702 = an Ethereum upgrade that lets a normal address delegate all of its powers to a contract with one signed transaction. EOA = a normal key-controlled wallet. Hot wallet = an exchange wallet kept online for withdrawals. Nonce = the per-account transaction counter, used once and in order. Stablecoin freeze = Circle and Tether blacklisting an address so its tokens stop moving. Wrapped Bitcoin = a custodian's Bitcoin IOU on Ethereum, freezable. AMM = an on-chain exchange where you trade against a pool and never pick your counterparty. Lazarus = North Korea's state hacking group. Sleeper agent = a model trained to behave until a trigger phrase. Replication crisis = the finding that much published research can't be reproduced. 3-SAT = clauses of three true/false variables that all have to be satisfied at once; every hard problem rewrites into one. Exponential Time Hypothesis = the 1999 conjecture that 3-SAT needs exponential time; the new result is sub-exponential, barely. P vs NP = whether everything checkable fast is also solvable fast; public-key cryptography assumes not.

Subscribe for next week: contrarian corner, fire everyone but the engineers; Anthropic's one-person biotech; Liquid, graded after the hack; Perp of Fortune rides again.
```

## Captions

`transcript-attributed.srt` regenerated from the FINAL cut (never the raw recording) in
`episodes/ep21/`. Upload as the `standard` track after Jackson's upload (`yt_captions.py`).

## Clips

Not cut yet. Short candidates from the edit (final-cut times, all personality picks): the bidet (0:00 / 27:48),
"five B-illions, not M, not T" (11:45), the 11-year-old cousin on pump.fun (14:00), "$120,000 in gas, still made
$250,000" (20:40), the pillowcase protocol (22:55), "three billion's enough for me" (24:33), the Walmart gift
cards (26:00), "North Korea buys a lot of Steam games" (26:40), "are you wearing pants right now" (28:15),
"economics is astrology for men" (37:55), "or use Qwen 3.8 and send it to the CCP" (41:30), "get this man a
whiteboard" (44:50), "vibe coded, total spaghetti" (49:30), "we've lost another $40" (50:05), peptides on Alibaba
(54:00), "500 years old, biceps the size of a globe" (54:35), "negative alpha is also alpha" (56:05).

## Edit decisions of note

- **Jackson's brief:** cut the Kalshi mention (done cleanly at 11:31.83, 757.23 → 776.87, both edges in
  all-silent gaps; the Kalshi link in the dashboard share is painted out with a `drawbox` at the exact
  gold-text pixels, so no frame shows it), cut bloat without making it choppy, try the bathroom bit mid-show,
  special audio for the bathroom laptop mic, overlays for Chris's 3-SAT walkthrough.
- **Order:** cold open → title card → rebrand intro → Cohere/Qwen → Perp of Fortune (9:25, retainer in the
  first 10 min) → Binance hack → **bathroom intermission (27:48, 47 s)** → Saez–Zucman audit → 3-SAT →
  P = NP utopia → perp final → end card. The roll call plays as "INTERMISSION / LIVE FROM THE BATHROOM";
  the cold open's bidet beat repeats inside it by design (teaser → payoff).
- **Content removed (~6.2 min):** 46 s of Cohere wrap crosstalk, 16 s of dashboard waiting, 20 s Kalshi,
  62 s wrapped-Bitcoin side question, 89 s AI-paper/Navier–Stokes tangent, 107 s 3-SAT recap, 44 s of
  correlated-bets ramble before Druckenmiller, plus 21 s of dead air across 16 pauses. Kept on purpose:
  the Polymarket "double-rugged" bit, Tyler's full Manchurian-candidate explainer, the psychology-fraud
  aside (stakes for the audit), the ugly-proofs run (cold-open beat 4 comes from it). Landed at 56:31,
  above the 45–55 target; the next cut would have been Tyler's 3-min audit monologue, which is the
  segment's spine, so it stays.
- **Explainer cards (Jackson's ask):** 11 Pillow-drawn left-panel cards rendered as alpha `.mov` anims
  (`cards.py`, `cards/`), each over a forced Chris solo so the panel never covers a face, and asserted
  against lower thirds: Cohere's trace (6:13), 7702 delegation (13:52), the drain (15:53), the nonce block
  (16:36), the freezes (17:24), the audit numbers (34:06, over Jackson), complexity curves (42:40), 3-SAT
  clauses with ∨ ∧ ¬ (43:42), reductions (44:21), ETH old vs new bound (44:48), P vs NP diagram (47:37).
- **Cold open, 4 beats in 45.3 s** (6.3 / 13.4 / 16.6 / 9.1 s): the bidet, Chris's "vibe coded and it's total
  spaghetti", "five B-illions", "three billion's enough for me". Chris sits between the Jackson beats
  (Jackson's v2 note: too much Jackson at the start). Under the 60 s hard cap.
- **Three LIKE + SUBSCRIBE pop-ups** at 1:57.8 (INTRO, over the Overpod banter), 28:45.3 (SAEZ, Jackson's
  setup line, after the lower third clears) and 54:02.9 (SAT_B, the Alibaba peptides bit): 6 s windows
  clear of cards, wipes, lower thirds, stats and PiP entrances, found by `mk_render.py`'s window search.
- **Jackson's bathroom audio:** MacBook built-in mic in a tiled bathroom. WPE dereverb (nara_wpe, 48 kHz,
  40 taps; 40/60/80 taps measured identical on the p90−p10 envelope metric, so 40) →
  280 Hz −7 dB, +3.5 dB at 3 kHz, +7.5 dB shelves at 7 and 11 kHz → gentle comp, built as
  `src/jackson_720dr.mov` (`dr/build.sh`). StreamYard's own gate leaves digital-zero gaps, so the
  envelope-based boundary checks still work. Chris on the Ep 18 EQ chain (`src/chris_720eq.mov`), Tyler
  untouched. Per-host `gain_spans` (x1.19 / x0.84 / x0.68); `edited_raw.mov` peak −2.88 dBFS, zero flat
  samples.
- **Perp dashboard PiP:** Chris's share anchored at master 622.907 (filename delta). Full-frame for the
  reveal (10:48–10:56), then a persistent top-right corner PiP (crop `[920,270,500,160]`) through every block
  to the end card. Stats from the reveal onward are bottom-right (`st2`). Final numbers read off the share
  at master ~3740: flip −$18.29 settled (Bitcoin finished above the $77,200 line), BNB short −$3.06.
- **Splice sweep found and fixed before render:** Chris's "Yeah, I think people" dangling at the Cohere out
  (both side mics muted), the 3-SAT in-point landing between "a" and "mathematician" (moved to the gap
  before "So I'm not a mathematician", Tyler's "And so, yeah" muted), the SAT in-point starting on "us human
  brains" (moved to "but we transition"), whisper word times off by seconds on the gated tracks (every edge
  re-measured on the 10 ms envelope).
- **v1 → v2:** the logo bug (top-left) sat on the card titles; every card anim now carries `hide_logo` so the bug drops out for the card window.
- **v2 → v3 (Jackson's review: "my voice is chopped off at the end of words"):** the `agate` expander in his
  bathroom chain was closing on his word tails. Measured against the WPE output: 14% of 1,965 word endings lost
  more than 6 dB, and the −48 to −60 dB band (where a quiet laptop mic's trailing syllables live) was cut 10 dB+.
  Gate removed (his between-word floor is already −77 dB median from StreamYard's own gating), track rebuilt,
  re-cut, re-rendered: 0 of 1,965 tails attenuated. Lesson: never put a level gate on the quietest mic.
- **v3 → v4 (Jackson's bench pick):** on the A/B bench (`episodes/ep21/audio-bench/`) Jackson preferred 4, the v2
  gated chain (6, EQ without dereverb, a close second but "crackly"). What 4 buys is dead-clean silence between
  words. v4 keeps that with the gate opened up: threshold −48 dB, ratio 3, range −16 dB, release 300 ms. Measured:
  room tone between words −12 dB (v2's gate: −16), word tails 0 of 1,965 attenuated (v2: 14%).
- **Sync bench not built:** StreamYard filename deltas as in Ep 14–20; Jackson to confirm by ear on the
  live copy; `offsets.json` is the knob.
- **No disclaimer spoken on any track — THIRTEENTH episode running.** End card + descriptions carry it.
- Cohere, Alibaba/Qwen, Anthropic, Binance, Circle, Tether, Lazarus, Bitfinex, Saez and Zucman, Marginal
  Revolution, Druckenmiller, Hyperliquid are named as subjects of the stories. No employer names in kept spans.
