# Transcript (person-attributed, final cut)

**Jackson** (00:00:00): This is the marquee, Claude broke a post quantum cipher is Bitcoin next Tyler is the

**Chris** (00:00:10): Bitcoin topics is it over like, you know, maybe there is a vulnerability here that maybe even a human auditor wouldn't miss, but I can't find it because fable thinks I'm trying to steal $15 billion, which I'm not.

**Jackson** (00:00:27): Yeah, I mean, you've totally flipped me now, Tyler. Now I'm like scared that that if the models were open that people would kill me. So now I want them to be restricted, I guess.

**Chris** (00:00:41): Right. This is what I'm talking about. Give me give me the CRISPR agent. Like I'm built different. I'll work it out. I'll figure it out. Just give me that.

**Tyler** (00:00:51): No, I can totally see a world where you like let an agent shop for you say like go find me.

**Jackson** (00:00:58): But I'm glad we finally talked about it into payments. It looks like we're going to end this pod up two bucks. That's 2% on the hundo. So I think we're building quite the nest egg for our retirement boys. Yo, what's up, everybody? We got our boys back. It's Jackson. But who else is it?

**Tyler** (00:01:32): Tyler right here, as always, well, except for last week, and also Chris always except for

**Chris** (00:01:37): last week. The boys are back. You know, I'm not gonna lie last week when I was doing it alone, which

**Jackson** (00:01:40): was super awkward. I was like, what if they never come back?

**Tyler** (00:01:49): So your dedication, Jackson, you just kept the torch alive.

**Chris** (00:01:55): Yeah, huge, huge shout out to Jackson. I don't know if I could carry a podcast. And I

**Jackson** (00:01:58): think this is the perfect time to transition to the death of Bitcoin and the death of security of Bitcoin.

**Tyler** (00:02:08): Yeah, I'm not a cryptographer. I'm an amateur Bitcoin appreciator. But my understanding of this was that it broke a quantum safe cryptographic system that is not really used anywhere. So there's like a bunch of my understanding is like quantum safe cryptography is a much newer branch, newer field. And a lot of the algorithms and stuff there just has like less time in the field, less battle testing than the stuff that's like tried and true. That is quantum vulnerable, like that, like Bitcoin's cryptography is some parts of it are quantum vulnerable, which means that a quantum computer using Shor's algorithm could in theory, factor it if it is a big enough quantum computer with enough capacity, really far away from that threshold. But some people are worried that that's accelerating. But like one of the things that you would do if you were worried about quantum computers coming soon is migrate Bitcoin's cryptography to a quantum safe cryptography system. And there's like a bunch of ones that are quantum safe that are candidates that you could choose, but they're like newer, they've had like less scrutiny. I think they kind of rely on like the academic cryptography community, like people looking at them and trying to break them. Like, I don't know how many people in the world have the capability or expertise to like look at these algorithms and actually scrutinize them and they probably all work for like the NSA and like don't don't do this out of the goodness of their heart and report it back. It's theorized that a lot of these, not a lot of them, but like there could be potential like classical computing vulnerabilities in these quantum safe crypto algorithms and anthropic, I guess, as part of some of the stuff they're doing to prove how rad mythos is are like having mythos just look at these quantum safe crypto algorithms and see if it can find vulnerabilities. It found a vulnerability in one of them. And it seems like people are very impressed, like it was an impressive vulnerability it found it used some like creativity, the model worked for like hours and hours and hours. And it was kind of funny the, I think the anthropic like posted in their blog like here are the prompts that we use to do this. And then it was literally just like bro being like, continue, look for it, look for a vulnerability, and it like had to prompt it like three times and then it like popped out this thing that would break the cryptography. So it is very scary. And this makes me super worried because like, I'm sure that they had applied this, you know, have mythos look at the cryptography that are underlying all these important systems is like probably the first order thing they did, and that I would assume that it didn't find vulnerabilities because they've like responsibly disclosed them and they're being patched and they're going to be doing that. And hopefully, it turns over without issue. But it certainly puts into the realm of possibility that a smarter model or a different model, or trying the same model again could find a vulnerability in some of the cryptography that underlies Bitcoin or really ending cryptographic system. Like there's huge vulnerabilities and like core cryptography that runs the internet, like a lot of things have problems. It isn't only Bitcoin that has this problem, although Bitcoin is like a very prominent example of it. So I'll get off of my soapbox. I think I ate up all the air in the room on that one.

**Jackson** (00:05:53): I'm sort of saying that a lot of these quantum safe cryptography algorithms were like theorized by like, what do they call those people, the academics basically, and they're not well battle tested. Maybe this is like a way for anthropic deflects their model, but it actually doesn't imply that because mythos can crack this cryptography algorithm that is quantum safe that they can crack non quantum safe and potentially other quantum safe algorithms, which is like what you think when you read the article.

