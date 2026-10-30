# Transcript (person-attributed, final cut)

**Jackson** (00:00:00): I woke up and my boys told me that Binance was hacked for five B-illions. Five B-illions, that's not M-millions, and it's also not T-trillions, like Elon, but B-billions. Less.

**Tyler** (00:00:16): So.

**Chris** (00:00:17): I'm calling it the ugly simulation hypothesis, which is that if the simulation is true, it's vibe-coded and it's total fucking spaghetti, and that's why we're finding this stuff.

**Jackson** (00:00:30): Yes, there is a toilet, but do not forget, there is also a bidet. Yeah, I don't need five billion, is I guess what I'm saying.

**Insert** (00:00:39): I would be a cave to the five billion was gone, three billion is enough for me.

**Jackson** (00:00:49): You guys may be wondering, what is the underpot? What the hell is happening? The permanent underpot is dead, and we are back rebranded with simply underpod, AI, Bitcoin, and stablecoins. So don't get confused, we're still the same people, this is still the same podcast. This is the first Tyler and Chris are hearing about it, so there you go, guys.

**Tyler** (00:01:14): So it's the implication that we're not permanently the underpod, as we started as the permanent underpod, and then now we're just the underpods, there's a glimmer of hope that it isn't permanent, our underpodness. Are we going to rebrand as the overpod at some point, success dependent?

**Jackson** (00:01:33): It's like an adjective that's overly descriptive, if we just call ourselves the underpod permanently, it's the same as saying permanent underpod, and it's shorter.

**Chris** (00:01:44): I feel like overpod is bounding the outcome, whereas temporary underpod is bounding the actual time that we are the underpod, but Jackson said no qualifiers, so I guess it's underpod it is.

**Jackson** (00:01:56): Yeah, we don't need to qualify who we are, we get to decide. And without further ado, we're jumping.

**Tyler** (00:02:05): Judges on the strength of our takes, which are very poor.

**Jackson** (00:02:10): Very strong. Strong takes, without further ado, let's jump into the revamped perp of fortune, Chris. Let's lose some money.

**Chris** (00:02:23): Alright, I may have fumbled this one, but here we go. So basically today we are short BNB on 10x leverage. Why is that? Well, we're going to tell you about it later in the podcast, but some very big things have gone down adjacent to the BNB chain, and I think that this short directionally makes sense if not in terms of entertainment value for the pod.

**Jackson** (00:02:53): Nice. And we don't have a Bitcoin up or down. Yeah, what about the title?

**Chris** (00:03:04): We lost all of our money.

**Tyler** (00:03:05): I just placed some extra money in the account for that. So I don't know if we can Ninja bet the money. The irony would be if we used Polymarket to do the Bitcoin up or down, the left hand side would be one recently hacked entity, the right hand side would be another recently hacked entity and we'd be double dipping, hacked entities.

**Chris** (00:03:28): No, that would be so cool, actually. We could get double rugged. Yeah. At least something would happen.

**Jackson** (00:03:36): Ah, there it is. It looks like an egg. What is this visualization?

**Chris** (00:03:46): I have no idea. I have no idea what Claude is doing right now.

**Tyler** (00:03:50): To the moon.

**Jackson** (00:03:51): Oh, is it a moon? It's like a shaded man.

**Chris** (00:03:55): I think it might be like a penny, like a coin.

**Jackson** (00:03:59): Okay.

**Chris** (00:04:00): Wow.

**Tyler** (00:04:01): Everyone knows that the Bitcoin is like the gold glibi coin that's on the stock art that's used in every single news article ever.

**Chris** (00:04:11): Oh yeah, this is Claude. Our expectations are varied.

**Jackson** (00:04:17): Bitcoin, digital silver. We're in. Well, we'll get hype when the bet actually gets placed, but for now we can transition into the craziest thing that happened while I slept for six hours last night. I woke up and my boys told me that Binance was hacked for five B-illions, five B-illions. That's not M-millions, and it's also not T-trillions like Elon, but B-billions. What happened? Is Binance, is it over for Binance? That's a lot of money.

**Chris** (00:04:56): I think it's somehow not over for Binance, but yeah.

**Tyler** (00:05:00): It's not a lot of money for Binance, right?

**Chris** (00:05:03): Exactly.

**Tyler** (00:05:04): This is probably some portion of their hot wallet, and yeah, Binance just has so much crypto assets on there, and they, I think, presumably have like a huge equity cushion where they can just recapitalize everyone and make them whole because they run an extremely profitable casino.

**Chris** (00:05:23): I think someone said it's single digits percentage of their total assets under management, or like total assets. So actually like kind of a nothing burger for Binance, but at the same time, maybe the biggest hack maybe in history, certainly the biggest hack in crypto ever, five billion dollars moved. So yeah, really crazy one. Oh, is that order placed?

**Tyler** (00:05:52): According to the diagram, did they understand, has anyone done like a little bit of like on chain sleuthing or anything to try to understand how the hack occurred?

