#!/usr/bin/env python3
"""Patch metadata on already-uploaded videos (the post-publish step: once the
full episode is live, swap the "Full episode …" placeholder in every clip's
description for the real link).

usage:
  python3 yt_update.py --replace "OLD TEXT" "NEW TEXT" <videoId> [videoId ...]
       [--dry-run]

Fetches each video's snippet, applies the replacement to its description, and
calls videos.update (title/categoryId are re-sent unchanged — the API requires
the full snippet). Videos whose description doesn't contain OLD TEXT are
skipped with a note. Uses the same OAuth token as yt_upload.py (broad
`youtube` scope; see youtube-setup.md). Each videos.update costs ~50 quota.
"""
import json, os, sys

SCOPES = ["https://www.googleapis.com/auth/youtube"]
CONF = os.path.expanduser("~/.config/clipify-youtube")


def get_creds():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    tok = f"{CONF}/token.json"
    creds = None
    if os.path.exists(tok):
        creds = Credentials.from_authorized_user_file(tok, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        open(tok, "w").write(creds.to_json())
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            f"{CONF}/client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)
        open(tok, "w").write(creds.to_json())
    return creds


def main():
    args = sys.argv[1:]
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if len(args) < 4 or args[0] != "--replace":
        sys.exit(__doc__)
    old, new, ids = args[1], args[2], args[3:]

    from googleapiclient.discovery import build
    yt = build("youtube", "v3", credentials=get_creds())
    resp = yt.videos().list(part="snippet", id=",".join(ids)).execute()
    found = {v["id"]: v["snippet"] for v in resp.get("items", [])}
    for vid in ids:
        sn = found.get(vid)
        if not sn:
            print(f"  {vid}: NOT FOUND (wrong channel token?)")
            continue
        if old not in sn.get("description", ""):
            print(f"  {vid}: placeholder not present — skipped ({sn['title'][:50]!r})")
            continue
        sn["description"] = sn["description"].replace(old, new)
        if dry:
            print(f"  {vid}: would update ({sn['title'][:50]!r})")
            continue
        yt.videos().update(part="snippet", body={"id": vid, "snippet": sn}).execute()
        print(f"  {vid}: updated ({sn['title'][:50]!r})")


if __name__ == "__main__":
    main()