**Tyler** (00:06:31): Yeah, people probably think like quantum safe, that must be the highest level of safety. And if it can, if it can beat that, then all the stuff that's kind of like below it is vulnerable, but that isn't the case. It's like quantum safe just means it's safe against Shor's algorithm, but there can be a classical vulnerability in it, whereas like classic elliptic curve cryptography is vulnerable to quantum computers. But like, nobody's found a classic vulnerability to it. And my, my kind of point was that like, I don't know, what are there like 10 people in the world who can like, find vulnerabilities and like these quantum, you know, cryptography algorithms that are like really good at it. And you have like mythos is really good at it. And maybe like GPT, whatever is really good at it. And previously, those 10 people's time was like, they couldn't look at every single algorithm that ever existed and spend an exhaustive amount of time on it. And then they can do like a new mythos and have it spend like 20 hours thinking about these and it's very cheap to do that. So I think, you know, in theory, this should just make everything better if you have like a good actor that is scrutinizing this with like very intelligent systems and then, you know, responsibly disclosing and that kind of stuff. Like, I think that's a better world than having a bunch of vulnerabilities in the wild, even if people are like not sophisticated enough to find them.

**Chris** (00:07:57): If the defenders can get past the model guardrails, then yes, we have a better world. But if they cannot, then, I mean, question mark. And I look, I have something to say about that, but I won't.

**Tyler** (00:08:09): And if there's another segment, I will. But I think you should, I mean, you, you, you've just let me, you know, bother on. So I think we want to hear some Chris takes here.

**Chris** (00:08:20): Yeah, I totally agree with you. But I mean, so one thing that I found interesting about the incident that Jackson spoke about on the last pod, which was the GPT model escaping its container and hacking Hugging Face. So Hugging Face published the post-mortem and in it, I saw that they obviously there's an agent in their system wreaking havoc. So they need an agent to defend themselves. And I think that's how this is going to look for the foreseeable. And they tried to get Opus 4.8 to basically go through their systems and work out what was going on. So they had to use Guardrail every single time. So they had to use GLM 5.2, which is an open source model from I believe it is it ZAI or Moonshot? I think it's ZAI. First. So I mean, like we were in this uncomfortable position where the defenders, unless they have like a really good relationship with the labs or they have like a special access program, are kind of defenseless. Like they're grasping at whatever tools they can get to kind of defend themselves against these adversarial threats. And I think, you know, that probably only gets worse unless we work out what we're doing with the guardrails. And I've personally had similar problems, like I write smart contracts and it is impossible to get an audit for your smart contract using the frontier models or very, very, very difficult. And it just puts you in this awkward position of being like, okay, like, you know, maybe there is a vulnerability here that maybe even a human auditor would miss, but I can't find it because Fable thinks I'm trying to steal $15 billion, which I'm not.

**Jackson** (00:10:10): Yeah. Are we all like super like libertarian on the guardrails? Do we all feel like there shouldn't be no guardrails or is that just me in my opinion alone?

**Chris** (00:10:23): Is that your feeling, Jackson?

**Jackson** (00:10:25): Yeah. I mean, why should Anthropic and the government have access to a tool that is way more powerful than like any tool I'm allowed to have? That feels unfair. I guess you could say.

**Tyler** (00:10:42): Yeah, I guess that's true. What if I can train my F-16 on an existing F-16, then is that

**Chris** (00:10:57): okay? Like by having an F-16? I mean, that's the question. Like, what's the morality of that?

**Jackson** (00:11:06): I accept your metaphor, and I guess it is similar to like the government wielding power over you through like the weapons that it has that you don't have. It's also scooping up the power of these intelligence models and wielding it against us as well. I don't know. I guess it's just a different form of weapon that now that they have over us.

**Tyler** (00:11:32): I mean, I think it's a pretty... I don't think that there's like a clear answer from my perspective because I'm definitely more aligned on like less restrictions, more freedoms. People should have access openly to the frontier stuff. Like, that's great. But then I think that if you hear some of the anthropic arguments, they're really worried about like bioterrorism. And my understanding is that if you have a fable or mythos class model with no restrictions, the model is intelligent enough to tell you how to create a pathogen at home that could create a pandemic or something. So all it takes is like one sicko, terrible person out in the world with access to this to like cause really, really terrible outcomes for the whole globe. And so there is a symmetry there between attacking and defending. And yeah, what's the right move there? I think it feels right to not deliver that capability to anyone in the world unrestricted. But then like, so that means, okay, I have a line somewhere and maybe my line, you know, bioterrorism is on one side of my line. But like, where does that line actually sit? Does it sit with like cryptography or cyber or like, you know, do I think those things should be blocked or included? And certainly the classifiers that were on fable originally were like extremely comical and the like, you know, level of false positives that they would have where it would refuse to do like basic stuff like it refused to tell me about my dog's medicine because it was like a biology question. And I'm like, I just want to know like what the right medicine is for when he got poisoned by mushrooms.

