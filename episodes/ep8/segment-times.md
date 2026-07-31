# Permanent Underpod — Ep 8 — Segment Times

**Final cut: 52:17 (94,117 frames) · −16.8 LUFS / −1.1 dBTP / LRA 4.3 / flat factor
0.000 on BOTH the final and the `edited_raw.mov` intermediate (no clipping anywhere)
· 0 drift (all 94,116 PTS steps exactly 1000/30000 ticks; A/V durations within 15 ms)
· FULLY-REMOTE episode (three local cams, offsets 0/0/0 — hosts confirmed simultaneous
recording) + continuous live Perp of Fortune dashboard PiP + title/end cards
+ whoosh & gold-wipe on all 15 transitions.**

## Episode video

- **URL:** https://youtu.be/hgLne4ec_Ig — published 2026-07-31 08:13 UTC (public)
- **File:** `media/ep8/Permanent Underpod - Ep 8 (Final Cut).mp4`
- **Title (published):** Claude Broke a Post-Quantum Cipher in 60 Hours. Is Bitcoin Next?
- Jackson uploaded manually. Title AND description match the draft in
  `production-sheet.md` verbatim (13 chapters + glossary). Duration on the live
  copy is 3137 s = 52:17, matching the local master exactly.
- **Tags: NONE on the live copy** — same as Ep 7's manual upload. Worth patching
  via the API (Ep 7 precedent): hawk, post quantum, bitcoin, quantum computing,
  claude, ai, cryptography, bip-110, agentic commerce, x402, podcast. Blocked on
  the OAuth re-auth below.
- Category: People & Blogs (22). Read back by scraping `ytInitialPlayerResponse`
  off the watch page + the channel RSS feed, NOT `yt_fetch.py` — all four tokens
  in `~/.config/clipify-youtube/` currently fail refresh with
  `invalid_grant: Token has been expired or revoked` (same pattern as 7/18).

## YouTube description (as published)

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

See `episodes/ep8/production-sheet.md` (unchanged from the draft).

## Captions

**NOT YET UPLOADED.** `episodes/ep8/ep8-final-cut.srt` is regenerated from the FINAL
assembled cut (never the raw cams — Ep 1 desync rule) and is ready to go; the
person-attributed copies are `transcript-attributed.srt` / `.md`. Upload needs
`token_captions.json` (`youtube.force-ssl`), which is among the revoked tokens.

## Clips (scheduled — daily Jul 31–Aug 7 2026, 2:00 PM Pacific = 21:00 UTC)

Eight 9:16 verticals in `media/clips/ep8/`; decision doc `clips.json`, per-clip copy in
`posting-copy.md`, upload manifest `publishing/manifest_clips.json` (playlist
**Underpod Shorts**, scheduled-private with `publishAt`). Seven are FULL-BLEED FACE
CROPS cut from `media/ep8/work/edited_raw.mov` — the pre-overlay master, so the baked
logo can't be caught on a left-edge crop — carrying the episode audio chain.
`short7` is the exception: it comes off the FINAL mp4 so the live Perp of Fortune
dashboard is visible (the panic-close *is* the dashboard moment), with `logo: false`
and `audio_chain: "anull"` so the bug isn't doubled and the already-mastered audio
isn't processed twice. Release order front-loads the end-of-show bit and separates the
two Ripple jokes so the second reads as a callback.

**Every in/out was pinned by transcribing the real audio in 2.5–3 s bracket windows,
not from the whisper cue times** — those tile backwards over silence and were off by up
to 6 s here, truncating three clips mid-sentence on the first pass. All 8 verified
three ways: content-complete at both ends, loudness (I ≈ −17, TP ≤ −1.44 dBTP), and
geometry (1080×1920, `nb_frames` == duration × 30 exactly).

**Not uploaded yet — blocked on the OAuth re-auth.** A video insert costs ~1600 of the
default 10,000 units/day, so the 8 uploads must be split across two days (6 + 2);
`publishAt` dates are independent of upload dates, so the schedule below still holds.

