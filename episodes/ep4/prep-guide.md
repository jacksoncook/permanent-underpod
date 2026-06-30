# Permanent Underpod — Ep 4 — Topics

**Record: next up after Ep 3 · Oakland — all three in person for the first time (no laptops).**
**Panel: Jackson (Korea markets) · Chris (stablecoins / DEXs / MEV) · Tyler (Bitcoin & Lightning)**

> **New format note.** Starting this episode we're dropping the hour-by-hour prep guide.
> This file is just a **list of candidate topics** (pick/order on the day) plus **pre-read
> references at the bottom**. That's it. Cold open still recorded LAST and cut to the front.
> Not affiliated with any employer. **Nothing here is financial advice.**

## Carryover from the end of Ep 3 (the promises we made on camera)

1. **All three in person, in Oakland** — "our final pod with all three of us in person… nobody's
   laptoped up this week. It's a milestone." Pays off the running "someone's always dialing in
   over the laptop" gag (Ep 1 Tyler remote, Ep 2 Chris remote from CDMX). Savor it / lampshade it.
2. **Agentic payments "for real this time"** — Ep 3's literal promise: *"Next episode will be
   agentic payments… we're going to pay for a burrito with the Perp of Fortune."* i.e. actually
   route a real-world payment through an AI agent (and/or off the live Hyperliquid $DRAM position).
3. **Jackson's contrarian take finally comes due** — Tyler took Contrarian Corner in Ep 1 and Ep 3.
   Jackson owes one. Plan: it lands on the MEV / Jared segment (see Topic B).

---

## Candidate topics

**A. Agentic commerce — is it actually viable? (the owed "agentic payments" callback)**
Lead: All. The Ep 3 promise comes due — try to make an AI agent complete a real purchase live
(stretch goal: fund it off the Perp of Fortune position). Frame the landscape without the jargon
soup: OpenAI + Stripe's **Agentic Commerce Protocol** / Instant Checkout in ChatGPT, **Visa's
Trusted Agent Protocol**, **Mastercard's Agent Pay for Machines (AP4M)**, and **Tempo's Machine
Payments Protocol** for agent-to-agent settlement. The honest question: is this real infrastructure
now, or a demo that falls over the second you hand it real money? Do the dumb thing on camera and
find out.

