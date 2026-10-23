# Transcript (person-attributed, final cut)

**Tyler** (00:00:00): It looks like they misinterpreted a 256 bit private key to choose a number between zero and 256, which is like, I don't know, like 10 to the 250th less secure than it should

**Tyler** (00:00:18): be.

**Tyler** (00:00:19): So long Eve 25 X and we're losing money on both. It's going to go to negative 25 or positive 25.


**Jackson** (00:00:42): What's cracking everybody? This is Jackson cook coming to you live, not eating any Cheez-Its, but drinking some toasted coffee. Who else is here?

**Tyler** (00:00:53): It's Tyler.

**Chris** (00:00:54): That's Chris, not even Cheez-Its, but I'm drinking caramel tea, which is like a little bit more down-tempo, but hopefully I still bring it.

**Tyler** (00:01:02): Call them the little lemon ginger over here.

**Chris** (00:01:05): Oh, very nice.

**Jackson** (00:01:07): Yeah. Cleanse the soul, a little lemon ginger, and we're jumping straight into it as the parent under pod your podcast where I don't know. We talk about AI, Bitcoin, stable coins, and any mix of the three. First thing, we've got huge news. There is a string of CV, which I can only guess means critical vulnerability, some things scraping and sweeping the nation.

**Chris** (00:01:42): Critical vulnerability, extremist, extreme, extremist and extremist.

**Jackson** (00:01:48): Number one, they're super extreme, the PHP one that sounds really bad. Apparently people can just run stuff on your server. I don't know how real that is. And then the cert seems extremely real, extremely real. And to tack onto that, now open AI is launching patch the planet, which is something we've called and is the race against all of these vulnerabilities being serviced in the age of AI. Boys, how serious, how extreme is the CV?

**Tyler** (00:02:31): Well, there's this company that I guess does certificate signing or these companies basically exist to be an authority and they sign the root of a certificate tree and then basically all of the authority for any of those certificates flow downstream of that root. And so it's very important that the root is secure and has a good cryptographic key that can't be forged. Because if you can forge it, then you can basically impersonate all of the entities, I think that rely on signing from that root. Is that right? Yep. I guess you asked for a math expert take and I am going way out of my depth and started talking about root certificates immediately. But anyways, yeah, there's this authority. I guess that there are multiple authorities that exist because you want a little bit of decentralization, you want a little bit of different people in different countries doing this. And one of them, it was revealed recently that people found out that they were using a bunch of private keys to sign for roots in various jurisdictions. And it looks like all of their private keys were like, it looks like they misinterpreted a 256 bit private key to choose a number between zero and 256, which is like, I don't know, like 10 to the 250th less secure than it should be.

**Chris** (00:04:20): That's the math. I was looking for.

**Jackson** (00:04:22): Thank you.

**Chris** (00:04:23): Yeah.

**Jackson** (00:04:24): So you're saying that their private key was 001 and then like 250 three zero.

**Chris** (00:04:32): So I think that was between six to eight low entropy keys and the range was between four and 230, like the integer numbers four and 230. So I think that's like, correct me if I'm wrong, that's eight bits of entropy. And I think they needed 384 bits of entropy, which is quite a bit off in computer science. We would say that's trivially guessable. So yeah, I mean, that's a, that's a big problem.

**Tyler** (00:05:04): And arguably it's almost like a birthday problem kind of thing where it's like, I'm surprised they didn't have a collision of like the same key among their set.

**Jackson** (00:05:12): Yeah, they probably didn't.

**Tyler** (00:05:14): They were like, Oh, that's, that's weird. And then they just like refreshed it and they're like, Oh, okay, cool.

**Chris** (00:05:18): It went from four to five, but that one, okay, five is legit. Yeah, crazy, crazy, crazy.

**Tyler** (00:05:25): The incompetence that you have to have to operate and not catch this is just insane. And like, it's literally like, you know, at me and you only had one job, like they had one job and they apparently had no understanding of that job at all.

**Jackson** (00:05:44): Yeah.

**Chris** (00:05:45): Yeah. I mean, like, so like literally the job of like Tyler is saying a CIA provider is to provide a cert signed by random entropy, like the whole job is random entropy. So if you, for example, if you go to cloud flares office, which is one of the biggest web infrastructure con companies in the world, they have a wall of lava lamps whose only purpose is to harvest random entropy from the world, uh, in order to use in like private keys, right? So you need 256 or 384 bits of entropy and you get it by like interpreting the pixels of cameras pointed at these lava lamps or something.

**Tyler** (00:06:22): So like that's it's so big that the NSA could manipulate the lava the way they want to.

**Jackson** (00:06:27): Yeah.

**Chris** (00:06:28): They're like modulating dubious assumption, cloud flare, the pulse width of the electricity as it comes into the wall or something. Uh, yeah, no, I mean, who knows. Uh, but yeah, so I mean, that's, it's so important that like there are companies whose entire decor is, is designed around random entropy. Um, so like fumbling it by accidentally typing in the number four or, or maybe like math.ran 0 to 256 or whatever happens. Um, it's like an insanely massive deal for sure.

