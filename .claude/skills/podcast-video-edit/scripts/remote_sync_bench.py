#!/usr/bin/env python3
"""Fully-remote episodes: build sync.html — the HUMAN sync bench. THIS IS THE
GROUND TRUTH STEP: file metadata offsets are only a starting hint (Ep 5's
creationdate was off by 26s-3.5min); a host drags the waveforms until the
group claps sound like ONE hit, then exports the offsets JSON back to the
agent. Run it for EVERY remote episode before any editorial work.

usage: python3 remote_sync_bench.py <workdir> [clapT1 clapT2 ...]
needs: <workdir>/offsets.json (initial guesses), audio/<track>_16k.wav,
       sources.json. Builds webaudio/<track>.m4a if missing (browser playback).
clap args = approximate master times for jump buttons (default 30).
"""
import json, os, subprocess, sys, wave
import numpy as np

WORK = sys.argv[1]
CLAPS = [float(a) for a in sys.argv[2:]] or [30.0]
os.chdir(WORK)
OFF = json.load(open('offsets.json'))
SRC = json.load(open('sources.json'))
TRACKS = list(SRC['tracks'].keys())
REF = min(TRACKS, key=lambda nm: abs(OFF.get(nm, 0)))  # locked reference row

PALETTE = ['#ffd24a', '#6fd3c7', '#c9a6ff', '#ff9e6f', '#8fd36f', '#6f9eff']
people = []
for nm in TRACKS:
    p = SRC['tracks'][nm]['person']
    if p not in people:
        people.append(p)
COLOR = {nm: PALETTE[people.index(SRC['tracks'][nm]['person']) % len(PALETTE)]
         for nm in TRACKS}

os.makedirs('webaudio', exist_ok=True)
env, dur = {}, {}
for nm in TRACKS:
    if not os.path.exists(f'webaudio/{nm}.m4a'):
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y',
                        '-i', f'audio/{nm}_16k.wav', '-c:a', 'aac', '-b:a', '96k',
                        f'webaudio/{nm}.m4a'], check=True)
    w = wave.open(f'audio/{nm}_16k.wav', 'rb')
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    dur[nm] = round(len(x) / 16000, 2)
    H = 2000  # 8 Hz envelope
    n = len(x) // H
    e = np.clip(np.abs(x[:n * H]).reshape(n, H).max(axis=1) * 3, 0, 1)
    env[nm] = [round(float(v), 2) for v in e]

T0 = min(min(OFF.get(nm, 0) for nm in TRACKS) - 60, -60)
T1 = max(OFF.get(nm, 0) + dur[nm] for nm in TRACKS) + 60
clap_btns = ''.join(
    f'<button class="mini" onclick="seek({t - 2:.0f})">clap ~{int(t) // 60}:{int(t) % 60:02d}</button>'
    for t in CLAPS)

