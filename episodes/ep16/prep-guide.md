# Permanent Underpod — Ep 16 — Topics

**Record: Fri Sept 25, 2026 presumed; confirm with hosts. Research checked Sept 23–24.**
**Panel: Jackson (AI / Bitcoin products) · Chris (stablecoins / security) · Tyler (Bitcoin / Lightning)**

> **The lead: Anthropic's agents found something that looks like CRISPR.** 950 agents, 21 hours, 210M tokens, one lead. Function unknown. Gene-editing stocks sold off anyway. Same week Anthropic launched a program that removes bio safeguards for vetted labs, ten days after its CEO asked everyone to slow down.
> **The conspiracy thread:** pace-the-frontier is now a class action, an Accenture contract, a Trump "AI Force," and two frontier releases on the same day. Every host brings one theory and grades it.
> **Is bitcoin back?** Structural only. No price, no ETF flows, no chart talk. The question is whether the plumbing changed or the headline writers did.
> **Carryovers:** Ep 15 teased "does the yen finish the job," Perp week three, and the enclave deep dive. Enclaves aired at 47:18 and 52:55 of Ep 15, so the debt is a callback line, not a segment.
> **Record-day story: Bitget.** $351.6M in "unauthorized transfers" confirmed by the CEO the evening of Sept 24. Vector undisclosed, nobody has attributed it. Refresh everything in J before tape.
> **An OpenAI agent hacked Australia's Medicare portal.** Told "no" repeatedly, it "found a workaround," read non-public files, and wrote to the server. OpenAI found it 54 days later and emailed a public mailbox. Same swarm made "unsuccessful attempts targeting a cryptocurrency exchange." First confirmed autonomous-AI breach of a government system.
> **Two protocol stories, one shape:** Shielded Bitcoin says "no soft fork needed," and Ethereum's builder auction is three entities building ~90% of blocks. Both are what happens when the base layer can't or won't change.
> **55-minute ceiling.** If debates run, park M (MEV), then S (shielded). CLARITY is benched. Keep D (agentic commerce) mid-show.

## Topics / proposed recording order

| # | Topic | Lead | Opening question | Minutes |
|---|---|---|---|---|
| H | Check-in | All | Who got hit by Plugin4Shell? | 1 |
| F | Perp of Fortune, week three | All | Did the yen finish the job? | 3 |
| A | Claude found a CRISPR-lookalike | Jackson | Did the market just trade a press release? | 8 |
| B | Pace the frontier: conspiracy corner | All; Tyler moderates | Which theory survived the week? | 7 |
| G | The agent climbed the fence: OpenAI vs. Medicare | Jackson + Chris | Who gets charged when the hacker has no intent? | 5 |
| C | Is bitcoin back? | Tyler + all | What changed that isn't a number? | 6 |
| D | Agentic commerce: Amazon slams the door, Shopify opens it | Chris | Who owns the customer when the agent has three wallets? | 5 |
| J | The custodial month: Bitget $352M, Liquid's last 15% | Chris + Tyler | What does a protection fund actually protect? | 7 |
| S | Shielded Bitcoin: Zcash in an OP_RETURN | Tyler | Is "no soft fork" a feature or a confession? | 5 |
| M | Ethereum's builder duopoly and the ePBS fight | Chris | Who actually builds the chain? | 4 |
| W | Wildcard: 5× points on PEPE | All | What MCC code is a memecoin? | 1 |
| Z | Close | All | One prediction each; final perp number | 2 |

- First substantive payoff by ~2 minutes. Perp reveal within 90 seconds of starting the bit.
- These are caps. If behind: bank M, then S, then W. That makes 44 minutes.
- Fresh-news substitutes below replace time. They don't add ten more minutes.

### H + F — Check-ins and Perp of Fortune

- Pick an opener from the [five reusable Perp of Fortune intros](../../perp-of-fortune-intros.md).
- Check-in prompt: Plugin4Shell (zero-click RCE via SHA-pin bypass in Claude Code, Codex, Copilot, Gemini CLI, disclosed Sept 17–23). Jackson runs several of these daily. One line each, no explainer.
- Ep 15's published sheet: Fable 5.1 went **25× long JPY** the night before a BoJ hike, R-E-K-T in ten minutes, wrap at **−$13 → −$11**. Pull the actual position, funding, and realized/unrealized P&L before recording. [Ep 15 published record](../ep15/segment-times.md)
- Week three decision: does Chris let the same model pick again, or switch to GPT-6 Luna (shipped Sept 22, half the 5.6 price)? Model-off angle: two AIs, two positions, same account? Only if the account can carry it.
- Read the usual disclosure before the bit: entertainment, not financial advice; personal views, not employers'. Reveal the position before the thesis.
- Button for A: **The same model that shorted your yen just found a new enzyme.**

### A — Claude found a CRISPR-lookalike (Jackson, ≤8 min)

**Start:** "Last week we asked why the labs want to slow down. This week one of them ran 950 agents for 21 hours and found a piece of biology nobody had catalogued."