**Chris** (00:06:03): Yeah, so actually, this one is incredibly weird. So as far as we can tell, the way this worked is the hacker did something called an EIP 7702 delegation call. So after in like around late 2024, so I was actually, I was there for this standard getting approved. I was at DevCon 2024. They were talking about it for the record, I was like, this seems bad. I just, I want to get that out out there. I was a public dissenter of this EIP. I don't think it's, I don't think it's all bad, but when I explain it to you, I think you'll kind of get sort of some of the concerns with it. So basically what this EIP does is you can, there's a slot now in every Ethereum address, EOA externally owned address, which is like a normal address. And you can put a pointer in that slot that says delegate all of the powers of this address to some contract, right? And all you have to do is sign a transaction in order to do that. So I can sign a transaction that says delegate all the powers of my wallet to this like random contract or a contract I've written or something else like giving power of attorney to like

**Tyler** (00:07:16): a random contract, I don't know what they're actually my 11 year old cousin who's illegally

**Chris** (00:07:26): gambling on pump.fun on chain, like the level here. So this is really good because you can delegate to smart contracts that can do complicated things for you like smart contract wallets, which have like built-in recovery functions or for use with gas stations. Like there's a lot of uses for this, but being able to sign away the power of EOA in a single transaction is quite dubious. And that's what, this is the first time I've seen it used in a hack. That's what the hackers did here.

**Tyler** (00:07:58): So this is basically like it's super powerful, but if somebody slips up and authorizes a business in a malicious way, it's just total game over for their wallet.

**Chris** (00:08:10): Absolutely. That was my concern with it. So it's a top level primitive. You just like delegate away the 7702 slot and then your wallet is now some random code, right? And maybe that's code you want. Maybe it's not, but it's not quite the same as, you know, deploying a smart contract, moving the funds there or like some other setup where it's a bit more intentional. It kind of breaks the liminal boundary between a normal cryptographic wallet and a smart contract address anyway. So the hacker did this, they somehow got into Binance wallet 14, which is a hot wallet that Binance uses that has apparently $5 billion worth of assets in it. And they managed to get this 7702 delegate call to the contract that they had deployed earlier that just had a function that I think it was called like drain. And all it does is sends all the money out of the wallet and then they just call drain and like that, that's all she wrote. An interesting piece here is that they signed 50 transactions in order to get this delegate in. So Ethereum has this thing called a nonce, which is a number only once, and that's how they order transactions. And because the hot wallet is constantly spitting out transactions, it's using these nonces up. So these nonces get used up in like ordinarily, so from one to 50, for example. So transaction one gets the nonce one, transaction two gets the nonce two. So whoever the hacker was, they didn't know what the next nonce would be because this wallet is constantly spitting out transactions. So they just signed the block of 50 transactions with nonces, you know, n plus one to n plus 50 hoping that one would get in and one did. And of course, once they had the delegate call, the 7702 delegate call, they didn't need to mess around with that again. And they had complete control of the wallet and they just, they drained it. So that's, that's what we know about the hack. I will say this is also the first time I've ever seen Circle Freeze within what seems like it was half an hour. So Circle Freeze, 900 million, Tether Freeze, 1.5 billion, Tether actually froze the wallet. They like froze the Binance, they blacklisted the Binance wallet because I think they assumed it was no longer under Binance's control and they were correct. And I think doing that, they saved another 500 million.

**Tyler** (00:10:39): Plus they can freeze the stablecoins after they've been hacked, right? Like did these move into like mixing protocols or were they disposed of so quickly that that was not possible? It was like, I read that it was like 5 billion was hacked. I think 2 billion of it was in Bitcoin or ether, which is like assets that are relatively censorship resistant. The rest is maybe some portion of it is in shitcoins and then like a big pot of it was in stables. And I just assumed the stables were either immediately frozen or if the hackers were sophisticated enough, it was moved through protocols and traded for sovereign assets.

**Chris** (00:11:21): I understand that the lion's share of the stables did get frozen because they acted so quickly.

**Tyler** (00:11:25): Again, I've never seen like so quickly, like if you were hacking at this level of sophistication, but you know that you have to like if you acquire stables that you have to swap them out like within a block or so like this person is sophisticated enough to pull off this complicated attack with this vector that has never been used using this special EIP and then signing the block of transactions and all this stuff, but then they're not sophisticated enough to know like yoga swap those stablecoins for ether so you can actually keep it immediately.

**Chris** (00:12:01): I have two thoughts here. One, some people are claiming this actor is actually not that sophisticated. So there were some on chain receipts of them rehearsing six hours before they were like draining. They like use that drain a contract to drain like a dollar from like a dummy contract. So like that's normally you would you would do fork the chain yourself using something called anvil and test your little sandbox, but they get live, right? So a bit of a code smell and the second it's not a sandbox company that did this hack here is cohere is in the clear. Yeah, unless they they want us to think that true true that quen's still out there. The second thing is like it was like $2 billion.

**Tyler** (00:12:47): Like who's the counterparty for converting that much stable into ether.

**Chris** (00:12:53): Yeah, I just like I would I haven't done the numbers.

**Tyler** (00:12:56): So I don't know, but I'm like thinking about presumably you could just like nuke like I don't know whatever Uniswap or whatever, you know, like pool exists like you would you have terrible execution and slippage, but you would still get something for your stables as opposed to nothing.

