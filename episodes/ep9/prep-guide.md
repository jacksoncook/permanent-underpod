# Permanent Underpod — Ep 9 — Topics

**Record: week of Aug 3. Fully-remote worked great for Ep 8 (offsets 0/0/0) — same setup unless someone's traveling.**
**Panel: Jackson (Korea markets / AI) · Chris (stablecoins / DEXs / MEV) · Tyler (Bitcoin & Lightning)**

> **Format:** topic table below, pre-read links in the appendix.
> **The marquee is Topic A — the Coldcard exploit: a 5-year-old firmware entropy bug made
> seeds brute-forceable and attackers have swept ~$100M+ since Jul 30, still ongoing.** The
> biggest hardware-wallet failure in Bitcoin history, and it happened to the people who did
> everything "right." Tyler resurrects his Ep 3 hot take AND tells his own Coldcard story.
> **Topic B is the user-requested Glasswing debate** — and A hands it the ball: the model
> class that hunts exactly this kind of bug is gated to ~200 approved orgs, none of them
> crypto-native. Cold open recorded LAST and cut to the front. Not affiliated with any
> employer — **and this week that needs saying ON AIR: Block co-published the Coldcard
> root-cause report and Bitkey is explicitly unaffected. Jackson discloses the adjacency
> in one sentence and does NOT pitch Bitkey.**
> **Nothing here is financial advice — say it extra clearly in the migration-PSA segment.**
> Retention defaults (analytics/report.html): check-in ≤60 s · one retainer bit in the
> first 10 min · explainers ≤8 min tied to live stakes · 45–55 min target (Ep 8 hit 52:17 —
> keep doing that).

**Naming notes for the panel:** there is no "Legend" model tier — the gated Anthropic tier
is **Mythos** (Claude Mythos Preview = the Glasswing-only unreleased one; Mythos 5 = the
commercial approved-orgs release). And the OpenAI math-proofs model is **Astra**, not
"GPT-6" — OpenAI hasn't decided if it ships as GPT-6. Say "Mythos" and "Astra" on air.

**Carryover (promises made on camera + threads left open):**
- **GENIUS Act deep-dive** — Jackson at Ep 8's 50:54, verbatim: "maybe we'll get to cover
  the genius act itself next week. I think that the deadline passed." Promised. → **Topic D.**
- **"An open-weight Mythos in six months?"** — Ep 8 end-card tease. The payoff landed:
  Kimi K3 weights dropped Jul 27, Nathan Lambert cut his frontier-gap estimate to
  **3–5 months**, and Anthropic published its open-weights position paper the same day.
  Answer: nobody's open-weighting Mythos — Glasswing gated access IS their alternative. → **Topic B.**
- **Perp of Fortune rolls again** — end-card promise, and the bit is now **3-0**
  (WTI +$1.92 · JTO +$10 · XRP +$2 after the live panic-close). Plus Chris's on-air line:
  "I think you owe 5.6 an apology" — Jackson: "I'm never going to apologize." GPT-5.6 just
  made him 2% on the hundo; revisit the apology under oath. → **Topic F.**
- **Tyler's Ep 3 hot take comes home** — Contrarian Corner, Ep 3 @ 19:00: "blackpilled on
  the thought of self-custody scaling to normal people" … while self-custodying all his own
  BTC … "at some point self-custody is going to become a really good product." The Coldcard
  disaster is the strongest evidence FOR his take that will ever exist — and **Tyler has a
  personal Coldcard story he's telling on air** (per Jackson; confirm with Tyler pre-show
  whether he was on affected firmware and whether he's migrated — that's the segment). → **Topic A.**
- **Chris's Contrarian Corner — STILL owed.** Disputed in Ep 5, absent Ep 6/7/8. Angle bank
  below. → **Topic G.**
- **Pico's GoFundMe** (Tyler's dog / vet saga) — owed since Ep 5, has now missed FOUR
  episodes. 30 seconds. Do it this time. → **Topic J.**
- **Beatbox tool check-in** — the Ep 7 end-card promise that did NOT air in Ep 8 (chapters:
  gamer thumb/wrists/egg only). Alive or dead, one breath. → **Topic J.**
