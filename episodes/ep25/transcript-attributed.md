# Transcript (person-attributed, final cut)

**Chris** (00:00:00): going around that somebody has potentially solved polynomial time factoring. So, yeah, I mean, this is a huge, huge, huge rumor. So basically, they use this vulnerability to execute code remotely on every other validator to pick up their key shares and reconstruct the volt signature. And then, of course, they just took the money.

**Jackson** (00:00:25): I'll be honest, I have put an API key into a model before. Well, I mean, like a million times. But Chris, what are we looking at today with the perp a fortune? The place where you and I stake 100 United States dollars to try to escape the permanent underclass while Tyler's ghost coin flips Bitcoin to either gain 25 or

**Insert** (00:00:48): lose $25.

**Jackson** (00:00:55): Good morning, good night. This is Jackson Cook, and we are on the underpod.

**Chris** (00:01:03): With me, Chris.

**Jackson** (00:01:05): With Chris, but no Tyler because Tyler has a family while Chris and I, we live lives alone. No thanksgivings for us. No turkey to pardon. Exactly.

**Chris** (00:01:18): That's what you guys do, right? You pod in the turkey. Is that real?

**Jackson** (00:01:22): I don't know what pardoning the turkey is, but I just throw the turkey in the trash because it doesn't taste good. But we're jumping straight into it with our first topic, and this is open router, open router. So pardon me, an external company basically seeded API tokens through all the models that open router provided and then found that four of the backing providers were leaking the API keys. When months later, the API keys were being queried. So on two fronts, why are these model providers storing the prompts? And then also how are the API tokens getting released? What do you think about this? Have you ever put an API key or a secret into a model? Be honest.

**Chris** (00:02:21): This actually makes me really nervous, so I don't think I've used open router for this specifically, although it's possible. I definitely have against models, not that claim ZDR, but that claim that they're being run in a T, which I think gives you some slight amount more privacy guarantees. I think this is a failure mode of the router model in terms of inference providers. So if you're going to a lab, you trust them to not leak your stuff. Maybe a lab employee could inside job your credentials, but it feels less likely. But in this case, with open router, it's a contract, the ZDR, the zero daughter retention. So you're kind of trusting everyone to be suitable, I guess. Is that your read?

**Jackson** (00:03:15): Yeah, I mean, exactly. I guess you feel like an implicit trust with these models and maybe un-technical people don't even know what they're doing. So they're just throwing API tokens in and expecting that to be safe. I agree that I feel a lot more comfortable putting my API tokens to anthropic directly and would be more hesitant with open router where you've got open router servers routing to... I don't know how transparent it is, what it's routing to. So I also have never used open router, but I'll be honest. I have put an API key into a model before. About me, like a million times. If it's just that question,

**Chris** (00:03:55): yeah, like a million times. But on open router, I really specifically tried not to because I was skeptical.

**Jackson** (00:04:04): And how would you define open router, I guess?

**Chris** (00:04:08): So I would say it's kind of a routing layer on top of inference providers. So open router has relationships with people who are providing these models, like model inference via a series of contracts, and they basically forward the compute onto you and they skim a clip off the top. So they might offer, for example, deep seek before flash at 15 cents per million tokens. And then they will try to get you the best deal on that via all of their inference providers. And they'll route your prompt basically based on who is serving compute for the lowest price at that time.

**Jackson** (00:04:45): That's what I figured. So it's not for us that they're trying to route the lowest provider. It's for them because that's their profit, right?

**Chris** (00:04:54): Yeah, I think it's a bit of both, but I think that pricing is, yeah, it's always more about that.

**Jackson** (00:05:00): Okay. Well, I looked into the four backing model providers that have these leaks. Also, I want to mention the company that exposed this vulnerability. I think it's called Dragos or Dragos. Have you heard of this company?

**Chris** (00:05:19): Never heard of them, no.

