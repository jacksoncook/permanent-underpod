#!/usr/bin/env python3
"""Build the yt_upload.py manifest for rendered standalones.

usage: standalone_manifest.py episodes/standalones.json episodes/standalones-copy.json <manifest.json>

Chapter timestamps are derived from the spec (hook + 3 s card + parts, 0.4 s gap between
episodes), so the manifest matches what standalone_render.py produced. Titles carry no
`- Ep N Clip` suffix on purpose: these are standalone search videos, not pulls.
"""
import json
import os
import sys

CARD_S, GAP_S = 3.0, 0.4


def tsec(v):
    if isinstance(v, (int, float)):
        return float(v)
    p = str(v).split(":")
    return sum(float(a) * m for a, m in zip(reversed(p), (1, 60, 3600)))


def mmss(t):
    t = int(t)
    return f"{t // 60}:{t % 60:02d}"


def main():
    spec, copy, out = json.load(open(sys.argv[1])), json.load(open(sys.argv[2])), sys.argv[3]
    ups = []
    for it in spec["items"]:
        c = copy[it["name"]]
        t = 0.0
        if it.get("hook"):
            t += tsec(it["hook"]["end"]) - tsec(it["hook"]["start"])
        t += CARD_S
        marks, prev = [("Intro", 0.0)], None
        for i, p in enumerate(it["parts"]):
            if prev and p["source"] != prev:
                t += GAP_S
            marks.append((c["chapters"][i + 1], t))
            t += tsec(p["end"]) - tsec(p["start"])
            prev = p["source"]
        first = it["parts"][0]
        link = f"https://youtu.be/{c['id']}?t={int(tsec(first['start']))}"
        desc = (f"{c['answer']}\n\nFull conversation (Episode {c['ep']}): {link}\n\n"
                + "\n".join(f"{mmss(s)} {name}" for name, s in marks)
                + "\n\nPermanent Underpod: Bitcoin, stablecoins and AI, weekly. Opinions are our own, "
                  "not our employers'. Not financial advice.\n\n" + c["hashtags"])
        ups.append({"file": os.path.abspath(os.path.join(spec["out_dir"], f"{it['name']}.mp4")),
                    "captions": os.path.abspath(os.path.join(spec["out_dir"], f"{it['name']}.srt")),
                    "title": it["title"], "description": desc, "tags": c["tags"],
                    "publishAt": c["publishAt"], "playlist": "Underpod Clips"})
    json.dump({"client_secret": "~/.config/clipify-youtube/client_secret.json",
               "token": "~/.config/clipify-youtube/token_captions.json",
               "defaults": {"categoryId": "22", "privacyStatus": "private", "madeForKids": False},
               "uploads": ups}, open(out, "w"), indent=1)
    print(f"{len(ups)} uploads -> {out}")
    for u in ups:
        print(f"  {u['publishAt']}  {u['title']}")


if __name__ == "__main__":
    main()