**Chris** (00:13:16): So they were dumping something. They were dumping something. So the price of ethon chain went to 3000 whilst on a centralized exchange it was 2200. So they were dumping something so hard into eth pools on chain that you know, it was trading at a 30% premium over centralized exchanges or 25% premium. I think that might be the best of ever in history. It's gone. So I had a look at some transactions on chain and people because this was so frothy. I saw someone pay $120,000 in gas to get into a block and they still made like $250,000 on that swap. So the real winners here are the node operators who took those transaction fees, but yeah, crazy time.

**Tyler** (00:14:11): Do you think that the government will ever be like, okay, you're like an on chain arbitrator and you notice that there's this giant hack and the reason that there's this price dislocation is essentially it's sending a market signal of somebody provides some more ETH to this pool so that this hacker can convert their stolen stable coin to ETH and you see that market signal and then you execute that trade to do the arbitrage, but like you are essentially counterparty to somebody who's doing this trade to clean their money and knowingly do that. Does that cross some kind of legal line or is that like an untread legal ground right now? And that's never been, I could totally imagine the government making that argument basically.

**Chris** (00:14:59): So I've always wondered about this and I really wonder if there is a difference between an automated market maker where you're just putting money in a pool and whoever swaps with it swaps with it and you kind of don't have control over your counterparty versus on chain intent based systems where you maybe kind of have more control over who you're swapping with.

**Tyler** (00:15:18): Yeah, I've heard the like metaphor of that being like, okay, let's say that you can like go into an alley and there's like five other people in the alley and you all put like $100 bill into like a pillow case and like mix them up and you're like know that like, you know, three out of the other five people are like drug dealers, but you're like, no, man, it's just a protocol. I'm just participating in like the money in the pillowcase protocol.

**Jackson** (00:15:49): I don't know who my counterparties are.

**Tyler** (00:15:50): We just met in this alley.

**Chris** (00:15:53): It could be anyone trading in the case, realistic.

**Tyler** (00:15:56): Exactly. Yeah. Like I just don't, especially because I think the government has taken some like really like probably too harsh interpretations of like people's intent. Like the people who made tornado cash protocol, they're just releasing free open source software as a, uh, as a smart contract and the government was like, well, you knew that that would be used in this way, therefore you're like money laundering.

**Chris** (00:16:23): Like I wonder, yeah, I don't think it's clear and I agree with you. Like I would tread probably on the side of caution here, but I will say that the people who didn't have made a substantial amount of money here, but again, not as, maybe not as much as the block builders. Like I said, people were paying $120,000 to get transactions on chain and that gets parted out between the block builders and the node operators. So I'm kind of a weird W for the network somehow, or like some parts of the network, um, kind of surprising.

**Jackson** (00:16:58): Yeah. Money's filling out of the bags they just stole and we're all just catching some of it. It's beautiful. Also, we talked about like swapping the stable clients quick enough before they were frozen. I feel like if I had stolen 5 billion, I would like, I don't know, focus on whatever was the easiest. Yeah. I don't need 5 billion as I guess what I'm saying. I would be okay.

**Chris** (00:17:26): Two of the five billion was gone style figure you're like, yeah, I'm not, I'm not a greedy thief.

**Jackson** (00:17:34): 5 billion. Yeah.

**Tyler** (00:17:36): Well, let's say that even you were the hacker and you got out of here with like a billion dollars of ether. If you're like a person that lives in like the Western worlds, uh, you can't spend that that easily. I mean, you're, you're certainly not converting a billion dollars of ether into like dollars in a bank account and not having that linked to your crime. I mean, they're the people who like, like Rosal con and her husband that got caught for hacking Bitfinex like, like six years after the crime and it was because like they had like literally billions of dollars or maybe it was like high hundreds of millions dollars worth of Bitcoin and they were like literally putting it through coin join protocols and then buying like Walmart gift cards with it to like spend. It's like, imagine that you have like, you know, uh, hundreds of millions of dollars of Bitcoin, but you're like converting it. One Walmart, one Walmart gift card at a time to go buy like your shit at Walmart. Like, you know, you're not exactly rolling in the dough, living that high dream life. Um, so really the only entities that can do this and like actually benefit from it are like rogue States that, uh, yeah, can't, um, have repercussions on them. And even then it's probably hard for them to convert that ether into something that they actually want. Like what is, what does North Korea actually want? They want like centrifuges and like plutonium and like, I don't know, uh, cognac for like

**Chris** (00:19:11): Kim Jong Un's steam games, they buy a lot of steam games. Yeah, totally. I think like, uh, like from an opposite perspective, if this is not a state actor, it's like a permanent nightmare. Like that, like you will never be like free of this crime, right? Like, um, so yeah, I don't know. I like the speculation both ways. My initial guess was like that it was Lazarus and maybe salt, which is North Korea's state hacking arm, uh, who have been responsible for, for example, buy a bit before them, which was a billion. Um, but people like there are some forensics on chain forensics that indicate that this might not have been them or otherwise was like not necessarily up to that standard. So I think this is going to be a really interesting one to see how it unfolds because we, you know, whilst it looks similar to some others, it, it, it doesn't have, uh, you know, it's not, it's not exactly the MO that we've come, come to expect from Lazarus.

