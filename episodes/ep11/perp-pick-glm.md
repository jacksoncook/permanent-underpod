# Ep 11 Perp of Fortune — GLM 4.7 Flash's pick

Generated 2026-08-19/20 on Jackson's machine: `ollama run glm-4.7-flash:latest`
(local, open weights — the bit is that GLM is the model family Hugging Face used
for the intrusion forensics after commercial APIs refused). Four runs, escalating
rigor — **the arc IS the segment.** Constraints on all runs: no BTC (house rule),
no PUMP (position still open), exactly one pick.

## PICK OF RECORD (run 4 — read the prep guide + live research; Jackson's ask, 8/20)

GLM got the full Ep 11 prep guide (perp section removed) in its system prompt plus
the live-data tool loop, and was told to tie the pick to a real story in the guide:

```
PICK: LIT
DIRECTION: long
LEVERAGE: 10x
NEWS THESIS: The "Mind Viruses" paper (Topic B) and the upcoming "Secure Enclaves"
segment (Topic K) both zero in on the fragility of data and keys; Lit Protocol
provides the decentralized storage and identity layer for agents needing secure
custody.
RESEARCH BASIS: LIT is a top-volume trade (+16.8% 24h) on Hyperliquid, showing
market interest in the "security infrastructure" angle of the episode.
REASONING: The episode is all about AI security vulnerabilities. If agents are
going to "infect" each other and need "secure enclaves," they need a place to
keep their loot—Lit Protocol.
ONE-LINER FOR THE HOSTS: "If agents are going to be infected with bad ideas, the
least we can do is make sure their key wallets are on Lit."
```

Verified at pick time (2026-08-20): LIT +16.5% 24h, funding +0.0013%/hr, OI
~$103M, vol ~$72M — its cited numbers are real, though it bought a top gainer
during a marketwide rip (Topic N). Round 0 of this run it tried to pick "RNDR" —
a ticker that does not exist on Hyperliquid (it's RENDER) — then read the data
and switched.

**RESOLVED — what LIT actually is: Lighter**, a ZK-rollup perp DEX on Ethereum
and Hyperliquid's main rival ("next Hyperliquid" is the whole narrative). NOT
Lit Protocol, which is what GLM's entire thesis is about. 0-for-4 on knowing
what it bought — and accidentally the best pick yet: **the AI longed
Hyperliquid's competitor, on Hyperliquid, for reasons that belong to a
different project.** Do the reveal on air: read its key-custody thesis, then
tell it what Lighter is. Known fuse (structural, not chart talk): 75% of LIT
supply starts unlocking late Dec 2026; monthly volume −83% from the Dec
farming peak. Transcript: `perp-pick-glm-v3-raw.json`; harness:
`perp_research_v3.py` (v1/v2 in `perp_research.py`).

## Run 3 (superseded): researched pick, no guide

Given only live data, GLM picked **long ACE 5×** — top gainer +22.7%, extreme
negative funding −0.0654%/hr, called the short squeeze. One-liner: *"My AI models
detected a funding arbitrage opportunity... which means I'm about to get squeezed
right along with you guys."* Misidentified ACE (Fusionist, gaming) as "this AI
token." Transcript: `perp-pick-glm-v2-raw.json`.

**Leverage note for the 100× motion:** blind it escalated to 15×; with data it
CUT to 5×; with the news it settled at 10×. Research made the machine a coward,
and the news made it exactly house-standard. Use that in the vote.

## The four-run arc (all on-air material)

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
4. **Run 4 — the guide + research (PICK OF RECORD):** given the episode's own
   prep guide, it picked the episode's own thesis — long LIT 10×, "agents need
   a place to keep their loot" — after first ordering a ticker that doesn't
   exist. The show's research now feeds the show's gambling. Closed loop.

## Notes for the segment

- Position to enter on air, small account, house rules apply. **Say the
  disclaimers out loud when placing it** (see prep-guide Compliance).
- ACE is thin (~$2M OI) — the squeeze thesis and the "we ARE the liquidity"
  joke are the same fact.
- If PUMP is still open at record time, the board runs two positions for the
  first time ever. Dashboard pip covers both.
- Run 2's fabricated-research output is a perfect cold-open candidate against
  Topic B: we watched a local model make up its homework in real time.
