#!/usr/bin/env python3
"""Render channel-data.json + insights.json into a single branded HTML report.

usage:
  report.py channel-data.json insights.json out.html [--logo brand/logo-480.png]

The data file comes from yt_pull.py. The insights file is written by the
analyst (LLM/human) — schema in examples/insights.example.json. Charts use
Chart.js from CDN (needs network when the report is opened). The logo, if
given, is base64-embedded so the file stays self-contained.
"""
import base64
import html
import json
import os
import sys

YELLOW, DARK, PANEL, INK, MUT = "#FFD24A", "#0E0E13", "#17171f", "#f2f2f5", "#9a9aa8"
PRIO_COLOR = {"high": "#ff6b6b", "med": YELLOW, "low": "#7bd88f"}


def esc(s):
    return html.escape(str(s if s is not None else ""))


def fmt_min(m):
    return f"{m / 60:.1f} h" if m >= 90 else f"{m:.0f} min"


def fmt_dur(s):
    return f"{int(s) // 60}:{int(s) % 60:02d}"


def insight_cards(items):
    out = []
    for it in items:
        p = (it.get("priority") or "med").lower()
        out.append(f"""
        <div class="card">
          <div class="card-head"><span class="prio" style="background:{PRIO_COLOR.get(p, YELLOW)}">{esc(p.upper())}</span>
          <h3>{esc(it.get('title'))}</h3></div>
          <p class="evidence"><b>Evidence:</b> {esc(it.get('evidence'))}</p>
          <p class="rec"><b>Do:</b> {esc(it.get('recommendation'))}</p>
        </div>""")
    return "\n".join(out) or "<p class='muted'>none</p>"


