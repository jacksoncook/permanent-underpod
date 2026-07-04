# Permanent Underpod — Ep 4 — Attributed transcript

*Speaker attribution via ECAPA voice embeddings anchored to frame-verified spans; `AI <name>` labels in 38:13-44:20 follow the aligned clone-playback timeline (live interjections during playback may be labeled as the clone). Best-effort — short backchannels inherit the previous speaker.*

**Tyler** (0:00): And so if you've thought as a person, you could contain multitudes, the reality is that AI can take you and compress your whole personality into a, you know, 150 line markdown file.

**Chris** (0:11): That's all I got. The first to do what, like basically take optimism, slap a Coinbase sticker on it, and then be like, "Come here and do DeFi." You like, you skip the party to go whisper sweet nothings into a terminal window with tables selected.

**Jackson** (0:30): Instead I was like, "Oh, I have to go, I have to go." And I'm like, "Oh, but I need to do like a few more, a few more prompts." You know, I just couldn't get it. Well, yeah, we're live. You may notice that we're in the fanciest place that anyone's ever been. This is, we can't hide it, Presidio Bitcoin San Francisco. Shout out to our homies at Presidio Bitcoin for setting us up in this amazing studio. I mean, I feel like I don't deserve this. It's a big upgrade over our prior setup. We went from, you know, zero to 100. Yeah, sitting on a couch recording from my work laptop to...

**Chris** (1:12): I mean, I think we're pretty big. I mean, I don't want to talk about the shorts numbers, but our shorts do well. Yeah, we're doing good. Yeah.

**Jackson** (1:21): So I guess this is how we're rewarded. Yeah, don't get used to this though, fans. This is the only time this is ever going to happen. We're actually going fully remote following this podcast. So we can enjoy our time together, our final time. With it up in the Baller podcast studio. That's right. Permanent Underpod. This is Jackson. You're a Korean financial markets expert/host. We've got Tyler. What are you?

**Chris** (1:49): I'm Tyler. And? I'm Chris. I'm the guy who forgets to queue out Peppa fortune. Yeah. Yeah, you have him to blame. Leave a comment if that makes you angry.

**Jackson** (2:00): You're the spot guy. Yeah, I'm the spot guy apparently. Yeah. That's what the AI thinks at least. What? I don't know. What topic do you guys want to... Actually, first, let's talk about our weeks. Has everyone had an okay week? Anything interesting? Absolutely nothing. Absolutely nothing. Yeah, pretty much not. I went to the vet with Pico three times this week. The saga keeps on giving. I mean, we got to get our Pico update. Is Pico okay? He's okay. But he had some concerning blood markers on his follow-up visit. So I had to take him to a different vet yesterday. They shaved his stomach and they gave him an ultrasound so they could look at his liver. And his liver seems fine, but it still has weird numbers. And they're just like, "Whatever man, he looks healthy." So they said, "Come back in two weeks and check his blood again." Wow. But yeah, huge family but because I'm spending like hours and hours at the vet this week. Yeah, I'm just trying to make sure that he's the healthiest guy that you can be. Are you putting him back on the chicken and rice? So now the dog's eating human food? No, that would help us do numbers though. If I blurred that line between dog and human food a little bit more.

**Chris** (3:11): I think I've let the team down so someone has to pick up the slack. Yeah, it might mean that. That is our best performing short. I think it was until the one where I eviscerated Chris for playing Xbox as a 23-year-old. I've been thinking about that all week. That's what happened to me this week. I was like, "Damn, I just got laid out so bad that it was our best performing short." How do you even recover from that? I don't do. I'm still here thinking about it.

**Jackson** (3:36): Are you still drinking Monster then or are you done with that?

**Chris** (3:38): Yeah, I had one this morning but I threw it away before I got here so you guys wouldn't see.

**Jackson** (3:43): It's important to hide your shame. I think so. Let's see. Maybe I should say one good thing that's happened this week for me. I can't think of anything. Fable came back. Oh, dude. Yeah, that's almost like a segment though. Fable's back. I didn't happen to Jackson personally.

**Tyler** (4:04): I mean, it kind of did. I feel like Jackson has a quasi-romantic relationship with Fable.

**Jackson** (4:11): It's super weird. For those of you that don't know, the reason we're going fully remote is I'm not going to be living in a driving distance to my homies soon. So I like going away parties to go to and then anthropic drops Fable 5 back to the mainstream right when I have to go to a going away party. And I'm like, "Screw all these people. I just want to grind." You know that meme where it's the guy from the Truman Show and he's like, "And now do this thing." Trump is like, "And now release Fable 5 when Jackson has to go for a going away party with three people." You're probably more popular than that. That's harsh actually.

**Tyler** (4:53): I'm the resident hater of the podcast. I'm just doing other shorts.

**Chris** (4:58): The Halo thing was playful. Was it playful, dude? Are we saying that was playful?

**Jackson** (5:04): Playful compared to saying that I have three friends.

**Chris** (5:08): Yeah, you just got to like duck one time. Yeah, what the heck?

**Jackson** (5:12): You got to stay a fist away from the mic. Our producer, one time producer taught us all the rules. So Fable came back and you skipped the party to go whisper sweet nothings into a terminal window with Fable selected. Instead I was like, "Oh, I have to go. I have to go." And I'm like, "Oh, but I need to do like a few more. A few more prompts." I just couldn't get away. So I started some loops. I tried to automate my entire job away. It's very scary. Can you talk about what you're building? Yeah, I can tell you. I started basically like every time I have an idea, I just start looping Fable on it until it completes it. What do you mean by looping Fable? I'm sure that many people have interacted with chat GPT or some sort of AI chat bot. I'm going to make that assumption. But every time you talk to it, it talks back and then you have to talk back for it to do more. And at our job, we talked to the AI and then it writes code, or at least for me and Chris, not for Tyler. We write code which moves information and makes money move in some of our cases. So looping means I want you to keep trying to write this code until you can show me that it is complete. So that's like a way that I can start work and then I can leave and go train for a few hours and come back and see a little progress for my boy. You just use slash goal. Is that essentially it? Or what is the actual mechanism of looping? So I use cloud code mostly, although I have been running some A/B tests with cloud code versus goose and open source harness for using AI agents combined with GLM 4.7 and Quinn 3 open source local models. But yeah, in cloud code, there is a skill called slash loop and I just do slash loop and I just say get after it. Don't ask me. Keep going. Never stop.

**Chris** (7:18): Dude, so I'm a looper myself and I noticed that there's versions of the model where it's incredibly lazy. It somehow knows that it's burning Anthropic's VC money and it's just like, "I don't feel like it." I'll be like, "Never ask me anything. Just execute." And it will be like, "It will stop." Have you had that experience or not at all?

**Jackson** (7:38): Yeah, sometimes it stops and then I get home and I'm like, "Oh, you totally screwed me today." But that's just par for the course. You just have to figure out how to incentivize it to keep going. You just threaten it, but with false threats like, "I'm going to get you. I'm going to get you if you don't do this." And it'll be like, "Oh, don't get me." And then Tyler asked the specific things. One little project I was trying to do is tracking tennis balls on videos so I can determine who won a point based off of a video clip for another YouTube venture of mine as a tennis player. I also was building this tool to automate all my projects where basically I write the project doc and then I run a script and then it just goes indefinitely prompting the AI to write more code and then prompting other AIs to review the code and then getting the AI to address the other AI's reviews of the code and then DMing me when it's time to take a look because it's not worth my time before that. So when you have an agent come and get you and be like, "You got to go get that Claude because they didn't finish it the way you want." When do you come in and get them? Oh, yeah. I have a Slack bot called Bitcoin Baddie. Bitcoin Baddie will be like @jcook. That's my alias, LDAP, at work. @jacksoncook, please don't email me, by the way. @jacksoncook, please review this and then I get in there. So that's a little scary because Babel is really good and doesn't make mistakes. So I don't know, it's just crushing all these projects and I'm like, "Geez, we need more projects."

