#!/usr/bin/env python3
"""Fully-remote episodes, phase 4: render the multicam cutlist and assemble
with the anti-drift recipe (frame-exact clips, PTS-restamped video concat,
byte-concatenated PCM audio — same guarantees as cut_render.py). Also resolves
plan overlays/pips/sheet to FINAL time (overlays.json / pip.json / sheet.md).

usage: python3 remote_cut.py <workdir> <remote_plan.json>

Per piece: video = solo full-frame OR duo/trio side-by-side column crops
(720p sources crop natively: duo 640+640, trio 426+428+426, even widths only
— yuv420p rounds odd crops down; no scaling);
audio = every covering mic track, aligned, per-track equalization gain,
idle-mic attenuation (volume between() spans from the planner's VAD).

remote_plan.json extras used here:
  "overlays": [{"name":"lt_x","block":"B","m":123.0,"dur":6,"kind":"lt"},
               {"name":"st_ai","block":"AI","rel":1.5,"dur":12,"kind":"st"}],
  "pips":     [{"file":"/abs/screen.mp4","block":"B2","m0":2868.3,"m1":2872.5,
                "anchor":2868.0,"mode":"full"},        # anchor: file t0 == anchor
               {..., "mode":"corner", "crop":[1100,550,410,130]}],
  "sheet":    [{"label":"Cold open","block":"COLD1"},{"label":"X","block":"B","m":2867.0}]
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

WORK, PLAN_PATH = sys.argv[1], sys.argv[2]
PLAN = json.load(open(PLAN_PATH))
CL = json.load(open(os.path.join(WORK, 'cutlist.json')))
CLIPDIR = os.path.join(WORK, 'clips')
os.makedirs(CLIPDIR, exist_ok=True)

FPS, SR = 30, 48000
SPF = SR // FPS
IDLE_GAIN = PLAN.get('params', {}).get('idle_gain', 0.12)
WIDTHS = {3: [426, 428, 426], 2: [640, 640], 1: [1280]}


def vol_expr(active):
    terms = "+".join(f"between(t,{a:.2f},{b:.2f})" for a, b in active)
    if not terms:
        return f"{IDLE_GAIN}"
    return f"{IDLE_GAIN}+{1-IDLE_GAIN:.2f}*min(1,{terms})"


def render_piece(i, c):
    out = os.path.join(CLIPDIR, f"c{i:03d}.mov")
    if os.path.exists(out):
        return True
    n = max(1, round((c['m1'] - c['m0']) * FPS))
    samples = n * SPF
    dur = n / FPS
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    fc, vins = [], []
    panels = c['panels']
    ws = WIDTHS[len(panels)]
    for k, p in enumerate(panels):
        cmd += ["-ss", f"{p['src_start']:.3f}", "-t", f"{dur + 1.5:.3f}", "-i", p['file']]
        w = ws[k]
        x0 = max(0, min(1280 - w, int(p['cx'] - w / 2)))
        crop = "" if len(panels) == 1 else f",crop={w}:720:{x0}:0"
        fc.append(f"[{k}:v]fps={FPS},setpts=PTS-STARTPTS{crop},format=yuv420p[v{k}]")
        vins.append(f"[v{k}]")
    vtag = "[v0]"
    if len(panels) > 1:
        fc.append("".join(vins) + f"hstack=inputs={len(panels)}[vv]")
        vtag = "[vv]"
    atags = []
    for j, a in enumerate(c['audio']):
        cmd += ["-ss", f"{a['src_start']:.3f}", "-t", f"{a['dur'] + 0.5:.3f}", "-i", a['file']]
        idx = len(panels) + j
        d = int(a.get('pad_head', 0) * 1000)
        delay = f"adelay={d}:all=1," if d > 0 else ""
        fc.append(f"[{idx}:a]aresample={SR},atrim=0:{a['dur']:.3f},asetpts=PTS-STARTPTS,"
                  f"volume={a['gain']:.2f},volume='{vol_expr(a['active'])}':eval=frame,"
                  f"{delay}apad[a{j}]")
        atags.append(f"[a{j}]")
    if len(atags) > 1:
        fc.append("".join(atags) + f"amix=inputs={len(atags)}:duration=longest:normalize=0,"
                  f"atrim=end_sample={samples}[aout]")
    elif atags:
        fc.append(f"{atags[0]}atrim=end_sample={samples}[aout]")
    else:
        fc.append(f"anullsrc=r={SR}:cl=mono,atrim=end_sample={samples}[aout]")
    cmd += ["-filter_complex", ";".join(fc), "-map", vtag, "-map", "[aout]",
            "-frames:v", str(n), "-video_track_timescale", "30000",
            "-c:v", "h264_videotoolbox", "-b:v", "10M",
            "-c:a", "pcm_s16le", "-ar", str(SR), "-ac", "1", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL c{i:03d}", r.stderr[-300:])
        if os.path.exists(out):
            os.remove(out)
    return r.returncode == 0


def render_insert(i, c):
    out = os.path.join(CLIPDIR, f"c{i:03d}.mov")
    if os.path.exists(out):
        return True
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", c['insert']], capture_output=True,
                             text=True).stdout.strip())
    n = round(d * FPS)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                        "-i", c['insert'],
                        "-vf", f"fps={FPS},scale=1280:720,format=yuv420p",
                        "-frames:v", str(n),
                        "-af", f"aresample={SR},apad,atrim=end_sample={n * SPF}",
                        "-video_track_timescale", "30000",
                        "-c:v", "h264_videotoolbox", "-b:v", "10M",
                        "-c:a", "pcm_s16le", "-ar", str(SR), "-ac", "1", out],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("FAIL insert", r.stderr[-300:])
    return r.returncode == 0


jobs = [(i, c) for i, c in enumerate(CL) if 'card' not in c]
with ThreadPoolExecutor(max_workers=3) as ex:
    if not all(ex.map(lambda t: render_insert(*t) if 'insert' in t[1] else render_piece(*t), jobs)):
        sys.exit("some clips failed")

files = [os.path.join(WORK, c['card']) if 'card' in c else
         os.path.join(CLIPDIR, f"c{i:03d}.mov") for i, c in enumerate(CL)]

cum = 0.0
for c, p in zip(CL, files):
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip())
    c['final_start'], c['dur'] = round(cum, 3), round(d, 3)
    cum += d
print(f"final runtime: {cum/60:.2f} min")

concat_txt = os.path.join(WORK, "concat.txt")
with open(concat_txt, "w") as f:
    for p in files:
        f.write(f"file '{os.path.abspath(p)}'\n")


def clip_vframes(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=nb_frames", "-of", "csv=p=0", path],
                       capture_output=True, text=True).stdout.strip()
    if r.isdigit():
        return int(r)
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-count_frames", "-show_entries", "stream=nb_read_frames",
                        "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip()
    return int(r)


raw_audio = os.path.join(WORK, "_audio_cat.raw")
with open(raw_audio, "wb") as outf:
    for p in files:
        target = clip_vframes(p) * SPF
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error",
                        "-i", p, "-map", "0:a",
                        "-af", f"apad,atrim=end_sample={target}",
                        "-f", "s16le", "-acodec", "pcm_s16le",
                        "-ar", str(SR), "-ac", "1", "-"], stdout=outf, check=True)

# VIDEO: concat FILTER with per-input normalization, NOT the concat demuxer +
# -vf: heterogeneous SAR/color tags across clips (ProRes- vs h264-sourced cams,
# PNG-sourced cards) force a filtergraph reconfiguration at the mismatch
# boundary, which RESETS setpts' frame counter N -> the muxer then monotonic-
# fixes every frame to +1 tick (33us staircase; bit Ep 5). A video-only concat
# filter has no PTS corruption and no audio-padding drawback, and the single
# setpts instance after it can't reset.
clean_video = os.path.join(WORK, "_video_cat.mov")
fcs = os.path.join(WORK, "_concat_video.fcs")
with open(fcs, "w") as f:
    tags = []
    for k in range(len(files)):
        f.write(f"[{k}:v]setsar=1,setparams=range=tv:color_primaries=bt709:"
                f"color_trc=bt709:colorspace=bt709[v{k}];\n")
        tags.append(f"[v{k}]")
    f.write("".join(tags) + f"concat=n={len(files)}:v=1:a=0,setpts=N/{FPS}/TB[vout]\n")
vcmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
for p in files:
    vcmd += ["-i", p]
vcmd += ["-filter_complex_script", fcs, "-map", "[vout]", "-an",
         "-fps_mode", "passthrough", "-video_track_timescale", "30000",
         "-c:v", "h264_videotoolbox", "-b:v", "12M", clean_video]
subprocess.run(vcmd, check=True)
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-i", clean_video, "-f", "s16le", "-ar", str(SR), "-ac", "1",
                "-i", raw_audio, "-c:v", "copy", "-c:a", "pcm_s16le",
                os.path.join(WORK, "edited_raw.mov")], check=True)
os.remove(raw_audio); os.remove(clean_video)
json.dump(CL, open(os.path.join(WORK, "clips.json"), "w"), indent=1)

# ---- resolve plan overlays / pips / sheet to FINAL time ----
def to_final(block, m=None, rel=None):
    for c in CL:
        if c['block'] != block:
            continue
        if rel is not None:
            return c['final_start'] + rel
        if 'm0' in c and c['m0'] - 0.01 <= m <= c['m1'] + 0.01:
            return c['final_start'] + (m - c['m0'])
    cands = [c for c in CL if c['block'] == block and 'm0' in c and c['m0'] >= (m or 0)]
    return min(cands, key=lambda c: c['m0'])['final_start'] if cands else None

omap = []
for o in PLAN.get('overlays', []):
    ft = to_final(o['block'], o.get('m'), o.get('rel'))
    if ft is None:
        print("WARN unmapped overlay", o['name']); continue
    omap.append(dict(name=o['name'], kind=o.get('kind', 'lt'),
                     start=round(ft, 2), end=round(ft + o.get('dur', 6), 2)))
json.dump(omap, open(os.path.join(WORK, 'overlays.json'), 'w'), indent=1)

pips = []
for p in PLAN.get('pips', []):
    for c in CL:
        if c['block'] != p['block'] or 'm0' not in c:
            continue
        a, z = max(p['m0'], c['m0']), min(p['m1'], c['m1'])
        if z - a < 0.5:
            continue
        fstart = c['final_start'] + (a - c['m0'])
        pips.append(dict(file=p['file'], mode=p['mode'], crop=p.get('crop'),
                         t0=round(a - p['anchor'], 2),
                         start=round(fstart, 2), end=round(fstart + (z - a), 2)))
pips.sort(key=lambda x: x['start'])
# merge windows contiguous in BOTH final and source time (one input per run),
# then hide the PiP while any overlay is up (+0.3s margin), advancing t0 so the
# dashboard resumes at the right source moment
merged = []
for p in pips:
    q = merged[-1] if merged else None
    if (q and q['mode'] == p['mode'] and abs(p['start'] - q['end']) < 0.06
            and abs((p['t0'] - q['t0']) - (p['start'] - q['start'])) < 0.5):
        q['end'] = p['end']
    else:
        merged.append(dict(p))
cut_wins = [(o['start'] - 0.3, o['end'] + 0.3) for o in omap]
final_pips = []
for p in merged:
    segs = [(p['start'], p['end'], p['t0'])]
    for a, b in cut_wins:
        nx = []
        for s, e, t0 in segs:
            if b <= s or a >= e:
                nx.append((s, e, t0)); continue
            if a > s:
                nx.append((s, a, t0))
            if b < e:
                nx.append((b, e, t0 + (b - s)))
        segs = nx
    for s, e, t0 in segs:
        if e - s >= 1.0:
            final_pips.append(dict(file=p['file'], mode=p['mode'], crop=p.get('crop'),
                                   t0=round(t0, 2), start=round(s, 2), end=round(e, 2)))
pips = final_pips
json.dump(pips, open(os.path.join(WORK, 'pip.json'), 'w'), indent=1)

def fmt(s):
    s = int(round(s)); h, r = divmod(s, 3600); m, sec = divmod(r, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"

rows = []
for r in PLAN.get('sheet', []):
    t = to_final(r['block'], r.get('m'))
    if t is not None:
        rows.append((r['label'], t))
rows.sort(key=lambda r: r[1])
with open(os.path.join(WORK, 'sheet.md'), 'w') as f:
    f.write("| Time | Segment |\n|---|---|\n")
    for label, t in rows:
        f.write(f"| {fmt(t)} | {label} |\n")
print(f"wrote edited_raw.mov, clips.json, overlays.json ({len(omap)}), "
      f"pip.json ({len(pips)}), sheet.md")
