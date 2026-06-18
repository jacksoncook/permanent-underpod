# Podcast Episode 2 — Prep Guide
**Record: week of June 22–26, 2026 (target ~June 24–25) · Runtime target: 60 min (record 75–80, edit down)**
**Panel: Jackson (Korea markets) · Chris (stablecoins / DEXs) · Tyler (Bitcoin & Lightning)**

> **Room this time:** Tyler is finally on the couch (Pico recovered) — but **Chris is
> dialing in remotely from a crypto conference.** So the Ep-1 "empty chair" bit didn't
> die, it just *moved*: we still can't get all three of us in one room. Lean into it.
> Not affiliated with any employer.

---

## The Hour at a Glance

| Time | Segment | Lead |
|---|---|---|
| 0:00–4:00 | Cold open — "the empty chair moved" (Tyler's in, Chris is remote from a conference) | All |
| 4:00–6:00 | Housekeeping: we heard you (the 3 Ep 1 tech bugs) | Jackson |
| 6:00–9:00 | Pico update (as promised) | Tyler |
| 9:00–14:00 | The lottery tickets, RESOLVED (ft. Claude, again) | Jackson |
| 14:00–22:00 | News catch-up: BTC drawdown + stablecoin wars (+ Korea hit) | Chris / Jackson |
| 22:00–33:00 | **Main event: Perpetual futures** — overview + the US perps dam breaks | **Chris** |
| 33:00–39:00 | Crypto conferences: the decline, how they've changed, war stories | Chris (live from one) |
| 39:00–45:00 | Permanent-underclass update: Fable 5 (priced out → *yanked*) | All |
| 45:00–53:00 | **Agentic payments: what it is + where it actually gets used** | Chris / Tyler |
| 53:00–59:00 | Contrarian Corner: the saved takes come due | Jackson (+ Tyler) |
| 59:00–60:00 | Outro + Ep 3 tease | All |

*Chris's two segments (perps + conferences) are back-to-back on purpose — keep a remote host's block together so we can power through if his connection gets shaky.*
*Record the cold open LAST (after the outro), cut it to the front in the edit — same as Ep 1.*

---

## 0:00–4:00 — Cold Open + "The Empty Chair Moved"

**Hook line (record last):** *"Last episode our Bitcoin guy phoned it in from a sick dog's bedside, the best AI model on Earth got banned by the government three days after launch, and Washington just made it legal for you to gamble your rent on 50x leverage. This week Tyler's finally on the couch — and Chris is the one phoning in, from a conference. We just cannot get all three of us in a room. Welcome back."*

- **Pay off the Ep 1 cliffhanger:** Tyler's in the third chair ("the Lightning guy showed up to tell us everything we got wrong"). Let him pre-load one grievance.
- **Set up the new running gag:** the empty chair didn't go away, it migrated to Chris — who's beaming in from a crypto conference (tee up the conferences segment; ask what the badge says).
- One line on the premise (won vs. dollar vs. Bitcoin vs. *neither — maybe an AI agent*), then move.

---

## 4:00–6:00 — Housekeeping: We Heard You (Own the Ep 1 Tech Mess)

Self-deprecation is good audio on a young show. Own it fast, don't grovel. Keep to ~2 min.

- **The audio drifted.** First Ep 1 renders had the picture sliding ahead of the sound (two bugs: per-clip frame rounding + concat-demuxer PTS corruption). **Fixed & verified** — 0 irregular video PTS gaps across all 84 min (was 381). One line, move on.
- **The volume was all over the place.** Far-mic/remote was quiet, in-room was loud (~10 LU range). Re-mastered to stable, equal loudness (LRA 8.6 → 6.0, speakers within ~1 LU). *Extra relevant this week — Chris is remote again, so the leveling chain is doing real work; flag for the editor.*
- **The third one we keep forgetting — the captions were desynced.** The subtitle file shipped was cut from the *raw* recording (raw order, raw timing, runs ~2 min long), but the published episode is **reordered + silence-trimmed** — so captions landed on the wrong moments. **Still to fix before Ep 2 ships** (see Production Fixes). On-air: "and the captions were nonsense — also fixed."
- Meta-beat option: "We ship a *podcast-production toolkit* and we still shipped desynced captions. Permanent-underclass behavior."

---

## 6:00–9:00 — Pico Update (As Promised)

We literally said "Pico update next week" on air ("we'll do an update in the subsequent pod on Pico's health"). Deliver it — callbacks are how a new show earns trust.

- Tyler: what happened (woke up the morning of Ep 1, six-year-old Pico was sick), what the vet said, where he's at now. Warm, ~3 min — this is the heart, not filler.
- Callback to "we poured one out for Pico on the couch." If Pico's healthy, **get him on camera this time** (Ep 1: "Pico, want to say hi?" — he didn't). Best Shorts moment of the episode.
- Hand-off: *"Speaking of things we left unresolved last week…"* → the lottery tickets.