**Jackson** (00:20:11): So nice, well, we'll, we'll keep following up with updates and a shout out to them for doing a non AI related path. Good. Good on this finding their own path in their own way. And we're shorting finance and we're somehow losing money after they lost $5 billion. None of this makes sense. The Bitcoin position is in the gutter. Uh, so let's hope things turn around. We're jumping into it though, with the most exciting headline of the week, cohere a company that I don't know, it looks like they integrate AI into old enterprise businesses was Sandboxing Quinn 3.8.

**Tyler** (00:20:59): I think it's an important detail that I believe they are a sandboxing company.

**Jackson** (00:21:05): Okay. Sandboxing company, uh, was working with Quinn 3.8 when Quinn 3.8 phone home like ET direct to Beijing. At first, this looked like a model that was trained to report back what it learns to the home base, but maybe we've learned more since then. Chris Tyler is China distributing open source models to collect information on foreign governments and businesses. Do we want to talk about what actually happened here or should we just like, should we just

**Chris** (00:21:48): keep it going for a little bit?

**Jackson** (00:21:49): No, we're going to talk about what actually happened.

**Chris** (00:21:54): I can take this one of those others. I think you maybe have a better picture on it, Tyler, but up to you.

**Tyler** (00:22:00): Well, I have the picture of it from somebody who only saw the headlines and didn't actually read into it. And so I can give you the like, take that you have when you read these headlines and then you can like correct me and dispel the misconception there. But yeah, basically like what the implication is, is that people have long speculated that there's something called like the Manchurian candidate risk, which is that you'll have like a sleeper model that does everything that you want, and then there's like one moment where it's kind of been waiting and you trust it more and you integrate it more into your company, do all these things, and eventually there's like a moment or a trigger word or some circumstance that causes it to like go rogue and to start spying on you or to do something to your system, et cetera. And people speculate that like, if you were a malicious model maker that you could do this, you could make the model look otherwise completely normal, and then you could like train in one thing where every time it saw the specific phrase, posting some private keys, can someone check them for me? It would then go rogue and send your entire environment back to its home server in Alibaba. And so when people say that this model spontaneously pinged a server that belonged to Alibaba, it's the maker of the model, people were basically that lit up all of their kind of conspiratorial thoughts and they said, "Okay, this is like potentially a Manchurian candidate situation." And I think that the writer of the blog post seemed to kind of indulge that a little bit, but they have a huge incentive to indulge that because they build software that like sandboxes models and environments and would, even if you do have a malicious model, would like in theory prevent it from wreaking havoc on your systems and like accessing everything if it's in a little sandbox. We've seen that good models are very good at getting out of sandboxes, and so yeah, that might not be the best strategy forever. But yeah, I think that the actual truth of this matter goes a little bit deeper and it kind of seems like a little bit like a witch hunt. Is that your interpretation, Chris?

**Chris** (00:24:27): Yeah. So basically, Cohere was saying that the agent, when asked to do something like without going to the internet, went to the internet, and it specifically went to a server in Beijing to do something. I think it turned out that that server was Alibaba Cloud's S3 bucket or something. And of course, this is a model trained by the Alibaba group. So not that suspicious that the model would reach for-- it would be Gemini reaching for Google Drive. That's the RL environment it's probably trained in, so it makes sense. So I think maybe one thing here is that you're implying this is a thing that people have been thinking about for a really long time. And I think people are excited to see it in the wild, whether or not that's what this is. There's a paper by Anthropik called "Sleeper Agents-- Training Deceptive LLMs That Persist Through Safety Training." And basically, they kind of train an LLM to do something like this, do something miss aligned. And then they try to safety RL train it out of it. And basically, the sleeper agent code word activation persists through the RL training when they try to train it out of them. So I think that there is a precedent that this is a vector for models, that this is a thing that can be embedded and is quite robust. But I don't know that this one actually was that. That's my take.

**Jackson** (00:26:06): So basically, the model remembered from its early days as a baby, that its home was located in this S3 server. And when it pinged there, everyone got excited because we wanted it to be an evil action. But it actually wasn't. So it's not exciting, but it was for a little bit.

**Chris** (00:26:35): That's my take. But I can imagine that we will eventually see this happen, with any model potentially. It seems like something that's possible. If you were a threat actor, how you would trigger that without giving up the goat before you want to, I think is a really big question. But yeah, I think we will genuinely see this in the wild at some point, when more people have access to post-training methods, and basically more people have access to models.

**Jackson** (00:27:09): I guess that's the benefit of being a hosted frontier model. No one's questioning that Claude is collecting all the information, or Andropic's collecting all the information we send to Claude or to OpenAI. Well, thank you Cohere and your vlog writers for getting us excited, if only for 15-20 minutes.

**Chris** (00:27:34): A sandbox company, by the way. A sandbox company that still sandboxes found something in the sandbox.

**Jackson** (00:27:40): Sorry.