html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Sync Bench</title><style>
body{font-family:-apple-system,sans-serif;margin:0;background:#111;color:#eee}
#top{position:sticky;top:0;background:#181818;padding:10px 14px;z-index:10;display:flex;gap:8px;align-items:center;flex-wrap:wrap;border-bottom:1px solid #333}
button{background:#333;color:#eee;border:0;border-radius:6px;padding:8px 12px;cursor:pointer}
button.primary{background:#ffd24a;color:#111;font-weight:700}
#tl{position:relative;overflow-x:scroll;background:#141414}
#tlinner{position:relative}
.row{position:relative;height:64px;border-bottom:1px solid #222}
.rowlabel{position:sticky;left:6px;top:4px;font-size:12px;color:#bbb;z-index:4;display:inline-block;background:#141414aa;padding:1px 4px;border-radius:4px}
.clip{position:absolute;top:14px;height:46px;border-radius:5px;cursor:grab;opacity:.95}
.clip canvas{width:100%;height:100%;border-radius:5px}
.clip.dragging{opacity:.6;cursor:grabbing}
#ruler{position:relative;height:22px;border-bottom:1px solid #333}
.tick{position:absolute;top:0;font-size:10px;color:#777;border-left:1px solid #333;padding-left:2px;height:22px}
#playhead{position:absolute;top:0;bottom:0;width:1px;background:#ff5c5c;z-index:6;pointer-events:none}
.ctl{display:flex;gap:4px;align-items:center;font-size:11px;color:#aaa}
#out{width:420px;height:36px;background:#101010;color:#9f9;border:1px solid #333;font-size:10px}
.mini{padding:3px 6px;font-size:11px}
</style></head><body>
<div id="top">
  <button class="primary" onclick="playPause()" id="pp">▶ Play</button>
  __CLAPBTNS__
  <span class="ctl">zoom <input type="range" min="2" max="40" value="8" id="zoom" oninput="setZoom(+this.value)"></span>
  <span class="ctl" id="tdisp">t = 0.0s</span>
  <button class="primary" onclick="exportOffsets()">✓ Confirm alignment</button>
  <textarea id="out" placeholder="offsets JSON appears here (auto-copied) — paste back to the agent"></textarea>
</div>
<div id="tl"><div id="tlinner"><div id="ruler"></div><div id="rows"></div><div id="playhead"></div></div></div>
<div style="padding:10px 14px;color:#888;font-size:12px">
Drag a waveform left/right to shift that recording (Shift-drag = fine, 10ms/px). Per-track: M mute · S solo · ±100ms nudge.
__REF__ is the reference (locked). Use the clap buttons: when aligned, each clap sounds like ONE hit, not an echo.
</div>
<script>
const OFF0 = __OFF__;
const DUR = __DUR__;
const ENV = __ENV__;
const COLOR = __COLOR__;
const TRACKS = __TRACKS__;
const REF = "__REF__";
let off = {...OFF0};
let PX = 8;
const T0 = __T0__, T1 = __T1__;
let playing=false, t=0, rafId=null, lastTs=0;
const audios={}, muted={}, solo={};
for(const nm of TRACKS){
  const a=new Audio('webaudio/'+nm+'.m4a'); a.preload='auto'; audios[nm]=a; muted[nm]=false;
}
const rows=document.getElementById('rows'), inner=document.getElementById('tlinner');
function x(sec){return (sec-T0)*PX}
function sec(px){return px/PX+T0}
function build(){
  inner.style.width=x(T1)+'px';
  const ruler=document.getElementById('ruler'); ruler.innerHTML='';
  for(let s=Math.ceil(T0/60)*60;s<T1;s+=60){
    const d=document.createElement('div');d.className='tick';d.style.left=x(s)+'px';
    d.textContent=(s<0?'-':'')+Math.floor(Math.abs(s)/60)+':'+String(Math.abs(s)%60).padStart(2,'0');
    ruler.appendChild(d);
  }
  rows.innerHTML='';
  for(const nm of TRACKS){
    const r=document.createElement('div');r.className='row';
    const lbl=document.createElement('span');lbl.className='rowlabel';
    lbl.innerHTML=nm+' <button class="mini" onclick="muted[\\''+nm+'\\']=!muted[\\''+nm+'\\'];sync(true)">M</button>'+
      '<button class="mini" onclick="toggleSolo(\\''+nm+'\\')">S</button>'+
      '<button class="mini" onclick="nudge(\\''+nm+'\\',-0.1)">−100ms</button>'+
      '<button class="mini" onclick="nudge(\\''+nm+'\\',0.1)">+100ms</button>'+
      ' <span id="off_'+nm+'">'+off[nm].toFixed(2)+'s</span>';
    r.appendChild(lbl);
    const c=document.createElement('div');c.className='clip';c.id='clip_'+nm;
    c.style.left=x(off[nm])+'px';c.style.width=(DUR[nm]*PX)+'px';c.style.background=COLOR[nm]+'33';
    c.style.border='1px solid '+COLOR[nm];
    const cv=document.createElement('canvas');cv.width=Math.min(16000,DUR[nm]*PX);cv.height=46;
    c.appendChild(cv); drawEnv(cv,nm);
    if(nm!==REF) enableDrag(c,nm);
    r.appendChild(c); rows.appendChild(r);
  }
}
function drawEnv(cv,nm){
  const g=cv.getContext('2d');g.clearRect(0,0,cv.width,cv.height);
  g.fillStyle=COLOR[nm];
  const e=ENV[nm], n=e.length;
  for(let px=0;px<cv.width;px++){
    const i=Math.floor(px/cv.width*n);
    const h=Math.max(1,e[i]*44);
    g.fillRect(px,(46-h)/2,1,h);
  }
}
function enableDrag(el,nm){
  let sx=0,so=0,fine=false;
  el.addEventListener('mousedown',e=>{
    sx=e.clientX;so=off[nm];fine=e.shiftKey;el.classList.add('dragging');
    const mv=ev=>{const d=(ev.clientX-sx)*(fine?0.01:1/PX);off[nm]=+(so+d).toFixed(2);
      el.style.left=x(off[nm])+'px';document.getElementById('off_'+nm).textContent=off[nm].toFixed(2)+'s';};
    const up=()=>{el.classList.remove('dragging');window.removeEventListener('mousemove',mv);window.removeEventListener('mouseup',up);sync(true)};
    window.addEventListener('mousemove',mv);window.addEventListener('mouseup',up);
  });
}
function nudge(nm,d){off[nm]=+(off[nm]+d).toFixed(2);
  document.getElementById('clip_'+nm).style.left=x(off[nm])+'px';
  document.getElementById('off_'+nm).textContent=off[nm].toFixed(2)+'s';sync(true)}
function toggleSolo(nm){solo[nm]=!solo[nm];sync(true)}
function audible(nm){
  const anySolo=Object.values(solo).some(v=>v);
  return !muted[nm] && (!anySolo || solo[nm]);
}
function sync(force){
  for(const nm of TRACKS){
    const a=audios[nm], lt=t-off[nm];
    const inR=lt>=0&&lt<DUR[nm]&&audible(nm);
    a.volume=audible(nm)?1:0;
    if(playing&&inR){
      if(a.paused) {a.currentTime=lt; a.play();}
      else if(force||Math.abs(a.currentTime-lt)>0.08) a.currentTime=lt;
    } else if(!a.paused) a.pause();
  }
}
function tick(ts){
  if(!playing)return;
  if(lastTs) t+=(ts-lastTs)/1000;
  lastTs=ts;
  document.getElementById('playhead').style.left=x(t)+'px';
  document.getElementById('tdisp').textContent='t = '+t.toFixed(1)+'s';
  if(Math.floor(ts/500)!==Math.floor((ts-16)/500)) sync(false);
  rafId=requestAnimationFrame(tick);
}
function playPause(){
  playing=!playing;lastTs=0;
  document.getElementById('pp').textContent=playing?'⏸ Pause':'▶ Play';
  if(playing){sync(true);rafId=requestAnimationFrame(tick);}
  else{for(const nm of TRACKS)audios[nm].pause();cancelAnimationFrame(rafId);}
}
function seek(s){t=s;document.getElementById('playhead').style.left=x(t)+'px';
  document.getElementById('tl').scrollLeft=x(t)-300;sync(true);
  document.getElementById('tdisp').textContent='t = '+t.toFixed(1)+'s';}
document.getElementById('ruler').addEventListener('click',e=>{
  const r=document.getElementById('tlinner').getBoundingClientRect();
  seek(sec(e.clientX-r.left));
});
function setZoom(z){const keep=t;PX=z;build();seek(keep);}
function exportOffsets(){
  const o=document.getElementById('out');
  o.value=JSON.stringify(off);o.select();document.execCommand('copy');
}
build();
</script></body></html>"""
html = (html.replace('__CLAPBTNS__', clap_btns)
            .replace('__OFF__', json.dumps({nm: OFF.get(nm, 0.0) for nm in TRACKS}))
            .replace('__DUR__', json.dumps(dur))
            .replace('__ENV__', json.dumps(env))
            .replace('__COLOR__', json.dumps(COLOR))
            .replace('__TRACKS__', json.dumps(TRACKS))
            .replace('__REF__', REF)
            .replace('__T0__', f'{T0:.0f}').replace('__T1__', f'{T1:.0f}'))
open('sync.html', 'w').write(html)
print('sync.html built —', {nm: dur[nm] for nm in TRACKS},
      f'(reference: {REF}; open in a browser, align, Confirm, paste offsets back)')