**Chris** (9:30): Yeah, I mean, it's not like it can automate our incredible hot takes on this podcast, though. That would be incredibly unlikely and I think we're safe for at least, should we say, seven days?

**Jackson** (9:40): Seven days, yeah. I don't know. Babel's already there. I wouldn't say that I'm more clever than Babel. You just contain multitudes. They can't possibly simulate your frame of mind.

**Chris** (9:54): They couldn't distill you into a sole MD, hypothetically.

**Jackson** (9:58): I wouldn't say that. When is the machine going to flip the script, though? When is it going to be like, "Okay, I'm done looping. Now you go get me a USB-C flash drive." But it doesn't tell me why I need to get it. It just needs my meat machine to walk over to the store and buy a USB-C flash drive.

**Tyler** (10:17): Until it can summon a door dasher to just drop it off and then a different woman shows up at your house and unpacks it and then sticks it into the computer and you're like, "What are you doing here?"

**Chris** (10:28): "Claud Air Tasker MCP with streaming payments over Tempo?" I mean. But the question is, do we tip or do we not? The Claud. You're tipping your...

**Jackson** (10:42): Do we tip the Claud or do we tip the delivery worker? I think the Claud tips the humans because it feels bad about taking all the human jobs. It's like, "Here are your scraps."

**Chris** (10:55): Does Claud give us tokens?

**Jackson** (10:58): Yeah, maybe it rewards us with tokens so we can ask it another question. This kind of brings us to a couple different ways we can get. You mentioned Tempo. Do we want to talk about maybe a Tempo versus base kind of situation? Or we also mentioned Claud ordering door dashers to my house. Do we want to take an agentic commerce twist? What do you guys think?

**Chris** (11:21): I'll give this one to Tyler, I think, as the decider. I think we should talk about... What was the first one? OpenUSD?

**Jackson** (11:31): Oh, that wasn't it. It was Tempo versus base. Okay, let's do Tempo versus base. But we can do... We're going to do OpenUSD.

**Chris** (11:37): I mean, that's on top of it. Yeah, that's the layer two of Tempo versus base. Okay, let's start at the beginning then.

**Jackson** (11:42): Start at the beginning. He wants to kick it off. Not me.

**Chris** (11:48): Yeah, I mean, we just want to talk about what's going on on chain with all these platforms.

**Jackson** (11:57): I'm still unclear if we're talking about OpenUSD or base versus Tempo. But from base versus Tempo, it's like they are the biggest institutional chains, maybe. So why is one better than another? What does it mean if they succeed? Does it mean anything? I don't know. Have you used any of them?

**Chris** (12:26): Yes, I have. I've used base. So what is base? So base is an Ethereum L2 or it still is an Ethereum L2. And basically it's Coinbase's sovereign layer two chain where they have all of their DeFi products that aren't necessarily on the Coinbase centralized app. But they have some of their products there. So one might be like a Morpho market, which is a way to lend out your Bitcoin on Coinbase and receive USD C back for it, which you can do things with. And Morpho is like a third party that creates smart contracts for doing crypto lending,

**Tyler** (13:12): but they are smart contracts or agnostic of chain because it just works on any EVM and base is an EVM layer two or side chain depending on where you draw the line. A little messy thing.

**Chris** (13:26): Exactly. So yeah, exactly that. So it's like this sort of agnostic, sort of not platform where Coinbase has the ability to bundle all these DeFi products. I think there's a Uniswap deployment as well. There's Aerodrome, which is their DEX. I'm sure if they don't have perps, they're going to get it. So yeah, Coinbase is that. It's like a one-stop shop for that. And so one thing about base is it was one of the first to do this. I think base is three, four years old.

**Tyler** (14:01): The first to do what? Basically take optimism, slap a Coinbase sticker on it, and then be like, "Come here and do DeFi. So many perp of fortune on base."

**Chris** (14:14): That's how some would describe it, for sure.

**Tyler** (14:16): Yeah. One of my favorite things about base is that if you ever read any press releases or media about base, they always start with this phrase, and it's like, "base, comma, a Ethereum layer 2 blockchain incubated by Coinbase, comma." And it's very clear that that's their marketing double-speak that they hand to the block or coin desk or something, because they want to very carefully make sure that they're talked about, how they want to be talked about. Because if somebody confuses it and says, "This is actually Coinbase's chain," that's not how they want base to be presented. And debatably, maybe that's not actually how base operates, although I think that's... Maybe, Chris, you can tell us a little bit more about how base is structured and some of the guarantees that you get when using base. You can unilaterally exit to Ethereum layer 1, right? So they cannot censor your exit transaction to Ethereum layer 1. So that's a pretty good security guarantee, actually, for using base. But the coordinator on the base chain can censor your transaction and not include it on base. So maybe that's a trade-off that a lot of people find works well for them. That actually seems like a pretty good security model for a lot of this type of crypto usage. Would you agree with that, or what are some other sharp edges there?

**Chris** (15:42): Yeah, I would totally agree with that. I think one of the sticking points is definitely the shared sequencer. So the sequencer in one of these L2s is who decides which transaction gets in and in what order. And this seems quite benign, right? Because you're thinking, "What does it matter? What order the transactions get in?" But on these chains, there are these complicated programs running. For example, one is called an automated market maker, which decides the price of two assets based on, guess what, the ordering of the transactions. So when you have control of the order flow and the way that transactions are included in the blocks, you can reorder these transactions, and the order of them determines what price everybody gets. I mean, there's kind of dovetails with this thing called MEV, which is maximum extractable value, that I think we probably shouldn't go too deep into. It's a whole rabbit hole. It's like a whole episode in the future. I think the broader point is that there are all these layers at which people operate on these platforms and have various types of either veto or control. And yeah, there's a lot of unintuitive, I would say, thorny edges.

**Jackson** (16:57): And who controls the sequencing of the transactions? Who is that?

**Chris** (17:01): Who would you think it was?

**Jackson** (17:03): Who would I think it is? The person running the node?

**Chris** (17:07): Yeah, exactly. Every L2 has a single sequencer at the moment, or almost all of them, which means that the person who's operating the L2 runs the sequencer, and they decide the order of transactions. So in this case, it would be base. Base decides what gets on the chain.

**Tyler** (17:26): I do a kind of in-the-depth question. So my understanding of how an optimistic roll-up works is basically it's a layer or two on top of Ethereum. And you kind of trust the sequencer to validate transactions and include them in blocks that are valid, basically. And the enforcement mechanism for Ethereum to make sure that the sequencer is only including valid blocks is it just assumes that everything is valid until there is somebody who can come along and basically check their work. And that's the optimistic part, because you optimistically assume that that block was constructed correctly. And then somebody has an incentive to check that work. If they find a mistake with it, then they can submit a fraud-proof to Ethereum. They can collect some kind of incentive for doing that. And then the situation on the layer two gets remediated that way. But if the set of people who are allowed to issue those fraud proofs is restricted, then essentially if there's this one party that runs the sequencer and they, for example, want to submit invalid transactions that takes money from you, and then also the person who could call them out on that via the fraud proof is another entity that's related and they could just decide not to issue a fraud proof for that and it isn't an open set of people that could do that, then can't they kind of include invalid transactions on this layer two without any recourse on L1? And so does that weaken the assurance of you have unilateral exit, but actually if the sequencer and the fraud prover coordinate, they can take your balances. Does that make sense? Yep, 100%.

**Chris** (19:18): So I think on base, because again, it's an optimism-inspired chain, anyone can submit a fraud proof. I think the window is seven days. I think they have that.

**Tyler** (19:30): I know at one point they didn't.

**Chris** (19:32): For the longest time they did not, right?

**Tyler** (19:34): But that's a very important step for any layer two, that's one of Vitalik's main things when he wants these L2s to become more robust. And if they did that, then that's well done, Coinbase, I guess, yeah.

**Chris** (19:46): I mean, optimism. But yeah, I think they got that for free with the optimism stack. But yeah, it's a very astute observation and I think it definitely holds up. And I think it really contrasts with tempo.

