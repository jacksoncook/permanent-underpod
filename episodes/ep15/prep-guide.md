# Permanent Underpod — Ep 15 — Topics

**Record: Fri Sept 18, 2026 presumed; confirm with hosts. Research checked Sept 17.**
**Panel: Jackson (AI / Bitcoin products) · Chris (stablecoins / security) · Tyler (Bitcoin / Lightning)**

> **The lead: why do the labs want to slow down now?** Each host brings an independent take on the real motive. Read the proposal first; don't assign anyone a position.
> **The money thread:** Erebor subsidizes conversions, Muse uses existing checkout, and Liquid needs its bitcoin back. Who pays for the convenience?
> **The privacy thread:** Anthropic alleges intermediaries sold user conversations. Chris connects that to what secure enclaves actually protect.
> **Carryovers:** Muse and enclaves were prepped for Ep 14 but didn't make the published episode. Liquid did: this week needs an update, not another range-proof lecture.
> **55-minute ceiling.** All requested topics have notes below. If the debates run, park loans first, then the standalone rails comparison. Keep Muse/enclaves mid-show.

## Topics / proposed recording order

| # | Topic | Lead | Opening question | Minutes |
|---|---|---|---|---|
| H | Check-in | All | What did your agent actually accomplish this week? | 1 |
| F | Perp of Fortune | All | Did last week's 2× BTC long make anything? | 3 |
| A | Pace the frontier | All; Jackson moderates | What's the real reason for slowing down now? | 9 |
| B | Erebor's free-conversion problem | Jackson + Chris | Did they buy customers or subsidize arbitrage? | 5 |
| C | Anthropic's threat-intelligence report | Jackson + Chris | Is your discount model provider selling your prompts? | 6 |
| D+T | Muse payments + secure enclaves | Chris | Who can see the data, and who can authorize the purchase? | 9 |
| E | Liquid heist update | Tyler, proposed | What's back, what's still missing, and can users exit? | 5 |
| G | Do federations earn their trust? | Tyler + all | Who is Fedimint better for than a single custodian? | 5 |
| J | Bitcoin-backed loans | Jackson + Tyler | Is borrowing against bitcoin a useful product or delayed selling? | 5 |
| K | Which stablecoin rail wins? | Chris + all | Who gets the payment when every chain is cheap? | 5 |
| Z | Close | All | One prediction each; final perp number | 2 |

- First substantive payoff by ~2 minutes. Perp reveal within 90 seconds of starting the bit.
- These are caps, not ten mandatory lectures. If behind: bank J, then K; that makes 45 minutes.
- Fresh-news substitutes below replace time. They don't add ten more minutes.

### H + F — Check-ins and Perp of Fortune

- Pick an opener from the [five reusable Perp of Fortune intros](../../perp-of-fortune-intros.md).
- One callback each: Tyler's Stripe-checkout SaaS has a paying customer? Jackson's egg-app distribution? Chris's fruit-fly trading experiment?
- Ep 14's published sheet records a **2× BTC long**, with an intrashow mark near **−$0.10**. That isn't a closing result. Pull the actual position, fees, funding, and realized/unrealized P&L before recording. [Ep 14 published record](../ep14/segment-times.md)
- Read the usual disclosure before the bit: entertainment, not financial advice; personal views, not employers'. Reveal the position before explaining the model's thesis.
- Button for A: **Would you trust the model with your money while its maker asks everyone to slow down?**

### A — Pace the frontier: each host's real-reason take

**Start:** “Last week we were grading the models. This week: why do their makers want more time?”

