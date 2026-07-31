# Permanent Underpod — Ep 8 — Production Sheet (pre-publish)

**Final cut: 52:17 (94,117 frames) · −16.8 LUFS / −1.1 dBTP / LRA 4.3 / flat factor
0.000 on BOTH the final and the `edited_raw.mov` intermediate (no clipping anywhere)
· 0 drift (all 94,116 PTS steps exactly 1000/30000 ticks; A/V durations within 15 ms)
· FULLY-REMOTE episode (three local cams, offsets 0/0/0 — hosts confirmed simultaneous
recording) + continuous live Perp of Fortune dashboard PiP + title/end cards
+ whoosh & gold-wipe on all 15 transitions.**

> **NOT YET PUBLISHED.** Fill in URL / published-at / tags after upload. Everything
> below is the paste-ready draft; per house rule the episode goes up FIRST, then
> `segment-times.md` gets backfilled from the live copy via `yt_fetch.py`.

## Episode video

- **URL:** _(pending upload)_
- **File:** `media/ep8/Permanent Underpod - Ep 8 (Final Cut).mp4` (2.87 GB)
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
2:06 The marquee: Claude broke a post-quantum cipher
8:33 The debate we owed you: who gets the dangerous model?
18:34 Check-in: gamer thumb, wrists & one egg
22:40 Palate cleanser: Margo vs the allergen test
24:06 BIP-110 and the spam war
31:00 Tyler's BitAxe has no chance
32:44 Perp of Fortune: GPT-5.6 goes long XRP at 20x
34:51 Confession corner: have you ever been a Ripple guy?
38:47 Agentic commerce, finally
45:38 The standards war: four protocols, zero winners
50:19 Wrap + next week

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
| 2:06 | The marquee: Claude broke a post-quantum cipher |
| 8:33 | The debate we owed you: who gets the dangerous model? |
| 18:34 | Check-in: gamer thumb, wrists & one egg |
| 22:40 | Palate cleanser: Margo vs the allergen test |
| 24:06 | BIP-110 and the spam war |
| 31:00 | Tyler's BitAxe has no chance |
| 32:44 | Perp of Fortune: GPT-5.6 goes long XRP at 20x |
| 34:51 | Confession corner: have you ever been a Ripple guy? |
| 38:47 | Agentic commerce, finally |
| 45:38 | The standards war: four protocols, zero winners |
| 50:19 | Wrap + next week |

## Spotify description (paste-ready)

Chapters in parenthesized form (≥30 s spacing), glossary inlined as plain text
since Spotify ignores markdown.

```
Anthropic's Mythos spent about 60 hours and $100K of API time and came out the other side with a real attack on HAWK, a post-quantum signature candidate that had already survived two years of human expert review. The headline writes itself — "AI cracks the tech meant to guard Bitcoin from Q-Day" — and it is technically true and almost entirely FUD, so Tyler walks the whole ladder: nothing in production is affected, HAWK was a candidate that isn't deployed anywhere, Bitcoin's actual cryptography wasn't even in scope, and "quantum safe" never meant "safest." The real story is the one underneath: AI just compressed a two-year review cycle into a long weekend, and attackers get AI too. Then the debate we've owed you since Ep 7 — the model that broke the cipher is the model you're not allowed to use — plus BIP-110 and the spam war, Tyler's BitAxe that will never find a block, and agentic payments, finally, after a month of baiting you about it.

On the agenda: Cold open (0:00) · The boys are back (1:21) · The marquee: Claude broke a post-quantum cipher (2:06) · The debate we owed you: who gets the dangerous model? (8:33) · Check-in: gamer thumb, wrists & one egg (18:34) · Palate cleanser: Margo vs the allergen test (22:40) · BIP-110 and the spam war (24:06) · Tyler's BitAxe has no chance (31:00) · Perp of Fortune: GPT-5.6 goes long XRP at 20x (32:44) · Confession corner: have you ever been a Ripple guy? (34:51) · Agentic commerce, finally (38:47) · The standards war: four protocols, zero winners (45:38) · Wrap + next week (50:19)

Recorded fully remote — three cameras, one live perp dashboard. Our opinions are our own, not our employers'. NOT financial advice. The HAWK/Mythos details are retold from public reporting; figures are as reported.

Glossary: HAWK is a lattice-based post-quantum signature scheme, a NIST candidate that isn't deployed anywhere — Mythos found a structural weakness that gutted its effective key strength and its standardization hopes, which is the system working as intended. Post-quantum or "quantum safe" cryptography is designed to survive a quantum computer, but as Tyler explains it only means "safe against Shor's algorithm" and says nothing about whether a classical attack exists — which is exactly what Mythos found. Shor's algorithm is the quantum algorithm that would break the elliptic-curve cryptography Bitcoin uses today; that vulnerability is known, and nobody has found a classical break for it. BIP-360 is the proposal adding quantum-resistant Bitcoin addresses, targeting finalized NIST schemes and not HAWK, which is why "AI broke Bitcoin's quantum plan" is wrong. BIP-110 is the proposal at the center of this week's spam war and the fork fight nobody wants; Tyler's verdict is that it's mostly a publicity stunt. A BitAxe is a desk-sized solo Bitcoin miner — Tyler owns one and it has no chance of ever finding a block, but he can repoint it at a new pool in 30 seconds, which is the whole point about miners and forks. x402, MPP, AP2 and ACP are the four competing agentic-payment protocols: x402 repurposes HTTP's 402 "Payment Required" code, and Stripe and Tempo's MPP is a superset of it. Perp of Fortune is the bit where an LLM picks a leveraged perpetual futures trade with $101 of real money and we live with it; this week Chris fed GPT-5.6 the podcast transcript and it went long XRP at 20x. Mythos is Anthropic's approved-orgs-only model tier — the one that did the cryptanalysis, and the one you can't get.

Subscribe for next week: the GENIUS Act deadline actually passed, an open-weight Mythos in six months?, and Perp of Fortune rolls again.
```

