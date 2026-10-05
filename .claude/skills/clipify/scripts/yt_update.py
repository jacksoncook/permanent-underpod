#!/usr/bin/env python3
"""Patch metadata on already-uploaded videos (the post-publish step: once the
full episode is live, swap the "Full episode …" placeholder in every clip's
description for the real link).

usage:
  python3 yt_update.py --replace "OLD TEXT" "NEW TEXT" <videoId> [videoId ...]
       [--dry-run]
  python3 yt_update.py --set-description path/to/desc.txt <videoId> [--dry-run]

--replace fetches each video's snippet, applies the replacement to its
description, and calls videos.update (title/categoryId are re-sent unchanged —
the API requires the full snippet). Videos whose description doesn't contain
OLD TEXT are skipped with a note.

--set-description replaces one video's whole description with the file's
contents (≤ 5000 chars) and prints a readback check. Use it after a manual
retitle when the opener has to change to match.

Uses the same force-ssl token as yt_upload.py (token_captions.json — the one
token that covers uploads, tags and captions; see youtube-setup.md). Each
videos.update costs ~50 quota.
"""
import json, os, sys

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
CONF = os.path.expanduser("~/.config/clipify-youtube")
MAX_DESCRIPTION_CHARS = 5000


def get_creds():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    tok = f"{CONF}/token_captions.json"
    creds = None
    if os.path.exists(tok):
        creds = Credentials.from_authorized_user_file(tok, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
        except Exception as e:
            print(f"token refresh failed ({e}) — re-authorizing…")
            creds = None
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            f"{CONF}/client_secret.json", SCOPES)
        print("Opening a browser to authorize YouTube access…")
        creds = flow.run_local_server(port=0)
    open(tok, "w").write(creds.to_json())
    os.chmod(tok, 0o600)
    return creds


def set_description(path, vid, dry):
    new = open(path, encoding="utf-8").read().rstrip("\n")
    if len(new) > MAX_DESCRIPTION_CHARS:
        sys.exit(f"description is {len(new)} chars; YouTube caps at {MAX_DESCRIPTION_CHARS}")
    from googleapiclient.discovery import build
    yt = build("youtube", "v3", credentials=get_creds())
    items = yt.videos().list(part="snippet", id=vid).execute().get("items", [])
    if not items:
        sys.exit(f"{vid}: NOT FOUND (wrong channel token?)")
    sn = items[0]["snippet"]
    print(f"  {vid}: {sn['title']!r} ({len(sn.get('description', ''))} → {len(new)} chars)")
    if dry:
        return
    sn["description"] = new
    yt.videos().update(part="snippet", body={"id": vid, "snippet": sn}).execute()
    back = yt.videos().list(part="snippet", id=vid).execute()["items"][0]["snippet"]
    same = back["description"].rstrip() == new.rstrip()
    print("  readback matches:", same)
    if not same:
        sys.exit("live description differs from the file after update")


def main():
    args = sys.argv[1:]
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if len(args) == 3 and args[0] == "--set-description":
        return set_description(args[1], args[2], dry)
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
