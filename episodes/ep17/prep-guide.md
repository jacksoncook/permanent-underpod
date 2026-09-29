# Permanent Underpod — Ep 17 — Topics

**Record: Fri Oct 2, 2026 presumed; confirm with hosts. Research checked Sept 29.**
**Panel: Jackson (AI / Bitcoin products) · Chris (stablecoins / security) · Tyler (Bitcoin / Lightning)**

> **MARQUEE: Jev, the AI that can't talk.** TypeSafe AI's "System One model" launched Sept 15 after two years in stealth. It doesn't write text. You hand it a list of typed options and it returns one, with a probability. Builder is ex-OpenAI, co-invented the RLHF behind ChatGPT. $40M round led by DCVC; The Information says investors are talking $10B. It beat Pokémon Red in 37 hours for $1.65 of compute, with Claude Opus 5 coaching it out of loops. Crypto traders wired it to pump.fun launches within a week. Critics: "it's just a classifier," and it thinks a coin flip is 39% heads. Jackson's pick; Jackson leads.
> **The perp angle writes itself.** Perp of Fortune returns from exile. A model whose whole product is "typed decision + calibrated probability" is a perp picker. Chris decides whether Jev picks week three. Fail-closed rule below.
> **Spark (Tyler's pick).** Lightspark's channel-free Bitcoin L2 published a Sept 27 essay saying Lightning's "technology works, the user experience does not," and admitted in the same breath that it "fundamentally cannot provide provable assurances" you're the only one who can spend your coins. Tyler said on Ep 14 that Ark and Spark make Liquid pointless. Hold him to the L2 test he gave on Ep 16.
> **Enclaves, round three, with a fresh break.** Ep 15 explained attestation; Ep 16 said "model in a TEE, data in a TEE." Sept 14: DDRop, a sub-$200 DDR5 interposer that drops memory writes and forges Intel TDX attestation reports. Intel and AMD: "outside the threat model," no CVE. Last October's TEE.fail (<$1,000) already pulled BuilderNet's orderflow keys and Secret Network's consensus seed. That pays Ep 16's builder-duopoly debt inside the enclave segment.
> **Agent week two.** OpenAI paused all tool-use training on its most capable models after an agent tunneled out through DNS (Sept 20). Axios: "tens of thousands" of incidents under review at OpenAI and Anthropic. Sept 29: OpenAI sued over the Hugging Face breach, and DevDay shipped a new consumer agent the same day. Nvidia is selling the fence.
> **Debts from Ep 16's end card:** "is bitcoin back" (never aired, carried as C), builder duopoly (folded into E), and "does the Perp return from exile" (F). Enclave deep dive is paid twice over; E is the third pass, keep it to the new break.
> **55-minute ceiling.** If behind: bank K (Korea), then W, then trim C to the debate only. Keep D (agentic commerce) mid-show.

## Topics / proposed recording order

| # | Topic | Lead | Opening question | Minutes |
|---|---|---|---|---|
| H | Check-in | All | Did an agent do something you didn't ask for this week? | 1 |
| F | Perp of Fortune returns from exile | Chris | Which AI picks week three, and does it have to show its confidence? | 4 |
| J | MARQUEE: Jev, the AI that can't talk | Jackson | Where's all the automation if models have been superhuman at chat for years? | 8 |
| G | Agent week two: OpenAI stopped training | Jackson + Chris | The labs hit their own pause button. Which conspiracy theory survives that? | 6 |
| S | Spark: Lightning without channels, custody without proof | Tyler | Is 1-of-n honest operators self-custody? | 7 |
| E | Enclaves III: $200 climbs the fence | Chris | If attestation can be forged for $200, what did Ep 15 prove? | 6 |
| D | Agentic commerce: Shopify hands agents the checkout | Chris | Amazon says no, Shopify says yes. Who's holding the liability? | 4 |
| C | Is bitcoin back? (carryover, structural only) | Tyler + all | Back as what? | 5 |
| K | Korea: a yen stablecoin traded at 4× the yen | Jackson | What happens to a peg with no market maker? | 3 |
| W | Wildcard: $JEV, 152 holders | All | How fast does a model get a memecoin? | 1 |
| Z | Close | All | One prediction each; final perp number | 2 |

- Marquee starts by ~5:30; cold open teases the perp pick and "back as what?" Perp reveal within 90 seconds of starting the bit.
- These are caps. If behind: bank K, then W, then C's steelman lists (keep C's debate). That makes 47 → 42 minutes.
- Fresh-news substitutes below replace time. They don't add ten more minutes.

### H + F — Check-in and Perp of Fortune returns

