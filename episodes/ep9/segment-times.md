# Permanent Underpod — Ep 9 — Segment Times (DRAFT — not yet published)

**Final cut: 56:07 · fully-remote episode (three local cams, offsets 0/0/0 —
platform-identical 3338.9 s exports, validated by turn-gap medians; the by-ear
host sync bench was skipped this episode, flag for spot-check) · live Perp of
Fortune dashboard PiP (anchor 2100.78, triple-verified against spoken P&L cues;
corner pip stays up from the reveal to the end card, board closes −$7.54/−8.1%)
· title/end cards · whoosh & gold-wipe on all 10 segment transitions · the
wrench-attack riff is cut per Jackson (master 791.96–853.46, RMS-verified
invisible splice).**

## Episode video

- **URL:** _pending — Jackson publishes (needs a release date/time)_
- **File:** `media/ep9/Permanent Underpod - Ep 9 (Final Cut).mp4`
- **Working title:** The Coldcard Catastrophe
- After publishing: patch tags via API, upload `ep9-final-cut.srt` (regenerated
  from the FINAL cut), backfill this sheet from the live copy via `yt_fetch.py`.
  Expect Jackson's manual upload to revoke the OAuth tokens again.

## Title (draft + alternates)

1. **Do Everything Right, Lose Everything: The Coldcard Catastrophe**
2. The Darkest Day in Bitcoin: One 4-Letter Commit Drained the Coldcards
3. An AI Found the Bug. Then It Found Everyone's Bitcoin.
4. "runs" — The Commit That Broke Bitcoin's Most Paranoid Wallet

## YouTube description (paste-ready draft)

```
Bitcoin's most paranoid hardware wallet — air-gapped, 9-volt-battery-powered, "don't trust, verify" — shipped a broken random number generator for five years, and last Thursday somebody's AI finally noticed. Tyler owned the exact device and walks the whole Greek tragedy: the copyleft license fight that made Coldcard rip out working Trezor code, the 4-letter commit message ("runs") that swapped in the broken RNG, the pseudonymous committer who turned out to be the CTO's alter ego, and why his own coins survived (he rolled dice 100 times like a maniac). Then the uncomfortable part: if frontier models can find these bugs, who gets the frontier models? We stress-test Anthropic's Glasswing program, invent the rent-a-Mythos audit, and game out the extortion equilibrium. Meanwhile Perp of Fortune goes long SK Hynix at 10× in solidarity with Korea's margin-called masses — live dashboard on screen — and the board bleeds out in real time while we argue about whether the frontier labs should stop flexing on us.

🔥 On the Agenda
0:00 Cold open
1:34 The boys are back
2:31 Perp of Fortune: long SK Hynix, 10×
5:16 The Coldcard catastrophe
14:57 The "runs" commit
16:34 Dice rolls & who was spared
17:30 Is self-custody cooked?
22:38 The 2×2 from hell
25:55 Glasswing: who gets the frontier models?
30:36 Rent-a-Mythos: the $200 audit idea
35:54 Perp check-in
38:51 How we're actually doing
40:31 The frontier-model pissing contest
44:49 Is the trajectory still steep?
51:01 Book-scanning for training data
53:27 Distillation poisoning
55:01 Wrap: stay safe out there

Recorded fully remote — three cameras, one live perp dashboard.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment; the Coldcard details are retold from public reporting. If you hold funds on a Coldcard Mk III, move them now.

GLOSSARY
• Coldcard Mk III: the Bitcoin-only, air-gapped hardware wallet for maximalists. Its RNG was broken from March 2021 — seeds were guessable, wallets drained en masse.
• The "runs" commit: thousands of lines swapping working Trezor RNG code for broken in-house code, four-letter commit message, committed by the CTO under a pseudonym. Hindsight is undefeated.
• Copyleft: the license fight — a VC-funded clone used Coldcard's code, Coldcard relicensed to lock them out, and the sloppy migration introduced the bug. No hubris, no bug.
• Dice rolls: mixing your own physical entropy into seed generation. Tedious, paranoid, and the reason Tyler still has his coins.
• Glasswing: Anthropic's partnership program giving ~select orgs access to Mythos-class models. The 2×2: source-viewable × frontier-access — and open source sits in the worst quadrant.
• Kimi K3: the open-weights model the attacker (presumably) pointed at public crypto repos. "Find me a vulnerability and make me a millionaire."
• Astra: the new OpenAI flagship. Ten open math problems, $2,000 in tokens, one annoyed Jackson.
• Perp of Fortune: an LLM picks a leveraged perp with a small real account and we live with it on a live dashboard. This week: long SK Hynix (Korean RAM!) at 10×, in solidarity with Korea's margin-called retail army.

🔔 Subscribe for next week: agentic commerce, finally — for very specific bad reasons.
```

