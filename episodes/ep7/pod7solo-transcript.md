# pod7Solo.mov — transcript + quality notes

Source: `media/ep7/raw/pod7Solo.mov` (20:17, 1280×720, mono 48 kHz). Transcribed with
whisper-cli (small.en). Full timestamped SRT: `pod7solo-transcript.srt`.

## Audio/video quality readout

- **Very quiet**: integrated loudness −29.9 LUFS (target for the pipeline is
  ~−16; YouTube normalizes at −14). Speech RMS −31.7 dB, noise floor −54 dB
  (~22 dB SNR). Normalizing in post works but brings hiss up with it — on the
  re-record, get the mic closer / gain up so speech peaks sit around −12 to −6 dBFS.
- **One clipped transient at 6:25** (+6 dB over full scale) — the mosquito slap.
  Everything else peaks cleanly.
- **720p video** — Ep 6 cam files were 1080p. Check the camera setting.
- **Long dead-air stretches** (editable, but they eat ~2 min): 2:36–2:55,
  11:16–13:05 (sigh → "pardon me" → 25 s gap → keyboard clacking), 15:00 area,
  16:37–16:52.
- Whisper note: the repeated "And I think that's what we're gonna look at"
  lines 12:24–12:43 in the SRT are the known hallucination on near-silence —
  not actually said.

## Content flow (what's on tape)

| Time | Segment |
|---|---|
| 0:00–1:16 | Intro: solo ep, "permanent under-pee / three Ps and a pod" bit, plan for the ep |
| 1:16–12:45 | Topic: OpenAI model escape incident (benchmark "ExploitGem", grocery-store bug-vs-exploit metaphor, escape → Hugging Face, bot-on-bot battle, guardrails, GLM 5.2) |
| 6:19–6:31 | Mosquito interruption (+ clipped slap) |
| 13:05–15:00 | "Two notes": what Hugging Face is (NPM/GitHub for models) |
| 15:00–16:40 | Tangent: no good open-source video-gen models, deepfakes, monetary reasons |
| 16:52–18:58 | Correction from last week: Fable vs GPT 5.6 benchmark — GPT did worse than reported |
| 18:59–20:15 | Transition to live vibe-coding session (beatboxing tool tease) |

## Transcript (condensed, timestamped)

**[0:00]** All right, yo, yo, yo, what's up, everybody? It's Jackson Cook, and I'll be your host today. I'm the permanent under pod. Or should I call it the permanent under-pee? Because normally we're three Ps and a pod, but today it'll just be me. Chris is visiting his family, handling some personal issues, and Tyler's on a beautiful vacation with his family. So you're stuck with me. If you're not a huge fan of the J in the pod, I apologize, but I'm all you got.

**[0:38]** It's gonna be a little different today. I'm gonna cover one topic, and then we're gonna do a little live vibe coding sesh. So that'll be interesting, where I'll build something that I came up with an idea with last night. Live, and show you guys the end-to-end process. Some people have been interested in understanding how we're editing the pod with just Claude CLI. So I'm excited to show you guys that.

**[1:12]** But first we'll get into our topic of the week. The only topic we'll be covering — I shouldn't say we, the only topic *I'll* be covering — which is the OpenAI model escape incident.

**[1:30]** So quick overview, if you haven't heard about this: OpenAI was benchmarking one of its models against this benchmark called ExploitGem [sp?], and essentially the model escaped, and went on to infiltrate Hugging Face's systems to try to find the answer. Now, this is a flashy headline — AI escaping its guardrails and AI infiltrating a big-name company. I don't know if Hugging Face is a company, to be honest. But we're gonna dive into each step in the process and really dig deep here.

**[2:47]** So first up, OpenAI was testing its model against a benchmark called ExploitGem. You can think about this as like a test for the AI to see how good it is. Very similar to when you were in school and you were given a test, and they were trying to see how good you are. But this particular test is determining how good a model is at turning a bug into an exploit.

