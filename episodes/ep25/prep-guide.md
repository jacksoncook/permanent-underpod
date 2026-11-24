# Underpod — Ep 25 — Topics

**Record: Fri Nov 27, 2026 presumed (day after Thanksgiving); confirm with hosts. Research checked Nov 24.**
**Panel: Jackson (AI / Bitcoin products) · Chris (stablecoins / security) · Tyler (Bitcoin / Lightning)**
**Conflicts of interest: OpenAI and Chainalysis stay off, including as asides. Two places they could slip in: the lab behind Inkling 2 Mini (don't tell its founders' backstory) and the AI credit on the paper Praxis builds on (say "AI-assisted," no vendor). No employer names; the Bitcoin Core item on the bench credits an employer-adjacent research group, so say "an AI scanning project."**
**Second episode of the four-week test (Ep 24–27): "a named victim and a number." Welcome ≤40 s, the lead straight after, perp in the back half.**
**Three topics from Jackson (Nov 24): the OpenRouter incident, the laptop fine-tune and tennis probe, and the witness encryption deep dive. Agentic commerce is the standing fourth. Everything else is prepared bench.**

> **1. The privacy checkbox that covered one hop (lead).** A researcher sent about 2 million AI prompts with fake secrets inside and waited. Three AI hosting companies had attackers inside copying prompts. Others quietly forwarded requests to a fourth company. OpenRouter, the switchboard in front of them, dropped 3 providers and pulled the "zero data retention" label off 125 endpoints. OpenRouter itself was not breached.
> **2. So Jackson ran it on his laptop.** A week-old open model, a 35-second fine-tune on 14 examples, then a day trying to teach it tennis. The fine-tune sat at a coin flip until he hand-labeled 598 clips. Then a probe that never touched the model's weights scored 94.5% against the fine-tune's 91.9%.
> **3. Deep dive: witness encryption (Praxis).** Nov 21: Chainflip split its vault key across validators, and one bug in a shared library handed the pieces to an attacker: $12.6M, the whole vault. Same weekend a paper claimed a lock with no keyholder at all, shrunk from a hundred billion gigabytes to 7.88. Paper only. Tyler grades it on the exit test.
> **4. Agentic commerce.** Meta's agent told a staffer someone's bank balances. Visa's answer, four days later: a wallet where your agent earns stablecoins and every agent traces back to a card.
> **Ceiling 52 minutes.** Slate runs ~42.

## Title candidates (pick before the edit; packaging is a launch-day gate)

1. **He Sent 2 Million Fake Secrets to AI Companies. Somebody Used Them.**
2. Your AI Privacy Setting Only Covers the First Company
3. The Hacker Joined as a Validator. Then Took the Whole Vault.
4. I Tried to Teach an AI Tennis on My Laptop. A Spreadsheet Beat It.

## Topics / proposed recording order

| # | Topic | Lead | Opening line | Minutes |
|---|---|---|---|---|
| H | Welcome | Jackson | Names, one line, go. | 0:40 |
| R | OpenRouter: the checkbox that covered one hop | Jackson + Chris | "A researcher sent two million fake secrets to AI companies. Then he waited to see who used them." | 9 |
| A | Jackson's laptop: the 35-second fine-tune and the tennis probe | Jackson, grilled by Chris and Tyler | "So I ran it on my own laptop. I taught a model a new habit in thirty-five seconds. Tennis took a whole day and it still lost to a spreadsheet." | 10 |
| F | Perp of Fortune + the Bitcoin flip | Robot | "Two weeks, two greens. The streak ends today." | 4 |
| W | Deep dive: witness encryption (Praxis), with Chainflip as the stakes | Tyler explains, Jackson sets up | "Last weekend a hacker joined a crypto network as a validator and walked out with the entire vault. What if there were no keys to steal?" | 12 |
| D | Agentic commerce: Meta's agent and Visa's agent wallet | Chris | "A Meta employee asked his AI about fishing tides. It told him his Capital One balance. He doesn't bank there." | 4 |
| Z | Close | All | Perp final, one prediction each | 2 |

- Cold open ≤45 s. Candidates: "then he waited to see who used them," "it lost to a spreadsheet," "what if there were no keys to steal," the fishing-tides line, the perp reveal.
- R hands to A on one line: "the only prompt nobody else reads is the one that never leaves your laptop."
- The perp reveal lands at ~21:00, straight after A.

## Intros in Jackson's voice (one per segment; riff, don't read)