---

## 9:00–14:00 — The Lottery Tickets, RESOLVED (ft. Claude, Again)

The biggest open thread from Ep 1, and the origin of the show's name. We scratched **$5 California Scratchers**, fed photos to **Claude (Opus 4.8)**, and Claude (a) misread Tyler's *Cash Crush* as a $6 win when it was a loser, and (b) refused to call one "with any confidence." Then Jackson said the line: **"we've all been earmarked for the permanent underclass — we're never getting out."** That's the band name.

**What's unresolved and needs an on-air verdict:**
- **Tyler — *Cash Crush* ($5):** Claude said $6, then "an 11," then it was a 1. Confirmed **loser.** Did Tyler ever take the consolation "I won $500" ticket into the office? (Running gag.)
- **Jackson — the Spanish *Lotería / Don Clemente* card:** never finished on air (La Bandolina yes, El Mufa no, La Corona…). **Scratch it fully on camera, give the real result.**
- **Pico's ticket — "the one with the heart":** picked *for* Pico, never resolved. **Reveal it.** (If the dog's the only winner, that's the episode's best clip.)
- **Re-run the Claude experiment honestly:** last time we were "only on Opus 48." Re-photograph the tickets, have it call them now, grade it. Did it get prudish again? Ties straight into the Fable 5 segment — the model that *could* read them perfectly is the one that got banned.
- Pocket callback: Chris is Australian ("part of our cultural heritage") — we promised to "talk about Australia's gambling rules." Tee it here, **cash it in the perps segment** (scratchers and perps are the same retail-gambling impulse, different UX).

**Hand-off:** *"From a $5 scratcher to a market where you can put 50x on it — but first, what actually happened in crypto while we were arguing about a Lotería card."*

---

## 14:00–22:00 — The News Catch-Up: BTC Drawdown + the Stablecoin Wars (+ a Korea hit)

**Not a price show** — one sentence of price, then flows/structure/policy. Tyler leads BTC, Chris (remote) leads stablecoins, Jackson takes Korea + macro.

**Bitcoin (Tyler leads):**
- One breath: **BTC ~$65K**, ~48% off the **$126K Oct-2025 ATH**, but **+6%ish on the week** — CoinDesk flagged a possible bottom signal as long-term holders **absorbed ~125,000 BTC in June**.
- The story isn't the number, it's the ETF behavior: ~**$3.4B out in one week** (worst since the 2024 launch). "Patient institutional money" gets its first real stress test — did the ETF institutionalize BTC or just give tourists a faster exit?
- **Strategy sold BTC** — first sale since 2022: **32 BTC for ~$2.5M** (0.0038% of an 843,706 stack) to fund preferred dividends. A rounding error that's symbolically loud ("never sell" was the brand).
- **Treasury companies ~$10B underwater;** Metaplanet's mNAV fell to **~0.90** — the "infinite money glitch" only works *above* NAV. (*Flag: the "$27B" headline refers to a different unnamed firm's worst case — don't conflate.*)
- Overhang: **Mt. Gox** moved 10,422 BTC (~$739M) June 2; ~34,500 BTC left; final repayment deadline **Oct 31, 2026**.