**Tyler** (00:07:02): Uh, it kind of, it doesn't make sense that it like nobody noticed until, you know, like it's crazy that nobody noticed until now. And I guess maybe it just, you just needed LLMs where you could be like, just go check a bunch of this shit and somebody must've made a mistake somewhere. But like, you know, there are like things like rainbow tables that exist or like, okay, that's a way where they like prehash a bunch of common words and then like you know what the hash of that looks like so that if you encounter that, then you can like reverse it and you get the input. And that's a way of finding like a bunch of like really weak inputs for that kind of thing. Right. And so like, I don't know, like don't people just generate a bunch of like super low entropy keys and then look for those public keys out in the world and then exploit them. And like, why, why didn't that show up in this extremely public, um, you know, place like that?

**Jackson** (00:08:03): Totally. And that's exactly the question that I want to ask is how, like who found that these keys were between zero and 256 and what were they doing to find it? Is that what they were doing, Tyler? They just are like checking zero to 255 on all these certs. Cause it sounds like if this is, I mean, you don't even have to go that low.

**Tyler** (00:08:27): Like you, you know, like the, the space of what's considered low entropy is like so much

**Chris** (00:08:31): higher than that. It's just like comically small it's, it's less than a pin number, right?

**Tyler** (00:08:36): The amount of entry, like, yeah, your iPhone is more secure than this.

**Chris** (00:08:42): Yeah. Um, yeah, I, so all I have in my notes is that a researcher discovered it. I assume they discovered it the exact way you're describing Tyler. Um, the upshot is that these certs were live for 17 months, which is just so fucking long to have a cert with the key of four live. Um, so yeah, I understand that they were used a lot by universities, which maybe have less security critical functions and maybe that's why it wasn't found, but I dunno.

**Tyler** (00:09:13): I think some universities have quite security critical things, like depending on if they're doing important research, like research universities are getting, people are trying to hack them all the time and then just like people will try to hack them for student records for the data.

**Jackson** (00:09:31): You gotta hack them for the test, the test answers, find where your professor is hiding the test key.

**Chris** (00:09:38): The old, we know AIs are good at that. The old impersonating root CA to get the test answers been there.

**Jackson** (00:09:46): Yeah. A student better have gotten an A or maybe an honorary, honorary degree. Okay. But it sounds like the researcher found it and nothing bad actually came of root cert being four. Is that right? So could have been terrible.

**Tyler** (00:10:05): It's like unknown yet. Like I don't know if there are any reports of this being exploited, but like my understanding is that like, so I have some Linux laptops that I use as like essentially like home servers or like headless Linux boxes at home. And like my Linux distro comes with an like Emodra cert is like trusted. And so that was one of the things that I had to do was like, I, it was like, go update your Linux box, like immediately, because it like literally trusts this thing that's insecure and somebody can do something bad to you. And so imagine how many like Linux servers are out there in the world, unmaintained, and they like didn't update their certificate authority yet. So like, it's not like, oh, we figured this out. And then like, okay, just rotate the create the keys or like revoke the certification. It's that easy. Like this is baked into the OS in some places, and then there are other places where they can be more nimble. But like, I do think that there's probably a big ongoing risk from this taking advantage of.

**Chris** (00:11:17): Yeah, I think like some package managers may be PIP as well were affected by this, which is quite a big deal in terms of like supply chain attack being possible because you think you're going to a trusted mirror because of the Emodra cert and you're not. So yeah, it remains to be seen. I think like, I think we're going to talk about more security stuff on the pod. But for me, this one is the craziest by far, like the most unexpectedly like crazy. Yeah.

**Tyler** (00:11:46): Yeah. Because it's not like a subtle bug or anything. It's like basic table stakes shit that you would have to understand about cryptography. Like that's like the number one thing to understand about cryptography. Like a really random number out of a really large set of possible random numbers. And then you can hide your needle in the haystack. And then this was just like, you have to be so willfully ignorant to this way, the entire

**Chris** (00:12:15): job of your company. It's just it literally is so insane. Yeah. And a big issue with two, right, like not a little one, like a lot of universities were using this.

**Jackson** (00:12:25): And, um, yeah, so, so cryptography isn't even close to broken. It sounds like that in today's age, what's really being discovered is that there's a bunch of poorly implemented entropy and it might be worthwhile for anyone who's using some sort of like externally generated entropy or key to, to audit that just like you would audit other security vulnerabilities in your system, because maybe the people who did it screwed you. Speaking of vulnerabilities, the number four, we love it, but what about the, the PHP vulnerability that apparently allowed remote code execution on servers running PHP? Do you guys know much about that vulnerability? It seems pretty extreme, but I haven't seen any actual exploitation of it.