**B. MEV & the jaredfromsubway.eth "sandwich" saga** — *Chris segment, Jackson's contrarian take*
Lead: **Chris** (explains MEV + sandwich attacks, jargon rule applies). **Jackson** brings the
contrarian take owed since Ep 1. The hook: Ethereum's most notorious sandwich bot —
**jaredfromsubway.eth**, responsible for ~70% of all sandwich attacks for the better part of a
year — got **drained of $7.5M on June 20–21, 2026** in a *reverse honeypot* (someone deployed 66
fake token contracts, tricked the bot into approvals, and swept it in one tx). The predator got
sandwiched. Contrarian angle for Jackson to pick from: MEV is just a tax that proves DEXs work as
designed / the bot getting robbed is poetic but changes nothing / "counter-MEV" is the same
extraction wearing a hero costume.
> *(Dictation check: read "Meb" as **MEV** and "the Jared sandwich situation" as
> **jaredfromsubway.eth**. Correct me if that's not the bit.)*

**C. "Open USD" — what even is it? (it doesn't mean anything)**
Lead: Chris / All. The runner: the name **"Open USD" is hopelessly overloaded.** *Today (June 30)*
a consortium called **Open Standard** — **Stripe, Visa, BlackRock + ~140 businesses** — announced
**OUSD ("Open USD")**, a yield-bearing dollar stablecoin built to rival Tether and Circle (Circle
stock dropped ~13% on the news). Meanwhile **OpenUSD** has *for years* meant **Pixar's Universal
Scene Description** — a 3D graphics file format with nothing to do with dollars. So: a stablecoin
and a 3D file format share a name, and the new one's pitch is basically "a dollar, but open." The
bit writes itself — *what does "open" even buy you here?*

**D. OUSD vs. Stripe's Tempo — rivals, or two ends of the same Stripe stack?**
Lead: Chris / Jackson. Stripe is somehow in **both**: **Tempo** is the L1 *rail* (no gas token,
fees paid in stablecoins, launched mainnet March 18, 2026), and **OUSD** is the consortium *asset*.
Are they competing, complementary, or is Stripe just hedging every layer of the stack? Where does
**USD1** (the first stablecoin issued natively on Tempo) fit? Good "follow the money / follow the
moat" segment.

**E. Tether's US play: USAT vs. USDT**
Lead: Tyler / Chris. **USA₮ (USAT)** launched Jan 27, 2026 — Tether's GENIUS-Act-compliant,
US-regulated stablecoin (issued via **Anchorage Digital Bank**, **Cantor Fitzgerald** as reserve
custodian, Bo Hines running it), while **USDT** stays the offshore global product. Worth it?
The tension: is a domesticated, regulated Tether a genuine Circle-killer, or a compliance hedge
that splits Tether's own brand — and does any of this matter to the OUSD launch in Topic C/D?

**F. GPT-5.6 gets the Fable treatment**
Lead: All (AI news beat; recurring "is Fable back?" runner from Ep 3). **GPT-5.6** (Sol / Terra /
Luna) dropped **June 26, 2026** — but gated to ~20 government-approved companies "at the behest of
the US government," with Sol pitched as a cybersecurity / vuln-research monster. Meanwhile
**Anthropic's Fable 5** shipped **June 9**, generally available, and is SOTA on nearly every
benchmark (80.3% SWE-bench Pro vs GPT-5.5's 58.6%). So the frontier model everyone *can* use is
already out, and OpenAI's answer is locked behind a 20-company door. Tie-in: a vuln-hunting flagship
model in the same week a $7.5M MEV bot got drained (Topic B) basically begs the question of who's
auditing whom.

---

## Pre-read references (optional prep)

Starting points pulled from current reporting — skim what's relevant to the segment you're leading.

**Agentic commerce (Topic A)**
- OpenAI — Buy it in ChatGPT: Instant Checkout & the Agentic Commerce Protocol: https://openai.com/index/buy-it-in-chatgpt/
- Stripe — Instant Checkout + ACP (co-developed with OpenAI): https://stripe.com/newsroom/news/stripe-openai-instant-checkout
- Agentic Commerce Protocol spec (OpenAI/Stripe): https://github.com/agentic-commerce-protocol/agentic-commerce-protocol
- Digital Commerce 360 — how Visa & Mastercard are approaching agentic commerce: https://www.digitalcommerce360.com/2026/04/02/visa-mastercard-in-agentic-commerce/
- CoinDesk — Tempo goes live with an AI-agent (Machine Payments) protocol: https://www.coindesk.com/tech/2026/03/18/stripe-led-payments-blockchain-tempo-goes-live-with-protocol-for-ai-agents

**MEV / jaredfromsubway.eth (Topic B)**
- Chainalysis — Sandwich Attack: How JaredfromSubway Lost $7.5M: https://www.chainalysis.com/blog/sandwich-attack-jaredfromsubway-hack/
- CoinDesk — Ethereum's biggest sandwich bot drained of $7.5M in an ironic exploit: https://www.coindesk.com/tech/2026/06/21/ethereum-s-biggest-sandwich-bot-drained-of-usd7-5-million-in-ironic-exploit
- Unchained — bot loses $7.5M to its own trading logic: https://unchainedcrypto.com/sandwich-bot-jaredfromsubway-eth-loses-7-5-million-to-its-own-trading-logic/
- The Block — jaredfromsubway.eth is back with a new MEV bot: https://www.theblock.co/post/312245/jaredfromsubway-eth-is-back-with-a-new-mev-bot-and-new-sandwich-attacks

**"Open USD" / OUSD + the name collision (Topic C)**
- Fortune — Stripe, Visa & 140+ businesses to launch OUSD to rival Tether and Circle: https://fortune.com/2026/06/30/stripe-visa-stablecoin-rival-ousd-tether-circle/
- (Name collision) Alliance for OpenUSD — Pixar's Universal Scene Description 3D format: https://aousd.org/

**OUSD vs. Tempo (Topic D)**
- Tempo — official site (the blockchain for stablecoin payments): https://tempo.xyz/
- Fortune — Tempo launches an advisory unit to push stablecoin adoption: https://fortune.com/2026/04/21/stripe-and-paradigm-tempo-advisory-stablecoin-adoption/
- Crypto Times — World Liberty's USD1 launches natively on Tempo: https://www.cryptotimes.io/2026/05/08/world-liberty-financial-launches-usd1-stablecoin-natively-on-stripe-backed-tempo-l1-blockchain/
- Sean Goedecke — an unofficial FAQ for Stripe's Tempo (good plain-English primer): https://www.seangoedecke.com/tempo-faq/

**Tether USAT (Topic E)**
- Tether — official USA₮ launch announcement: https://tether.io/news/tether-announces-the-launch-of-usat-the-federally-regulated-dollar-backed-stablecoin-made-in-america/
- Cointelegraph — Tether launches USAt under the GENIUS Act: https://cointelegraph.com/news/tether-launch-usat-regulated-stablecoin-us
- PYMNTS — Tether's GENIUS-Act-compliant dollar stablecoin: https://www.pymnts.com/blockchain/2026/tether-launches-dollar-backed-stablecoin-designed-to-comply-with-genius-act/

**GPT-5.6 vs Fable 5 (Topic F)**
- OpenAI — Previewing GPT-5.6 Sol: https://openai.com/index/previewing-gpt-5-6-sol/
- Axios — OpenAI releases GPT-5.6 under government-imposed restrictions: https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump
- Anthropic — Claude Fable 5 & Mythos 5: https://www.anthropic.com/news/claude-fable-5-mythos-5
- Tom's Hardware — Fable 5 is SOTA on nearly all tested benchmarks: https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-fable-5-brings-mythos-to-the-masses-anthropics-next-frontier-model-is-state-of-the-art-on-nearly-all-tested-benchmarks
