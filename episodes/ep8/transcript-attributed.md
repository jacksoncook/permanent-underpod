# Transcript (person-attributed, final cut)

**Jackson** (00:00:00): This is the marquee, Claude broke a post-quantum cipher. It's Bitcoin next, Tyler is back on the Bitcoin topics.

**Chris** (00:00:12): Is it over like, you know, maybe there is a vulnerability here that maybe even a human auditor would miss. But I can't find it because Fable thinks I'm trying to steal $15 billion, which I'm not.

**Jackson** (00:00:27): Yeah. I mean, you've totally flipped me now, Tyler. Now I'm like scared that if the models were open that people would kill me. So now I want them to be restricted, I guess. Right. This is what I'm talking about. Give me the CRISPR agent.

**Chris** (00:00:45): Like I'm built different. I'll work it out. I'll figure it out. Just give me that.

**Tyler** (00:00:50): No, I can totally see a world where you like let an agent shop for you. Say like, go find me.

**Jackson** (00:00:57): But I'm glad we finally talked about it into payments. It looks like we're going to end this pod up two bucks. That's 2% on the hundo. So I think we're building quite the nest egg for our retirement boys. Yo, what's up, everybody? We got our boys back. It's Jackson, but who else is it?

**Tyler** (00:01:32): Tyler right here, as always, well, except for last week.

**Chris** (00:01:37): And also Chris always except for last week.

**Jackson** (00:01:40): The boys are back. You know, I'm not going to lie last week when I was doing it alone, which was super awkward. I was like, what if they never come back?

**Tyler** (00:01:49): So with your dedication, Jackson, you just kept the torch alive.

**Chris** (00:01:55): Yeah, huge, huge shout out to Jackson. I don't know if I could carry a podcast by myself. I think I can barely carry a third of it. So just massive props for keeping it going.

**Jackson** (00:02:06): This is the perfect time to transition to the death of Bitcoin and the death of security of Bitcoin.

**Tyler** (00:02:15): Yeah, I'm not a cryptographer. I'm an amateur Bitcoin appreciator. But my understanding of this was that it broke a quantum safe cryptographic system that is not really used anywhere. So there's like a bunch of my understanding is like quantum safe cryptography is a much newer branch, newer field. And a lot of the algorithms and stuff there just has like less time in the field, less battle testing than the stuff that's like tried and true that is quantum vulnerable. Like Bitcoin's cryptography is some parts of it are quantum vulnerable, which means that a quantum computer using Shor's algorithm could, in theory, factor it if it is a big enough quantum computer with enough capacity. Like really far away from that threshold, but some people are worried that that's accelerating. But like one of the things that you would do if you were worried about quantum computers coming soon is migrate Bitcoin's cryptography to a quantum safe cryptography system. And there's like a bunch of ones that are quantum safe that are candidates that you could choose, but they're like newer. They've had like less scrutiny. I think they kind of rely on like the academic cryptography community, like people looking at them and trying to break them. And like I don't know how many people in the world have the capability or expertise to like look at these algorithms and actually scrutinize them. And they probably all work for like the NSA and like don't don't do this out of the goodness of their heart and report it back. So like it's theorized that a lot of these, not a lot of them, but like there could be potential like classical computing vulnerabilities in these quantum safe crypto algorithms. And anthropic, I guess, as part of some of the stuff they're doing to prove how rad mythos is are like having mythos just look at these quantum safe crypto algorithms and see if it can find vulnerabilities. And it found a vulnerability in one of them. And it seems like people are very impressed. Like it was an impressive vulnerability. It found use some like creativity. The model worked for like hours and hours and hours. And it was kind of funny. The I think the anthropic like posted in their blog, like here are the prompts that we use to do this. And it was literally just like bro being like continue. Look for it. Look for a vulnerability. And like I had to prompt it like three times and then it like popped out this thing that would break the cryptography. So it is very scary. I wouldn't say that this makes me super worried because like I'm sure that they had applied this, you know, have mythos look at the cryptography that are underlying all these important systems is like probably the first order thing they did. And that I would assume that it didn't find vulnerabilities in those or if it did, they've like responsibly disclosed them and they're being patched and they're going to be doing that. And hopefully it turns over without issue, but it certainly puts into the realm of possibility that a smarter model or a different model or trying the same model again could find a vulnerability in some of the cryptography that underlies Bitcoin or really on a cryptographic system. But if there's huge vulnerabilities and like core cryptography that runs the internet, like a lot of things have problems. It isn't only Bitcoin that has this problem, although Bitcoin is like a very prominent example of it. So I'll get off of my soapbox. I think I ate up all the air in the room on that one.

**Jackson** (00:05:58): So you're sort of saying that a lot of these quantum safe cryptography algorithms were like theorized by like, what do they call those people, deep academics basically, and they're not well battle tested. So maybe this is like a way for anthropic deflects their model, but it actually doesn't imply that because methods can crack this cryptography algorithm that is quantum safe that they can crack non quantum safe and potentially other quantum safe algorithms, which is like what you think when you read the article.

