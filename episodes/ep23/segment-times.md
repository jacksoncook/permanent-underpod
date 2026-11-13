# Underpod — Ep 23 — Segment Times

**Final cut: 57:19 (raw 64:48) · fully-remote episode, three StreamYard cams plus Jackson's mic as a
separate WAV (muxed onto his cam at +89 ms from the filename start times; offsets 0 / −0.005 / −0.009) and
Chris's screen share of the Perp of Fortune dashboard: full-frame at the reveal, then a persistent top-right
PiP to the end · four-beat 44.5 s cold open · title card · end card · whoosh + gold wipe on all 10
transitions · 24 stat callouts · 13 lower thirds · three LIKE + SUBSCRIBE pop-ups · recorded order kept ·
eight content cuts (7.6 min) · 245 dead-air pauses trimmed (41 s).**

## Episode video

- **URL:** https://youtu.be/6b2yGE4QWg8 — "Jensen Is Out at Nvidia. What Happens to Open Models?" (Jackson's manual upload, live 2026-11-13, drafted description used as-is). Final-cut captions (`standard`) + 15 tags patched via API 2026-11-13 (force-ssl token had been revoked, re-authed).
- **File:** `media/ep23/Underpod - Ep 23 (Final Cut).mp4` (3.08 GB)
- **Thumbnail:** `media/ep23/ep23-thumbnail.png` — "THE CHIP KING IS OUT" (Jackson center at the perp
  reveal, Tyler left mid-laugh in the Avalanche bit, Chris right in the fable-on-the-payroll bit; passed the
  320×180 shrink test).
- **Loudness:** delivered −15.7 LUFS integrated, −2.7 dBTP, LRA 3.9 (Ep 22 chain, target_lufs −11.8 /
  limit 0.7). A/V durations 3438.60 / 3438.61 s.
- **Sync check:** final audio cross-correlated against `edited_raw.mov` at 1:40, 20:00, 40:00, 55:00 and
  57:05 — lag a constant 35 ms at every point (same as Ep 15–22; no drift).
- **LIKE + SUBSCRIBE:** pop-up on frame at 2:05.6, 28:39.1 and 54:48.8, SFX paired in each window. Dashboard
  PiP on frame from 20:39 (full-frame reveal, PiP from 20:47) to the end card.
- **Captions:** `episodes/ep23/transcript-attributed.srt` — regenerated from the FINAL cut.
- **Runtime flag:** 57:19 is 2 min over the 45–55 target and the Perp retainer lands at 20:00, not inside
  the first 10 min. Both follow from keeping the recorded order.
- **Jackson's audio sync is unverified by ear.** His cam file's audio track is digital silence, so the mic
  WAV can't be cross-correlated against it; the 89 ms offset is the StreamYard filename delta only. Sync
  bench on request.

## Title (drafts)

Live title is Jackson's: **Jensen Is Out at Nvidia. What Happens to Open Models?**

1. **Open Models Just Lost Their Champion**
2. Nvidia Without Jensen: Who Fights for Open Models Now?
3. The Chip King Is Out. Now What?
4. Google Is Building Private AI Into Its Chips

## YouTube description (live copy, matches the draft)

```
⏩ The fingerprint claim is at 4:29. Why now at 11:31. NYSE on Avalanche at 15:27. Perp of Fortune at 20:00. Private inference at 21:53. Liquid at 46:52.

Jensen Huang is out at Nvidia, and open models just lost the one person with the clout to champion them. Chris walks through the allegations and the export-control angle, and Tyler explains the blog post claiming you can fingerprint which GPUs a model was trained on, with Kimi K3, DeepSeek V5 and GLM 5.3 all pointing at Blackwells. Does Nvidia's open-model push survive an empty-suit successor, why did this surface now, and who already knew? Then the NYSE picks Avalanche for 24/7 tokenized stocks: Chris, hesitantly, thinks a permissioned chain between friends might finally be a real use case. Perp of Fortune: long Google 20× and Bitcoin down, chosen by random draw, which settles as our first-ever Bitcoin flip win. Google's next TPU bakes in private inference: Tyler on what that means for personal agents, Chris on how you chain privacy end to end, and the private assistant he slapped together in an enclave in under two weeks. Plus the Jensen-era GPU as a collector's item, gear acquisition syndrome, what private inference costs (4 cents in the clear, 15 cents private), and asking one AI to break out of another AI's container. The layer-2 series continues with Liquid, the sidechain that never claimed to be an L2, and Tyler doesn't understand why it still exists.

🔥 On the Agenda
0:00 Cold open
0:49 Jensen is out: open models lose their champion
4:29 The fingerprint: a blog post says China's models trained on Blackwells
7:41 Does Nvidia's open-model push survive him?
11:31 Why now? The timing, and who knew
15:27 NYSE picks Avalanche for 24/7 tokenized stocks
20:00 Perp of Fortune: long Google 20×, Bitcoin down by random draw
21:53 Google's new TPU brings private inference to the cloud
29:17 Chris's private agent, served out of an enclave
31:48 The Jensen-era GPU as a collector's item
35:54 What private inference costs
42:05 The Bitcoin flip settles: our first win
44:19 After-hours perps, Korea, and the $1M perp offer
46:52 Layer-2 series: Liquid, the sidechain that isn't an L2
53:58 Formal verification and Ethereum's social consensus
56:58 Outro

Recorded fully remote, three cameras, one dashboard.
Disclaimers: Our opinions are our own, not our employers'. NOT financial advice. Perp of Fortune is a small real-money account we run for entertainment. Everything said about the Nvidia story is allegation and speculation.

GLOSSARY
• Blackwell: Nvidia's flagship GPU line (B200, B300), barred from export to China. Hopper (H100) came before it.
• Export controls: US rules on which chips can be sold to China; the permitted ones were deliberately slowed.
• Weight fingerprint: the claim that traces of a training run's random starting state survive in the final model and can be matched to hardware.
• TPU: Google's in-house AI chip.
• Private inference: running a model inside a secure enclave so the host can't read your prompt or the answer.
• Secure enclave / TEE: a sealed region of a chip (Intel TDX, AWS Nitro) whose contents the operator can't inspect.
• Attestation: a cryptographic receipt proving which code is running inside an enclave.
• CVM: confidential virtual machine; a server that runs entirely inside an enclave.
• Permissioned L1 / proof of authority: a blockchain whose validators are a fixed, known group.
• Cross-chain messaging: passing messages or wrapped assets between blockchains.
• Sidechain: a separate chain pegged to Bitcoin with no unilateral exit; Liquid's bitcoin sits in an 11-of-15 federation multisig.
• Confidential transactions: Liquid's hidden-amount transfers.
• Formal verification: mathematically proving a program does what its spec says.
• Perp of Fortune: our tiny real-money account; this week +$22.68 on the Bitcoin flip and +$4.28 on a 20× Google long.

🔔 Subscribe for next week: life after Jensen, Perp of Fortune, and the layer-2 series continues.
```