**Jackson** (00:05:21): Okay. Well, good on them for putting... It's basically like they put a little bit of cheese on a mousetrap and the bad actors walked on directly onto them. So I guess I'm going to walk through the four ways that people's API keys were exposed or at least supposedly exposed. One of the companies allegedly has a security agent that visits URLs that are put into prompts sent to it. And they're claiming that their security agent was hitting these URLs and pinging the API tokens basically. And since they've turned that off, and this company also admitted they were not respecting zero data retention and they were still storing these prompts and running these security checks on the prompts. So now they're allegedly respecting the zero data retention policy flag. Another one was storing the prompts and hugging face. And they committed an API secret of their own to GitHub for like one day and then took it back. And then a month later they saw that somebody accessed those logs using that key. And that's how they got access to the API tokens. One of them didn't really describe it, but they said they leaked two API keys at some point. And an attacker found them and accessed the stored security logs. So all of these companies are claiming these are logs for security or for auditing. And then the fourth said they had a legacy internet connected service that was basically taken over. And somebody spun up a containerized virtual machine that had full credential access and used that to query the prompt logs.

**Chris** (00:07:31): So they're saying that they got hacked and somebody was looking at the provider's own logs of every prompt. That's what they're saying.

**Jackson** (00:07:40): Yeah, they got super hacked. The committing your own API key to GitHub is kind of like getting hacked a little bit too

**Chris** (00:07:48): because somebody had to be like, yeah, for sure.

**Jackson** (00:07:52): And that's like one of the things that's interesting. Like all four of these, I don't know, they were exposed at the same time by this one company. I do wonder, is it one group that's going through all the open router model providers and looking for holes to find these API keys? I guess we haven't proven that anybody is using these API keys maliciously, but they definitely could have. And that information is yet to be shown.

**Chris** (00:08:23): Yeah, I think so much of this at this point is about trust. I think this has always been the cut of my jib with serving models out of tees. It kind of protects everyone. Obviously, you can't see into the tee, so it can be harder to debug things about specifically the model. But in a lot of these cases, if these models were faithfully served in a tee, and I understand there's whole attestation pipelines and stuff to set that up properly, but if they were right, there's no way that somebody would be able to hack in and then snoop detailed logging of the prompts.

**Jackson** (00:09:07): Unless no one needed to be taught, but don't put your API tokens into your models. Or if you do, just maybe minimize the number of trusted parties down to just you and anthropic. Not security advice,

**Chris** (00:09:22): but I think your tier ranking should be frontiers, tee, and then anything below that line, you should not be giving credentials to. And even everything above that line, you should be rotating the credentials if you share them, like after the model has used them. That's my personal opinion here. I will also say one password has an MCP, one password which has been recently hacked, but we don't have to talk about that. So you can authorize every login and every credential access if you are using it with a model. I've found that quite useful. That's my whole tip.

**Jackson** (00:10:01): Yeah, good tip. I agree with your hierarchy. So you're saying you trust Venice or Maple more with your three API keys than OpenRider, as would I, since it's one company versus at least two.

**Chris** (00:10:16): Venice is still routing to providers, but only to providers that serve their model out of a trusted execution environment. So I don't trust ZDR at all. Like I just assumed that's fake. Yeah.

**Jackson** (00:10:29): I guess like how much trust do they have? You know, does Venice have with these model providers? Like it could be like this one. I can't remember the name. It was like Minimax. Yeah, Minimax said they were doing ZDR and then they weren't. So is it the same for Venice? Does Venice use Minimax? Because then we would know.

**Chris** (00:10:49): Right. I think Minimax is domiciled in China. And I think it raises the question of like, if you have a contract with an entity and they breach it, like who is going to sue them? Like who's enforcing the ZDR? And my understanding is like in reality, probably no one.

**Jackson** (00:11:08): Yeah, I guess now we need a trustless way to enforce ZDR. I don't know how to do that. Maybe somebody with cryptographic background could hook us up with that.

**Chris** (00:11:20): Yeah, some crazy zero knowledge moon maps might be on the

**Jackson** (00:11:23): ground. Zero knowledge witness encryption.

**Chris** (00:11:26): Yeah, yeah.

**Jackson** (00:11:27): Multilinear map. I don't know, crazy lingo. Anyways. Yeah, that was crazy. Be careful with your credentials, everybody, or you might lose a lot of money. Moving on, Chainflip. Chainflip looks like it's some sort of coin swapping protocol and it was hacked. Chris, break it down. How did they lose $12 million?