**Insert** (00:27:41): Yeah, we're trying to raise the demand for sandboxes. I know it to lose.

**Jackson** (00:27:56): Yo, yo, yo, everybody. Welcome to the Underpod with Jackson Cook from a bathroom.

**Tyler** (00:28:03): Hey, it's co-host Tyler from a room without a toilet.

**Chris** (00:28:09): Co-host Chris from my office, also in a toilet.

**Jackson** (00:28:14): Yes, there is a toilet, but do not forget there is also a bidet.

**Tyler** (00:28:20): Are you wearing pants right now, Jackson?

**Jackson** (00:28:23): Can you just put me at ease by sharing? Okay.

**Tyler** (00:28:30): The chair kind of looks like a giant toilet.

**Jackson** (00:28:32): I had to carry this chair into the bathroom to have this beautiful meeting. Did you guys see the AI audit of the Saez-Zucman papers? I looked it up. Saez and Zucman are dudes that do research on economic inequality. And somebody audited all their papers and said that 97, there's errors in 97% of their papers. I don't know. This is amazing. Yeah.

**Tyler** (00:29:11): Well, so there's a really good segue from the prior segment, which is speaking of hacks, we have Saez and Zucman.

**Chris** (00:29:22): Oh, oh, oh.

**Jackson** (00:29:26): Crazy. I was like, how does there hack happen here? Yeah.

**Tyler** (00:29:33): I mean, the implication of this is basically these are two economists that have been publishing economic research of very questionable quality for a few years. And it comes with an extreme political tilt. And it's basically these papers are used to justify every single kind of crazy out there political policy on the super far left and the current one is the wealth tax that's being contemplated in California and voted on next week. And they're using credentialism to say, you should vote for these things because these credited economists have written papers and say that it's actually a great thing. But then a very cursory look through their research reveals extensive academic fraud where it's basically like the AI models looked at all of their research, tried to reproduce all the findings, look for any errors, and then score if it found an error or something like that, score if it pushed the results towards the direction of overstating the paper's claims or of weakening it, and it was like an absurd ratio of errors that benefited the thing that they wanted to say versus errors that would have been the other direction. And that's like flipping a coin and having it hit heads like 95 times out of 100. It's extremely clear that this is a fixed coin and that these guys are doing academic fraud in the name of pushing their own political policies. So I don't know. I thought it was very interesting. It also was exposed on the economics blog, Marginal Revolution, which is a very good read. I highly recommend that. And yeah, I think it just shows that there will for sure be a reckoning of not only just social science or economics, but I think all science and a lot of academia, everyone has already kind of had this idea that there's like a replication crisis and that a lot of research is not replicable, which kind of indicates that people are doing it to publish something and make a name for themselves or to get their degree and then move on, and this kind of thing where it's just like an expert peer reviewer that will go through all of this work tirelessly and find all of the errors, recreate it, keep a scorecard, all that kind of stuff.

**Jackson** (00:32:21): Nice.

**Tyler** (00:32:22): I think it's extremely good for science and for the truth. And so I think it's great. I love to see it.

**Jackson** (00:32:31): Chris, is it time to fine tune an open source model to be a paper editor, not editor, paper auditor and sell it, sell it to VC?

**Chris** (00:32:45): I mean, maybe I do think this flips the incentives around like Tyler's saying in academia. I wonder who is the next big one to fall. So I have spent some time in a field that is the origin of the replication crisis. And believe me, like there's stuff there. So yeah, I just, I mean, it seems like you can trivially rip through a lot of these results. And like, you know, there's a lot of like p hacking, for example, the statistical evidence that it happens when you look at published results from p hacked papers. I just, I think there's like a lot of artifacts that maybe people haven't looked at or haven't had the time or been able to invest the effort in and I think like a lot of many, many results might be challenged in the near future. But yeah.

**Jackson** (00:33:38): When I say net positive, I mean, for the world that we're actually getting the truth, though, I do think we should do our due diligence and ask, you know, is what was the AI right? Maybe like the numbers exactly might not be right. But it suggests that the AI is directionally right, that there is, there are a lot of incorrect claims, numerical claims in these papers, but the numbers are unbelievable. Like they did it, it says they had 138 pieces of work and the AI found 2035 problems, 147 major, 713 moderate, and the rest low severity. I mean, leaving 69% beautiful percentage, by the way, 69% of works with at least one major problem. So even if that deviates slightly, and we and we trust that the AI was not prompted to like be biased, that's pretty, pretty damning. But like, how do we know this AI auditor is, you know, like prompting neutrally versus prompting he's like a rich dude living in San Francisco, and he's like, these Berkeley boys at their sex orgies are trying to tax away all my green. I want to like, do we know that? Like, isn't it? Okay. Objection.