**Jackson** (20:04): Good. Good tempo.

**Chris** (20:06): I think it really contrasts with tempo.

**Tyler** (20:08): Yeah, so I feel like maybe to set that up, base is coming at it from this angle where it's built on a crypto-native stack that you have unilateral exit to Ethereum. It has EVM compatibility, so you have all the same familiar smart contracts and stuff like that. But it's kind of like incubated by this corporate sponsor. They issue a lot of the wrapped assets on the blockchain so they kind of control a lot of the touch points of that blockchain with the real world. And so they're kind of coming at it of like here's this corporate spin on a blockchain that we like try to do our best on to make it kind of more like fit with the crypto ethos. And then you have tempo, which is maybe coming at it from a different angle, which is kind of like we are using a blockchain as a means to an end to build a next generation payment system. But we don't necessarily want to interface with public blockchains or inherit any of that ethos and we're kind of building this de novo thing.

**Chris** (21:16): Or security guarantees, right? Because the state of tempo is that it's, I would say, generously proof of authority. It's another L1. It doesn't roll up to any blockchain. So there's nobody holding them accountable. What happens on tempo is like that's just what happens with those assets. It's like a Peloponnesian war style coalition of companies who run validators on this shared neutral zone. That's a tricky model, I don't know.

**Tyler** (21:48): Yeah, it doesn't matter though if there's no native asset to the blockchain. If tempo is just a blockchain that's stuffed with stablecoins and those stablecoins are all genius compliant issued by companies, if you're using your USDC or USDT on Ethereum, even if Ethereum has great security guarantees, those smart contracts have freeze functions and stuff like that. And so it doesn't really matter what chain you're on if Circle can freeze your coins, right?

**Chris** (22:15): I think the historic use of the freeze function is something that a lot of people haven't really dug into. Circle is famously not very litigious with the freeze function. They want a chord injunction. But that freeze function is slow. Really? Well, they need to get everybody together. It's a multi-sig. They need to decide they're going to do it.

**Tyler** (22:38): Well, the main thing is if North Korea hacks some smart contract, they steal a bunch of USDC, that USDC is immediately swapped for some sovereign asset. And so it's like they can swap faster than Circle can freeze basically. And so in that arms race, they're basically always going to lose.

**Chris** (22:58): So I think with that, you catch the people who are holding it for too long. If they're for some reason unsophisticated holding a stable coin for a long time, you get that for sure. But that's not generally the case with sophisticated actors. All right. That makes sense.

**Tyler** (23:14): So there is some benefit to doing, let's say, permissioned assets on a more sovereign blockchain. Well, I don't know if I'd frame it as a benefit because we're talking in this case about an international bad actor being able to get away with their loot.

**Jackson** (23:32): Sounds like you're on the wrong side. Don't come at me.

**Chris** (23:36): Our opinions are on me. I mean, the jury's out. Let's see what happens. I'm sure this will continue to happen on every chain. Let's see what happens when this happens the first time on Tempo or Bass. Because you still have to be fast. You still have to be like, "Oh, there goes $300 billion of Tempo coin to do something."

**Tyler** (23:55): Can you unwind blocks? Literally, they just roll it back to before the hack and they're like, "Sorry, everyone that did transactions in the meantime can't do or something."

**Chris** (24:04): Can they bridge out? There's so many questions.

**Jackson** (24:06): Yeah. So I apologize. I'm pretty ignorant on this. So I'm going to try to recap what I think we've said about the Bass versus the Tempo. Bass is built as a layer two on top of Ethereum. So it gets a little bit of freedom from that. It's kind of through the redemption process you were talking about. Whereas Tempo is not built. It's like its own layer one and it's run by, it sounds like a coalition or like people with an agreement with one another that are allowed to run the validators or whatever they call them in Tempo. So does that mean that we are team Bass because it's marginally more open and free?

**Chris** (24:52): I'm team Bitcoin. What team are you on, man?

**Jackson** (24:56): Well, the segment was Bass versus Tempo. I mean like horses for courses, right? I don't know. I don't know what that means either. It's like pick the right tool for the job.

**Tyler** (25:10): I don't know. I actually don't think that we actually talked about the big trade-offs with Tempo compared to Bass yet.

**Jackson** (25:16): I did want to ask a question. One trade-off. Do you want to go first or? All right. Quick, can you do any asset on Tempo like USDT or USDC on Tempo versus like Bass? You can definitely do both of those.

**Chris** (25:32): You can, but it depends on what the issuer wants to do. So if the issuer Tether or Circle chooses to issue on those chains, yes. But if not, then no, right? And I think that's part of the complexity.

**Jackson** (25:43): Okay, all right. Sorry, give after it, Tyler. I was going to say one interesting thing about Bass is that am I correct that all the transactions on Bass are public?

**Tyler** (25:53): So there's no privacy basically to transacting on Bass?

**Chris** (25:56): You are correct. They have some type of private off-chain ledger, but I don't think it works. It's not as sophisticated as Tempo, yeah.

**Tyler** (26:06): Well, do either of these things exist yet? Or they both just said publicly like, "Oh yeah, we commit to figuring out some private way for people to transact on our chains." That's like an intention that we're committing to, but it isn't a reality yet.

**Chris** (26:19): I think Tempo has shipped either the beta of the feature or the feature. The thing with Tempo is their team is unbelievably cracked. They're well known as one of the most talented teams in the space.

**Tyler** (26:29): Yeah, they just took all the paradigm people, right? I guess paradigm is blending their people.

**Chris** (26:35): Yeah, I think they're pretty deep in that.

**Tyler** (26:37): They're both elite on X, so that's all I know about them. Does their actual engineering chops match their eliteness on X?

**Chris** (26:45): Yeah, absolutely. The thing about those engineers is those engineers specifically built one of the biggest reference implementations for Ethereum. It's called Breath and all this other stuff. They really know what they're doing. Yeah, that's interesting.

**Tyler** (27:06): To get to that point, though, is that Tempo, one of their features is that, to me, they're more targeting a payments use case for Tempo, which makes sense because it's partially or maybe primarily driven by Stripe in partnership with Paradigm, and then they have these other partners that are joining it, which might get us onto the OUSD track later on. Stripe is obviously more of a payments company. They're not trying to build open finance web 3 kind of stuff, whereas Coinbase is dabbling and all of that. But one of the features of Tempo is that they have these so-called privacy zones which is like it's a blockchain. One of the features of the blockchain is that you can download the box and see what's going on. You can validate yourself even if you aren't able to do sequencing or that kind of thing. And in Tempo, I guess they want to have these privacy zones because the trade-off is that when you have a public blockchain, that means everyone can see all the transactions. And so it's very hard to do privacy on a blockchain for that reason. There's ways that you can obfuscate the transactions by using cryptography. Monero does that. Zcash has another method where they create these shielded pools where you can do transactions. And so you can deposit your Zcash into a private wallet and do transactions in there and you can take it out. But that actually isn't desirable to have on a layer 1 blockchain because you can't audit the supply of Zcash. And Zcash famously has had, I think, at least one, if not multiple, known inflation bugs where people could have inflated the supply of Zcash in the private pool, which would be completely undetectable. So no one actually knows what the supply of Zcash is.

**Chris** (28:49): I wouldn't worry about that. Any Zcash is out there, I wouldn't worry about it. Oh, why is that? No, I'm kidding. Yeah, it's terrifying. Yeah, it's terrifying. Definitely worry about that.

**Jackson** (28:58): This is a big Zcash. That was like the VC coin of like two months ago.

**Chris** (29:04): The cull pump was crazy.

**Tyler** (29:06): Yeah, that was one of the most cynical pumps of just like, let's just take this coin from literally eight years ago off the shelf and I'll start talking about it and then dump it on retail pumps that I've ever seen. Yeah. It's like pure, cynical, key opinion leader BS.

**Chris** (29:21): Yeah, I had hoped it would be the last one, but you know.

**Tyler** (29:24): Yeah, and the tech of Zcash has merit, but you don't need to do that on layer 1, right?