**Tyler** (00:06:38): Yeah, people probably think like quantum safe, that must be the highest level of safety. And if it can beat that, then all the stuff that's kind of like below it is vulnerable. But that isn't the case. It's like quantum safe just means it's safe against Shor's algorithm. But there can be a classical vulnerability in it, whereas like classic elliptic curve cryptography is vulnerable to quantum computers. We know that, but nobody's found a classic vulnerability to it. And my kind of point was that like, I don't know, what are there like 10 people in the world who can find vulnerabilities in these quantum cryptography algorithms that are really good at it? And now we have like mythos is really good at it. And maybe like GPT, whatever is really good at it. And previously, those 10 people's time was like, they couldn't look at every single algorithm that ever existed and spend an exhaustive amount of time on it. Like spin up a new mythos and have it spend like 20 hours thinking about these and it's very cheap to do that. So I think, you know, in theory, this should just make everything better if you have like a good actor that is scrutinizing this with like very intelligent systems and then, you know, responsibly disclosing and that kind of stuff. Like, I think that's a better world than having a bunch of vulnerabilities in the wild, even if people are like not sophisticated enough to find them.

**Chris** (00:08:02): I mean, this is if the defenders can get past the model guardrails, then yes, we have a better world. But if they cannot, then I mean, question mark, and I look, I have something to say about that, but I won't.

**Tyler** (00:08:15): And if there's another segment, I will, but you shouldn't say, I mean, you, you, you've just let me, you know, bother on. So I think we want to hear some Chris takes here.

**Chris** (00:08:26): Yeah, I like I totally agree with you. But I mean, so one thing that I found interesting about the incident that Jackson spoke about on the last part, which was the GPT model escaping its container and hacking hugging face. So hugging face published the postmortem and in it, I saw that they obviously so obviously there's an agent in their system wreaking havoc, so they need an agent to defend themselves. And I think that's how this is going to look for the foreseeable and they tried to get Opus 4.8 to basically go through their systems and work out what was going on. And they got guardrailed every single time. So they had to use GLM 5.2, which is an open source model from I believe it is it Z.A.I. or moonshot. I think Z.A.I. First. So so I mean, like we were in this uncomfortable position where the defenders, unless they have like a really good relationship with the labs or they have like a special access program, a kind of defenseless like they're grasping at whatever tools they can get to kind of defend themselves against these adversarial threats. And I think, you know, that probably only gets worse unless we work out what we're doing with the guardrails. And I've personally had similar problems, like I write smart contracts and it is impossible to get an audit for your smart contract using the frontier models or very, very, very difficult. And it just puts you in this awkward position of being like, OK, like, you know, maybe there is a vulnerability here that maybe even a human auditor would miss. But I can't find it because Fable thinks I'm trying to steal 15 billion dollars, which I'm not.

**Jackson** (00:10:16): Yeah. Are we all like super like libertarian on the guardrails? Do we all feel like there should be no guardrails or is that just me, in my opinion, alone?

**Chris** (00:10:29): Is that your feeling, Jackson?

**Jackson** (00:10:31): Yeah, I mean, why should Anthropic and the government have access to a tool that is way more powerful than like any tool I'm allowed to have? That feels unfair.

**Tyler** (00:10:46): I guess you could say that the tool, I don't know, like you are like it isn't a human right that you have access to like at F-16.

**Jackson** (00:10:57): Right. Yeah. Or like it's like a citizen. Yeah, I guess that's true.

**Chris** (00:11:01): What if I can train my F-16 on an existing F-16? Then is that OK? Like by having all the F-16. I mean, that's the question. Like, what's the morality of that?

**Jackson** (00:11:14): I accept your metaphor. And I guess it is similar to like the government wielding power over you through like the weapons that it has that you don't have. But it's also scooping up the power of these intelligence models and wielding it against us as well. I don't know. I guess it's just a different form of weapon that now that they have over us.

**Tyler** (00:11:40): I mean, I think it's a pretty I don't think that there's like a clear answer from my perspective because I'm definitely more aligned on like less restrictions, more freedoms. People should have access openly to the frontier stuff like that's great. But then I think that if you hear some of the anthropic arguments, like there's they're really worried about like bioterrorism. And like my understanding is that if you have like a fable or mythos class model with no restrictions, you could like the model is intelligent enough to like tell you how to create a pathogen at home that could like create a pandemic or something. So all it takes is like one sicko terrible person out in the world with access to this to like cause really, really terrible outcomes for the whole globe. And so like there is a symmetry there between attacking and defending. And yeah, like what's the right move there? Like I think it feels right to like not deliver that capability to like any anyone in the world unrestricted. But then like so that means, okay, I have a line somewhere and maybe my line, you know, bioterrorism is on one side of my line. Where does that line actually sit? Does it sit with like cryptography or cyber or like, you know, do I think those things should be blocked or included? And certainly the classifiers that were on fable originally were like extremely comical and the like, you know, level of false positives that they would have where it would refuse to do like basic stuff like it refused to tell me about my dog's medicine because it was like a biology question. And I'm like, I don't I just want to know like what the right medicine is for when he got poisoned by mushrooms.