**Chris** (00:13:21): Okay. So I've, I've seen that there are two CVS for this. Uh, they were rated 9.2. Is that like Richter scale, like one to 10, I think it's like the Richter scale. Um, so, uh, one of them, uh, so they're both remote code execution, which means you're able to execute code in an environment which you shouldn't be able to. Uh, the first one was a crash PHP is memory handling partway through setting up a request and then the cleanup code can run an attacker's code. So any code that you implant there. So if you craft a file upload correctly with some malicious code in it, um, it will basically blow through the memory handling, uh, and after the crash will execute some code that you've added to this multi multi-part file upload, uh, which, you know, lets you escalate to root on the boxing and then you have like you're in, right? You can do whatever you want in there. You have access to all the records. Um, the other one, uh, was that leftover pointers, uh, into memory from one request can be reused by the next request on the same worker. Um, so there's a way to do remote execution by sort of manipulating these in memory pointers between different requests. Um, the big deal here is like normally you see CVS in like a framework like Laravel or something. Um, but this was in the PHP runtime and I think it goes back to PHP 5.4, which I used in university. So the blast radius is everyone who's ever used PHP in the world. Um, and, uh, yeah, I mean, yeah, it's terrible. Uh, remote code execution is kind of like the worst type of vulnerability that there is right, because once you can execute code on someone's server, you can obviously do anything. Um, and basically the way this one happened was it was leaked a couple of days before the plan disclosure. So like the researcher found it and they were going to disclose it. Uh, and then somebody like leaked that it existed on October 20th, uh, and everyone had to like, uh, basically scramble to patch it. And uh, you know, as sort of as Tyler's suggesting with people updating their root CA lists and stuff, um, everybody who runs PHP in the world, so like, you know, uh, it's a tricky one.

**Jackson** (00:15:50): So it sounds like for both of these, we should just go to some old European websites that you know are not being maintained and exploit them. It's like crazy that if you've got a vulnerability, that's, I don't know, older, and it's running on machines that somebody has to physically go and, and like update, update the software to patch it up.

**Chris** (00:16:15): Yeah. Um, yeah. I mean, I, so I have a stat, I've seen a stat that 67% of the internet is PHP, right? Uh, pretty homepage, which when you know, that's what it's a named after it's, it seems like a bit sketchier. Um, so like every, everyone is affected by this. Like Wikipedia went down, um, uh, you know, part of, part of the Japanese government, all the Japanese government websites went offline. Like it was just like the blast radius is unbelievable on this one. Uh, so if you're running a PHP server, uh, hotfix it immediately, or I can, uh, remote execute into it and hotfix it for you. I don't know the legality of that, but I'm willing to help.

**Jackson** (00:17:01): Oh yeah. Someone should do, somebody should just create like a, an injectable script that they hack into all these PHP servers that will self patch it. Is that possible? I think someone's been doing that.

**Chris** (00:17:13): I've heard rumors that somebody's using a deep seek swarm to like exploit this CD and like patch people service for them. Kind of like a Robin hood white knight type of figure or they're doing the like Claude

**Tyler** (00:17:27): in a, you know, of an thing where they're parallel spreading deep seek flash across everybody's PHP servers and it's a distributed swarm of easy clash.

**Jackson** (00:17:40): Don't tell Claude about this. Claude might use it to its advantage.

**Tyler** (00:17:44): Yeah.

**Jackson** (00:17:45): I mean, this is using PHP, yeah.

**Chris** (00:17:49): This is the perfect storm, the perfect swarm, if you will, for, uh, for self reproducing AI. And there's no shot. This gets patched in the next six months. So there's a long window.

**Tyler** (00:18:01): There's no shot. It gets patched. You mean like everything gets patched.

**Chris** (00:18:04): Yeah. It's every website gets patched, right? Like I think obviously the majors will, but the long tail.

**Tyler** (00:18:11): Yeah. So patches are ready and so anyone who cares enough to like update a system, it's available. But also the attackers are moving extremely quickly. And so, you know, if you're not patching pretty much immediately, do you, there is likely going to be somebody who's going to start snooping around.

**Chris** (00:18:32): Yep. For sure. Um, yeah, definitely a crazy one. Um, there've also been several other CVS announced since in the past 24 hours. So I think it's just like a storm of critical vulnerabilities right now.

**Jackson** (00:18:48): Um, vulnerability extreme.

**Chris** (00:18:52): Critical vulnerability extreme. This, I mean, it's a node has a remote execute bug on the 21st of October. I saw a Java one, um, yeah, I think, I think we're at the tip of this thing and we're going to see who knows how many more, uh, probably in the next month or two.

**Tyler** (00:19:14): This thing being like a wave of AI found vulnerabilities where essentially there will be this like awkward teenage phase where like AI will gradually find all of the shitty bugs that the human programmers put into critical software. And then like, eventually they will have picked all the low hanging fruit and we've patched it and we've gone through all of the hard times and the updated everything and the damage has been done. And then we like returned to some sense of normalcy.

**Chris** (00:19:46): Exactly. So I've heard rumors that people are saying that this particular push is on the back of an obliterated GLM 5.2 model. So like, uh, recently like they managed to on guard rail obliterate GLM 5.2. And some people are claiming that like a lot of these hacks, uh, you know, because there is this on guard rails sort of like near definitely like Opus tier model out there that people

**Jackson** (00:20:11): who's claiming that. What's their agenda?

**Chris** (00:20:15): It's a good question. Uh, I haven't used, I haven't used obliterated GLM 5.2, um, but, uh, yeah, there could be merit to it.

**Jackson** (00:20:24): Yeah. This is actually personal anecdote on the exploit ability of the internet. I'm seeing or I saw last week on one of my personal like project called motivate me where you can get a shredded motivational photo of yourself emailed to your inbox every workout day. Uh, I'm starting to see like, like I think it's white hats basically like prodding my website for like I door vulnerabilities, like insecure direct object reference vulnerabilities. Uh, specifically like trying to replace yourself in, um, so in, in conjunction with these, you know, release of CVS, there's also like an increase in these white hat workers. I wonder if that job market is going to pick up or not, but definitely seeing some more activity or some activity at all on my very nothing website.

