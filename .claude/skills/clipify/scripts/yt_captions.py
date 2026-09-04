#!/usr/bin/env python3
"""Upload (or replace) a caption track on a published video.

usage: python3 yt_captions.py <videoId> <file.srt> [--name standard] [--lang en] [--dry-run]

Captions need the youtube.force-ssl scope — the broad `youtube` scope used by
yt_upload.py does NOT cover them — so this keeps its own token
(~/.config/clipify-youtube/token_captions.json). Jackson's manual uploads tend to
revoke tokens; a revoked token just re-opens the browser flow (pick the brand
channel). An existing track with the same name is replaced, not duplicated.
"""
import os, sys

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
CONF = os.path.expanduser("~/.config/clipify-youtube")


def get_creds():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    tok = f"{CONF}/token_captions.json"
    creds = Credentials.from_authorized_user_file(tok, SCOPES) if os.path.exists(tok) else None
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            open(tok, "w").write(creds.to_json())
        except Exception as e:
            print("refresh failed (revoked?):", e)
            creds = None
    if not creds or not creds.valid:
        creds = InstalledAppFlow.from_client_secrets_file(f"{CONF}/client_secret.json", SCOPES).run_local_server(port=0)
        open(tok, "w").write(creds.to_json())
    return creds


def main():
    args = [a for a in sys.argv[1:]]
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    name, lang = "standard", "en"
    if "--name" in args:
        i = args.index("--name"); name = args[i + 1]; del args[i:i + 2]
    if "--lang" in args:
        i = args.index("--lang"); lang = args[i + 1]; del args[i:i + 2]
    if len(args) != 2:
        sys.exit(__doc__)
    vid, srt = args
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    yt = build("youtube", "v3", credentials=get_creds())
    existing = yt.captions().list(part="snippet", videoId=vid).execute().get("items", [])
    for c in existing:
        print(f"  existing track: {c['id']} {c['snippet']['language']} {c['snippet']['name']!r} {c['snippet']['trackKind']}")
    if dry:
        print(f"dry-run: would upload {srt} as {lang}/{name!r} to {vid}"); return
    media = MediaFileUpload(srt, mimetype="application/octet-stream", resumable=False)
    same = [c for c in existing if c["snippet"]["name"] == name and c["snippet"]["language"] == lang]
    if same:
        r = yt.captions().update(part="snippet", body={"id": same[0]["id"], "snippet": same[0]["snippet"]}, media_body=media).execute()
        print("replaced", r["id"])
    else:
        r = yt.captions().insert(part="snippet", body={"snippet": {"videoId": vid, "language": lang, "name": name, "isDraft": False}}, media_body=media).execute()
        print("inserted", r["id"], r["snippet"]["trackKind"])


if __name__ == "__main__":
    main()