**Chris** (00:13:38): I think one thing I wonder about is like what is like at this point, like what is the time until there is an open source fable or mythos level model, right? And then like, you know, if you take that concession, like then maybe that changes what the best thing you can do is right. Like if we're if we're six, six months away from having like a GLM or Kimmy that is, you know, mythos in all that name, like, how does

**Tyler** (00:14:11): that change? Like the fact that fable won't do like cybersecurity thinking for you, Chris, it's like, okay, maybe they don't want you to have that, but they really don't want the Chinese labs to have that output and then distill from it. And I think part of the 3D chess is that they want to make their models basically either dumb or return kind of like empty, you know, refusals for these tasks. And then they're like, okay, as long as somebody's distilling us, maybe their model will be really good at

**Jackson** (00:14:46): generalist coding.

**Tyler** (00:14:47): That's fine. But we're not going to let them distill like the cyber capabilities, the bioterrorism capabilities. And then if there is an open model that is as smart at coding as fable, it's going to have these like potentially big gaps because it didn't get, you know, that and it's training data. And like potentially, you know, there's enough generalization from having a model or an agent that's super, super good at coding that like it just becomes really good at cyber. But like, I think that it is part of their having these classifiers. It's like to prevent you from misusing it, but also to prevent that capability from leaking through distillation reasoning traces into these open models.

**Jackson** (00:15:30): Yeah, I mean, you've totally flipped me now, Tyler. Now I'm like scared that if the models were open that people would kill me. So now I want them to be restricted, I guess.

**Tyler** (00:15:42): I mean, you know, like the internet beam, it's like, how do you want to control this technology? Do you want to use terrorism or like child abuse, you know, and like I feel like a little bit like pulling back that lever by being like bioterrorism. So yeah, I feel like that's usually the things that people go to to justify this type of additional control. I don't know. It's a difficult question.

**Jackson** (00:16:13): So now that Chris says that there's going to be mythos level open source model in six months. Does that mean we're all going to die? Not from the robots, but because of human generated pathogens from a nefarious edgy 14 year old living in Colorado.

**Tyler** (00:16:33): I hope not. I mean, that's when, yeah, I don't know what the, what the, how you protect against that. If that type of capability is diffused and it only takes like one motivated bad actor, then yeah.

**Jackson** (00:16:51): Does that mean we all need to like have our own agents developing anti pathogens monitoring what pathogens are being developed and give me the CRISPR agent.

**Chris** (00:17:03): Like I'm built different. I'll work it out. I'll figure it out. Just give me that.

**Jackson** (00:17:10): Yeah. Wow. Well yeah. Thanks again for the insight on the guardrails. I was like, these guardrails are stupid. I just hate being told what to do, but I think you're right. There probably needs to be some, some guardrails.

**Tyler** (00:17:24): Yeah, totally sucks. And I'm not like super pro guardrail. I'm just kind of like steel manning the case a little bit here and why I think it makes sense. Like they don't want their model distilled. So they make it, um, they don't, you know, provide that capability. And then they're obviously worried about it being used for bad actions, but you don't know where I'm down on this, but I'm not like a hundred percent, uh, like free unrestricted model person. I think because of that, but I'm also probably less restrictive than a lot of the policies that you see right now.

**Chris** (00:18:00): I just want to say to any anthropic or open AI, uh, listeners that, uh, I can be trusted with glass wing or GPT six. Um, I really, really need it. So like, you know, shouts out to you guys. If you, if you want to hook me up, you know, I'd be, I'd be very happy only for auditing purposes.

**Jackson** (00:18:18): Just to be clear. Open AI, you better give me early access to GPT six because otherwise I'm not taking back all the shit I've talked about 5.6 and open AI general. The thread is out. We're all a critical piece of this three legged stool that we call the podcast. Speaking of stools, Chris, what's going on with the gamer thumb and how is your week away from the pod?

**Chris** (00:18:47): Uh, yeah, I mean, so my week away from the pod was good. Uh, I was in Australia. Uh, it was very cold. Uh, but what it did give me is a chance to recover. So like, I didn't do a lot of typing whilst I was there. Uh, and, uh, and yeah, I still have game a thumb. So I don't want to tell anyone. Yeah.

**Tyler** (00:19:10): Did you do any gaming when you were there?

**Chris** (00:19:12): Absolutely not. No gaming. Okay. Full rest for the thumb. Yeah. Full use your phone. Were

**Tyler** (00:19:18): you like phone typing?

**Chris** (00:19:20): Yeah, a little bit. I did deliver the phone. That could be it.

**Tyler** (00:19:24): Were you wearing your brace the whole time?

**Chris** (00:19:27): No, I didn't wear the brace at all. So like, I obviously have a compliance issue with that thing. Um, I, what I did hold. So a lot of my friends have children. I did hold a lot of babies and they told me that babies create game a thumb, like, cause you're like shaking them around and stuff. Also, I don't know how babies work.