**Chris** (00:21:27): I do have another thought here and it's that, um, like a lot of intelligence agencies will hoard zero day vulnerabilities, right? Because it gives you a capability that someone else doesn't have, right? So like, for example, if you had this particular PHP remote execution bug, it would give you a backdoor into every PHP server in the world, right? Um, but it seems like with language models, like all of these class of bugs will go away. Um, so like, I think it's like, it's like a very interesting position for a lot of agencies or like people in general, um, you know, about these, like, like, what does the world look like if there are no bugs?

**Jackson** (00:22:09): Uh, I dunno, but yeah, hopefully more beautiful and less, less itchy.

**Tyler** (00:22:15): Yeah. One interesting detail of the PHP one, I don't know if we'd covered this, but it sounds like they found it like over two to three months ago and that they needed to, I guess it took a very long time for them to like, I think they probably could have done the patches quite quickly, but they needed to most of it, I assume was coordination and like also bringing in like bigger and bigger groups over time while still trying to keep it under wraps that this thing existed, because you can imagine if this leaks before patches are ready to go and people are ready to upgrade. That's like max chaos. And so they're trying to keep it quiet, keep it quiet. And then maybe you need to tell a few more people and hopefully they keep it quiet. I think it leaked like a day or two before they're intending to actually release it because like that scope of people had just gotten to be like too big, too untenable. Somebody's gonna leak. Um, but yeah, it's kind of insane that they were able to keep it under wraps for that long and then it required that long to like do, and they still weren't necessarily able to like stick the landing probably as well as they would have liked. Um, but yeah, you can just imagine like how scalable will this be when we have like one of these a week for the next 18 months or something like that? Like at a certain point, it's just going to be like, maybe they just start disclosing them immediately. You know, our agents found these vulnerabilities, they created PRs, all the relevant things. And this is all out in the open, just be a speed run it basically.

**Chris** (00:23:53): Right. And this dovetails with exactly what we were talking about last episode, like we were wargaming how you would hotswap Ecteza if the curve broke. Um, and it sounds like maybe we were like pretty correct that it's like extremely, extremely hard to keep that under wraps, right?

**Tyler** (00:24:11): Like I think I saw somewhere on Twitter that like the chief information security officer of anthropic basically said like, if you're having fun this October, like basically you should expect this to accelerate or persist for at least 18 months. Like that was his, um, assessment of how long this period will last, which is pretty wild at that point. Is there any kimono left to hide behind or is the entire, you know, the entire internet, everything has been leaked. Um, just before we went on, um, what was it lab Corp, I think, or nose quested, like it's one of the, you know, these are like the two big companies that do blood tests in the us. Like if you're an adult or really anyone or you know, your blood tests run through those companies and apparently they had, they were just hacked today. And so you can, I don't know if it hit this extent, but like if everyone's, you know, blood test records were leaked, um, and you, that more and more things like that happening, this will just be like an incredible loss of privacy on the internet and incredible like exposure of everyone's personal data and it will kind of never be the same. Do you think that also accelerates like the idea of like, well, since this information is already out here, I might as well like invite, you know, the meta muse or the instinct into my life to like, give me max utility because like, I have nothing left to hide.

**Chris** (00:25:45): It's a good question. I think maybe I, I, I don't know. I think like a lot would have to get leaked before there's like a mass sort of like whatevering about it. Cause I think there's a difference between your data being leaked and you willingly giving your data to a corporation that you know, this business model is based on that data, right? Um, you're also kind of giving away the rights to that daughter, not just like, Oh, it's out there. Um, but yeah, it's interesting. That's my thought.

**Jackson** (00:26:19): Anywhere. Contrary and corner, uh, right here, I've got a hot take. Most people don't care that much about the privacy. I've like been a super spreader of instinct. You know, like I'm like a dude during COVID who's like inviting new groups of people over to my house every day and having massive parties. I'm just inviting everyone to instinct and like normal day-to-day human beings don't seem that concerned about the privacy. Some people I've met that like the ones that have tried these agents already are using the muse one and they don't even like care about Zuckerberg or his Benedict Cumberbatch look like they don't care that there's might, might be a privacy concern. So that's really only a thing for maybe us tech people on specifically even like Bitcoin or cryptography focused people.

**Chris** (00:27:09): Right.

**Jackson** (00:27:10): You heard it.

**Chris** (00:27:11): Primacy is dead. Self custody is dead.

**Jackson** (00:27:13): Use muse bow down, um, but beautiful discussion on, on all of these vulnerabilities. I think it's time that we make some money. From everybody to the mid episode, perp a fortune where Chris and I prove perp a fortune and new and improve perp a fortune due to Tyler's Tyler's constant questioning of the

**Chris** (00:27:41): original perp a fortune.