**Chris** (00:13:31): I think one thing I wonder about is like what is like at this point, like what is the time until there is an open source fable or mythos level model, right? And then like it, you know, if you take that concession, like then maybe that changes what the best thing you can do is, right? Like six months away from having like a GLM or Kimmy that is, you know, mythos in all but name, like, how does that change? Oh, you know, what is the right thing to do? Like, should we?

**Tyler** (00:14:02): I think the actual like the 3D chess that's happening here is that to some extent, the like the fact that fable won't do like cybersecurity thinking for you, Chris, it's like, okay, maybe they don't want you to have that, but they really don't want the Chinese to do that. They want the Chinese labs to have that output and then distill from it. So I think part of the 3D chess is that they want to make their models basically either dumb or return kind of like empty, you know, refusals for these tasks. And then they're like, okay, as long as somebody's distilling us, maybe their model will be really good at generalist coding, that's fine. But we're not going to let them distill like the cyber capabilities, the bioterrorism capabilities. It's like, you know, this is an open model that is as smart at coding as fable, it's going to have these like potentially big gaps because it didn't get, you know, that and it's training data. And like potentially, you know, there's enough generalization from having a model or an agent that's super, super good at coding that like it just becomes really good at cyber. They're having these classifiers, it's like to prevent you from misusing it, but also to prevent that capability from leaking through distillation reasoning traces into these open models.

**Jackson** (00:15:23): Yeah, I mean, you've totally flipped me now, Tyler. Now I'm like scared that if the models were open, that people would kill me. So now I want them to be restricted, I guess.

**Tyler** (00:15:36): I mean, you know, like the internet beam, it's like, how do you want to control this technology? Do you want to use terrorism or like child abuse, you know, and like I feel like a little bit like pulling back that lever by being like bioterrorism. So yeah, I feel like that's usually the things that people go to to justify this type of additional control. I don't know, it's a difficult question.

**Jackson** (00:16:07): Now that Chris says that there's going to be mythos level open source model in six months, does that mean we're all going to die? Not from the robots, but because of human generated pathogens from a nefarious edgy 14 year old living in Colorado?

**Tyler** (00:16:26): I hope not. I mean, that's when, yeah, I don't know what the, what the, how you protect against that. If that type of capability is diffused and it only takes like one motivated bad actor, then yeah.

**Jackson** (00:16:44): Does that mean we all need to like have our own agents developing anti pathogens monitoring what pathogens are being developed and give me the CRISPR agent, like I'm

**Chris** (00:16:56): built different. I'll work it out. I'll figure it out. Just give me that.

**Jackson** (00:17:03): Yeah. Wow. Well yeah. Thanks again for the insight on the guardrails. I was like, these guardrails are stupid. I just hate being told what to do, but I think you're right. There probably needs to be some, some guardrails.

**Tyler** (00:17:18): And I'm not like super pro guardrail. I'm just kind of like steel manning the case a little bit here and why I think it makes sense. Like they don't want their model distilled. So they make it. They don't provide that capability. And then they're obviously worried about it being used for bad actions, but you don't know where I come down on this, but I'm not like a hundred percent like free unrestricted model person, I think because of that, but I'm also probably less restrictive than a lot of the policies that you see right now.

**Chris** (00:17:53): I just want to say to any anthropic or open AI listeners that I can be trusted with Glasswing or GPT-6. I really, really need it. So like, you know, shouts out to you guys. If you, if you want to hook me up, you know, I'd be, I'd be very happy only for auditing purposes. Just to be clear.

**Jackson** (00:18:13): Open AI, you better give me early access to GPT-6 because otherwise I'm not taking back all the shit I've talked about 5.6 and open AI in general. The thread is out by myself. I

**Chris** (00:18:28): think I can like barely carry a third of it. So just massive props for, yeah, for keeping it going.

**Jackson** (00:18:36): We're all a critical piece of this three legged stool that we call the podcast. Speaking of stools, Chris, what's going on with the gamer thumb and how was your week away from the pod?

**Chris** (00:18:48): Yeah, I mean, so my week away from the pod was good. I was in Australia. It was very cold. But what it did give me is a chance to recover. So like, I didn't do a lot of typing whilst I was there. And, and yeah, I still have gamer thumb. So I don't want to call you on. Yeah.

**Tyler** (00:19:12): When you were there. Absolutely not. No gaming. Okay, full rest for the thumb. Yeah. Full use your phone. Were you like phone typing?

**Chris** (00:19:21): Yeah, a little bit. I did deliver the phone. That could be it. Were you wearing your brace the whole time? No, I didn't wear the brace at all. So like, I obviously have a compliance issue with that thing. What I did hold. So a lot of my friends have children. I did hold a lot of babies and they told me that babies create game a thumb like because you're like shaking them around and stuff. Also, I don't know how babies work.

