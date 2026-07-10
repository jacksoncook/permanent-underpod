#!/usr/bin/env python3
"""Turn-based rebuild, step 2: sequence turns into solo BEATS for the
discussion windows. Serialization by turn start: overlapping speech plays one
turn after another (conversation-flow order), never stacked.

Rules:
- windows: only turns whose midpoint falls in a rebuild window
- drop backchannels: text empty/short-ack AND dur < 2.5s
- drop turns in DROP (curation, by index into turns.json)
- merge consecutive same-person turns with source gap < 2.0s
- each beat: cam/mic = the speaker only; boundaries padded 0.30s
Writes beats.json (consumed by gen_cutlist.py).
"""
import json, re

turns = json.load(open('turns.json'))
WINDOWS = [  # (label prefix, lo, hi) in master seconds
    ('V', 306.0, 1232.0),     # Venice reaction .. engineer-in-a-box
    ('P', 1528.0, 1762.0),    # P2/P3 (DRAM, DoD, Opus roast)
    ('U', 1788.0, 2629.0),    # USDC chain drift
    ('B', 2820.0, 3358.0),    # BonkDAO
]
# curated exclusions/moves matched by (person, m0 within 0.6s) — stable keys.
# DROPS: mumbles, empty-energy turns, truncated duplicate fragments, cut topics
DROPS = [
    ('tyler', 310.4), ('jackson', 331.1), ('tyler', 337.9), ('jackson', 341.0),
    ('jackson', 399.5), ('jackson', 494.8), ('chris', 525.8), ('jackson', 703.3),
    ('chris', 800.3), ('chris', 941.8), ('chris', 993.0), ('chris', 1061.8),
    ('chris', 1527.1), ('chris', 1544.9), ('chris', 1568.2), ('jackson', 1587.8),
    ('jackson', 1739.3), ('jackson', 1791.0), ('chris', 1793.9), ('chris', 1979.4),
    ('jackson', 2097.2), ('chris', 2188.6), ('chris', 2204.8), ('chris', 2229.0),
    ('tyler', 2233.8), ('chris', 2315.2), ('chris', 2341.4), ('tyler', 2417.5),
    ('tyler', 2437.9), ('chris', 2506.9), ('chris', 2576.7), ('jackson', 2817.6),
    ('jackson', 2827.6), ('jackson', 2910.9), ('tyler', 3014.1), ('tyler', 3019.6),
    ('jackson', 3118.9), ('chris', 3142.4), ('tyler', 3157.9), ('chris', 3214.1),
    ('chris', 3225.0), ('chris', 3354.9),
    # round 2 (from cut_preview read): dangling fragments & duplicate echoes
    ('tyler', 931.46), ('tyler', 948.53), ('jackson', 1005.58),
    ('jackson', 1565.93), ('chris', 2032.22),
]
# MOVES: (person, m0, new sort key) — thread untangling: Voorhees history
# completes before the local-models thread; questions precede answers;
# the two-gigs sidenote becomes the segue into the P1 clap
# TRIMS: (person, m0, new_m0) — cut a turn's head (pre-window meta fragments)
TRIMS = [
    ('chris', 298.9, 308.5),   # start at "Okay, that's crazy...he's literally me"
]
MOVES = [
    ('jackson', 597.5, 833.0),   # "we respect you + second question: local models"
    ('jackson', 690.6, 834.2),   # "Quinn 3 and GLM 4.7 ... run locally"
    ('jackson', 717.0, 835.0),   # "on an M2 and an M5..."
    ('jackson', 735.2, 836.0),   # "my computer is 10 grand"
    ('jackson', 760.8, 838.0),   # "maybe just paying Venice is the way"
    ('jackson', 1049.7, 1016.5), # "fable has been blocking me"
    ('jackson', 1071.5, 1017.5), # "rate limiting both...wasting my time"
    ('jackson', 1094.3, 1230.0), # two-gigs sidenote -> V-section closer
    ('jackson', 1817.8, 1808.0), # "Chris wrote a sexy blog post..." before explainer
    ('jackson', 2074.9, 2030.0), # cash-out question before Chris echoes it
    ('chris', 2424.3, 2400.5),   # "final standard" before the ENS gag
    ('tyler', 2444.8, 2442.0),   # "fire sale prices?" before "they got did done"
    ('jackson', 2534.0, 2523.0), # revolver question before "standout architecture"
    # round 2: complete Tyler's split sentence; Q's before their answers
    ('tyler', 686.2, 665.5),     # "against him for operating Shapeshift..."
    ('jackson', 2861.68, 2820.0),# "what does DAO mean?" before Chris's explainer
    ('jackson', 3092.2, 3081.0), # "able to exit with USD?" before the answer
]