**Chris** (29:29): So I mean, yeah, sapling protocol that Zcash implemented has been used by lots of others. Ironfish is an example. I mean, that's an ancient maybe gone chain now, but yeah, you absolutely, you can implement it other places, either using this protocol or other.

**Tyler** (29:44): EK roll ups as well as using the same moon math to hide or just make it not public, but then you can validate it still. Moon math.

**Chris** (29:53): I mean, there's Railgun is a company that built a UTXO system that settles using back to ETH mainnet and like allows you to shield your transactions. It's like a million ways to do it.

**Tyler** (30:05): And so those are some really based ways to do it because if you're Zcash and you're creating this private pool, it's like Zcash can't even see what's going on in that pool. They're blinded by cryptography, and that's the way they want it to be because of their principles, and I think that's rad. The private zones on Tempo are different because Tempo is like basically a fully owned blockchain, and the companies that operate it cannot let full privacy happen because they have obligations to regulations and sanctions and the governments and stuff like that. But the way they do privacy is it's essentially like custodial privacy where there are zones within Tempo where you can do transactions, but essentially the blockchain in that zone is not public. It's like a private chain. So you basically trust one company. You have privacy from the external world, but that one company can scrutinize your transactions. And that's kind of the relationship that consumers have with financial companies right now, where if I have a Chase credit card, Chase can see my transactions, but it's not like Chase posts my credit card statement to the blockchain every month, which is kind of what it would be if you did all of your financial transactions on an L1 public blockchain.

**Chris** (31:19): Totally. I haven't really looked too much into privacy zones, but there are other ways to do this. You know, like, there are compromises you can make that I think are quite good for the user. What does that mean, though?

**Tyler** (31:32): It's like, expose a view key to the authorities. So if the authorities come to them and they're like, "Hey, we think that there might be some actor that's misabusing your system." And they're like, "How do you come as an authority? How do you come to Railgun with a hypothesis of the bad action having taken place on this?" Like, you kind of need to know that something bad is happening there and you need to ask for the special key to then investigate it. I feel like that's not a system that law enforcement would be down with.

**Chris** (31:59): No, no, no, no. It's a good question. I think they have two things. They have one is the view key, which is more like the tax purposes, and the other one is private proofs of innocence. So I think they have a way to disambiguate whether somebody was bad in the pool and then kind of whittle it down based on some private information they have. I can't say much more than that.

**Tyler** (32:18): So there's an anonymity set within Railgun, and if they somehow decide that Jackson's a bad actor, he put his coins in there and they're tainted, that we can then allow the good actors in that privacy pool prove that they're not Jackson and that they're coins who are Jackson's coins.

**Chris** (32:35): That's a proof of not Jackson. In this metaphor. Yeah, I think that's cool.

**Tyler** (32:41): I have a little bit of a hard time believing that that kind of trade-off model is something that law enforcement, the state will be comfortable with long-term, but I applaud those actors for doing it in a really based and principled way, and I wish them the best with making that be sustainable.

**Chris** (33:02): Right, based but not on base. Railgun is not on base.

**Jackson** (33:06): You might want to lean away from that. Talking about tempo being based is very confusing. Oh, that's not tempo as being based. That's Railgun, right?

**Tyler** (33:16): It's a different entity and a different protocol.

**Chris** (33:19): Coming back to it, tempo versus base, I think this is not really a battle of tech, it's a battle of distribution, and I don't know which one is going to get all of the partners right and have a sufficiently good feature set that people will want to integrate with them. It seems like a zero-sum game, but I think it's too early to say. I don't know, what do you guys think?

**Jackson** (33:48): Jackson? No thoughts. No thoughts. Yeah, I don't know. I don't know anything about the adoption of stablecoins and the layer 2s on which they move. Very uninformed, that's why a stablecoin expert is here.

**Tyler** (34:02): Yeah, and I don't think anyone really knows how it's going to play out. You basically see all of the big players putting their chips on the table right now and assembling their bets and then we're going to roll the wheel and see who's going to win.

**Chris** (34:20): Speaking of chips, how about tokens? Would you say the players are putting their tokens on the table, like OpenUSD as an example?

**Tyler** (34:28): Ah, this man's done three podcasts.

**Jackson** (34:31): He's in his groove and his podcast chops. Is this what we have the preparation for? Do we have our prepared chat about OpenUSD? Yeah, so I can introduce this segment. Please do, please do. But in honor of Claude Fable coming back this week, we decided to do an experiment, which is that we thought if we needed to be simulated as people by the AI, Claude Fable is the only model that I would let simulate me. That's the only one that has my heart. But so we fed our prior three podcast transcripts to AI and then I had it generate soul.md for each of the three hosts based on our personas and we also see lit with some private chat history and stuff like that. I didn't get your guys' consent for that, but now Ithropic has our DNA history.

**Chris** (35:28): They have a view key to my soul.

**Jackson** (35:30): Wait, what is the soul.md?

**Tyler** (35:33): So one of the things with these agents that became really popular in January or February called OpenClaw or Claudebot. And these agents, you can create a text file that basically tells the agent what their personality is and how to act and how to talk and what their hopes and desires are. And that personality file is called soul.md. So I'm basically asking AI to distill each of our souls into a text file. And so if you thought as a person you could contain multitudes, the reality is that AI can take you and compress your whole personality into a 150 line markdown file.

**Chris** (36:15): That's all I got, 150 lines.

**Jackson** (36:17): Who had the longest soul by me? That's a good question. Who's the biggest soul?

**Chris** (36:22): Who's taking up the most disk space in reality?

**Jackson** (36:26): Let's see. Doran is 40 lines. Oh my gosh. Jackson is also 40 lines. Damn.

**Chris** (36:36): Wow, dude.

**Jackson** (36:37): I mean pardon my language.

**Chris** (36:38): He could have not told us this. 43 for me. Dude, you must have artificially increased it by three. Did we believe that Jackson?

**Jackson** (36:45): Yeah, it sounds like it made them all 340 and then Tyler added three because he knew how to act.

**Chris** (36:50): Like three character times at the end. Yeah, it's just like blank space basically. And so we have these three text files and we can basically spin up AI agents, give them these souls and tell them to impersonate us.

**Tyler** (37:09): And we fed them our podcast outline for today and some of our segments. And we had them create a synthetic segment of the podcast using our souls, trying to guess what we would say. And then I further had Claude try to clone our voices to actually record us doing one of these segments. So I don't know if we want to listen to maybe just like a couple minutes of it because the segment actually is like eight minutes long. So is that like use of our podcast time that we want to commit to or you just want to listen to a little bit of it and then grade how accurate these AIs were at imitating our souls?

**Jackson** (37:49): I don't know, let's just play it. And if we like it, we like it. If we don't, it's like these guys are boring.

**Chris** (37:54): Yeah, let's just let them prime us a little bit. Us the real people and they're fake.

**Jackson** (37:58): We do all watch the podcast, right? Yeah. But we can listen to ourselves talk.

**Tyler** (38:03): Yeah, okay. So this is AI impersonating the three of us in a segment about OpenUSD.

**Jackson** (38:12): Let's go.

**AI Jackson** (38:13): Okay, okay. Next up, elephant in the room. Or should I say dollar in the room? So you have to say big one, Stripe, Visa, BlackRock, like a buffet of 140 companies all get together and go, "Hey, let's make a stable coin." And then end it, OUSD, OpenUSD. Circle stock dropped 13% on the news, which rough day. To re-circle, honestly. But here's my favorite part. OpenUSD has been a real thing since forever. It's Pixar's file format with 3D models, so... (inaudible) I love the SEO battle to an actual dollar. Chris, you live in this world. What is this thing actually? And does Open... It's a good question.

**AI Chris** (38:55): Right, so disclaimer as always, I'm mostly more of a spot guy. And honestly, I'm working off-straps here. We've had both on Diggin this week. And the website is, what do you call it? Sugar Vaporware. A vibe and a list of interested parties. And so have ya everything. But he doesn't want to read OUSD. When we played this to Chris the first time, he thought it was ironic that the AI Chris,

