#!/usr/bin/env python3
"""Fully-remote episodes: render the PLANNED cut as a readable transcript
(final block order, mic filters and mutes applied) so the LLM can review
conversation flow BEFORE spending a render cycle. Run after remote_cutlist.py,
read the whole thing, fix the plan, repeat until it reads like a coherent show.

usage: python3 remote_preview.py <workdir>     ->  <workdir>/cut_preview.md

Reading guide (Ep 5 lessons):
- whisper line STARTS tile backwards over silence: a line shown missing at a
  block edge (or bleeding just before m0) is usually fine — verify the actual
  utterance with an energy scan before moving boundaries (remote_sync ideas).
- repeated identical lines are hallucinations on a near-silent own-voice track
  (collapsed here); they say nothing about the audio.
- WATCH FOR: meta lines that break an insert's illusion ("pretend we just
  watched it"), dangling sentence fragments at block starts, parallel-thread
  lines that contradict the edit's flow -> fix with boundaries, mics, or mute.
"""
import csv, json, sys

WORK = sys.argv[1]
OFF = json.load(open(f'{WORK}/offsets.json'))
SRC = json.load(open(f'{WORK}/sources.json'))
PERSON = {nm: t['person'].upper() for nm, t in SRC['tracks'].items()}
lines = []
for nm in OFF:
    with open(f'{WORK}/tx/{nm}.csv') as f:
        for r in csv.DictReader(f):
            txt = r['text'].strip()
            if not txt or txt == '[BLANK_AUDIO]':
                continue
            lines.append((float(r['start']) / 1000 + OFF[nm], nm, txt))
lines.sort()

cl = json.load(open(f'{WORK}/cutlist.json'))
seen = {}
out = []
cur = None
for c in cl:
    if c.get('block') != cur:
        cur = c.get('block')
        out.append(f"\n===== {cur} =====")
    if 'card' in c:
        out.append("  [card]")
        continue
    if 'insert' in c:
        out.append(f"  [insert: {c['insert']}]")
        continue
    mics = {a['track'] for a in c['audio']}
    for t, nm, txt in lines:
        if c['m0'] - 0.3 <= t <= c['m1'] and nm in mics:
            key = (nm, txt)
            if seen.get(key, -1e9) > t - 30 and len(txt) < 60:
                seen[key] = t
                continue
            seen[key] = t
            out.append(f"  {PERSON[nm]:8s} ({t:7.1f}): {txt}")
open(f'{WORK}/cut_preview.md', 'w').write("\n".join(out))
print(f"wrote {WORK}/cut_preview.md ({len(out)} lines) — READ IT before rendering")