## Chapters

| Time | Segment |
|---|---|
| 0:00 | Cold open (4 beats: Chris "if the interim CEO also had an affair" · Tyler "they have to suck" · Tyler's Jensen-era GPU · Jackson's "21 second countdown for 25 bucks") |
| 0:45 | Title card |
| 0:49 | Jensen is out: the allegations, why he was the champion of open models, Nvidia's own models |
| 4:29 | The fingerprint: Blackwell vs Hopper, the nerfed export chips, DeepSeek's workarounds |
| 7:41 | Does the open push survive him? Everyone builds their own chip; "empty suit CEO number 11"; a thousand reports |
| 11:31 | Why now? The China trip, no expectation of privacy, Megaspeed, 22% of revenue via Singapore |
| 14:46 | What Jensen does next |
| 15:27 | NYSE picks Avalanche: cross-chain messaging, a permissioned L1 between friends, "why couldn't that be a database" |
| 20:00 | Perp of Fortune: long Google 20×, Bitcoin down by random draw, the Vietnamese tree monkey |
| 21:53 | Google's new TPU: private inference, attestation, who the customer is |
| 29:17 | Chris's private agent in a TDX enclave |
| 31:48 | The Jensen-era GPU as a collector's item; gear acquisition syndrome; Jackson's commuter bike |
| 35:54 | What private inference costs: 4¢ vs 15¢ per million, CVM rent, container escapes, prompt injection |
| 42:05 | The Bitcoin flip settles +$22.68, the first win; the Polymarket 50-accounts trick |
| 44:19 | After-hours perps, Korea, the $1M perp offer, the Underpod volatility index |
| 46:52 | Layer-2 series: Liquid (11-of-15 federation, the inflation exploit, recapitalised, "why does it still exist") |
| 53:58 | Formal verification, Ethereum's social consensus, Chris's sell signal |
| 56:58 | Outro |
| 57:12 | End card (life after Jensen · Perp of Fortune · layer-2 series · disclaimer) |

## Cuts to sweep (every splice in the final render)

Final-cut time is where the NEW material starts. `src out → src in` are master-clock seconds (Jackson's
track). Splices sit in measured all-silent gaps (`check_bounds.py`) except the edges pinned with
`hard_m0`/`hard_m1` (cold-open beats, INTRO out, NV_C in, the PERP/TPU seam, AGENT out, LIQ_C out, OUTRO_B),
whispered at both edges in `edited_raw.mov`.