_[FOR JACKSON before publish: the prep guide called for a one-sentence on-air
Block-adjacency disclosure on the Coldcard topic (Block co-published the
root-cause; Bitkey unaffected). It was never said in the recording. Either add
a line to the description disclaimers or record a pickup — your call.]_

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open |
| 1:29 | Title card |
| 1:34 | The boys are back |
| 2:31 | Perp of Fortune: long SK Hynix, 10× |
| 5:16 | The Coldcard catastrophe |
| 14:57 | The "runs" commit |
| 16:34 | Dice rolls & who was spared |
| 17:30 | Is self-custody cooked? |
| 22:38 | The 2×2 from hell |
| 25:55 | Glasswing: who gets the frontier models? |
| 30:36 | Rent-a-Mythos: the $200 audit idea |
| 35:54 | Perp check-in |
| 38:51 | How we're actually doing |
| 40:31 | The frontier-model pissing contest |
| 44:49 | Is the trajectory still steep? |
| 51:01 | Book-scanning for training data |
| 53:27 | Distillation poisoning |
| 55:01 | Wrap: stay safe out there |

## Spotify description (paste-ready draft)

```
Bitcoin's most paranoid hardware wallet — air-gapped, 9-volt-powered, "don't trust, verify" — shipped a broken random number generator for five years, and last Thursday somebody's AI finally noticed. Tyler owned the exact device and walks the whole Greek tragedy: the copyleft license fight that made Coldcard rip out working Trezor code, the 4-letter commit ("runs") that swapped in the broken RNG, the pseudonymous committer who turned out to be the CTO's alter ego, and why his own coins survived (100 dice rolls). Then: if frontier models can find these bugs, who gets the frontier models? We stress-test Anthropic's Glasswing program, invent the rent-a-Mythos audit, and game out the extortion equilibrium. Meanwhile Perp of Fortune goes long SK Hynix at 10× in solidarity with Korea's margin-called masses, and the live board bleeds out while we argue about frontier labs flexing.

Chapters: Cold open (0:00) · The boys are back (1:34) · Perp of Fortune: long SK Hynix 10× (2:31) · The Coldcard catastrophe (5:16) · The "runs" commit (14:57) · Is self-custody cooked? (17:30) · The 2×2 from hell (22:38) · Glasswing (25:55) · Rent-a-Mythos (30:36) · Perp check-in (35:54) · The frontier-model pissing contest (40:31) · Book-scanning & distillation (51:01) · Wrap (55:01)

Recorded fully remote — three cameras, one live perp dashboard. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. If you hold funds on a Coldcard Mk III, move them now. Glossary: Coldcard Mk III = the air-gapped Bitcoin wallet whose RNG was broken from March 2021, seeds guessable, wallets drained. The "runs" commit = the four-letter commit message on the change that broke it, committed by the CTO under a pseudonym during a license-fight code migration. Dice rolls = adding your own physical entropy at seed time; it saved Tyler. Glasswing = Anthropic's program giving select orgs Mythos-class access; the episode's 2×2 puts open source in the worst quadrant. Kimi K3 = the open-weights model the attacker presumably used ("find me a vulnerability and make me a millionaire").

Subscribe for next week: agentic commerce, finally — for very specific bad reasons.
```

## Captions

_Pending: regenerate SRT from the FINAL cut (never the raw cams — Ep 1 desync
rule), upload via captions API after the episode is live (`trackKind` reads back
lowercase; use `token_captions.json` / `youtube.force-ssl`)._

## Edit decisions of note (details in `remote_plan.json` `_notes`)

- **Wrench-attack discourse removed** (Jackson's ask): master 791.96–853.46
  (61.5 s) — Tyler's "you will not succeed in the wrench attack / I can take
  that wrench and turn it back on you", Chris's "don't find me either / it's a
  deterrent", Jackson's "most hidden place" bit, and the tank-top riff. Splice:
  "…no longer have funds on a cold card." → "Yeah, I didn't know all of the
  details about this, Tyler…". Both bounds in measured all-silent union gaps;
  the join gets no whoosh/wipe so it reads as one conversation.
- Reorder: intro ends on the SOS-gesture punchline; the Perp roll moves up to
  2:31 (retainer <10 min per channel analytics); the marquee re-opens on
  Jackson's own "jump straight into a topic" toss; perp banter + check-in
  return after Glasswing, restoring the original "we will transition to another
  segment" seam into the rant.
- Cold open = Kimi K3 heist read + "darkest day in Bitcoin," ending on "Nobody
  could catch it until these amazing models came through." No literal finale
  tease: Tyler's "escape the permanent underclass" line has no clean in-gap.
- Perp dashboard anchor 2100.78, triple-verified against spoken cues (+3.3% ↔
  "we're 3% up"; +$1.51 ↔ "we're at 150"; −$0.09 ↔ "and we're negative.
  Shoot."). Corner pip stays up from the reveal to the end card; the board
  closes −$7.54 / −8.1% under the outro.
- COLD2 runs Tyler-only mic/cam: Jackson's off-topic interjection at 914.7 s
  would read as noise without context.
- **No Block/Bitkey disclosure was spoken on air** (searched all three tracks)
  — flagged above for Jackson before publish.