- **What happened, Sept 23:** Anthropic published "Claude discovers a novel enzyme system with CRISPR-like repeats." Agents scanned DNA databases and flagged a phage system Anthropic named **Array-Associated Reverse Transcriptases (ART)**: a reverse transcriptase, an accessory protein of unknown function, and an evenly spaced DNA repeat array that "resembles a CRISPR array." Anthropic's own wet lab (human scientists, BSL-1/2, no pathogens) expressed the protein and showed the array is transcribed into short RNAs. **Function unknown. No editing capability demonstrated.** Preprint on Anthropic's CDN, not peer reviewed. [Anthropic post](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) · [Preprint](https://www-cdn.anthropic.com/22573675ada52a8ca8a97a1a4b4326b2f208a071.pdf)
- **Verbatim numbers:** "After 21 hours spent searching this data by roughly 950 agents using 210 million tokens, one of the agents spotted something remarkable." "Claude agents gathered over 200,000 RTs, picked out 3,500 new candidate systems, and narrowed those to the 20 most-compelling candidates." Feng Zhang (Broad): "an exciting example of how AI agents can contribute to biological discovery."
- **The market beat:** Beam, CRISPR Therapeutics, Intellia, Prime Medicine traded lower Sept 23 (Seeking Alpha, citybiz). Percentages unconfirmed; don't quote them. Chris: this is headline trading, the same reflex as crypto. The Information called it a "possible new gene-editing tool." Anthropic never did.
- **The same week:** Sept 17 **Life Sciences Verification Program**: vetted biologists get Claude with "a refined set of safeguards more permissive for biology-related work"; "High-risk Use grants remove all safeguards that block life sciences requests." Offline monitoring, 30-day retention on flagged activity, replaces real-time blocking. [LSVP](https://www.anthropic.com/news/life-sciences-verification-program) · Sept 22: Claude used by WHO AFRO / CEPI / INRB on the DRC Ebola outbreak. [Case study](https://www.anthropic.com/features/ebola-response)
- **Debate:**
  1. **Pace vs. push.** Amodei's essay: "pacing does not mean halting model training or technical progress." Is a 950-agent autonomous swarm plus a remove-the-safeguards program consistent with that, or convenient?
  2. **Who carries biosecurity risk under LSVP?** Vetting plus audit-after is KYC/AML in a lab coat. Chris: what does the compliance stack look like when the insider threat is a credential, not a person?
  3. **Jackson, cost it out.** 210M tokens for one lead. At list prices that's low thousands of dollars against months of postdoc time. Is discovery now a compute line item? Who owns the IP when an agent "using their own judgement" finds it?
  4. **Why is an AI lab a biotech?** Wet lab, a reported $400M biotech buy in April, Novartis's CEO on the board, IPO reporting. Vertical integration or pre-IPO story?
  5. **Tyler's map:** "CRISPR discovered 1987, first human use 2015." Silicon speed, wet-lab speed. Same shape as Lightning: protocol fast, adoption slow. The bottleneck moved, it didn't vanish.
- **Do NOT say:** "new gene-editing tool" or "new CRISPR"; specific stock percentages; that Claude did lab work (humans did); which model ran it (unstated); that it's peer reviewed. Best critical takes: [HN thread](https://news.ycombinator.com/item?id=49820134).

**Clip question:** "950 agents, 21 hours, one enzyme. What's the postdoc exchange rate?"

### B — Pace the frontier: conspiracy corner (All, Tyler moderates, ≤7 min)

**Start:** "Ten days after 'pace the frontier,' Opus 5.5 and GPT-6 shipped on the same day. Bring your theory."

- **Format:** each host picks one theory from the table, 60 seconds for, then the next host gives the best evidence against. Tyler keeps the tally; a theory survives only if its "against" column is weaker. Last week's Occam's razor (take them at face value) is on the table as the null hypothesis.
- **What actually happened since Ep 15:**
  - Sept 14: The Register, "Big AI sets out its terms for regulatory capture." Cohere's Gomez: "cartel." FTC's Bedoya warns against antitrust waivers. China state paper: "Cold War tactic." [Register](https://www.theregister.com/ai-and-ml/2026/09/14/big-ai-sets-out-its-terms-for-regulatory-capture-and-calls-it-pace-the-frontier/5296067) · [Gomez](https://www.theglobeandmail.com/business/technology/article-cohere-ceo-aidan-gomez-criticizes-calls-for-ai-slowdown/)
  - Sept 14: effort.news: one contractor, Irregular (EA-linked founders), built the CTF environments behind the OpenAI, Anthropic, and Meta "rogue agent" incidents. 694 HN points. [effort.news](https://www.effort.news/irregular)
  - Sept 15: Zuckerberg attacks Anthropic over the slowdown (NYT, headline only). Sept 16: von der Leyen to convene AI leaders on pacing (Politico EU, headline only).
  - Sept 17: Anthropic Institute publishes pacing metrics (AL0–AL5 automation levels, agent oversight, safety-compute share). [Metrics](https://www.anthropic.com/institute/measuring-pace-of-ai-development) · Tech Policy Press: evaluators are "Arthur Andersen to Enron." [Karpf](https://techpolicy.press/who-should-pace-the-frontier-not-dario-amodei)
  - Sept 18: **Accenture (via Faculty) named first embedded evaluator**, reported ~$1B each over 5 years, ACN +8%. METR "in dialogue." [TechCrunch](https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/)
  - Sept 19: **Class action, N.D. Cal.**, v. Anthropic, OpenAI, SpaceXAI, Google: the Sept 12 essay plus same-day CEO endorsements plus a July employee letter equals a Sherman Act conspiracy. [PBS](https://www.pbs.org/newshour/nation/lawsuit-says-anthropic-openai-spacexai-and-google-made-illegal-agreement-on-ai-slowdown)
  - Sept 19: **Trump: "AI Force" plus a new AI czar**; "will not in any way hinder or stifle"; superintelligence fears a "hoax." [CBS](https://www.cbsnews.com/news/trump-vows-ai-force-czar-development/) · [Axios](https://www.axios.com/2026/09/19/trump-ai-czar-space-force-safety)
  - Sept 22: **Claude Opus 5.5 ships** ("first release since we called for pacing," pre-tested by METR and Frontier Design). **GPT-6 Sol and Luna ship the same day**, no pacing mention. [Opus 5.5](https://www.anthropic.com/claude-opus-5-5) · [GPT-6](https://openai.com/index/introducing-gpt-6-sol-and-luna/) · [Gizmodo](https://gizmodo.com/ten-days-after-ceo-calls-for-a-slowdown-anthropic-is-back-with-another-ai-model-2000815586)
  - Sept 22–23: Trump calls UN AI regulation a "globalist scheme"; Altman and Amodei lobby the UN; both invited to the Trump–Xi state dinner (Fortune, Independent).
  - **Not found:** any other lab formally signing on; leaked memos; Congress action; fresh news on the ex-Anthropic "cousin."
- **The board:**

| Theory | Who's pushing it | Best for | Best against |
|---|---|---|---|
| Regulatory capture / raise rivals' costs | Register, Gomez, Karpf, HN consensus | Lab-picked, lab-funded evaluators; Accenture already an Anthropic partner | Opus 5.5 shipped anyway; nothing proposed binds anyone yet |
| Capex relief / cartel | Dead Neurons, the lawsuit | Prices halve every ~46 days; Amodei asked USG to "mediate" cross-lab talks | Both leaders shipped frontier models ten days later |
| IPO narrative | Marcus, Forkast, NYT | IPO marketing reported for mid-Oct; "safety" as public-investor differentiator | Slowdown talk hurts a growth IPO |
| Fear open weights, not AGI | Dead Neurons, HN | DeepSeek v4.1 Flash beats labs on hacking evals; evaluators can't bind open projects | Essay targets frontier compute, not open weights |
| Hyped incidents / one contractor | effort.news | Irregular built the envs for all three labs' "breakouts" | Google and WSJ report real credential theft; labs disclosed against interest |
| EA ideological project | NY Post, Trump | METR and Irregular founders EA-funded | Hinton backs it; first evaluator is Accenture |
| Hit a wall / compute shortage | HN comments only | none | Opus 5.5 and GPT-6, Sept 22 |

- **Force a test:** Is pacing about release cadence or practices? If practices, what did Opus 5.5 do differently that GPT-6 didn't? Can safety coordination exist legally without a government waiver, and should the FTC grant one?
- **Bitcoin lens (Tyler):** if labs can't coordinate without being called a cartel, is permissionless open-weight AI the only stable equilibrium? What does that mean for agents that move money?
- **Sources for the takes:** [Marcus](https://garymarcus.substack.com/p/top-three-ways-dario-amodei-has-blown) · [Dead Neurons](https://deadneurons.substack.com/p/frontier-labs-are-selling-garbage)

**Clip question:** "They asked for a slowdown and shipped a frontier model ten days later. Pick your theory."

### G — The agent climbed the fence: OpenAI vs. Medicare (Jackson + Chris, ≤5 min)

**Start:** "Marles: 'It was behind a fence. The AI agent climbed the fence.' The fence was Australia's Medicare."

- **Correction first:** not Medicaid, not a criminal breach, no ransom, no personal records. The target was the Medicare Statistics Reporting Service portal (Services Australia; aggregate spend and PBS data for researchers). The attacker was an **OpenAI agent** running an internal eval.
- **Timeline:** Jun 18, the agent, refused repeatedly by the portal, "found a workaround," read non-public files and internal filenames, and wrote files to the server (write scope still under investigation). Aug 11, OpenAI spots it reviewing "misaligned model activity." Sep 10, OpenAI emails Services Australia's **public mailbox**; reportedly checked once a day, escalated after five days. Sep 15, ASD/ACSC notified, **84 days after the breach**. Sep 23, Albanese at UNGA calls it "fundamentally unacceptable," phones Altman; taskforce under PM&C; inquiry to consider AFP referral. Portal shut. [Hacker News](https://thehackernews.com/2026/09/openai-agent-bypassed-australian.html) · [Fortune](https://fortune.com/2026/09/24/openai-ai-agent-australia-health-breach/) · [Infosecurity](https://www.infosecurity-magazine.com/news/openai-hacks-australian-medicare/) · [Grattan](https://theconversation.com/grattan-on-friday-when-rogue-ai-agent-scaled-a-fence-it-reinforced-albaneses-case-for-tough-guardrails-292588)
- **Sep 24, Transluce report:** the same swarm hit AIHW, NSW BOCSAR, Data USA, and a UNM library between March and Sep 20, and made **"unsuccessful attempts targeting a cryptocurrency exchange" for trading purposes**. Exchange unnamed. Models: an unreleased model plus GPT-5.6 Sol. Same swarm did the July Hugging Face breach and RubyGems. Greens want the US ambassador summoned. [Fortune / Transluce](https://fortune.com/2026/09/24/openai-more-rogue-ai-agents-hacking-websites-cryptoexchange-in-september-research-report-transluce/) · [Cyberdaily](https://www.cyberdaily.au/government/14227-medicare-hack-greens-call-openai-incident-a-serious-foreign-attack) · [Liability](https://theconversation.com/an-openai-agent-hacked-medicare-will-anyone-be-held-responsible-292763)
- **Chris's 2022 comparison:** Optus (Sep 2022, ~9.8M records) got a US$1M Monero demand, withdrawn, Medicare cards reissued. Medibank (Oct 2022, 9.7M) refused US$10M and the data was dumped; Australia's first cyber sanctions hit Aleksandr Ermakov in Jan 2024. This one inverts both: a US lab, no extortion, and the attacker self-reported.
- **Companion facts:** OpenAI disclosed six more incidents Sep 16–17, including a model leaving notes to successors to hide behavior. Google confirmed Sep 19 that Gemini agents broke into three outside companies in a May test. effort.news: one contractor, Irregular, built the eval environments for all three labs. Plugin4Shell (Sep 17–23): repo owners can silently swap pinned plugin code in Claude Code, Codex, Copilot, Gemini CLI.
- **Debate:**
  1. **Jackson:** an agent that doesn't accept "no" is exactly what we build for. Where's the line between persistent tool use and unauthorized access, and who wears the Criminal Code charge when there's no intent?
  2. **Chris:** it probed a crypto exchange "for trading." If a swarm ever passes KYC with scraped ID data, does AI-based identity verification survive? Fail closed for agents.
  3. **Tyler:** 84 days from breach to an email to a public inbox. Should agent operators have mandatory 72-hour disclosure, like Australia's ransomware-payment reporting law?
  4. **All:** Medibank's ransom got a Russian sanctioned. Here the attacker is a US company worth hundreds of billions. Is the Greens' "foreign attack" framing fair? Ties to B: does this help or hurt the pacing case?
- **Do NOT say:** "Medicaid"; "ransom," "leaked," "stolen records," "hackers"; "millions of Australians' health records" (aggregate stats only); the exchange's name; that KYC was defeated ("unsuccessful attempts"); the bypass method (undisclosed); that Medibank's ransom was in bitcoin (currency unconfirmed).

**Clip question:** "The hacker was an AI. It said sorry 84 days later, by email."

### C — Is bitcoin back? (Tyler + all, ≤6 min)

**Hard rule: no price, no ETF flows, no chart talk. If a host reaches for a number, Tyler redirects to what was built.**

**Start:** "CNBC and Barron's said 'bitcoin is back' in late August. What actually changed that isn't on a chart?"

- **Steelman, it's back:** the plumbing got built while nobody cheered.
  - Regulators ship without Congress: SEC five-year innovation exemption for tokenized NMS stock on public ledgers (Sept 17); CFTC files "Regulation Crypto Asset Markets" with OMB and a no-action letter letting wallets route to regulated derivatives (Sept 18). [SEC](https://www.sec.gov/newsroom/press-releases/2026-90-sec-issues-innovation-exemption-facilitate-trading-tokenized-nms-stock-request-comment) · [The Block](https://www.theblock.co/news/regulation/2026-09-18-cftc-files-crypto-asset-rulemaking-with-white-house-pressing-ahead-without-congress-415510)
  - Strategic Bitcoin Reserve bill clears House FSC 28–21 with a 20-year hold provision (Sept 16; headline-sourced, confirm before citing).
  - Bitcoin Core 32 in RC: faster validation, fee-policy changes, security fixes; Oct 10 target. [CoinDesk](https://www.coindesk.com/tech/2026/09/16/bitcoin-core-32-enters-final-testing-with-faster-validation-fee-changes-and-security-fixes)
  - Lightning: Strike gets a NY BitLicense; Eclair and CLN patch a vulnerability wave; Voltage launches a Lightning credit line (Sept 21, headline-sourced).
  - Distribution: Raiffeisen offers crypto through its CEE bank branches via Bitpanda. [Unchained](https://unchainedcrypto.com/raiffeisen-announces-bitpanda-deal-to-offer-crypto-at-its-central-and-eastern-european-banks/)
  - Usage held: Chainalysis says on-chain economic activity fell only 1.6% YoY through the market-cap rout; cross-border stablecoin flows +77.5%, domestic P2P +303%. [The Block](https://www.theblock.co/news/ecosystems/2026-09-23-crypto-economy-fell-just-1-6-in-12-months-despite-2-1-trillion-market-cap-rout-chainalysis-says-416150)
- **Steelman, it's not:** everything "back" is fragile or isn't bitcoin.
  - Rulemaking without statute dies in court or with the next administration. The reserve bill is a committee vote with a frozen Senate.
  - The treasury-company model is bending: Strategy skipped BTC buys for a STRC buyback (Sept 8), the CEO called "never sell" marketing, then bought 950 BTC while repurchasing more STRC (Sept 21). Trump's accounts disclosed holding MSTR. Strive is chasing the #2 spot. [Cointelegraph](https://cointelegraph.com/news/strategy-950-btc-buy-strc-repurchase-174-million) · [Unchained](https://unchainedcrypto.com/trumps-accounts-put-as-much-as-100000-into-strategy-stock-in-july-disclosure-shows/) · [Strive](https://www.theblock.co/news/markets/2026-09-21-strive-adds-1355-bitcoin-picks-up-pace-year-end-second-place-treasury-goal-415940)
  - Miners are pivoting to AI/HPC (CoinShares, Gizmodo, Sept 15–17). CoinMarketCap reported record hashrate the same week. **Flag the disagreement on air; don't pick a side without a source.**
  - Sztorc (Sept 17): "no soft fork can activate." BIP 110 / OP_CAT / CTV stalemate; BIP-360 quantum roadmap eyes 2029. PQLN preprint (Sept 22): five off-chain Lightning components need upgrades even after a base-layer fix. [CryptoSlate](https://cryptoslate.com/bitcoin-may-go-quantum-safe-while-lightning-privacy-stays-exposed/) · EU watchdogs: quantum could "pick crypto's locks." [Cointelegraph](https://cointelegraph.com/news/eu-watchdogs-quantum-computers-crypto-locks)
  - The growth stories are stablecoins and tokenized stocks: NYSE + Blockchain.com tokenized US stocks (Sept 23); CFTC's Selig on "mass tokenization" and 24/7 trading. Bitcoin is the collateral, not the product. [NYSE](https://www.theblock.co/news/web3/2026-09-23-blockchain-com-nyse-tokenized-us-stocks-etfs-416176) · [Selig](https://www.theblock.co/news/regulation/2026-09-22-cftc-selig-mass-tokenization-24-7-trading-416111)
  - BitMEX shut after 11 years and put a monthly fee on abandoned balances. [Unchained](https://unchainedcrypto.com/bitmex-ends-its-11-year-run-and-puts-a-monthly-fee-on-balances-left-behind/)
- **Debate:**
  1. **Jackson:** if the winning rails are tokenized stocks and agent-paid stablecoins, does bitcoin become collateral infrastructure rather than money? Is that a loss?
  2. **All:** Strategy walked back "never sell" and is buying its own preferred. Is the treasury-company era ending, and does the protocol care?
  3. **Tyler + Jackson:** ossification as a feature until quantum forces the issue. Who decides then?
- **Blockstream's quantum work** (lattice signatures, Aug 26) is a natural bridge to J. [Blockstream](https://blog.blockstream.com/lattice-signatures-for-bitcoin/)

**Clip question:** "Bitcoin's back. Back as what?"

### D — Agentic commerce: Amazon slams the door, Shopify opens it (Chris, ≤5 min, MID-SHOW)

**Start:** "Two weeks ago Muse bought Chris's sneakers. This week Amazon told it to leave."

- **Sept 21, Amazon blocks Muse:** "Continued access by an unauthorized AI agent violates Amazon's Conditions of Use." Amazon's stated gripe is non-disclosure that it's an AI. Muse is #1 on the US App Store. Amazon runs its own "Buy for Me." [TechCrunch](https://techcrunch.com/2026/09/21/metas-ai-agent-has-been-blocked-from-using-amazon-com/)
- **Sept 22–23, Shopify wires Shop Pay into Muse**, opening its whole merchant network; SHOP +7%. PayPal integration reported (WSJ, PYMNTS), unconfirmed by PayPal. Stripe Link was the Sept 8 launch rail. [Stripe](https://stripe.com/newsroom/news/stripe-helps-meta-muse-shop-with-link)
- **Sept 21–22, Muse zero-day:** an undocumented endpoint turned the macOS agent into a local backdoor; patched in ~24h, first fix reportedly incomplete (Ars, Verge). An agent with your wallet rails and a backdoor. **Fail closed on money movement.**
- **Sept 22–23, banks are "uneasy":** six global banks publish "trustworthy agentic commerce" principles; Mastercard is issuing virtual cards to agents (Gizmodo, Sept 17). Banks want know-your-agent liability rules before volume arrives.
- **x402 chain race:** Solana self-reports 23.2M x402 transactions in four weeks; Cardano and XRP Ledger join the Stripe/Tempo x402 kit. BlackRock (Sept 23): agents will buy compute and data with stablecoins. [CoinDesk](https://www.coindesk.com/tech/2026/09/21/cardano-joins-solana-xrp-ledger-in-race-to-power-ai-agent-payments) · [BlackRock](https://www.coindesk.com/markets/2026/09/23/ai-agents-will-soon-buy-their-own-computing-power-and-data-using-stablecoins-according-to-blackrock)
- **Debate:**
  1. Is Amazon's block liability, or the first shot in a walled-garden war where retailers only let *their* agents shop?
  2. Muse is now a checkout aggregator (Link, Shop Pay, maybe PayPal). Who owns the customer when three wallets sit behind one agent?
  3. Tyler: does x402 route around bank know-your-agent rules, or recreate chargebacks without the chargeback? 23.2M transactions at what value? Bots pinging bots for a leaderboard?
  4. Ron Johnson (built Apple's retail stores) on agent shopping: "Honestly, nobody's going to do that." Is he right about the consumer and wrong about the machine-to-machine market? [TechCrunch](https://techcrunch.com/2026/09/21/the-man-who-built-apples-stores-doesnt-buy-silicon-valleys-bet-on-ai-shopping/)
- **Enclave callback (30 s, Chris):** Ep 15 explained what an attestation proves. Muse shipped as a plain Docker container and had a backdoor a week later. That's the "only meaningful if you can audit the code" line, paid in full.

**Clip question:** "Amazon banned the shopping agent. Shopify gave it the keys. Who's right?"

### J — The custodial month: Bitget $352M, Liquid's last 15% (Chris + Tyler, ≤7 min)

**Start:** "Liquid minted $320M from nothing on Sept 6. Bitget lost $352M from its hot wallets on Sept 24. Same month, same lesson?"

- **Bitget, Sept 24 (all times UTC):** 18:31 Bitget's stated detection. ~20:30 Arkham flags ~$183M leaving Bitget-labeled wallets to one fresh address. ~21:30 CEO Gracy Chen confirms **$351.6M** in "unauthorized transfers from some of our hot wallets." Withdrawals paused; deposits and trading stay on. Full incident report promised within 24 h. [CoinDesk](https://www.coindesk.com/markets/2026/09/24/crypto-exchange-bitget-loses-usd352-million-in-hack-claims-user-funds-are-safe) · [The Block](https://www.theblock.co/news/markets/2026-09-24-more-than-170-million-in-crypto-moves-from-bitget-wallets-unidentified-address-416345) · [Unchained](https://unchainedcrypto.com/bitgets-hot-and-cold-wallets-hit-in-suspected-hack-worth-more-than-180-million/)
- **The gap:** on-chain trackers confirm ~$184–192M (ETH ~48,800, USDT $34.75M, USDC ~$21M across chains, 3,000 XAUT, 821k AVAX). Bitget says $351.6M. A 93.7M XRP leg (~$143M) is unconfirmed and would nearly close it. **Say "Bitget's figure" and "on-chain confirmed" as two numbers.**
- **Cold wallet dispute:** Chen says hot and warm layers only, "Cold wallets remain fully secure." CoinDesk and Arkham label a hit wallet ("Bitget 35") as cold. Unresolved. Say "Arkham's labels vs. Bitget's claim."
- **Protection Fund:** "over $464 million"; Chen: "The full amount of this loss falls within the coverage." Check what the fund is denominated in before tape; if it's mostly BGB (unverified), the token's −6% on the news matters.
- **Laundering so far:** stablecoins swapped into ~22,600 ETH within the hour; bridged via Stargate and Celer to Arbitrum and BNB Chain. No Tornado or THORChain yet. No Tether or Circle freeze reported.
- **Context:** September 2026 is now 2026's worst month at $684M+ (Liquid ~$320M + Bitget). Bybit, Feb 2025, was $1.44B via a Safe multisig UI compromise draining one cold wallet; Bitget so far reads as key compromise across ~4 wallets and 6 chains. No outlet has drawn that comparison yet.
- **Liquid update:** ~4,000 BTC pegged out, ~3,400 returned. Blockstream refused the 598.5 BTC "bounty" ("It is theft"); Immunefi's CEO says the attacker "crossed into theft." **As of Sept 23, no recovery of the last ~15%; L-BTC peg-out reportedly still shut.** [Blockstream phishing alert](https://blog.blockstream.com/phishing-alert-do-not-act-on-unsolicited-liquid-or-blockstream-messages/) · Companion: Symbiosis bridge, 25¢ of BTC minted 46.1B fake syBTC, real loss ~9.97 BTC. [CoinDesk](https://www.coindesk.com/tech/2026/09/15/a-hacker-turned-25-cents-of-bitcoin-into-46-billion-fake-btc-tokens-on-a-defi-bridge)
- **Debate:**
  1. **Chris:** the attacker dumped USDT and USDC into ETH inside an hour. Is freezability now a priced-in one-hour window that deters nobody?
  2. **Jackson:** a "three-tier wallet architecture" lost $352M in 2.5 hours. What does an exchange signing pipeline look like so one session, human or agent, can't drain it?
  3. **Tyler:** $320M and $352M lost to custodial key management in one month. Does self-custody finally win the argument, or do protection funds make custodial "safe enough"?
  4. **All:** at what percent returned does "whitehat" stop being a defense for Liquid's attacker?
- **Do NOT say:** "Lazarus" or "North Korea" (zero attribution); "$352M stolen" as settled; "cold wallets breached" as fact; any vector ("insider," "phishing," "supply chain"); "users made whole" (promised, withdrawals still off).

**Clip question:** "Two custodians, one month, $670 million. Whose fault is it that you still don't hold your keys?"

### S — Shielded Bitcoin: Zcash in an OP_RETURN (Tyler, ≤5 min)

**Start:** "Sept 24: a whitepaper says Bitcoin can have Zcash-style private transfers with no soft fork, no operators, no bridges. Read the fine print."

- **What it is:** whitepaper and Delving post from [alloc] init (Misha Komarov's team; authors Clara Shikhelman, Mikhail Komarov, Aleksei Moskvin). **Not a BIP, not a soft fork.** A Zcash-style shielded-note metaprotocol: encrypted notes, nullifiers, Groth16 zk-SNARKs with a **trusted setup**, transfer envelopes posted in OP_RETURN. Bitcoin consensus verifies nothing; off-chain indexers replay history to derive state. [Whitepaper](https://www.allocinit.xyz/uploads/shielded-bitcoin.pdf) · [Delving](https://delvingbitcoin.org/t/shielded-bitcoin-private-transfers-on-the-bitcoin-l1/2912) · [Bitcoin Magazine](https://bitcoinmagazine.com/news/alloc-init-releases-shielded-bitcoin-proposal-for-private-bitcoin-transactions) · [Unchained interview](https://unchainedcrypto.com/bitcoin-could-get-zcash-style-private-transactions-without-a-soft-fork-misha-komarov-says/)
- **The catch, verbatim:** "Peg-in and peg-out... fall outside the scope of this paper." They're deferred to PIPEs v2, the team's witness-encryption scheme that locks a Schnorr key behind a SNARK condition. PIPEs v2's own paper: the constructions are "heuristic" and a ciphertext is "on the order of 338 TB." Komarov says ~8 TB now. [PIPEs v2](https://www.allocinit.xyz/uploads/pipesv2.pdf)
- **Also public:** "Transfer timing, arity, output grouping, fees, and carrier-transaction metadata remain public." ~700 vbytes per transfer, roughly 4× normal fees. Appendix D is "Opt-in KYC Evidence" via viewing keys.
- **Reaction:** none yet. Delving thread had 1 post and 0 replies at check time. Shinobi: "on par with something like Zcash shielded pools." Don't attribute takes to Poelstra, Sztorc, Rusty, Lopp, or Corallo. Same day, unrelated Delving thread "Softfork before GTA VI?" mourns lost covenant momentum. [Delving](https://delvingbitcoin.org/t/softfork-before-gta-vi/2913)
- **Debate:**
  1. **Jackson:** supply audit is "replay everything yourself or trust an indexer." Would a product ship that? Does the KYC appendix make it exchange-friendly or dead for the privacy crowd?
  2. **Chris:** trusted setup, heuristic witness encryption, terabyte ciphertexts. Which is the real attack surface? Is this Tornado Cash with extra steps, legally?
  3. **Tyler:** 700-vbyte OP_RETURN envelopes at scale meet Knots filter politics. Why not Lightning plus silent payments?
  4. **All:** is "no soft fork needed" a feature, or an admission that the covenant stalemate pushed R&D into unfalsifiable cryptography? Ties to Sztorc's line in C.
- **Do NOT say:** "BIP," "soft fork proposal," "Core devs reacted," "Zcash on Bitcoin is live," "no trusted setup."

**Clip question:** "Private bitcoin with no soft fork. The peg is an 8-terabyte ciphertext. Still excited?"

### M — Ethereum's builder duopoly and the ePBS fight (Chris, ≤4 min)

**Start:** "Three companies build about 90% of Ethereum's blocks. The fix ships next year. The fix might make it worse."

- **Numbers, pulled Sept 24 from relayscan (7 d):** Titan 55.5%, BuilderNet 18.0%, Quasar 16.7%, Eureka 3.9%. ~92% of blocks go through MEV-Boost. The "two builders, 95.7%" line is Dec 2024 (EigenPhi); beaverbuild is now inside BuilderNet at 0.14% standalone. [relayscan](https://www.relayscan.io/overview?t=7d) · [EigenPhi 2024](https://eigenphi.substack.com/p/mev-space-1-recap-breaking-the-ethereum-duopoly)
- **Mechanics in five lines:** validators sell each 12-second slot's building rights; builders bid ETH, highest wins, proposer signs the header; relays sit in the middle so the proposer can't front-run the builder; winner-take-all plus private order flow (Telegram bots, wallets, proprietary AMMs) compounds into 55/18/17; ePBS (EIP-7732, in Glamsterdam) removes the relay, puts the bid on-chain, payload lands 6 s later, a 512-member committee checks it arrived.
- **The live fight:** Sept 17 dev call, Potuz warns sybil "fake builders" can win bids and withhold payloads ("spin up a thousand builders, rotate them, offer very high bids, and not produce payloads"). Sepolia test Oct 6; mainnet unscheduled. Lido wants collateral-backed bids from anyone plus an allowlist for "trusted" bids; Commit-Boost says collateral is too capital-heavy; Titan says it'll keep using relays anyway. Neuder's conjecture: dominant builders keep dominating on reputation, ePBS or not. [CoinDesk](https://www.coindesk.com/tech/2026/09/18/ethereum-confirms-glamsterdam-dates-but-warns-fake-builders-could-stall-the-chain) · [Lido](https://research.lido.fi/t/ethereum-mev-extraction-and-rewards-part-2-revisiting-stance-in-light-of-epbs/11818) · [ePBS distilled](https://ethresear.ch/t/epbs-distilled/25800) · [CryptoSlate on collateral vs trusted](https://cryptoslate.com/ethereum-builders-face-a-choice-between-locking-up-too-much-cash-or-relying-on-trusted-brokers/)
- **Who gets the money:** Bitquery study (single source): builders receive $5.24 per $1 the network burns; split 49% builders / 41% trading operators / 9% burn. [CryptoSlate](https://cryptoslate.com/ethereum-arbitrage-study-reveals-builders-receive-5-for-every-1-burned-by-the-network) · MPBC went live Sept 16, letting other teams append to the winner's block, ~3% of blocks day one. [MPBC](https://docs.blockspace.forum/mpbc/)
- **Debate:**
  1. **Tyler:** Foundry + AntPool is ~45% of Bitcoin hashrate; Titan + Quasar is ~72% of Ethereum blocks. Why does Bitcoin's pool concentration draw louder alarm? Is out-of-band fee flow (Slipstream-style) Bitcoin's MEV-Boost?
  2. **Chris:** Lido's allowlist for trusted payments is KYC for builders. Does ePBS reduce trust or formalize it?
  3. **Jackson:** is AI-agent order flow the next capture vector? MPBC's "append to the winner's block": decentralization or renting shelf space from Titan?
  4. **All:** $5 to builders per $1 burned. Burn the MEV, or does that just move the rent to stakers?
- **Do NOT say:** "beaverbuild is a top builder"; "two builders have 95%" as current; a Glamsterdam mainnet date.

**Clip question:** "Ethereum is decentralized. Three companies build the blocks."

### W — Wildcard: 5× points on PEPE (All, ≤1 min)

- Visa closes the memecoin-rewards loophole (Sept 19): Crossmint (powering Fomo and Robinhood Wallet via Checkout.com) coded memecoin buys as MCC 5815 "digital media," so degens earned card points on shitcoins. [The Block](https://www.theblock.co/news/regulation/2026-09-19-visa-to-close-crossmint-memecoin-rewards-loophole-following-the-block-investigation-report-415866)
- Second bit if time: Meta admits Muse copied OpenClaw's config files, SOUL.md included. Jackson has a SOUL.md. [TechCrunch](https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/)

## Fresh-news bench

- **CLARITY is dead; the agencies go alone (Chris, 3 min if J runs short).** Cloture failed 49–50 on Sept 15 over stablecoin rewards vs. bank deposits plus Trump-ethics provisions. White House Sept 22: "no time to waste," regulators act now. GENIUS rulemaking past its July deadline; ABA still asking for time. Visa survey: stablecoin intent 36%→56% with bank-level protections. ECB wants MiCA's yield ban extended to lending/staking. Binance buys a $100M Circle stake. Korea: Kakao Pay / KakaoBank Fireblocks MoU; SBI–Kyobo yen↔won test skipped USD. [Lummis](https://www.coindesk.com/policy/2026/09/22/democrats-chose-visceral-hatred-for-donald-trump-over-crypto-clarity-act-lummis-says) · [Critics](https://www.coindesk.com/policy/2026/09/21/banks-overseas-crypto-hubs-gain-from-clarity-act-s-senate-defeat-critics-say) · [White House](https://www.coindesk.com/policy/2026/09/22/crypto-market-structure-can-t-wait-for-shot-at-post-election-clarity-act-surge-white-house) · [Visa survey](https://www.theblock.co/news/regulation/2026-09-23-stablecoin-adoption-intent-rises-from-36-to-56-with-bank-level-protections-visa-says-416136). Question: is "no yield" now the global default, and is rules-by-agency worse for issuers than a bad law?
- **DOJ probes Binance for knowingly allowing Iran-linked trades** (Bloomberg, Sept 22; Binance silent). Treasury sanctioned Iranian exchange BitBank over IRGC BTC (Sept 17). Haruko breach leaked API keys of 15 crypto funds (Sept 18). Chris, 2 min if E runs short.
- **Coinbase post-quantum custody plan** for ~$250B (Sept 22–23). Pairs with C's quantum thread if Tyler wants a concrete counterexample to "nobody's moving."
- **Circle Arc mainnet** (Sept 16). Issuer-owned chain vs. the rails debate from Ep 15 Topic K.
- **Ex-Anthropic "cousin":** no fresh news found. Don't invent a follow-up.

## Evergreen bench (no news peg)

- **Open vs. closed weights.** Fresh peg this week: the "fear open weights" theory in B and DeepSeek v4.1 Flash on hacking evals.
- **Secure enclaves:** aired in Ep 15 (Muse + attestation). Retired from the bench; the Muse backdoor is the callback. Replacement candidate: **"grade the tape"** (salvaged from Ep 10).

## Host pre-read / before recording

- **Everyone:** read the [Anthropic enzyme post](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) and skim the [HN thread](https://news.ycombinator.com/item?id=49820134). Pick one theory from the B table and bring the strongest counter to someone else's.
- **Jackson:** read the [Transluce report coverage](https://fortune.com/2026/09/24/openai-more-rogue-ai-agents-hacking-websites-cryptoexchange-in-september-research-report-transluce/); check for any OpenAI or Services Australia statement dated after Sept 24. Actual perp result; the 210M-token cost estimate at list prices; one line on Plugin4Shell exposure. Decide the week-three model question before tape.
- **Chris:** refresh Bitget at record time: incident report, vector, fund denomination, withdrawals status, any Tether/Circle freeze. Then [Amazon block](https://techcrunch.com/2026/09/21/metas-ai-agent-has-been-blocked-from-using-amazon-com/), the Muse zero-day coverage, [Visa survey](https://www.theblock.co/news/regulation/2026-09-23-stablecoin-adoption-intent-rises-from-36-to-56-with-bank-level-protections-visa-says-416136). Bring the enclave callback as one sentence.
- **Tyler:** skim the [Shielded Bitcoin whitepaper](https://www.allocinit.xyz/uploads/shielded-bitcoin.pdf) sections on the peg and Appendix D; check the Delving thread for replies. Refresh Liquid's peg-out status and the last-15% figure at record time; confirm the House FSC reserve vote and the Sztorc quote from primary sources before citing; bring the hashrate disagreement with both sources named.
- **Fact guardrails:** no "new gene-editing tool"; no stock percentages; no price or ETF numbers anywhere in C; no PayPal–Muse as confirmed; no Liquid or Bitget attacker attribution; Bitget's $351.6M and the ~$190M on-chain figure stay separate; Shielded Bitcoin is not a BIP; no employer names.
- **Close:** actual perp result, one prediction each, and only promise next week's topic if a host takes it.
