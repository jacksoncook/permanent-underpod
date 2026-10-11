#!/usr/bin/env python3
"""Flatten every rendered vertical short into media/clips/library/ and write episodes/shorts-library.md.

Links each local master to its YouTube video (upload manifests, then the per-episode sheet tables),
pulls lifetime views from analytics/channel-data.json, and ranks the index by views so the list
doubles as a repost order. Hardlinks, so the library costs no disk; re-run after each episode.
"""
import glob, json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../.."))
LIB = os.path.join(ROOT, "media/clips/library")
INDEX = os.path.join(ROOT, "episodes/shorts-library.md")


def ep_num(path):
    return int(re.search(r"/ep(\d+)/", path).group(1))


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height:format=duration", "-of", "json", path],
                         capture_output=True, text=True).stdout
    j = json.loads(out)
    s = j["streams"][0]
    return s["width"], s["height"], float(j["format"]["duration"])


def manifest_links():
    links = {}
    for m in sorted(glob.glob(os.path.join(ROOT, "media/clips/ep*/*.json"))):
        if m.endswith(".results.json") or "clips" in os.path.basename(m) or "pin-comments" in m:
            continue
        try:
            j = json.load(open(m)); r = json.load(open(m + ".results.json"))
        except Exception:
            continue
        for u in j.get("uploads") or j.get("items") or []:
            f = u.get("file")
            if not f or f not in r:
                continue
            links[(ep_num(f), rel(f))] = {"videoId": r[f]["videoId"], "title": u.get("title", ""),
                                          "publishAt": r[f].get("publishAt", "")}
    tiktok = os.path.join(ROOT, "media/clips/tiktok/manifest.json")
    if os.path.exists(tiktok):
        for it in json.load(open(tiktok))["items"]:
            links.setdefault((ep_num(it["file"]), rel(it["file"])), {"videoId": it["ytId"], "title": ""})
    return links


def rel(path):
    """Path below the episode dir, so ep5's facecrop/ re-renders stay distinct from the v1 masters."""
    return re.search(r"/ep\d+/(.+)$", path).group(1)


def sheet_links():
    links = {}
    for sheet in glob.glob(os.path.join(ROOT, "episodes/ep*/segment-times.md")):
        ep = ep_num(sheet)
        for line in open(sheet):
            m = re.search(r"`?(short[\w-]+)`?.*?youtu\.be/([\w-]{11})", line)
            if m:
                links[(ep, m.group(1) + ".mp4")] = {"videoId": m.group(2), "title": ""}
    return links


def main():
    data = json.load(open(os.path.join(ROOT, "analytics/channel-data.json")))
    by_id = {v["id"]: v for v in data["videos"]}
    links = sheet_links(); links.update(manifest_links())
    os.makedirs(LIB, exist_ok=True)
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "media/clips/ep*/**/*.mp4"), recursive=True)):
        w, h, dur = probe(f)
        if h <= w:
            continue
        ep = ep_num(f); base = os.path.basename(f)
        link = links.get((ep, rel(f))) or links.get((ep, base)) or {}
        v = by_id.get(link.get("videoId"))
        title = (v or {}).get("title") or link.get("title") or base[:-4]
        views = (v or {}).get("stats", {}).get("views")
        url = f"https://youtu.be/{link['videoId']}" if link.get("videoId") else ""
        if link.get("videoId") and not v:
            if link.get("publishAt", "9") < data["pulledAt"]:
                continue
            url += " (scheduled after the last analytics pull)"
        name = f"ep{ep:02d}-" + rel(f).replace("/", "-")
        dst = os.path.join(LIB, name)
        if os.path.lexists(dst):
            os.remove(dst)
        os.link(f, dst)
        rows.append((views if views is not None else -1, ep, name, title, round(dur), url or "never published"))
    rows.sort(key=lambda r: (-r[0], r[1]))
    with open(INDEX, "w") as out:
        out.write("# Shorts library\n\n")
        out.write(f"Every rendered vertical master, hardlinked flat into `media/clips/library/` "
                  f"(gitignored, {len(rows)} files). Ranked by lifetime YouTube views as of "
                  f"{data['pulledAt'][:10]} (`analytics/channel-data.json`); clips the pull predates and never-published alternates sort last; superseded re-uploads (ids no longer live) are left out. "
                  f"Regenerate: `python3 .claude/skills/clipify/scripts/shorts_library.py`.\n\n")
        out.write("| # | Views | Ep | File | Title | Len | YouTube |\n|---|---|---|---|---|---|---|\n")
        for i, (views, ep, name, title, dur, url) in enumerate(rows, 1):
            out.write(f"| {i} | {'' if views < 0 else views} | {ep} | `{name}` | {title} | {dur}s | {url} |\n")
    unmatched = [r for r in rows if r[0] < 0]
    print(f"{len(rows)} verticals -> {LIB}; {len(unmatched)} without a YouTube match")
    for r in unmatched:
        print("  unmatched:", r[2])


if __name__ == "__main__":
    sys.exit(main())