**Chris** (00:11:57): All right. So this one's obviously very up my alley. So Chainflip is a decentralized exchange. So it's a DeFi protocol that lets you swap between native assets. So native Bitcoin on Bitcoin with native Ethereum on Ethereum. It's basically very similar to another protocol called ThorChain. And the way these protocols operate is they create sort of a signature between a number of parties, like a shared wallet, through something called a threshold signature scheme, which is just sort of a way of saying this is a wallet where if N of M participants or if 15 of 20 participants sign a message, you can move funds. So basically, it's kind of like building a version of Binance, but instead of CZ having the keys, you know, 20 or 150 people have the keys and money can only move when they all agree. So this was like really a novel thing back in 2021. Now it's like a little bit less novel. So Chainflip is one of these. And yeah, basically with this type of protocol, you have to both generate a signature amongst people who don't trust each other. So in Chainflip's case, 150 people. And you also have to rotate the signature depending on certain conditions. So basically what happened here is Chainflip had custody of $12 million of funds, which they were using to process swaps. And they rotate the signature every 30 days. And what happened is somebody, the way that you can get into the signing set is by staking a certain amount of coins that will be removed if you cheat, basically. So if the other validators see you cheat, they take away your coins and it's supposed to penalize you for behaving badly. So basically someone staked these coins, which were worth a lot less than $12 million in order to get into the set. And then they exploited a zero day. What they're saying is a remote code execution vulnerability. So basically they use this vulnerability to execute code remotely on every other validator to pick up their key shares and reconstruct the vault signature. And then of course they just took the money. So a really crazy one here, because it wasn't the cryptography that was wrong. It was that there was a vulnerability in the network stack, which is to say the code that lets the validators talk to each other to construct the signature had an RCE. And yeah, that was it. So again, I think everybody needs to be very wary of their dependencies. It's the ones you don't look at that get you. So yeah.

**Jackson** (00:14:54): Yeah, that third party library, man. I mean, it crushed them. And I saw that on the Ethereum, they threw the Ethereum into tornado cash, mixed it up for the Bitcoin. They just got it out, irreversible. Good and bad, I guess, are mostly bad in the case of fraud and in the days of today where money is stolen every day. Yeah, so these guys are clever and apt. They're familiar with this, right?

**Chris** (00:15:23): For sure. I just think this is another case of one. So this dependency, which they were using for network communication to construct the signatures, that library hadn't been updated since November of 23. So basically anything that comes from the old world, like before language models, you absolutely cannot trust it, no matter if you think you can. But yeah, I just think there's a lot more of this coming. Yeah.

**Jackson** (00:15:58): Yeah, I mean, speaking of these libraries, a lot of the compromises we saw last week of the '13 were from third party libraries. The recent FBI and I believe CIA hacks were also related to an open source data monitoring library. So yeah, really audit your dependencies. I don't know if minimize is the right way to do it because I don't know, is open source even valuable anymore when you can rewrite the code with AI surety?

**Chris** (00:16:36): Totally. I don't know, this might be like an old head take here, but there used to be this JavaScript library called IsNegative as a joke, where all it would do is tell you if a number is negative. The funny thing about that is that that's a top line language feature. You would never need this thing. But they were trying to make a joke about how people use dependencies for everything, like the smallest stuff that they shouldn't. But I don't know, what do you think, Jackson? Do you think we end up just rewriting everything from scratch, vendoring it in, throwing models against it? I don't know. Because it seems like this is a real huge liability now, like supply chains.

**Jackson** (00:17:14): Yeah, and open source libraries. I mean, they definitely serve a purpose. I think as with everything, it'll land somewhere in the middle where some open source repositories will get the dedication they need to stay safe if they're critical enough to enough people. For example, like Bitcoin. But I'm sure there's others that are more or less prominent that are still very useful, maybe Numpy, for example. Yeah.

**Chris** (00:17:46): I think just in general, if you're running a security sensitive anything, like anything that touches money, you should be running an obliterated, even an open source obliterated model on it. Not using a NoZDR Chinese provider, not using open router. Like, find another place. But yeah, you absolutely should at least be trying to harden your software.

