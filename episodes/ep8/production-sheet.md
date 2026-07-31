# Permanent Underpod — Ep 8 — Production Sheet (pre-publish)

**Final cut: 52:18 (94,154 frames) · −16.5 LUFS / −0.7 dBTP / flat factor 0.000
(no clipping) · 0 drift (94,154 × 1600 audio samples exactly; all PTS gaps 1/30 s;
A/V durations equal within 1.7 ms) · FULLY-REMOTE episode (three local cams,
offsets 0/0/0 — hosts confirmed simultaneous recording) + live Perp of Fortune
dashboard PiP + title/end cards.**

> **NOT YET PUBLISHED.** Fill in URL / published-at / tags after upload. Everything
> below is the paste-ready draft; per house rule the episode goes up FIRST, then
> `segment-times.md` gets backfilled from the live copy via `yt_fetch.py`.

## Episode video

- **URL:** _(pending upload)_
- **File:** `media/ep8/Permanent Underpod - Ep 8 (Final Cut).mp4`
- **Title (draft):** Claude Broke a Post-Quantum Cipher in 60 Hours. Is Bitcoin Next?
- **Alternates:**
  - The Model That Broke the Cipher Is the One You're Not Allowed to Use
  - An AI Did $100K of Cryptanalysis Over a Long Weekend
  - We Finally Talked About Agentic Payments — Four Protocols, Zero Winners
  - Anthropic's Mythos Broke the Crypto Meant to Save Bitcoin From Q-Day (It's Fine)

## YouTube description (paste-ready)

```
Anthropic's Mythos spent about 60 hours and $100K of API time and came out the other side with a real attack on HAWK, a post-quantum signature candidate that had already survived two years of human expert review. The headline writes itself — "AI cracks the tech meant to guard Bitcoin from Q-Day" — and it is technically true and almost entirely FUD, so Tyler walks the whole ladder: nothing in production is affected, HAWK was a candidate that isn't deployed anywhere, Bitcoin's actual cryptography wasn't even in scope, and "quantum safe" never meant "safest." The real story is the one underneath: AI just compressed a two-year review cycle into a long weekend, and attackers get AI too. Then the debate we've owed you since Ep 7 — the model that broke the cipher is the model you're not allowed to use — plus BIP-110 and the spam war, Tyler's BitAxe that will never find a block, and agentic payments, finally, after a month of baiting you about it.

🔥 On the Agenda
0:00 Cold open
1:21 The boys are back
1:59 The marquee: Claude broke a post-quantum cipher
8:27 The debate we owed you: who gets the dangerous model?
18:28 Check-in: gamer thumb, wrists & one egg
22:41 Palate cleanser: Margo vs the allergen test
24:08 BIP-110 and the spam war
31:01 Tyler's BitAxe has no chance
32:45 Perp of Fortune: GPT-5.6 goes long XRP at 20x
34:52 Confession corner: have you ever been a Ripple guy?
39:26 Agentic commerce, finally
45:39 The standards war: four protocols, zero winners
50:21 Wrap + next week

Recorded fully remote — three cameras, one live perp dashboard.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. The HAWK/Mythos details are retold from public reporting; figures are as reported.

GLOSSARY
• HAWK: a lattice-based post-quantum signature scheme, a NIST candidate — not deployed anywhere. Mythos found a structural weakness that gutted its effective key strength and its standardization hopes. The system working as intended: better to learn this now than after everyone migrated onto it.
• Post-quantum / "quantum safe": cryptography designed to survive a quantum computer. Tyler's key point — it only means "safe against Shor's algorithm." It says nothing about whether a classical attack exists, which is exactly what Mythos found.
• Shor's algorithm: the quantum algorithm that would break the elliptic-curve crypto Bitcoin uses today. We know that vulnerability exists; nobody has found a classical break for it.
• BIP-360: the proposal adding quantum-resistant Bitcoin addresses. Targets finalized NIST schemes — not HAWK — which is why "AI broke Bitcoin's quantum plan" is wrong.
• BIP-110: the proposal at the center of this week's spam war, and the fork fight nobody actually wants. Tyler's verdict: mostly a publicity stunt.
• BitAxe: a desk-sized solo Bitcoin miner. Tyler owns one. It has, in his words, no chance of ever finding a block — but he can repoint it at a new pool in 30 seconds, which is the whole point about miners and forks.
• x402 / MPP / AP2 / ACP: the four competing agentic-payment protocols. x402 repurposes HTTP's 402 "Payment Required"; Stripe and Tempo's MPP is a superset of it. Four proposals, zero winners so far.
• Perp of Fortune: an LLM picks a leveraged perpetual futures trade with $101 of real money and we live with it. This week Chris fed GPT-5.6 the podcast transcript and it went long XRP at 20x.
• Mythos: Anthropic's approved-orgs-only model tier — the one that did the cryptanalysis, and the one you can't get.

🔔 Subscribe for next week: the GENIUS Act deadline actually passed, an open-weight Mythos in six months?, and Perp of Fortune rolls again.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open |
| 1:21 | The boys are back |
| 1:59 | The marquee: Claude broke a post-quantum cipher |
| 8:27 | The debate we owed you: who gets the dangerous model? |
| 18:28 | Check-in: gamer thumb, wrists & one egg |
| 22:41 | Palate cleanser: Margo vs the allergen test |
| 24:08 | BIP-110 and the spam war |
| 31:01 | Tyler's BitAxe has no chance |
| 32:45 | Perp of Fortune: GPT-5.6 goes long XRP at 20x |
| 34:52 | Confession corner: have you ever been a Ripple guy? |
| 39:26 | Agentic commerce, finally |
| 45:39 | The standards war: four protocols, zero winners |
| 50:21 | Wrap + next week |

## Spotify description (paste-ready)

Chapters in parenthesized form (≥30 s spacing), glossary inlined as plain text
since Spotify ignores markdown.

```
Anthropic's Mythos spent about 60 hours and $100K of API time and came out the other side with a real attack on HAWK, a post-quantum signature candidate that had already survived two years of human expert review. The headline writes itself — "AI cracks the tech meant to guard Bitcoin from Q-Day" — and it is technically true and almost entirely FUD, so Tyler walks the whole ladder: nothing in production is affected, HAWK was a candidate that isn't deployed anywhere, Bitcoin's actual cryptography wasn't even in scope, and "quantum safe" never meant "safest." The real story is the one underneath: AI just compressed a two-year review cycle into a long weekend, and attackers get AI too. Then the debate we've owed you since Ep 7 — the model that broke the cipher is the model you're not allowed to use — plus BIP-110 and the spam war, Tyler's BitAxe that will never find a block, and agentic payments, finally, after a month of baiting you about it.