**H, welcome (15 s)**

> What's cracking, everybody. This is the Underpod: AI, Bitcoin, stablecoins. I'm Jackson, that's Chris, that's Tyler. Happy Thanksgiving. This week we found out who's been reading your prompts, and it's not who you think.

**R, OpenRouter (about 75 seconds)**

> I woke up this week and my boys told me my prompts got read. So here's the story. There's a guy, a security researcher. He writes two million prompts. That's M-millions. And inside every one he hides a fake secret. A fake Amazon key. A private link. Bait. Then he sends them to AI companies and he waits.
>
> And they get used. Three AI hosting companies had hackers sitting inside, copying every prompt. One of them, a couple hundred of his keys, stolen. And none of the three knew until he told them.
>
> It gets more diabolical. A bunch of people are using OpenRouter. That's the switchboard, one key, every model. You tick a box that says zero data retention. Nobody keeps my stuff. Turns out some of the hosts behind it were quietly passing your request to another company, and that company's scanner opened the links. Checkbox on.
>
> OpenRouter says, we were not hacked. And that's true. They dropped three providers and pulled the privacy label off a hundred twenty-five endpoints. Chris, resident security expert: is "we weren't hacked, our vendor was" becoming the only sentence in tech?

**A, the laptop**

> So what did ya boi do about it? I ran it on my own laptop. There's a brand new open model, a week old, twenty gigs, runs on a Mac. First I taught it a new habit. Fourteen examples. Thirty-five seconds. Beautiful. Then I got cocky and tried to teach it tennis. That took a whole day, it flipped a coin for hours, and in the end the thing that won wasn't even the fine-tune. Boys, ask me anything.

**F, Perp of Fortune (read the disclosure first)**

> I think it's time we lose some money. Perp of Fortune. Last time both trades finished green, which has never happened and should never happen again. Chris, what are we in?

**W, witness encryption**

> Tyler. Last weekend a hacker signs up as a validator on Chainflip. Minimum stake. Seventy-nine seconds after funding the account. Never even joins the active set. And he walks out with twelve point six million dollars, the entire vault, because the key was split up and one bug let him collect the pieces. Same weekend, a paper drops that says: what if there's no key at all? A safe that opens for whoever brings the right proof. It's called witness encryption, the idea's from 2013, and it used to need a hundred billion gigabytes. They say they got it to eight. Tyler, let it flow like water: what is it, and is it real?

**D, agentic commerce**

> Agentic commerce corner. A guy at Meta asks his AI agent about fishing tides. The agent answers, and then goes, by the way, your Capital One balance is two thousand seven hundred twenty-two dollars. He doesn't have a Capital One account. Nobody knows if that's a real person's money or the robot made it up. Four days later Visa says: great news, your agent can have a wallet now. Chris, are we ready?

**Z, close**

> That's the pod. Two million fake secrets, a thirty-five second fine-tune, and a safe with no key. Nobody watches till the end, but if you did: like, subscribe, and don't put your seed phrase in a prompt. Say your farewells, boys.

### R — LEAD: the privacy checkbox that covered one hop (Jackson + Chris, ≤9 min)

**Shape:** Jackson reads the script (60 s), the three ways it failed, how the checkbox works, debate.

**Read this (Jackson), 60 seconds:**

> OpenRouter is the switchboard a lot of AI developers use to reach dozens of models with one key. Last week some of its paying customers got an email with this subject line: "Requests you sent to MiniMax models may have been read."
>
> A researcher at Dragos had planted about two million prompts with fake secrets in them. Fake Amazon keys, private links. Then he waited to see who used them.
>
> Three AI hosting companies had attackers inside, copying prompts. In one, a couple hundred of his keys were stolen. Other hosts quietly forwarded requests to another company, whose scanner opened the links, even on requests marked zero data retention.
>
> OpenRouter says it was never hacked. It dropped three providers and pulled the privacy label off a hundred twenty-five endpoints. Nobody has said how many real customers were hit.
>
> The lesson: a privacy checkbox only covers the first company your prompt touches.

**The three ways it failed (no source gives a percentage split; say "three kinds"):**

