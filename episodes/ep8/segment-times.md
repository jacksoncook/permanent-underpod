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
- **Tags (patched via API 2026-07-31):** agentic commerce, ai, bip-110, bitcoin,
  claude, cryptography, hawk, podcast, post quantum, quantum computing, x402 — the
  manual upload had none, same as Ep 7. Verified on read-back that the title and
  description came through byte-identical (the `videos.update` gotcha: a `None`-valued
  snippet field makes the API silently drop the tags edit; omit absent fields).
  The API returns tags ALPHABETIZED, so compare as a set, not a list.
- Category: People & Blogs (22). The published metadata above was first read back by
  scraping `ytInitialPlayerResponse` off the watch page — all four tokens in
  `~/.config/clipify-youtube/` were revoked (`invalid_grant`) when Jackson published
  manually, the third time that has happened. Re-authed 2026-07-31, all four on the
  brand channel (`Permanent Underpod - Podcast`, UCmZ_tUPnopsFJS615b-NtbA); the dead
  ones are retired as `token*.json.revoked-2026-07-31`.

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

**UPLOADED 2026-07-31 via the captions API** — `episodes/ep8/ep8-final-cut.srt`,
regenerated from the FINAL assembled cut, never the raw cams (Ep 1 desync rule).
Track `en`, trackKind `standard`, status **serving**, alongside YouTube's own `asr`
track. Person-attributed copies are `transcript-attributed.srt` / `.md`. Token
`token_captions.json` (`youtube.force-ssl` — the broad `youtube` scope 403s on every
captions method). Note `trackKind` reads back LOWERCASE (`asr`), so a case-sensitive
"skip if a non-ASR track exists" guard wrongly skips the upload.

## Clips (scheduled — daily Aug 1–7 2026 at 2:00 PM Pacific = 21:00 UTC;
short7 leads at **6:00 PM PT Jul 31** = 2026-08-01T01:00:00Z)

**Why short7 is off the 2 PM slot:** Ep 7's `short6-freestyle` already publishes Jul 31
at 2 PM PT, so the lead clip was pushed 4 h to 6 PM PT rather than stacking two shorts
in one slot on the same day. Everything after it is on the house 2 PM cadence.

Eight 9:16 verticals in `media/clips/ep8/`; decision doc `clips.json`, per-clip copy in
`posting-copy.md`, upload manifest `publishing/manifest_clips_v2.json` (playlist
**Underpod Shorts**, scheduled-private with `publishAt`). Seven are FULL-BLEED FACE
CROPS cut from `media/ep8/work/edited_raw.mov` — the pre-overlay master, so the baked
logo can't be caught on a left-edge crop — carrying the episode audio chain.
`short7` is the exception: it comes off the FINAL mp4 so the live Perp of Fortune
dashboard is visible (the panic-close *is* the dashboard moment), with `logo: false`
and `audio_chain: "anull"` so the bug isn't doubled and the already-mastered audio
isn't processed twice. Release order front-loads the end-of-show bit and separates the
two Ripple jokes so the second reads as a callback.

**RE-CUT AND RE-UPLOADED 2026-07-31** (v2). Jackson watched the first batch and found
two defects; both are fixed in the skills (commits `d835f6b`, `5c26548`) and every clip
was re-rendered and re-uploaded. The URLs in the table below are the v2 ones — the v1
videos were deleted, all while still private, so nothing broken ever reached an audience.

1. **"Boomerang."** The shot appeared to swing off a person and return, sometimes with
   no speaker change. `clipify.py` was easing EVERY `face_crops` key across 0.35 s, but
   the vertical crop is a 406 px column of a 1280 px frame — narrower than the gap
   between any two faces — so a glide always spends its middle frames on the panel seam:
   wall plus two half-faces. Worst when the same person sat on both sides of the switch.
   All crop switches are now hard cuts; verified 14/14 land on the new x one frame after
   the key.
