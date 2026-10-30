import json
CL = json.load(open('clips.json')); OV = json.load(open('overlays.json')); PIP = json.load(open('pip.json'))
R = json.load(open('render.json'))
def blk_start(b): return next(c['final_start'] for c in CL if c['block'] == b)
def to_final(b, m):
    for c in CL:
        if c['block'] == b and 'm0' in c and c['m0'] - 0.01 <= m <= c['m1'] + 0.01:
            return c['final_start'] + (m - c['m0'])
    raise SystemExit(f"unmapped {b} {m}")
def contiguous(b, m, dur):
    return abs((to_final(b, m + dur) - to_final(b, m)) - dur) < 0.02
trans = [('COLD_D', None, -0.15), ('COLD_A', None, -0.15), ('COLD_C', None, -0.15), ('INTRO', None, -0.3),
         ('PERP_A', None, -0.3), ('PERP_C', 783.9, -0.3), ('COHERE', None, -0.3), ('INTERLUDE', None, -0.3),
         ('SAEZ', None, -0.3), ('SAT', None, -0.3), ('SAT_B', 3623.5, -0.3)]
cards = [('c_cohere', 12, 'COHERE', 372.0), ('c_7702', 12, 'PERP_C', 921.0), ('c_drain', 12, 'PERP_C', 1042.0),
         ('c_nonce', 12, 'PERP_C', 1085.0), ('c_freeze', 10, 'PERP_C', 1133.0), ('c_audit', 14, 'SAEZ', 2156.0),
         ('c_curves', 14, 'SAT', 2760.0), ('c_clauses', 16, 'SAT', 2822.0), ('c_reduce', 12, 'SAT', 2861.0),
         ('c_eth', 14, 'SAT', 2888.0), ('c_pnp', 14, 'SAT', 3062.0)]
sfx, anim = [], []
for b, m, lead in trans:
    cut = blk_start(b) if m is None else to_final(b, m)
    sfx.append({'file': 'sfx_whoosh.wav', 'block': b, 'offset': round(cut + lead - blk_start(b), 3)})
    anim.append({'file': 'wipe.mov', 'start': round(cut - 0.18, 3), 'end': round(cut + 0.22, 3), 'x': 0, 'y': 0})
sfx.append({'file': 'sfx_sting.wav', 'block': 'CARD_END', 'offset': 0.0})
bath = blk_start('BATH')
anim.append({'file': 'wipe.mov', 'start': round(bath - 0.18, 3), 'end': round(bath + 0.22, 3), 'x': 0, 'y': 0})
for name, dur, b, m in cards:
    assert contiguous(b, m, dur), (name, b, m)
    s = to_final(b, m)
    for o in OV:
        if o['start'] < s + dur and o['end'] > s and o['file'].startswith('lt_'):
            raise SystemExit(f"card {name} collides with lower third {o}")
    anim.append({'file': f'cards/{name}_{dur}.mov', 'start': round(s, 3), 'end': round(s + dur, 3), 'x': 0, 'y': 0, 'hide_logo': True})
    print(f"card {name} final={s:.1f} ({int(s//60)}:{s%60:04.1f})")
total = CL[-1]['final_start'] + CL[-1]['dur']
def clear(s):
    if any(o['start'] < s + 6 and o['end'] > s for o in OV): return False
    if any(s - 1 < p['start'] < s + 7 for p in PIP): return False
    if any(a['start'] < s + 7 and a['end'] > s - 1 for a in anim): return False
    return True
def place_like(target):
    best = None
    for c in CL:
        if 'm0' not in c: continue
        if c['block'].startswith('COLD') or c['block'].startswith('CARD') or c['block'] == 'BATH': continue
        for s in [c['final_start'] + k * 0.5 for k in range(int(c['dur'] * 2))]:
            if s + 6 > c['final_start'] + c['dur'] - 0.3: break
            if abs(s - target) > 120: continue
            if clear(s) and (best is None or abs(s - target) < abs(best - target)): best = s
    if best is None: raise SystemExit(f"no likesub window near {target}")
    return best
likes = [place_like(120.0), place_like(total / 2), place_like(total - 150.0)]
for s in likes:
    c = next(c for c in CL if 'm0' in c and c['final_start'] - 0.01 <= s < c['final_start'] + c['dur'])
    b = c['block']
    sfx.append({'file': 'sfx_likesub.wav', 'block': b, 'offset': round(s - blk_start(b), 3)})
    anim.append({'file': 'likesub.mov', 'start': round(s, 3), 'end': round(s + 6, 3), 'x': 0, 'y': 0})
    print(f"likesub {b} master={c['m0'] + s - c['final_start']:.1f} final={s:.1f} ({int(s//60)}:{s%60:04.1f})")
anim.sort(key=lambda a: a['start'])
R['sfx'] = sfx; R['anim'] = anim
json.dump(R, open('render.json', 'w'), indent=1)
print("total", round(total, 1), f"({int(total//60)}:{total%60:04.1f})", "whoosh", sum(s['file']=='sfx_whoosh.wav' for s in sfx),
      "wipes", sum(a['file']=='wipe.mov' for a in anim), "cards", sum('cards/' in a['file'] for a in anim),
      "likesub", sum(s['file']=='sfx_likesub.wav' for s in sfx), sum(a['file']=='likesub.mov' for a in anim))
for a in anim:
    if a['file'] == 'wipe.mov': print("wipe", a['start'])
