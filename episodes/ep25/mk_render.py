import json
CL = json.load(open('clips.json')); OV = json.load(open('overlays.json'))
R = json.load(open('render.json'))
def blk_start(b): return next(c['final_start'] for c in CL if c['block'] == b)
def to_final(b, m):
    for c in CL:
        if c['block'] == b and 'm0' in c and c['m0'] - 0.01 <= m <= c['m1'] + 0.01:
            return c['final_start'] + (m - c['m0'])
    raise SystemExit(f"unmapped {b} {m}")
TRANS = [('COLD_B', -0.15), ('COLD_C', -0.15), ('COLD_D', -0.15), ('INTRO', -0.3), ('CHAIN_A', -0.3), ('PERP', -0.3),
         ('FT_A', -0.3), ('WEB_A', -0.3), ('ENCL', -0.3), ('RUMOR', -0.3), ('OUTRO', -0.3)]
LIKES = [('OPENR_A', 82.0), ('FT_A', 1532.5), ('OUTRO', 3404.3)]
sfx, anim = [], []
for b, lead in TRANS:
    cut = blk_start(b)
    sfx.append({'file': 'sfx_whoosh.wav', 'block': b, 'offset': lead})
    anim.append({'file': 'wipe.mov', 'start': round(cut - 0.18, 3), 'end': round(cut + 0.22, 3), 'x': 0, 'y': 0})
sfx.append({'file': 'sfx_sting.wav', 'block': 'CARD_END', 'offset': 0.0})
for b, m in LIKES:
    s = to_final(b, m)
    if abs(to_final(b, m + 6) - s - 6) > 0.02:
        print(f"WARNING likesub {b} {m}: window crosses a splice")
    for o in OV:
        if o['start'] < s + 6 and o['end'] > s:
            raise SystemExit(f"likesub {b} {m} collides with {o}")
    sfx.append({'file': 'sfx_likesub.wav', 'block': b, 'offset': round(s - blk_start(b), 3)})
    anim.append({'file': 'likesub.mov', 'start': round(s, 3), 'end': round(s + 6, 3), 'x': 0, 'y': 0})
    print(f"likesub {b} master={m} final={s:.1f} ({int(s//60)}:{s%60:04.1f})")
anim.sort(key=lambda a: a['start'])
R['sfx'] = sfx; R['anim'] = anim
json.dump(R, open('render.json', 'w'), indent=1)
total = CL[-1]['final_start'] + CL[-1]['dur']
print("total", round(total, 1), f"({int(total//60)}:{total%60:04.1f})", "whoosh", sum(s['file'] == 'sfx_whoosh.wav' for s in sfx),
      "wipes", sum(a['file'] == 'wipe.mov' for a in anim), "likesub", sum(s['file'] == 'sfx_likesub.wav' for s in sfx),
      sum(a['file'] == 'likesub.mov' for a in anim))