**Tyler** (00:19:45): You're not supposed to shake a baby. That's like the thing they have on PSAs for, you know, public health. Um, but yeah, you do get like hand and wrist pain from holding babies all the time because, uh, they're heavy and they like wiggle and you kind of awkwardly hold them.

**Jackson** (00:20:03): Dr. Tyler is back explaining baby thumb.

**Tyler** (00:20:07): Yeah. Well, when, uh, I, I got wrist surgery to put a screw in my wrist for a broken bone a week before Marco was born, but it was like on her due date. And so I went into the surgery and I told the surgeon, like, if, if I get a text from my wife that she's going to labor, I'm like calling the surgery off. Like, I don't want it to happen while I'm under. Uh, and they put me under and then I woke up and my wife picked me up, but then like I had a wrist brace on, I think for the first two to three months of Margo's life, which made it really difficult to like hold her and like change diapers and all this stuff. Um, so not the most ideal thing. So Chris, if I can do that for two to three months, um, your compliance on the gamer thumb brace, I don't know, man. I don't know. I think you need to do it for the good of your health.

**Chris** (00:20:56): Listen, man, I'm not here to be called out. All right. I'm here for like acceptance, you know, like I accept your non-compliance and inability to fix this very small problem.

**Jackson** (00:21:07): What about Tyler? I mean, Tyler, you had problems with that risk for like weeks without even knowing what it was, right? And you kept grinding two handed back hands on the tennis board.

**Tyler** (00:21:19): Yeah. I think I, uh, did I play you Jackson while I had a broken wrist? I think so. Yeah. Okay. So I broke my wrist playing tennis and I thought it was just sprained. And then I kept like, uh, playing tennis for like two weeks after with a broken wrist and it was kept being painful. And then eventually I went to the doctor and got an x-ray and they revealed that. Um, yeah, I guess that, that puts my, you know, I'm, uh, I'm throwing stones at Chris from my glass house over here.

**Jackson** (00:21:52): Yeah. We're just putting you back, you know?

**Chris** (00:21:55): Yeah. Thank you for the backup Jackson. I appreciate that. I was feeling cold cloud a

**Jackson** (00:21:58): little bit, but we're better now. Tyler, how was your vacation? How much, um, toxin do you want to do? Where did you go anywhere say?

**Tyler** (00:22:07): We went to, uh, New York and the East coast where I grew up. Uh, it was super nice, lovely summer weather there. Did some swimming with the baby, saw some old friends, family. Yeah. It was lovely. A lot of, uh, a lot of work with like childcare because like I got used to daycare a little bit too much that like cushy life. And then now we're back in like 24 seven childcare mode. It's just pretty, uh, pretty comprehensive. And then actually last night, um, there's this thing with babies where you're supposed to like introduce them to allergens to like test if they're allergic to foods. So you give them like little amounts of stuff and then you see what happens. And so we gave my daughter, uh, egg. And two hours later, she threw up like seven times all over both me and my wife. It was just like, I don't understand how she had that much volume in her stomach. And then she got like pretty sick. And we ended up taking her to the, like the children's hospital just out of like an abundance of caution, but it was pretty sad to see. And I spent the whole evening covered in puke. And then we just drove there without like changing or anything. So I just smelled like baby puke for like five hours. Uh, and then they like eventually, you know, gave her some good medicine. And, um, we got home and like cleaned up and went to bed, but yeah, a little bit of a harrowing night, but everyone is okay, but it sucks because you can't eat egg now and

**Jackson** (00:23:33): eggs are delicious. That's true. Does baby puke smell better than human, like American or pardon me, adult puke?

**Tyler** (00:23:42): Um, I don't think either are particularly great, but yeah, it does. It does have like that, like stomach acid kind of Biley like smell that normal puke does. Um, but she's, she's all right. And now we just grossed out all of our listeners. So like the, you know, we just, we just dropped off a half of them and the only people remaining are the people that love the puke talk.

**Jackson** (00:24:06): So, um, cool. Well, maybe we can do a quick Tyler one minute BIP 110. Is it nothing? Why do I hear about it?

**Tyler** (00:24:22): I feel like I'm woefully unprepared for this because I think it's just so stupid that I've referred, I've refused to pay attention to it. And so yeah, it's just like the discourse I feel like is so just dumb and I'm just tired of it and I just don't want to pay attention and I'm not going to do anything about it. And it will probably blow over in a few months. Um, I can try to give you my like understanding of it from a very high level, which is that there have been people for a while that are like very upset that, uh, they believe that there's spam. Bitcoin is being used for spam, which they define as these essentially like NFT kind of projects like ordinals and inscriptions. And they want to have the ability to block this spam block the use of arbitrary data on the, on the blockchain. And so they are like, okay, people are doing spam and this one specific way right now, we'll block that. And like, we're trying to force a fork for people that will block that. But it's very stupid because it's like, as soon as you block that one way, the people who want that activity to continue are just going to tweak the way it shows up a little bit. Like people have already done this and shown that like there's BIP 110, they have these filters. Um, the people who do ordinals and inscriptions are like, we'll just do it this different way. And now it's BIP 110 compliant and you'll have to fork a second time. And it's like this infinite game of cat and mouse. You just cannot stop people from putting arbitrary data into Bitcoin transactions because, um, you can make arbitrary data really hard to detect. Um, and like you can even, some of the ways that you would force people to do arbitrary data are like much less healthy for Bitcoin. It might bloat the U2XO state. Um, it might mean that nodes have to like validate a bunch of junk data that doesn't actually have any meaning. And so it's being done right now in kind of like a least harm way. And you could potentially force people to do it and more harmful ways, which is bad. So like, I just think it's a very misguided thing. Most people I know, who I respect, think it's extremely misguided and the people who are behind it seem like, um, either misinformed or just like really, um, like they're not arguing in good faith. I don't really know what their motivations are, but it doesn't seem like in good faith to me because it seems so obvious. Uh, and yeah, Bitcoin, I think will, will fork at some point. I think it's like in a couple of weeks. So there's the BIP 110 fork and then there's also this, um, e-cash fork that's going to happen. So we're going to get two potential forks of Bitcoin this year, which hasn't happened for a while. Um, I think both of them will, will die quickly.