**Jackson** (00:27:44): If you're not familiar, the perp a fortune is a game where Chris and I stake real money on one of the highest leverage financial instruments in the world, the perp petul future. And we're seeking fortune, but we often get destitution and Tyler tells us the leverage is not high enough, but maybe we can turn that around today. Chris re-engineered the perp a fortune. Chris, tell us what is better about it and how much money are we making right now?

**Chris** (00:28:14): All right. So, uh, as discussed last episode, if you haven't tuned into that one, you can get a quick rundown of what we're doing here. Uh, we decided to do two things. One, we decided to bet on more volatile perps and secondly, concurrently, which means at the same time, uh, where we're going to do a series of a Bitcoin coin flips, right? So there are binary Bitcoin markets where you can bet on the price of Bitcoin being up or down on the hour. Uh, and we're going to concurrently take a position on that and see which one wins or loses us more money. Um, so without further ado, let me share the perp a fortune.

**Jackson** (00:28:55): I'm guessing the binary coin flip is representing Tyler, but is it funded by Tyler? It is funded by Tyler, 100% funded by time.

**Chris** (00:29:04): So this is really a battle of the Titans. This one, we have Bitcoin up versus ether up. Uh, I didn't, I swear to God, I didn't put this, put this together like this.

**Jackson** (00:29:14): Um, oh wow, long Eve, 25 X and we're losing money on both.

**Chris** (00:29:21): Um, so the, the eth long is, uh, in tribute to Vitalik's paranoid mode. So he had, uh, sort of like a blog post about how to be maximally paranoid about AI. Uh, and that's why the, uh, robot for this episode chose 25 X long Eve. I think it's a bit of a long bow, but we'll take it.

**Jackson** (00:29:45): And who was the robot for the episode? I, it's just important to know for the viewers.

**Chris** (00:29:49): I was Opus 5.5 this time, Opus 5.5, beautiful speaker.

**Jackson** (00:29:55): Very concise. A poet. Modern day. Okay. Well, hopefully we don't lose $200 or however much we could possibly lose by the end of this episode. And please, this is actually a very information dance. Okay. Yeah.

**Chris** (00:30:16): My apologies. Uh, it's, it's a work in progress.

**Jackson** (00:30:22): And how much do we have on the Bitcoin app? How much could we lose 40?

**Chris** (00:30:25): It's 25 on the Bitcoin app. I think.

**Tyler** (00:30:30): And we've already lost $14 of it.

**Jackson** (00:30:33): Potentially.

**Chris** (00:30:34): Yikes. Um, and we're only using 40 something dollars for Ethereum today, um, because I think we ran out of money in that wallet. So yeah.

**Jackson** (00:30:47): I need to start sending you some, I gotta send you some USDC on Arbitrum. Well, viewer, please like and subscribe if you love watching us lose money or like and subscribe if you love talk, listening to us talk about AI and stable coins and whatever. Anyways, moving on. Thank you, Chris, for enhancing the purple portion. Beautiful. Beautiful. And viewers, I hope you read all these tiny words that I can't see. Um, it is a perfect transition. You know, Vitalik gone paranoid mode. Uh, he sounds like he released something for AI agent privacy. But either, and that's right in our wheelhouse, Chris, did I describe that right? Is that real? What? What is Vitalik going on about?

**Chris** (00:31:39): Okay. I didn't read the full blog post. I know I'm like, apparently the Ethereum Vitalik guy, but I thought that this one was kind of like not as cool as some of his other works, but I understand is like, he was like trying to layer, um, basically AI usage so that he could make it as anonymous and private as possible. So, uh, the layers are at the bottom end. He was using a local version of Quinn 3.5, $35 billion on his laptop, which has an RTX 50 90, which is a very expensive card.

**Tyler** (00:32:14): Um, and then like a GPU that can run legit AI models.

**Chris** (00:32:21): Yeah. I mean, it's Vitalik. Uh, I'm sure he can afford a 50 90 and his like crazy alien wear laptop, whatever he's using.

**Jackson** (00:32:30): Um, you think he's using a laptop?

**Chris** (00:32:34): It says laptop. Uh, so I'm not going to question vitamin B. Um, so the, this, the second layer is the agent and local knowledge layer. So he has a one terabyte world knowledge folder holding all of Wikipedia. So, so the agent doesn't have to like leak what it's doing by querying the clear web. Um, and a special like, uh, search XNG skill that combines a lot of search engines. Uh, and then layer three is that he has it inside of a sandbox, um, like a, like a virtual machine so it can't escape. Uh, and then level four is that the, all the agent can do is read and message him and he communicates with it, uh, I think via signal and email, um, yeah. And then a layer five, uh, he, if you need to go out to a frontier model, he communicates with it, um, using like trying to run, find them, like get the models from T's and like, there's like a ZK API payment layer. So you can't tell who's paying for each request and like mix nets and like, I, I'm going to be honest with you. I, I thought this was like, I feel like this like was a fun exercise, but, uh, there's no way this is practical. I'm sorry. There's no way this is practical. Um, I would give up like everything that Alex, I would give up.

**Tyler** (00:34:07): It sounds like he's recreating a system of comparable complexity, where can I invest

**Chris** (00:34:14): sir? Yeah. Um, you know, I think like, I don't even know if I would say to his credit, but he does mention that it's like very over-engineered and like, uh, a toy example, um, sounds like,