- **Read first:** Dario Amodei's September essay proposes embedded outside evaluators, coordination among democratic countries' frontier labs, then international coordination. Anthropic commits to the evaluator step; the wider framework needs others. He points to faster AI-assisted AI development and recent loss-of-control incidents. This is a proposal to pace capability gains, not an announcement that training has stopped. [Original essay](https://darioamodei.com/post/we-must-pace-the-frontier)
- **Round one, 60 seconds each:** Jackson → Chris → Tyler. Each gives the main motive, strongest evidence, and one observation that would change their mind. No interruptions. Hosts choose their own takes.
- **Round two:** each host challenges the next person's causal story. Finish with a prediction for what the labs will actually do in the next 90 days.
- **Competing hypotheses, not established motives:** sincere concern about control; time to fix operational failures; incumbents raising entry costs; breathing room to monetize existing models; a geopolitical bargain over access to compute.
- **Force a test:** Would they slow while a rival keeps shipping? Accept an evaluator publishing an embarrassing finding? Apply the same rule to themselves while leading? What evidence distinguishes a real safety commitment from useful positioning?
- **Close:** Which safeguard would you support even if you distrust the CEO? Which proposed restriction would you reject even if the danger is real?

**Clip question:** “What would they give up to prove they mean it?”

### B — Erebor: free conversions meet professional traders

- **Reported Sept 15–16:** Erebor withdrew a free stablecoin-to-cash offer after trading firms used it for arbitrage at the bank's expense. Reports name Wintermute and Galaxy. The accessible coverage attributes the story to The Information; the full original wasn't accessible in this research pass. **Reported story; exact loss and trade mechanics unverified.** [Accessible secondary account](https://www.onebullex.com/news/articles/erebor-bank-absorbs-losses-as-wintermute-galaxy-exploit-free-stablecoin-conversion)
- **Explain the possible economics, explicitly hypothetical:** buy $1 million face value at $0.999, redeem at $1, receive a $1,000 gross spread before fees, funding, and timing risk. If the bank can't recover those costs, volume makes the subsidy larger. This illustrates the incentive; it is not a reconstructed Erebor trade.
- **Jackson:** Where was the intended payback: deposits, lending, other services, or customer acquisition? What behavior would tell you the promotion is buying the wrong customers?
- **Chris:** Is par redemption the product people actually want? Who pays for liquidity and the fiat exit when the chain transfer is cheap?
- **Fight:** If a trader follows your published terms, is that abuse or your pricing mistake? Would limits, spreads, or minimum balances preserve the useful service?
- Don't equate the bank's accounting losses with losses from this offer. No verified dollar total here. Don't describe arbitrage as a hack or theft.

**Bridge:** “Cheap service can have a second business model. Now apply that to tokens.”

### C — Anthropic's report: who else gets your conversation?

- **Primary claim:** Anthropic says Moonshot and DeepSeek silently routed some customer queries to Claude and harvested outputs/reasoning for training. It also describes proxy services selling user exchanges, SenseTime buying such data, and a proxy operation it attributes to MiniMax. These are Anthropic's findings and attributions, not independently established findings by the pod. [September threat-intelligence report, distillation section](https://www.anthropic.com/threat-intelligence-report-september-2026)
- **The router angle is directly relevant:** the alleged market includes intermediaries collecting real user conversations. Legitimate routing, unauthorized model substitution, and resale of transcripts are different practices.
- **Jackson's hypothesis to debate:** Could unusually cheap inference be subsidized to acquire valuable human tasks and frontier-model answers? Distinguish commercial data harvesting from Chinese state funding. **The report does not establish that China subsidizes cheap routers to harvest prompts.**
- **Chris:** A retention promise from the frontend doesn't answer which downstream provider receives the request. What would persuade you: named subprocessors, enforceable retention terms, independent audits, verifiable execution?
- **Countercase:** discounts can come from caching, batching, routing to cheaper models, or customer-acquisition budgets. A cheap price alone proves nothing.
- **Privacy fight:** Anthropic could investigate because it saw abuse-related activity. What monitoring should a provider do, and what access are customers implicitly buying into?
- Don't accuse OpenRouter or another named service without service-specific evidence. Don't turn the report into a claim about every Chinese model or user.

**Clip question:** “If the answer is cheap, what else did you pay with?”

### D+T — Muse pays, and Chris finally explains enclaves

**Payments, ~4 minutes**

- **Shipped Sept 8:** Muse integrates Stripe Link. At over one million Link businesses, it uses the customer's saved payment method; elsewhere, Link supplies a single-use virtual card scoped to an approved purchase. **Two checkout paths.** Don't describe every Link checkout as a virtual-card payment. [Stripe announcement](https://stripe.com/gb/newsroom/news/stripe-helps-meta-muse-shop-with-link)
- **Chris:** Walk one purchase: user instruction → approval → payment credential → merchant checkout. Which part is novel, and which part inherits existing acceptance and support?
- **Debate:** Did cards win this consumer use case because of merchant reach, authorization controls, refunds, or simple time to market? Which of those advantages could a stablecoin stack reproduce?
- Separate the agent interface, payment credential, and settlement rail. A consumer paying by card doesn't tell us every rail used behind the scenes.

**Secure enclaves, ~5 minutes; Chris leads**

- Meta says Muse runs in a per-user Secure VM with a separate Sentinel that gates outbound activity and handles credentials. It announces a **Confidential VM for later in 2026**. Don't present that future protection as shipped. [Meta launch](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), [security design](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)
- **Chris's 60-second explainer:** a trusted execution environment can isolate computation and memory from parts of the surrounding host. Remote attestation lets a verifier check evidence about the environment/code before releasing secrets. The exact boundary depends on the design and hardware.
- **Make it concrete:** a cloud operator, malicious webpage, compromised agent, and chip vulnerability are four different adversaries. Which does the proposed boundary address?
- **Critical connection to C:** protecting a VM doesn't automatically protect prompts once sent to a remote model API. Trace where plaintext exists, who holds keys, what code can send out, and what the attestation actually covers.
- Hardware isolation doesn't establish that the model picked the right merchant or that a purchase is authorized. Approval policy and transaction limits still matter.
- **Close:** Would Chris put email, passwords, and purchasing power into today's product? What specific change would flip that answer?

**Clip question:** “Your agent can spend money. Who can spend through your agent?”

### E — Liquid: Tyler's update, not the explainer again

- **Where the audience left off:** Ep 14 covered the reserve drain, return of most funds, and the attacker's self-awarded fee. Jackson explicitly asked whether more would come back next week. [Transcript, 50:57](../ep14/transcript-attributed.md)
- **New reported development, Sept 11:** Blockstream rejected the demand to keep the remaining roughly 600 BTC and demanded its return. Attribute the refusal to the report; don't frame the retained amount as an agreed bounty. [The Block](https://www.theblock.co/news/ecosystems/2026-09-11-return-the-bitcoin-blockstream-refuses-ransom-demand-for-remaining-600-btc-from-liquid-exploit-414247)
- **Status limit:** the official status page retrieved Sept 17 still exposed a Sept 10 recovery update. That is not a fresh Sept 17 confirmation of peg-in/peg-out availability. [Official status](https://status.blockstream.com/)
- **Tyler's update card:** BTC recovered / BTC still outstanding; who funds any shortfall; transfers vs peg-ins vs peg-outs; final post-mortem released or still pending. Give each answer an as-of time. If unavailable, say unknown.
- **Correction to last week's discussion:** the transcript speculated that AI found/chained the bugs. We haven't verified that attribution. Don't repeat it as fact.
- **Debate:** Does reimbursement repair the trust model, or reveal that users ultimately rely on a sponsor's balance sheet?
- If no newer verified development lands, do the refusal in two minutes and give the remaining time to G.

### G — Do federations have a value proposition? Fedimint case

- **20-second distinction:** Liquid is a federated sidechain; Fedimint is a federated custody and ecash system. Fedimint's guardians collectively custody bitcoin; users transact with ecash, and Lightning gateways connect payments beyond the federation. Blind signatures support transaction privacy. Users still trust the federation's custody. [How Fedimint works](https://fedimint.org/users/how-it-works), [guardian responsibilities](https://fedimint.org/guardians/intro)
- **Best case:** community custody, private everyday payments, and shared operational burden for people who would otherwise use one custodian. The relevant comparison may be a custodial wallet, not a hardware wallet.
- **Tyler defends or rejects:** name a real user whose life gets better. Family? Merchant community? Local savings group? What amount would that user keep there?
- **Chris attacks:** do guardians actually fail independently if they run the same code and depend on the same infrastructure? Does “people I know” help if they collude or disappear?
- **Jackson:** who pays for operations, resolves disputes, and helps a user exit? Does privacy justify added coordination?
- **Verdict:** each host names one use case that earns the trust, or says none. A federation is not unilateral self-custody; Liquid's incident alone doesn't prove every federation has identical failure modes.

### J — Bitcoin-collateralized loans: useful liquidity or forced selling later?

- **Use case:** someone wants dollars now while retaining BTC exposure. Compare a short bridge funded by future income with indefinitely borrowing to fund living costs.
- **Public example:** Coinbase documents BTC converted into cbBTC and deposited into Morpho as loan collateral. Its linked help page gives an 86% liquidation LTV threshold. That is a specific product's rule, not a universal lending standard. [Collateral and liquidation](https://help.coinbase.com/en-gb/coinbase/trading-and-funding/loan/collateral)
- **Round-number example, no live price:** $100,000 collateral, $30,000 debt = 30% LTV. A 50% BTC fall makes LTV 60%. With an illustrative 80% liquidation threshold, $37,500 collateral reaches the trigger: a 62.5% fall, ignoring interest and fees.
- **Jackson:** when is this better than selling a small amount? What's the repayment source if BTC stays flat for three years?
- **Tyler:** who holds the keys? Can collateral be rehypothecated? What happens if the lender fails? In an onchain product, add wrapper, oracle, contract, and liquidation risks.
- **Chris:** can you repay or add collateral during a weekend crash? Does the promised liquidity survive when everyone needs it?
- **Close:** name the borrower this product serves well, and the borrower it should turn away. Avoid blanket “tax-free” claims; treatment depends on jurisdiction and transaction structure.

### K — Which rail wins the stablecoin payment?

**Keep the dollar token fixed where possible. Pick the job before picking the chain.**

| Rail | What it brings | What to challenge |
|---|---|---|
| Ethereum L1 | Shared settlement and contract composability | Is L1 execution worth its cost for this payment? |
| Ethereum rollups, including Base / Arbitrum | Lower execution costs with Ethereum settlement | Sequencer, upgrade, bridge, exit, and fragmented-liquidity assumptions vary by rollup. |
| Solana | One shared execution environment; payments tooling and fast, low-cost transfers | End-to-end reliability, usable ramps, and merchant distribution beat a TPS claim. |
| Tron | Established USDT transfer use case; resource-based transaction pricing | Who supplies or pays for Energy/Bandwidth? Compare actual cash-out costs. |
| Stellar | Payments tooling and MoneyGram cash access | Where is cash-out actually available, with what limits and fees? |
| Bitcoin / Lightning with Taproot Assets | Bitcoin payment routing with asset conversion at the edges | Asset liquidity, quotes, wallet support, and issuer risk still matter. |
| Card / bank rails | Existing checkout and bank-account reach; benchmark for the user journey | Access, fees, reversibility, operating hours, and intermediaries differ by system. |

- Technical pre-reads: [Ethereum rollups](https://ethereum.org/developers/docs/scaling/optimistic-rollups/), [Solana payments](https://solana.com/solutions/institutional-payments), [Tron resources](https://developers.tron.network/docs/bandwidth-and-energy), [Stellar / MoneyGram](https://stellar.org/products-and-tools/moneygram), [Taproot Assets on Lightning](https://docs.lightning.engineering/the-lightning-network/taproot-assets/taproot-assets-on-lightning).
- **Three jobs, quick picks:** $100 cross-border family payment; $100,000 supplier payment; a $0.01 agent API purchase. Each host names a rail and the decisive assumption. A different winner for each is allowed.
- **Score the entire trip:** funding → transfer → recipient's usable money. Include conversion spread, liquidity, failure recovery, privacy, and who can freeze funds.
- **Interoperability countercase:** Circle's CCTP burns and mints native USDC across supported chains using Circle attestations. Does cheap movement make the wallet/router the winner, rather than any single chain? [CCTP design](https://www.circle.com/blog/scaling-your-app-for-high-volume-usdc-transactions-with-cctp)
- **Fresh peg, Sept 10:** Circle says Noble will not receive CCTP V2; new minting ends Oct 13, with contract/CCTP pause Jan 12, 2027. A working chain can still lose issuer support. [Circle notice](https://www.circle.com/es/blog/circle-is-discontinuing-support-for-usdc-and-cctp-v1-on-noble)

**Clip question:** “The transfer costs a penny. Getting dollars out costs what?”

## Fresh-news bench

- **CLARITY follow-up, Chris, 2 minutes:** the Sept 15 procedural vote failed 49–50; 60 votes were required. This was failure to advance, not final rejection of the bill. Ask whether temporary agency policy is enough for builders. Check for a subsequent vote before recording. [AP](https://apnews.com/article/e3caf262dc138147941787299e5f0a66)
- **Noble / CCTP:** already folded into K. Stronger than another generic “stablecoins are growing” beat because the issuer can change the usefulness of a rail.
- **Core Lightning disclosure:** Ep 14's prep expected an embargo to lift Sept 11. No new CVE details verified for this guide. Tyler can substitute a sourced release-note update for Liquid time; don't repeat the old expected date as an outcome.

## Host pre-read / before recording

- **Everyone:** read [Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier); bring your own motive, evidence, and falsifier. Save the takes for tape.
- **Jackson:** prepare the real perp result; keep Erebor's loss unquantified unless the original report establishes it. Frame state-subsidized harvesting as a hypothesis.
- **Chris:** read the [distillation section](https://www.anthropic.com/threat-intelligence-report-september-2026), [Stripe checkout announcement](https://stripe.com/gb/newsroom/news/stripe-helps-meta-muse-shop-with-link), and [Muse security design](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse). Bring the enclave explainer and a rail pick for each job.
- **Tyler, proposed:** refresh Liquid's balances, backing, and actual withdrawal status; bring the strongest Fedimint case. Use [official status](https://status.blockstream.com/) and any newly published post-mortem, dated at record time.
- **Fact guardrails:** no invented Erebor loss; no government-subsidy claim presented as proven; no unverified Liquid AI attribution; no promise that an enclave prevents an authorized app from exporting data.
- **Close:** actual perp result, one prediction each, and only promise next week's topic if a host takes it.