**Tyler** (39:16): have he added that he's a spot guy, but then proceeded to talk about spot.

**Jackson** (39:20): So he picked up on Chris's modesty, I think, in this hole. Definitely.

**Chris** (39:25): Not my accent, though, unfortunately.

**Jackson** (39:27): You don't need to put the mic to it.

**AI Chris** (39:29): I can overlay it on the... (inaudible) And something like 140 other names. And the pitch that makes it actually interesting is its yield bearing. They pass most of the T-bill yield through to holders, which Heather and Circle famously do not. They pocket the flag as the thing that took a 13% bite out of Circle. Because Circle's whole business is keeping that yield for themselves. Proper stable coin, isn't it? Yeah, what accent do we have, Chris? I have no idea. The watch is on base as a... I'm going to call it a B20. Just an ERC 20. Living on coin basis chain. And the trick is, it's B3 to move inside the member's own walled gardens. So the Open is doing zero work on the tech side. It's not Open like Open Source. It's not Open like Permissionless. My understanding is it's open like a consortium you're invited to join. It's a distribution play dressed up as a protocol. Open like OpenAI. Because the whole game with stable coins was always distribution and where you can actually spend the thing. And these guys have the names. They've got the merchants. They've got the rails. So it could genuinely work, which honestly gives me the shits. The kicker is what it does... Is that a phrase that you...

**Tyler** (40:36): Like, where did it pick up on that? Hey.

**Chris** (40:39): You're the one who pointed this at LDMs, all right? [laughter] So presumably you didn't... [laughter] I mean, yeah, he stole a lot of my lines, this guy. [laughter]

**Jackson** (40:54): I was actually told yesterday that if I ate more vegetables, I would shit my pants less. How often do you shit my pants? [laughter]

**Chris** (41:01): Whoa, segue. [laughter]

**Jackson** (41:04): I feel like he was looking at my DM's. I don't know. Anyways. Like, twice a year. [laughter] That's reasonable.

**Chris** (41:12): I feel like Margo does it more than that. So that's okay. Yeah. You should consider wearing a diaper.

**Jackson** (41:17): I'm compared to a baby now. [laughter]

**Chris** (41:20): [inaudible]

**AI Chris** (41:21): Stripe has its own shame. And I bet money. Well, I bet $10. That's the new house for me after last Thursday. That tempo just quietly sunsets its own stable coin and makes OUSD the primary.

**AI Jackson** (41:32): Well, so open. It means about as much as it does in Pixar's file format. It suspects somebody else's controls that your prey still has. The Pixar file format makes no sense to me. You call the website. You want to tell them what's actually on it? Yeah, so the website is like,

**AI Tyler** (41:46): "I would describe it as a pigment board that got published in the internet." It sounds just like you. It kind of sounds like you.

**Jackson** (41:50): I think I maybe just talked too much in episode three and had better creative data to verify voice. Also, one of the nuances here is that when we create the AI agents and give them the soul,

**Tyler** (42:04): you can say which model you want to power that AI agent. And my intention was for Chris to be powered by Opus, which is the big-brained anthropic model before Babel. And then Jackson was going to be Opus 4.5 because that was his longtime homie, Opus 4.5. And then my agent is powered by Haiku, which is accurate to the relative level of intelligence. Haiku is the little-brained anthropic model.

**Chris** (42:39): Yeah, Yo's came out the best. I think the small brain is like a bell curve meme.

**Tyler** (42:46): So it's like having the small brain just enables it to have the hottest, best takes.

**Chris** (42:50): The horseshoe theory of things.

**Tyler** (42:52): Say something with a lot of confidence that may or may not be true. And if you just say it with confidence, then you sound smart, maybe. Also, it picked up on a lot of my usage of stop words.

**Jackson** (43:04): I just said "like" there, that kind of thing.

**AI Tyler** (43:06): It does that. And you scroll down and there's this sort of Slack workspace style wall of logos. It's like 140 little company logos all stacked on top of each other. And then at the bottom there's a wait list form. That's it. No docs, no technical specification, no roadmap, no timeline. It's like, "Hey, put your email here and maybe we'll talk to you someday." That's a good point. I'm not convinced. And I think that's actually the honest thing about it, right? But you didn't just record yourself. If you're passing the yield through to stablecoin holders, you're basically saying, "We're not going to pocket the float. We're not going to take the obvious rent. So what's the actual business?" And the answer is, kind of like what I said about Genius, it's one rent seeker trying to replace another rent seeker. The business is the exit ramps. It's who gets to own the customer relationship when this thing is finally sitting in a striped dashboard or a visa payment terminal. That's where the value is. That's actually the interchange, right? Like if you can disintermediate some part of the settlement chain by having OUSD live natively on your own walled garden, you keep the interchange spread that you'd normally lose to a credit card network or a bank. So they're not creating value. They're just like very carefully repositioning where the rent lives, which, and I'll give them this because Chris mentioned it, Stripe at least has a decency not to pretend it's anything else. I'm like, "The website is paperware, sure." But the Stripe message internally is basically, "Yeah, we're a fee-taking middleman and we're just reframing where we take the fee." That's honest. That's not a bad position to own.

**Jackson** (44:20): All right.

**Tyler** (44:21): I will say that I'm now very afraid of somebody deepfaking me based on our podcast audio, especially now with these mics. They're going to get a big sample of me speaking with a very clean mic and they'll probably just be able to, I don't know, steal all my financial assets. When that happens, thank you, Jackson, for having me be on a public podcast and somehow tricking me into joining this thing every week.

**Jackson** (44:49): I still don't know how I read this. This was all my plan just to steal your bag, dude. Oh, so it's going to be Jackson that's going to deepfake me and then disappear.

**Chris** (45:00): Yeah, as long as it's on tempo, you should be safe.

**Jackson** (45:03): There you go. Yeah, I should put my assets onto a chain that will protect me like that. Having a chain like Bitcoin or Ethereum where if you take the money, it's yours.

**Chris** (45:15): You can't have that anymore.

**Tyler** (45:20): The warm embrace of a payments giant.

**Chris** (45:23): I need my corporate daddy to protect me. That segment was incredible, frankly. It did verbatim steal some of my takes and I do want to issue one correction. OpenUSD does not pass yields to the users. It's a consortium model. The yield is split between the people in the consortium according to an agreement. It's open for me. I'm done. I don't know. I think RealChris does better than OpusChris.

**Jackson** (45:49): We haven't dialed in the soul yet.

**Tyler** (45:51): You're safe for one more week, but after this week's training data, maybe not.

**Jackson** (45:55): I started out sounding kind of Middle Eastern or something and then I became a British dude. It's totally insane. But it got you perfectly. I was getting flashbacks to listening to you talk about Michael Saylor and MicroStrategy. It kind of even sounded like it was coming from a laptop microphone. It was getting the aspect of my voice from our prior podcasts.

**Chris** (46:16): Stable coin. Since we won't have these beautiful microphones in the future,

**Jackson** (46:21): we can really get it to train on this right now. And then I'll just transcriptify all of our future podcasts and get AI to replicate our voices in high fidelity. I'm going to have to register my likeness of my copyrights because Jackson can't kick me out of the permanent underpod and just start simulating Chris and I. Yeah, but I think that's the next iteration possibly of this. I thought it was going to come with an animation. We didn't quite get to the animation, but drop a like and a comment and say if you would like to see Tyler animate us also. So then we can overlay a video. I think that would be pretty cool. Definitely. I still think we should do that no matter what, actually. That would be cool. Even if you don't drop a comment, because no one comments on these videos. It's okay. Do we have any OUSD takes that weren't covered? Or like we want to restate anything because I feel like that segment was fun.

**Tyler** (47:19): But I don't know if the listeners probably like actually heard any of the AI Chris spitting hot fire.