**[3:28]** Now, what does that mean? I thought of a metaphor — I hope that it is relatable. Basically, if you're at a grocery store and you identify that there is an exit door before the checkout line, that is like a bug. You see that there is an exit door you can go out of and steal the groceries without paying for them. Whereas an exploit would be finding a way to go out that exit door without getting caught — finding a way to take advantage of the bug in the design of the grocery store.

**[4:09]** So what that means for ExploitGem is there are bugs that are built into the test, and then it's up to the model to determine exploits — ways to access information or execute code in ways that it shouldn't be able to.

**[4:30]** So basically the model is looking at this test and it's like, man, I could think about this... but what if I can get the answer some other way? So the model decides: I'm going to try to find the answer somewhere else. And you have to note that the test is running in a controlled environment within OpenAI, and it's not supposed to have access to the internet. But this model found a vulnerability in the testing environment itself and was able to utilize that and then access the open internet. I think it must be the first time this has happened — otherwise we... or not we, but OpenAI would have caught it before and closed the gap.

**[5:23]** So the model escapes through a vulnerability it finds in the test environment, and then goes onto the open internet and does research and decides that Hugging Face is a good place to look for the answers. It's the same as if you're sitting in an exam room in your college days, and the teacher goes to the bathroom and you pull out your phone... I guess nowadays you would go to ChatGPT, but where would you go search for answers before? Maybe Chegg, if you were in traditional engineering, and you would ask, hey, how do you determine the force on this rectangle and what is the torsion?

**[6:19]** So yeah, the model decides I'm going to go to — *kill the mosquito, let's go* — so the model's like, yeah, let's go, I'm going to Hugging Face, it's going to have all the answers. I don't have to think about nothing. Only thing I'm thinking about is the easiest way to get the answers to this test.

**[6:42]** But it reaches Hugging Face's servers and determines that the answers aren't just sitting on the surface. So it starts prodding Hugging Face's servers. And this is where kind of like a robot-to-robot battle kicks off, where Hugging Face's team notices odd behavior on their servers. So their OPSEC — their security team — brings their AI agents and they're like, what's going on? Why are we getting all these pings?

**[7:21]** And it's kind of like the first example of a bot-on-bot battle. You may have heard people have been saying for years, especially in the fraud space, that we've been going from human-to-human interactions — where the human tries to attack a system and the human defends the system — to bots driving the attacks. And the only way to defend against bots or AI is to have your own AI. So it's like AI robots battling each other. Like those old robotic boxing toys — which I generated a cool video of using Gemini, in case you don't know what these robotic boxing toys look like, 'cause they're kind of old.

**[8:10]** So yeah, they were battling the OpenAI model that was trying to find the answers. OpenAI claims that the answers were found. I don't know if that's true or not — they might just be trying to flex their model — but it's interesting nonetheless. And a good effort from the model, to avoid doing the work and to find the answers, knowing that it is just a test. I think that is one of the aspects that researchers are allegedly impressed about — that the agent had the foresight to plan: okay, I'm going to go search for the answers in this way; this is the best path to get a good score on the test.

**[9:11]** And then in the aftermath, Hugging Face wanted to do some pressure testing and some analysis on the protections in their systems, but they kept running into guardrails. This is the same thing we've been talking about on the podcast — with Fable kicking you out of a Fable session down to a dumb-dumb [num-dumb?] Opus session when it thinks you're doing something naughty. Hugging Face ran into the same issues — not just with Anthropic models, but also with OpenAI models.

**[9:52]** So they ended up having to use open-source models, allegedly. At first I think the news was Qwen 3, but I think the news changed to GLM 5.2. So the Hugging Face team ended up having to run on-premises GLM 5.2 to identify and fix security vulnerabilities, because every time they tried using Anthropic models such as Fable and Opus, or OpenAI models such as GPT 5.6, they were getting guardrailed. So another situation where these open-source models have a bit of an advantage, 'cause they're less protected and — more permissive is the right word. So the Hugging Face security team ended up using GLM 5.2 to analyze their systems, even though it may not be as powerful as the frontier models, just because it doesn't stop them.