def main():
    args = sys.argv[1:]
    logo_b64 = ""
    if "--logo" in args:
        i = args.index("--logo")
        p = args[i + 1]
        del args[i:i + 2]
        if os.path.exists(p):
            logo_b64 = base64.b64encode(open(p, "rb").read()).decode()
    data_p, ins_p, out_p = args[0], args[1], args[2]
    data = json.load(open(data_p))
    ins = json.load(open(ins_p))

    ch, videos = data["channel"], data["videos"]
    pub = [v for v in videos if v.get("privacyStatus") == "public"]
    longs = [v for v in pub if not v["is_short"]]
    shorts = [v for v in pub if v["is_short"]]
    watch_min = sum((v.get("analytics") or {}).get("watch_min", 0) for v in videos)
    avg_pct_long = (sum((v.get("analytics") or {}).get("avg_view_pct", 0) for v in longs) / len(longs)) if longs else 0

    # video bar chart (published only, chronological)
    bar_labels = [((v["publishedAt"] or "")[:10] + " · " + (v["title"] or "")[:38]) for v in pub]
    bar_views = [v["stats"]["views"] for v in pub]
    bar_colors = [YELLOW if not v["is_short"] else "#5aa9e6" for v in pub]

    daily = data.get("daily", [])
    day_labels = [d["day"] for d in daily]
    day_views = [d.get("views", 0) for d in daily]
    day_subs = [d.get("subscribersGained", 0) - d.get("subscribersLost", 0) for d in daily]

    ret_sets = []
    palette = [YELLOW, "#5aa9e6", "#ff6b6b", "#7bd88f", "#c792ea", "#f78c6c", "#89ddff"]
    for i, v in enumerate([v for v in longs if v.get("retention")]):
        ret_sets.append({
            "label": (v["title"] or v["id"])[:44],
            "data": [{"x": round(p["ratio"] * 100), "y": round((p["watch_ratio"] or 0) * 100, 1)}
                     for p in v["retention"]],
            "borderColor": palette[i % len(palette)],
            "pointRadius": 0, "borderWidth": 2, "tension": 0.3,
        })

    traffic = data.get("traffic", [])
    tr_labels = [t["insightTrafficSourceType"].replace("_", " ").title() for t in traffic]
    tr_views = [t.get("views", 0) for t in traffic]

    rows = []
    for v in sorted(videos, key=lambda x: x.get("publishedAt") or "9999", reverse=True):
        a = v.get("analytics") or {}
        r = v.get("reach") or {}
        impr = f"{r['impressions']:,}" if r else "–"
        ctr = f"{r['ctr_pct']:.1f}%" if r else "–"
        status = v.get("privacyStatus")
        badge = ("<span class='tag short'>short</span>" if v["is_short"] else "<span class='tag'>episode</span>")
        if status != "public":
            badge += f" <span class='tag sched'>{esc(status)}</span>"
        rows.append(f"""<tr>
          <td><a href="{esc(v['url'])}">{esc(v['title'])}</a> {badge}</td>
          <td>{esc((v.get('publishedAt') or v.get('publishAt') or '')[:10])}</td>
          <td>{fmt_dur(v['duration_s'])}</td>
          <td class="num">{impr}</td>
          <td class="num">{ctr}</td>
          <td class="num">{v['stats']['views']:,}</td>
          <td class="num">{a.get('avg_view_pct', 0):.0f}%</td>
          <td class="num">{fmt_dur(a.get('avg_view_s', 0))}</td>
          <td class="num">{v['stats']['likes']}</td>
          <td class="num">{v['stats']['comments']}</td>
          <td class="num">{a.get('shares', 0)}</td>
          <td class="num">{a.get('subs_gained', 0)}</td>
        </tr>""")

    logo_img = f'<img src="data:image/png;base64,{logo_b64}" alt="">' if logo_b64 else ""
    experiments = "".join(f"<li>{esc(e)}</li>" for e in ins.get("experiments", []))

    html_out = f"""<!doctype html><html><head><meta charset="utf-8">
<title>{esc(ch['title'])} — Channel Report</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>
<style>
  body {{ background:{DARK}; color:{INK}; font:15px/1.55 Arial, sans-serif; margin:0; }}
  .wrap {{ max-width:1180px; margin:0 auto; padding:28px 32px 80px; }}
  header {{ display:flex; align-items:center; gap:18px; margin-bottom:6px; }}
  header img {{ width:72px; border-radius:14px; }}
  h1 {{ font-family:'Arial Black', Arial; font-size:30px; margin:0; }}
  h1 span {{ color:{YELLOW}; }}
  h2 {{ font-family:'Arial Black', Arial; font-size:20px; margin:44px 0 14px;
       border-bottom:2px solid {YELLOW}; padding-bottom:6px; }}
  .muted {{ color:{MUT}; }}
  .headline {{ background:{PANEL}; border-left:5px solid {YELLOW}; padding:14px 18px;
              border-radius:8px; font-size:16px; margin:18px 0; }}
  .kpis {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }}
  .kpi {{ background:{PANEL}; border-radius:10px; padding:14px 16px; }}
  .kpi b {{ display:block; font-size:26px; font-family:'Arial Black', Arial; color:{YELLOW}; }}
  .grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }}
  .panel {{ background:{PANEL}; border-radius:10px; padding:16px; }}
  canvas {{ max-height:340px; }}
  .cards {{ display:grid; grid-template-columns:1fr; gap:12px; }}
  .card {{ background:{PANEL}; border-radius:10px; padding:14px 18px; }}
  .card-head {{ display:flex; gap:10px; align-items:center; }}
  .card h3 {{ margin:0; font-size:16px; }}
  .prio {{ color:{DARK}; font-weight:bold; font-size:11px; padding:2px 8px; border-radius:10px; }}
  .card p {{ margin:8px 0 0; }} .evidence {{ color:{MUT}; }}
  table {{ width:100%; border-collapse:collapse; font-size:13.5px; }}
  th, td {{ text-align:left; padding:7px 9px; border-bottom:1px solid #26262f; }}
  th {{ color:{MUT}; font-weight:normal; }} td.num, th.num {{ text-align:right; }}
  a {{ color:{INK}; }} a:hover {{ color:{YELLOW}; }}
  .tag {{ background:#2a2a35; color:{YELLOW}; font-size:11px; padding:1px 7px; border-radius:9px; }}
  .tag.short {{ color:#5aa9e6; }} .tag.sched {{ color:#ff6b6b; }}
  ul.exp li {{ margin:6px 0; }}
</style></head><body><div class="wrap">
<header>{logo_img}<div>
  <h1>PERMANENT <span>UNDERPOD</span> — channel report</h1>
  <div class="muted">pulled {esc(data['pulledAt'])} · {esc(data['range']['start'])} → {esc(data['range']['end'])}</div>
</div></header>

<div class="headline">{esc(ins.get('headline', ''))}</div>

<div class="kpis">
  <div class="kpi"><b>{ch['subscribers']:,}</b>subscribers</div>
  <div class="kpi"><b>{ch['totalViews']:,}</b>total views</div>
  <div class="kpi"><b>{len(longs)}</b>episodes · {len(shorts)} shorts live</div>
  <div class="kpi"><b>{fmt_min(watch_min)}</b>watch time</div>
  <div class="kpi"><b>{avg_pct_long:.0f}%</b>avg viewed (episodes)</div>
</div>

<h2>Views by video</h2>
<div class="panel"><canvas id="views"></canvas>
<div class="muted" style="margin-top:6px">yellow = episodes · blue = shorts (chronological)</div></div>

<div class="grid2">
  <div><h2>Daily views &amp; net subs</h2><div class="panel"><canvas id="daily"></canvas></div></div>
  <div><h2>Traffic sources</h2><div class="panel"><canvas id="traffic"></canvas></div></div>
</div>

<h2>Audience retention — episodes</h2>
<div class="panel"><canvas id="retention"></canvas>
<div class="muted" style="margin-top:6px">% of viewers still watching at each point of the video</div></div>

<h2>Improve the channel</h2>
<div class="cards">{insight_cards(ins.get('channel', []))}</div>

<h2>Improve the pod</h2>
<div class="cards">{insight_cards(ins.get('pod', []))}</div>

{'<h2>Experiments to run</h2><ul class="exp">' + experiments + '</ul>' if experiments else ''}

<h2>All videos</h2>
<table><tr><th>Title</th><th>Date</th><th>Len</th><th class="num">Impr</th>
<th class="num">CTR</th><th class="num">Views</th>
<th class="num">Avg %</th><th class="num">Avg time</th><th class="num">Likes</th>
<th class="num">Comments</th><th class="num">Shares</th><th class="num">Subs+</th></tr>
{''.join(rows)}</table>

</div><script>
const MUT = "{MUT}", GRID = "#26262f";
Chart.defaults.color = MUT; Chart.defaults.borderColor = GRID;
new Chart(document.getElementById('views'), {{
  type: 'bar',
  data: {{ labels: {json.dumps(bar_labels)},
          datasets: [{{ data: {json.dumps(bar_views)}, backgroundColor: {json.dumps(bar_colors)} }}] }},
  options: {{ plugins: {{ legend: {{ display: false }} }},
             scales: {{ x: {{ ticks: {{ autoSkip: false, maxRotation: 60, minRotation: 45, font: {{ size: 10 }} }} }} }} }}
}});
new Chart(document.getElementById('daily'), {{
  data: {{ labels: {json.dumps(day_labels)}, datasets: [
    {{ type: 'line', label: 'views', data: {json.dumps(day_views)}, borderColor: "{YELLOW}",
       pointRadius: 0, borderWidth: 2, tension: 0.3, yAxisID: 'y' }},
    {{ type: 'bar', label: 'net subs', data: {json.dumps(day_subs)}, backgroundColor: '#5aa9e6', yAxisID: 'y1' }} ] }},
  options: {{ scales: {{ y: {{ position: 'left' }}, y1: {{ position: 'right', grid: {{ display: false }} }} }} }}
}});
new Chart(document.getElementById('traffic'), {{
  type: 'doughnut',
  data: {{ labels: {json.dumps(tr_labels)},
          datasets: [{{ data: {json.dumps(tr_views)},
            backgroundColor: ['{YELLOW}','#5aa9e6','#ff6b6b','#7bd88f','#c792ea','#f78c6c','#89ddff','#666'] }}] }},
  options: {{ plugins: {{ legend: {{ position: 'right' }} }} }}
}});
new Chart(document.getElementById('retention'), {{
  type: 'line',
  data: {{ datasets: {json.dumps(ret_sets)} }},
  options: {{ parsing: false,
    scales: {{ x: {{ type: 'linear', min: 0, max: 100, title: {{ display: true, text: '% through video' }} }},
              y: {{ min: 0, title: {{ display: true, text: '% of viewers watching' }} }} }} }}
}});
</script></body></html>"""

    with open(out_p, "w") as f:
        f.write(html_out)
    print(f"wrote {out_p}")


if __name__ == "__main__":
    main()