| Date (2 PM PT) | Clip | Format | Title | Episode ts | URL |
|---|---|---|---|---|---|
| Fri Jul 31 | short7-quick-close-it | 9:16 · 0:12 | We're almost down — quick, CLOSE IT 📉 | 51:39 | _pending upload_ |
| Sat Aug 1 | short4-ever-been-a-ripple-guy | 9:16 · 0:15 | Have you ever been a Ripple guy? 🌊 | 34:46 | _pending upload_ |
| Sun Aug 2 | short3-seven-times-one-evening | 9:16 · 0:19 | The baby egg allergy test went badly 🥚 | 22:35 | _pending upload_ |
| Mon Aug 3 | short6-my-last-name-is-cook | 9:16 · 0:13 | Wait, your last name is actually Cook? 👨‍🍳 | 48:58 | _pending upload_ |
| Tue Aug 4 | short1-nsa-audits-the-crypto | 9:16 · 0:14 | They probably all work for the NSA 🕵️ | 3:41 | _pending upload_ |
| Wed Aug 5 | short8-claude-dont-cut-it-out | 9:16 · 0:12 | Claude, don't cut this out 🎙️ | 51:52 | _pending upload_ |
| Thu Aug 6 | short5-my-agent-only-buys-ripple | 9:16 · 0:09 | My agent only buys Ripple 🤖 | 43:29 | _pending upload_ |
| Fri Aug 7 | short2-give-me-the-crispr-agent | 9:16 · 0:17 | Give me the CRISPR agent, I'm built different 🧬 | 16:51 | _pending upload_ |

**Funnel checklist, manual per clip in Studio once each is public: related video →
episode; pinned comment = `https://youtu.be/hgLne4ec_Ig?t=<seconds>` at the timestamp
above; end screens.** This is the channel's weakest metric.

### Per-clip posting copy

**short7-quick-close-it** (9:16 · 0:12 · episode 51:39)
- Title:   We're almost down — quick, CLOSE IT 📉
- Caption: We let GPT-5.6 pick a 20x leveraged XRP trade with $101 of real money, and the boys had to panic-close it live on air while saying goodbye. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #crypto #xrp

**short4-ever-been-a-ripple-guy** (9:16 · 0:15 · episode 34:46)
- Title:   Have you ever been a Ripple guy? 🌊
- Caption: Tyler asks the question no crypto podcast is brave enough to ask, then diagnoses the condition. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #crypto #xrp

**short3-seven-times-one-evening** (9:16 · 0:19 · episode 22:35)
- Title:   The baby egg allergy test went badly 🥚
- Caption: You're supposed to introduce babies to allergens one at a time to see what happens — here is what happened. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #parenting #dadlife

**short6-my-last-name-is-cook** (9:16 · 0:13 · episode 48:58)
- Title:   Wait, your last name is actually Cook? 👨‍🍳
- Caption: Jackson reveals his surname mid-podcast and immediately gets accused of doxxing himself. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #podcast #cooking

**short1-nsa-audits-the-crypto** (9:16 · 0:14 · episode 3:41)
- Title:   They probably all work for the NSA 🕵️
- Caption: Almost nobody on earth can audit a post-quantum cipher — Tyler's take on who those people work for. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #cryptography #ai

**short8-claude-dont-cut-it-out** (9:16 · 0:12 · episode 51:52)
- Title:   Claude, don't cut this out 🎙️
- Caption: The boys sign off by apologizing for the puke talk, then instruct the AI editing the podcast to make it the centerpiece. It did. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #ai #podcast

**short5-my-agent-only-buys-ripple** (9:16 · 0:09 · episode 43:29)
- Title:   My agent only buys Ripple 🤖
- Caption: If you let an AI agent shop for you, someone has to decide what it's allowed to buy. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #ai #crypto

**short2-give-me-the-crispr-agent** (9:16 · 0:17 · episode 16:51)
- Title:   Give me the CRISPR agent, I'm built different 🧬
- Caption: The case against AI guardrails, argued by two men who would absolutely not be fine. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #ai #biotech
