#!/usr/bin/env python3
"""Upload finished clips / episodes to YouTube via the Data API v3.

usage:
  python3 yt_upload.py <manifest.json> [--dry-run] [--force]
                       [--publish-at "2026-07-01T17:00:00Z"]  # override every entry
                       [--privacy private|unlisted|public]    # override every entry

This is the PUBLISH step for the `clipify` and `podcast-video-edit` skills. Those
skills make the files plus the title/description/tags (the "posting copy"); this
uploads them and — by default — schedules each one PRIVATE with a `publishAt` time
so YouTube flips it public automatically at release.

One-time OAuth setup: see youtube-setup.md. You need a Google Cloud project with
"YouTube Data API v3" enabled and a Desktop OAuth client (client_secret.json).
Secrets live OUTSIDE the repo (default ~/.config/clipify-youtube/). NEVER commit them.

manifest.json:
{
  "client_secret": "~/.config/clipify-youtube/client_secret.json",
  "token":         "~/.config/clipify-youtube/token.json",   # auto-created on first auth
  "defaults": {"categoryId": "22", "privacyStatus": "private",
               "madeForKids": false, "tags": []},
  "uploads": [
    {"file": "/abs/short5.mp4", "title": "...", "description": "...",
     "tags": ["#Shorts", "..."], "publishAt": "2026-07-01T17:00:00Z"}
  ]
}

- publishAt (RFC3339 UTC, e.g. 2026-07-01T17:00:00Z): the video uploads private and
  auto-publishes at that instant. publishAt forces privacyStatus=private (API rule).
- No publishAt -> uses privacyStatus (default from `defaults` / --privacy).
- Already-uploaded files are skipped (tracked in <manifest>.results.json) unless --force.

NOTE: a brand-new / unverified channel locks ALL API uploads to private until you
verify the channel by phone in YouTube Studio. Scheduled publish won't fire until then.
"""
import json, os, sys, time

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
RETRIABLE = {500, 502, 503, 504}


def die(msg, code=1):
    print(msg)
    sys.exit(code)


def need_libs():
    try:
        import google.auth.transport.requests  # noqa: F401
        import google.oauth2.credentials  # noqa: F401
        import google_auth_oauthlib.flow  # noqa: F401
        import googleapiclient.discovery  # noqa: F401
    except ImportError:
        die("Missing Google API libraries. Install them into a venv once:\n"
            "  python3 -m venv ~/.config/clipify-youtube/.venv\n"
            "  ~/.config/clipify-youtube/.venv/bin/pip install "
            "google-api-python-client google-auth-oauthlib google-auth-httplib2\n"
            "then run this script with ~/.config/clipify-youtube/.venv/bin/python.")


def expand(p):
    return os.path.abspath(os.path.expanduser(p)) if p else p


def rfc3339(s):
    """Validate an RFC3339 timestamp (UTC 'Z' or offset); return it unchanged."""
    from datetime import datetime
    v = str(s).strip()
    try:
        datetime.fromisoformat(v.replace("Z", "+00:00"))
    except ValueError:
        die(f"publishAt '{s}' is not RFC3339 (want e.g. 2026-07-01T17:00:00Z)")
    return v


def get_creds(client_secret, token_path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(client_secret):
                die(f"client_secret not found: {client_secret}\nSee youtube-setup.md.")
            flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
            print("Opening a browser to authorize YouTube upload access…")
            creds = flow.run_local_server(port=0)
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, "w") as f:
            f.write(creds.to_json())
        os.chmod(token_path, 0o600)
    return creds