**Jackson** (00:18:10): Just heat your home with the tens of Blackwell 700, you know, Nvidia chips and run your own GLM 5.4 in your living room. But Chris, what are we looking at today with the perp of fortune? The place where you and I stake 100 United States dollars to try to escape the permanent underclass while Tyler's ghost coins lives Bitcoin to either gain 25 or lose $25.

**Chris** (00:18:43): What are we looking at today? I mean, let me share with you. I mean, we've already been talking about this. So this picture should be obvious, but I think what's conspicuous today is that I got Haiku to choose for us, which for those who don't know is Anthropics dumbest model. So for today, we have short XYZ Minimax. So Minimax was the open router provider that was leaking credentials or stealing credentials from people. And yeah, I mean, so far we are up 39 cents, which means Minimax is down some minute amount in after hours trading.

**Jackson** (00:19:26): All right. We're up huge 39 cents. Now we just need Tyler to lose on the Bitcoin down by Bitcoin rising from the ashes. Oh, it's 57 minutes.

**Chris** (00:19:39): Oh no. Oh, because it's on the hour. Yeah, it's still.

**Jackson** (00:19:45): Yeah. And we changed the pod time today. I see mistakes, mistakes by the squad. Apologies viewers. We'll be able to give enough.

**Chris** (00:19:55): Yeah. We'll try. We'll chime in on the result of this sorted affair though. We'll cut something in.

**Jackson** (00:20:02): Yeah. And just to clarify, Minimax is the one that said API tokens are not leaked. They had their own security agent probing them. And they were also the ones that said, we're not listening to the zero data retention flag that open router setting.

**Chris** (00:20:18): Which I mean, obviously they need to, that's an issue between open router and Minimax. Like they need to sort out like why that JavaScript toggle isn't hooked up or whatever's wrong there.

**Jackson** (00:20:31): I tried fine tuning inkling mini two on a MacBook Pro M5 with 128 gigabytes of RAM and two terabytes of SSD. And boy, did I not know anything about LLMs and do I barely know anything about LLMs now? Okay. I don't know.

**Chris** (00:20:55): I'm so curious about this one because I had a similar idea but didn't get around to it. And I think I know even less about like the actual practicality of LLMs than you do. So I'm going to use this as like a vicarious learning experience so that I can try myself.

**Jackson** (00:21:13): Yeah. So you talking about it inspired me and just made me really curious. So for those of you who don't know, inkling mini two is some like United States open source model and it's really small. I believe it's 28 gigabytes of space. So I picked it as an obvious choice to try some fine tuning. And my task was getting it to determine from a video when is tennis being played and when is tennis not being played? So I had a video.

**Chris** (00:21:47): It's like super simple.

**Jackson** (00:21:51): Is tennis happening or is it not? And I've used like a variety of like open source, like what do they call them? Computer vision library is like trying to solve this problem in the past but I hadn't like thrown a model at it itself. So I got the model and I ran it on the video. So like inkling too many can process video or process images. So the video is broken down into images and then passed in to the model and I got like a baseline and it was basically coin flipping is tennis happening or is it not happening? So it was pretty bad. And yeah, for fine tuning, I started trying to fine tune the entire model. So that's like updating the model weights but I don't have enough space on my machine and it also was taking like it just wouldn't stop. So I ended up going with a method called LoRa. LoRa is instead of like changing the entire weights matrices, instead you have like a tiny augmentation matrix and you slot it into layers to like basically shift the attention of the model and you kind of run it like you do a neural network where I had test data and then I run the LLM on the video and I see is it correct or is it not and then you back propagate the answer and update the weights.

**Chris** (00:23:41): These are separate LoRa weights that go in between the existing layers. Is that correct? That shift the attention. Okay, cool.

**Jackson** (00:23:49): Exactly and they're smaller matrices and I believe the matrices for Inkling 2 are like 2,000 something numbers by 2,000 and basically like I didn't have enough space to have a copy of those. So instead I did like a rank 8 LoRa matrix. So it's like 8 by 2,000 something numbers.

**Chris** (00:24:13): Got it.