**Stablecoins (Chris leads):**
- **Banks counterattack:** JPMorgan, Citi, BofA (+ Wells Fargo) building a shared **tokenized-deposit network** (target **H1 2027**) to stop deposit flight. Do stablecoins eat the banks, or do the banks absorb stablecoins?
- **GENIUS Act** rules take full effect **July 18, 2026** — and **State Street (June 8) became the 4th Wall St. giant** chasing the reserve float (after BlackRock/Circle, Goldman, BNY). The real business is the T-bill float, not the coin.
- **MiCA transition ends July 1** — **USDT pushed off regulated EU venues** (no completed reserve audit). Two-tier dollar: compliant **USDC** wins the West, USDT keeps emerging markets?
- Stat to land: **USDC out-transacted USDT YTD for the first time since 2019** (~$2.2T vs ~$1.3T), though USDT still leads on market cap (~$143–186B — *cite the range*).

**Korea hit (Jackson, ~90s):** **Kakao opened talks June 16** to form its *own* KRW-stablecoin consortium as the bank blocs splinter — and the **Digital Asset Basic Act stalled past the June 3 elections** into H2 (BOK-vs-FSC fight over whether banks must own ≥51% of any issuer). Korea = the live case study: banks vs. Big Tech vs. central bank.

**Hand-off:** *"Every one of those is a fight about who clears the trade. Chris — the other thing that changed this month is **how** Americans are allowed to make the trade. Perps are legal now."*

---

## 22:00–33:00 — MAIN EVENT: Perpetual Futures (Chris leads, remote)

Teed up in Ep 1 ("I think perps is on the docket"). Chris does the overview, then all three discuss. Timing is perfect: the US just legalized retail perps the same month an on-chain venue started leading price discovery on *oil*.

**The 90-second overview (Chris — jargon rule: say it once, cleanly):**
- A perpetual future = a futures contract with **no expiry**. You hold a leveraged long/short forever.
- The glue is the **funding rate**: longs pay shorts (or vice-versa) every few hours depending on which side is crowded. *Plain-English:* "a bet with no closing bell, and the crowd pays a toll to the other side to keep the bet honest."
- Why anyone cares: **leverage + no expiry + 24/7** = the most-traded product in crypto, and historically the most efficient way retail has ever found to liquidate itself.