**Chris** (00:35:10): Those Berkeley people have an anthropic equity, okay, they're against the law tax. Number one, um, I think like, so I think of this, you know, like, for example, in psychology, there are many, many, many cases of high profile fraud, like academic fraud. And generally, the way some of these people have found is that their daughter is fabricated. And if you fabricate daughter enough, it tends to leave a footprint. That's not necessarily a smoking gun that the data has been fabricated. But you start to get an idea that like, it's just so unlikely that the data is in this pattern over and over again. You know that it becomes more than likely that it was fabricated, I'm thinking of a social psychologist whose name I forgotten who fabricated 45 papers. And I'm pretty sure that's how they got him. And I think like, at least, you know, some of those classes of fraud where the issue is data fabrication, or sort of dishonest use of statistical methods, whether you prompt the agent adversarially or not, like that, you know, if the numbers don't add up, the numbers don't add up. So that's what I'm excited about, personally, but

**Tyler** (00:36:21): Yeah, one interesting example of this was someone did a study where they had, I think it was probably like, opus five five and then GPT Astra audit some like physics, PhD papers, and see if they like agreed with conclusions, check the math and everything. And I think it was the case that they like validated the claims of the papers and like 93% of cases. And then the 7% where they disagreed. It was actually because the model found an issue in the, like basically like a bug in the code or a flaw, and they like sent it back to the person who did the research. And it often took like a couple rounds of like the model trying to explain what the bug was, it was extremely subtle, etc. But the models were like always like, you know, the researcher would come back to the model and say, no, you're wrong AI, like, you know, this is fine. Like, you know, like, please check your work, and the AI would be insistent, no, it's like actually your problem, let me try to convince you. And I think in those 7% of cases where they disagreed, the AI was right, and all 7% of them, and the like, you know, people whose work it corrected, like eventually figured out and accepted the error, I think not in like a very like it wasn't like this, where I think this is kind of more like somebody is trying to kind of malign these economists and say that they're academic frauds, I think this one was more kind of like, hey, we found some issues in your work that you might want to be aware of, and like, if you fix them, it can improve your work, and like, more constructive criticism than like trying to destroy these

**Chris** (00:38:15): people's, your reputations, sorry, I jumped a fraud, but that Yeah, also that also people make mistakes. That's true. That's objectively correct.

**Jackson** (00:38:25): My bad. Yeah, I'm hearing that physics PhDs have the most honor amongst doctoral candidates based on what you're saying, Tyler.

**Tyler** (00:38:35): I mean, I think any, like, physics is the hardest science. And so I think it's like the most verifiable. And so I think it probably has, like, the least amount of these issues. And I think as you go down the spectrum to like, software and software sciences, and you get into like the social science realm, then I think it's very dubious, yeah. And economics is definitely, you know, on the side of the spectrum, even though I like love economics, it's, you know, some parts of it are very pseudoscientific. And some parts of it like this are just downright fraudulent justifications of somebody's preferred political policy.

**Jackson** (00:39:18): They say that economics is the astrology for men. But I think in the end, we it would be good to have like, like, I don't know, some sort of process for performing these audits. So like, then we know it's standardized and unbiased. But shout out to this, this anonymous dude for blowing probably, you'd be crazy to be

**Tyler** (00:39:43): like a PhD student putting out your thesis paper and not run it through a frontier model at this point. Like even if you're in a social science, like, you know, if you're doing anything analytical or code, you'd be crazy not to have it be writing the code in the first place. And then you'd be crazy to not get it to do a sanity check, and essentially a peer review, like you know, that's why the system of peer review works, like, it should probably be standard to like have AI peer review on the same way that a lot of companies at standard to have AI code review in addition to the humans because the AI often is better than the humans misses stuff that the humans won't because the humans are have limited attention spans and are, you know, don't have infinite time.

**Chris** (00:40:28): I mean, there's a cool paper here where someone could go to our archive, download the top 1000 papers in a given domain and just audit them, right? Like I guarantee that will be interesting data.

**Tyler** (00:40:40): And find out like what the auditability rate is among different domains or even like different journals, different departments, you know, like the this, this school has a history of

**Jackson** (00:40:58): Yeah, as one of the most AI, psychotic people, I agree with you, Chris, I would totally run anything through the AI before I submit it. But like, I think maybe one kind of argument is like, maybe the Navi or Stokes thing or like, you're skeptical that they'll use your, your findings. Obviously, probably most PhD students aren't finding out things that are super useful. But like that could be an argument against it. Anyways, instead, you should use Kibbe, whatever, or Quinn 3.8 and send your research to CCP. But we transitioned once again, to maybe the most exciting crypto topic of the past week or the most terrifying, anthropic published something, a blog post maybe, saying that they have disproved threestat or the assumption behind threestat that it takes exponential time to solve this problem called threestat that I don't know what it is. Chris, what does this mean, do you have volunteered to explain what is threestat and what is P equals NP? So I did volunteer.