2. **Clips cutting mid-sentence.** The earlier claim here that all 8 were "content-complete
   at both ends" was **wrong**: an audit against a 10 ms speech-band RMS envelope plus
   word-level whisper found **11 of the 16 in/out points sitting mid-speech**, including
   `short7` truncating "Close it!" — the exact line in its own caption — and `short5`
   chopping Tyler's reply. Bracket-window transcription is not enough; cue times can't
   resolve a word boundary. Every boundary now lands in a measured quiet run (procedure
   in the clipify skill's gotchas), re-verified on the rendered files: 15/16 read ≥8 dB
   below their own body level, and the 16th (`short3`) is word-complete — it ends on the
   decaying /f/ of "wife", 0.03 s before "It" begins.

Loudness and geometry re-verified on v2: I = −16.9 … −18.7 LUFS, TP ≤ −1.45 dBTP,
1080×1920, and video/audio stream durations matching to under 1 ms on all 8.

Upload mechanics: `yt_upload.py` with `publishing/manifest_clips_v2.json` (same titles,
descriptions, tags, playlist and `publishAt` as v1, reordered by publish date so the
soonest-out clip was replaced first); results in
`publishing/manifest_clips_v2.json.results.json`. Brand channel confirmed
(`Permanent Underpod - Podcast`, UCmZ_tUPnopsFJS615b-NtbA). Note: **16 uploads in one
day** (8 + 8) plus playlist inserts and 8 deletes, with no quota error — the
"~1600 units/upload, max 6/day" rule of thumb is very pessimistic.

| Date (2 PM PT) | Clip | Format | Title | Episode ts | URL |
|---|---|---|---|---|---|
| Fri Jul 31 **6 PM PT** | short7-quick-close-it | 9:16 · 0:13 | We're almost down — quick, CLOSE IT 📉 | 51:39 | https://youtu.be/rxXTQV6CMDk |
| Sat Aug 1 | short4-ever-been-a-ripple-guy | 9:16 · 0:15 | Have you ever been a Ripple guy? 🌊 | 34:46 | https://youtu.be/VcK4YeUkVmY |
| Sun Aug 2 | short3-seven-times-one-evening | 9:16 · 0:21 | The baby egg allergy test went badly 🥚 | 22:33 | https://youtu.be/Sea_5hXtt8Q |
| Mon Aug 3 | short6-my-last-name-is-cook | 9:16 · 0:14 | Wait, your last name is actually Cook? 👨‍🍳 | 48:57 | https://youtu.be/wvUSSldQ-hM |
| Tue Aug 4 | short1-nsa-audits-the-crypto | 9:16 · 0:14 | They probably all work for the NSA 🕵️ | 3:41 | https://youtu.be/auQnwEs1Xos |
| Wed Aug 5 | short8-claude-dont-cut-it-out | 9:16 · 0:12 | Claude, don't cut this out 🎙️ | 51:52 | https://youtu.be/FoONooRI6AE |
| Thu Aug 6 | short5-my-agent-only-buys-ripple | 9:16 · 0:09 | My agent only buys Ripple 🤖 | 43:29 | https://youtu.be/LqwTSrZsxPA |
| Fri Aug 7 | short2-give-me-the-crispr-agent | 9:16 · 0:18 | Give me the CRISPR agent, I'm built different 🧬 | 16:50 | https://youtu.be/w8SkPn-I0ts |

**Funnel checklist, manual per clip in Studio once each is public: related video →
episode; pinned comment = `https://youtu.be/hgLne4ec_Ig?t=<seconds>` (exact seconds in the
per-clip copy below); end screens.** This is the channel's weakest metric.

### Per-clip posting copy

**short7-quick-close-it** — https://youtu.be/rxXTQV6CMDk · pin `https://youtu.be/hgLne4ec_Ig?t=3099`
(9:16 · 0:12 · episode 51:39)
- Title:   We're almost down — quick, CLOSE IT 📉
- Caption: We let GPT-5.6 pick a 20x leveraged XRP trade with $101 of real money, and the boys had to panic-close it live on air while saying goodbye. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #crypto #xrp

**short4-ever-been-a-ripple-guy** — https://youtu.be/VcK4YeUkVmY · pin `https://youtu.be/hgLne4ec_Ig?t=2086`
(9:16 · 0:15 · episode 34:46)
- Title:   Have you ever been a Ripple guy? 🌊
- Caption: Tyler asks the question no crypto podcast is brave enough to ask, then diagnoses the condition. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #crypto #xrp

**short3-seven-times-one-evening** — https://youtu.be/Sea_5hXtt8Q · pin `https://youtu.be/hgLne4ec_Ig?t=1353`
(9:16 · 0:19 · episode 22:35)
- Title:   The baby egg allergy test went badly 🥚
- Caption: You're supposed to introduce babies to allergens one at a time to see what happens — here is what happened. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #parenting #dadlife

**short6-my-last-name-is-cook** — https://youtu.be/wvUSSldQ-hM · pin `https://youtu.be/hgLne4ec_Ig?t=2937`
(9:16 · 0:13 · episode 48:58)
- Title:   Wait, your last name is actually Cook? 👨‍🍳
- Caption: Jackson reveals his surname mid-podcast and immediately gets accused of doxxing himself. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #podcast #cooking

**short1-nsa-audits-the-crypto** — https://youtu.be/auQnwEs1Xos · pin `https://youtu.be/hgLne4ec_Ig?t=221`
(9:16 · 0:14 · episode 3:41)
- Title:   They probably all work for the NSA 🕵️
- Caption: Almost nobody on earth can audit a post-quantum cipher — Tyler's take on who those people work for. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #cryptography #ai

**short8-claude-dont-cut-it-out** — https://youtu.be/FoONooRI6AE · pin `https://youtu.be/hgLne4ec_Ig?t=3112`
(9:16 · 0:12 · episode 51:52)
- Title:   Claude, don't cut this out 🎙️
- Caption: The boys sign off by apologizing for the puke talk, then instruct the AI editing the podcast to make it the centerpiece. It did. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #ai #podcast

**short5-my-agent-only-buys-ripple** — https://youtu.be/LqwTSrZsxPA · pin `https://youtu.be/hgLne4ec_Ig?t=2609`
(9:16 · 0:09 · episode 43:29)
- Title:   My agent only buys Ripple 🤖
- Caption: If you let an AI agent shop for you, someone has to decide what it's allowed to buy. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #ai #crypto

**short2-give-me-the-crispr-agent** — https://youtu.be/w8SkPn-I0ts · pin `https://youtu.be/hgLne4ec_Ig?t=1010`
(9:16 · 0:17 · episode 16:51)
- Title:   Give me the CRISPR agent, I'm built different 🧬
- Caption: The case against AI guardrails, argued by two men who would absolutely not be fine. Full episode: https://youtu.be/hgLne4ec_Ig
- Tags:    #shorts #ai #biotech