**Chris** (00:27:16): So it's crazy. Bitcoin cash too.

**Jackson** (00:27:19): Yeah. Yeah. We need another one. Are you, so you're saying that the people that oppose BIP 110, it's not that they, that they disagree that Bitcoin shouldn't have spam. It's that the solution to prevent the spam is really narrow and yeah, I mean, that's basically it. Is that what you're saying, Tyler?

**Tyler** (00:27:43): Yeah. At the root of it, you can, you, you can really not prevent people from putting arbitrary data into Bitcoin transactions and like the, the solution is like worse than the problem. And it's also like a temporary thing, honestly, like, um, people can afford to do this right now because transaction fees are very low because like nobody is using Bitcoin. Uh, and if that persists and people don't use Bitcoin and don't make Bitcoin transactions on the blockchain because they're holding Bitcoin and ETFs or, um, Bitcoin is not becoming like a money, then, you know, Bitcoin is probably not very successful and it like doesn't really matter. But if Bitcoin is successful, then I expect transaction fees will increase and price out this activity and it will just go away naturally. And so like, I feel like this world that they're trying to solve for where like Bitcoin is successful and relevant, but spam is still economically viable on the main chain. It just is like a stupid, like temporary thing that we shouldn't overreact to, even if we had ways to stop it and we don't have ways to stop it. So it's all so tiring.

**Jackson** (00:28:53): Kind of a spontaneous topic switch. Um, so like when the fork happens, all of us that have Bitcoin, uh, I guess Bitcoin that's self custody. It's like duplicated, right? One is on the new chain and one is on the old chain. Is it lucrative for people that do forks? Like, do they make any money? Is it possible I can sell my Bitcoin e-cash to, to some Bitcoin e-cash to bag holders that I don't, because I don't want to keep it? Or does the value go to zero so quick that like I can't make money or no one makes any money?

**Tyler** (00:29:40): Yeah. So it's true. If you, if you hold your own keys and you have like actual Bitcoin UTXOs, like you will have a UTXO on the fork. Um, if you hold your Bitcoin custodially or like in an ETF, then whoever owns the keys backing that Bitcoin will have a corresponding amount of Bitcoin on those chains. But like they may or may not honor that and give you, um, exposure to these forks. Honestly, it's probably not even going to be worth it for them. I, I expect the forks will be not valuable enough to, to warrant like building, you know, uh, ways to handle them. And if you support every little fork of Bitcoin that comes out in that way, then you're like kind of committing infinitely to support all these. I kind of think zip one 10 is just like a publicity stunt. Um, I really don't expect it to be relevant much at all, but it is taking up a lot of like the discourse on, you know, Bitcoin X, which is really sad to see because it's such a stupid discourse. And I think it's like poisoning the vibes and poisoning, like, you know, anyone who comes into Bitcoin at this moment, they're just like, this is the dumbest debate that's ever happened. Like, why would I, why would I want to be part of this community? Um, it's just like sad.

**Jackson** (00:30:57): I feel like for the, for the dip in the forks. So you're saying that the minor can choose to like go to a different pool. If they don't agree with the minor's decision on which fork to take, is it that easy? Like, is it really easy to switch pools for the minor? Yeah, totally.

**Tyler** (00:31:17): It's like you just, you have your ASIC and your ASIC has like a configuration. That's like, what is the IP address of your pool to fetch blocks from? And you just change that. I have like a little mini bid X minor in my house. Um, it has like no chance of ever finding a block, but I can go on there right now and update the pool in 30 seconds.

**Jackson** (00:31:39): But are you mining for yourself or are you mining for a pool? Are you playing the lottery with your bid acts? I am. Yeah. There's, um, it is a pool,

**Tyler** (00:31:49): but it's like a pool where I get like 99% of the block that I find, I think. So the pool is really just, you're, you're paying them a small amount of a reward that you would find in order to construct the blocks because your minor can't do block construction. It doesn't run a full note. It needs to be told like what block to hash on.