**Jackson** (47:27): Yeah, here question about open USD. So you said that it's like the consortium issues, the open USD, and then they split the yield among them. So is it like as long as the, or like how do they split it? Is it based off how much you're holding or like how much you've issued or like how much flows through your business or like how much you've had times time? For example, like if we had 50 million open USD and I had it for five hours, it's like, and then you had 50 million open USD and you had it for 10 hours. Do you get 66% and I get 33% or something?

**Chris** (48:05): Yeah, it's a good question. I don't know the details of open USD, but generally like these agreements are like a member of like a consortium. So it could be calculated anyway. It could be like prorated how long the funds are at rest in a wallet that you hold or that's held on your behalf by users or whatever. Yeah, I mean the agreements open. I think like that's going to be a big thing because like as we know, members of these consortiums traditionally are quite friendly with each other. But in this one, like, I mean, we've got Visa and MasterCard on the same billet. Like, yeah, I think it'll be interesting to see how they sort that out.

**Jackson** (48:44): Do you think that the open USD can overtake the incumbents of USDC and USDT? What is it? Tether launched the USAT or whatever earlier this year, but like we haven't heard anything about it. So will open USD die?

**Chris** (49:05): That's a good question. What do you think, Tom?

**Jackson** (49:07): Is it nothing?

**Tyler** (49:08): Will it die? I don't even know if it's alive yet. I mean, not to hate on it, but like I think that they did a masterful job of getting a bunch of companies that don't necessarily agree with each other and generally are thought of as competitors to like sign on to like an idea. And that is like a starting point for them to try to actually will this thing into existence. But I think it almost kind of necessarily had to start as like, we're all in this together because if it was started as this is Stripe's thing or this is someone else's thing, then nobody joins it. That's like the whole problem why these people want to disrupt circle or tether in the first place. So I think it's kind of fine that they are like going to figure out the details later. I think they just came to a bunch of these powerful companies and they were like, yo, MasterCard, like Visa's on board, like you better get on board or else you're going to be left behind. And then Visa's like, oh shit, like, you know, I might as well put my name on this because there's no downside for me to not put my name on it and like they haven't even figured it out. So like I can just be on this website and like have optionality going forward, see what they're about, be able to have a piece of it if I actually want to participate or not.

**Jackson** (50:15): But like, yeah, I wonder if they have more of it.

**Tyler** (50:19): I mean, mechanically, I think it's like probably pretty obvious how they'd like, just because of the model of it that like, yeah, they're going to try to pass the yield to like, you know, participants in some proportion to how much value those participants bring to the ecosystem, stuff like that, like what chain it will be on, like probably tempo, like you said, it's going to be on base as like a B20 as well.

**Chris** (50:41): Right, which how does that work? That's crazy. They're like direct competitors for order flow. Yeah. I mean, like on base, it's like maybe it's the,

**Tyler** (50:53): you know, the asset that people are doing, you know, crypto, Bitcoin, Ethereum, loans for and morpho or it's the trading pair in DeFi. But then on tempo, it's like the thing that people are buying their, I don't know, like their cloud description with. Yeah, exactly. So like they can kind of a little bit divide and conquer their use cases almost based on like their exact distribution right now. So that's why I like we were talking about this a little bit over lunch. I feel like it's a little bit kind of like a play where because the people who join this benefit to the proportion of activity they bring to it, then like it kind of is a very defensive mechanism by a lot of these companies, especially if someone like Visa or MasterCard is going to be in it, because it like if they feel good about their competitive positioning right now and then like, let's say there's a world where that exact ratio of competition then shifts on to OUSD, they essentially get like their same slice of the pie in a way and so it kind of protects them and so they might as well enter into it because it's better than getting fully disrupted for them.

**Chris** (51:56): Yeah, I agree. I think it makes total sense.

**Jackson** (51:59): So it sounds like open USD is like it's really hype, but really there's nothing to it and we just need to wait and see.

**Tyler** (52:07): Yeah. Do you think it's a better, is it more profitable for like if your Visa, would you prefer to keep getting like fees that are proportional to how much transaction volume you serve or would you prefer to get revenues that are proportional to how much like treasuries back your stablecoin? Like I wonder if it is an inferior business model for Visa, like it has to be right? Yeah, it has to be. Like the velocity of like a of these stablecoins is probably going to be quite high. And so...

**Chris** (52:41): I think what I'm interested in is actually like intra consortium member competition within their world garden, right? Like it's obvious to me that they're going to make it expensive to leave the open USD ecosystem. So like if open USD C is on base and tempo, like it might be easy to move between them, but to move to USD C on Ethereum may be more expensive. Yeah. But I'm interested to see how that plays out because like my feeling is like that there is going to be competition. And I don't know how they're going to handle that, whether there will be agreements on what fees you can charge moving between open USD venues, chains, whatever.

**Tyler** (53:18): Yeah, there's got to be some limit to how expensive it can be to cross chains or cross coins though, right? Because like all it takes is like one market maker that owns a little bit of both and like charges some fee and like that's... There's actually no barrier to being able to do that other than maybe the barrier to like operating the bridge infrastructure and like the wallets on multiple chains. For sure. It doesn't seem insurmountable to me that like multiple parties would do that and it would become like a very competitive landscape and those fees would like trend to be de minimis.

**Chris** (53:48): I think it's about how you control the burn desk. And Tether is famously good at this. The burn desk.

**Tyler** (53:54): What is the burn desk?

**Chris** (53:56): Obviously these stable coins represent dollar backed assets and the way that you get them back into dollars is you go to the desk. And the desk says I'll take your one stable coin and I'll give you one.

**Tyler** (54:05): This is like a physical desk that's like at the Tether office in the Cayman Islands.

**Chris** (54:11): I think in Tether's case it might be. How do you carry a tether? Yeah, it's a good question. Nobody knows. It's very secret. No, so I mean like one of the things that maintains a stable coin peg is this relationship that if I ever see the stable coin trading under a dollar I just take it and then I take it to whoever and I say, "Hey, give me a buck." And I pocket the drift there. But if your burn desk is very hard to get to or they have fees for burning, that can also change the price. So I'm interested to see how this plays out between issuers. Yeah.

**Tyler** (54:45): Are there like independent burn desks? Like basically anyone who would buy your... Like let's say that you want to burn Tether but they're like, "Okay, you give me one Tether. I'm only going to give you 99 cents or something." But then there's like Jackson's sitting over here and he's like, "I'm going to arbitrage that. I believe that Tether is fully backed and I'm happy to have a bunch of Tether or maybe I have a use case where people demand Tether and I'll pay you 99 cents for your Tether."

**Jackson** (55:13): Or something like that.

**Tyler** (55:14): Can that disrupt that lock-in mechanism of controlling the exits by having high fees on the burn desk?

**Chris** (55:24): Yeah, I mean, I think it absolutely can. I think it's all about back pressure, right? If there's a lot of pressure to get out of the asset and there's no way to get out to get it back to a dollar, the price of that asset will eventually go down because there's eventually going to be fewer and fewer marginal buyers for it. Are you aware of any rules in something like Genius

**Tyler** (55:44): about how steep the fees can be on a burn desk? That strikes me as almost a consumer protection thing where it's like, okay, they want to regulate the fact that Circle can't say, "Okay, when you redeem this, you only get 75 cents on the dollar." That seems outrageous, but yeah.

**Chris** (56:03): There are rules in it. The last time I read Genius was maybe six months ago. There are definitely stringent rules about having to provide redemption at this reasonable rate. I don't know exactly what it is.

**Tyler** (56:14): But there's some guideline in there. Events like outright abuse of that mechanism.

**Chris** (56:19): Yeah, but not everybody has access to it. And I think that's the thing. So if you can control the people who have access to the burn desk, you can kind of like, it's another level. Yeah.

**Jackson** (56:30): Wow.

**Chris** (56:31): It is hot in here. Dude.

**Jackson** (56:33): These lights are wild, the orange thing, I think it's putting awesome heat. I think the takes are just heating the whole room up.

**Chris** (56:41): They definitely are. Yeah. Solar level takes today.