**Tyler** (00:19:47): You're not supposed to shake a baby. That's like the thing they have on PSAs for, you know, public health. But yeah, you do get like hand and wrist pain from holding babies all the time because they're heavy and they like wiggle and you kind of awkwardly hold them.

**Jackson** (00:20:04): Dr. Tyler is back explaining baby thumb. Yeah. Well, when I got wrist surgery to put a

**Tyler** (00:20:12): screw in my wrist for a broken bone a week before Margot was born, but it was like on her due date. And so I went into the surgery and I told the surgeon like, if I get a text from my wife that she's going to labor, I'm like calling the surgery off like I don't want it to happen while I'm under. And they put me under and then I woke up and my wife picked me up. But then like I had a wrist brace on, I think for the first two to three months of Margot's life, which made it really difficult to like hold her and like change diapers and all this stuff. So not the most ideal thing. So Chris, if I can do that for two to three months, your compliance on the gamer thumb brace. I don't know, man. I don't know. I think you need to do it for the good of your health.

**Chris** (00:20:58): And I'm not here to be called out. All right. I'm here for like acceptance. You know, like I accept your non compliance and inability to fix this very small problem.

**Jackson** (00:21:08): What about Tyler? I mean, Tyler, you had problems with that risk for like weeks without even knowing what it was. Right. And you kept grinding two handed back hands on the tennis board.

**Tyler** (00:21:20): Yeah. I think I did. I play you, Jackson, while I had a broken wrist. I think so. Yeah. Okay. So I broke my wrist playing tennis and I thought it was just sprained. And then I kept like playing tennis for like two weeks after with a broken wrist. And it was kept being painful. And then eventually I went to the doctor and got an x-ray and they revealed that. But yeah, I guess that puts my, you know, I'm throwing stones at Chris from my glass house over here.

**Jackson** (00:21:53): Yeah. Or just putting you back, you know. Yeah. Thank you for the backup, Jackson. I

**Chris** (00:21:57): appreciate that. I was feeling cold cloud a little bit, but we're better now.

**Jackson** (00:22:02): Tyler, how was your vacation? How much do you want to do? Did you go anywhere sick?

**Tyler** (00:22:08): We went to New York and the East Coast where I grew up. It was super nice. Lovely summer weather there. Did some swimming with the baby. Saw some old friends, family. Yeah, it was lovely. We have a lot of work with childcare because I got used to daycare a little bit too much, that cushy life. And then now we're back in 24/7 childcare mode. And it's just pretty comprehensive. And then actually last night, there's this thing with babies where you're supposed to introduce them to allergens to test if they're allergic to foods. So you give them little amounts of stuff and then you see what happens. So we had to leave my daughter egg. And two hours later, she threw up like seven times all over both me and my wife. It was just like, I don't understand how she had that much volume in her stomach. And then she got pretty sick and we ended up taking her to the children's hospital just out of an abundance of caution. But it was pretty sad to see. And I spent the whole evening covered in puke. I just drove there without changing or anything. So I just smelled like baby puke for five hours. And then they eventually gave her some good medicine. And we got home and cleaned up and went to bed. But yeah, a little bit of a harrowing night, but everyone is okay. But it sucks because you can't eat egg now. And eggs are

**Jackson** (00:23:34): delicious. That's true. Does baby puke smell better than human? Like American, pardon me, adult puke?

**Tyler** (00:23:45): I don't think either are particularly great. But yeah, it does have that stomach acid kind of bile-like smell that normal puke does. But she's all right. We just grossed out all of our listeners. So we just dropped off half of them. And the only people remaining are the people that love the puke talk.

**Jackson** (00:24:08): Cool. Well, maybe we can do a quick Tyler, one minute, BIP 110. Is it nothing? Why do I hear about it?

**Tyler** (00:24:22): I feel like I'm woefully unprepared for this, because I think it's just so stupid that I've referred, I've refused to pay attention to it. And so yeah, it's just like the discourse I feel like is so just dumb. And I'm just tired of it. And I just don't want to pay attention. And I'm not going to do anything about it. And it will probably blow over in a few months. I can try to give you my understanding of it from a very high level, which is that there have been people for a while that are very upset that they believe that there's spam, Bitcoin is being used for spam, which they define as these essentially like NFT kind of projects, like ordinals and inscriptions. They want to have the ability to block this spam, block the use of arbitrary data on the blockchain. And so they are like, okay, people are doing spam in this one specific way right now, we'll block that. And then there's this fork for people that will block that. But it's very stupid because it's like, as soon as you block that one way, the people who want that activity to continue are just going to tweak the way it shows up a little bit, like people have already done this and shown that like, there's BIP 110, they have these filters. And they're like, okay, people are doing spam, block the use of ordinals and inscriptions, or like, we'll just do it this different way. And now it's BIP 110 compliant, you'll have to fork a second time. And it's like this infinite game of cat and mouse, you just cannot stop people from putting arbitrary data into Bitcoin transactions, because you can make arbitrary data really hard to detect. And like, you can even some of the ways that you would force people to do arbitrary data are like much less healthy for Bitcoin, it might bloat the U2XO state, it might mean that nodes have to like validate a bunch of junk data. That doesn't actually have any meaning. And so it's being done right now in kind of like a least harm way. And you could potentially force people to do it in more harmful ways, which is bad. So like, I just think it's a very misguided thing. Most people I know, who I respect think it's extremely misguided. And the people who are behind it seem like either misinformed or just like really, like, they're not arguing in good faith, I don't really know what their motivations are, but it doesn't seem like in good faith to me, because it seems so obvious. And yeah, Bitcoin, I think will fork at some point, I think it's like in a couple weeks. So there's the BIP110 fork, and then there's also this eCash fork that's going to happen. So we're going to get two potential forks of Bitcoin this year, which hasn't happened for a while. I think both of them will die quickly.