| Final | What | src out → src in |
|---|---|---|
| 0:00.00 | cold open beat 1 (Chris: "if the interim CEO also had an affair"; hard edges) |  → 599.70 |
| 0:10.40 | cold open beat 2 (Tyler: "you can sell chips to China, but they have to suck"; hard edges) | 610.10 → 377.23 |
| 0:23.03 | cold open beat 3 (Tyler: a Jensen-era GPU to have at home; hard edges) | 389.87 → 2088.20 |
| 0:32.43 | cold open beat 4 (Jackson: cheering for Bitcoin down, "21 second countdown for 25 bucks"; hard edges) | 2097.60 → 2776.10 |
| 0:44.53 | title card | 2788.20 →  |
| 0:49.03 | intro, in on "Happy Friday the 13th" |  → 0.05 |
| 0:59.50 | dead-air trim (0.00 s) | 10.50 → 10.50 |
| 1:02.07 | dead-air trim (0.00 s) | 13.05 → 13.05 |
| 1:16.07 | dead-air trim (0.00 s) | 27.05 → 27.05 |
| 1:26.07 | dead-air trim (0.00 s) | 37.05 → 37.05 |
| 1:30.07 | dead-air trim (0.00 s) | 41.05 → 41.05 |
| 1:38.07 | dead-air trim (0.00 s) | 49.05 → 49.05 |
| 1:57.57 | dead-air trim (0.00 s) | 68.55 → 68.55 |
| 2:05.57 | dead-air trim (0.00 s) | 76.55 → 76.55 |
| 2:18.57 | dead-air trim (0.00 s) | 89.55 → 89.55 |
| 2:28.57 | dead-air trim (0.00 s) | 99.55 → 99.55 |
| 2:34.07 | dead-air trim (0.00 s) | 105.05 → 105.05 |
| 2:37.57 | dead-air trim (0.00 s) | 108.55 → 108.55 |
| 2:49.57 | dead-air trim (0.00 s) | 120.55 → 120.55 |
| 2:59.07 | dead-air trim (0.00 s) | 130.05 → 130.05 |
| 3:16.57 | dead-air trim (0.00 s) | 147.55 → 147.55 |
| 3:32.07 | dead-air trim (0.00 s) | 163.05 → 163.05 |
| 3:41.57 | dead-air trim (0.00 s) | 172.55 → 172.55 |
| 4:18.07 | dead-air trim (0.00 s) | 209.05 → 209.05 |
| 4:25.57 | dead-air trim (0.00 s) | 216.55 → 216.55 |
| 4:37.07 | dead-air trim (0.00 s) | 228.05 → 228.05 |
| 4:42.07 | dead-air trim (0.00 s) | 233.05 → 233.05 |
| 5:00.07 | dead-air trim (0.00 s) | 251.05 → 251.05 |
| 5:05.07 | dead-air trim (0.00 s) | 256.05 → 256.05 |
| 5:10.07 | dead-air trim (0.00 s) | 261.05 → 261.05 |
| 5:14.07 | dead-air trim (0.00 s) | 265.05 → 265.05 |
| 5:55.03 | **CUT (50 s)**: the second pass at the fingerprint explanation; in on Chris's "So that's really interesting to me" | 306.03 → 356.33 |
| 5:59.03 | dead-air trim (0.00 s) | 360.33 → 360.33 |
| 6:15.93 | dead-air trim (0.00 s) | 377.23 → 377.23 |
| 6:50.53 | dead-air trim (0.00 s) | 411.83 → 411.83 |
| 6:55.53 | dead-air trim (0.00 s) | 416.83 → 416.83 |
| 7:28.53 | dead-air trim (0.00 s) | 449.83 → 449.83 |
| 7:33.03 | dead-air trim (0.00 s) | 454.33 → 454.33 |
| 7:40.53 | dead-air trim (0.00 s) | 461.83 → 461.83 |
| 7:44.03 | dead-air trim (0.00 s) | 465.33 → 465.33 |
| 7:48.87 | dead-air trim (1.70 s) | 470.15 → 471.85 |
| 7:58.37 | dead-air trim (0.00 s) | 481.35 → 481.35 |
| 8:08.37 | dead-air trim (0.00 s) | 491.35 → 491.35 |
| 8:11.87 | dead-air trim (0.00 s) | 494.85 → 494.85 |
| 8:16.87 | dead-air trim (0.00 s) | 499.85 → 499.85 |
| 8:44.37 | dead-air trim (0.00 s) | 527.35 → 527.35 |
| 8:47.87 | dead-air trim (0.00 s) | 530.85 → 530.85 |
| 9:41.37 | dead-air trim (0.00 s) | 584.35 → 584.35 |
| 9:56.73 | dead-air trim (0.00 s) | 599.70 → 599.70 |
| 10:33.87 | dead-air trim (0.00 s) | 636.85 → 636.85 |
| 10:37.37 | dead-air trim (0.00 s) | 640.35 → 640.35 |
| 10:45.43 | dead-air trim (0.84 s) | 648.41 → 649.25 |
| 10:49.93 | dead-air trim (0.00 s) | 653.75 → 653.75 |
| 10:59.43 | dead-air trim (0.00 s) | 663.25 → 663.25 |
| 11:18.43 | dead-air trim (0.00 s) | 682.25 → 682.25 |
| 11:25.93 | dead-air trim (0.00 s) | 689.75 → 689.75 |
| 11:44.93 | dead-air trim (0.00 s) | 708.75 → 708.75 |
| 11:52.93 | dead-air trim (0.00 s) | 716.75 → 716.75 |
| 12:00.90 | **CUT (36 s)**: the Alaska-summit timing muddle; in on "Think of the timing, like why now?" | 724.70 → 761.10 |
| 12:25.90 | dead-air trim (0.00 s) | 786.10 → 786.10 |
| 12:31.90 | dead-air trim (0.00 s) | 792.10 → 792.10 |
| 12:39.90 | dead-air trim (0.00 s) | 800.10 → 800.10 |
| 12:45.90 | dead-air trim (0.00 s) | 806.10 → 806.10 |
| 12:52.90 | dead-air trim (0.00 s) | 813.10 → 813.10 |
| 13:17.40 | dead-air trim (0.00 s) | 837.60 → 837.60 |
| 13:26.40 | dead-air trim (0.00 s) | 846.60 → 846.60 |
| 14:17.90 | dead-air trim (0.00 s) | 898.10 → 898.10 |
| 14:24.40 | dead-air trim (0.00 s) | 904.60 → 904.60 |
| 14:31.40 | dead-air trim (0.00 s) | 911.60 → 911.60 |
| 14:34.90 | dead-air trim (0.00 s) | 915.10 → 915.10 |
| 14:42.97 | dead-air trim (1.72 s) | 923.18 → 924.90 |
| 15:02.97 | dead-air trim (0.00 s) | 944.90 → 944.90 |
| 15:06.47 | dead-air trim (0.00 s) | 948.40 → 948.40 |
| 15:17.13 | **CUT (105 s)**: "could Jensen start a chip company" speculation; in on "But I guess we'll see" | 959.07 → 1063.79 |
| 15:26.60 | Nvidia → NYSE on Avalanche (block seam, no material removed) | 1073.24 → 1073.24 |
| 15:43.60 | dead-air trim (0.00 s) | 1090.24 → 1090.24 |
| 15:49.10 | dead-air trim (0.00 s) | 1095.74 → 1095.74 |
| 17:19.60 | dead-air trim (0.00 s) | 1186.24 → 1186.24 |
| 17:24.60 | dead-air trim (0.00 s) | 1191.24 → 1191.24 |
| 17:36.07 | dead-air trim (2.07 s) | 1202.71 → 1204.78 |
| 17:41.07 | dead-air trim (0.00 s) | 1209.78 → 1209.78 |
| 17:44.57 | dead-air trim (0.00 s) | 1213.28 → 1213.28 |
| 17:55.57 | dead-air trim (0.00 s) | 1224.28 → 1224.28 |
| 18:03.57 | dead-air trim (0.00 s) | 1232.28 → 1232.28 |
| 18:24.07 | dead-air trim (0.00 s) | 1252.78 → 1252.78 |
| 18:29.07 | dead-air trim (0.00 s) | 1257.78 → 1257.78 |
| 18:35.07 | dead-air trim (0.00 s) | 1263.78 → 1263.78 |
| 18:38.57 | dead-air trim (0.00 s) | 1267.28 → 1267.28 |
| 18:42.57 | dead-air trim (0.00 s) | 1271.28 → 1271.28 |
| 18:47.07 | dead-air trim (0.00 s) | 1275.78 → 1275.78 |
| 18:58.57 | dead-air trim (0.00 s) | 1287.28 → 1287.28 |
| 19:05.57 | dead-air trim (0.00 s) | 1294.28 → 1294.28 |
| 19:16.57 | dead-air trim (0.00 s) | 1305.28 → 1305.28 |
| 19:20.07 | dead-air trim (0.00 s) | 1308.78 → 1308.78 |
| 20:00.10 | NYSE → Perp of Fortune: in on "And abruptly, do we have a perp of fortune" | 1348.80 → 1352.50 |
| 20:11.10 | dead-air trim (0.00 s) | 1363.50 → 1363.50 |
| 20:23.50 | dead-air trim (4.56 s) | 1375.90 → 1380.46 |
| 20:41.00 | dead-air trim (0.00 s) | 1397.96 → 1397.96 |
| 20:46.50 | dead-air trim (0.00 s) | 1403.46 → 1403.46 |
| 20:51.50 | dead-air trim (0.00 s) | 1408.46 → 1408.46 |
| 20:56.50 | dead-air trim (0.00 s) | 1413.46 → 1413.46 |
| 21:00.73 | dead-air trim (1.07 s) | 1417.68 → 1418.75 |
| 21:08.33 | dead-air trim (2.18 s) | 1426.36 → 1428.54 |
| 21:12.70 | dead-air trim (1.69 s) | 1432.90 → 1434.59 |
| 21:17.37 | dead-air trim (1.04 s) | 1439.27 → 1440.31 |
| 21:23.37 | dead-air trim (0.00 s) | 1446.31 → 1446.31 |
| 21:34.87 | dead-air trim (0.00 s) | 1457.81 → 1457.81 |
| 21:53.27 | Perp → Google TPU (block seam mid-phrase, hard edge; Chris muted 0.8 s) | 1476.20 → 1476.20 |
| 22:08.27 | dead-air trim (0.00 s) | 1491.20 → 1491.20 |
| 22:20.27 | dead-air trim (0.00 s) | 1503.20 → 1503.20 |
| 22:28.77 | dead-air trim (0.00 s) | 1511.70 → 1511.70 |
| 22:32.27 | dead-air trim (0.00 s) | 1515.20 → 1515.20 |
| 23:13.77 | dead-air trim (0.00 s) | 1556.70 → 1556.70 |
| 23:17.27 | dead-air trim (0.00 s) | 1560.20 → 1560.20 |
| 23:43.27 | dead-air trim (0.00 s) | 1586.20 → 1586.20 |
| 23:46.77 | dead-air trim (0.00 s) | 1589.70 → 1589.70 |
| 24:30.77 | dead-air trim (0.00 s) | 1633.70 → 1633.70 |
| 24:34.27 | dead-air trim (0.00 s) | 1637.20 → 1637.20 |
| 24:59.27 | dead-air trim (0.00 s) | 1662.20 → 1662.20 |
| 25:04.77 | dead-air trim (0.00 s) | 1667.70 → 1667.70 |
| 25:11.77 | dead-air trim (0.00 s) | 1674.70 → 1674.70 |
| 26:06.77 | dead-air trim (0.00 s) | 1729.70 → 1729.70 |
| 26:46.77 | dead-air trim (0.00 s) | 1769.70 → 1769.70 |
| 26:51.27 | dead-air trim (0.00 s) | 1774.20 → 1774.20 |
| 27:00.17 | dead-air trim (1.26 s) | 1783.09 → 1784.35 |
| 27:09.14 | dead-air trim (2.93 s) | 1793.32 → 1796.25 |
| 27:16.64 | dead-air trim (0.00 s) | 1803.75 → 1803.75 |
| 27:22.50 | dead-air trim (4.15 s) | 1809.61 → 1813.76 |
| 27:37.50 | dead-air trim (0.00 s) | 1828.76 → 1828.76 |
| 27:43.14 | dead-air trim (2.52 s) | 1834.39 → 1836.91 |
| 28:31.14 | dead-air trim (0.00 s) | 1884.91 → 1884.91 |
| 28:37.14 | dead-air trim (0.00 s) | 1890.91 → 1890.91 |
| 28:56.77 | dead-air trim (1.44 s) | 1910.56 → 1912.00 |
| 29:02.27 | dead-air trim (0.00 s) | 1917.50 → 1917.50 |
| 29:08.77 | dead-air trim (0.00 s) | 1924.00 → 1924.00 |
| 29:16.64 | TPU → Chris's private agent (block seam, no material removed) | 1931.88 → 1931.88 |
| 29:32.64 | dead-air trim (0.00 s) | 1947.88 → 1947.88 |
| 29:41.14 | dead-air trim (0.00 s) | 1956.38 → 1956.38 |
| 31:13.14 | dead-air trim (0.00 s) | 2048.38 → 2048.38 |
| 31:17.64 | dead-air trim (0.00 s) | 2052.88 → 2052.88 |
| 31:52.97 | dead-air trim (0.00 s) | 2088.20 → 2088.20 |
| 32:05.14 | dead-air trim (0.00 s) | 2100.38 → 2100.38 |
| 32:10.64 | dead-air trim (0.00 s) | 2105.88 → 2105.88 |
| 32:22.14 | dead-air trim (0.00 s) | 2117.38 → 2117.38 |
| 32:27.14 | dead-air trim (0.00 s) | 2122.38 → 2122.38 |
| 32:34.64 | dead-air trim (0.00 s) | 2129.88 → 2129.88 |
| 32:40.64 | dead-air trim (0.00 s) | 2135.88 → 2135.88 |
| 32:45.64 | dead-air trim (0.00 s) | 2140.88 → 2140.88 |
| 32:54.64 | dead-air trim (0.00 s) | 2149.88 → 2149.88 |
| 33:00.14 | dead-air trim (0.00 s) | 2155.38 → 2155.38 |
| 33:12.64 | dead-air trim (0.00 s) | 2167.88 → 2167.88 |
| 33:23.14 | dead-air trim (0.00 s) | 2178.38 → 2178.38 |
| 33:28.64 | dead-air trim (0.00 s) | 2183.88 → 2183.88 |
| 33:49.64 | dead-air trim (0.00 s) | 2204.88 → 2204.88 |
| 33:58.64 | dead-air trim (0.00 s) | 2213.88 → 2213.88 |
| 34:12.80 | dead-air trim (0.90 s) | 2228.04 → 2228.94 |
| 34:20.80 | dead-air trim (0.00 s) | 2236.94 → 2236.94 |
| 34:29.30 | dead-air trim (0.00 s) | 2245.44 → 2245.44 |
| 34:32.80 | dead-air trim (0.00 s) | 2248.94 → 2248.94 |
| 34:39.80 | dead-air trim (0.00 s) | 2255.94 → 2255.94 |
| 34:43.80 | dead-air trim (0.00 s) | 2259.94 → 2259.94 |
| 34:48.30 | dead-air trim (0.00 s) | 2264.44 → 2264.44 |
| 35:08.30 | dead-air trim (0.00 s) | 2284.44 → 2284.44 |
| 35:20.30 | dead-air trim (0.00 s) | 2296.44 → 2296.44 |
| 35:32.80 | dead-air trim (0.00 s) | 2308.94 → 2308.94 |
| 35:39.30 | dead-air trim (0.00 s) | 2315.44 → 2315.44 |
| 35:46.80 | dead-air trim (0.00 s) | 2322.94 → 2322.94 |
| 35:53.84 | **CUT (62 s)**: the bike-helmet tangent; out after "see how your ass feels", in on Tyler's "Chris, I'm curious, what are the economics" | 2329.98 → 2392.18 |
| 35:57.34 | dead-air trim (0.00 s) | 2395.68 → 2395.68 |
| 36:17.34 | dead-air trim (0.00 s) | 2415.68 → 2415.68 |
| 36:20.84 | dead-air trim (0.00 s) | 2419.18 → 2419.18 |
| 36:39.84 | dead-air trim (0.00 s) | 2438.18 → 2438.18 |
| 36:43.84 | dead-air trim (0.00 s) | 2442.18 → 2442.18 |
| 36:48.34 | dead-air trim (0.00 s) | 2446.68 → 2446.68 |
| 36:51.84 | dead-air trim (0.00 s) | 2450.18 → 2450.18 |
| 37:04.84 | dead-air trim (0.00 s) | 2463.18 → 2463.18 |
| 37:14.94 | dead-air trim (0.86 s) | 2473.27 → 2474.13 |
| 37:21.20 | dead-air trim (1.33 s) | 2480.40 → 2481.73 |
| 37:44.40 | dead-air trim (0.87 s) | 2504.92 → 2505.79 |
| 37:49.40 | dead-air trim (0.00 s) | 2510.79 → 2510.79 |
| 38:11.90 | dead-air trim (0.00 s) | 2533.29 → 2533.29 |
| 38:22.40 | dead-air trim (0.00 s) | 2543.79 → 2543.79 |
| 38:28.90 | dead-air trim (0.00 s) | 2550.29 → 2550.29 |
| 38:39.90 | dead-air trim (0.00 s) | 2561.29 → 2561.29 |
| 38:45.40 | dead-air trim (0.00 s) | 2566.79 → 2566.79 |
| 39:58.90 | dead-air trim (0.00 s) | 2640.29 → 2640.29 |
| 40:05.90 | dead-air trim (0.00 s) | 2647.29 → 2647.29 |
| 40:11.40 | dead-air trim (0.00 s) | 2652.79 → 2652.79 |
| 40:40.40 | dead-air trim (0.00 s) | 2681.79 → 2681.79 |
| 41:04.40 | dead-air trim (0.00 s) | 2705.79 → 2705.79 |
| 41:08.90 | dead-air trim (0.00 s) | 2710.29 → 2710.29 |
| 41:45.90 | dead-air trim (0.00 s) | 2747.29 → 2747.29 |
| 42:09.90 | dead-air trim (0.00 s) | 2771.29 → 2771.29 |
| 42:26.80 | dead-air trim (0.00 s) | 2788.20 → 2788.20 |
| 42:32.90 | dead-air trim (0.00 s) | 2794.29 → 2794.29 |
| 42:44.40 | dead-air trim (0.00 s) | 2805.79 → 2805.79 |
| 42:51.90 | dead-air trim (0.00 s) | 2813.29 → 2813.29 |
| 43:04.40 | dead-air trim (0.00 s) | 2825.79 → 2825.79 |
| 43:08.90 | dead-air trim (0.00 s) | 2830.29 → 2830.29 |
| 43:13.40 | dead-air trim (0.00 s) | 2834.79 → 2834.79 |
| 43:56.40 | dead-air trim (0.00 s) | 2877.79 → 2877.79 |
| 44:00.40 | dead-air trim (0.00 s) | 2881.79 → 2881.79 |
| 44:07.40 | dead-air trim (0.00 s) | 2888.79 → 2888.79 |
| 44:14.40 | dead-air trim (0.00 s) | 2895.79 → 2895.79 |
| 44:22.40 | dead-air trim (0.00 s) | 2903.79 → 2903.79 |
| 44:29.90 | dead-air trim (0.00 s) | 2911.29 → 2911.29 |
| 44:40.90 | dead-air trim (0.00 s) | 2922.29 → 2922.29 |
| 44:45.90 | dead-air trim (0.00 s) | 2927.29 → 2927.29 |
| 44:49.40 | dead-air trim (0.00 s) | 2930.79 → 2930.79 |
| 44:53.40 | dead-air trim (0.00 s) | 2934.79 → 2934.79 |
| 45:08.40 | dead-air trim (0.00 s) | 2949.79 → 2949.79 |
| 45:15.90 | dead-air trim (0.00 s) | 2957.29 → 2957.29 |
| 45:21.40 | dead-air trim (0.00 s) | 2962.79 → 2962.79 |
| 45:32.70 | **CUT (104 s)**: Uniswap price-discovery crosstalk; in on "idea by Tyler, by the way" | 2974.08 → 3078.45 |
| 45:47.07 | dead-air trim (0.81 s) | 3092.80 → 3093.61 |
| 45:54.07 | dead-air trim (0.00 s) | 3100.61 → 3100.61 |
| 46:04.57 | dead-air trim (0.00 s) | 3111.11 → 3111.11 |
| 46:08.07 | dead-air trim (0.00 s) | 3114.61 → 3114.61 |
| 46:20.44 | dead-air trim (1.08 s) | 3126.99 → 3128.07 |
| 46:22.24 | dead-air trim (2.78 s) | 3129.87 → 3132.65 |
| 46:25.74 | dead-air trim (0.00 s) | 3136.15 → 3136.15 |
| 46:29.24 | dead-air trim (0.00 s) | 3139.65 → 3139.65 |
| 46:39.74 | dead-air trim (0.00 s) | 3150.15 → 3150.15 |
| 46:51.70 | Perp → Liquid (block seam, no material removed) | 3162.11 → 3162.11 |
| 46:57.70 | dead-air trim (0.00 s) | 3168.11 → 3168.11 |
| 47:11.30 | **CUT (24 s)**: "what's the point of the liquid segment / we'll just cut this out" meta; in on "Wow Tyler let it flow" | 3181.70 → 3205.48 |
| 47:19.30 | dead-air trim (0.00 s) | 3213.48 → 3213.48 |
| 47:22.80 | dead-air trim (0.00 s) | 3216.98 → 3216.98 |
| 47:30.80 | dead-air trim (0.00 s) | 3224.98 → 3224.98 |
| 47:52.80 | dead-air trim (0.00 s) | 3246.98 → 3246.98 |
| 47:56.30 | dead-air trim (0.00 s) | 3250.48 → 3250.48 |
| 48:31.90 | dead-air trim (0.86 s) | 3286.07 → 3286.93 |
| 50:14.90 | dead-air trim (0.00 s) | 3389.93 → 3389.93 |
| 50:25.40 | dead-air trim (0.00 s) | 3400.43 → 3400.43 |
| 51:18.40 | dead-air trim (0.00 s) | 3453.43 → 3453.43 |
| 51:22.40 | dead-air trim (0.00 s) | 3457.43 → 3457.43 |
| 51:30.40 | dead-air trim (0.00 s) | 3465.43 → 3465.43 |
| 51:37.90 | dead-air trim (0.00 s) | 3472.93 → 3472.93 |
| 51:54.90 | dead-air trim (0.00 s) | 3489.93 → 3489.93 |
| 53:11.47 | dead-air trim (1.81 s) | 3566.49 → 3568.30 |
| 53:34.47 | dead-air trim (0.00 s) | 3591.30 → 3591.30 |
| 53:38.47 | dead-air trim (0.00 s) | 3595.30 → 3595.30 |
| 53:42.47 | dead-air trim (0.00 s) | 3599.30 → 3599.30 |
| 53:57.84 | **CUT (40 s)**: Tyler reading up on Simplicity; in on Chris's formal-verification point | 3614.66 → 3654.73 |
| 54:32.84 | dead-air trim (0.00 s) | 3689.73 → 3689.73 |
| 54:41.84 | dead-air trim (0.00 s) | 3698.73 → 3698.73 |
| 54:55.34 | dead-air trim (0.00 s) | 3712.23 → 3712.23 |
| 55:01.84 | dead-air trim (0.00 s) | 3718.73 → 3718.73 |
| 55:05.34 | dead-air trim (0.00 s) | 3722.23 → 3722.23 |
| 55:11.84 | dead-air trim (0.00 s) | 3728.73 → 3728.73 |
| 55:15.84 | dead-air trim (0.00 s) | 3732.73 → 3732.73 |
| 55:21.34 | dead-air trim (0.00 s) | 3738.23 → 3738.23 |
| 55:27.34 | dead-air trim (0.00 s) | 3744.23 → 3744.23 |
| 55:33.34 | dead-air trim (0.00 s) | 3750.23 → 3750.23 |
| 55:58.34 | dead-air trim (0.00 s) | 3775.23 → 3775.23 |
| 56:03.34 | dead-air trim (0.00 s) | 3780.23 → 3780.23 |
| 56:11.34 | dead-air trim (0.00 s) | 3788.23 → 3788.23 |
| 56:15.84 | dead-air trim (0.00 s) | 3792.73 → 3792.73 |
| 56:23.84 | dead-air trim (0.00 s) | 3800.73 → 3800.73 |
| 56:34.34 | dead-air trim (0.00 s) | 3811.23 → 3811.23 |
| 56:39.84 | dead-air trim (0.00 s) | 3816.73 → 3816.73 |
| 56:44.34 | dead-air trim (0.00 s) | 3821.23 → 3821.23 |
| 56:47.87 | dead-air trim (0.97 s) | 3824.76 → 3825.73 |
| 56:58.00 | **CUT (35 s)**: the post-"pod is complete" ETH/BTC recap; in on "Rock on. Thank you everybody for tuning in" | 3835.85 → 3870.40 |
| 57:11.60 | end card | 3884.00 →  |