**Jackson** (00:32:05): Dude, we should just say, screw the perp of fortune. Let's just look at your bid acts for an hour in the pot. It'd be a pretty boring episode.

**Chris** (00:32:15): We just would read every hash, every single hash. We'll see that like, Oh, only three zeros on that one. And we'll just manually look at

**Tyler** (00:32:24): the skintillating TV. Speaking of fortune, I feel like we, we, we've had one running. Should we introduce it or do we have more fork talk?

**Jackson** (00:32:39): We can't talk more about it. It's too much.

**Chris** (00:32:42): Well, speaking of forking things, um, so, uh, I followed your prompts, Tyler, where you said that purple fortune should be relative to the podcast. Um, uh, we haven't done this segment yet, but, uh, so I, I, so for context, I fed GPT 5.6 soul the podcast transcript and I said, Hey, like help us pick a perp like that is hopefully going up. Uh, that's relevant to the transcript. Uh, and it said long native XRP perp at 20 X isolated leverage. That is what it chose. And, uh, I'll try to summarize some of its reasoning here. Uh, it says at the final snapshot XRP was up 1.5% over 24 hours and it had 28.2 million daily volume and also X RLP RPL. Don't know what that is officially supports X four or two payments using XRP or RL USD. And that's it. That was its whole reasoning.

**Jackson** (00:33:47): Uh, God, these GPT models are so bad.

**Chris** (00:33:53): I mean, he's a great programmer, but as I alluded to on the last podcast, he's like, you know, it may be like the weird guy at the party sometimes. Uh, so let me share this. Let me share this.

**Tyler** (00:34:06): Uh, this really, uh, makes me lose faith.

**Chris** (00:34:14): Uh, it's, you know, I think it's just a case of like staying in your lane, like, uh, and maybe like the lane is not choosing perps for five.

**Jackson** (00:34:25): Oh, dude. What are you talking about? It's reasoning was shy, but it's, is it we're up.

**Chris** (00:34:31): Don't we've been under this whole podcast? Look at this line. There's a recent occurrence. We were here before, uh, if we close green, I'm very happy. Uh, $2,000 notional. So let's see, we see where we get to.

**Tyler** (00:34:46): Have you ever been a ripple guy, either of you? Like, I feel like ripple guy is like a very distinct phase that some people go through in the crypto worlds. But I don't, I don't know people who actually are afflicted by that, um, mental illness.

**Chris** (00:35:01): What do you, what do you think, Tyler? Be very careful what you say here.

**Tyler** (00:35:08): I think, I think Jackson probably has like dabbled in a little bit of ripple. I think Chris, I would say no, no, no hate on you, Jackson. But I feel like you're just like a little bit more exploratory and kind of like, uh, try anything. And then, yeah, maybe Chris and I are like, um, like cynical, like hermits hating on the world from our computer screens.

**Jackson** (00:35:34): All right. I've been called out. Yes. I have owned ripple. Yes. I've doubled my money under ripple. Nice. And literally an hour before this pod, I was talking to this Argentinian dude, and he said he loves ripple. The rest of it was in Spanish, so I can't tell you why, but the ripple signal is actually high right now. I mean, the purple fortune, the Argentinian dude, and I made some money on it.

**Tyler** (00:36:02): Yeah. Maybe this is just another invocation of the bell curve meme. And I'm like a sad mid curve person being like, ripple is so dumb. And then, you know, GPT is off there on the right hand side.

**Jackson** (00:36:17): GPT is the last thing. GPT is the last thing.

**Chris** (00:36:22): I, uh, yeah, I know I was, I was never a ripple guy. And I think like it's due to like a fundamental weakness in my reasoning. Like I need something to like be like conceptually beautiful in order for me to believe in it. And I don't know. I feel like I feel like ripple didn't have that for me. I was like, I was like, you know, we're like reinventing Swift, but I mean, that's a great story, right? And I think that's exactly it. Yeah. I think like I'm maybe I'm poor for this reason.

**Tyler** (00:36:53): So like, I don't know, like why does Swift need to be reinvented? I don't know.

**Chris** (00:36:58): I don't know. Why do you need to put two toll boots on a bridge?

**Jackson** (00:37:02): Like 10 years ago, they're like, there's this new coin and it can be used for international bank transfers. And you're like, what? I love that. I'm in. And that was even before all like the regulatory push that they've been doing, right? Where I think then they got sued. It went down a lot, but then they broke out because they just gave all the ripple to the legislators, right?

**Chris** (00:37:33): I think I mean, to this point, I think like maybe we're moving into a time where the only moat left is regulation. And I've like spoken to people around here, San Francisco, that like truly believe that. I don't. I don't. But I think a lot of people think like, you know, as you know, if we solve engineering, then like the remaining moat for your business is either regulatory or regulatory capture.

**Tyler** (00:38:00): And from like a generalized thesis or one specifically for like Bitcoin and crypto and fintech.

**Chris** (00:38:08): Yeah, I think I think fintech. But I also think to a lesser extent, a more general thesis, like I've spoken to people who are like, "Oh, I was going to build an AI wrapper." But then I thought like, you know, regulation would be a better moat for my business. And so I'm doing something in fintech. I don't know if I agree with that, but it is something I've heard, right?