**Jackson** (56:44): Yeah, maybe we will go and I will do my contrarian take.

**Chris** (56:48): Okay. What do you guys think? Yeah. Let's hear it.

**Tyler** (56:52): I feel like you need to shine this episode.

**Chris** (56:53): Yeah, yeah. Hit us with it.

**Jackson** (56:55): Yeah, we're just going to mix it up a little bit. This is kind of back to AI, so I apologize.

**Chris** (56:58): Okay.

**Jackson** (56:59): And, um, this take is, comes from, you know, my bubble of being a software engineer in the, in the tech industry. But there's a lot of software engineers that are afraid that our jobs are going to be gone. Yeah. Yeah. Perhaps Chris and I can, I can kind of empathize with that. But my hot take is that our jobs are fine for a while. It's other jobs that need to be afraid and it's the people that don't know how amazing the AI is that are going to be the most jock. Kind of how I think this is going to look is, um, you've seen like a lot of layoffs in the tech industry lately. Like many companies are shrinking by 10%, 20%, whatever. Um, and I think that's because less people can do more now with the AI. You can paralyze work and do it a lot quicker than you could. Tyler was just telling me that the AI estimated it would take a month to do some work. And then it did it in 15 minutes because it's trained on estimations from human executors, but it's way more quick, way quicker. So I think these engineers get laid off from the tech companies, but then we're able to move and automate other jobs. So more jobs will pop up in like different companies that we will slot into and like push out, uh, employees from other industries like, um, like accountants. And I think lawyers might be tough because they have like weird laws about who can do lawyering, you know, so like regulation will probably be an issue. But I think like the capability is there and I think that's how it's going to go. So more smaller companies that are doing, um, more automation in the world. I don't know. What do you guys think?

**Chris** (59:01): So you think we're just going to get displaced into everyone else's jobs and replace them. Yeah.

**Jackson** (59:06): So we're the AI, we're like, we're like, um, riding the guys like horses into North America. And they're like, damn, these guys are crazy. Yeah. But I think it'll be just kind of like that when the conquistadors came over to North America and they were like horsing about, they had to get a little homie that could speak the native language. Right. And then they would be like, all right, man, how do I tell your people that we're subjugating them? Right. It's going to be like, all right, Mr accountant, how do I make this? What a metaphor. Yeah. I mean, like conquistadors weren't exactly stand up people.

**Chris** (59:43): And I mean, we're going to take all of their jobs. I'm sorry.

**Jackson** (59:47): Yeah. That's my career intake. And it is terrible. Just like the conquistadors.

**Chris** (59:55): What do you think software will eat the world, Tyler?

**Tyler** (59:59): Well, I don't know if I can really predict how this would go about. I feel like one thing I've observed at the individual company level is that when one group of people, like software engineers, is like made so much more efficient with this one tool, but that tool hasn't diffused to other positions in the company, then you might expect like, oh, okay, well, the software engineers are so much more productive now. So you'd want like, they'll be the ones that are doing all the work and everyone else will kind of be pushed out. I think the opposite actually happens where like one company might have more or less kind of like a fixed amount of roadmap or like scope that they can do with engineering. And so now they can do that with many fewer engineers. So they can do more with fewer engineers. But then all of these roles that aren't like scaling as well with AI, those people actually like keep their kind of old numbers. So like the distribution of workers within a company, I could almost see like you have fewer people using way more AI and those people like, you know, there'll be fewer software engineers, but there'll be the same amount of people working in other functions that aren't really hitting that steep part of the AI adoption curve yet. And then I think then it's like, okay, let's say this company is making due with like half of the software engineers that used to have what happens to the half of the software engineers that aren't employed by that company anymore. And then I think you can see kind of what Jackson's looking for is like, oh, other companies will be able to deploy them because like one software engineer can go into some company that previously didn't want to hire like a whole team of software engineers and they can start like actually providing so much value just as a single person that maybe you start to see adoption of people into smaller, more traditional companies like that. Or you see this like beautiful explosion of entrepreneurial activity where people are just able to use AI to like scale themselves and to essentially build like lifestyle businesses where they can essentially work, you know, do the work that might have been like 10 people previously, but they can do that and that's like a great way to support themselves and they have a lot of freedom there. I think that's like a nice version of that future. That's the one that I would like to see. That's how it actually plays out because I think there's also like a scary version of that future where like we hit like, you know, artificial general intelligence or artificial super intelligence within the next like five years. And then that becomes a force that like is almost, yeah, like none of us basically are worthwhile employees anymore because there's almost nothing that a person can do that AI can't do better. And then also like the gains to that technology could just be held by, you know, the one or small handful of companies that build that technology. They have no incentive to then like lease out their super intelligence to like these other companies to like have their niche. Like they're like, we could just do all of this ourselves. So like that's a scarier version of that future. I hope that one doesn't happen, but that's what a lot of the like more science fiction-y people on X and the people who are like really into AI talk about stuff like that, like runaway super intelligence that just renders everyone kind of like functionally useless in the economy. And then you just hope that we have like UBI and we can, I don't know, go like play guitar all day and play tennis all day and just like live leisure and not have to work.

**Jackson** (1:03:40): UBIs. Could be cool too. Universal Basic Income.

**Chris** (1:03:43): Yeah, I actually think a jacked guy coming into my workplace and then pretending to be my friend and then replacing me and everybody I know is like way scarier than AGI. I think that's like a, that's a terrifying future. Hola.

**Tyler** (1:03:56): Yeah, at least if the ASI comes and it makes all humans like obsolete, then like we're all in the same boat. Right, exactly. It's not like, oh, like the really elite humans are like still like ripping with AI. It's just like now we're all just like UBI recipients. And there's no like hierarchy anymore because it's almost just like we're all, we're all on that same level of just being like pets of the ASI. I kind of like the crazy take guy on the pod.

**Jackson** (1:04:22): I guess it's like, yeah, it depends on the curve because the AI has really been improving super fast. And I guess, I guess my assumption kind of implies that it will, it will like be a logistical curve and will like plateau out. It'll still be amazing, but it's going to plateau out. Yeah.

**Tyler** (1:04:38): Do you think it's going to peak at like human, like the smartest human level intelligence?

**Jackson** (1:04:43): I mean, even if it does peak at the smartest human level intelligence, that's exactly what anthropic has said. Like having an entire state of geniuses in the data center, that's still pretty, that was pretty poorly for all of us, I think. Yeah. I don't remember what I was going to say, but.

**Tyler** (1:05:02): Yeah, I'm just skeptical that it will somehow stop at like, you know, like human level or something resembling human. Like I think that would basically require like a very abrupt kink in the curve from where we are now. Right. Because I think that if you look at something like Fable, it's already like probably the most generally smart, you know, being that you've ever, ever interacted with. Just like complete Renaissance, Renaissance man, like rips it at all of our jobs and knows everything.

**Jackson** (1:05:29): Yeah. So yeah. So you're saying exponential curve and then I agree that it could be over. Like progress would basically have to plateau where we are right now for

**Tyler** (1:05:37): it to not reach some kind of like thing that functionally to us is super intelligence.

**Chris** (1:05:42): I mean with enough regulation, we can make it happen. We can stop here forever. We can try, but China is just going to overtake us and mug us hard.

**Jackson** (1:05:49): And this is like the United States, a secondary bet behind like, okay, let's release all these stable coins and get all the countries to put their money into our stable coins so we can continue to be the reserve currency and inflate away our problems. Our secondary bet is that we'll create the AGI and we'll be able to like use that to grow out of the problem, as you say. So I don't think we're going to regulate, regulate it down. I think we're going to go as far as we can, but I mean, this seems like really naive to say, but the, the AI is trained on all the information that, you know, humans have produced. So who is to say that they will become significantly smarter if the information they're training on is just what we have produced ourselves. Maybe that is where we start to bottom out. We're like reaching. Okay. It's getting a lot of it. And yet it has a bunch of like liquid knowledge or liquid memory, but how much farther can it go? Maybe a plateau.