## Captions

**PENDING UPLOAD.** `episodes/ep8/ep8-final-cut.srt` — 674 cues regenerated from the
FINAL assembled v2 cut (never the raw recordings; Ep 1 desync rule), capped at 90
chars / split on word, running to 52:11. Person-attributed copies alongside it
(`transcript-attributed.srt` / `.md`, 674 cues / 136 turns) from `remote_attribute.py`.
Upload via the captions API with `~/.config/clipify-youtube/token_captions.json`
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
- **REORDERED.** Only the welcome stays up front; the whole check-in + vomit block
  moves to 18:34 as a mid-show palate cleanser. Jackson calls this on mic at master
  438 ("maybe we'll move this to the middle").
- **Cut for length (~7 min):** BIP-110 fork minutiae (futures markets/Bitfinex,
  pool-switching detail, Bitmain covert ASIC boost, Luke Dash Jr), Jackson's
  unanswered geo-fence war-tool question, Chris's Ethereum-Classic replay-attack
  detour, the OCC-charter tail, the "we went red" dead patch, and the repetitive
  multi-rail hedging in the standards-war wrap. Lands 52:17, inside the 45–55 target.
- **Cold open:** six teasers, ~77 s, ending on the perp finale tease with the
  dashboard already on screen.

### v2 revision (Jackson's notes on the first cut)

- **Chris's compliment restored to the intro.** v1 split S1 at master 38.0, which
  landed mid-utterance and dumped the tail of "…by myself, I can barely carry a third
  of it so just massive props" at 18:28, mid-show. Root cause: whisper logged that
  line as starting at 21 s, so the seam audit never showed Chris still talking at 38.0;
  `spans.py` proved he speaks continuously 34.28→45.22. Split moved to the next true
  all-silent gap, **45.71**. Verified by transcribing the rendered audio: the whole
  compliment now plays at ~1:52–2:05.
- **"And I think" removed** before "…this is the perfect time to transition."
  Word-level whisper put the boundary at 444.64–444.66 and a 5 ms energy envelope
  confirmed the dip; S2a's `m0` moved 443.48 → **444.66**. Because S1 already ends at
  a block boundary this created NO new splice. Confirmed in the render: it goes
  straight from "…for keeping it going." to "This is the perfect time to transition."