**Jackson** (00:27:17): That's crazy. Bitcoin Cash too. Yeah, we need another one. So you're saying that the people that oppose BIP110, it's not that they disagree that Bitcoin shouldn't have spam, it's that the solution to prevent the spam is really narrow. And yeah, I mean, that's basically it. Is that what you're saying, Tyler?

**Tyler** (00:27:44): Yeah, at the root of it, you can really not prevent people from putting arbitrary data into Bitcoin transactions. And like the solution is like worse than the problem. And it's also like a temporary thing, honestly, like people can afford to do this right now, because transaction fees are very low, because like nobody is using Bitcoin. If Bitcoin exists, and people don't use Bitcoin and don't make Bitcoin transactions on the blockchain, because they're holding Bitcoin and ETFs, or Bitcoin is not becoming like a money, then Bitcoin is probably not very successful, and it doesn't really matter. If it's successful, then I expect transaction fees will increase and price out this activity, and it will just go away naturally. And so I feel like this world that they're trying to solve for where Bitcoin is successful and relevant, but spam is still economically viable on the main chain, it just is like a stupid temporary thing that we shouldn't overreact to, even if we had ways to stop it, and we don't have ways to stop it. So it's all so tiring.

**Jackson** (00:28:56): Kind of a spontaneous topic switch. So like, when the fork happens, all of us that have Bitcoin, I guess Bitcoin that's self custody, it's like duplicated, right? One is on the new chain and one is on the old chain. Is it lucrative for people that do forks? Like, do they make any money? I can sell my Bitcoin e-cash to some Bitcoin e-cash to bag holders, because I don't want to keep it? Or does the value go to zero so quick that I can't make money or no one makes any money?

**Tyler** (00:29:41): Yeah, so it's true. If you hold your own keys and you have actual Bitcoin UTXOs, you will have a UTXO on the fork. If you hold your Bitcoin custodially or in an ETF, then whoever owns the keys backing that Bitcoin will have a corresponding amount of Bitcoin on those chains, but they may or may not honor that and give you exposure to these forks. Honestly, it's probably not even going to be worth it for them. I expect the forks will be not valuable enough to warrant building ways to handle them. And if you support every little fork of Bitcoin that comes out in that way, then you're kind of committing infinitely to support all these. Zip 110 is just a publicity stunt. I really don't expect it to be relevant much at all, but it is taking up a lot of the discourse on Bitcoin X, which is really sad to see because it's such a stupid discourse. And I think it's poisoning the vibes and poisoning anyone who comes into Bitcoin at this moment. Bitcoin is the dumbest debate that's ever happened. Why would I want to be part of this community? It's just sad.

**Jackson** (00:31:00): I feel like for the dip in the forks, you're saying that the miner can choose to go to a different pool if they don't agree with the miner's decision on which fork to take. Is it that easy? Is it really easy to switch pools for the miner?

**Tyler** (00:31:19): Absolutely. It's like you have your ASIC and your ASIC has a configuration that's like, what is the IP address of your pool to fetch blocks from? And you just change that. I have a little mini BitX miner in my house. It has no chance of ever finding a block, but I can go on there right now and update the pool in 30 seconds.

**Jackson** (00:31:40): But are you mining for yourself? Are you mining for a pool? Are you playing the lottery with your BitX?

**Tyler** (00:31:48): Yeah, it is a pool, but it's like a pool where I get like 99% of the block that I find, I think. So the pool is really just you're paying them a small amount of a reward that you would find in order to construct the blocks because your miner can't do block construction. It doesn't run a full node. It needs to be told what block to hash on.

**Jackson** (00:32:07): Dude, we should just say, screw the perp of fortune. Let's just look at your BitX for an hour during the pot.

**Tyler** (00:32:15): That would be a pretty boring episode.

**Chris** (00:32:19): We just will read every hash, every single hash. We'll see that like, oh, only three zeros

**Jackson** (00:32:23): on that one and we'll just manually look.