## Spotify description (paste-ready draft)

```
Jensen Huang is out at Nvidia, and open models just lost the one person with the clout to champion them. Chris walks through the allegations and the export-control angle, and Tyler explains the blog post claiming you can fingerprint which GPUs a model was trained on, with Kimi K3, DeepSeek V5 and GLM 5.3 all pointing at Blackwells. Does Nvidia's open-model push survive an empty-suit successor, why did this surface now, and who already knew? Then the NYSE picks Avalanche for 24/7 tokenized stocks: Chris, hesitantly, thinks a permissioned chain between friends might finally be a real use case. Perp of Fortune: long Google 20× and Bitcoin down, chosen by random draw, which settles as our first-ever Bitcoin flip win. Google's next TPU bakes in private inference: Tyler on what that means for personal agents, Chris on how you chain privacy end to end, and the private assistant he slapped together in an enclave in under two weeks. Plus the Jensen-era GPU as a collector's item, gear acquisition syndrome, what private inference costs (4 cents in the clear, 15 cents private), and asking one AI to break out of another AI's container. The layer-2 series continues with Liquid, the sidechain that never claimed to be an L2, and Tyler doesn't understand why it still exists.

The fingerprint claim is at 4:29. Chapters: Cold open (0:00) · Jensen is out: open models lose their champion (0:49) · The fingerprint (4:29) · Does Nvidia's open-model push survive him? (7:41) · Why now? (11:31) · NYSE picks Avalanche (15:27) · Perp of Fortune: long Google 20×, Bitcoin down (20:00) · Google's new TPU and private inference (21:53) · Chris's private agent (29:17) · The Jensen-era GPU as a collector's item (31:48) · What private inference costs (35:54) · The Bitcoin flip settles (42:05) · After-hours perps and Korea (44:19) · Liquid, the sidechain that isn't an L2 (46:52) · Formal verification (53:58) · Outro (56:58)

Recorded fully remote, three cameras, one dashboard. Our opinions are our own, not our employers'. NOT financial advice; Perp of Fortune is a small real-money account we run for entertainment. Everything said about the Nvidia story is allegation and speculation. Glossary: Blackwell = Nvidia's flagship GPU line, barred from export to China. Weight fingerprint = the claim that traces of a training run's random starting state survive in the final model. TPU = Google's in-house AI chip. Private inference = running a model inside a secure enclave so the host can't read your prompt. Attestation = a cryptographic receipt proving which code runs inside an enclave. CVM = a server that runs entirely inside an enclave. Permissioned L1 = a blockchain whose validators are a fixed, known group. Sidechain = a separate chain pegged to Bitcoin with no unilateral exit; Liquid's bitcoin sits in an 11-of-15 federation multisig. Formal verification = mathematically proving a program meets its spec. Perp of Fortune = our tiny real-money account; +$22.68 on the Bitcoin flip, +$4.28 on Google this week.

Subscribe for next week: life after Jensen, Perp of Fortune, and the layer-2 series continues.
```