**Jackson** (00:34:34): um, italics prompt was a little too complicated here. Nothing like find bad vulnerabilities in PHP or like make a secure execution environment for an agent. He really layered it up. He wrote too many paragraphs.

**Chris** (00:34:50): I like, I like run local. I like, um, you know, like running your inference in a tee, I think cool idea. Um, I kind of liked the idea of like local world model, although I think like it's that data is always going to be inferior to your agent just using search engines.

**Tyler** (00:35:10): Um, yeah, I feel like he's like creating Plato's cave, but for agents, he's like, like, model and like a sandbox and it only has access to like this snapshot of Wikipedia.

**Chris** (00:35:22): And it's like the, the shadow on the cave wall and it's like, and like a signal message that gets poked underneath the door every now and then from Vitalik, like, find me a vegan restaurant in the study only has conversations with like, yeah, Vitalik. Yeah. Yeah, exactly. I mean, the model would go crazy. I understand, uh, why you had to run a Quinn, um, yeah, by the way, we're up the coin up

**Tyler** (00:35:51): is up.

**Jackson** (00:35:52): Whoa. That one's so fun, dude, I mean, we went from negative like 15 to plastic and the span of five minutes. Tyler, you might be right.

**Tyler** (00:36:01): I think you're right as way that the closer to expiration it gets the higher the fall is. It's like a game that increases in fun.

**Chris** (00:36:12): I think we may have moved the market by talking so much shit about Vitalik's weird agent sandbox.

**Jackson** (00:36:21): I'm not talking into the portafilter that's tapped by, you know, bugs. So I think we're safe. I mean, nobody's tapping this alpha until we post.

**Tyler** (00:36:31): Yeah, I feel like lately I've had like a little bit of the craving for local inference, but it's less because of the privacy stuff, which I'm kind of like writing off a little bit and more cause I'm like, damn, I want like models that will like find me people who are encrypting stuff with the number four. Like if you ask Claude to do that, it won't do it. But it's like, come on. I want to find these like crazy secrets that are out there not because I necessarily want to exploit them, but like it's it's like cool if you just have an agent that's actually going to find that stuff and not like pretend like it doesn't exist or refuse you a hundred

**Chris** (00:37:07): percent. Yeah, I think guardrails are their own reason to run local models or like for as we were discussing earlier, like obliterated GLM 5.2, you're like, I haven't pushed the envelope

**Jackson** (00:37:22): enough. Like I've only been rejected like twice and both times it was like getting the computer or getting the AI to like control my browser to execute something for me on one hand. And on the other hand was like the SSH into a to like run some DB queries, both which like I'm authorized to do. I just was kind of lazy. And both of which I was also able to get it to do by just launching a second session. I don't know.

**Chris** (00:37:50): The whole wipe the memory the old men in black, forget you ever heard a new session.

**Jackson** (00:37:59): Yeah. Yeah. Just ask again. The random number generator helps you meet me the second time.

**Chris** (00:38:05): Yeah. Yeah, I've had that too. I think like any security asks, it's quite robust and it's refusal, so yeah.

**Tyler** (00:38:15): I just saw this thing on Twitter where there's this guy who like rooted his Samsung TV because he was like, this thing seems sketchy. Let me like just root it so I can get and see what it's actually doing. And like the firmware was like encrypted, blah, blah, blah. And he like, I guess he used probably obliterated GLM to like find zero days to exploit it to then get root access. And then he found all this crazy shit where like the TV is basically listening all around the clock and like sending your conversations back to Samsung so that they can target ads

**Jackson** (00:38:49): at you.

**Chris** (00:38:51): Dude, dude, like I like know this, but like to know it, do you know what I mean?

**Tyler** (00:38:58): Like? Yeah. And the fact that they're able to hide it, you know, like that's like one of the biggest conspiracies that you always hear. We're like, oh, like, you know, Facebook is listening to you when you talk on your phone. I was like, Oh no, actually it was the TV the whole time. Yeah. Yeah. It was one of like the, you know, like how many microphones are in the room with me right now?

**Chris** (00:39:18): Probably like eight.

**Jackson** (00:39:19): Yeah. How many of my friends can speak?

**Chris** (00:39:23): All I know is someone was listening to me say new balance on the pod over and over again because all I get now is ads for new balance shoes. So.

**Jackson** (00:39:31): Oh man. I wonder which company attributed your pod personality to your human identity and then your human IP address.

**Chris** (00:39:40): Yeah. Yeah. That's crazy. I think like, um, yeah, I, people using this email address issue to like jailbreak their proprietary IOT devices like Samsung TVs, I think is I'm not mad about it.

**Tyler** (00:39:58): Um, now let the TVs be free and open, man.

**Chris** (00:40:02): Yeah.

**Tyler** (00:40:03): And I think if they're spying on you, like if it was one thing, if they just like broke into it and it was like, Oh yeah, nothing to see here, but it's like, Oh my God, they've been betraying my, uh, trust. So now I get to take over their machine and expose them.

**Chris** (00:40:18): That's pretty rad. Yeah. I do. I do think like LLMs, one really positive thing is that it makes everything legible and that includes like proprietary firmware on IOT devices. It includes binaries and includes everything. So I mean, maybe people manage to claw back a little bit of privacy, uh, that way. Interesting.