def plan_one(up, defaults):
    """Resolve an upload entry into (file, body, privacy, publishAt) and print it."""
    f = expand(up["file"])
    privacy = up.get("privacyStatus", defaults.get("privacyStatus", "private"))
    publish_at = up.get("publishAt")
    if publish_at:
        publish_at = rfc3339(publish_at)
        privacy = "private"  # API requires private for scheduled publish
    snippet = {
        "title": up["title"][:100],  # YouTube hard limit is 100 chars
        "description": up.get("description", ""),
        "tags": up.get("tags", defaults.get("tags", [])),
        "categoryId": str(up.get("categoryId", defaults.get("categoryId", "22"))),
    }
    status = {
        "privacyStatus": privacy,
        "selfDeclaredMadeForKids": bool(
            up.get("madeForKids", defaults.get("madeForKids", False))),
    }
    if publish_at:
        status["publishAt"] = publish_at
    sched = f" -> publish {publish_at}" if publish_at else ""
    print(f"  {os.path.basename(f)}  [{privacy}]{sched}")
    print(f"      title: {snippet['title']}")
    return f, {"snippet": snippet, "status": status}, privacy, publish_at


def upload_one(youtube, f, body, privacy, publish_at):
    from googleapiclient.http import MediaFileUpload
    from googleapiclient.errors import HttpError
    media = MediaFileUpload(f, chunksize=8 * 1024 * 1024, resumable=True, mimetype="video/*")
    req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    resp, tries = None, 0
    while resp is None:
        try:
            prog, resp = req.next_chunk()
            if prog:
                print(f"      uploading… {int(prog.progress() * 100)}%", end="\r")
        except HttpError as e:
            if getattr(e, "resp", None) and e.resp.status in RETRIABLE and tries < 5:
                tries += 1; time.sleep(2 ** tries); continue
            die(f"\n  FAIL {os.path.basename(f)}: {e}")
        except Exception as e:  # transient socket/SSL errors are worth a retry
            if tries < 5:
                tries += 1; time.sleep(2 ** tries); continue
            die(f"\n  FAIL {os.path.basename(f)}: {e}")
    vid = resp["id"]
    url = f"https://youtu.be/{vid}"
    print(f"      done: {url}            ")
    return {"videoId": vid, "url": url, "privacy": privacy, "publishAt": publish_at}


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        die(__doc__, 0)
    manifest_path = args[0]
    dry = "--dry-run" in args
    force = "--force" in args
    publish_override = rfc3339(args[args.index("--publish-at") + 1]) if "--publish-at" in args else None
    privacy_override = args[args.index("--privacy") + 1] if "--privacy" in args else None

    spec = json.load(open(manifest_path))
    defaults = spec.get("defaults", {})
    uploads = spec.get("uploads", [])
    for u in uploads:
        if publish_override:
            u["publishAt"] = publish_override
        if privacy_override:
            u["privacyStatus"] = privacy_override
            if privacy_override != "private":
                u.pop("publishAt", None)
    if not uploads:
        die("manifest has no `uploads`.")
    for u in uploads:
        f = expand(u["file"])
        if not os.path.exists(f):
            die(f"file not found: {f}")

    if dry:
        print(f"DRY RUN — validating {len(uploads)} upload(s) (no auth, no upload):")
        for u in uploads:
            plan_one(u, defaults)
        print("ok (dry run). Remove --dry-run to upload.")
        return

    need_libs()
    from googleapiclient.discovery import build
    client_secret = expand(spec.get("client_secret", "~/.config/clipify-youtube/client_secret.json"))
    token_path = expand(spec.get("token", "~/.config/clipify-youtube/token.json"))
    creds = get_creds(client_secret, token_path)
    youtube = build("youtube", "v3", credentials=creds)

    results_path = manifest_path + ".results.json"
    results = json.load(open(results_path)) if os.path.exists(results_path) else {}
    done = 0
    for u in uploads:
        f, body, privacy, publish_at = plan_one(u, defaults)
        if f in results and not force:
            print(f"      SKIP (already uploaded: {results[f].get('url', '')})")
            continue
        r = upload_one(youtube, f, body, privacy, publish_at)
        results[f] = r
        with open(results_path, "w") as out:
            json.dump(results, out, indent=2)
        done += 1
    print(f"\nuploaded {done} new video(s). results -> {results_path}")
    sched = [r for r in results.values() if r.get("publishAt")]
    if sched:
        print("scheduled (stay private until publishAt):")
        for r in sched:
            print(f"  {r['url']}  -> {r['publishAt']}")


if __name__ == "__main__":
    main()
