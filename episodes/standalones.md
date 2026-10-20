# Standalones — evergreen explainers to re-cut as search-intent videos

Built 2026-10-20 from `analytics/study/{blocks,segments}.csv` (relative retention per
chapter, `vs` below; 0.50 = YouTube typical) and the channel's search-traffic pull.
Status lives in the per-item table here until the first one ships; then move to the
publishing sheet.

## Why this lever

- Search is the channel's #2 source (2,008 lifetime views) but today it is novelty
  queries: "fruit fly brain" (35), "will smith eating spaghetti" (19). The only
  Bitcoin how-to queries we rank for are "dice roll seed phrase" (5) and "bip 110" (3).
- Topic-titled episodes pulled 20–30% of views from search (Ep 6, 10, 11, 12, 13, 14,
  19). News-titled Ep 16/17/18 pulled 4–10%. Search follows the title, not the content.
- Long-form pulls already outperformed whole episodes when the title named the topic:
  "AI cloned us… - Ep 4 Clip" 98 views vs Eps 5–7 at 37–55 each.
- Explainer blocks only hold when they have stakes (study §4), so every pick below
  is anchored to a real incident, not a lecture.

## Packaging rules (proposal, confirm or override)

- Title is the search query, phrased as a question or "how X works". **No `- Ep N Clip`
  suffix** (that convention is for pulls; these are standalone videos).
- 8–12 min target. 10–15 s hook from the block's best line, then title card, then the block.
- Description: one-line answer, then "Full conversation: <episode url>&t=<start>", then
  chapters. Playlist: Underpod Clips. Thumbnail: text-forward, the question itself.
- Cadence: one per week, published Tuesday 2 PM PT, so it never collides with the
  Thursday episode or the daily short. Grade at day 7 on search views, not total views.
- This revives long-form pulls, retired 2026-08-14 for shorts. Default: standalones are
  a separate category, shorts stay the only pull format. Jackson to confirm.

## Ranked picks