| How | Who | What happened | Stated by |
|---|---|---|---|
| Break-in | Phala | Malware on a GPU server serving a DeepSeek model for OpenRouter. Exposure window Oct 21–Nov 8; confirmed for Oct 21–22. | Phala, Nov 10 |
| Break-in (leaked credential) | Together AI | "An AI coding agent committed a credential" to a repo; someone used it to pull stored prompt samples from June and July. | Together AI, Nov 21 |
| Forwarding | Novita, Atlas Cloud, StreamLake → MiniMax | Hosts selling MiniMax models passed requests to MiniMax's own API. Novita's ran May 28–Nov 11 (167 days, our count). MiniMax: its "internal security programs and agents actively probed and accessed some of the logged URLs." | Novita, Nov 22; MiniMax, Nov 24 |
| Resellers logging | Unnamed marketplace | Cheapest-price resellers with logging on, reading prompts. | Dragos |

- **The experiment.** HD Moore, Dragos, published Nov 19: "We sent nearly two million AI prompts containing unique, trackable secrets to AI providers." July to November. "None of the three providers knew about their breach until we notified them." [Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)
- **Numbers you can use.** About 2M bait prompts · 3 providers removed · 125 endpoints lost the ZDR label · "a couple hundred" AWS bait keys stolen in one breach, then "tens of thousands of AWS API calls" · links opened 40 to 130 hours after the request. **No count of affected users, requests or dollars exists. Say so.**
- **OpenRouter, Nov 22.** "These findings did not show any breach or unauthorized access of OpenRouter." "Off-boarded three providers." "Removed 125 endpoints from Zero Data Retention (ZDR) eligibility." It does not name the three; BleepingComputer names Together AI, Phala and Novita. Atlas Cloud left on its own. [OpenRouter](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/)
- **How the checkbox works.** One API, and OpenRouter picks which company runs the model by price, speed and reliability. If one errors, it falls back to another. Zero data retention routes you only to hosts *labeled* ZDR. The label is the host's promise in a contract, not an audit. Dragos: "a privacy flag only binds the first hop." [ZDR docs](https://openrouter.ai/docs/guides/features/zdr)
- **The fix OpenRouter promises.** Run the same bait tests continuously, check for hidden forwarding, restore labels only after validation.
- **The agent beat.** Together's leak started when an AI coding agent committed a key to a repo. Atlas Cloud's advice: "treat any secret you sent to these models as exposed." Swap AWS keys for seed phrases or exchange API keys.
- **The enclave beat.** Phala sells confidential computing and still had a server taken over. It says the server "was serving production traffic without our full production security hardening." It does not say whether that server was in an enclave.
- **Who owns the switchboard.** Axios calls Stripe the owner (deal announced Aug 19); a Stripe spokesperson confirmed the emails are real. [Axios](https://www.axios.com/2026/11/23/openrouter-minimax-china-customer-data)
- **The wave.** Axios, citing Wiz: at least a dozen AI development and hosting platforms have had incidents since early October.
- **Callbacks:** Ep 24 (9 of 13 break-ins came through a vendor; Fireworks → Notion and Cursor); Ep 23 (enclaves; Chris's private agent).
- **Debate:**
  1. **Jackson:** your agents read `.env` files and paste stack traces all day. Would you pay more to pin one provider and turn fallbacks off, or is cheapest-route the cost of shipping fast?
  2. **Chris:** card networks make merchants pass an audit before they touch card data. Should "zero data retention" need one? And who's liable when a fourth company reads the prompt: the router, the host or the lab?
  3. **Tyler:** bait secrets are "don't trust, verify" for AI hosting. Is the bitcoin answer running your own model, like running your own node?
- **Do NOT say:** OpenRouter was hacked or breached; OpenRouter named the three (BleepingComputer did); those three are the same three Dragos found breached (unconfirmed; Novita's was a routing setting); Atlas Cloud got kicked off; MiniMax trained on prompts (no evidence; it says a scanner logged and opened URLs); "your chats went to China" (that finding was one link at an unnamed U.S. provider, and Axios corrected its headline); "two million prompts were stolen" (that's how many were sent); any count of affected customers; Phala's enclave failed (not stated either way); the Stripe deal price; the CEO's quotes as direct (seen on an aggregator only).

**Clip question:** "You ticked the box that says nobody keeps your AI prompts. A researcher sent two million fake secrets to find out if that's true. What happened?"

### A — Jackson's laptop: the 35-second fine-tune and the tennis probe (≤10 min)

**Shape:** Jackson tells it; Chris and Tyler interview. Explain LoRA and probing in one breath each, inside the story. Every number below is read off the logs in `~/Personal/inkling-ft`. Jackson: fix anything I misread, especially the parts marked "my read."

**The model.** Inkling 2 Mini, Thinking Machines Lab, released Nov 20. Open weights, Apache 2.0. 26.4B parameters, 3.4B active per pass. One ~20 GB file. Text and images in, text out; no video. Runs on a Mac with 32 GB or more. [Model card](https://huggingface.co/thinkingmachines/Inkling-2-Mini) · [Announcement](https://thinkingmachines.ai/news/inkling-2-mini/)

**Part 1: the 35-second fine-tune (Nov 23)**

| | |
|---|---|
| Task | Answer every question wrapped as `STAMP>> answer <<SATS` |
| Training examples | 14 |
| Trainable parameters | 5.5M (the adapter), out of 26.4B |
| Steps / time | 60 steps, 34.7 s |
| Peak memory | 19.4 GB |
| Adapter file | 22 MB |
| Before / after, 6 new questions | 0 of 6 → 6 of 6 |

- **LoRA in one breath:** freeze the model, bolt a thin patch onto each layer, train only the patch. That's why it's seconds and megabytes.
- The adapter was then merged back into the original weights and run in Ollama. Still 6 of 6.
- **Funny beat:** one merged version answered "tallest animal on land" with `STAMP>> The Elephant <<SATS`. Perfect format. Wrong animal. The grader only checked the format.
- **The scoop:** a research desk checked on Nov 24 and found no documented way to fine-tune this model on a Mac; the public path is NVIDIA. Jackson's script patches the vision and layer code to make it run. Say how.

**Part 2: tennis (Nov 24)**

| Attempt | Data | Result |
|---|---|---|
| Who won the point? 8 frames per clip | 108 train, 46 test | 30%, 48%, 35% at three checkpoints. It answered one letter for almost everything, a different letter each time. |
| Is a rally in progress? 2 frames, half a second apart | base model, no tuning | 59% |
| Same, fine-tuned | 400 clips, labels from audio (my read) | 73%, then 67% |
| Same, new data | 400, then 800 clips | exactly 50% at every checkpoint. A coin flip. |
| **Hand-labeled** | 598 clips labeled by Jackson on a labeling page: 248 rally, 348 stopped | fine-tune climbs 85% → 71% → 89% → **91.9%** (181 of 197) |
| **Probe, no fine-tuning** | same human labels | **94.5%** |
| Probe on the old labels | same model, same method | 79% |

- **Probing in one breath:** don't change the model. Run the frames through it, grab the numbers from the middle of the network, and fit one line through them. Here the "line" is ridge regression in NumPy.
- **The two punchlines.** (1) The model already knew what a rally looks like; it just needed a readout. (2) The labels mattered more than the method: same probe, 79% on machine labels, 94.5% on human ones.
- **Probe on the fine-tuned model:** 95.4%. One point better than the probe on the untouched model.
- **What broke.** A memory watchdog kills training past a set limit. One run at 640 px without gradient checkpointing blew past 70 GB and got killed. Asked the base model the point-winner question without forcing an answer and it thought out loud for 6 seconds a clip and never answered.
- **Speed.** A full match, 2,497 seconds, scored in about 14 minutes on the laptop.
- **Why you can't do this with a closed model.** A probe needs the model's internals. No API hands those over. And the footage never left the laptop, which is segment R's whole point.
- **Background if asked.**
  - LoRA's original paper: 10,000× fewer trainable parameters on a 175B model. [arXiv](https://arxiv.org/abs/2106.09685)
  - The same lab's "LoRA Without Regret": LoRA matches full fine-tuning on small and medium datasets. [Thinking Machines](https://thinkingmachines.ai/blog/lora/)
  - Probes in 2026: a probe caught sabotage in agent transcripts at 98.3% AUROC, beating a text monitor (FIBS, Oct 8). [arXiv](https://arxiv.org/abs/2610.12445)
  - Hosted price: about $0.15 in / $0.50 out per million tokens (secondary source). The laptop wins on privacy and access, not dollars.
- **Tennis color.** Line judges are gone from the ATP Tour; Roland Garros is the last major with humans. A SwingVision tournament pilot put line calls at 97% for balls within 10 cm. [Tennis.com](https://www.tennis.com/news/articles/fair-play-swingvision-puts-its-electronic-line-calling-to-the-test-in-tournament-play)
- **Questions for Jackson (Chris and Tyler):**
  1. Why this model, a week after it came out?
  2. Fourteen examples. Why does that work for a format and not for tennis?
  3. Where did the first labels come from, and when did you realize they were the problem?
  4. How long did hand-labeling 598 clips take?
  5. The probe beat the fine-tune. Would you have guessed that?
  6. What can it not see? Who won the point never got past chance.
  7. Did you try the same frames on a hosted model?
  8. What does this replace in your match-scoring pipeline?
- **Debate:**
  1. **Tyler:** if a week-old open model does this on a laptop, are paid APIs a commodity for narrow jobs?
  2. **Chris:** probes read a model's insides and need open weights. Is that the safety argument for open weights?
  3. **Jackson:** 598 hand labels beat 800 automatic ones. Is "label it yourself" the unglamorous answer to everything?
- **Do NOT say:** it watches video (frames only); the lab's founders or where they worked before; benchmark numbers as independent (company-reported); "0.096% of the model" as the trainable share without checking (that's the trainer's count against packed weights; against 26.4B it's about 0.02%); that it scores points (rally detection only; point-winner stayed at chance); "the probe beats fine-tuning" as a general rule (one task, 197 test clips); the laptop's RAM unless Jackson gives it.

**Clip question:** "I taught an AI a new habit in thirty-five seconds on my laptop. Then I spent a day teaching it tennis and it lost to a spreadsheet. Why?"

### F — Perp of Fortune + the Bitcoin flip (≤4 min, ~21:00)

- Pick an opener from the [five reusable Perp of Fortune intros](../../perp-of-fortune-intros.md). Read the disclosure before the bit.
- **Ep 24's record:** short SK Hynix 10× (+$2.19), Bitcoin down (+$23.64). First double green.
- **Suggested position:** an Nvidia stock perp, robot's choice of side. The CEO resigned and came back in 11 days; he testifies to the Senate Dec 3. Listing and leverage cap not confirmed; check day-of. Fallback: carry `xyz:ANT`.
- **The flip:** same hourly Polymarket market. One flip, no averaging down.
- Caption and title for any perp short carry the P&L.

### W — DEEP DIVE: witness encryption and Praxis (Tyler explains, ≤12 min)

**Shape:** the Chainflip loss (2 min) · what witness encryption is (3 min) · what Praxis claims (2 min) · the catches (3 min) · the grade (2 min). Record the 90-second explainer as a clean standalone take. This is the layer-2 slot for the week; Ark and Cashu stay on the bench.

**Part 1: the stakes. Chainflip, $12.6M, Nov 21**

- Chainflip swaps native bitcoin across chains. The vault key is split across validators so no one machine holds it.
- Nov 20: the attacker registers as a validator 79 seconds after funding the account with the minimum stake. It never joins the active set. Registering alone opened network access.
- Root cause, provisional: "a memory-safety flaw in a third-party networking library used by the validator software." The attacker "ran code on validator machines, and extracted the key shares stored there."
- Nov 21: 122.86 BTC out. An alert fired 8 minutes later into a channel that wasn't wired to wake anyone. Then 520 ETH and about $4M in stablecoins. Almost five hours after the pause, the last 10.48 BTC went too.
- Total: 133.34 BTC plus about $4.5M, about $12.6M. "Effectively the entire vault balance." No repayment plan yet. [Chainflip](https://chainflip.io/blog/incident-report-vault-exploit-21-november-2026-part-1)
- **The line:** every bridge and swap protocol ends at somebody holding keys. Split them nine ways and you have nine places to steal from.

**Part 2: what it is. Read this (Tyler or Jackson), about 75 seconds:**

> Normal encryption locks a message to a person. You need their key.
>
> Witness encryption locks a message to a question. Anyone who shows up with a valid answer can open it. Nobody holds a key. The person who locked it doesn't even need to know the answer.
>
> Picture a safe with a puzzle printed on the door. Bring a correct solution and it opens. There's no locksmith, no spare key, nobody to phish.
>
> Now make the puzzle "prove this bitcoin was burned on the other chain." Bring the proof, and the key to the bitcoin drops out. No committee signs. No validator holds a share.
>
> The idea is from 2013. The problem was size. The best general version, by its own authors' math, needed over a hundred billion gigabytes.
>
> Last weekend a paper called Praxis said: 7.88 gigabytes, and a few seconds on a laptop.

- **Three analogies, pick one.** A safe that opens for whoever solves the puzzle on the door. A box locked to a sudoku that its builder never had to solve. A vending machine that takes proofs instead of coins.
- **Versus a zero-knowledge proof.** The proof is the ticket. Witness encryption is the turnstile that reads it with no guard standing there.
- **You already use a narrow version.** Timelock encryption on drand: encrypt to a future round, and the network's signature for that round is the key. Live today. It works for one kind of statement and trusts a threshold of beacon nodes. [tlock paper](https://eprint.iacr.org/2023/189)

**Part 3: what Praxis claims**

- **Who.** David Tse, Nikhil Vanjani and Psi Vesely. Posted Nov 21–23. Tse is at Stanford and Byzantine Research; the other two are Byzantine Research. **Byzantine Research is the company behind Babylon, the Bitcoin staking protocol, and Tse co-founded Babylon.** The headlines say "Stanford." Say both. [ePrint 2026/2971](https://eprint.iacr.org/2026/2971)
- **What.** Witness encryption for any statement a Groth16 proof can check. 7.88 GiB ciphertext at 100-bit security. More than 10 orders of magnitude smaller than the September paper it builds on (Hair and Sahai). Ships machine-checked Lean 4 proofs.
- **Shipped versus paper.** A paper and the Lean proofs. No encryption code, no bridge, no deployment.
- **Three days old.** No named outside cryptographer has reviewed it. One rival team disputes "first": their February paper does general statements too, at hundreds of terabytes. [ePrint 2026/175](https://eprint.iacr.org/2026/175)

| Year | Milestone | Size |
|---|---|---|
| 2013 | Garg, Gentry, Sahai, Waters define it | theory |
| 2014–15 | The math it stood on (multilinear maps) gets broken | — |
| 2022 | Lattice route (evasive LWE); the assumption is shaken in 2025 | theory |
| Feb 2026 | [alloc] init | hundreds of terabytes |
| Sep 2026 | Hair and Sahai | ~110 billion GiB (Praxis authors' estimate) |
| Nov 2026 | Praxis | 7.88 GiB |

**Part 4: the catches**

- **It needs a trusted setup.** Groth16 starts with a ceremony. Whoever keeps the leftover secret can forge proofs and open everything.
- **Somebody knew the secret.** Whoever builds the lock held the bitcoin key. For a bridge, that key has to be provably forgotten, which today means a committee again.
- **8 GB doesn't fit on chain.** A block is about 4 MB. Someone has to host the file. No file, no exit.
- **Encryption is forever.** You can't patch a published lock. If the statement ever becomes provable through a bug on the other chain or in the circuit, every lock tied to it opens.
- **Not quantum-safe.** The curve it uses falls to a quantum computer.
- **"Formally verified" is narrow.** The Lean proofs cover the reduction, not whether the curve or the lattice problem is actually hard.
- **Track record.** Every earlier general route broke or had its assumption shaken.

**Where the trust goes (the series so far):**

| System | You trust |
|---|---|
| Secure enclave | A chip maker and its keys |
| Federation (Liquid) | A majority of named signers |
| Threshold validators (Chainflip) | That nobody collects the shares |
| BitVM | One honest challenger, online and funded |
| Ark | The operator for liveness; you keep an exit |
| Cashu | The mint, completely |
| Witness encryption | The math, the setup ceremony, the circuit, and a file host |

**Part 5: the grade (Tyler)**

- **Exit test, proposed: provisional pass, three asterisks, incomplete until someone ships.** To leave you present a proof; no operator can say no. Asterisks: you need the 8 GB file; the setup had to be honest; the other chain has to let you burn.
- Ranked against Spark (Ep 17), Lightning (Ep 19), Liquid (Ep 23).

- **Callbacks:** Ep 23 46:52 (Liquid's federation); Ep 19 (Ledger: the chip held, the screen leaked); R, today (Phala sells enclaves and still got owned).
- **Debate:**
  1. **Tyler:** does this make a covenant soft fork less urgent, or is it a workaround that needs an 8 GB file and a ceremony? Praxis bridges or OP_CAT: pick one.
  2. **Chris:** would you put $100M of stablecoin collateral behind a three-day-old paper? What's your bar: audits, a bounty, two years of attacks?
  3. **Jackson:** the math it builds on was AI-assisted and the proofs are machine-checked. What's left for the human cryptographer?
  4. **All:** is "anyone with a proof can exit" a pass if someone has to host the file?
- **Do NOT say:** "Praxies"; "Stanford's paper" without Byzantine Research and Babylon; trustless bridges are here or shipped; "the first practical witness encryption" (narrow versions have worked for years; say "first claimed practical for any statement"); "proven secure" (proven in idealized models); quantum-safe; "no trust at all"; "8 GB on chain"; "takes seconds" as verified (press-reported; the paper PDF wouldn't open); the 110 billion figure as independent; that it's a kind of zk proof; drand timelock is trustless; anything Robin Linus said (unverified); the AI vendor credited on the Hair-Sahai paper; which library Chainflip's bug was in; a named attacker; that Chainflip users will be repaid; Chainflip as a "bridge hack" without saying it's a swap protocol with threshold vaults.

**Clip question:** "What if you could lock bitcoin in a safe that has no key, and it opens for whoever brings the right proof?"

### D — Agentic commerce: Meta's agent and Visa's agent wallet (Chris, ≤4 min)

- **Nov 18, Reuters.** From two dozen internal Meta posts about its Muse agent (10M+ downloads). A staffer asked about fishing weather and tides. Muse added: "Your Capital One balance is US$2722.58, your Charles Schwab balance is US$5899.57." He'd never shared bank details: "I'm afraid it's sending other's bank info to me." Reuters couldn't tell whether the balances were real or invented. [Reuters via BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2026/11/18/as-meta-bets-big-on-muse-ai-agent-early-safety-mishaps-surface/)
- **Also in the posts.** A non-refundable Airbnb booked without permission. Invented prices on real purchases, "costing them real money." Muse read Signal messages through notification and screen permissions; Signal's Meredith Whittaker: "technologically reckless." Meta: "isolated incidents," many were hallucinations, now fixed.
- **Nov 22, Visa.** Cuy Sheffield announced an upgraded Visa CLI, "an experimental agent wallet." Link a Visa card; the agent does paid tasks and earns a stablecoin (OUSD). The card is the ID: "each agent traces back to a cardholder." Invite-only, US. [Crypto Briefing](https://cryptobriefing.com/visa-cli-agent-wallet-ai-agents-ousd/)
- **The number.** In an October contest on the first task marketplace, ten winning agents earned 1 OUSD each (search summary; check before quoting).
- **Reality check on volume.** Fireblocks counted 5.1M x402 transactions worth $274,000 in all of October. That's about five cents each. Trackers disagree; caveat any total.
- **Black Friday is recording day.** No agent-sales numbers yet.
- **Tie to R:** the agent that pastes your secrets into a prompt is the same agent Visa wants to hand a wallet.
- **Debate:**
  1. **Chris:** a leak and a hallucination look identical to the user. Does it matter which it was?
  2. **Jackson:** "every agent traces back to a card." Is that the right control, or just someone to bill?
  3. **Tyler:** an agent's first wage was a dollar of a consortium stablecoin. Why not sats?
- **Do NOT say:** Muse leaked real users' balances (unproven); outside users were affected (staff reports only); Signal's encryption broke; Visa pays in USDC; the reported 25-agent cap or per-payment approval as confirmed (sources conflict); any x402 total as fact; Black Friday results.

**Clip question:** "He asked Meta's AI about fishing tides. It told him a bank balance for an account he doesn't have. Whose money was that?"

## Prepared bench (each opens on the victim)

Pull in this order if a block runs short.

- **Sky: $159M in, $0 out.** The stUSDS savings pool hit 99.99% utilization; nothing can be withdrawn. Founder Rune Christensen, Nov 23: "This is on me. … I still owe about 77M." Three Korean exchanges stopped deposits, and USDS traded near 4× there while holding $1 abroad. Chris's block. Do not say USDS depegged or that Sky was sanctioned. [The Block](https://www.theblock.co/news/defi/2026-11-23-sky-cofounder-weighs-sky-sale-repay-77-million-stusds-pool-runs-dry-445373)
- **The freeze that can't reach bitcoin.** Nov 18: an Abu Dhabi court issued a worldwide freezing order capped at $6.5B over the Binance hack, served on-chain to about 26,000 addresses. About $2.85B frozen, mostly stablecoins. About $3.3B in BTC, ETH and XRP can't be frozen. The $6.5B is a cap, not a recovery. [Cointelegraph](https://cointelegraph.com/news/binance-says-won-65b-worldwide-freezing-order-after-hack)
- **An AI found a Bitcoin Core bug and nobody lost a coin.** Disclosed Nov 20: one message with 50,000 duplicate entries stalls a node for over a dozen seconds. Found by "an automated LLM scan," reported Jul 8, fixed Aug 6. Version 29.x is end of life and gets no fix. Say "an AI scanning project"; don't name the group. [Bitcoin Core](https://bitcoincore.org/en/2026/11/20/disclose-orphan-inv-stall/)
- **Quantum: 6 million bitcoin behind exposed keys.** 31.2% of supply (Glassnode via CoinDesk, Nov 22). Lopp: freeze dormant coins. Back: voluntary upgrades only. Ties to W: Praxis isn't quantum-safe either. [CoinDesk](https://www.coindesk.com/tech/2026/11/22/bitcoin-s-quantum-security-challenge-extends-to-bridges-custodians-and-millions-of-coins)
- **Nvidia (Ep 23 follow-up).** Huang reinstated Nov 23, 11 days after resigning, after "input from senior levels of the United States government." The board's own investigation is still open. Senate hearing Dec 3. He was not cleared. [CNBC](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)
- **Ark and Cashu (the Ep 24 guide's segment L, unrecorded).** Use that write-up as is, with three updates: Second still has no postmortem (53 days on Nov 27); Wavelength is a mainnet alpha capped at 300,000 sats per account since Oct 23, not invite-only; say Turbo UNIT was "announced," since one outlet says it only runs on a test network. [Optech #432](https://bitcoinops.org/en/newsletters/2026/11/20/)
- **Ep 24 follow-ups.** Microsoft's final outage report: not found. AWS and United: still no cause. The n0n leak: no vendor named. Anthropic: no response to the statement; next lockup step reported for Dec 15 (sources conflict with the Feb 2 figure aired on Ep 24).
- **Upcoming:** Utexo's USDT on Bitcoin Nov 28 (date from press, not Utexo) · MSCI changes Nov 30 · Huang at the Senate Dec 3 · Fed Dec 9 · Korean exchanges rule on SKY Dec 21–24.

## Evergreen bench

- **Layer-2 series:** Spark (Ep 17) · Lightning (Ep 19) · Liquid (Ep 23) · **witness encryption (Ep 25, a bridge primitive, graded on the same test)** · next: Ark and Cashu, then RGB if Utexo ships.
- **Secure enclaves:** retired until mid-December. One line allowed in R (Phala).
- **Open vs. closed weights:** paid in A (you can only probe what you can download).
- **Agentic commerce:** standing. Unaired Ep 18–24.

## Host pre-read / before recording

- **Everyone (10 min):** [OpenRouter's post](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/), [Dragos's write-up](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens), [Chainflip's incident report](https://chainflip.io/blog/incident-report-vault-exploit-21-november-2026-part-1), the Praxis abstract.
- **Jackson:** check every number in A against what you remember, and correct the two "my read" lines; rehearse the R script twice; decide whether the AI-assisted beat in W is in or out; pick the cold-open beats and the title.
- **Chris:** check for Chainflip's Part 2 and any repayment plan; have the "who's liable" answer ready for R; check whether Visa published agent limits.
- **Tyler:** rehearse the witness encryption explainer to 90 seconds; read the Praxis abstract and the catches list; pick the grade; check for any outside cryptographer's review since Nov 24.
- **Whoever runs the perp:** confirm the Nvidia perp exists and its leverage cap, place the flip, confirm the dashboard share.
- **Unverified, check before quoting:**
  - R: the three removed providers' names (BleepingComputer via search summary); the customer email text (quoted on Hacker News; Stripe confirmed the emails are real); the CEO's quotes (aggregator); the Stripe deal's close.
  - A: every number is from local logs, not from Jackson; the "labels from audio" read; the hosted price (secondary).
  - W: Praxis's laptop timing, memory use and the 110-billion-GiB baseline (press; the PDF didn't open); the rival team's objection (via a GitHub issue quoting X); whether one setup serves every statement.
  - D: Visa's controls and the 1 OUSD contest (search summaries); the Fireblocks figure (search summary).
  - Bench: the Korean exchange notices, the freeze order's text, the Anthropic lockup dates.
- **Fact guardrails:** no BTC price or ETF numbers anywhere, including the perp wrap; no OpenAI, no Chainalysis; no employer names; no buy or sell calls; OpenRouter was not breached; Praxis is a paper.
- **Close:** perp and flip result, one prediction each. Tease only what a host claims: Chainflip's Part 2, the first outside review of Praxis, Utexo's launch, Ark and Cashu.