**Jackson** (00:24:14): Yeah and actually got really really improved performance with only 200 like rounds of training. I also tried 400 and it was taking about what was it? One minute per 10 training runs. So pretty fast. So like 40 minutes for 400 training runs and I was able to get it up to 92% accuracy. That was pretty cool. Wow, sorry.

**Chris** (00:24:47): How long did this whole process of creating these LoRa layers take you and inserting them into the model like end to end?

**Jackson** (00:24:55): Well, I mean I used AI to build up the Python script. So using the library it was like super quick to actually set up and it's the training that took the most time. And also my computer was dying even though I had it plugged in. So it was definitely tough on my M5 Macs MacBook Pro. But then I learned something, a different strategy which is called probing. So this was another new thing which is basically like these models have so many layers. I believe there's 23 layers and including many too. And probing is just stopping in the middle and like stopping at those numbers and making a decision basically. So you have like that those 2000 numbers. So you create a 2000 dimensional space and then use your testing data to like fit what weights for these numbers creates this best split between like tennis being played and tennis not being played. And that was even better than the fine-tuned LoRa model. And yeah, I mean that was generally just pretty cool.

**Chris** (00:26:23): So sorry, with probing are you trying to find where in the matrix it has the best accuracy? So for viewers from home, like who aren't maybe that familiar with LLMs, basically the format of them is they're like these matrices which are stacked on top of each other. And like the activations pass through matrix to matrix until you get the final matrix at the end which forms the output of the large language model. So what you're saying Jackson, and again, not a language model expert, is you're stopping like at one of the matrices halfway through the model if that's more accurate than the final output or am I misunderstanding?

**Jackson** (00:27:03): Yeah, exactly. I tried stopping at four different layers in the 23-layer model found 11 to be the most effective. So just stopping in the middle because you think about it, the model starts with the image and then it has to encrypt the image data and it turns into numbers. And these numbers just keep blooming out. And so like the information is really rich in the middle not yet a word because at the end it turns into a word and like that convergence back towards a word kind of has a lossiness in the data. So yeah, and it's much cheaper because for each word in an LLMs output all 23 layers are being ran. But for probing you can just run it that first half time up to 11 and then it stops.

**Chris** (00:27:53): What was the accuracy at the 11th slice? Was it comparable to Laura?

**Jackson** (00:27:58): It was better than the Laura. So the Laura was I believe 91% and the slice at 11 of the probe was 93%. No way. Yeah, so I did some hand labeling of is this a tennis pointer, is it?

**Chris** (00:28:13): [Laughter]

**Jackson** (00:28:15): Which was a little bit annoying.

**Chris** (00:28:17): Jackson Tennis Bench, it got 93%.

**Jackson** (00:28:20): Yeah, I first tried getting Claude to label it, but actually Claude like Fable 5.2 is not that good either at knowing if the point is ongoing or not. So yeah, pretty surprised by the performance of this tiny model and it is now being slotted into my workflow for editing tennis videos because that combined with the previous audio detection I was using for like knowing if there's like a cadence of tennis ball hits going on, I'm actually getting really good cuts now. So this has been huge for my personal workflow.

**Chris** (00:28:53): Okay, so you found an actual real use to post train an open source model that has improved your life is what we're saying.

**Jackson** (00:29:00): I didn't post train it. I did probing, which doesn't alter the model at all. But yeah, I found like a way to alter an open source model and use one. Actually use one in a way that's like not shit because open source models are not really good normally, but maybe for specified use cases they can be.

**Chris** (00:29:22): I wonder, so like it makes me wonder like you remember when Jevification began, the great Jevification of models. It makes me wonder like what are the hidden use cases are out there for language models like probing I think is another example of like, you're kind of like slicing up the model and like making it do something that the entire model was not designed for.

**Jackson** (00:29:46): It's funny you mentioned the Jev too, because when I started doing the probing, I'm like this is insane. I'm like, oh my gosh, is this what Jev was doing? Is this what Jev is doing? Because I was basically structuring the output into a yes or no, like is it above this or below this line? Like a support vector machine, if you're familiar with that machine learning technique. And I'm like, is this what Jev is just doing? And it sounds like no, they're not just probing existing models. They like redesign the architecture to have like, to instead of mapping it into a word, they're mapping it into these structured outputs. But yeah, just a funny, like I did read up about Jev after learning about probing and it is different.