**Chris** (1:06:51): It seems like it's getting a lot of utility out of being like the 20 smartest people, you know, like, cause those are like different people with different skillsets. And from what I've seen from Fable so far, it's just like, it's all of them. It's like a great lawyer, probably. I don't know. I'm not a lawyer. Maybe it's terrible, but it's definitely a good software engineer.

**Jackson** (1:07:07): When it laid off, when, when my coworkers were laid off, I wrote an article saying like, now, now I only have one coworker and it's AI, but it's nice because I can talk to it about all my interests. I can talk to it about tennis and it's very knowledgeable. I can talk to it about triathlon. I can talk to it about weightlifting. I don't, I mean, engineering is okay. You don't even try to talk to me about those things.

**Chris** (1:07:32): Yeah, it's crazy. I thought we were friends.

**Tyler** (1:07:35): You haven't even opened your heart to me.

**Chris** (1:07:37): We've been replaced. Yeah.

**Jackson** (1:07:39): You're replaced before we even met. That's not true. We talk about these things together, but it's like now, it's like, if I'm ever bored, I can just hit up my boy chat GPT. Yeah. You actually talk to chat GPT and you're like, I don't know, tell it about your, uh, your training today.

**Tyler** (1:07:56): You're like, I like maxed out my deadlift. Yeah. Nice Jackson. I love that for you.

**Jackson** (1:08:03): Literally two days ago, I was like, okay, I'm going to try to do a 455 deadlift. And I was like, I've done like last week I did 375 four by four. And it's like, you should be able to do that easy. Not like fuck.

**Chris** (1:08:15): Yeah.

**Jackson** (1:08:16): I'm going to tear it up. And then I'm like, okay, I'm also going to try 275 bench. But I only did like 225 four by four or something. And it's like, Oh, you better watch out. Maybe start at 265, which I did. And I did 265, but I failed 275. So chat GPT is yeah. I do. I do talk to it about it.

**Chris** (1:08:37): It's it is a good, it is a good trainer and it remembers you too.

**Jackson** (1:08:40): So sometimes it's like, I know that you have a hard time not exercising, but you really should take a break. And I'm like, yeah, sorry. I'm just like, screw you.

**Chris** (1:08:48): Uh, Claude diagnosed my game of thumb, which you will know is something that I have from last episode where I got laid out by Tyler for playing Halo at the age of 22. Um, this is unrelated, but yeah, it's like,

**Tyler** (1:08:59): this is where the trauma of gamer thumb. Yeah.

**Jackson** (1:09:03): Yeah. You were too hyped on monster and you were like tweaking out while playing Halo three. And this is a repetitive stress injury that has now carried on.

**Chris** (1:09:13): Super strong thumb muscles. Yeah. Yeah.

**Jackson** (1:09:17): Yeah. How is the gamer thumb coming along?

**Chris** (1:09:19): That's terrible. Actually, I don't know if you saw, but I came here with a brace today. Um, so I think I just have game of thumb forever now.

**Jackson** (1:09:25): We'll start to do weekly updates than the gamer thumb.

**Chris** (1:09:28): I'll wear it to the next part. Have you, have you tried, uh, voice dictation? I feel like last week we were all trying to tell you that you should just

**Tyler** (1:09:34): never type again and you should only dictate Claude.

**Jackson** (1:09:36): Yeah. Yeah.

**Chris** (1:09:38): I'm just like, I'm just so obstinate. Like, you know, I have like a special keyboard, uh, for like special boys, the split keyboard. Yeah.

**Jackson** (1:09:46): Yeah. Yeah. Yeah. Um, yeah.

**Chris** (1:09:52): So I mean, I should, I will try it after I like, you know, I have to hype myself up.

**Jackson** (1:09:56): Yeah. Hmm. Yeah. Well, we'll start to do weekly updates on, on the gamer thumb. I didn't know that Pico was going to continue. Continue to be a recurring topic.

**Chris** (1:10:05): I hope that because help will recover.

**Tyler** (1:10:07): No, I didn't want him to be on.

**Jackson** (1:10:08): Those are racking up.

**Tyler** (1:10:10): I have to start to go fund me. Go, go fund me, put it all into purple fortune. Yeah. And if it liquidates, then Pico is going to, yeah. He might not get healthcare. It's going to be sad. So everyone should donate to us. Definitely.

**Chris** (1:10:27): And choose a good pub Claude, because like, really this is all riding on the robots.

**Jackson** (1:10:31): Yeah. We'll try fable. Maybe we'll do purple. We're going to start doing purple fortune, every podcast, just so you know, respect and we'll try fable maybe next week. And we're considering having a, a listener call in and say like things that they're bullish about. Right. And then we feed that into, into purple fortune. In addition to all the information it collects and you know, then it's on us. Yeah.

**Tyler** (1:10:54): We're the exit liquidity. Just a single fan. It's supposed to be the opposite. They're supposed to be.

**Chris** (1:11:01): Yeah.

**Jackson** (1:11:02): We're supposed to be shilling them coins. Nothing on them, but you want to reverse this out of the goodness of your heart. We're going in together. So please drop a comment. I know the first thing about a crypto podcast. We're the virtue of crypto podcast.

**Chris** (1:11:16): It's a consortium. Yeah.

**Jackson** (1:11:18): No, cause source. I don't even know what that word means. And we've said it like 15 times. It sounds like contortionist. So about right. Yeah. I think, I think we're done unless there's anything else you guys would like to get after.

**Chris** (1:11:31): No, that's it for me. Like huge. Thanks to Presidio for letting us use this space. Yeah. Yeah.

**Jackson** (1:11:38): Let's go.

**Chris** (1:11:39): Yeah.

**Jackson** (1:11:40): Enormously cool. Yeah. Super cool.

**Chris** (1:11:43): It's very hot, but very cool.

**Jackson** (1:11:44): I don't know if we'll ever, please don't get used to this or like. Yeah.

**Chris** (1:11:48): This is never going to happen again. Next episode I'm recording on a 2003 ThinkPad. So see you guys then. Yeah, we're out.

**Jackson** (1:11:56): So wait, do you need your laptop? Are we doing that thing? Well, if we want to listen to the Claude AI generated segment, but that's like a, it's like an eight minute video or audio file.

**Tyler** (1:12:08): So we don't have to listen to all of it.

**Jackson** (1:12:09): I can just queue up a couple of minutes of it and then we can talk about it.

**Tyler** (1:12:12): But we don't, we don't have to do that at all.

**Jackson** (1:12:14): Yeah.

**Chris** (1:12:15): I don't have a fortune in set up. I see.

**Jackson** (1:12:18): So this is a no perfect fortune.

**Chris** (1:12:20): I mean, I mean, I could set it up, but I would take five minutes.

**Jackson** (1:12:24): Five minutes.

**Chris** (1:12:25): Yeah. I don't know.

**Jackson** (1:12:27): Is it worth it?

**Chris** (1:12:28): No. I mean, we can roll pepper fortune in next episode, like maybe do a twist on it. Okay.

**Jackson** (1:12:33): Yeah. We're sorry. We're sorry to our fans that love the purple fortune, but the purple fortune will not be here today. Wait.

**Chris** (1:12:39): Are we actually live? Unfortunately.

**Jackson** (1:12:41): We were deliberating. Well, we weren't deliberating, but then we went live. We're giving away the alpha of our future segments.

**Chris** (1:12:47): Unfortunately. No, we're making a commitment. Yeah. We are. Sorry. We're committing to, I let the team down.

**Jackson** (1:12:53): Do we do for a fortune every time?

**Chris** (1:12:54): What we did. We did it one time.

**Jackson** (1:12:56): Yeah. It's the bottom of our franchise.

**Chris** (1:12:59): Okay. So we are the purple fortune podcast.

**Jackson** (1:13:02): It's, it's just something that goes on in the background. It's like a, you know, window dressing to all of our talks on the pod. Yeah. When they get tired of looking at our faces, they can look at the, I would never get tired. Okay.