| # | Standalone title (search query) | Source block | Len | vs | Lead | Edit notes |
|---|---|---|---|---|---|---|
| 1 | How the Lightning Network actually works (and why it can't onboard 7 billion people) | Ep 19 34:26–52:03 | 17.6 → ~11 min | 0.28 | Tyler | Drop Chris "blow up the pod" 41:41–43:13. One "today" at 34:26, trim. Keep the 2-of-2 pot + HTLC walk-through whole. |
| 2 | Will quantum computers break Bitcoin? | Ep 18 9:08–28:39 | 19.5 → ~12 min | 0.39/0.24/0.57 | Tyler | No dated refs. Order: Q-Day vs classical break (14:38) → address reuse exposure → Drake bunker mode (9:08) → Dankrad cleartext internet (24:03) → disclosure (22:42). Cut perp halftime at 28:39. |
| 3 | What is a Bitcoin L2? Lightning vs Spark vs Ark (the unilateral-exit test) | Ep 17 24:46–26:56 + 41:06–44:00, Ep 16 11:49–15:49, Ep 16 36:40–38:29, Ep 19 41:41–43:13 | ~11 min | 0.23/0.53, 0.07, 0.46, 0.23 | Tyler | Standalone from Spark, not a chapter of it. Spine: Tyler's test (can you exit to L1 alone?) from Ep 16 11:49, then Lightning / Spark / Ark one at a time, Ark privacy bit from Ep 16 36:40, Spark 80% haircut from Ep 19. Three source episodes, Ep 17 is a gallery recording: hard cuts, level-match audio. Links forward to #1 and #4. |
| 4 | Spark explained: Lightning without channels | Ep 17 23:06–44:00 | 20.9 → ~12 min | 0.40 | Tyler | Drop the "L2 is" primer (goes to #3) and the Ronin/Wormhole aside 32:04. Privacy block 36:58 is the best-held 4 min (0.75), lead the hook from it. Two "today"s at 23:06/24:46. |
| 5 | The Coldcard bug: how a dice-roll seed phrase went wrong for 5 years | Ep 9 5:16–22:38 | 17.3 → ~12 min | 0.57/0.77/0.49 | Tyler | "dice roll seed phrase" already ranks. Fix "last week" (5:16) and "this week" (17:30). Keep "who was spared" (16:34). Title is close to the parent's; parent has 80 views, fine. |
| 6 | How white hats drained Liquid: federated sidechains explained | Ep 14 37:58–53:56 + Ep 15 31:27–36:08 epilogue | 16 + 4.7 → ~12 min | 0.52 / 0.36 | Tyler | One "next week" at 48:38; the Ep 15 epilogue answers it, so cross-ep stitch is justified. Keep the fee / North Korea-or-teenager beat. |
| 7 | Is Bitcoin anonymous? Chain surveillance, shielded Bitcoin, and Tyler's opsec | Ep 16 29:19–43:52 | 14.5 → ~10 min | 0.46–0.60 | Tyler | Best-held stretch of Ep 16 (parent: 4% search). No dated refs. Open on the Best Buy laptop bit (30:08). |
| 8 | What is MEV? The $15M sandwich bot that got sandwiched, and Jito | Ep 6 9:55–26:47 | 16.9 → ~11 min | 0.43 / 0.27 | Chris | Ep 6 had the channel's best search share (30%). No dated refs. Cut the perp pick 18:26–21:47. Jito half drags; keep to the monopoly point. |
| 9 | How to protect a hardware wallet after the Ledger implant: multisig and vaults | Ep 19 12:58–20:42 | 7.7 min | 0.47/0.38 | Tyler, Chris | Parent is the newest episode; wait 2 weeks so it does not cannibalize. Intro needs 20 s recap of the implant (5:43). |
| 10 | What a secure enclave actually proves (TEEs, attestation, agentic commerce) | Ep 15 47:18–56:22 + Ep 16 17:57–20:16 | 9 + 2.3 → ~9 min | 0.40–0.46 / 0.09 | Chris | Standing topic (prep guide). No dated refs. Lead with "I let Facebook buy my shoes" (58:20). Ep 16 TEE bit is weakly held, optional. |
| 11 | How stablecoin issuers make money: the mint/redeem glitch and the burn desk | Ep 15 22:30–27:49 + Ep 4 53:49–56:55 | 5.2 + 3.1 → ~8 min | 0.31 / 0.33 | Chris | Ep 4 burn desk already a clip (8 views) under a bad title. Two-episode stitch, audio levels differ. Low retention; last of the Bitcoin set. |
| 12 | The 5 levels of AGI (DeepMind) and where ChatGPT sits | Ep 13 5:42–17:38 | 11.9 min | 0.40 | Jackson, Chris | Off-mission (AI) but "AGI" is the one topic title that pulled search (21%, 225 views). "last episode" at 5:42. Table overlays already rendered. |

Skipped: Ep 3 "self-custody won't scale" (15 min, no speaker attribution, early audio),
Ep 11 Bank Secrecy Act (best-held explainer at 0.72 but opinion, weak search),
Ep 4 soul.md clones (0.82 but dated AI gimmick, already a 98-view clip),
Ep 11 mind viruses (dated x2), Ep 12 tokenomics (3 min), Ep 1/2 stablecoin contrarian
pieces (already pulled as clips).

## How to cut one

1. `plan.json` for the standalone: chapters = the block rows above, `cold_open` = the
   hook line, title card from `brand.json`. Reuse `cut_render.py` + `final_render.py`;
   Ep 17 is a gallery recording (per-clip tile crops).
2. `check_bounds.py --plan` (never mid-word), SRT regenerated from the final cut.
3. `yt_upload.py` scheduled-private, title per table, playlist Underpod Clips, 15 tags
   from the query cluster, pinned comment to the parent timestamp.
4. Day-7 grade: search views ≥ 30 or it is a dud; two duds in a row on the same lead
   host → stop the series.