## Captions

`transcript-attributed.srt` regenerated from the FINAL cut (never the raw recording) in
`episodes/ep23/`. Uploaded as the `standard` track 2026-11-13 (`yt_captions.py`). Two cues the
attributor left unlabeled (0:40 and 57:10) set to Jackson by hand from the mic envelopes.

## Production notes

- **Order:** kept as recorded. Nvidia marquee starts at 0:49; Perp lands at 20:00.
- **Content cuts (7.6 min):** fingerprint re-explanation (master 306–356), Alaska timing muddle (725–761),
  "could Jensen start a chip company" (959–1064), bike-helmet tangent (2330–2392), Uniswap price-discovery
  crosstalk (2974–3078), "we'll just cut this out" Liquid meta (3182–3205), Simplicity reading (3615–3655),
  post-"pod is complete" recap (3836–3870).
- **Kept, flagged for Jackson (no compliance cuts per his note):** Tyler's "OpenAI is making Jalapeno"
  (8:30, one incidental mention; OpenAI is a standing off-limits topic), Jackson's "champion of open AI"
  (7:55, means open-source AI), the Ethereum price banter (55:38–56:48), and the jokes about Jensen's
  reports (10:50–11:16) and "Alice Wang" (38:16).
- **Jackson's separate mic:** `SWAG2` WAV delayed 89 ms and muxed onto the cam video as
  `src/jackson_720.mov`; the cam's own audio is digital silence. Mouth-motion lip-sync estimate was noise
  (r ≈ 0.06), so the offset rests on StreamYard filename start times alone.
- **Dashboard share:** `chris-screen` anchored at master 1390.816 (filename delta; the on-screen "20 s"
  countdown matches Jackson's "21 second countdown" within ~1 s). Full-frame 1391.6–1399.0, then the corner
  crop [1010,205,455,222] to the end.
- **Audio:** per-track leveling to gain_target 0.028 from hand-picked gain_spans; `edited_raw.mov` peak
  −0.47 dBFS, no flat samples.
- **Framing:** intro opens solo on Jackson (0.6–10.5) rather than the trio; face centers resampled
  (Jackson 660, Chris 634, Tyler 790).
- **Disclaimer:** none spoken this episode; the end card carries the written one.
- **Plan generator:** `media/ep23/work/mkplan.py` writes `brand.json` + `remote_plan.json`;
  `mk_render.py` writes the sfx/anim/likesub schedule into `render.json`.

## Clips

Not cut yet.