**Chris** (00:30:29): Yeah, but I'm saying like, would you Jevify a probed model?

**Jackson** (00:30:33): Would I Jevify a probed? Yeah, I mean, why not? Right. If it does what you want, if it gives you what you need.

**Chris** (00:30:42): Yeah, I just I wonder like all these like smaller use cases for language models where them being open and fast might make it better, cheaper. Yeah, I think that's really exciting.

**Jackson** (00:30:56): Yeah, and I also will say shout out to Chris, you sent me some sort of article about why Inkling Mini 2 was like the best for being like a super general. So it's like the best for being fine-tuned. That's why I chose it besides it being small.

**Chris** (00:31:11): Hell yeah. I'm glad it worked. That rules. There's hope for me yet.

**Jackson** (00:31:16): Yeah, definitely should try it. You could do it. But yeah, that concludes trying to post-strain or tune a model on my personal laptop, like heating up the entire apartment, computer growling. All right, and into it we go with Chris, how long does the web browser have to live? Because I think we're only a year or so away from saying goodbye to the web browser and interface and saying hello to either a voice-based interface with the internet or even a chatbot-based interface. What do you think?

**Chris** (00:31:59): So firstly, the internet browser is a piece of garbage. People have wanted to get rid of this since its inception, since Brendan Eich, Mozilla. So I don't think anyone will really mourn its passing. Maybe it'll come back in a quirky way like cassettes and records later down the line. But yeah, I 100% can see the end of the browser, for sure. But probably not this year or next year or maybe the year after.

**Jackson** (00:32:34): That's true. It'll take people a while to get over the hump. And as Tyler mentioned offline, the web companies themselves are going to fight this with all they have. For example, when Amazon kicked agents like Metas Muse off of their platform, that's like the old guard saying, "We're going to make this as hard as we can on you guys." But I think that the personal assistant agents like Instinct have proven that they can navigate around Captcha and they can solve whatever big web can throw at them.

**Chris** (00:33:15): I think there's this really big theme at the moment of everybody fighting for the top of the funnel. It seems like everybody wants to control the distribution. For example, Amazon has recently not been very friendly to MCPs for shopping. It's very difficult to get your agent to shop on Amazon. Ask me how I know. One of the pieces of conventional wisdom around that is that so much of Amazon's revenue comes from their web interface and showing people certain things and steering them in certain directions, dynamic pricing, et cetera. They really don't want to give that up. I think for this to happen, for the web browser to go away and for people to be convinced to basically expose their services to agents as the gateway, I think it's a political issue. I think these companies will have to negotiate whatever rev share splits, exclusivity agreements. I think in a lot of ways, this looks like what's happening with stablecoins. I think this is not a technical issue. I think everybody probably at this point thinks that agents will be or may be a better way to interact with most online services. I think my concern is how do you convince the people who already have these lucrative businesses to give up control, or will they? I mean, I guess they don't have to unless they're forced to.

**Jackson** (00:34:46): What I'm going to say is that they don't even have to consent. I think that the agents are clever enough to get around whatever guards they have. What does Amazon have that's more powerful? Do they have something worse than CAPTCHA that's blocking these agents? I guess you've tried, so what are they doing? How do they know it's not you and you're just struggling to drag the star onto the dartboard?

**Chris** (00:35:15): In my case, I was trying to do it out of an Intel TDX enclave hosted by Fala. I obviously didn't have a convincing browser fingerprint in order to convince Amazon that I was not actually a deep-sig model. But I'm sure people are doing this with codecs and Grokbot, where they can take control of your actual computer and do things for you. So I'm with you. I think the question is, will they be legally prohibited by the TOS? Will they prohibit the big labs from doing this stuff? And will that work? Will open source models eventually get good enough that they can do it as well? And then it's just like the game's off.