On the agenda: Cold open (0:00) · The boys are back (1:21) · The marquee: Claude broke a post-quantum cipher (1:59) · The debate we owed you: who gets the dangerous model? (8:27) · Check-in: gamer thumb, wrists & one egg (18:28) · Palate cleanser: Margo vs the allergen test (22:41) · BIP-110 and the spam war (24:08) · Tyler's BitAxe has no chance (31:01) · Perp of Fortune: GPT-5.6 goes long XRP at 20x (32:45) · Confession corner: have you ever been a Ripple guy? (34:52) · Agentic commerce, finally (39:26) · The standards war: four protocols, zero winners (45:39) · Wrap + next week (50:21)

Recorded fully remote — three cameras, one live perp dashboard. Our opinions are our own, not our employers'. NOT financial advice. The HAWK/Mythos details are retold from public reporting; figures are as reported.

Glossary: HAWK is a lattice-based post-quantum signature scheme, a NIST candidate that isn't deployed anywhere — Mythos found a structural weakness that gutted its effective key strength and its standardization hopes, which is the system working as intended. Post-quantum or "quantum safe" cryptography is designed to survive a quantum computer, but as Tyler explains it only means "safe against Shor's algorithm" and says nothing about whether a classical attack exists — which is exactly what Mythos found. Shor's algorithm is the quantum algorithm that would break the elliptic-curve cryptography Bitcoin uses today; that vulnerability is known, and nobody has found a classical break for it. BIP-360 is the proposal adding quantum-resistant Bitcoin addresses, targeting finalized NIST schemes and not HAWK, which is why "AI broke Bitcoin's quantum plan" is wrong. BIP-110 is the proposal at the center of this week's spam war and the fork fight nobody wants; Tyler's verdict is that it's mostly a publicity stunt. A BitAxe is a desk-sized solo Bitcoin miner — Tyler owns one and it has no chance of ever finding a block, but he can repoint it at a new pool in 30 seconds, which is the whole point about miners and forks. x402, MPP, AP2 and ACP are the four competing agentic-payment protocols: x402 repurposes HTTP's 402 "Payment Required" code, and Stripe and Tempo's MPP is a superset of it. Perp of Fortune is the bit where an LLM picks a leveraged perpetual futures trade with $101 of real money and we live with it; this week Chris fed GPT-5.6 the podcast transcript and it went long XRP at 20x. Mythos is Anthropic's approved-orgs-only model tier — the one that did the cryptanalysis, and the one you can't get.