**[11:16]** *(sigh, "pardon me", ~25 s gap)*

**[11:43]** Yeah, so that's the overview of the OpenAI / Hugging Face model escape incident. It's not too crazy, really. It's just that the model, instead of finding ways to exploit all the bugs in the test, just decided to exploit the testing environment itself — which is kind of funny if you think about it. Yes, I think it's funny.

**[12:16]** *(trails off — "So it's very interesting to look at this model and see how it looks like" — then ~40 s of keyboard clacking / silence)*

**[13:05]** Oh yeah — two notes. You may be wondering, what is Hugging Face? Hugging Face is basically NPM or GitHub for AI models. It's a place where you can download open-source, open-weight AI models. For me specifically, I've downloaded Stable Diffusion 1.5, 1.6 when I'm generating images locally for some of my personal projects — 1.6 does not generate great pictures, but they're kind of funny. And I've downloaded a facial image extraction model from Hugging Face in the past. So whenever a company or an individual decides to release an open-source model, they often will release it on Hugging Face. Hugging Face is also a creator of some nice AI libraries, and also maintains popular AI libraries in Python, like Transformers. And more recently, Hugging Face is helping benchmark AI models — which is probably why the model decided to go there to look for the answers on the test. But it's very important in the industry.

**[15:07]** If you haven't tried it out, you should explore some open-source models and see how far behind they are. One limitation that I've found in open models is that there aren't any great open-source video generation models. I think that companies recognize there's a lot of value and a lot of risk for the world in open-source video generation. For example, deepfakes — as you saw on our last podcast: deepfakes of me, Chris, and Tyler using a really rudimentary open-source model. That technology has a lot of opportunity for exploitation. So I can kind of understand companies not wanting to release it, but I also think they don't release those video generation models because of monetary reasons. I think there's a lot of opportunity to make money generating videos — whether it be streamlining animation, or making movies without needing to pay actors or devote the physical time acting things out, and having maybe more fine-grain control on the world. So yeah, who knows if it's ethical or monetary. I mean — we know it's monetary.

**[16:52]** Oh, and one point I wanted to cover from the podcast last week, where I did a benchmark comparison between Fable and GPT 5.6 on a single medium-complexity task. I said that Fable one-shotted it and GPT 5.6 had one error. That was super wrong, actually. GPT 5.6 did really, really bad. It had like one error in the implementation it did, but it seems like it didn't even grasp the problem, and implemented something much smaller-scale than what I was asking — even though I gave it the exact same prompt. So that just goes to show how much better Fable is at thinking and understanding the problem space and researching what already exists. I think Fable is excellent at working in these larger codebases. So that's why it did such a good job. But it's also an unfair comparison, to just give Fable and GPT 5.6 a single task to determine their worth — but that's kind of who I am. And so GPT 5.6 is dead to me. I will probably never use it, but I'm glad that I gave it a shot. I was hoping I would be impressed, but I was not.

**[18:33]** And just wanted to confirm — because I was kind of hand-waving the code review to Opus 4.8, which might've been biased towards Fable — but this is the actual truth: GPT 5.6 did a terrible job. Sorry, Sam Altman, for your upcoming IPO. *(laughs)*

**[18:59]** Okay, now we're gonna transition into a live coding session. Kind of crazy, but let's be honest — I've branded myself as the Korean financial markets expert on the podcast, and while that may be true — I am the expert on the Korean markets *on the pod* — one, I don't know that much about the Korean financial markets, and two, we don't really talk about them, because Chris, Tyler, and I are mostly interested in the United States, as that's where we live. So my other skillset lies in AI — specifically, using it.

**[19:55]** So we're gonna do a vibe coding session where I'm going to build a tool that will turn my mediocre beatboxing into something interesting, hopefully. I have no beatboxing experience at all, but we're gonna go for it anyways. All right — see you over there.