- **Whoosh + gold wipe on ALL 15 transitions** (Jackson: "always do transition sound
  + wipe" — now a house rule in the skill). v1 shipped 12 `sfx` and `"anim": []`, so
  the wipes were entirely absent. Each wipe starts 0.18 s before its cut so the accent
  bar peaks on the splice.
- **Far more multi-person framing.** `remote_motion.py` (new) detects *visual*
  reactions — a silent laugh, a nod, hands up — which the VAD-only planner could never
  see, and the cutlist now puts reactors on screen NEXT TO the speaker (the speaker is
  always retained, so a reaction can only widen a shot, never cut away from whoever is
  talking). Swept 5 threshold combos; `group_thresh 0.18 / react_thresh 0.35` gave
  56.5% split-screen — over half the show, which defeats the point. Shipped
  **0.25 / 0.60 → 34.0% multi-person** (duo 26.4% + trio 7.6%, vs v1's 14.2%), solo
  still the 66% majority. 255 live pieces: 116 solo / 111 duo / 28 trio.
- **Perp of Fortune PiP now runs continuously** from 33:55 to 51:46 instead of only
  during the perp segment. Safe because master time is monotonic across S5→S8, so the
  wall-clock-synced dashboard never rewinds or spoils the finale. The only holes are
  the by-design 6.6 s windows where a lower third is up (`remote_cut.py` hides the PiP
  ±0.3 s around any overlay).
- **Consequence, accepted:** S1 grew ~7.7 s, so the marquee moves 1:59 → 2:06,
  slightly past the "first real segment by ~2 min" retention default. Jackson
  explicitly wants the compliment in the intro, so this is the right trade.

## Pipeline notes / bugs fixed in the shared scripts

- `remote_cut.py` — `to_final()` crashed (`float <= None`) on any `sheet` row, since
  sheet rows carry no `m`. Now falls back to the block's start.
- `remote_cutlist.py` — the per-track gain clamp had a **0.5 floor that binds** at a
  low `gain_target`, silently destroying the per-speaker equalization it exists for
  (chris 0.36 and tyler 0.39 were both pinned to 0.5). Floor lowered to 0.05.
- **`gain_target` 0.028 was still clipping** (the Ep 5 note only ruled out 0.055). It
  drove `edited_raw.mov` to 0 dBFS with 192k flat-topped samples across 1,595 clusters
  — jackson alone at ×2.88 peaked at 2.06. Now **0.006** (worst-case sum ≈0.67) with a
  matching `volume=13.1dB` inside the render chain so `afftdn`/`acompressor` still see
  the levels they were tuned for. v2 intermediate: peak −0.49 dBFS, flat factor 0.000.
- `final_render.py` — **`anim` windows were phase-broken.** `-stream_loop -1` restarts
  the file on multiples of its OWN duration while `enable=between()` only gates
  visibility, so a window opened at phase `(start mod dur)` and the animation wrapped
  mid-sweep: measured at start=76.59 the gold bar peaked 2 frames in, vanished, then
  reappeared later in the same window. Windows whose start happened to be a near-
  multiple of 0.4 s looked fine, which is why it hid. Now the input PTS is shifted by
  `(start mod dur)` so frame 0 lands exactly on `start` for every window.
- `final_render.py` — added **`--audio-only`**, which re-runs just the audio graph and
  remuxes into the existing render with `-c:v copy`. SKILL.md has prescribed this fix
  for hot masters since Ep 1 but nothing implemented it, so the only option was a full
  ~10 min re-encode of an hour of video for an audio problem. The audio-only pass takes
  **72 s** and leaves the video bit-identical; both loudness iterations below used it.
- **Corrected a false note I had written into `final_render.py`**: the 4×-oversampled
  limiter did NOT fix Ep 8's true peak — it produced a bit-identical file, because the
  overage had already been clipped into the 16-bit PCM intermediate upstream. The
  comment now says so, since shipping it would have misled the next episode.
- **Delivery loudness needed two audio-only iterations.** At `limit` 0.84 the master
  decoded at **+1.1 dBTP** (3 samples at 32:54.24, 1 at 38:16.35 — the resample+AAC
  overshoot factor measured ~1.35× above the limiter ceiling, consistently). Dropping
  to `limit` **0.65** gave −1.1 dBTP with zero overs, but cost 0.9 LU (−17.4 LUFS).
  Since the limiter fixes true peak regardless of how much gain precedes it,
  `target_lufs` was raised to **−14.5** purely as make-up; delivered **−16.8 LUFS**.
  Note `target_lufs` is therefore a *pre-limiter setpoint*, not the delivered loudness.
  Stopped there: +1.5 dB of extra gain only bought +0.6 LU, which is the limiter
  telling you it's absorbing the rest — pushing further just flattens transients.

## Clips

Not cut yet — `clipify` pass comes after the episode is live (house rule: episode
first, then clips staggered daily at 2 PM PT / 21:00 UTC). Candidate picks from this
cut, personality-first (times are v2):

| Candidate | Time | Why |
|---|---|---|
| "Fable thinks I'm trying to steal $15 billion, which I'm not" | cold open | best line in the episode |
| "Give me the CRISPR agent, I'm built different" | ~9:05 | Chris, guardrails debate |
| "They probably all work for the NSA and don't do this out of the goodness of their heart" | ~9:25 | Tyler, marquee |
| "My agent only buys Ripple" | COLD5 source | Tyler, agentic commerce |
| "Did you know my last name is Cook" | ~49:00 | Jackson, nominative determinism |
| "It's over. Ripple Bros, it's over." | ~34:55 | Chris |
| Seven times, one evening, both parents | ~22:40 | the palate cleanser |