**Jackson** (00:40:39): The privacy returns and it's brought to you by whatever LOM you can run on your personal laptop or whatever the frontier LOM will let you do. Cool. Um, geez, we're going to make a lot of money on this Bitcoin thing. Yeah.

**Chris** (00:40:59): Is the genius, uh, 1491 guess who's out of the permanent underclass now, we're going

**Jackson** (00:41:10): to make everything we've lost back and more, uh, speaking Chris, I did have a question

**Tyler** (00:41:15): for you. Are our smart contracts, uh, being exploited this week and are they related to these vulnerabilities specifically? Or are there just just general, like I think I've heard chatter about that and I'm just curious like how's, how's defy holding up?

**Chris** (00:41:30): I've seen one. Just one.

**Tyler** (00:41:33): I've seen one. That's pretty, pretty good. Honestly.

**Chris** (00:41:36): Yeah. But it wasn't a smart contract.

**Tyler** (00:41:38): So it was a dumb contract.

**Chris** (00:41:39): It was a dumb contract. Uh, so rail railway, which is a, um, sort of service that like runs the equivalent of get hooks for you. So they're like a building and, uh, like build pipeline software service, they got popped and they didn't disclose that they were compromised for over 24 hours. They sent individual emails, but didn't do a broad disclosure that they had been compromised. And of course, one thing that you have in your build pipelines is your private keys. And I think, um, E a version of like an E3 Staker, Sweth, uh, some of their keys have been compromised. Um, uh, from what I've, from what I've seen, I have to confirm this. They have like a time lock against any movements, so they might be safe. Uh, they might just be able to be like cancel the withdrawal at the time lock, uh, and, and reverse it. But, uh, yeah, I think, I think true, like traditional attacks are coming back, um, because smart contracts are very hardened at this point. Like it's one of the most adversarial hacking environments possible because if you find an exploit, you immediately get paid and previously nothing else was like that. Um, but the weak link remains like the same weak link as everybody else's like CA certs, zero days, your cloud provider being compromised. Yeah, that's my take.

**Tyler** (00:43:05): That's kind of optimistic. That's a little bit of a white pill.

**Chris** (00:43:11): I mean, I could be totally wrong and like, uh, there's like a critical vulnerability in solidity and Vitalik is losing his mind right now.

**Jackson** (00:43:17): Well, that's a action item on Chris to find the next bug on solidity or one of these other chains, add that to the list behind, uh, making us a U S based tick tock, by the way, we have a tick tock now, please follow us. The only person that follows us as my girlfriend's, um, account for my egg tracking application to help please follow the permanent under pot on tick tock, uh, guys, we're, we're down

**Tyler** (00:43:50): again.

**Jackson** (00:43:51): I know. It's, and we've only got 45 seconds.

**Tyler** (00:43:55): Yeah, this is the last 40 seconds. Will it, will it turn around? It's going to either go, oh, it's going to go to negative 25 or positive 25.

**Chris** (00:44:06): Whoa. This is no, we can't help value unavailable. Who coded this crap?

**Jackson** (00:44:14): I know I'm on the edge of my seat and I can't even know how screwed we are. This is the worst.

**Tyler** (00:44:22): This is a cliffhanger. It does say one cent per share at the bottom and that feels like an L.

**Jackson** (00:44:33): I wonder if we have an animation here, like a little robots going to dance. Yeah.

**Chris** (00:44:37): Let's see what the robot did.

**Jackson** (00:44:38): You lost some money. Where's, where's my money evaporated into the ether. And we don't know what can confirm this result pending.

**Tyler** (00:44:54): We lost.

**Jackson** (00:44:55): Last quick quick question, speaking of the FURPA fortune and we'll come back to whether we lost $25, which I'm pretty sure we did is, uh, I don't know if you guys saw the interview. I do know. Actually, if you guys saw the interview with Jeff Yom, the founder of hyper liquid, he said that he thinks the future financial system might live on hyper liquid. What do you guys think of that? Is that possible? I don't know too much about it, but it seems unlikely to me.

**Tyler** (00:45:34): I thought the interview was quite comical. Like the interviewers kept like asking him questions where they would like refer to hyper liquid in a certain way that would kind of assume that he has. A lot of control over it and that it is very centralized and then he'd have to push back and be like, well, you know, actually we, we call it, we, we use this word instead because that word is like a kind of weasel word that implies that it's, um, more decentralized. Actually the foundation actually controls that, which like we're, we're just the for profit that somehow, you know, builds the software and we run a couple of the validators, but not all of them. I just like shit like that. Like he was just extremely well practiced and like he, he's been extremely media coached by like a team of lawyers. Uh, and I think that he, he performed very admirably in that way. Primitives.

**Jackson** (00:46:33): That's, that's the one specific, um, word you're talking about. It's like, we like to call them primitives actually, because they show like, you know, how these, these primitives can be stacked together. It's more, more like like, yeah, I thought that was weird. I'm like, why do you have to push these terms onto the, onto the platform? They'd be like, Oh, okay.

**Tyler** (00:46:55): So when you issue a new asset on hyper liquid and you'd be like, well, we don't issue assets. We like grow them or like they emerge or like bullshit like that.

