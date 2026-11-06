# Underpod — Ep 22 — Segment Times

**Final cut: 59:09 · fully-remote episode, three StreamYard cams (offsets 0 / −0.079 / −0.079 from the
filename deltas, validated by turn-gap medians) plus Chris's screen share of the Perp of Fortune dashboard:
full-frame at the reveal, then a persistent top-right PiP for the rest of the show · four-beat 42 s cold open
that opens on the evil-Qwen sandwich · title card · end card · whoosh + gold wipe on all 8 transitions ·
22 stat callouts (incl. the non-copyrighted Bart head Jackson asked the editor for on air) · 12 lower thirds ·
three LIKE + SUBSCRIBE pop-ups · Jackson back on the good mic (light EQ only, no dereverb/gate), Chris on
the Ep 18 EQ chain · recorded order kept (Jackson's note) · one content cut (Tyler's "we're cutting this",
24.9 s) · 31 dead-air pauses trimmed (36 s).**

## Episode video

- **URL:** (Jackson's manual upload; backfill from `yt_fetch.py` after it goes live)
- **File:** `media/ep22/Underpod - Ep 22 (Final Cut).mp4`
- **Thumbnail:** `media/ep22/ep22-thumbnail.png` — "ONE BANK. 60% OF A COUNTRY." (Jackson center at
  "That's terrible", Tyler left mid-eyebrow-raise at the no-Bitcoin-flip reveal, Chris right at the Bart
  explainer; passed the 320×180 shrink test).
- **Loudness:** delivered −15.6 LUFS integrated, −2.6 dBTP, LRA 4.1 (chain in `render.json`: the Ep 21 chain, target_lufs −11.8 / limit 0.7).
  A/V durations 3549.47 / 3549.45 s.
- **Sync check:** final audio cross-correlated against `edited_raw.mov` at 1:40, 30:00, 51:07 and 58:55 — lag a constant 35 ms at every point (same as Ep 15–21; no drift).
- **LIKE + SUBSCRIBE:** pop-up on frame at 1:46.0, 29:27.8 and 56:39.3, SFX paired in each window. Dashboard
  PiP on frame from 24:38 (full-frame reveal, PiP from 24:46) to the end card.
- **Captions:** `episodes/ep22/transcript-attributed.srt` — regenerated from the FINAL cut.
- **Runtime flag:** 59:09 is over the 45–55 min target and the Perp retainer lands at 24:04, not inside the
  first 10 min. Both follow from keeping the recorded order; Jackson's call whether to reorder a v2.

## Title (drafts)

1. **One Bank Froze 60% of a Country's Money**
2. Paraguay's Biggest Bank Just Froze Everyone's Money
3. An AI Did Brain Surgery on Another AI (It Went Evil)
4. TikTok Runs a Neural Net on Your Face. Here's What It Scores.

## YouTube description (paste-ready draft)

```
⏩ The bank freeze is at 2:01. LLM neurosurgery at 9:23. The evil sandwich at 14:52. TikTok scoring your face at 18:59. Fire everyone but the engineers at 42:03.

Sixty percent of Paraguay's adults banked at Ueno, and this week Ueno froze. $800 million of public money inside, the pension fund, the hydro-dam operator, and a president who resigned on the spot. Chris and Tyler on why a country lets one bank get that big, why Australia's four banks could do the same, and why this is a Bitcoin story on every level. Then the brain stuff: frontier models are now doing neurosurgery on smaller models, editing weights by hand in a 20,000-parameter Qwen, and someone found the single neuron that turns Qwen murderous when you ask it for a sandwich. Tyler explains why mechanistic interpretability was given up for dead and why it might be back. Chris found the local CNN inside TikTok that scores your age, expression and attractiveness before anything leaves your phone (the Samsung TV callback). Perp of Fortune: long ZhiPu 10×, no Bitcoin flip this week (Chris dropped the coin), and the platonic Bart pattern, visualised. Chris has been living on GLM 5.3 Flash at 15 cents a million tokens and says it's better than Opus; it also filed his forms in Chinese. Jackson's Instinct booked seven things for his trip and he checked none of them. Proton Mail: Tyler calls it a fortress nobody else lives in. Contrarian corner: the Proton CEO stops hiring engineers, so Chris argues the opposite, long live the capital-E Engineer, and Tyler explains why the people who get 10× more productive stop being the bottleneck and get laid off anyway. Then Mithril, the one-person biotech Anthropic bought: a Goldman MBA running 11 contract labs through Claude. Tyler closes with a pitch for a cracked team of three.

🔥 On the Agenda
0:00 Cold open
0:47 Check-in: still holding our bags
2:01 Paraguay: 60% of a country banked at Ueno, and it froze
9:23 LLM neurosurgery: frontier models editing model weights by hand
14:52 Evil Qwen: one neuron, one murderous sandwich
18:59 TikTok's edge CNN scores your face
24:04 Perp of Fortune: long ZhiPu 10×, no Bitcoin flip, the platonic Bart
26:41 GLM 5.3 Flash: the free model that's "better than Opus"
35:06 Instinct update: seven bookings, zero checks, one bad hotel
38:02 Proton Mail: a fortress nobody else lives in
42:03 Contrarian corner: fire everyone but the engineers
50:09 Mithril: the one-person biotech Anthropic bought
56:18 Tyler's pitch: acquire this cracked team of three
58:42 Perp final + outro

Recorded fully remote, three cameras, one dashboard.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment.

GLOSSARY
• Ueno: Paraguay's largest neobank-style bank, placed into resolution this week with deposits frozen; roughly 60% of adults banked there.
• Solvency ratio: the capital a bank must hold against its loans; fall below it and the central bank steps in.
• Fractional reserve: banks lend out most deposits, so the money isn't there if everyone asks at once.
• Mechanistic interpretability: mapping what each neuron and circuit in a neural network does.
• Distillation: training a small model to copy a big one, either on its outputs or on its internal states (logits).
• Edge model / CNN: a small convolutional neural network that runs on your device and sends back summaries, not the raw video.
• ZhiPu (Z.ai): the Chinese lab behind the GLM models; this week's perp.
• GLM 5.3 Flash: ZhiPu's small open-weights model, about 15¢ per million tokens.
• Bart pattern: a chart that goes straight up, flat, then straight down; the silhouette of Bart Simpson's head.
• Instinct: the agent product that booked Jackson's trip.
• Aqua-hire: buying a company to get its people, not its product.
• Perp of Fortune: our tiny real-money account; this week a 10× long on ZhiPu, +$2.67 at the bell.

🔔 Subscribe for next week: the Bitcoin flip returns to Perp of Fortune, agentic commerce, and the layer-2 series continues.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (4 beats: Tyler's evil-Qwen sandwich · "thank you, Ueno" · "$204 million in biotech, off YouTube on a podcast" · "What's one million times a dollar? It's one million.") |
| 0:42 | Title card |
| 0:47 | Check-in: still holding our bags; "the lower the market goes the more money you got to throw into it"; the first spoken "not financial advice, personal opinions" in 14 episodes |
| 2:01 | Paraguay: 60% of adults banked at Ueno and it froze; $800M of public money; the president resigns; Australia's four banks; Dodd-Frank consolidation |
| 9:23 | LLM neurosurgery: Opus 5.5 / GPT-6 class models editing a 20,000-parameter Qwen by hand; distillation vs surgery |
| 14:52 | Evil Qwen: one neuron, one murderous sandwich; why mech interp was given up and why it's back |
| 18:59 | TikTok's edge CNN scores your face (age, expression, attractiveness); Samsung TV callback; the hotness-appropriate toaster |
| 24:04 | Perp of Fortune: long ZhiPu 10×, no Bitcoin flip ("I've dropped the coin"), Tyler's eyebrows (on screen before and during Jackson's call-out), the platonic Bart, visualised |
| 26:41 | GLM 5.3 Flash: Chris's free model at 15¢/M tokens, forms returned in Chinese, "better than Opus" |
| 35:06 | Instinct update: seven bookings, zero checks, one bad hotel; the punishment is butter at Aldi Spain |
| 38:02 | Proton Mail: "what do you get out of proton male that you don't get out of gene male"; the fortress nobody else lives in; "oh, you're a privacy guy" |
| 42:03 | Contrarian corner: the Proton CEO stops hiring engineers; Chris: long live the capital-E Engineer; Tyler's law of the bottleneck |
| 50:09 | Mithril: the one-person biotech Anthropic bought; 11 contract labs via Claude; 11 acquisitions averaging $204M; the aqua-hire meta |
| 56:18 | Tyler's pitch: acquire this cracked team of three, slightly bloated |
| 58:42 | Perp final (+$2.67) and outro; "Buy Bitcoin, no financial advice" / "Adios, amigos" (3.7 s of pauses pulled out of the closeout) |
| 59:02 | End card (Bitcoin flip returns · agentic commerce · layer-2 series · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock seconds
(Jackson's track). Every splice sits in a measured all-silent gap (`check_bounds.py`) except the edges pinned
with `hard_m0`/`hard_m1` (cold-open beats and the Instinct cut, micro-whispered at both edges).

| Final | What | src out → src in |
|---|---|---|
| 0:00.00 | cold open beat 1 (Tyler: evil Qwen makes a sandwich; hard edges) |  → 872.90 |
| 0:15.27 | cold open beat 2 (Jackson: "thank you, Ueno"; Tyler muted on the tail, hard out) | 888.15 → 257.64 |
| 0:26.13 | cold open beat 3 (Chris: "$204 million in biotech, off YouTube on a podcast"; Jackson's "people don't like robot us" muted) | 268.50 → 3184.46 |
| 0:37.67 | cold open beat 4 ("What's one million times a dollar? It's one million."; Chris + Tyler muted, hard edges) | 3195.98 → 3481.95 |
| 0:42.33 | title card | 3486.60 → |
| 0:46.83 | intro, in on "Good morning, good afternoon, and good evening" |  → 0.69 |
| 1:19.47 | dead-air trim (1.51 s) | 33.31 → 34.82 |
| 2:26.50 | dead-air trim (1.02 s) | 101.84 → 102.86 |
| 4:36.93 | dead-air trim (1.44 s) | 233.28 → 234.72 |
| 4:47.53 | dead-air trim (0.92 s) | 245.33 → 246.25 |
| 5:25.73 | dead-air trim (0.82 s) | 284.44 → 285.26 |
| 7:32.33 | dead-air trim (1.54 s) | 411.85 → 413.39 |
| 9:05.00 | dead-air trim (1.94 s) | 506.04 → 507.98 |
| 9:22.67 | Paraguay → LLM neurosurgery: out after "truly terrible", in on "But let's talk about something else now" | 525.66 → 527.77 |
| 9:57.60 | dead-air trim (0.97 s) | 562.71 → 563.68 |
| 11:11.73 | dead-air trim (1.02 s) | 637.82 → 638.84 |
| 11:35.50 | dead-air trim (0.99 s) | 662.60 → 663.59 |
| 18:47.57 | dead-air trim (1.01 s) | 1095.66 → 1096.67 |
| 21:46.40 | dead-air trim (1.01 s) | 1275.50 → 1276.51 |
| 24:04.30 | Norway shoutout → Perp of Fortune (block seam, no material removed; the dashboard share is anchored here) | 1414.41 → 1414.41 |
| 24:57.17 | dead-air trim (0.99 s) | 1467.28 → 1468.27 |
| 28:20.80 | dead-air trim (0.84 s) | 1671.89 → 1672.73 |
| 30:20.27 | dead-air trim (0.90 s) | 1792.21 → 1793.11 |
| 30:54.37 | dead-air trim (0.91 s) | 1827.20 → 1828.11 |
| 33:38.63 | dead-air trim (1.29 s) | 1992.39 → 1993.68 |
| 35:06.17 | GLM → Instinct update: in on "speaking of instinct maybe i can give an instinct update" | 2081.22 → 2083.40 |
| 36:44.87 | **THE CUT (24.9 s)**: out after "that Opus 4.5, 4.6 level of model" (hard edge mid-breath before "And Tyler, you seem to know..."), in on "Yeah, and that concludes the Instinct update" | 2182.10 → 2206.97 |
| 38:02.13 | dead-air trim (0.96 s) | 2284.24 → 2285.20 |
| 38:09.20 | dead-air trim (0.87 s) | 2292.27 → 2293.14 |
| 43:50.03 | dead-air trim (1.38 s) | 2633.99 → 2635.37 |
| 43:51.83 | dead-air trim (1.06 s) | 2637.16 → 2638.22 |
| 43:55.30 | dead-air trim (0.82 s) | 2641.70 → 2642.52 |
| 44:00.47 | dead-air trim (1.12 s) | 2647.68 → 2648.80 |
| 44:25.87 | dead-air trim (0.87 s) | 2674.20 → 2675.07 |
| 45:48.80 | dead-air trim (1.93 s) | 2757.99 → 2759.92 |
| 50:37.20 | dead-air trim (1.09 s) | 3048.32 → 3049.41 |
| 52:11.67 | dead-air trim (0.85 s) | 3143.87 → 3144.72 |
| 54:44.60 | dead-air trim (1.55 s) | 3297.66 → 3299.21 |
| 54:52.10 | dead-air trim (0.93 s) | 3306.72 → 3307.65 |
| 55:06.30 | dead-air trim (1.06 s) | 3321.84 → 3322.90 |
| 55:45.83 | dead-air trim (2.49 s) | 3362.42 → 3364.91 |
| 58:41.80 | pitch wrap → outro (block seam, no material removed) | 3540.88 → 3540.88 |
| 58:58.27 | outro tightened: 1.5 s of the 1.9 s pause after "It's not me today" removed; in on Chris's "Buy Bitcoin, no financial advice" (all three mics silent at both edges) | 3557.35 → 3558.85 |
| 59:00.37 | outro tightened: Chris's 2.1 s laugh-gap removed; in on Tyler's "Adios, amigos" (all three mics silent at both edges) | 3560.95 → 3563.10 |
| 59:02.47 | end card; "Adios, amigos" is the last line | 3565.20 → |

## Spotify description (paste-ready draft)

```
Sixty percent of Paraguay's adults banked at Ueno, and this week Ueno froze. $800 million of public money inside, the pension fund, the hydro-dam operator, and a president who resigned on the spot. Chris and Tyler on why a country lets one bank get that big, why Australia's four banks could do the same, and why this is a Bitcoin story on every level. Then the brain stuff: frontier models are now doing neurosurgery on smaller models, editing weights by hand in a 20,000-parameter Qwen, and someone found the single neuron that turns Qwen murderous when you ask it for a sandwich. Tyler explains why mechanistic interpretability was given up for dead and why it might be back. Chris found the local CNN inside TikTok that scores your age, expression and attractiveness before anything leaves your phone. Perp of Fortune: long ZhiPu 10×, no Bitcoin flip this week, and the platonic Bart pattern. Chris has been living on GLM 5.3 Flash at 15 cents a million tokens and says it's better than Opus; it also filed his forms in Chinese. Jackson's Instinct booked seven things for his trip and he checked none of them. Proton Mail: a fortress nobody else lives in. Contrarian corner: the Proton CEO stops hiring engineers, so Chris argues the opposite, and Tyler explains why the people who get 10× more productive stop being the bottleneck and get laid off anyway. Then Mithril, the one-person biotech Anthropic bought. Tyler closes with a pitch for a cracked team of three.

The bank freeze is at 2:01. Chapters: Cold open (0:00) · Check-in: still holding our bags (0:47) · Paraguay: 60% of a country banked at Ueno, and it froze (2:01) · LLM neurosurgery (9:23) · Evil Qwen: one neuron, one murderous sandwich (14:52) · TikTok's edge CNN scores your face (18:59) · Perp of Fortune: long ZhiPu 10×, no Bitcoin flip (24:04) · GLM 5.3 Flash (26:41) · Instinct update (35:06) · Proton Mail (38:02) · Contrarian corner: fire everyone but the engineers (42:03) · Mithril: the one-person biotech (50:09) · Tyler's pitch (56:18) · Perp final + outro (58:42)

Recorded fully remote, three cameras, one dashboard. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. Glossary: Ueno = Paraguay's largest bank, placed into resolution with deposits frozen. Solvency ratio = the capital a bank must hold against its loans. Fractional reserve = banks lend out most deposits, so the money isn't there if everyone asks at once. Mechanistic interpretability = mapping what each neuron and circuit in a network does. Distillation = training a small model to copy a big one. Edge model = a small network that runs on your device and sends back summaries. ZhiPu (Z.ai) = the Chinese lab behind GLM; this week's perp. GLM 5.3 Flash = ZhiPu's small open-weights model at about 15¢ per million tokens. Bart pattern = straight up, flat, straight down. Aqua-hire = buying a company for its people. Perp of Fortune = our tiny real-money account; +$2.67 this week.

Subscribe for next week: the Bitcoin flip returns to Perp of Fortune, agentic commerce, and the layer-2 series continues.
```

## Captions

`transcript-attributed.srt` regenerated from the FINAL cut (never the raw recording) in
`episodes/ep22/`. Upload as the `standard` track after Jackson's upload (`yt_captions.py`).

## Production notes

- **The cut:** Jackson asked Tyler on tape what model Instinct runs ("What's your intel?"); Tyler: "We're
  cutting this, not coverable"; Jackson: "cut that question, Claude, and move on." Removed raw 36:22–36:47
  (master 2182.10 → 2206.97). Out edge is mid-breath after "level of model" (the silence gap at 2180.69 would
  have stranded the sentence at "level of"), resume is "Yeah, and that concludes the Instinct update." No whoosh
  on a surgical removal.
- **Tyler's eyebrows (Jackson's note):** the auto shots had Tyler off screen for the raise (1428) and the encore (1439). Pinned duo Chris+Tyler 1427.0–1435.4 and duo Jackson+Tyler 1435.4–1443.0 so he's on frame before and during "I didn't know your eyebrows could go that high."
- **Outro (Jackson's note):** OUTRO split into three hard-edged pieces; removed 1.5 s before "Buy Bitcoin" and the 2.1 s laugh-gap before "Adios, amigos" (3.65 s total). Edges from the three-mic RMS envelope, words from micro-whisper.
- **Order:** kept as recorded. Perp lands at 24:04 and the cut runs 59:09; flagged above.
- **Cold open leak:** first COLD_C cut carried Jackson's "the people don't like robot us" under Chris's line;
  Jackson's track muted 3184.4–3188.1 for the beat.
- **Dashboard share:** `chris-screen` StreamYard file anchored at master 1440.197 (filename delta); full-frame
  1448–1456, then the corner crop [976,100,664,200] through to 3560.8.
- **Bart overlay:** Jackson's on-air request ("overlay a visualization of a non-copyrighted Bart head") is
  `st_bart.png`, a hand-drawn chart callout at PERP master 1562.5 for 8 s; it lives outside `brand.json` so
  `graphics.py` won't regenerate over it.
- **Audio:** Jackson back on the headset mic; light EQ only (`jackson_720eq.mov`, no WPE / gate). Chris on the
  Ep 18/21 chain. Per-track gains ×1.24 / ×0.96 / ×0.72 to gain_target 0.028; edited_raw peak −1.4 dBFS, no flat
  samples.
- **Sync bench not built** (Ep 14–21 precedent for StreamYard filename offsets); turn-gap medians −0.41 / −0.21 /
  +0.21 s across the three pairs confirm the −0.079 offsets.
- **Disclaimer:** Tyler and Jackson say "Not financial advice, personal opinions" at 1:48 final, the first
  spoken disclaimer since Ep 8; the end card still carries the written one.