Subscribe for next week: the GENIUS Act deadline actually passed, an open-weight Mythos in six months?, and Perp of Fortune rolls again.
```

## Captions

**PENDING UPLOAD.** `episodes/ep8/ep8-final-cut.srt` — regenerated from the FINAL
assembled cut (never the raw recordings; Ep 1 desync rule), 52:09 of cues capped at
90 chars / split on word. Person-attributed copies alongside it
(`transcript-attributed.srt` / `.md`) from `remote_attribute.py`. Upload via the
captions API with `~/.config/clipify-youtube/token_captions.json`
(`youtube.force-ssl` scope).

## Editorial decisions (this cut)

Requested by Jackson, all verified against VAD-confirmed silence so every seam
lands in a real pause:

- **"I work in fintech" — CUT.** Body ends 2721.97, resumes 2768.23, plus a
  `mute` on jackson 2768.30–2771.00 to kill the tail. Keeps Tyler's "the marketing
  department of Ripple is amazing" and Chris's "It's over. Ripple Bros, it's over."
- **Baby-vomit story — TRIMMED 155 s → ~90 s.** Keeps the allergen setup, the egg,
  the seven-times/children's-hospital beat and the "we grossed out all of our
  listeners" button; drops the egg-and-applesauce concoction riff, the allergist
  plan and the ghost/lethargic beat. Tyler's outro callback ("sorry about all the
  puke talk earlier") still lands.
- **REORDERED.** Only the 38 s welcome stays up front so the marquee starts at
  1:59; the whole check-in + vomit block moves to 18:28 as a mid-show palate
  cleanser. Jackson calls this on mic at master 438 ("maybe we'll move this to the
  middle").
- **Cut for length (~7 min):** BIP-110 fork minutiae (futures markets/Bitfinex,
  pool-switching detail, Bitmain covert ASIC boost, Luke Dash Jr), Jackson's
  unanswered geo-fence war-tool question, Chris's Ethereum-Classic replay-attack
  detour, the OCC-charter tail, the "we went red" dead patch, and the repetitive
  multi-rail hedging in the standards-war wrap. Lands 52:18, inside the 45–55
  target.
- **Cold open:** six teasers, ~77 s, ending on the perp finale tease with the
  dashboard already on screen.

## Pipeline notes / two bugs fixed in the shared scripts

- `remote_cut.py` — `to_final()` crashed (`float <= None`) on any `sheet` row,
  since sheet rows carry no `m`. Now falls back to the block's start.
- `remote_cutlist.py` — the per-track gain clamp had a **0.5 floor that binds** at
  a low `gain_target`, silently destroying the per-speaker equalization it exists
  for (chris 0.36 and tyler 0.39 were both pinned to 0.5). Floor lowered to 0.05.
- `final_render.py` — the final limiter now runs **4× oversampled**. `alimiter`
  caps sample peak, but AAC encodes the continuous waveform, so inter-sample peaks
  become real samples on decode.
- **`gain_target` 0.028 was still clipping** (my Ep 5 note only ruled out 0.055).
  It drove `edited_raw.mov` to 0 dBFS with 192k flat-topped samples across 1,595
  clusters — jackson alone at ×2.88 peaked at 2.06. Now **0.006** (worst-case sum
  ≈0.67), with a matching `volume=13.1dB` restored inside the render chain so
  `afftdn`/`acompressor` still see the levels they were tuned for. Result: flat
  factor 0.000, and loudness unchanged because `loudnorm` normalizes anyway.

## Clips

Not cut yet — `clipify` pass comes after the episode is live (house rule:
episode first, then clips staggered daily at 2 PM PT / 21:00 UTC). Candidate picks
from this cut, personality-first:

| Candidate | Time | Why |
|---|---|---|
| "Fable thinks I'm trying to steal $15 billion, which I'm not" | cold open | best line in the episode |
| "Give me the CRISPR agent, I'm built different" | ~9:00 | Chris, guardrails debate |
| "They probably all work for the NSA and don't do this out of the goodness of their heart" | ~9:21 | Tyler, marquee |
| "My agent only buys Ripple" | 31:xx (COLD5 source) | Tyler, agentic commerce |
| "Did you know my last name is Cook" | 49:01 | Jackson, nominative determinism |
| "It's over. Ripple Bros, it's over." | 34:5x | Chris |
| Seven times, one evening, both parents | 22:41 | the palate cleanser |
