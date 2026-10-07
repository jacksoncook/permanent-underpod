# Host souls

These are transcript-grounded writing profiles for simulating **Permanent Underpod**
from an episode outline:

- [Jackson](jackson/soul.md): energetic emcee, hands-on AI builder, provocative
  audience proxy, and the show's Korea-market lens.
- [Chris](chris/soul.md): self-deprecating systems explainer who follows liquidity,
  incentives, coordination, and the engineering underneath a claim.
- [Tyler](tyler/soul.md): dry premise-checker, Bitcoin/privacy advocate, and patient
  technical explainer who also gives an imperfect product credit where deserved.

Read all three for a three-host episode. Their shared slang is less distinctive
than their reasoning, timing, and responses to one another. They can change their
minds and agree on a good point; they are not three fixed positions in a debate.

Created **2026-10-07**, from the corpus available at main **`c34fa87`**, through
episode 17. No earlier `soul.md` files were found in the checkout or tracked
history. These profiles synthesize the hosts' public, on-show personas. They do
not claim access to private beliefs, supply current facts, or authorize voice
cloning or publication.

## Use with an outline

Supply the three files, the outline, and a separate factual brief. The outline
sets the topics and sequence; the brief supplies dated claims, numbers, product
behavior, and links. The souls supply conversational voice and characteristic
questions. A historical take can inform a reaction without becoming an assertion
that a product or market still works that way today.

Example prompt:

```text
Write an explicitly fictional Permanent Underpod conversation using the attached
Jackson, Chris, and Tyler soul.md files.

OUTLINE:
<segments, main question and stakes of each, desired duration or word budget,
 any requested public recurring bits>

FACTUAL BRIEF:
<dated facts, sources, uncertainties, and any approved hypothetical assumptions>

Follow the outline, while allowing short tangents, interruptions, questions,
corrections, and callbacks. Jackson usually introduces the stakes and hands off;
Chris traces mechanisms and incentives; Tyler tests premises and trust claims.
Let expertise and the particular topic change who leads. Avoid equal-length
round-robin speeches: mix quick reactions with occasional sustained explainers.

Preserve each host's qualifiers and genuine concessions. Express inferred
reactions as fictional dialogue, not authenticated quotations. The profiles'
dated opinions are characterization; the factual brief is the source for factual
claims. If neither supplies a needed detail, omit it, ask a question in dialogue,
or mark it as uncertain. Do not invent current prices, executed trades, research,
personal incidents, private messages, family details, or new affiliations.

Use slang and familiar public bits lightly. An exaggerated leverage joke is a
joke, not financial advice or evidence of a real bet. Do not copy AI-host inserts
from old transcripts. Do not fabricate accents, vocal acoustics, or biographies.
No host represents an employer.

Output labelled dialogue: Jackson: / Chris: / Tyler:. Start with
"Fictional transcript — generated from an outline; not an actual recording."
```

For a thin outline without a factual brief, generate questions, hypothetical
tradeoffs, and reactions at the level the supplied material supports. These files
are ready for text generation; an audio/video pipeline is a separate task.

## Corpus and attribution

All available episode transcript sets were reviewed across the three host passes,
with a separate pass over episode 17 and source-only material. Duplicate formats
were compared rather than counted as additional observations.

| Material | Treatment |
| --- | --- |
| Episodes **4–6, 8–11, 13–16** | Read the 11 attributed Markdown transcripts and surrounding dialogue. Their spoken bodies match the corresponding SRTs after removing labels and normalizing whitespace; the unlabelled SRTs in 4–6 repeat this speech too. |
| Episodes **1–3** | Read the complete speech; each CSV's utterances match its SRT. There are no speaker labels. Use explicit self-introductions, named handoffs, and coherent stretches cautiously; otherwise retain ensemble context. Episode 1's stored source clock does not match the published chapter clock. |
| Episode **4** source CSV | Reviewed the alternate raw transcription and material outside the final transcript. Raw timestamps differ from the final cut; spelling/filler differences and production chatter do not establish new traits. |
| Episode **7** | Read both Jackson-only SRT takes and the condensed Markdown/quality notes. The takes are separate versions, not two independent instances of every repeated point. The documented silence hallucination is excluded. |
| Episodes **5, 6, 8** `session.md` | Read each host's source-session speech to check attribution and corroborate nuance. These clocks differ from the final-cut transcripts; overlapping remote turns, recording chatter, and ASR loops require caution. Off-air/private anecdotes are excluded from the profiles. |
| Episode **17** | Read the complete final SRT. It is unlabelled. Explicit introductions/handoffs and editorial segment notes support qualified attribution, not a confident label for every interjection. Raw `shots.json` times must not be joined directly to final SRT times. |
| Episode **12** | No transcript is present. |
| Episode **18** | Prep/outline only at this revision; no transcript to analyze. |

The episode 1 word-level CSV is an alignment representation of the same speech,
not additional dialogue. Links in the profiles point to the stored transcript;
their accompanying timestamps identify passages within that file, not guaranteed
published-video times.

Excluded evidence includes `AI Hosts`, `AI Jackson`, `AI Chris`, `AI Tyler`,
`Gemini`, and other inserted/non-host voices. Episode 4 explicitly warns that
live interjections during clone playback may inherit clone labels; that mixed
playback range is unsuitable for confident host-specific quotation. Some other
speaker blocks also span multiple people, so a label alone does not prove every
word belongs to that host. Repeated cold opens, transcription misspellings, and
near-silence hallucinations are not recurring personality signals.

## Refresh and fidelity checks

When new transcripts arrive, read the new real-host speech in context, compare
it with existing themes, and update dated preferences or genuine revisions.
Add evidence for a new trait; avoid making one hot take a permanent worldview.
Retain useful contradictions: adoption can matter alongside sovereignty,
experimentation alongside privacy, and safety concern alongside coordination
skepticism. A host being absent is not evidence of a change in voice.

Before using a generated episode, check:

- Can each host be recognized from the reasoning and conversational moves even
  after removing names and catchphrases?
- Does Chris sometimes caveat or revise, Tyler sometimes explain or praise, and
  Jackson sometimes ask a basic question or accept a correction?
- Are the turns responses to one another, with uneven lengths and actual handoffs?
- Are precise facts grounded in the brief, and invented personal history absent?
- Is the result labelled fictional, with historical jokes kept distinct from
  advice or claimed real events?

The source links make the synthesis auditable. They are evidence anchors, not a
claim that a generated episode has already been validated by the real hosts.
