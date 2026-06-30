#!/usr/bin/env python3
"""Pull published video metadata (title, description, REAL tags, chapters-in-desc)
for the authenticated channel via the YouTube Data API v3.

Companion to yt_upload.py: where the uploader pushes, this reads back what's live —
e.g. to backfill the per-episode `segment-times.md` sheets from the actual published
titles/descriptions instead of guessing.

usage:
  python3 yt_fetch.py [out.json]
    - reads  ~/.config/clipify-youtube/client_secret.json   (same OAuth client as the uploader)
    - caches ~/.config/clipify-youtube/token_readonly.json   (separate read-only token)
    - scope: youtube.readonly  -> as the channel OWNER you also get each video's real tags
  default out.json: ~/.config/clipify-youtube/channel_dump.json

Run with the uploader venv's python:
  ~/.config/clipify-youtube/.venv/bin/python yt_fetch.py
First run opens a browser once to authorize read access.
"""
import json, os, sys

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CFG = os.path.expanduser("~/.config/clipify-youtube")


def get_creds():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    tok = os.path.join(CFG, "token_readonly.json")
    cs = os.path.join(CFG, "client_secret.json")
    c = None
    if os.path.exists(tok):
        c = Credentials.from_authorized_user_file(tok, SCOPES)
    if not c or not c.valid:
        if c and c.expired and c.refresh_token:
            c.refresh(Request())
        else:
            if not os.path.exists(cs):
                sys.exit(f"client_secret not found: {cs}\nSee youtube-setup.md (steps 1-3).")
            print("Opening a browser to authorize read-only access to your channel…")
            c = InstalledAppFlow.from_client_secrets_file(cs, SCOPES).run_local_server(port=0)
        os.makedirs(CFG, exist_ok=True)
        with open(tok, "w") as f:
            f.write(c.to_json())
        os.chmod(tok, 0o600)
    return c


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(CFG, "channel_dump.json")
    from googleapiclient.discovery import build
    yt = build("youtube", "v3", credentials=get_creds())

    ch = yt.channels().list(part="contentDetails,snippet", mine=True).execute()
    if not ch.get("items"):
        sys.exit("No channel found for this account.")
    uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    print(f"channel: {ch['items'][0]['snippet']['title']}   uploads playlist: {uploads}")

    ids, page = [], None
    while True:
        r = yt.playlistItems().list(part="contentDetails", playlistId=uploads,
                                    maxResults=50, pageToken=page).execute()
        ids += [it["contentDetails"]["videoId"] for it in r["items"]]
        page = r.get("nextPageToken")
        if not page:
            break
    print(f"{len(ids)} videos in uploads")

    vids = []
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,contentDetails", id=",".join(ids[i:i + 50])).execute()
        for it in r["items"]:
            sn = it["snippet"]
            vids.append({
                "id": it["id"],
                "url": f"https://youtu.be/{it['id']}",
                "title": sn.get("title"),
                "description": sn.get("description"),
                "tags": sn.get("tags", []),
                "publishedAt": sn.get("publishedAt"),
                "duration": it["contentDetails"].get("duration"),
            })
    vids.sort(key=lambda v: v.get("publishedAt") or "")
    with open(out, "w") as f:
        json.dump(vids, f, indent=2, ensure_ascii=False)
    print(f"wrote {len(vids)} videos -> {out}\n")
    for v in vids:
        d = (v["publishedAt"] or "??????????")[:10]
        ntags = len(v["tags"])
        print(f"  [{d}] {v['title']}  ({v['url']})  tags:{ntags}")


if __name__ == "__main__":
    main()