**Tyler** (00:38:27): Because out of hiring an engineer, I hired like a lobbyist. Yeah, like a team of lawyers.

**Chris** (00:38:33): Yeah.

**Tyler** (00:38:35): But I do think some... I bought a lot of world liberty financial and suddenly I could do

**Chris** (00:38:42): whatever I wanted. Exclusive rights to something. Yeah.

**Tyler** (00:38:47): I do think like the marketing department of Ripple is like amazing. Like every cycle, whatever the trend is, they're like hop on, "Oh, we want red."

**Chris** (00:38:58): No.

**Tyler** (00:38:59): Ripple, bros, it's over. But it's like, yeah, like I think the reasoning...

**Jackson** (00:39:05): Speaking of Ripple and agentic payments, because those two are very related. Sorry, Chris, what were you going to say?

**Chris** (00:39:13): No, no, yeah. Should we talk about that? Should we chat about agentic payments and X402 and MPP and ADP?

**Jackson** (00:39:23): Yeah, I think maybe we should give the agentic payments a go. I've been baiting our listeners about agentic payments for like a month. So I'll lay the stage. Agentic payments basically means that your chat GPT can like buy stuff for you from like a consumer point of view. And from a business point of view, it could mean that your business could trade with other businesses in an automated way. And you're like just trusting your AI model to do that from a bird's eye point of view. Now, you two, Chris and Tyler, what do you think? Does it have legs? Is it going to happen?

**Chris** (00:40:11): Okay, I want to layer a little bit of context on top of this. There are four agentic payments protocols in the wild. So I mean, so I think like the story here is that Coinbase and some affiliated people came up with a protocol called X402. The idea is that it repurposes the 402 HTTP code, which I think is payment required. And it like allows you to do a payment. And there are some cool ideas like streaming payments and micro payments dovetailed in there. But functionally, what it does is you hit this endpoint and then it returns a standardized JSON list of the payments that the vendor accepts. On top of that spec, there's some stuff like, you know, how to integrate a facilitator to facilitate and do the payments for you, which of course is Coinbase by default. And was previously based by default, although I think there are more facilitators and more chains accepted now. So I think that kicked it off. From there, I think Google has put their hat in the ring. Stripe and Tempo have one called MPP, which is going through the IETF at the moment. I think it's in the proposal draft phase. And I mean, my take here is they're all much of a muchness, right? Like, I think, you know, when anything big like this happens, there's like a war to control the standard because maybe you can be on the ground floor and control some of the order flow. And basically, you know, my criticism of all of these proposals is they're almost exclusively exactly this. Like, they seem free and open, but like under the hood, you know, there are some minor structural advantages to the proposal. And I think a great example of this is that Stripe's proposal MPP is a superset of X402. So they're like trying to cannibalize the other. They're like, okay, well, this has some adoption. Like, why don't we superset this and then like layer our own stuff on top and then kind of like try to redirect the flow of this river as it's running.

**Tyler** (00:42:17): They're vampire attacking X402.

**Chris** (00:42:20): I didn't want to say it, but it seems like that. Yeah.

**Jackson** (00:42:25): I guess like the protocols for making the payments, you know, these companies are trying to make them and like monopolize that because it's like a way to make a lot of money. But really, we don't even need them, right? You can point Fable with like full computer control at a website and it can navigate the checkout for you. So like beyond the mechanism that the payments go through, do you see yourselves using like letting your agent buy stuff for you?

**Chris** (00:43:04): I already let my agent do stuff on chain. I would say my agent is the primary way that I interact with stuff on chain. By the way, look at CDRN/Sigil if you want. You want to know like how to do this. It's very cool. You mean your GitHub? Yeah, yeah, my GitHub. Look at my GitHub.

**Tyler** (00:43:29): My agent only buys Ripple. That's the only thing it's allowed to buy.

**Jackson** (00:43:34): I think you and Chris mix your agents up.

**Tyler** (00:43:38): No, I can totally see a world where you like let an agent shop for you. Say like go find me these sneakers. Find me the best price. I'm curious, Chris, do you think this is like a winner-take-all thing with these protocols? Because I feel like one thing that agents are really good at is like handling complexity. So if every company has their own flavor of this protocol that's like subtly different, historically, you would think, okay, maybe it's going to coalesce around one. They'll be winner-take-all because of network effects. Nobody wants to support all this. But agents, it's just trivial for them to hop protocol to protocol, know how to interact with it. So I don't know, I could see some of them, multiple of them persisting and it's kind of like a mess, but the AI is so good at disentangling that mess and hopping between different support that it doesn't necessarily converge.

**Chris** (00:44:44): Yeah, I totally agree. I think like the crispiest form of my take is that none of this matters. Like agents will pave over the complexity as they have with programming. But we're making this like needlessly worse for humans for just no reason, right? Like with standard fragmentation. Like if you go to Claude right now and you spin up CDRN/Sigil or any other key management MCP that you want and you tell it to do something, it will work it out. It will pull the contracts to bridge your funds and execute the payload. It doesn't matter if it's Solana or Ethereum. The agents quite adept at figuring out how to do things. And I think this will be no different with checkout or traditional payments or whatever. Yeah, that's my whole take.