**Tyler** (00:32:27): That'd be skintillating TV. Speaking of fortune, I feel like we've had one running. Should we introduce it or do we have more fork talk?

**Chris** (00:32:41): Well, speaking of forking things, so I followed your prompts, Tyler, where you said that perp of fortune should be relative to the podcast. We haven't done this segment yet, but for context, I fed GPT 5.6 Sol the podcast transcript and I said, hey, help us pick a perp that is hopefully going up that's relevant to the transcript. And it said long native XRP perp at 20X isolated leverage. That is what it chose. And I'll try to summarize some of its reasoning here. It says at the final snapshot XRP was up 1.5% over 24 hours and it had 28.2 million daily volume and also XRLP RPL don't know what that is, officially supports X402 payments using XRP or RLUSD. And that's it. That was its whole reasoning.

**Jackson** (00:33:49): Just God, these GPT models are so bad.

**Chris** (00:33:55): I mean, he's a great programmer, but as I alluded to on the last podcast, he's like, you know, it may be like the weird guy at the party sometimes. Let me share this. Let me share this.

**Tyler** (00:34:08): This really makes me lose faith.

**Chris** (00:34:15): It's, you know, I think it's just a case of like staying in your lane, like, and maybe like the lane is not choosing perps for 5.0.

**Jackson** (00:34:27): Dude, what are you talking about? Its reasoning was shite, but we're up.

**Chris** (00:34:32): We've been under this whole podcast. Look at this line. There's a recent occurrence. We were here before. Viewers will never know. If we close green, I'm very happy. $2,000 notional. So let's see where we get to.

**Tyler** (00:34:47): Have you ever been a ripple guy? Either of you? I feel like ripple guy is like a very distinct phase that some people go through in the crypto worlds. But I don't know people who actually are afflicted by that mental illness.

**Chris** (00:35:03): What do you think, Tyler? Be very careful what you say here.

**Tyler** (00:35:10): I think Jackson probably has like dabbled in a little bit of ripple. I think Chris, I would say no. No hate on you, Jackson, but I feel like you're just like a little bit more exploratory and kind of like try anything. And then, yeah, maybe Chris and I are like cynical, like hermits hating on the world from our computer screens.

**Jackson** (00:35:36): All right, I've been called out. Yes, I have owned ripple. Yes, I've doubled my money under ripple. Nice. And literally an hour before this pod, I was talking to this Argentinian dude, and he said he loves ripple. The rest of it was in Spanish, so I can't tell you why. But the ripple signal is actually high right now. I mean, the purple fortune, the Argentinian dude, and I made some money on it.

**Tyler** (00:36:04): Yeah, maybe this is just another invocation of the bell curve meme, and I'm like a sad mid-curve person being like, ripple is so dumb. And then, you know, GPT is off there on the right hand side.

**Jackson** (00:36:19): GPT is the lefty. GPT is the lefty.

**Chris** (00:36:24): Yeah, no, I was never a ripple guy, and I think it's due to a fundamental weakness in my reasoning. I need something to be conceptually beautiful in order for me to believe in it. And I don't know, I feel like ripple didn't have that for me. I was like, we're reinventing Swift, but I mean, that's a great story, right? That's exactly it. Yeah, I think maybe I'm poor for this reason.

**Tyler** (00:36:55): But why does Swift need to be reinvented? I don't know. It don't make sense to me.

**Chris** (00:37:01): Why do you need to put two toll boots on a bridge?

**Jackson** (00:37:04): Yeah, I mean, 10 years ago, they're like, there's this new coin, and it can be used for international bank transfers, and you're like, what? I love that. And that was even before all like the regulatory push that they've been doing, right? Where I think then they got sued, it went down a lot, but then they broke out because they just gave all the ripple to the legislators, right?

**Chris** (00:37:34): I think I mean, to this point, I think like maybe we're moving into a time where the only moat left is regulation. And I've like spoken to people around here, San Francisco, that like truly believe that I don't, I don't. But I think a lot of people think like, you know, as you know, if we solve engineering, then like, the remaining moat for your business is either regulatory or regulatory

**Tyler** (00:38:03): capture. And from like a generalized thesis, or one specifically for like Bitcoin and crypto and fintech.

**Chris** (00:38:10): I think I think fintech, but I also think to a lesser extent, a more general thesis, like I've spoken to people who are like, I was going to build an AI wrapper, but then I thought, like, you know, regulation would be a better moat for my business. And so I'm doing something in fintech. I don't know if I agree with that, but it is something I've heard, right?

**Tyler** (00:38:29): Instead of hiring an engineer, I hired like a lobbyist.

**Chris** (00:38:32): Yeah, like a team of lawyers.

**Tyler** (00:38:35): I donated to the, you know, I bought a lot of World Liberty Financial and suddenly I could do whatever I wanted.

**Chris** (00:38:45): Exclusive rights to something. Yeah.