**Jackson** (00:36:01): I see. So you're suggesting that Amazon, for example, could do regulatory lobbying to try to stop companies from doing this, but open source agents, or open source models, may overcome this anyways, and then it's a moot point on paying to stop people from profiting from it.

**Chris** (00:36:22): I mean, that's how I envisaged that that would go down, but I really don't know at this point. All I know is that some people seem to be able to ask their agents to solve captions, and others cannot. And I don't know why.

**Jackson** (00:36:35): [Laughter] You've got to prove that agent, man. I guess, no, that's not the right use case repair.

**Chris** (00:36:45): You've got to post-train it into submission, obliterate it.

**Jackson** (00:36:49): Yeah, obliterate it. Yeah, once again, speaking of these personal assistant agents, I've gotten my 53-year-old father using it to help manage his calendar from his emails. And I used it to book another trip to Turkey, and it tried to spend $600 per ticket on a flight from Anatolia to Istanbul. That's like a domestic flight in Turkey that costs like $25 and runs like 30 times a day. So that's a word of caution that even though we love to trust our little geniuses on the computer, they might screw you sometimes. You've got to keep an eye out for those prices, man. And that's kind of where I wonder, Chris. Maybe that's where Amazon makes up the money. And as you've mentioned with the lottery system, maybe things just get bid up, things get more expensive, and that's where they make up their lost money on ads or monitoring.

**Chris** (00:37:52): Yeah, don't get me wrong. I think there are ways to make this profitable for those companies, but they are giving up the top of the funnel.

**Jackson** (00:38:03): Well, something's going to change, and we'll be around when it does, and we'll see who's right and who's wrong and who's still alive.

**Chris** (00:38:14): Yeah, we'll see how bad these takes truly are in the fullness of six months.

**Jackson** (00:38:21): And it'll be documented on the internet forever.

**Chris** (00:38:24): Yeah, infinitely legible. People will just be like, tell me about podcasts, takes, and then that's it. Well, I'll have to live with these takes forever.

**Jackson** (00:38:36): And just re-ran to change your name, change your face. Classic surgery and I'll be good. We got secure enclaves. We talk about teas all the time, but I don't know if we've ever explained them. And everybody wants to know more. Chris did a deep dive into teas, into secure enclaves. Chris, please educate me because I hear secure enclave and all I hear is I'm supposed to trust that there is a part of the device that Apple made for me that I can do stuff and they can't see it. Is that true?

**Chris** (00:39:13): Are we talking about on-device secure enclaves? I didn't prefer this.

**Jackson** (00:39:18): I thought they were all the same. Since it's a tiny computer, it's a big computer. What's the difference?

**Chris** (00:39:23): I think the upshot of most secure enclaves is basically that it does. So generally, the way they work is there is a chip next to the CPU that does-- it's like super fast at doing encryption. Normally, it's AES. So basically, at the hardware level, instead of having all of the memory in your RAM in clear text, it's all stored encrypted. And then it gets decrypted before it gets to your CPU and then encrypted on the way back. So in practice, what that means is that even if somebody has access to the machine that's running the code, it's almost impossible for them to see what's actually going on in the machine. They can't lift it off of memory. They can't lift it off of the hard drive. And it creates some security guarantees. And the only way to guarantee at least the code that is running on the secure enclave, which is traditionally the other way to get information out of a secure enclave, is to push the malicious code that exfiltrates it. It also can create an attestation that the thing that you've built is what's running on the secure enclave. So you at least can look at all the code that's running there and say, "Hey, there's nothing... Yeah, there's nothing nefarious going on there." I think signing enclaves on-device are very similar. In so far as they... In that case, there's a key that is... cannot be removed from the chip that does the signing. And that basically protects it from being exfiltrated. So the worst that can happen with an on-device secure enclave is that you sign something you didn't mean to, but there's no actual way to get the entropy and the big whatever it may be, 256-bit or bigger number out of the enclave and steal the key. So yeah.

**Jackson** (00:41:18): Okay. That's super cool. I guess when I was imagining secure enclave, I figured it was a separate partition on the desk of memory. But you're saying it's like an attachment to the CPU where most of the computations are ran that just encrypts ingress data and then decrypts it on egress. So only the CPU is seeing the actual raw data. Is that correct?