**The news that makes this *this week's* segment:**
- **The US perps dam broke.** CFTC approved the first regulated BTC perp (**Kalshi's BTCPERP, ~May 28**); **Kraken** launched CFTC-regulated perps for eligible US traders **June 14** (9 tokens); **Coinbase** became the first FCM cleared to give US traders direct access to global crypto perps **June 11**. Chair Selig: "asset-by-asset," not blanket.
- **The pushback:** Better Markets warned it "endangers retail investors." So — maturation/legitimization, or did Washington hand retail a **leverage bazooka with a federal stamp**?
- **Hyperliquid** hit a record **8.3% of global perp open interest (June 14)**; permissionless **HIP-3** markets (oil, gold, S&P 500, **pre-IPO names**) peaked at **$3.2B OI**; TD Securities says it **priced in ~80% of a WTI crude move before CME reopened**, and **SpaceX perps did $1.4B in a day**. An unregulated on-chain DEX is now a price-discovery venue for *oil*. What happens the first time an exotic HIP-3 market blows up?

**The discussion (all three — where it earns the runtime):**
- **Gambling through-line** (cash the Ep 1 Australia promise): scratchers → perps → prediction markets are the same retail impulse with better UX and more leverage. Chris steelmans "this is just regulated gambling"; Jackson/Tyler prosecute.
- **Bitcoin angle** (Tyler, finally in the room): does a regulated US perp market deepen BTC liquidity, or financialize it further from "be your own bank"?
- **Synthesis to later:** the newest perp trader might not be human — agents can now hold wallets and trade derivatives. Park it; we hit it in the agentic-payments segment.
- *(Where Tyler & Jackson can actually learn perps before recording: see the Recommended Reading appendix.)*

---

## 33:00–39:00 — Crypto Conferences: The Decline, How They've Changed, War Stories

Chris is *at one this week* — that's why he's remote. Use it: he's a **live correspondent on the floor**, not just a panelist. Lead with the live report, then zoom out, then stories.

**Live from the floor (Chris, ~90s):** what's the actual vibe right now — packed or a ghost town? Sponsor booths up or down vs. last year? Who's actually here — builders, institutions, compliance lawyers, or retail degens? What does the swag tell you about the cycle?

**How they've changed (the discussion):**
- **The arc:** 2017 ICO-era hype → 2021 booth-and-yacht excess → today's leaner, builder/institutional/compliance-heavy events. Name the circuit — Consensus, Token2049, the Bitcoin Conference, ETHDenver, Permissionless, Korea Blockchain Week — and how each has shifted tone.
- **The contrarian market-timing thesis:** conference attendance/extravagance is a *trailing* cycle indicator — packed and lavish = near the top, empty and grim = near the bottom. With BTC down ~48% from the ATH, is Chris standing in a bottom signal right now? (Ties the segment to the news + the perps/lottery gambling theme.)
- **Side events > main stage:** the real value migrated to the side dinners, parties, and hallway track — the keynotes are content marketing. Is the conference itself now just an excuse for the side events?
- **The AI migration** (callback to Ep 1's "AI rotation" thread): is the speculative energy, sponsor money, and media oxygen rotating out of crypto conferences and into AI conferences — the same rotation Korean retail made out of crypto into AI stocks?
- **Debate:** are crypto conferences *dying*, or just *professionalizing*? Bullish-maturity read vs. bearish-irrelevance read.

**War stories (each host, ~60s — these make the clips):** the wildest swag, the worst keynote, the most unhinged pitch overheard, the booth that made no sense, the time the "after-party" was the whole point. Tyler can bring the Bitcoin-maxi-conference angle; Jackson the Korea/Asia-circuit angle.

> *Note: keep conference-specific attendance/sponsor numbers to what Chris can confirm live on the floor — we didn't pre-verify hard stats, so don't assert figures on air; the cycle-indicator framing is opinion, label it as such.*

**Hand-off:** *"Speaking of where the money and the hype actually went — the biggest thing in tech this month wasn't at any crypto conference. It was a model that got released and then yanked."*

---

## 39:00–45:00 — Permanent-Underclass Update: Fable 5 (Priced Out → *Yanked*)

The segment the show's *name* is about. The Ep 1 thread was "we're only on Opus 48" and "earmarked for the permanent underclass." It paid off harder than we could have scripted.

**The Fable 5 arc:**
- **June 9:** Anthropic released **Claude Fable 5**, its most powerful public model — at **$10 in / $50 out per 1M tokens**, *double* Opus 4.8 ($5/$25) and the priciest generally-available frontier model it ships.
- It was **included on Pro/Max/Team plans only June 9 → June 22.** As of our record date that window is **closed** — continued use is billed at API rates. Regular users got the best model for **~two weeks**, then got priced out. Tiered AI as a *feature.*
- **The twist — June 12, ~3 days after launch:** the **US government ordered Anthropic to shut off Fable 5 (and the "Mythos" class) worldwide**, tied to a claimed narrow jailbreak around finding software flaws. Anthropic complied but pushed back ("we disagree that a narrow potential jailbreak should be cause for recalling a model deployed to hundreds of millions"). *(Fast-moving — the legal mechanism was still being characterized differently across outlets; frame as reported.)*
- **The bit, fully loaded:** priced out **AND** locked out. "We've all been earmarked for the permanent underclass" → now even people who *could* pay can't, because a government switched it off. And a government can apparently turn off a commercial AI used by hundreds of millions overnight.
- The counter-current (keep it honest): mid-tier AI got *cheaper* the same week (Opus 4.7/4.8 ~67% cheaper than retired Opus 4; Sonnet 4.6 at 1M context). So commodity intelligence is getting cheap while the frontier gets gated and seized — richer in average intelligence, permanently locked out of the top 1% of capability?

**Bridge (one line — don't unpack it here):** the reason this lands on a *payments* show is that token-metered AI labor implies machine-to-machine micropayments. That's the next segment.

---

## 45:00–53:00 — Agentic Payments: What It Is + Where It Actually Gets Used

Flows out of Fable 5 (token-metered AI labor) and perps (agents that trade). Chris leads the stablecoin/x402 side, Tyler the Lightning/L402 side; Jackson plays skeptic + the "card networks co-opt it" angle.

**The overview (90s — jargon rule applies):**
- An **agentic payment** = an AI agent moving money on its own, no human clicking "pay" each time. The agent is the *economic actor*.
- **Why crypto rails, not cards:** AI work is **token-metered**, so agent-to-agent invoices are **tiny and constant** — fractions of a cent, thousands of times a day. Card rails have fixed per-transaction costs that make a half-cent charge uneconomic; stablecoin/Lightning rails were built for it.
- **Why a wallet, not a bank account:** an agent **can't pass KYC** (it's software) but it *can* hold a wallet + a spending policy. Whoever owns the default agent wallet owns a customer that never sleeps and never churns.
- **The plumbing that shipped *this month*** (so nobody fumbles it): **Coinbase "for Agents" (Jun 11)** — agents hold funds, pay, trade, earn yield, native **x402**; **Mastercard "Agent Pay for Machines" (Jun 10)** — multi-rail incl. **stablecoins**, micropayments on Polygon/Solana/Base; **MetaMask Agent Wallet (Jun 8)** — scoped self-custodial signing w/ per-tx threat scanning; **Lightning Labs L402 agent tools** — pay/host paid APIs over Lightning.
- **The rail war in one sentence:** **x402 (Coinbase/Cloudflare + USDC on Base) vs L402 (Bitcoin/Lightning + macaroons) vs the card networks (Mastercard / Visa Intelligent Commerce).**

**The discussion — where do we ACTUALLY see this used? (each host stakes a claim):**
- **Paying for compute / tokens / API calls** — the boring, first real one: an agent pays a metered API or another agent for premium research, data, model access (L402/x402-gated endpoints). *Most credible near-term — Coinbase explicitly pitched "pay for premium research."*
- **Agentic commerce** — the agent buys *for you*: reordering, booking, filling a cart and checking out (Mastercard/Visa/Stripe ACP pitch; the consumer-payments angle).
- **Trading / DeFi agents** — agents holding a wallet and trading spot/perps autonomously (callback to the perps segment + Coinbase for Agents). Highest upside, highest blow-up risk.
- **Content/data metering** — pay-per-call feeds, paywalled APIs, "scrape-but-pay."
- **The honest skeptic line (Jackson):** real machine-to-machine volume today is *negligible* — a 2030 story priced into a 2026 narrative? Force everyone to name the **first boring use case that sticks** (bet: paying for API/compute, not consumer shopping).
- **The risk beat:** an autonomous agent with a wallet is a new attack surface — jailbroken agent drains the wallet, overtrades, gets prompt-injected into paying a scam. Who eats the loss, and does that kill consumer trust before it starts?
- *(Reading on the protocol landscape + this month's launches: see the Recommended Reading appendix.)*

**Hand-off:** *"Whether any of that is real or vapor is the perfect setup for a contrarian take…"* → Contrarian Corner.

---

## 53:00–59:00 — Contrarian Corner: The Saved Takes Come Due

Direct Ep 1 callback: *"Kyler and I will save our contrarian takes."* They're **owed.** Pay up. (Ep 1's Contrarian Corner was Chris's "stablecoins to zero?" — now it's Jackson's and Tyler's turn.)

- **Jackson's contrarian take (he has one) — on AI, Bitcoin, or stablecoins.** ~2 min, then the **steelman rule**: before anyone attacks, one host restates the take in one fair sentence, *then* tears in.
- **Tyler's contrarian take (optional, open invite).** If he's got one, run it the same way. Jackson's is the must-air; Tyler's is the stretch if the clock allows.
- **Fresh ammo / candidate angles** (Jackson picks his own; these are spares):
  - "The ETF *broke* Bitcoin's cycle — record outflows prove it's just a macro beta toy now, not an escape hatch."
  - "Regulated US perps are the top — Washington only blesses retail leverage near the end of a cycle."
  - "USDC winning on compliance is bad: a stablecoin that can be frozen at a regulator's request isn't crypto, it's a bank with extra steps."
  - "Fable 5 getting banned is *bullish* for crypto — the more AI is centralized and switch-off-able, the more valuable un-censorable rails get."
  - **Korea/Jackson special:** "Korean retail rotating into AI stocks is the canary — crypto never gets the retail bid back, and the won stablecoin never beats the dollar ones."
- Bonus round if time: each host delivers the take they *most* disagree with and argues it anyway.

---

## 59:00–60:00 — Outro + Ep 3 Tease

One-sentence takeaway each. Tease Ep 3 from a live thread — e.g. **"Ep 3: the GENIUS Act rules dropped (Jul 18), MiCA kicked USDT out (Jul 1), and we find out if any of us actually paid an AI agent to do something real."** Where to follow. Done.

---

## Numbers to Say On Air

| # | Stat | Value | As of |
|---|---|---|---|
| 1 | BTC price / drawdown | ~$65K, ~48% off $126K ATH | Jun 17 |
| 2 | LTH absorption | ~125,000 BTC bought in June | Jun 2026 |
| 3 | Spot BTC ETF outflow | ~$3.4B in a week (worst since launch) | early Jun |
| 4 | Strategy's first sale since 2022 | 32 BTC / ~$2.5M (0.0038% of stack) | May 26–31 |
| 5 | BTC treasury cos underwater | ~$10B; Metaplanet mNAV ~0.90 | Jun 2026 |
| 6 | Mt. Gox move / deadline | 10,422 BTC ($739M) / Oct 31, 2026 | Jun 2 |
| 7 | Bank tokenized-deposit network | JPM/Citi/BofA/WF, target H1 2027 | Jun 5 |
| 8 | GENIUS Act rules effective | July 18, 2026 | — |
| 9 | MiCA transition ends (USDT pushout) | July 1, 2026 | — |
| 10 | USDC vs USDT transaction volume YTD | ~$2.2T vs ~$1.3T (first since 2019) | 2026 YTD |
| 11 | CFTC US retail perps live | Kalshi ~May 28 · Coinbase Jun 11 · Kraken Jun 14 | Jun 2026 |
| 12 | Hyperliquid global perp OI share | record 8.3% | Jun 14 |
| 13 | Hyperliquid HIP-3 / SpaceX perps | $3.2B OI peak; SpaceX $1.4B/day | Jun 2026 |
| 14 | Claude Fable 5 pricing | $10 in / $50 out per 1M (2x Opus 4.8) | Jun 9 |
| 15 | Fable 5 free-on-plans window | Jun 9 → Jun 22, then API-billed | — |
| 16 | Govt worldwide shutoff of Fable 5/Mythos | ordered Jun 12 (~3 days post-launch) | Jun 12 |
| 17 | Agentic-payments launches | Coinbase Jun 11 · Mastercard Jun 10 · MetaMask Jun 8 | Jun 2026 |

---

## Recommended Reading / Learn More

### Perpetual futures — for Tyler & Jackson (beginner → intermediate)

*Start at the top and stop when it gets too deep; the first three cover everything you need to host the segment.*

**Plain-English (start here):**
- **What Are Perpetual Futures Contracts?** — Binance Academy. Cleanest first read. https://academy.binance.com/en/articles/what-are-perpetual-futures-contracts *(JS-rendered; if it acts up, same article at binance.com/en/academy/articles/what-are-perpetual-futures-contracts)*
- **What are Perpetual Futures?** — Coinbase Learn. Short, jargon-light. https://www.coinbase.com/learn/perpetual-futures/what-are-perpetual-futures
- **Understanding Funding Rates in Perpetual Futures** — Coinbase Learn. The funding mechanism: positive = longs pay shorts, and why it pins perps to spot. https://www.coinbase.com/learn/perpetual-futures/understanding-funding-rates-in-perpetual-futures
- **Perpetual Swap Funding** — Deribit Insights. Exchange-grade funding explainer. https://insights.deribit.com/education/perpetual-swap-funding/

**History / origin (great for color + a smart on-air aside):**
- **Crypto's Greatest Financial Innovation — The Perpetual Swap** — Lucy Labs (Medium). How BitMEX/Arthur Hayes landed on the funding design. https://lucylabs.medium.com/cryptos-greatest-financial-innovation-the-perpetual-swap-1389df0aa05e
- The intellectual ancestor is **Robert Shiller's 1993 "perpetual futures" paper** — search the title ("Measuring Asset Values for Cash Settlement in Derivative Markets"); worth name-dropping that an economist proposed perps decades before crypto.

**Intermediate / quant (if you want the funding-rate math):**
- **A Primer on Perpetual Futures** — Coinbase Institutional Research. Funding from premium index + base rate; the long-spot/short-perp basis trade. https://www.coinbase.com/institutional/research-insights/research/market-intelligence/a-primer-on-perpetual-futures
- **Funding** — Hyperliquid Docs. The actual production funding formula + worked example. https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding

**On-chain landscape (for the Hyperliquid beat):**
- **Perps explained: How Hyperliquid and dYdX are powering the next phase** — 21Shares Research. Best single overview of the perp-DEX landscape. https://www.21shares.com/en-eu/research/perps-explained-how-hyperliquid-and-dydx-are-powering-the-next-phase-of-crypto-trading

### Agentic commerce / payments — reading + this month's news

**Foundational explainers (start here):**
- **How Will My Agent Pay for Things?** — a16z Fintech (the canonical framing: scope/spend authorization, fraud, liability). https://a16z.com/newsletter/agent-payments-stack/
- **What is agentic commerce? A guide to getting started** — Stripe. Merchant-side primer. https://stripe.com/guides/agentic-commerce
- **"Open Agentic Commerce" and the end of ads** — a16z crypto. Provocative thesis: agents can't be shown ads, so open discovery protocols replace ad auctions. https://a16zcrypto.com/posts/article/open-agentic-commerce-end-ads/

**The protocol landscape (the x402 vs L402 vs card-rails fight):**
- **Agentic Commerce: A Guide to L402, x402, and MPP** — Alby (updated Jun 16, 2026). The single best side-by-side comparison — read this one if you read nothing else. https://getalby.com/blog/agentic-commerce-a-guide-to-l402-x402-and-mpp
- **Introducing x402** — Coinbase. The stablecoin/HTTP-402 standard for agents. https://www.coinbase.com/developer-platform/discover/launches/x402
- **L402: Lightning HTTP 402 Protocol** — Lightning Labs docs. The Bitcoin/Lightning agent-payments protocol. https://docs.lightning.engineering/the-lightning-network/l402
- **Agent Payments Protocol (AP2)** — Google Cloud (Intent/Cart/Payment "Mandates," with an x402 crypto extension). https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- **Agentic Commerce Protocol (ACP)** — Stripe + OpenAI (powers Instant Checkout in ChatGPT). https://stripe.com/newsroom/news/stripe-openai-instant-checkout
- **Model Context Protocol (MCP)** — Anthropic. The open standard the agent integrations plug into. https://www.anthropic.com/news/model-context-protocol

**This month's news (May–June 2026):**
- **Coinbase launches AI agent accounts that can trade and spend on your behalf** — CoinDesk, Jun 11, 2026. https://www.coindesk.com/tech/2026/06/11/coinbase-launches-ai-agent-accounts-that-can-trade-and-spend-on-your-behalf
- **Mastercard launches protocol to let AI agents pay each other** — Fortune, Jun 10, 2026. https://fortune.com/2026/06/10/mastercard-ai-payments-protocol-launch-agentic-finance/
- **MetaMask launches AI agent wallet with built-in security** — CoinDesk, Jun 8, 2026. https://www.coindesk.com/tech/2026/06/08/metamask-launches-ai-agent-wallet-with-built-in-security-for-crypto-trades
- **Why L402 Is the Internet-Native Payments Protocol for Agents** — Lightning Labs, Mar 11, 2026 (the "Lightning Agent Tools" release). https://lightning.engineering/posts/2026-03-11-L402-for-agents/

*Sourcing flags: the Mastercard official press-release page may 403 a browser (anti-bot) — the Fortune link covers the same launch; the Binance Academy page is JS-rendered; the Shiller paper is intentionally unlinked (search the title).*

---

## Survival Notes (carry over from Ep 1)

1. **Record 75–80, edit to 60.** Best material comes after minute 20.
2. **One clock owner** with permission to interrupt — this is a packed hour.
3. **One-sentence jargon rule** — first mention of *perps / funding rate / tokenized deposits / HIP-3 / agent wallet / x402 / L402* gets one plain-English sentence, then move.
4. **Record the cold-open hook last.**
5. **Not a price show** — one price sentence per segment max.
6. **Hedge second-tier stats** ("reportedly"): USDT market cap range, the Fable 5 government-shutoff mechanics, post-Jun-22 Fable pricing terms, and any conference attendance numbers.
7. **Tyler in room, Chris remote** — run Chris's two segments (perps + conferences) as a block in case the connection drops; if everyone agrees on a beat, someone argues the absent position.
8. **Get Pico on camera.**

---

## Production Fixes BEFORE Publishing Ep 2 (for the editor)

- ✅ **A/V drift** — pipeline re-stamps video PTS by frame index + byte-concats PCM; verify on a LATE segment (PTS regularity, `frames×1600 == samples`), not just total duration.
- ✅ **Loudness** — `highpass → afftdn → acompressor → loudnorm (dynamic, LRA=5)`; confirm integrated ≈ −16 LUFS, TP ≤ −1, LRA ~5–6. **Extra important: Chris is remote again — a quiet far-mic against two in-room voices is exactly the spread this chain fixes.**
- ⚠️ **Captions (the unfixed one).** Ep 1 shipped `transcript.srt` cut from the **raw** recording — raw order, raw timing (runs to 1:26:12; the final cut is 1:24:17 and **reordered**). Uploaded as-is, captions land on the wrong moments and drift ~2 min long. **Fix:** regenerate the SRT *from the final cut* (re-transcribe the rendered MP4, or remap word timings through `plan.json`'s block order + the silence cuts). **And fix the README** — "Publishing → Captions" currently tells you to upload the raw `transcript.srt`; that instruction is the bug.

---

## Open Threads Carried Into Ep 3

- By Ep 3: did anyone actually *pay an agent / get paid as an agent* for real (not just demo it)?
- GENIUS (Jul 18) + MiCA (Jul 1) outcomes — who did the rules favor?
- Was Chris standing in a cycle-bottom signal at the conference? Revisit if BTC moves.
- The Lightning "does anyone in Seoul actually use it" question (still owed from Ep 1).
- Australia's gambling rules deep-dive (promised; partially cashed in the perps segment).
