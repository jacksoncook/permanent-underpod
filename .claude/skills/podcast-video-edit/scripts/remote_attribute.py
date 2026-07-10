#!/usr/bin/env python3
"""Fully-remote episodes: person-attributed transcript for the FINAL cut.

Attribution is free on remote episodes — each host has their own mic — so map
every cue of the final-cut SRT back to master time (via clips.json m0) and ask
each person's VAD who was speaking. Inserts (clips with no m0, e.g. an AI
video) get the label passed in remote_plan.json blocks ("attr") or "Insert".

usage: python3 remote_attribute.py <workdir> <final_cut.srt> <out_basename>
writes <out_basename>.srt (cues prefixed "Name: ") and <out_basename>.md.
"""
import json, re, sys, wave
import numpy as np

WORK, SRT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
cl = json.load(open(f'{WORK}/clips.json'))
OFF = json.load(open(f'{WORK}/offsets.json'))
SRC = json.load(open(f'{WORK}/sources.json'))
PERSON = {nm: t['person'] for nm, t in SRC['tracks'].items()}
PLAN = json.load(open(f'{WORK}/remote_plan.json'))
INS_LABEL = {b['id']: b.get('attr', 'Insert')
             for b in PLAN.get('blocks', []) if b.get('insert')}

VAD = {}
for nm in PERSON:
    w = wave.open(f'{WORK}/audio/{nm}_16k.wav', 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    n = len(x) // 160
    e = np.sqrt(np.mean(x[:n * 160].reshape(n, 160) ** 2, axis=1))
    thr = max(np.percentile(e, 10) * 6, 0.004)
    VAD[nm] = np.convolve((e > thr).astype(np.float32), np.ones(41), 'same') > 0

pieces = sorted((c for c in cl), key=lambda c: c['final_start'])

def who(a, b):
    """dominant speaker (title-cased person) for final-time window [a,b]."""
    votes = {}
    t = a
    while t < b:
        for c in pieces:
            if c['final_start'] <= t < c['final_start'] + c['dur']:
                if 'm0' not in c:
                    votes[INS_LABEL.get(c['block'], 'Insert')] = \
                        votes.get(INS_LABEL.get(c['block'], 'Insert'), 0) + 100
                    break
                m = c['m0'] + (t - c['final_start'])
                for nm, p in PERSON.items():
                    i = int((m - OFF[nm]) * 100)
                    if 0 <= i < len(VAD[nm]) and VAD[nm][i]:
                        votes[p.title()] = votes.get(p.title(), 0) + 1
                break
        t += 0.1
    return max(votes, key=votes.get) if votes else None

def ts(s):
    h, m, sec = s.split(':')
    return int(h) * 3600 + int(m) * 60 + float(sec.replace(',', '.'))

cues = re.findall(
    r'(\d+)\n(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)\n(.*?)(?:\n\n|\Z)',
    open(SRT).read(), re.S)
out_srt, out_md, last = [], [], 'Jackson'
for idx, a, b, text in cues:
    text = ' '.join(text.split())
    spk = who(ts(a), ts(b)) or last
    last = spk
    out_srt.append(f'{idx}\n{a} --> {b}\n{spk}: {text}\n')
    if out_md and out_md[-1][0] == spk:
        out_md[-1][2] += ' ' + text
    else:
        out_md.append([spk, a.split(",")[0], text])

open(f'{OUT}.srt', 'w').write('\n'.join(out_srt))
with open(f'{OUT}.md', 'w') as f:
    f.write('# Transcript (person-attributed, final cut)\n\n')
    for spk, a, text in out_md:
        f.write(f'**{spk}** ({a}): {text}\n\n')
print(f'{OUT}.srt / .md — {len(cues)} cues, {len(out_md)} turns')