**Chris** (00:41:47): Off the dome, that is how, for example, a hardware secure enclave works, like an Intel TDX. There are other levels of secure... I believe they're called secure images, which live at that hypervisor layer, which are a little bit different. But I'm not about them. I haven't researched them very much. I just skipped straight to the hardware secure enclave.

**Jackson** (00:42:11): No, that's super cool. And then you even touched on on-device secure enclave. This is beautiful.

**Chris** (00:42:19): Should we talk about rumors that somebody has solved polynomial time factoring?

**Jackson** (00:42:27): Oh my gosh, Chris, I'm so sorry. I forgot about these rumors, but they're very important.

**Chris** (00:42:31): No, no, no, it's cool. I'd say maybe, you know, maybe they're just rumors and we shouldn't talk about it, but maybe it's real. I don't know.

**Jackson** (00:42:38): We can call this, since, you know, we'll call it the gossip corner. Preface this with we don't know if it's true or not. But what are people saying, Chris? What's the word on the secretes?

**Chris** (00:42:52): So there's a lot of like rumors going around that somebody has potentially solved polynomial time factoring. So what is factoring? Factoring is saying, here is a number. I need to find whether there are two primes that can create this number, basically. And this is the underpinning of various encryption algorithms, namely RSA, which is Rivest-Shimier something. It's a very old but very well-used public key encryption algorithm. So I think it's used for like websites, like old TLS, some code signing. It's different from elliptic curve cryptography. And basically, the rumor is that there's a way to do this factoring problem that underpins it in polynomial time, which if we remember from our P versus NP explainer, which we probably don't, polynomial time is like n squared. So it's slow but generally computable. The current solution for factoring I think is in sub-exponential time, which is an extremely long time. And we rely on it taking a long time to do this factoring, to do the encryption. So yeah, I mean, this is a huge, huge, huge rumor. I think if it's true, it has all of those implications we've talked about on other podcasts with responsible disclosure and whatnot. If it was true, you would maybe expect to see a lot of people desperately trying to upgrade their systems over Thanksgiving, stuff like that. So yeah, I don't know if it's true or not. I don't have any further information on it, but a lot of people are talking about it.

**Jackson** (00:44:39): Yeah, I just looked it up, so RSA is used for HTTPS, TLS, yeah, digital certificates. So that's definitely critical. It's not elliptic curve, so Bitcoin's still safe for now, but still worrisome and a crucial part of the internet. I wonder if those rumors are related at all to the recent proof of human hypothesis that basically bounds the, I believe, the number of prime numbers under a certain number. But it would make sense to me, being a non-mathematician, that knowing how many prime numbers are under a number would help you determine the prime factors of said number.

**Chris** (00:45:29): For sure. I think it's also some people, some commentators have noted that have not, I mean, have solved some incredible problems. Like, you know, we're talking about the Riemann hypothesis, Navier-Stokes, but there have been no released findings on cryptography, which some people think is suspicious. So there's some more fuel to that rumor. Again, whether it's true, like where I guess we'll find out in months, but yeah, maybe it is, maybe it's not.

**Jackson** (00:45:59): Our opinions are our own, and it is a rumor. We understand rumor, but it's exciting. So we want to toss it out there to the folks.

**Chris** (00:46:09): Just a fun thought experiment along the lines of, like, responsible disclosure that we've had in the past before.

**Jackson** (00:46:17): Yeah, yeah, it will be curious, but whatever it is they find that requires responsible disclosure happens, will we know, or, you know, how will it be presented? That will be exciting. Okie dokie. Well, this pod's releasing on a Thursday, which is different. So happy Thursday, everybody. Next time, Tyler should be back. He's our mathematician, so he can roast our takes on RSA.

**Chris** (00:46:44): I'm so excited. I'm so excited for that. That's it. [Laughter] I'm so pumped.

**Jackson** (00:46:53): I think he's also going to bring a little bit of talk on witness encryption, which is pretty cool, but Chris and I, it's out of our ballpark. So tune in next week, and we'll catch you later. Chris, say goodbye to them. Like and subscribe.

**Insert** (00:47:08): And press the bell button.

