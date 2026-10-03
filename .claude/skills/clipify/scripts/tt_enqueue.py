#!/usr/bin/env python3
"""Append a YouTube upload manifest's clips to the standing TikTok queue, one per day.

usage: tt_enqueue.py <yt-upload-manifest.json> [media/clips/tiktok/queue.json] [--dry-run]

Each upload entry becomes a queue item: postOn = the Pacific date of its YouTube publishAt (never
earlier than today; bumped to the next free day if that date is already taken), caption = hook (title minus the
" - Ep N Clip" suffix) + first description line + "Full episode: Permanent Underpod." + the
description's hashtags minus #shorts. Idempotent: files already queued are skipped. The YouTube
video id is copied from <manifest>.results.json when it exists. tt_upload.py drains the queue.
"""
import datetime
import json
import os
import re
import sys
import zoneinfo

DEFAULT_QUEUE = "media/clips/tiktok/queue.json"
HOUSE_TZ = zoneinfo.ZoneInfo("America/Los_Angeles")
ACCOUNT = "permanentunderpod"
SLOT_HOUR = 19
EPISODE_SUFFIX = re.compile(r"\s*[-–|]\s*Ep\s*\d+\s*Clip\s*$", re.I)
FULL_EPISODE_LINE = re.compile(r"^\s*full episode", re.I)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        print(__doc__); sys.exit(2)
    yt_path = args[0]
    queue_path = args[1] if len(args) > 1 else DEFAULT_QUEUE
    repo = os.getcwd()
    yt = json.load(open(yt_path))
    results_path = yt_path + ".results.json"
    results = json.load(open(results_path)) if os.path.exists(results_path) else {}
    queue = json.load(open(queue_path)) if os.path.exists(queue_path) else {
        "account": ACCOUNT, "postHourLocal": SLOT_HOUR, "items": []}
    queued_files = {it["file"] for it in queue["items"]}
    taken = {it["postOn"] for it in queue["items"]}
    added = []
    for up in yt["uploads"]:
        rel = os.path.relpath(up["file"], repo)
        if rel in queued_files:
            print(f"skip (queued) {rel}"); continue
        if not up.get("publishAt"):
            print(f"skip (no publishAt) {rel}"); continue
        day = local_date(up["publishAt"])
        while day.isoformat() in taken:
            day += datetime.timedelta(days=1)
        taken.add(day.isoformat())
        item = {"postOn": day.isoformat(), "file": rel, "caption": caption_for(up)}
        yt_id = (results.get(up["file"]) or {}).get("videoId")
        if yt_id:
            item["ytId"] = yt_id
        queue["items"].append(item)
        queued_files.add(rel)
        added.append(item)
        print(f"queue {item['postOn']} {rel}\n      {item['caption']}")
    queue["items"].sort(key=lambda it: it["postOn"])
    if dry:
        print(f"dry run: {len(added)} would be added to {queue_path}"); return
    os.makedirs(os.path.dirname(queue_path) or ".", exist_ok=True)
    json.dump(queue, open(queue_path, "w"), indent=2, ensure_ascii=False)
    print(f"{len(added)} added; {len(queue['items'])} items in {queue_path}")


def local_date(publish_at):
    utc = datetime.datetime.fromisoformat(publish_at.replace("Z", "+00:00"))
    return max(utc.astimezone(HOUSE_TZ).date(), datetime.datetime.now(HOUSE_TZ).date())


def caption_for(up):
    hook = EPISODE_SUFFIX.sub("", up["title"]).strip()
    lines = [l.strip() for l in up.get("description", "").splitlines() if l.strip()]
    body = next((l for l in lines if not l.startswith("#") and not FULL_EPISODE_LINE.match(l)), "")
    tags = [t for l in lines for t in re.findall(r"#\w+", l) if t.lower() != "#shorts"]
    if "#podcast" not in [t.lower() for t in tags]:
        tags.append("#podcast")
    if hook[-1:].isalnum():
        hook += "."
    parts = [hook, body, "Full episode: Permanent Underpod.", " ".join(tags)]
    return " ".join(p for p in parts if p)


if __name__ == "__main__":
    main()