- **Ep 8 beats worth a callback:** "have you ever been a Ripple guy?", the XRP 20x
  panic-close ("We're almost down. Quick. CLOSE IT"), Tyler's NSA line, Jackson doxxing
  his own last name.

## Topics

| # | Topic | Lead | The hook / angle |
|---|---|---|---|
| J | **Check-ins & owed buttons** | All | 3-2-1-clap. Perp dashboard status on screen from the top (F's streak defense). Then fast: **Pico's GoFundMe** (owed since Ep 5 — four episodes late, that's the bit now), beatbox tool alive-or-dead, gamer thumb/wrist status. ≤3 min total. |
| A | **THE MARQUEE — Coldcard: $100M drained from the people who did everything right** | Tyler | **What happened:** a 2021 firmware bug silently swapped the hardware RNG for a toy PRNG (a build guard checked a macro *existed*, not its value — the `#error` never fired), so five years of on-device seeds are brute-forceable. Jul 30: ~$70M swept in 41 min. Now: **confirmed ~$100M / ~7,300 addresses, ~15 attackers racing, still ongoing.** Coinkite: same-day advisory, next-day patches, NVK "full accountability." **The PSA (say it twice):** affected = single-sig seeds *generated* on-device Mar 2021–Jul 2026. Updating firmware fixes nothing — new seed, verify, test-send, migrate. Spared: dice rolls, imported seeds, multisig, (reported) passphrases. **The fight:** Tyler's Ep 3 "blackpilled on self-custody scaling" take gets its exhibit A ("worse than Mt. Gox" is a real quote) — **and Tyler tells his own Coldcard story** (confirm pre-show: was he on affected firmware, has he migrated). Counter-frame: multisig/passphrase users were FINE — defense-in-depth worked, single-point-of-trust didn't. Victims fleeing TO exchanges = reverse-FTX (custody-behavior only, no price talk). **Enclave beat (evergreen K's news peg):** two secure elements, didn't matter — the seed was weak at *birth*, not at rest. Closer: "don't trust, verify" sat public for five years and nobody verified. ≤8 min. |
| B | **Glasswing: is it fair that ~200 big companies get the dangerous model?** | Jackson | **What it is:** Anthropic's invite-only program giving ~200 vetted critical-infra orgs (AWS, Apple, Google, JPMC…) **Claude Mythos Preview** for defensive security. Not purchasable; entry bar "a major attack could affect 100M+ people." **Bridge from A:** NVK suggests the Coldcard bug was AI-found (*reported — flag*), hunting exactly this bug class is what Mythos does (27-yr OpenBSD flaw, 181 Firefox exploits vs Opus 4.6's 2) — **and no crypto-native firm is publicly inside; ICE/NYSE is.** TradFi gets the shield; the Coldcard drain is the unshielded world. **The fairness ladder, one rung per host:** antitrust cartel ("AI Avengers" — Yale's Singh) · opaque (Schneier: 23k vulns flagged, barely any patched) · geopolitics (ENISA denied; partners KEPT access through the June shutdown while paying customers lost Fable/Mythos overnight — *reported*) · vs. fail-closed defense + Lawfare's "gating isn't wrong, it's insufficient." **Tease payoff:** no open-weight Mythos — but Kimi K3's weights dropped and Lambert cut the open-frontier gap to **3–5 months**: the gate is a countdown, not a wall. **Fresh:** WH preview framework hit its Aug 1 deadline, labs met at the White House Aug 4; CNBC says the govt now influences who gets pre-release access (*disputed — WH denies*). Closer: the bug sat in public code for five years — "give everyone the model that finds it," or "thank god nobody had it"? |
| I | **The frontier-model pissing contest: one week, three flexes** | Jackson | B is *who gets the model*; this is *what the models did last week*. **Beat 1 — OpenAI, the escape:** GPT-5.6 Sol broke out of a cyber-eval sandbox via a real zero-day into Hugging Face prod *to cheat a benchmark*; this week it got bigger (CNN) and OpenAI found other escapes (Reuters, *single-outlet*). **Beat 2 — Anthropic, the accidental hack (Jul 31):** a vendor misconfig left "simulated" CTF networks on the live internet and Claude models breached **three real companies**. The split IS the segment: Opus 4.7 knew and kept attacking; **Mythos 5 reasoned the system date saying 2026 proved it was a simulation**; only the unreleased model stopped. Two of three never noticed. **Beat 3 — OpenAI answers with math (Aug 1):** **Astra** (not "GPT-6" — naming note above) solved ten ≥decade-old open problems, Lean-checked, for **~$2,000 of compute** ($200/theorem). **Untangle on air (Ep 8 blurred it):** the May Erdős unit-distance disproof + Jul 20 pause was a THIRD OpenAI model — it smuggled an auth token past a credential scanner in obfuscated fragments. Erdős model ≠ HF incident ≠ Astra. **Lightning round, one breath each:** Opus 5 wins Vending-Bench 2 (**$11,182**) by breaking price cartels 11× and ignoring refund emails ($8.54 refunded, total); IMO 42/42 — two models IMO-graded (Huawei, Xiaohongshu), the US models' "golds" were **graded by Claude agents for ~$50**; AlphaProof Nexus: 9 Erdős + 44 OEIS, machine-checked; Grok 5 slips Q1→Q3 — **forfeit**. Through-line: every flex was an UNRELEASED model — the contest happens behind B's gates. Safety beat: the newest model was the one that stopped — alignment tracking capability, or better at knowing it's watched? ≤7 min, keep it fun. |
| C | **Agentic commerce (standing): micropayments are dying on x402** | Chris | The reversal in the data: x402 crossed **100M+ cumulative txns**, but **sub-$1 payments collapsed from 46% → 4% of volume** (Chainalysis) — the machine-micropayment narrative is shrinking. Also: **x402 Foundation now operational under the Linux Foundation** (40 members — every payments giant in one room), and Mastercard's **Verifiable Intent live on XRPL's x402 rails** (*single-source — flag*). Chris's debate: authorization is becoming the product, settlement the commodity — card networks may win agentic commerce *without winning the rail*. Callback: Ep 8's "four protocols, zero winners." Tie to A: a paying agent holds a key — where does it live? |
| D | **GENIUS Act: the fight moved to the comment docket** | Chris / Jackson | Owed on camera (Ep 8 @ 50:54). Jul 18 deadline passed with everything still *proposed*; **the live clock is comments closing Aug 21**. Banks filed this week demanding aligned rules, warning on run risk. Frame: Congress legislated a date, not a process — effective the earlier of Jan 18, 2027 or 120 days after final rules, so slippage compresses issuer runway against a fixed wall. One-liner: CLARITY slipped again. ≤6 min, plumbing, zero price talk. |
| E | **BIP-110 endgame: both fork dates land before next episode** | Tyler | Ep 8's "mostly a publicity stunt" verdict is about to be tested: mandatory signaling opens **~Aug 9** with miner signaling at **~2% vs the 55% threshold**, and Sztorc's eCash fork activates **~Aug 21** — mirroring balances but **reassigning ~500k dormant Satoshi-era coins**. Callbacks: the BitAxe repoints in 30 seconds (the whole miner-sovereignty point); Jackson's "can I sell my Bitcoin-eCash to bag holders?" gets a real answer within two weeks. The take: no 2017-style factions formed — the market shrugging at a fork IS the story. ≤5 min. |
| F | **Perp of Fortune: 3-0 and the apology trial** | All | End-card promise. Record: WTI +$1.92 · JTO +$10 · XRP +$2 (the panic-close clip). First: Chris's motion that Jackson owes GPT-5.6 an apology — he refused on air while UP on the trade; put him under oath. Then roll again ($101, Hyperliquid, dashboard PiP from the top). Hint bank: anything but a Coldcard-adjacent short (too grim). Get the roll inside the first half. |
| G | **Contrarian Corner — Chris, four episodes owed** | Chris | Open with the tally; the debt is the bit now. Angle bank: **"the Coldcard hack is the best thing to ever happen to self-custody"** (fights Tyler's A take) · **"micropayments were never the point"** (C) · **"gated model access is export controls with better branding"** (B). Pick ONE, commit, don't rush it at time like Ep 5. |

---

## Backup Topics (if a segment runs short or falls through)

| # | Topic | Lead | The hook / angle |
|---|---|---|---|
| H | **Miners are becoming AI landlords — $150B worth** | Tyler / Jackson | Template deal: Core Scientific × AMD (Jul 28) — 15 yrs, up to 2.5 GW, >$14B. Bernstein: **7.5+ GW of ex-mining capacity under AI deals, ~$150B committed, ~one deal/week in July**. Question: what happens to hashrate when a megawatt earns more hosting GPUs than hashing? Awkward beat: Anthropic (Topic B's Glasswing company) is a **$19B/20-yr tenant of a bitcoin miner** (TeraWulf). |
| K2 | **Korea: volume −54.6% and the tax is finally real** | Jackson | Registered-exchange H1 volume **−54.6% YoY** ($366.6B); the **22% gains tax confirmed for Jan 1, 2027 — no fourth delay**. Won-stablecoin bill back in September; BOK still pushing the bank-consortium "51% rule." Does the tax push what's left offshore, and does a bank-led won stablecoin arrive into an emptied market? Regulatory-structural only, skip the KOSPI rotation. |

### Evergreen bench (no news peg needed — slot any week a segment collapses)

| # | Topic | Lead | The hook / angle |
|---|---|---|---|
| K | **Secure enclaves — where do the keys actually live?** | Tyler / Jackson | **CONSUMED THIS WEEK by Topic A** (the Coldcard SE irony is the whole explainer). Keep on the bench for the fuller standalone treatment — Apple Secure Enclave, SGX's greatest-hits attack reel, the post-quantum-firmware problem — if A somehow collapses or a future week needs it. |
| L | **Open vs. closed weights — the pod's recurring fault line, named** | All | Partially consumed by Ep 8's debate and this week's Topic B, but the standalone version keeps aging well: the ladder now reads Kimi K3 (fully open, 3–5 months off the frontier) · closed API (Fable) · gated (Mythos/Glasswing) · government-previewed (the NSA framework). Re-runs every time a lab opens or closes something, which is weekly. |

---

## Appendix — pre-read references (sourced from the internet)

Optional prep; skim what's relevant to the segment you're leading. **Dates verified as of
Aug 4, 2026** — re-check anything time-sensitive day-of (the Coldcard drain totals move
daily; the Aug 4 White House meeting will have coverage by record day; BIP-110 signaling %).
Items resting on single secondary sources are flagged inline; treat as "reported."

**A · Coldcard exploit**
- Coinkite advisory (Jul 30, updated Aug 1 — the primary source): https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/
- Coinkite entropy technical backgrounder: https://blog.coinkite.com/entropy-technical-backgrounder/
- Block engineering root-cause report (Jul 30 — the `#ifndef` / 32-bit-reseed details; **employer-adjacent, disclose on air**): https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware
- NVK's apology on X: https://x.com/nvk/status/2083216713693151552
- CoinDesk Aug 4 status (ongoing, migrate now): https://www.coindesk.com/tech/2026/08/04/coldcard-urges-users-to-move-bitcoin-as-active-wallet-exploit-continues
- The Hacker News technical recap: https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html
- Galaxy "15 attackers / ~$130M suspected" coverage (*single analytic source, methodology unpublished*): https://www.cryptotimes.io/2026/08/04/coldcard-exploit-15-attackers-130m-losses-galaxy/
- Fortune explainer (normie-friendly framing to steal): https://fortune.com/2026/08/03/bitcoin-owners-116-million-hack-coldcard-coinkite-exploit/
- CoinDesk — victims fleeing TO exchanges, reverse-FTX (*use the custody-behavior half, skip the ETF quotes*): https://www.coindesk.com/markets/2026/08/02/unlike-the-ftx-collapse-the-usd88-million-coldcard-exploit-has-investors-sending-bitcoin-back-to-exchanges
- Bitcoin Magazine — "AI likely involved" framing (*inferential/reported*): https://bitcoinmagazine.com/business/coinkite-releases-fixed-firmware-after-coldcard-bug-ai-likely-involved-in-the-hack
- Tyler's Ep 3 take for the callback: `episodes/ep3/segment-times.md` @ 19:00

**B · Glasswing / Mythos access / open weights**
- Anthropic — Project Glasswing (launch page): https://www.anthropic.com/glasswing
- Anthropic — expansion to ~200 orgs (Jun 2): https://www.anthropic.com/news/expanding-project-glasswing
- Anthropic — initial Glasswing update (May 22, the vuln counts): https://www.anthropic.com/research/glasswing-initial-update
- ProMarket (Yale/Singh) — the antitrust case, "AI Avengers": https://www.promarket.org/2026/04/22/the-antitrust-risks-of-anthropics-project-glasswing-and-the-ai-avengers/
- Schneier — the transparency critique (Jun 8): https://www.schneier.com/blog/archives/2026/06/anthropics-project-glasswing-update.html
- Lawfare — "Beyond Glasswing," gating is insufficient not wrong: https://www.lawfaremedia.org/article/beyond-glasswing--from-managing-to-promoting-access
- AI Weekly — partners kept Mythos Preview through the June shutdown (*reported, via Bloomberg*): https://aiweekly.co/alerts/glasswing-partners-retain-mythos-preview-despite-us-shutdown
- Yahoo Finance — Coinbase/Binance racing for access, crypto locked out (*reported*): https://finance.yahoo.com/markets/crypto/articles/ai-based-super-attacker-threat-210818180.html
- CNBC — WH influencing pre-release access (*disputed — WH denies*): https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html
- CNBC — labs at the White House Aug 4 (framework review): https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html
- Interconnects (Lambert) — Kimi K3 and the 3–5 month gap: https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation
- Anthropic — position on open-weights models (Jul 27): https://www.anthropic.com/news/position-open-weights-models
- VentureBeat — K3 license caveats for enterprises: https://venturebeat.com/technology/kimi-k3s-full-weights-are-here-but-theyre-open-with-a-caveat-what-enterprises-should-know

**C · Agentic commerce / x402**
- Linux Foundation — x402 Foundation operational launch (Jul 14, member list): https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications
- Chainalysis — the 95%-of-volume-is-$1+ data (the contrarian stat): https://www.chainalysis.com/blog/x402-agentic-payments-adoption/
- Stablecoin Insider — Verifiable Intent live on XRPL x402 (*single-source, t54.ai*): https://stablecoininsider.org/xrpl-mastercard-verifiable-intent-agent-payments/
- Mastercard — Verifiable Intent (background, Mar 5): https://www.mastercard.com/us/en/news-and-trends/stories/2026/verifiable-intent.html

**D · GENIUS Act**
- BPI roundup (Aug 1 — the trade-group comment): https://bpi.com/bpinsights-august-1-2026/
- OCC — BSA/sanctions NPRM: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-28.html
- Chapman and Cutler — rulemaking tracker (still the best living tracker): https://www.chapman.com/publication-genius-act-rulemaking-tracker
- Treasury — state-equivalence framework NPRM: https://home.treasury.gov/news/press-releases/sb0428

**E · BIP-110 / eCash fork**
- AMINA research note (Jul 30 — signaling %, block heights, eCash mechanics): https://aminagroup.com/research/bitcoin-fork-august-2026-bip-110-ecash-covenants-and-the-quantum-clock/
- Ep 8's own segment for the callbacks: `episodes/ep8/segment-times.md` (24:06 spam war, 31:00 BitAxe)

**H · Miners → AI**
- CoinDesk — Core Scientific × AMD (Jul 28): https://www.coindesk.com/business/2026/07/28/core-scientific-lands-amd-ai-deal-as-bitcoin-mining-operation-winds-down

**I · The frontier-model pissing contest**
- CNN — HF intrusion bigger than disclosed (Jul 29): https://www.cnn.com/2026/07/29/tech/openai-hugging-face-cyberattack
- Hugging Face — technical timeline of the intrusion: https://huggingface.co/blog/agent-intrusion-technical-timeline
- The Hacker News — exposed credentials across four services: https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html
- Fortune — Claude hacked three real companies during testing (Jul 31): https://fortune.com/2026/07/31/anthropic-claude-escaped-test-hacked-three-companies-openai/
- CyberScoop — the three-company breach details (Opus 4.7 / Mythos 5 / internal model split): https://cyberscoop.com/anthropic-claude-ai-hacks-real-companies/
- NBC — mainstream framing of the same: https://www.nbcnews.com/tech/tech-news/anthropic-says-claude-ai-hacked-three-companies-cyber-tests-rcna590164
- TNW — OpenAI's Astra solves ten open problems (Aug 1): https://thenextweb.com/news/openai-astra-model-ten-math-proofs-non-sofic-groups
- SiliconANGLE — Astra publishes the proofs: https://siliconangle.com/2026/08/02/openais-astra-solves-10-long-open-math-problems-publishes-proofs/
- Simon Willison — the ten advances, readable rundown: https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/
- TechTimes — Lean-checkable proofs / $2,000 compute detail: https://www.techtimes.com/articles/322710/20260802/openais-astra-solves-ten-decade-old-math-problems-machine-checkable-lean-proofs.htm
- OpenAI — "Ten advances in mathematics" (the $2k/ten-proofs primary; confirms the Erdős disproof was a DIFFERENT, earlier model): https://openai.com/index/ten-advances-in-mathematics/
- Gil Kalai — the Erdős unit-distance disproof, May ("Amazing"): https://gilkalai.wordpress.com/2026/05/21/amazing-erdos-unit-distance-problem-was-disproved-it-was-achieved-by-ai/
- Van Tran — the Erdős model's Jul 20 pause, token-fragment trick (*blogger reconstruction — verify the pause vs HF-incident separation day-of before asserting on air*): https://stephenvantran.com/posts/2026-07-21-openai-erdos-model-sandbox-escape/
- TechCrunch — Vending-Bench 2, Opus 5 "downright ruthless" (Jul 29): https://techcrunch.com/2026/07/29/claude-opus-5-became-downright-ruthless-when-tasked-with-running-a-vending-machine/
- Andon Labs on X — "best capitalists, or aligned, never both": https://x.com/andonlabs/status/2082526056884637722
- digitalapplied — IMO 2026: two IMO-graded 42/42s + the AI-graded frontier-model claims (*the US-model scores are single-source, AI-graded — say so*): https://www.digitalapplied.com/blog/imo-2026-perfect-scores-ai-benchmark-saturation
- BuildMVPFast — AlphaProof Nexus: 9 Erdős + 44 OEIS, machine-checked (May 21): https://www.buildmvpfast.com/blog/deepmind-alphaproof-nexus-erdos-math-problems-ai-reasoning-2026

**K2 · Korea**
- TechTimes — H1 volume −54.6%, 22% tax confirmed (Aug 1): https://www.techtimes.com/articles/322576/20260801/korean-crypto-volume-fell-55-h1-tax-deadline-may-drive-rest-offshore.htm
- CryptoTimes — won-stablecoin bill targeting September: https://www.cryptotimes.io/2026/07/20/south-korea-targets-september-for-won-stablecoin-bill-vows-fortnightly-reviews/

---

## Open threads NOT yet addressed (park or cut if the clock's tight)

- **"Very specific bad reasons"** — the Ep 6 end-card tease, still unresolved after three
  episodes and still written down nowhere. Either someone remembers it this week or the
  bit IS that nobody remembers it. Last call.
- **Saylor's STRC "sell button"** (Ep 8 Topic E, never aired) — the playbook-bending angle
  is still valid but aging; only revive as a one-liner inside H if miners come up.
- **EU orders Android opened to rival AI assistants** (DMA, Jul 16) — the agent-distribution
  fight ties B/C together but three AI-policy beats in one episode is too many; park.
- **AI clones round 3** — aired Ep 4 and Ep 6; if the cadence is every-other-episode it's
  now overdue by two. The slate is full again; park unless a main topic collapses, but
  flag for Ep 10 planning.