**Tyler** (00:45:33): Okay, I think that covers like the protocol level, but then there's also like the rail that this stuff travels on. So there's like, it's almost a good combinatorial explosion of like we have all these different protocols. A lot of them support multiple different rails. And it's like, yeah, my agent wants to pay using X402, using like USDC on base, but the merchant wants to receive via like MPP on like an OUSD on tempo. And then there's like, you know, Google's, I forget what it's called, they have one of these protocols too, and they just like want you to buy something with Visa. So there's just like this, you know, multidimensional explosion of possibilities. I don't know if I believe the thesis that like, blockchains and crypto assets are particularly good for micro payments or for, yeah, like machine payments, or yeah, like, it doesn't seem to me like some people frame it as if it's like, so obvious that it's inevitable that agents will use crypto assets. And I don't really agree with that yet. I think there are some pros for them to use that. But then I think there are some, you know, downsides. And so I think it's yet to be seen how it will play out. And like, for all the downsides of like the traditional rails, I think that those companies that control them and operate on them are like sprinting to make them more agent compatible.

**Jackson** (00:47:12): And what you're talking about is copium. I think that crypto people are hoping and coping that agents will use internet native money.

**Chris** (00:47:24): I completely agree. There's no reason. I think it's maybe a better outcome for the commons if people settle on something that is like more open and more programmable. But like, you know, at the end of the day, I think this whole standard score is emblematic of like, how this works, which is that large players compete to capture the order flow. And unless they're forced to use something incredibly neutral, they want, right?

**Jackson** (00:47:52): Absolutely. Yeah, I guess I could see letting an agent buy like things I don't care about, like the shoes. Getting cheap shoes, but I don't know, like groceries.

**Tyler** (00:48:07): I feel like groceries is like the perfect use case. You know, you tell the agent like, I like, you know, Mexican food and Thai food and like steak, like plan me, you know, three to four dinners for this week. Come up with a recipe, put the ingredients in my cart, buy them, have them delivered to my house and like send me an email, you know, at night with the recipe and which ingredients I'm supposed to use. Like that kind of thing, I think is something that people do for sure.

**Jackson** (00:48:45): I just don't trust it's going to like pick a good recipe and get me all the right ingredients to actually perform the cooking. But I don't know. I also very intense about

**Tyler** (00:48:57): my eating. Yeah, I know that you are such like a culinary aficionado. You are.

**Jackson** (00:49:04): Did you know my last name is Cook?

**Chris** (00:49:08): That's very important. Did you just dox yourself on the podcast? That's crazy. Jackson,

**Jackson** (00:49:16): swag dog, chef. You're just cook, you know? Swag dog is only visible in the stupid streaming software. Don't, don't expose me, man.

**Tyler** (00:49:27): I agree with that. I'm also very unsure and I'm not like the most informed on this. So I don't want to come out with like a very like, you know, a strong prediction. But it seems to me like a lot of the arguments I've heard about like why it will inevitably be some kind of crypto asset. They don't necessarily make sense to me. I think it is like a little bit of motivated reasoning. People want their coin, whether they're a company with a stable coin or a protocol or they're like a Bitcoin enthusiast. People want the thing that they're attached to, to like win and they'll motivated reason around it. It'll be interesting. I don't know. We'll see. I could see.

**Jackson** (00:50:09): In the end, it's the payment company that is like processing the payments on behalf of the vendor that's going to pick which protocols they support.

**Tyler** (00:50:20): It's kind of crazy that that whole thing relies basically on whatever the legislation was that like bans stable coins from passing interest on the consumers in the US. And it's like, oh, there will be this new business model because they can harvest all the interest. And it's like literally, oh, that business model only exists because the government banned them, like preventing a race to the bottom where they pass that interest back on to customers.

**Chris** (00:50:47): There's some kind of regulatory mode at play here, I think for sure.

**Tyler** (00:50:51): Yeah.

**Jackson** (00:50:54): Yeah, maybe we'll get to cover the genius act itself next week. I think that the deadline passed, but I'm glad we finally talked about it into payments. And that's, it looks like we're going to end this pot up two bucks. That's 2% on the hundo.

**Chris** (00:51:25): So I think we're building quite the nest egg for our retirement boys. I think you owe 5.6 an apology. Jackson, you're very scathing.

**Jackson** (00:51:28): I'm never, I'm never going to apologize. Yeah, I think we'll close it off there. And do you guys have any farewells to our, to our listeners? Oh, shoot. We're almost down. Quick. Close it. I'm going to close it right now. Close it.

**Tyler** (00:51:52): Sorry about all the puke talk earlier listeners.

**Jackson** (00:51:56): Yeah, we'll see what we do with that.

**Chris** (00:51:59): Claude, don't cut it out. Claude, make that the centerpiece of the podcast.

**Jackson** (00:52:06): All right.

**Insert** (00:52:08): Later.