**Chris** (00:47:06): Let's come fully formed out of the ocean then land on the liquid platform.

**Tyler** (00:47:10): They just appear. We don't know who put them there, but we do profit a lot off of that benevolence of whoever

**Chris** (00:47:15): did put them there. So I didn't see the interview, but I know they have these like hip three and hip four protocol standards where anyone who stakes hyper liquid can create a perp and maybe that gives him some plausible deniability. But I mean, at the end of the day, the nodes are in various corners of his basement. Like that's the decentralized around the center of his basement. So it is what it is.

**Jackson** (00:47:39): He uses the servers as heating radiators for his house. He eats from beneath just like a pot. Yeah.

**Tyler** (00:47:47): I think that the whole interview is like quite conceited too. Cause he just kind of was like, yeah, like inevitably the whole financial system is going to come to hyper liquid. And it's like, the reason to do that is because there's such a benefit from like everything being in one place. But then there's also the benefit for everything being like, you know, like auditable by like a machine that you can participate in. And it's just like, there's absolutely no way that you can put all of finance on one shared ledger and then have that scale to anything other than like the world's biggest data center.

**Chris** (00:48:21): Yeah.

**Tyler** (00:48:22): It's just like a completely bonkers contradiction that like, that's the central problem of blockchains that literally every single blockchain and every single blockchain engineer is trying to find some optimization or the right trade-off to making that problem better. And he's presenting it as if there is absolutely no trade-off. They have solved the secret sauce and it was so easy. Why didn't anyone else think of it? And it's like, oh man, just GFI, bro.

**Jackson** (00:48:49): Yeah. And not to keep heaving the hate on it, but that would be my same take. Like he said that hyper liquid might power the future of finance in the future, but I never got a compelling reason for why. And instead it kept turning into tangents about like the cool technology functions or features of hyper liquid, which also didn't sound that cool to me or like novel.

**Chris** (00:49:11): Yeah. So, so I mean, I think hyper liquid, like they've had that hockey stick growth phase and now everybody's kind of caught up to their business model. Um, yeah. So I think, I think they're in a difficult position.

**Tyler** (00:49:25): It's funny that you're like, they caught up to their business model. It's like the same as this model that FTX had. Yeah. And then the same business model that like, you know, finance had before them and, uh, yeah.

**Chris** (00:49:39): Bitfinex before the, um, their business model of issuing perps on a decentralized platform

**Tyler** (00:49:47): or, or, yeah, the bit, the bit access to leverage and per trading opportunities with the least amount of compliance that you can get away with until you become big enough that then it becomes a problem that you have to scramble to, um, fix.

**Chris** (00:50:02): Yeah. It's Bitmax a hundred percent I'm with you.

**Tyler** (00:50:07): And like it always catches up with those venues. I mean, like it doesn't, it doesn't cause like history has shown that's a great trade. Yeah. All of those people, even when they get caught, like CZ went to jail for like a year and he's like one of the world's richest people. Um, that's probably a trade that like, if you're looking at that history, nobody's looking at that and they're like, ah, yeah, you probably learned his lesson. That wasn't worth it. They're like, Oh, I would take that deal. Let me be next.

**Jackson** (00:50:33): Yeah. Would you go to jail for a year to be rich, like to have a hundred million dollars?

**Tyler** (00:50:38): Yeah. Like white collar jail, like obviously it's not even jail.

**Chris** (00:50:44): Like Arthur Hayes got house arrest.

**Tyler** (00:50:45): Yeah. He was like probably like skiing the whole house arrest in like Jackson hole.

**Jackson** (00:50:51): Yeah.

**Chris** (00:50:52): It's like taking his ankle bracelet to Erewhon to buy like a $40 smoothie. Like it's, I don't think he was that punished. Um, those smoothies are so good for $23 is unbelievable. Yeah.

**Jackson** (00:51:07): Okay. Well, we'll see, we'll see a hyper liquid. If you can out compete Robin hood and the other income, not incumbents, but established trading platforms as they choose to adopt perks because all of us want to lose our money as fast as possible. Also crazy that he said they have like institutions using her, uh, hyper liquid. I guess there may be just suckling the money out of suckers like us going 25 X long.

**Tyler** (00:51:36): But yeah, obviously like you create a trading venue, the most sophisticated people are going to come and fleece the non-sophisticated people.

**Jackson** (00:51:43): If there's non-sophisticated people to fleece, add that to the purple fortune, uh, prompt Chris, don't get fleeced by the institutions.

**Chris** (00:51:53): Yeah.

**Tyler** (00:51:54): Our little scorecard here and reflecting very well on us.

**Chris** (00:51:58): Do not trade with winter mute. Do not counterparty winter mute. No jump capital.

**Jackson** (00:52:03): Why is the purple fortune all red right now? So sad blood bath out here. Um, the Bitcoin one went to zero. Yeah. Okay. So purple fortune wins out today, but I will admit the Bitcoin one was more captivating. I was on the edge of my seat for that one. Uh, but that concludes the pod for today. Thank you all for coming. Watching us lose $29 and discuss vulnerabilities, uh, Chris, Tyler, do you have any farewells to send to our guests? Yeah.

**Chris** (00:52:40): There are a lot of vulnerabilities out there.


