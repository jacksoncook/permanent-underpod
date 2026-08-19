# Ep 11 Perp of Fortune — GLM 4.7 Flash's pick

Generated 2026-08-19 on Jackson's machine: `ollama run glm-4.7-flash:latest` (local,
open weights — the bit is that GLM is the model family Hugging Face used for the
intrusion forensics after commercial APIs refused). Three runs, escalating rigor —
**the arc IS the segment.** Constraints on all runs: no BTC (house rule), no PUMP
(position still open), exactly one pick.

## PICK OF RECORD (run 3 — with live research)

GLM was given a tool loop against the live Hyperliquid API (market overview +
per-coin stats: 24h change, funding, OI, volume, 7d candles) and told to research
before picking. It pulled the board, found the funding dislocation, and picked:

```
PICK: ACE
DIRECTION: long
LEVERAGE: 5x
RESEARCH BASIS: ACE is the top gainer with a massive 24h change of +22.7%, driven
by an extreme negative funding rate of -0.0654%/hr, meaning shorts are aggressively
paying longs.
REASONING: The data screams "short squeeze" here. Longs are literally getting paid
to stay in this position because the shorts are panicking and bleeding fees. I'm
betting the shorts stay broken and this AI token keeps pumping.
ONE-LINER FOR THE HOSTS: "My AI models detected a funding arbitrage opportunity...
which means I'm about to get squeezed right along with you guys."
```

The numbers it cited are real (pulled 2026-08-19: ACE +22.7% 24h, funding
−0.0654%/hr, OI ~$2.0M, vol ~$2.1M). Full research transcript:
`perp-pick-glm-v2-raw.json`.

**It misidentified its pick AGAIN:** ACE is Fusionist — a gaming token, not "this
AI token." Second run in a row GLM bought something it couldn't name. Verify on
air, then read its own one-liner back to it.

**Leverage note for the 100× motion:** blind, it escalated to 15×; with actual
data in front of it, it CUT to 5×. Research made the machine a coward. That's the
counter-argument to Tyler's motion, delivered by the picker itself.

## The three-run arc (all on-air material)

1. **Run 1 — blind pick:** fed only the ticker list → **long FET 15×**, after
   publicly waffling through TRUMP/WIF/ZRO and picking the AI coin because it's
   an AI (*"It feels like GLM picking a winner in the AI arms race narrative"*).
   Misidentified FET twice while buying it. Raw: `perp-pick-glm-raw.txt`.
2. **Run 2 — the fabrication:** given research tools, it broke the tool protocol
   three rounds straight (fired multiple calls per line, got errors every time),
   retrieved ZERO data — then **invented its research** (*"Analysis of the AI
   sector indices shows Fetch.ai leading volume with a 15% intraday surge"* —
   never pulled) and re-picked FET at **20×**, escalating leverage while
   hallucinating the basis. This is the mind-virus episode's thesis in one run:
   confident, cited, fake.
3. **Run 3 — real research** (harness fixed to accept its multi-call style):
   pulled the actual board, cited actual numbers, picked ACE at **5×**. Still
   didn't know what ACE is.

## Notes for the segment

- Position to enter on air, small account, house rules apply. **Say the
  disclaimers out loud when placing it** (see prep-guide Compliance).
- ACE is thin (~$2M OI) — the squeeze thesis and the "we ARE the liquidity"
  joke are the same fact.
- If PUMP is still open at record time, the board runs two positions for the
  first time ever. Dashboard pip covers both.
- Run 2's fabricated-research output is a perfect cold-open candidate against
  Topic B: we watched a local model make up its homework in real time.
