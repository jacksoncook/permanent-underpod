# Permanent Underpod — Ep 6 — Topics

**Record: next up after Ep 5. Format TBD (Ep 5 was fully remote — the "three laptops,**
**two crashes" run; decide in-person vs. remote on the day and set the pipeline accordingly).**
**Panel: Jackson (Korea markets) · Chris (stablecoins / DEXs / MEV) · Tyler (Bitcoin & Lightning)**

> **Format:** topic table below, pre-read links in the appendix.
> **The two anchors — AGENTIC COMMERCE and MEV — are the on-camera promises from Ep 5's**
> **sign-off** (Tyler: "Maybe MEV… something you'd pitched earlier"; Jackson: "we still need
> to talk about agentic payments, it's important"). Land them both — agentic commerce is the
> thread we've teased since Ep 1 and never put on air.
> Cold open recorded LAST and cut to the front. Not affiliated with any employer.
> **Nothing here is financial advice.**

**Carryover from Ep 5 (promises made on camera + threads left open):**
- **Agentic payments** — Jackson closed Ep 5 with "we still need to talk about agentic
  payments… it's important." This is the marquee. (Teased since Ep 1, landscaped in Ep 4
  Topic A, backup-only in Ep 5.) → **Topic A.**
- **MEV** — Tyler's explicit Ep 6 pitch at the sign-off. → **Topic B.**
- **Gamer thumb saga → WEEK 4.** Ep 5 status: brace **OFF** (Chris's elite split keyboard
  isn't brace-compatible, so he took it off to hit alt — "this is why you have gamer thumb,
  Chris"). Quick check-in, don't let it eat the clock. → **Topic J.**
- **Perp of Fortune.** Ep 5 closed the Fable-picked LONG WTI crude (20x, $100) at **~+$1.92
  ("best we've ever done")** — position closed on air. Open hooks for the callback: **Tyler
  owes "a hundo next time"** (promised ~46:40), and the running joke that they *should* have
  "perped into Bonk" / longed the BonkDAO hacker's "Bonk 2.0." → **Topic A-perp / running bit.**
- **Contrarian Corner.** Chris got a rushed one at time in Ep 5 ("maybe the time of the DAO
  is over") — **confirm whether that counted or he's still owed a real one.** Prior tally
  (per Ep 4): Tyler had Ep 1 & 3, Jackson had Ep 4.
- **Pico's GoFundMe** (Tyler's dog / vet saga) — was on the Ep 5 carryover list but **never
  made air.** Still owed a 30-second check-in.
- **The Fable rate-limit / guardrail saga** — dominated Ep 5 (all three got throttled/
  guardrailed mid-record; Perp had to fall back Fable → Opus to place the trade) and is the
  post-credits stinger ("I'll probably have to use Opus to edit the pod"). It has now become
  *literally automatic* — see Topic C. Recurring bit.
- **"$10 pod software vs. $100 perp" gag** — Tyler: "we'll YOLO $100 into Perp every week but
  won't pay $10/mo for pod software"; Jackson: "I'm building open source." Reusable button.

## Topics

| # | Topic | Lead | The hook / angle |
|---|---|---|---|
| J | **Gamer thumb saga — week 4 check-in** | Chris | Cold-open button before the meat: quick status on the RSI. Ep 5 ended with the brace OFF because it's incompatible with the elite split keyboard he immigrated with. Did he cave and get a normie keyboard, or is the thumb "just going to be like this forever"? One breath. |
| A | **Agentic commerce — did anyone actually SHIP it?** | Chris / Jackson | **The marquee — the thread we've teased since Ep 1 and owe the audience.** The arc writes itself: **(1) the pullback** — OpenAI is *sidelining* in-chat "Buy it in ChatGPT" checkout after Walmart found it converted **~3× worse** than click-through to walmart.com (only ~30 Shopify merchants ever went live); **(2) the comeback** — Visa just ran **LIVE agent purchases at independent merchants in Europe on Jul 2** (lastminute.com, Frasers, BrickDepot) via its Trusted Agent Protocol + Agent Directory, and Worldline + ING + Visa completed a full end-to-end agent payment in Germany (agent picks the product, user authenticates with a Visa passkey, ING authorizes); **(3) the crypto undercurrent** — the volume actually lives on stablecoin rails: **Base crossed ~169M agentic transfers (20M in one 90-day window), 95% now ≥$1**, mostly USDC via **x402**; Mastercard's "Agent Pay for Machines" settles across cards *and stablecoins* down to sub-cent; **Coinbase wired x402 into Amazon Bedrock AgentCore.** **(4) the open question** — Anthropic is the one big lab still on the sidelines (ad-free, user-initiated, MCP-based — spec finalizes Jul 28). So: is agentic commerce a card-network story with crypto as invisible plumbing, or do the stablecoin rails eat the middle? **Tie-in to Perp:** is THIS the episode an agent completes a real purchase on camera? |
| B | **MEV — the sandwich bot got sandwiched** | Chris | The other on-camera promise, and a clean callback to Ep 4/5's jaredfromsubway.eth + BonkDAO segments. **jaredfromsubway.eth — the most prolific sandwich bot on Ethereum — was drained for ~$15M in a "reverse honeypot":** an attacker spent weeks planting fake token contracts that tricked Jared's bot into granting unlimited `transferFrom` approvals, then swept the funds (the exact careless-approval mistake that dooms retail, turned back on the predator). Widen out from there: **Flashbots now argues MEV/arb spam is the #1 limit to scaling blockchains** (reframes MEV from a fairness problem to a throughput problem); **Solana's Jito is basically an MEV monopoly** (~95% of staking, >60% of priority-fee volume) and just launched a consumer trading terminal (JTX) routing revenue to JTO holders; and the **based-rollup** debate — should L2 MEV flow back to Ethereum L1 instead of a centralized sequencer? Good bridge from Topic A: the same block-ordering games that extract MEV are what an agent's on-chain payment has to survive. |
| C | **Fable now silently downgrades you to Opus — and keeps your data** | All / Jackson | The Ep 5 running bit, now automatic and confirmed real. **Claude Fable 5 hard-blocks cybersecurity/crypto/bio queries and silently falls back to Opus 4.8** (~5% of sessions get quietly downgraded) — i.e., the "I'll probably have to use Opus to edit the pod" joke is now a product feature. Plus: Anthropic **forced 30-day traffic retention on all Fable users, even prior zero-retention customers** (privacy backlash), **reset Claude Code limits mid-outage**, is fighting a **Claude Max usage-limits lawsuit**, and users found a **cache bug reportedly inflating bills 10–20×.** Meanwhile it **extended free Fable access through Jul 19** as a GPT-5.6 counterpunch. **Verify the Jul 19 date day-of.** Natural contrast: Venice AI (Ep 5) as the anti-Anthropic — uncensored, no retention. |
| D | **Saylor is SELLING bitcoin — at a loss** | Tyler | Bitcoin hit, and a genuine narrative crack for a BTC show. Strategy/MicroStrategy rolled out a "Digital Credit Capital Framework" and **sold ~3,588 BTC (~$216M) to fund preferred dividends** (bumped to 12%), and booked an **~$8.3B Q2 loss** on holdings — average cost **~$75.5K vs. ~$60K spot, i.e. underwater.** Still the largest corporate treasury (843,775 BTC), but the "never sell" playbook is visibly bending. Frame against the tape: BTC rangebound **~$59–66K**, and spot ETFs just reversed their worst-ever outflow stretch (June ~$4.5B out; early-July 10-day bleed → +$221M inflow day Jul 3). **Re-check BTC price + ETF flow day-of** (Farside). |
| E | **The GENIUS Act clock hits zero — THIS Friday, July 18** | Jackson / Chris | Whatever day we record, this is live: the **six agencies (OCC, FDIC, NCUA, Treasury, FinCEN, OFAC)** face a **July 18, 2026 statutory deadline** to finalize stablecoin rules — and as of mid-June, **no final rules had published yet** (all comment periods closed Jun 9). **VERIFY status day-of** — did they hit it, slip it, or ship rules with teeth? The Act takes effect the earlier of Jan 18, 2027 or 120 days after final rules. Hooks straight into Topic F: whichever regime wins shapes which stablecoin gets the compliant lane. |
| F | **Stablecoin power shift — USDC's volume lead + the corporate-chain land grab** | Chris | Two threads that pair. **(1)** USDC has pulled ahead of USDT in *transaction volume* (~70% vs ~25%; record ~$1.79T in June, +63% MoM) even though **USDT still wins market cap** (~$184B vs ~$73B) — which number actually matters? **(2)** The rails are fragmenting: **Robinhood Chain** went to mainnet (Jul 1, Arbitrum L2, 95 tokenized stocks 24/7), **Tempo** (Stripe+Paradigm) is ramping with payment-dedicated lanes and a Visa/MC/Shopify/OpenAI/Anthropic partner list, and **Open USD** (Coinbase/BlackRock + 140 companies) is a new dollar-stablecoin coalition. Callback to Ep 5's "chain drift" — now it's "which chain even survives." |
| G | **Contrarian Corner** | **confirm on the day** | Chris's Ep 5 "time of the DAO is over" was rushed at time — decide whether it counted. If he's still owed, angle bank: agentic commerce is a card-network trojan horse, not a crypto win (A); MEV can't be fixed, only redistributed (B); or Saylor selling proves the BTC-treasury trade was always reflexive (D). |

---

## Backup Topics (if a segment runs short or falls through)

| # | Topic | Lead | The hook / angle |
|---|---|---|---|
| H | **The $40K trillion-parameter box — the leaf-blower bit, upgraded** | Jackson | Direct callback to Ep 5's "$50K leaf blower" / "software-engineer-in-a-box." Four Mac Studios linked over **RDMA-on-Thunderbolt-5** (macOS Tahoe) form a 1.5TB unified-memory cluster running a **1T-param model (Kimi K2) at ~25 tok/s for ~$40K at ~500W** — vs. ~$780K / 18kW for the H100 equivalent. And open weights caught up: **GLM-5.2 is the first open model to beat GPT-5.5 on SWE-Bench Pro.** So — is the box actually here now, and is it the escape hatch from Fable's rate limits (Topic C)? |
| I | **The state is now in the model-release loop** | Tyler / Jackson | **OpenAI shipped GPT-5.6 (Sol / Terra / Luna) to GA on Jul 9 — ~2 weeks after a U.S.-government-requested limited rollout was lifted**, mirroring Anthropic's Fable/Mythos export-control pause in June. Governments now gate frontier releases on both sides. Pairs with a fresh security angle: **CISA added a Langflow (AI-agent-builder) CVE to its must-patch list** after attackers used it to steal cloud creds, and Sen. Warner floated the **first federal agentic-AI bill (AI AGENT Act).** Ties the agent-commerce optimism (A) to "these agents are already getting exploited." |

---

## Appendix — pre-read references (sourced from the internet)

Optional prep; skim what's relevant to the segment you're leading. **Dates verified as of
Jul 16, 2026** — re-check anything time-sensitive (BTC price + ETF flows, GENIUS Act status,
the Fable-free-access Jul 19 date) the day we record. A few near-future items rest on single
secondary sources — flagged inline; treat as "reported."

**A · Agentic commerce**
- FF News — Visa unlocks agentic commerce in Europe; agents executing live retail transactions (Jul 2): https://ffnews.com/news/visa-unlocks-agentic-commerce-in-europe-ai-agents-now-executing-live-retail-transactions
- Worldline — Worldline, ING & Visa complete a live agentic payment in Europe (Jul 2): https://www.globenewswire.com/news-release/2026/07/02/3321259/0/en/WORLDLINE-Worldline-ING-and-Visa-complete-a-live-agentic-payment-transaction-in-Europe-Press-release.html
- Digital Applied — "Discover in AI, buy on site": why OpenAI sidelined in-chat checkout (Walmart 3× conversion gap): https://www.digitalapplied.com/blog/ai-agentic-commerce-discover-in-ai-buy-on-site-2026
- CNBC — OpenAI's agentic shopping and the retailer pullback: https://www.cnbc.com/2026/03/20/open-ai-agentic-shopping-etsy-shopify-walmart-amazon.html
- Crypto Briefing — Base crosses 20M agentic transfers in 90 days (~169M cumulative, 95% ≥$1): https://cryptobriefing.com/base-agentic-payments-20-million-transfers/
- Mastercard — Agent Pay for Machines (multi-rail incl. stablecoins, sub-cent): https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html
- Coinbase — Amazon Bedrock AgentCore Payments, powered by x402 + Coinbase: https://www.coinbase.com/blog/introducing-amazon-bedrock-agentcore-payments-powered-by-x402-and-coinbase
- Google Cloud — Agent Payments Protocol (AP2) + A2A x402 crypto extension: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- Nuvei — first in-agent payment with Visa + merchant-led strategy: https://www.prnewswire.com/news-releases/nuvei-completes-first-party-in-agent-payment-with-visa-unveils-merchant-led-agentic-payments-strategy-302816873.html
- Crypto Daily — Meta as an agentic-commerce surface; stablecoins as invisible rails (analyst piece, *reported*): https://cryptodaily.co.uk/2026/07/metas-agentic-commerce-stablecoins-invisible-rails

**B · MEV**
- BleepingComputer — jaredfromsubway.eth MEV bot hacked in ~$15M theft (WebFetch-verified): https://www.bleepingcomputer.com/news/security/jaredfromsubway-mev-bot-hacked-in-15-million-crypto-theft/
- CoinDesk — Ethereum's biggest sandwich bot drained in an ironic exploit: https://www.coindesk.com/tech/2026/06/21/ethereum-s-biggest-sandwich-bot-drained-of-usd7-5-million-in-ironic-exploit
- The Block — Flashbots: MEV bots are clogging blockchains faster than networks can scale: https://www.theblock.co/post/358512/mev-bots-are-clogging-blockchains-faster-than-networks-can-scale-says-flashbots
- Crypto Briefing — Jito: $351M market cap, $78M MEV fees, JTX terminal on Solana: https://cryptobriefing.com/jito-351m-market-cap-78m-mev-fees-solana/
- ethresear.ch — MEV for based rollups (redistribution debate): https://ethresear.ch/t/mev-for-based-rollup/15636

**C · Fable / Anthropic / rate limits**
- TechCrunch — Anthropic releases Claude Fable 5 (guardrails + Opus fallback context): https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/
- Forbes — Claude Fable 5 free access extended to July 19 (GPT-5.6 counterpunch): https://www.forbes.com/sites/sandycarter/2026/07/13/claude-fable-5-extends-to-july-19-7-days-7-power-moves/
- StartupFortune — Anthropic resets Claude Code usage limits after a rough week (*reported*, page 403'd fetcher): https://startupfortune.com/anthropic-resets-claude-code-usage-limits-again-after-a-rough-week-of-outages/
- Engadget — Anthropic hit with lawsuit over Claude Max usage limits (*reported*): https://www.engadget.com/2194626/anthropic-hit-with-lawsuit-over-its-claude-max-usage-limits/

**D · Bitcoin / Saylor / ETF flows**
- CoinDesk — Saylor's struggles over Bitcoin strategy yield a big loss: https://www.coindesk.com/markets/2026/07/06/one-month-that-shook-the-market-saylor-s-struggles-over-bitcoin-strategy-yields-big-loss
- BeInCrypto — MicroStrategy sold far more bitcoin than reported (*single-source "7×" claim — treat cautiously*): https://beincrypto.com/microstrategy-sold-far-more-bitcoin/
- Farside Investors — Bitcoin ETF flow tracker (pull a live screenshot day-of): https://farside.co.uk/btc/

**E · GENIUS Act rulemaking deadline (July 18)**
- Stablecoin Insider — Six agencies race to finalize GENIUS Act rules by July 18 (WebFetch-verified): https://stablecoininsider.org/six-federal-agencies-have-35-days-to-finalize-genius-act-stablecoin-rules-by-july-18/
- Chapman and Cutler — GENIUS Act Rulemaking Tracker (best living tracker; re-check day-of): https://www.chapman.com/publication-genius-act-rulemaking-tracker

**F · Stablecoins / corporate chains**
- CoinDesk — Circle's USDC is leaving Tether behind in the volume race: https://www.coindesk.com/business/2026/07/06/circle-s-usdc-is-leaving-tether-behind-in-the-stablecoin-volume-race
- Forbes — Robinhood launches its own blockchain (stock tokens + DeFi): https://www.forbes.com/sites/ninabambysheva/2026/07/01/robinhood-launches-its-own-blockchain-new-stock-tokens-and-defi-products/
- crypto.news — The corporate-chain land grab: Base, Tempo, Robinhood Chain: https://crypto.news/corporate-chain-land-grab-base-tempo-robinhood-chain/

**H · Local models (backup)**
- Awesome Agents — Mac Studio clusters for local LLM inference over RDMA (trillion-param at ~$40K): https://awesomeagents.ai/news/mac-studio-clusters-local-llm-inference-rdma/
- InsiderLLM — best local coding models 2026 (GLM-5.2 beats GPT-5.5 on SWE-Bench Pro; *search-sourced*): https://insiderllm.com/guides/best-local-coding-models-2026/

**I · Model-release gating / agent security (backup)**
- OpenAI — GPT-5.6 (Sol / Terra / Luna): https://openai.com/index/gpt-5-6/
- CNBC — OpenAI expanding GPT-5.6 as government limits end: https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html
- Tech Policy Press — Sen. Warner's first foray into agentic-AI regulation (AI AGENT Act): https://www.techpolicy.press/senator-warner-makes-a-first-foray-into-agentic-ai-regulation/

---

## Open threads NOT yet addressed (park or cut if the clock's tight)

- **Base vs. Tempo** — any sequencer/decentralization update? Now sharpened by the "corporate
  chain land grab" (Topic F) and the based-rollup MEV-redistribution debate (Topic B).
- **Venice AI** was fully covered in Ep 5 — only bring it back as the one-line anti-Anthropic
  foil inside Topic C, not a fresh segment.
- **The "$10 pod software" gag / "I'm building open source"** — reusable button, especially
  if this episode also has a QuickTime/edit mishap to complain about.