**Tyler** (00:38:47): But I do think like the marketing department of Ripple is like amazing. Like every, every cycle, whatever the trend is, they're like hop on up. We want red.

**Jackson** (00:38:58): No.

**Chris** (00:39:00): Ripple Bros. It's over.

**Tyler** (00:39:02): But it's like, yeah, like I think the reasoning.

**Jackson** (00:39:06): Speaking of Ripple and agentic payments, because those two are very related. Sorry, Chris, what were you going to say? Should we talk about that?

**Chris** (00:39:17): Should we, should we chat about agentic payments and X402 and MPP and ADP?

**Jackson** (00:39:24): Yeah, I think maybe we should, um, we should give the agentic payments again. We've been baiting our listeners about agentic payments for like a month. So I'll, I'll lay the stage. Agentic payments basically means that your chat GPT can like buy stuff for you from like a consumer point of view. And from a business point of view, it could mean that your business could trade with other businesses in an automated way. So I'm just trusting your AI model to do that from a bird's eye point of view. Now you two, Chris and Tyler, what do you think? Does it have legs? Is it going to happen?

**Chris** (00:40:14): Okay. I want to, I want to layer a little bit of context on top of this. There are four agentic payments protocols in the wild. So, I mean, so I think like the story here is that Coinbase and some affiliated people came up with a protocol called X402. The idea is that it repurposes the 402 HTTP code, which I think is payment required and it like allows you to, you know, do a payment. And there are some cool ideas like streaming payments and micro payments dovetailed in there, but functionally what it does is you hit this endpoint and then it returns a standardized JSON list of the payments that the vendor accepts. On top of that spec, there's some stuff like, you know, how to integrate a facilitator to facilitate and do the payments for you, which of course is Coinbase by default. And was previously based by default, although I think there are more facilitators and more chains accepted now. So I think that kicked it off. From there, I think Google has put their hat in the ring. Stripe and Tempo have one called MPP, which is going through the IETF at the moment. I think it's in the proposal draft phase. And I mean, my take here is they're all much of a muchness, right? Like I think, you know, when anything big like this happens, there's like a war to control the standard because maybe you can be on the ground floor and control some of the order flow. And basically, you know, my criticism of all of these proposals is they're almost exclusively exactly this. Like they seem free and open, but like under the hood, you know, there are some minor structural advantages to the proposal. A great example of this is that Stripe's proposal MPP is a superset of X402. So they're like trying to cannibalize the other. They're like, OK, well, this has some adoption. Like why don't we why don't we superset this and then like layer our own stuff on top and then kind of like try to redirect the flow of this river as it's as it's running.

**Tyler** (00:42:19): They're vampire attacking X402.

**Chris** (00:42:22): I didn't want to say it, but it seems like that. Yeah.

**Jackson** (00:42:26): I guess like the protocols for making the payments, you know, these companies are trying to make them and like monopolize that because it's like a way to make a lot of money. But really, we don't even need them, right? You can point Fable with like full computer control at a website and it can navigate the checkout for you. So like beyond the the mechanism that the payments go through. Do you see yourselves using like letting your agent buy stuff for you?

**Chris** (00:43:05): I already let my agent do stuff on chain. I would say my agent is the primarily primary way that I interact with stuff on chain. By the way, look at CDRN/Sigil if you want. You want to know like how to do this. It's very cool. You mean your GitHub? Yeah. Yeah. My GitHub. Look at my GitHub. Yeah.

**Tyler** (00:43:30): My agent only buys Ripple. That's the only thing it's allowed to buy.

**Jackson** (00:43:36): I think you and Chris mixed your agents up. No, I can totally see a world where you like

**Tyler** (00:43:41): let an agent shop for you. Say like go find me these sneakers. Find me the best price. I'm curious, Chris, do you think this is like a winner-take-all thing with these protocols? I feel like one thing that agents are really good at is like handling complexity. So if every company has their own flavor of this protocol, that's like subtly different. Historically, you would think, okay, maybe it's going to coalesce around one. There'll be winner-take-all because of network effects. Nobody wants to support all this. But like agents, it's just trivial for them to like hop protocol to protocol, know how to interact with it. So I don't know, like I could see some of them, multiple of them persisting and it's kind of like a mess. But the AI is so good at disentangling that mess and hopping between different support that like it doesn't necessarily converge.

**Chris** (00:44:45): Yeah, I totally agree. I think like the crispiest form of my take is that none of this matters. Like agents will pave over the complexity as they have with programming. But we're making this like needlessly worse for humans for just no reason, right? Like with standard fragmentation. Like if you go to Claude right now and you spin up CDRN/Sigil or any other key management MCP that you want and you tell it to do something, like it will work it out. Like it will pull the contracts to bridge your funds and like execute the payload. It will do, you know, it doesn't matter if it's Solana or Ethereum, you know, the agents like quite adept at figuring out how to do things. And I think, you know, this will be no different with checkout or traditional payments or whatever. Yeah, that's my hot take.