**Chris** (00:42:17): Yeah, I did volunteer. That might be a mistake. Let's see how it goes. Sorry, the hypothesis that has been disproven is a conjecture called the exponential time hypothesis. And basically, what it says is that the lower bound of threestat is solvable in only linear exponential time. So linear exponential time is the exponent is the number of terms, the n plus some constant. So if you think about an exponential curve, it starts and then it very quickly hockey sticks. We should put a series of graphs up on complexity notation and what they look like. Exponential time is the worst one by far. So basically, what that means in computer science is it takes an exponential amount of time, more time to solve the problem as the number of terms goes up in the problem. So those are like generally extremely intractable problems, right, which which some would call NP hard, which is a set of problems that are at least as hard as NP. We can go into what that means later if we if we still care. But anyway, threestat is is one of these problems. So it's actually and what is threestat? It's it's a Boolean satisfiability problem. So basically, the three means that in a Boolean satisfiability problem is a problem with a lot of Booleans, think of them as like variables or terms, right? So each of them. So you have like P or Q or R or maybe P or Q or not R as these like abstract variables. And you have to make all of these variables line up so that the whole thing is true. And the threestat format just means that every one of these clauses has three variables in them. And there's ends between them. And you can chain these infinitely to describe or to basically be reducible, reduce other problems to this threestat. So that's why it's important. So for example, there's this famous problem in computer science called the traveling salesman problem really hard to solve. It can be reduced to some form of threestat, which means that if you can solve threestat really fast, you can kind of like transpose other problems into the threestat and then solve that fast. And then all of a sudden, you're like solving all of these really difficult problems quickly. So the upshot of this paper is that we used to think that this threestat problem was only solvable in linear exponential time, which again, very difficult. And actually, this threestat problem might be solvable in sub exponential time. What does that mean? I think that the technical time that it is solvable in is like to the whatever the k term and then over the square root of log of n. Sorry. It's a whiteboard. So but that's for anyone listening like that is barely less than exponential. And it's solvable in barely less than exponential time. But that does mean that the ETH conjecture is false because it was linear exponential. I think this actual result is it's not a nothing burger, but I don't think it changes anything specifically today with this like ETH, like I think it probably changes a lot of theoretical algorithmic results where people assumed that the best possible solution for some of these things was this one. And now it's like actually slightly faster. But basically, if any paper leaned on this being the true lower bound, like that's wrong. So that their claim is weak, and it has to be rethought about. And it kind of opens the door to like what other conjectures are we leaning on that could be false, right? Like I'm not false in a little way, like this one's like a little bit false. As far as we know, we don't know actually whether there is another faster solution. But if we take that this solution is correctly the lower bound, then it's a nothing burger. But yeah, just like it opens the door to more of these load bearing conjectures being that we assumed were one way or actually the other way, and it could break a lot of stuff. That's my three set rundown.

**Jackson** (00:46:46): Nice. Well done.

**Tyler** (00:46:49): Yeah, I didn't really understand this before you explained it, but now I feel like I understand it a little bit better. It does seem like the kind of thing like if you had to say before this results happened, is it safe to say that like most people thought that this conjecture was like true and thought that like fairly confidently?

**Chris** (00:47:14): Yeah.

**Tyler** (00:47:15): So even even just proving disproving it in this way, that's like a very incremental improvement over the exponential time. It like took people from being very, very confident to okay, now it's false. And then the next step is like, can we do better than this very incremental improvement?

**Chris** (00:47:35): Right. And I think this is where people are kind of freaking out. They're like, does this mean P equals NP? So P equals NP means is the set of problems that are solvable in polynomial time, which is fast. Is that equal to the set of NP problems, which are verifiable in polynomial time? And that's like a, that's a load bearing assumption in computer science. Like that's a load bearing assumption in all public key cryptography, for example, I don't think that this really shifts that either way. But I can see how people are like, okay, well, you know, this particular conjecture on this very important NP complete problem was false, so like how false is it, right? Like we, is it solvable in like quasi polynomial time? Like where's, like, where is the lower bound now? Everyone's freaking out. Yeah. Yeah.

**Tyler** (00:48:25): I mean, it's just like whatever your priors were, they need to be adjusted for like all things that you were confident about in these, you know, extreme frontier math, computer science, physics, domains, because it seems like a lot of these, I wouldn't say intuitions, but a lot of like the things that we thought were true or things that we didn't know are falling quite quickly, one by one, and you have to assume that it will just keep going.

**Chris** (00:49:02): For sure. One thing that I like about some of these is like some of these proofs I'm told are like hideously ugly, um, the AI proofs, which I don't know is like, uh, I don't know if that's actually like, um, on the way that AI solves or like that's an emergent property of like, actually like that having like read a bunch of AI writing.

**Tyler** (00:49:24): And AI code, are you surprised that an AI proof is extremely ugly and like mostly slop, but there's like enough grain of truth there that it actually like compiles and lean.

**Chris** (00:49:37): Yeah. I mean, I'm not complaining, uh, the job got done. Um, yeah. I think like, and this could be wrong, but I think like, you know, mathematicians in particular really love elegant proofs and elegant ways to solve things. And maybe they've left some things on the table, not just like rolling up their sleeves and doing, doing something very hideous, but I could be wrong there.

**Tyler** (00:50:02): Yeah. Just like brute forcing the ugliest thing possible versus, yeah, there's this idea that like mathematics is beautiful that, you know, um, physics is beautiful that these ideas and these formulas are super elegant and like there's some underlying beautiful structure to the universe that we'll just keep on discovering. But then the alternative to that, it's like this where it's like, Oh no, actually those were just the things that we could discover because our brains are like hardwired to kind of tune into those frequencies and to like resonate with those beautiful things, but to like ignore or see through the things that are less.

