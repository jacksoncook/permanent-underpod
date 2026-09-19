#!/usr/bin/env python3
"""Post the funnel comment (episode link + timestamp) on each short once it is public.

usage: yt_pin_comment.py <queue.json> [--dry-run]

queue.json: {"token": "~/.config/clipify-youtube/token_captions.json",
             "items": [{"videoId": "...", "text": "Full episode: https://youtu.be/<ep>?t=238 ..."}]}

Idempotent: skips private/scheduled videos (the API 403s on those), skips videos where the
channel already left a comment containing the episode link, and records posted ids in
<queue>.done.json. Pinning is not in the Data API — the owner pins in Studio. Meant to run
from cron ~10 min after each publish slot.
"""
import json, os, sys, datetime

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    qpath = args[0]
    q = json.load(open(qpath))
    done_path = qpath + ".done.json"
    done = json.load(open(done_path)) if os.path.exists(done_path) else {}
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    tok = os.path.expanduser(q.get("token", "~/.config/clipify-youtube/token_captions.json"))
    creds = Credentials.from_authorized_user_file(tok, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request()); open(tok, "w").write(creds.to_json())
    yt = build("youtube", "v3", credentials=creds)
    me = yt.channels().list(part="id", mine=True).execute()["items"][0]["id"]
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    pending = [it for it in q["items"] if it["videoId"] not in done]
    if not pending:
        print(f"{stamp} nothing pending"); return
    status = {v["id"]: v["status"]["privacyStatus"] for v in
              yt.videos().list(part="status", id=",".join(i["videoId"] for i in pending)).execute()["items"]}
    for it in pending:
        vid = it["videoId"]
        if status.get(vid) != "public":
            print(f"{stamp} {vid} {status.get(vid)} -> wait"); continue
        link = it["text"].split("?t=")[0].split()[-1]
        try:
            existing = yt.commentThreads().list(part="snippet", videoId=vid, maxResults=50).execute().get("items", [])
        except HttpError as e:
            print(f"{stamp} {vid} list failed {e.resp.status}"); continue
        mine = [t for t in existing if t["snippet"]["topLevelComment"]["snippet"].get("authorChannelId", {}).get("value") == me
                and link in t["snippet"]["topLevelComment"]["snippet"]["textOriginal"]]
        if mine:
            done[vid] = {"commentId": mine[0]["id"], "note": "already present", "at": stamp}
            print(f"{stamp} {vid} already has the channel comment -> done"); continue
        if dry:
            print(f"{stamp} {vid} public, no channel comment -> WOULD POST: {it['text'][:70]}"); continue
        try:
            r = yt.commentThreads().insert(part="snippet", body={"snippet": {"videoId": vid, "topLevelComment": {
                "snippet": {"textOriginal": it["text"]}}}}).execute()
            done[vid] = {"commentId": r["id"], "at": stamp}
            print(f"{stamp} {vid} POSTED {r['id']}  (pin it in Studio)")
        except HttpError as e:
            print(f"{stamp} {vid} insert failed {e.resp.status}: {e.content.decode()[:120]}")
    if not dry:
        json.dump(done, open(done_path, "w"), indent=1)


if __name__ == "__main__":
    main()