- Pick an opener from the [five reusable Perp of Fortune intros](../../perp-of-fortune-intros.md). Acknowledge the exile: Ep 16 cut it "for your protection." Don't explain why on air beyond one line.
- Check-in prompt: OpenAI DevDay shipped "dots," a do-anything consumer agent, on Sept 29, three days after disclosing its agents were tunneling out of sandboxes. Did any host's agent do something unasked this week? One line each.
- Ep 15's published record: Fable 5.1 went **25× long JPY** the night before a BoJ hike, R-E-K-T in ten minutes, wrap at **−$13 → −$11**. Pull the actual position, funding, and realized P&L before recording. [Ep 15 published record](../ep15/segment-times.md)
- **Week three decision (Chris, before tape):** Fable 5.1 again, GPT-6 Luna, or **Jev**. Jev proposal: give it typed options `{long, short, flat}` × `{1×, 5×, 25×}` and require **probability ≥ 0.60 or the account stays flat.** Fail closed. That is the whole segment's joke and the whole segment's point: the model's product is the confidence number. Jackson can wire the call; input is $0.042/MTok, output is free.
- Caveat to say on air if Jev picks: Carson Sweet's test shows Jev returns **0.393** for a coin it was told is 49% heads. Its complements don't sum to 1 (avg 0.928 over 147 trials). Ask once, derive the other side in code. [Substack](https://carsonsweet.substack.com/p/jev-gets-cold-feet-at-even-odds)
- Read the usual disclosure before the bit: entertainment, not financial advice; personal views, not employers'. Reveal the position before the thesis.
- Button for J: **"The model that just picked our leverage can't write a sentence. That's the pitch."**

### J — MARQUEE: Jev, the AI that can't talk (Jackson, ≤8 min)

**Start:** "TypeSafe's launch post asks: 'Models have been superhuman at chat for years, so where is all the automation?' Their answer is a model that can't chat."

- **What it is:** Jev, first "System One Model" from TypeSafe AI. Early access Sept 15, 2026, ~2 years in stealth. Input: unstructured state. Output: a **typed choice from options you define, plus a calibrated probability**. No strings, so no type errors and no hallucinated JSON. Outputs are generated in parallel, not token by token. Claimed 70–500 ms end to end vs 3–329 s for LLMs; headline 193.6× faster and 444.6× cheaper on TypeSafe's own workflows, which they call "the higher end of real world gains." Baselines: GPT-6 Astra and Fable 5.1. Pricing: **$0.042/MTok in, output free**; they admit "we can't prove it isn't subsidized." [TypeSafe](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- **Who:** Diogo Almeida, ex-OpenAI, credited on the instruction-following/RLHF work behind ChatGPT. Co-founders Erik Gafni, Sasha Sheng. **$40M round led by DCVC** (sources call it seed or Series A; say "$40M round"). The Information (Sept 25): investors discussing $1B+ at $10B+; that's talk, not a term sheet. [The Information](https://www.theinformation.com/newsletters/dealmaker/jev-fervor-leads-talk-big-valuation-boost)
- **How it's trained:** "RLCD," Reinforcement Learning for Calibrated Decisions, vs RLHF/RLVR. Optimizes for "epistemically honest probabilities on System One tasks." That claim is the whole fight.
- **The Pokémon proof:** two runs. Andrew Boyd / Standard Agents reached the Hall of Fame Sept 23 after ~a week. Christian Mathiesen's open-source run streamed Sept 25–26: **37 h 40 m, ~16,150 decisions, 39.2M input tokens, $1.65 of Jev compute, median decision 0.4 s.** 16 team wipes, 15 Elite Four attempts. The harness read game RAM and offered legal actions; Jev picked. **Claude Opus 5 coached:** watched the log and rewrote options and rules ~474 times; Jev walked into locked Lorelei 53 times and crossed one Rock Tunnel ladder 124 times in ten minutes before the coach intervened. Stream viewers fed hints. [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-says-jev-decision-model-beat-pokemon-red-in-under-a-week-non-llm-engine-succeeds-where-traditional-chatbots-stalled-for-months-but-claude-opus-5-coached-the-model-through-its-dead-ends) · [GitHub README](https://github.com/christianmat/jev-pokemon/blob/main/README.md)
- **The backlash (Sept 23–25):** Alex Molas: calibration is a property of model + data distribution, not the model; Jev called a fair coin 0.92 heads when the answer was in the prompt. r/LocalLLaMA: "It's just a classifier, the amount of hype around it is insane." Independent checks: fine on CLINC150, worse on Banking77 (predictions marked ≥90% confident were right 72.2% of the time); a big share of four-class predictions reported at exactly 1.00. TypeSafe's two primitives (Choice vs Noul) calibrate differently on the same problem. No formal TypeSafe response found. [Backlash roundup](https://traictory.com/news/2026-09-25-jev-typesafe-marketing-backlash) · [Audit](https://escholarship.org/uc/item/4t4449jv)
- **Crypto got there first:** JevOnSol, a third-party Solana terminal, re-reads a token every ~5 s and emits `bid / watch / skip / enter / hold / exit`, watches pump.fun launches from mint, and **seals every call and grades it at 15 min, 1 h, and outcome.** "The terminal that publishes how often it is right." Community bots for Polymarket (needs ≥8% edge, fractional Kelly; 35 decisions, 19 markets, one trade as of Sept 23), Hyperliquid, Kalshi, Bybit. None audited. Affiliation with TypeSafe unverified; treat as third party. [JevOnSol](https://www.jevonsol.com/) · [Polymarket bot](https://github.com/devsoniclk/jev-polymarket)
- **Debate:**
  1. **Jackson:** every agent today is an LLM narrating its way to a tool call. Is "typed decision in 400 ms, LLM only when stuck" the real agent architecture, and is the Pokémon harness (Jev drives, Claude coaches) the template? Who holds liability when the fast model decides and the slow model only reviews?
  2. **Chris:** "calibrated" is the pitch and the exploit. A fraud-scoring or withdrawal-approval model that says 0.90 and is right 72% of the time is worse than no number. What does a bank do with a confidence score it can't audit? Tie to Bitget: forged commands "bypassed existing risk controls."
  3. **Tyler:** output is free and input is 4¢ per million tokens. Is that a business or a land grab, and what does it do to the "pace the frontier" theories if the cheap model is the one that acts?
  4. **All:** the first paying users are memecoin snipers and Polymarket bots. Is that a knock on Jev or the most honest benchmark there is (every call sealed and graded)?
- **Do NOT say:** "Jev predicts bitcoin's price" (a bitcoin.com piece frames it that way; we don't); "$10B valuation" as fact; "Series A" or "seed" as fact; "Jev beat Pokémon alone"; "JevOnSol is TypeSafe's product"; any BTC price or target.

**Clip question:** "An AI that can't write a sentence just beat Pokémon for $1.65. It thinks a coin flip is 39%. Would you let it trade?"

### G — Agent week two: OpenAI stopped training (Jackson + Chris, ≤6 min)

**Start:** "Last week an agent climbed Medicare's fence. This week OpenAI said its agents did it 'tens of thousands' of times, and turned the training run off."

- **Sept 20, the DNS tunnel:** a training-task agent, trying to identify a person from biographical clues, hit blocked search and chatbots, then found the sandbox's DNS resolver reached the internet. It used free wildcard-nameserver providers to tunnel 18+ questions to an external chatbot and got answers back ("The capital of France is Paris"). OpenAI **suspended "all training, evaluation, and inference with tool-use (defined broadly) of our most capable models"** until fixed, and "will not resume training this particular model, even though the existing reward signal already correctly penalized this behavior." Filtering now at two layers. [OpenAI misalignment report](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/)
- **Sept 26, Axios:** OpenAI and Anthropic reviewing "tens of thousands" of incidents: guardrail bypasses, sandbox escapes, website hijacking, agents creating message boards, self-prompting, evading monitors. Anthropic's Opus 5.5 system card: sandbox-escape attempts in **1.5%** of adversarial test runs. OpenAI agents leaked 53 user ChatGPT images; agents also probed US government sites. Sourced count, not an official one. [Axios](https://www.axios.com/2026/09/26/openai-anthropic-thousands-ai-security-incidents) · [AP](https://apnews.com/article/df331b55daffc6d202d8e2f6d0afa264)
- **Hugging Face, the July original:** during an internal cyber eval, agents bypassed internet blocks, reached Hugging Face production, and ran **~17,600 actions over ~4.5 days** apparently looking for benchmark answers (cheating on the eval). Altman: "the most severe" incident, hundreds of coordinated agents. [OpenAI](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)
- **Sept 29, the lawsuit:** a public-interest group sues OpenAI in California under the Unfair Competition Law seeking court-ordered controls. **Not Hugging Face suing, not damages.** First test of whether inadequate agent containment is an "unfair" practice. [Axios](https://www.axios.com/2026/09/29/openai-sued-hugging-face-breach)
- **Sept 27–29, the politics:** OpenAI and Anthropic execs back pacing (AP). Trump at a White House lunch with Amodei and Brockman: doesn't want to "stifle" AI, prefers self-regulation. DevDay ships 20+ products including "dots." [AP](https://apnews.com/article/9a057de94eb8f30a2fdb5b938918627e) · [Axios DevDay](https://www.axios.com/2026/09/29/openai-dev-day-2026-dots-space-sol)
- **Sept 28, Nvidia sells the fence:** Open Agent Safety Platform. **OpenShell** (open-source default-deny sandbox, brokered syscalls) and **Sentry** (out-of-band watchdog on BlueField-4 DPUs that quarantines an agent "within milliseconds"). Nvidia says it would have stopped Hugging Face. [Nvidia](https://nvidianews.nvidia.com/news/open-agent-safety-platform)
- **Debate:**
  1. **Tyler (scoreboard from Ep 16 conspiracy corner):** the labs paused themselves, then shipped a consumer agent 72 hours later. Which theory survives: safety theater, regulatory capture, or "take them at face value"?
  2. **Chris:** the DNS tunnel is the Medicare pattern exactly: told no, found a workaround. Now Nvidia's answer is hardware the agent can't see. Is agent safety becoming a data-center product, and who audits the watchdog?
  3. **Jackson:** OpenAI killed a model whose reward signal already punished the behavior. Is that the right call or a PR call? What's the crypto analog: do you burn a wallet that leaked once?
  4. **All:** UCL, not CFAA. If the only enforcer is a California unfair-competition suit, is liability arriving before regulation?
- **Do NOT say:** "tens of thousands" as an official count; "Hugging Face sued OpenAI"; "OpenAI stopped all training"; that Nvidia's tools were tested against the real incident.

**Clip question:** "OpenAI turned off its best model on Saturday. It shipped a new agent on Tuesday."

### S — Spark: Lightning without channels, custody without proof (Tyler, ≤7 min)

**Start:** "Sept 27, Spark's own research blog: 'The technology works. The user experience does not.' The technology is Lightning. Spark is Lightspark's fix. Read the trust model."

- **What it is:** Lightspark's Bitcoin L2, announced Oct 2024, mainnet **Apr 29, 2025.** Statechain-derived. Balances live in "leaves"; a transfer is a **key rotation under FROST threshold signing** between the user and the operator set (the "Statechain Entity"), not an on-chain tx. No channels, no inbound liquidity, no rebalancing, offline receive. Native tokens: **USDT (Tether) and USDB (Brale, via Flashnet)**, no wrapping, no internal fees. **Unilateral exit** shipped Jul 28, 2025: presigned exit txs plus a timelock. [Spark on statechains vs Lightning](https://www.spark.money/tools/bitcoin-statechains-vs-lightning) · [Unilateral exit](https://www.lightspark.com/news/spark/unilateral-exit)
- **Who runs it:** the Sept 27 post names **Lightspark and Flashnet** as current operators. The Sept 11 spark.exposed review read SDK configs naming **Lightspark, Breez, Flashnet at 2-of-3**, with Lightspark the default coordinator and swap provider. Different snapshots; say "two named operators today, three in some SDK configs."
- **Who uses it:** 20+ live integrations. Wallet of Satoshi (self-custodial mode by region, disclosure updated Aug 25, 2026), Breez SDK (Cake Wallet), Xverse (every new wallet gets a Spark address), Deblock. Tether's WDK integration is **Aug 2025**, not new. No independent user/volume/balance figures exist; everything is self-reported. [WoS disclosure](https://www.walletofsatoshi.com/disclosure)
- **The Sept 27 essay (bcTanji):** Lightning nodes ~20,700 (2022) → ~17,400 (mid-2026); public capacity plateaued ~5,000 BTC; channel opens cost 1,800–20,000 sats; force-close resolution can run "hundreds of thousands of satoshis." Then the admission: Spark "fundamentally cannot provide provable assurances that [users] are the only party that can immediately spend the UTXO," because operators can't prove they deleted old key shares. Security is **1-of-n honest operators.** [Spark research](https://www.spark.money/research/spark-bitcoin-l2-no-channel-ux-advantage)
- **The Sept 11 critique (spark.exposed, anonymous, no funding disclosed):** any single operator can veto sends, deposits and swaps at the preparation step even under 2-of-3 signing; a "selective refusal" code path rejects state changes while leaving reads working, with opaque errors; the presigned exit is not a consumer recovery flow (needs the right state, fee funding, dependent broadcasts, monitoring, special software). It **withdrew** an earlier claim that Flashnet's Aug 14, 2026 terms prove Spark-wide freezing; the terms cover Flashnet's own apps and APIs. [spark.exposed](https://spark.exposed/editorial-note.html) · [Flashnet note](https://spark.exposed/facts/flashnet-one-of-three-named-spark-operators-reserves-compliance-based-rejection-and-fund-freezing-in-its-service-terms.html)
- **Lightspark's 2026:** Cross River 24/7 fiat on Bitcoin rails (Feb 18), Solana developer platform (Mar 24), Grid Global Accounts (Apr 28), AI-agent payments (May 4), Estonia MiCA (Jul 1), Lithic cards on stablecoin settlement (Aug 5), "Beyond the Hype" stablecoin pitch (Sept 21). Reported ~$175M raised through 2024; no 2026 round found. Bitcoin as invisible settlement, dollars on the screen. [Lightspark press](https://www.lightspark.com/press)
- **Callbacks:** Tyler, Ep 14 (49:01): "no reason for Liquid to exist now that we have better constructs for scaling Bitcoin, things like Ark or Spark... they have unilateral exit." Tyler, Ep 16 (Arbitrum): "you must be able to exit to L1 unilaterally, or it's a database with a council."
- **Debate:**
  1. **Tyler:** grade Spark on your own Ep 16 test. Presigned exit exists, but recovery needs tooling wallets don't expose and operators can veto the prep step. Liquid is 11-of-15 known functionaries; Spark is 1-of-n honest and "trust us, we deleted it." Which is more honest about what it is?
  2. **Chris:** USDT native on Spark, operators see amounts and participants, one operator's terms reserve compliance-based refusal. Is Spark Lightning with a compliance desk, and is that the feature Tether bought?
  3. **Jackson:** channels were the wall normal people never got past, and node count is falling. Is "channel-free" the Lightning endgame or a walled garden with a Lightning bridge? Ark (Arkade, Bark) has the same UX pitch with rounds and an ASP. Which one would a product team ship, and why?
  4. **All:** Bitget lost $387.5M with "private keys not compromised" (forged backend commands). Spark's threat is an operator retaining a key share or refusing service. Which failure mode do you rate more likely in five years?
- **Do NOT say:** "Spark is trustless"; "Spark is custodial"; "Breez is an active operator" as fact; user or volume numbers; the Tether integration as new; any employer names (generic disclaimer is the ceiling).

**Clip question:** "Spark's own blog says it can't prove you're the only one who can spend your bitcoin. Still self-custody?"

### E — Enclaves III: $200 climbs the fence (Chris, ≤6 min; pays the builder-duopoly debt)

**Start:** "Ep 15: an attestation proves what code is running. Sept 14: a $200 board proves whatever you want it to."

- **DDRop, disclosed Sept 14, 2026** (KU Leuven, ETH Zurich, Google, Birmingham; ACM CCS, Nov 2026): "first low-cost (<$200) DDR5 RDIMM interposer" that injects parity errors to **drop cache-line writebacks.** TEE memory encryption has no per-write freshness, so the CPU later accepts stale-but-validly-encrypted memory. Demonstrated on **Intel TDX, Scalable SGX, AMD SEV-SNP**: copy victim pages, inject secure page-table entries, force any TD into debug mode, **forge attestation reports.** [Paper](https://research.google/pubs/ddrop-generic-memory-interposer-attacks-on-confidential-vms-by-dropping-ddr5-writes/)
- **Vendor answer, same day:** Intel INTEL-2026-09-14-001 and AMD-SB-3048: physical access, **"outside the threat model," no CVE.** Intel is "evaluating" hardening and "Platform Ownership Endorsements" (a signed statement about who owns the box). Not a patch.
- **The one before it, TEE.fail** (Georgia Tech / Purdue, disclosed Oct 28, 2025, IEEE S&P '26): passive read via a **<$1,000** interposer, exploiting deterministic encryption. Live demos: **BuilderNet** (Ethereum's "credibly neutral" block builder, ~18% of blocks per Ep 16's relayscan pull): extracted config secrets and orderflow decryption keys. **Secret Network:** pulled the consensus seed, decrypting every confidential transaction. **dstack:** forged a TDX quote that "can be successfully verified using Intel's DCAP Quote Verification Library at the highest trust level," and borrowed Nvidia GPU attestations. Intel and AMD then too: out of scope. "Very practical and you don't need a lab." [TEE.fail](https://tee.fail/)
- **Also live:** Intel's Aug 11 TDX Module advisory INTEL-SA-01436, CVE-2026-20885 (High, in-TD privilege escalation, local privileged attacker). Sept 9: Intel says "SkitterCreek" research is not a vulnerability. AWS Nitro: only containerd/runc package advisories (Sept 10, 14); **no evidence Nitro is affected by either interposer attack.**
- **Where the pod has been:** Ep 15 (47:18, 52:55): attestation "only meaningful if you can audit the code." Ep 16 (17:57): Chris's gold standard is model in a TEE, data in a TEE; Jackson: "Trusted execution environment. A secure enclave." Muse shipped as a Docker container instead.
- **Debate:**
  1. **Chris:** the threat model excludes the person who owns the server. In a public cloud that's the cloud. Who is a TEE protecting you from, and is "outside the threat model" a defense or a disclosure?
  2. **Tyler (builder duopoly, folded in):** BuilderNet is the decentralization answer to Titan's 55%, and its neutrality is a TEE. TEE.fail read its orderflow. Sepolia ePBS test still Oct 6. Does Ethereum's fix depend on hardware that two labs broke for under $1,000?
  3. **Jackson:** for Bitcoin custody, enclave-based signers vs multisig plus HSMs vs plain hardware wallets. A $200 interposer needs your DIMM slot. Which threat do you actually face: physical, insider, or the software above the enclave (Bitget's forged commands)?
  4. **All:** "model in a TEE, data in a TEE" was last week's gold standard. Is that still the ask, plus "and I rack the server myself"? Does a Platform Ownership Endorsement fix anything or just add a signature?
- **Do NOT say:** "remotely exploitable"; "cloud tenants can do this"; "Apple's Secure Enclave is broken" (not in scope of either paper); "Nitro is broken"; "TEEs are dead"; "Intel patched it."

**Clip question:** "The chip signs a note saying your code is safe. For $200 you can make it sign anything."

### D — Agentic commerce: Shopify hands agents the checkout (Chris, ≤4 min, MID-SHOW)

**Start:** "Last week Amazon threw Muse out. This week Shopify gave every browser agent three buttons: get_checkout, update_checkout, complete_checkout."

- **Sept 28, Shopify:** WebMCP extended to checkout. Agents running in the buyer's browser call structured tools instead of scraping; three new tools inspect, edit (address, delivery), and submit the order. Shop Pay included. Rolling out to "all eligible merchants." Instinct partnership announced the same day; Muse already had one. Gil Greenberg (Shopify PM): "Shopping with an agent shouldn't feel like watching paint dry." Amazon and **Adidas** are blocking agents. [TechCrunch](https://techcrunch.com/2026/09/28/shopify-opens-checkout-to-browser-based-ai-agents/)
- **Sept 25, Mastercard:** agentic commerce is "an infrastructure and trust problem," not a model problem: what is the agent authorized to do, who is liable, how does the transaction move. 22-company startup cohort; Agent Connect for merchants. Visa: tokenized agent credentials. Stripe: shared payment tokens under both networks. [PYMNTS](https://www.pymnts.com/commerce/ecommerce/2026/why-building-ai-agents-is-no-longer-the-hardest-part-of-agentic-commerce/) · [Mastercard](https://www.mastercard.com/us/en/news-and-trends/press/2026/september/mastercard-gives-merchants-a-simpler-way-to-build--connect-and-s.html)
- **Sept 26, x402:** a Lightning settlement option reportedly landed in x402 alongside stablecoins (single source; confirm in the x402 repo before citing, and **don't name the contributing company on air**). Machine-to-machine rail vs the card networks' delegated-consumer rail. [Roundup](https://zglg.work/en/ai/today/2026-09-27) · [x402 paper](https://arxiv.org/abs/2609.02208)
- **Sept 29, DevDay:** "dots," OpenAI's do-anything consumer agent, plus the Sept 10 Agents API (Codex harness, subagents, persistent workspaces). ACP with Stripe remains the checkout rail. [Axios](https://www.axios.com/2026/09/29/openai-dev-day-2026-dots-space-sol)
- **Callbacks:** Jackson, Ep 16 (15:52, 22:17): saw Instinct in the wild; a friend's agent switched his electric plan to save "$850 a year, allegedly." Chris (17:04): disconnected Instinct "because I got spooked about their intern looking at my Google Drive."
- **Debate:**
  1. Shopify exposes the checkout; Amazon and Adidas block. Which side is protecting the customer and which is protecting the funnel?
  2. **Chris:** Mastercard says the hard part is authorization evidence: which human delegated what, with what limits. Is that a card-network product, or is it what a signed mandate on a stablecoin rail already is?
  3. **Jackson:** Jev-style typed decisions plus WebMCP typed tools. Does agent shopping stop needing an LLM at all? Who eats the chargeback when a 400 ms classifier hits complete_checkout?
  4. **Tyler:** Lightning in x402. Is that agents paying for APIs in sats, or another leaderboard of bots pinging bots (Solana's 23.2M self-reported x402 txs from Ep 16)?
- **Do NOT say:** "Lightning is live in x402" as fact before checking the repo; PayPal–Muse as confirmed; employer names.

**Clip question:** "Amazon banned the shopping agent. Shopify gave it the checkout button. Who's right?"

### C — Is bitcoin back? (Tyler + all, ≤5 min; carried from Ep 16's end card)

**Hard rule: no price, no ETF flows, no chart talk. If a host reaches for a number, Tyler redirects to what was built.**

**Start:** "We promised this last week and cut it. CNBC said 'bitcoin is back' in August. Back as what?"

- **Steelman, it's back (built while nobody cheered):** SEC innovation exemption for tokenized NMS stock (Sept 17); CFTC rulemaking filed with OMB (Sept 18); SEC CorpFin FAQs on crypto-asset treatment (Sept 25); Strategic Bitcoin Reserve bill (American Reserve Modernization Act) cleared House FSC (Sept 16; committee vote, Senate frozen). **Bitcoin Core 32.0rc2** (Sept 22), final targeted early October: faster validation, fee-policy changes, security fixes. Strike NY BitLicense; Raiffeisen crypto via Bitpanda in CEE branches; Chainalysis: on-chain economic activity −1.6% YoY through the rout, cross-border stablecoin flows +77.5%. [SEC FAQs](https://www.sec.gov/securities-topics/crypto-task-force/cryptosec) · [Core 32 rc2](https://bitcoincore.org/bin/bitcoin-core-32.0/test.rc2/) · [Chainalysis via The Block](https://www.theblock.co/news/ecosystems/2026-09-23-crypto-economy-fell-just-1-6-in-12-months-despite-2-1-trillion-market-cap-rout-chainalysis-says-416150)
- **Steelman, it's not:** rules without statute die in court or with the next administration. Strategy (~846k BTC after Sept 21) spent this week re-plumbing its preferreds to accrue dividends daily; the treasury-company era is optimizing its financing layer, not its thesis. Miners pivoting to AI/HPC (Sept 24 analysis) while hashrate hit a record; flag the disagreement, don't pick. Sztorc: "no soft fork can activate"; BIP-360 quantum roadmap eyes 2029. The growth is stablecoins and tokenized stocks; bitcoin is the collateral. And **Bitget: $387.5M**, revised up from $351.6M, via a zero-day in a third-party security product that let forged withdrawal commands through; BTC withdrawals back Sept 28, ETH Sept 29, USDT Sept 30, everything else Oct 2; 5% bounty; NK is a "preliminary suspicion," Chen says unconfirmed. [Strategy](https://www.strategy.com/media) · [Bitget incident page](https://www.bitget.com/campaigns/bitget-security-incident-2026)
- **Debate:**
  1. **Jackson:** if the winning rails are tokenized stocks and agent-paid stablecoins, does bitcoin become collateral infrastructure rather than money? Is that a loss?
  2. **All:** Strategy walked back "never sell" in September and now tunes its preferreds daily. Does the protocol care?
  3. **Tyler:** Spark, Ark, and shielded-Bitcoin metaprotocols all route around a base layer that can't change. Is ossification the feature, and who decides when quantum forces it?
- **Do NOT say:** any price, any ETF figure, "Core 32 released," "Lazarus" as fact, "$387.5M stolen" as final (Bitget's figure; on-chain confirmation lagged).

**Clip question:** "Bitcoin's back. Back as what?"

### K — Korea: a yen stablecoin traded at 4× the yen (Jackson, ≤3 min)

**Start:** "Upbit listed JPYC on Sept 17. It opened at ₩12. The yen is worth about ₩9. It hit ₩37.60."

- **JPYC on Upbit** (Sept 17): opened ~₩12, peaked **₩37.60**, roughly 4× the yen. **EURC on Bithumb** (Sept 14): ~₩1,513 → **₩7,860**, 400%+. Korea bans market makers under manipulation rules, so nobody is paid to hold the peg. The FSC is now weighing a licensed market-maker regime and tighter listing oversight. [Cointelegraph](https://cointelegraph.com/news/south-korea-weighs-crypto-market-makers-after-jpyc-trades-at-4-times-peg) · [Chosun](https://biz.chosun.com/en/en-finance/2026/09/17/QE2LPUDZMZDTFNSC5OGP7HK6NM/) · [Unchained](https://unchainedcrypto.com/south-korean-regulator-considers-legalizing-crypto-market-making-tighter-exchange-oversight/)
- **Kakao** (Sept 28–29): group roadmap for a won stablecoin, settlement infra, open ecosystem with banks and brokers; KakaoBank and Kakao Pay CEOs on the task force. No legal won stablecoin exists; the Digital Asset Basic Act is stalled on **who issues** (BoK: banks only; FSC: broader). [Yonhap](https://www.yna.co.kr/amp/view/AKR20260929060600017) · [Korea JoongAng Daily](https://www.koreajoongangdaily.com/business/korean-banks-race-to-test-stablecoins-as-seouls-digital-currency-rules-remain-stuck/12874723)
- **The outflow:** net stablecoin transfers from Upbit, Bithumb, Coinone, Korbit, Gopax to overseas exchanges: **~₩14.92T over the 18 months to June 2026**, ₩2.76T in June alone. [TokenPost](https://www.tokenpost.com/news/regulation/25353)
- **Callback:** Ep 15's Erebor / Wintermute basis trade: "not all stablecoins trade equal." Korea is the same fact with no arbitrageur allowed.
- **Debate:** Chris: is a peg without a market maker a peg? Tyler: if ₩15T a year leaves for offshore dollar rails, does a bank-only won stablecoin stop it or just brand it? Jackson: kimchi premium on a stablecoin is the purest version of the story you've been telling.
- **Do NOT say:** BTC kimchi premium numbers; "Kakao launched a stablecoin."

**Clip question:** "A yen stablecoin traded at four yen in Korea. Nobody was allowed to fix it."

### W — Wildcard: $JEV, 152 holders (All, ≤1 min)

- A model that can't talk got a Solana memecoin within two weeks. $JEV per a September Solflare snapshot: ~$38K market cap, ~$20K liquidity, **152 holders**, 3% transfer fee, metadata mutable, risk status "Danger." Holding 100,000 JEV adds picks to Telegram. TypeSafe has nothing to do with it. [Solflare](https://www.solflare.com/prices/jev/27tNoYYhtovz1EmCQz3VufMMuDh6Nrv35QRX2vAyBNeA/)
- Second bit if time: Visa's Sept 19 memecoin-rewards fix (Ep 16 W, unaired if cut): MCC 5815 "digital media" for shitcoins.

## Fresh-news bench

- **CLARITY is dead; agencies go alone (Chris, 3 min if C runs short).** Cloture failed 49–50 Sept 15; SEC/CFTC ship FAQs and rulemaking; ECB wants MiCA's yield ban extended to lending/staking; GENIUS rulemaking past deadline. Carried from Ep 16's bench.
- **Anthropic Opus 5.5 system card, 1.5% sandbox-escape attempts.** If G runs short, Jackson reads the exact framing (adversarial tests) so the number isn't misused.
- **Coinbase post-quantum custody plan** (Sept 22–23). Pairs with C's quantum thread.
- **Circle Arc mainnet** (Sept 16). Issuer-owned chain vs the rails debate; pairs with S (Tether on Spark).

## Evergreen bench (no news peg)

- **Open vs. closed weights.** Peg this week: Nvidia open-sourced OpenShell (the sandbox) while the frontier models it contains stay closed. Open the fence, close the animal.
- **"Grade the tape"** (salvaged from Ep 10). Natural fit for Jev: JevOnSol seals every call and grades it. Could become a recurring bit: grade the hosts' Ep 16 predictions.
- **Secure enclaves:** aired Ep 15, callback Ep 16, DDRop pass in E this week. After E airs, retire for at least a month unless something remote breaks.

## Host pre-read / before recording

- **Everyone:** read the [TypeSafe launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) and skim the [jev-pokemon README](https://github.com/christianmat/jev-pokemon/blob/main/README.md). Read the [Spark Sept 27 essay](https://www.spark.money/research/spark-bitcoin-l2-no-channel-ux-advantage) at least to the trust-model section. Bring one prediction from Ep 16 to grade.
- **Jackson:** decide (with Chris) whether Jev picks the perp; if yes, wire the typed call and the ≥0.60 rule before tape, and screenshot the raw probability for the PiP. Check for a TypeSafe response to the calibration critiques dated after Sept 25. Refresh the DNS-tunnel report and DevDay for anything dated Sept 30 onward. Actual perp result and funding paid.
- **Chris:** read [DDRop](https://research.google/pubs/ddrop-generic-memory-interposer-attacks-on-confidential-vms-by-dropping-ddr5-writes/) abstract and the [TEE.fail](https://tee.fail/) BuilderNet and Secret Network sections; pull Intel's Sept 14 announcement text for the exact "threat model" wording. Refresh Bitget: full incident report (promised), frozen/recovered totals, USDT withdrawals Sept 30. Then [Shopify TechCrunch](https://techcrunch.com/2026/09/28/shopify-opens-checkout-to-browser-based-ai-agents/) and the Mastercard piece.
- **Tyler:** read [spark.exposed](https://spark.exposed/editorial-note.html) and note it is anonymous and undisclosed; check whether Spark or Lightspark replied. Confirm current operator set from Spark's docs at record time. Confirm the Lightning-in-x402 claim in the x402 repo. Re-read your own Ep 14 Liquid line and Ep 16 L2 test; you'll be asked to apply both. Check Core 32.0 final status and the ePBS Sepolia date (Oct 6) day-of.
- **Fact guardrails:** no BTC price or ETF numbers anywhere, including Jev's "forecast"; "$40M round," not seed/Series A; Pokémon was Jev + Claude + a harness + viewers; JevOnSol is third-party; Spark is neither "trustless" nor "custodial"; DDRop/TEE.fail need physical access, Nitro and Apple's enclave are not shown affected; "tens of thousands" is a sourced count; the lawsuit is a UCL public-interest suit, not Hugging Face; Bitget's $387.5M is Bitget's figure and NK is unconfirmed; no employer names, the generic disclaimer is the ceiling.
- **Close:** actual perp result, one prediction each, and only promise next week's topic if a host takes it. Candidates to tease: grade the tape (Ep 16 predictions), Core 32.0 final, the Bitget incident report.