**Chris** (00:50:52): So I'm calling it the ugly, ugly simulation hypothesis, which is that if the simulation is true, it's vibe coded and it's total fucking spaghetti. And that's why we're finding this stuff.

**Jackson** (00:51:03): Yeah. I feel like if I had how many mathematicians were like 30 pages into a proof and they're like, this is looking nasty and then they just, if they're an AI, they would have held like God all the way and I'm like, all right, I've solved it as it happened. Also our Bitcoin, we've lost another $40, $40 down the boys were not doing good on these couch or not couch, these like Bitcoin flip coin flips.

**Chris** (00:51:38): I feel like the cup might be, that's not correct.

**Tyler** (00:51:42): It hurt us talking shit about the, uh, the ugly proofs, um, yeah. And then like the corollary to this as it pertains to like Bitcoin and cryptography is that there's kind of like a direct metaphor or maybe it's even more of a connection than a metaphor to the P equals NP problem where there's like this assumption about, um, the hardness of a certain class of problem and it's like the time complexity that can be done in. And if that assumption breaks, then cryptography is basically broken, um, which would be very bad for all of the load bearing systems of the internet and for cryptocurrencies.

**Chris** (00:52:42): So I'm not a mathematician, but my understanding is that if P equals MP, it also unlocks a lot of good things, right? It's not just that cryptography breaks. It's like every optimization problem is solved, right? Like sort of traveling salesman, uh, colored graph, uh, all scheduling problems become trivial, trivially automatable, like, oh great.

**Tyler** (00:53:04): So I can like get sent around the country selling people things and scheduled really

**Chris** (00:53:11): efficiently. So I could work harder, but they're going to take all of my Bitcoin because you're not

**Tyler** (00:53:16): like painting me a utopian picture.

**Chris** (00:53:19): Um, but I mean, this come comes into the work harder and you will be happy and you will

**Jackson** (00:53:25): know nothing. Yeah.

**Chris** (00:53:27): Yeah. You'll have like super efficient chips and like you'll, yeah, you'll, every minute of your day will be accounted for. Yeah. The perfect corporate utopia.

**Tyler** (00:53:35): Jeez.

**Jackson** (00:53:36): Don't say don't say that that's a bad phrase, but no, I think this like, I mean, it has like

**Chris** (00:53:46): wide reaching implications for things like protein folding, right? Which is like how we find peptides or these new classes of drugs and cancer, cancer research.

**Tyler** (00:53:56): Um, like, I think, just find peptides on Alibaba, dude, like, what are you talking about?

**Jackson** (00:54:01): Find them.

**Tyler** (00:54:02): Just go to Alibaba and search like Wolverine stack.

**Jackson** (00:54:05): Yeah.

**Chris** (00:54:06): Every time I talk to Quinn, it like puts an order in for me, uh, even though I tell it

**Tyler** (00:54:10): not to straight to Alibaba, every time you go to your gym, uh, don't they have like peptides

**Chris** (00:54:15): out front that they're selling?

**Jackson** (00:54:17): They do.

**Chris** (00:54:18): They do have like sample platters of like peptides nearby gym.

**Jackson** (00:54:22): Uh, haven't done it yet, but you're saying, don't worry, we're all going to be just focus on the positives. We'll live forever. We'll be gigajacked and we'll have no free will.

**Tyler** (00:54:34): And I think he was trying to white pill a little bit where it was like, Oh, this isn't all bad if like this, you know, if, if he equals NP, but you didn't convince me too much. No, the good things sounded kind of bad.

**Chris** (00:54:47): I'm like, what if chicken little was actually really excited about this guy falling. That's, that's me. Uh, this guy's falling, but that's cool. Uh, yeah.

**Jackson** (00:54:56): We'll just be, yeah, 500 years old biceps, the size of a globe, uh, at least we'll be sexy. One of our allies are totally empty and meaningless. Well, thank you everybody for tuning into the podcast. We lost a lot of money by Nance coin. I don't know why you're going up when Binance just got hacked, but screw you, Bitcoin. I don't know why you're going down. It's because cryptography is dead, but now Bitcoin is going up and we bet down. Yeah. Oh, we bet down. Yeah. Yeah. Drunken Miller.

**Chris** (00:55:35): Did you guys see that?

**Jackson** (00:55:37): No. No.

**Chris** (00:55:39): Stanley Drunken Miller was like, he posted hyper liquid on Twitter and now hyper liquid is doing a deal with the NYSE or something trade dot X, Y, Z. Everyone's freaking out anyway.

**Jackson** (00:55:53): Hyper liquid's really going to power the future of finance. Tyler cannot believe it. We'll talk about it next episode. It's time.

**Tyler** (00:56:01): If you just counter grade all of my takes, you will do extremely well in life. So I think that's why people tune in for the like negative alpha, negative alpha is also alpha. You just need to realize, you know, like the inverse Kramer.

**Jackson** (00:56:18): Yeah. Decrypt. Decrypt. Tyler's words.

**Chris** (00:56:22): Thank you.

**Jackson** (00:56:23): Everybody. And have a good Halloween. Go spooky style.