BACKCHANNEL = re.compile(
    r"^\s*((yeah|yes|yep|yup|okay|ok|right|sure|no|wow|hmm+|mm+|so|and|exactly|totally|"
    r"jeez|boom|correct|true|nice|got it|i see|oh|oh,? (yeah|wow|okay)|that's crazy|"
    r"that's true|thank you)[.!?,\s]*)+$", re.I)

def in_window(t):
    mid = (t['m0'] + t['m1']) / 2
    for lab, lo, hi in WINDOWS:
        if lo <= mid <= hi:
            return lab
    return None

# spans already covered by hand-crafted beats (person-scoped: only Tyler's
# pretend-line lives in V0 — Chris talks through that span legitimately)
HANDLED = [('tyler', 324.4, 331.0)]

def matches(lst, t):
    for entry in lst:
        if entry[0] == t['person'] and abs(entry[1] - t['m0']) < 0.6:
            return entry
    return None

beats = []
for i, t in enumerate(turns):
    lab = in_window(t)
    if lab is None or matches(DROPS, t):
        continue
    if any(p == t['person'] and a < t['m1'] and b > t['m0'] for p, a, b in HANDLED):
        continue
    tr = matches(TRIMS, t)
    if tr:
        t = dict(t, m0=tr[2])
    mv = matches(MOVES, t)
    t = dict(t, key=mv[2] if mv else t['m0'])
    dur = t['m1'] - t['m0']
    if True:
        txt = t['text'].strip()
        if not txt and dur < 4.0:
            continue
        if BACKCHANNEL.match(txt) and dur < 2.5:
            continue
        if re.search(r"(keyboard clicking|keyboard clacking|Chris laughing|"
                     r"Chris chuckling|Chris sniffs|\(laughs\)|\(silence\)|"
                     r"\(chuckles\))", txt) and len(txt) < 40 and dur < 4.0:
            continue
        # whisper hallucination loops
        words = txt.lower().split()
        if len(words) > 6 and len(set(words)) <= max(4, len(words) // 4):
            continue
    beats.append(dict(idx=i, label=lab, person=t['person'], key=t['key'],
                      m0=t['m0'], m1=t['m1'], text=t['text']))

beats.sort(key=lambda b: b['key'])
# merge consecutive same-person beats with small source gap
merged = []
for b in beats:
    q = merged[-1] if merged else None
    if (q and q['person'] == b['person'] and q['label'] == b['label']
            and 0 <= b['m0'] - q['m1'] < 2.0):
        q['m1'] = b['m1']
        q['text'] = (q['text'] + ' ' + b['text'])[:400]
    else:
        merged.append(dict(b))
beats = merged

out = []
for k, b in enumerate(beats):
    out.append(dict(id=f"{b['label']}T{k:03d}", m0=round(b['m0'] - 0.30, 2),
                    m1=round(b['m1'] + 0.30, 2), cam=b['person'],
                    mics=[b['person']], text=b['text']))
json.dump(out, open('beats.json', 'w'), indent=1)
tot = sum(b['m1'] - b['m0'] for b in out)
print(f"{len(out)} beats, {tot/60:.1f} min "
      f"({sum(1 for b in out if b['cam']=='chris')} chris / "
      f"{sum(1 for b in out if b['cam']=='jackson')} jackson / "
      f"{sum(1 for b in out if b['cam']=='tyler')} tyler)")