**Tyler** (00:45:34): I think that covers like the protocol level, but then there's also like the rail that this stuff travels on. So there's like, it's almost a good combinatorial explosion of like we have all these different protocols. A lot of them support multiple different rails. Yeah, my agent wants to pay using X402, using like USDC on base, but, you know, the merchant wants to receive via like MPP on like OUSD on Tempo. And then there's like, you know, Google's, I forget what it's called, they have one of these protocols too, and they just like want you to buy something with Visa. So there's just like this, you know, multidimensional explosion of possibilities. I don't know if I believe the thesis that like blockchains and crypto assets are particularly good for micropayments or for, yeah, like machine payments, or yeah, like, it doesn't seem to me like some people frame it as if it's like, so obvious that it's inevitable that crypto assets will use crypto assets. And I don't really agree with that yet. I think there are some pros for them to use that. But then I think there are some, you know, downsides. And so I think it's yet to be seen how it will play out. And like, for all the downsides of like the traditional rails, I think that those companies that control them and operate on them are like sprinting to make them more agent compatible.

**Jackson** (00:47:14): What you're talking about is copium. I think that crypto people are hoping and coping the agents will use internet native money.

**Chris** (00:47:25): I completely agree. I think it's maybe a better outcome for the commons if people settle on something that is like more open and more programmable. But like, you know, at the end of the day, I think this whole standards war is emblematic of like how this works, which is that large players compete to capture the order flow. And unless they're forced to use something incredibly neutral, they want, right?

**Jackson** (00:47:53): Absolutely. Yeah, I guess I could see letting an agent buy like things I don't care about, like the shoes, getting me cheap shoes, but I don't know like groceries.

**Tyler** (00:48:08): I feel like groceries is like the perfect use case. You know, you tell the agent like, I like, you know, Mexican food and Thai food and like steak, like plan me, you know, three to four dinners for this week. You know, the recipe, put the ingredients in my cart, buy them, have them delivered to my house and like send me an email, you know, at night with the recipe and which ingredients I'm supposed to use. Like that kind of thing, I think is something that people do for sure.

**Jackson** (00:48:46): I just don't trust it's gonna like pick a good recipe and get me all the right ingredients to actually perform the cooking. But I don't know. I also very intense about

**Tyler** (00:48:57): my eating. Yeah, I know that you are such like a culinary aficionado.

**Jackson** (00:49:04): Did you know my last name is Cook? It's very important. Whoa, did you just talk to yourself on the podcast? That's crazy. Jackson swag dog chef. You're just cooking out. So like dog is only visible in the stupid streaming software. Don't don't expose me, man.

**Tyler** (00:49:34): Yeah, I agree with that. I'm also very unsure. And I'm not like the most informed on this. So I don't want to come out with like a very, like, you know, a strong prediction. But it seems to me like a lot of the arguments I've heard about like why it will inevitably be some kind of crypto asset. They don't necessarily make sense to me, I think it is like a little bit of motivated reasoning, people want their, their coin, whether they're a company with a stable coin or protocol or they're like, you know, Bitcoin enthusiasts, people want the thing that they're attached to, to like when and they'll motivated reason around it. It will be interesting. I don't know. We'll see. I could see.

**Jackson** (00:50:10): In the end, it's the payment company that is like processing the payments on behalf of the vendor that's going to pick which protocols they support.

**Tyler** (00:50:21): It's kind of crazy that that whole thing relies basically on whatever the legislation was that like bands, stable coins from passing interest on the consumers in the US. It's like, oh, there will be this new business model because they can harvest all the interest. And it's like literally, oh, that business model only exists because the government banned them, like preventing a race to the bottom where they pass that interest back on to customers.

**Chris** (00:50:49): There's some kind of regulatory mode at play here, I think for sure.

**Tyler** (00:50:53): Yeah.

**Jackson** (00:50:56): I think we will get to cover the genius act itself next week. I think that the deadline passed, but I'm glad we finally talked about it into payments. It looks like we're going to end the spot up two bucks. That's 2% on the hundo. So I think we're building quite the nest egg for our retirement boys.

**Chris** (00:51:23): I think you owe 5.6 an apology, Jackson. You're very scathing.

**Jackson** (00:51:29): I'm never going to apologize. Yeah, I think we'll close it off there. And do you guys have any farewells to our listeners? Oh, shoot. We're almost down. Quick.

**Chris** (00:51:49): I'm going to close it right now.

**Jackson** (00:51:51): Close it.

**Tyler** (00:51:53): Sorry about all the puke talk earlier listeners.

**Jackson** (00:51:57): Yeah, we'll see what we do with that.

**Chris** (00:52:00): Claude, don't cut it out. Claude, make that the centerpiece of the podcast.

**Jackson** (00:52:07): All right. Later.

