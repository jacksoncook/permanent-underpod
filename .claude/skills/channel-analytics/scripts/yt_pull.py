#!/usr/bin/env python3
"""Pull the full performance picture for the authenticated channel:

  Data API v3      -> per-video metadata + public stats (views/likes/comments)
  Analytics API v2 -> lifetime per-video analytics (watch time, avg % viewed,
                      shares, subs gained), daily channel timeseries, traffic
                      sources, and audience-retention curves for long-form videos

usage:
  yt_pull.py [out.json] [--expect-channel "Permanent Underpod"]
    - reads  ~/.config/clipify-youtube/client_secret.json  (same OAuth client as clipify)
    - caches ~/.config/clipify-youtube/token_analytics.json (readonly + yt-analytics scopes)
    - default out.json: analytics/channel-data.json (relative to cwd)

Run with the uploader venv's python:
  ~/.config/clipify-youtube/.venv/bin/python yt_pull.py analytics/channel-data.json

First run opens a browser — ON THE CHANNEL-SELECTION SCREEN PICK THE BRAND
CHANNEL (Permanent Underpod), not the personal account. --expect-channel makes
that mistake fatal instead of silent: on mismatch the token is deleted and the
script exits so you can re-auth.
"""
import datetime
import json
import os
import re
import sys

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/yt-analytics.readonly",
]
CFG = os.path.expanduser("~/.config/clipify-youtube")
TOKEN = os.path.join(CFG, "token_analytics.json")
SHORT_MAX_S = 183  # YouTube Shorts cutoff (3 min); we have no vertical-flag via API


def get_creds():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    cs = os.path.join(CFG, "client_secret.json")
    c = None
    if os.path.exists(TOKEN):
        c = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not c or not c.valid:
        if c and c.expired and c.refresh_token:
            try:
                c.refresh(Request())
            except Exception as e:
                print(f"token refresh failed ({e}); re-authorizing…")
                c = None
        if not c or not c.valid:
            if not os.path.exists(cs):
                sys.exit(f"client_secret not found: {cs}\nSee clipify/youtube-setup.md.")
            print("Opening a browser to authorize analytics access…")
            print(">>> PICK THE *PERMANENT UNDERPOD* BRAND CHANNEL on the second screen <<<")
            c = InstalledAppFlow.from_client_secrets_file(cs, SCOPES).run_local_server(port=0)
        os.makedirs(CFG, exist_ok=True)
        with open(TOKEN, "w") as f:
            f.write(c.to_json())
        os.chmod(TOKEN, 0o600)
    return c


def iso_dur_s(d):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    if not m:
        return 0
    day, h, mi, s = (int(x or 0) for x in m.groups())
    return day * 86400 + h * 3600 + mi * 60 + s


def rows_as_dicts(resp):
    cols = [h["name"] for h in resp.get("columnHeaders", [])]
    return [dict(zip(cols, r)) for r in resp.get("rows", [])]


def main():
    args = [a for a in sys.argv[1:]]
    expect = None
    if "--expect-channel" in args:
        i = args.index("--expect-channel")
        expect = args[i + 1]
        del args[i:i + 2]
    out = args[0] if args else os.path.join("analytics", "channel-data.json")

    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    creds = get_creds()
    yt = build("youtube", "v3", credentials=creds)
    yta = build("youtubeAnalytics", "v2", credentials=creds)

    ch = yt.channels().list(part="snippet,statistics,contentDetails", mine=True).execute()
    if not ch.get("items"):
        sys.exit("No channel found for this account.")
    c = ch["items"][0]
    title = c["snippet"]["title"]
    print(f"channel: {title}")
    if expect and expect.lower() not in title.lower():
        os.remove(TOKEN)
        sys.exit(f"AUTHED AS WRONG CHANNEL ({title!r}, expected {expect!r}). "
                 f"Token deleted — rerun and pick the brand channel.")
    st = c.get("statistics", {})
    channel = {
        "id": c["id"],
        "title": title,
        "publishedAt": c["snippet"].get("publishedAt"),
        "subscribers": int(st.get("subscriberCount", 0)),
        "totalViews": int(st.get("viewCount", 0)),
        "videoCount": int(st.get("videoCount", 0)),
    }
    start = (channel["publishedAt"] or "2020-01-01")[:10]
    today = datetime.date.today().isoformat()

    uploads = c["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, page = [], None
    while True:
        r = yt.playlistItems().list(part="contentDetails", playlistId=uploads,
                                    maxResults=50, pageToken=page).execute()
        ids += [it["contentDetails"]["videoId"] for it in r["items"]]
        page = r.get("nextPageToken")
        if not page:
            break
    print(f"{len(ids)} videos in uploads")

    videos = {}
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,contentDetails,statistics,status",
                             id=",".join(ids[i:i + 50])).execute()
        for it in r["items"]:
            sn, stt = it["snippet"], it.get("statistics", {})
            dur = iso_dur_s(it["contentDetails"].get("duration"))
            videos[it["id"]] = {
                "id": it["id"],
                "url": f"https://youtu.be/{it['id']}",
                "title": sn.get("title"),
                "publishedAt": sn.get("publishedAt"),
                "duration_s": dur,
                "is_short": dur <= SHORT_MAX_S,
                "tags": sn.get("tags", []),
                "privacyStatus": it.get("status", {}).get("privacyStatus"),
                "publishAt": it.get("status", {}).get("publishAt"),
                "stats": {
                    "views": int(stt.get("viewCount", 0)),
                    "likes": int(stt.get("likeCount", 0)),
                    "comments": int(stt.get("commentCount", 0)),
                },
                "analytics": None,
                "retention": None,
            }

    # lifetime per-video analytics, chunked filters
    vids = list(videos)
    for i in range(0, len(vids), 50):
        chunk = vids[i:i + 50]
        resp = yta.reports().query(
            ids="channel==MINE", startDate=start, endDate=today,
            metrics=("views,estimatedMinutesWatched,averageViewDuration,"
                     "averageViewPercentage,likes,comments,shares,subscribersGained"),
            dimensions="video", filters="video==" + ",".join(chunk),
            maxResults=200,
        ).execute()
        for row in rows_as_dicts(resp):
            videos[row["video"]]["analytics"] = {
                "views": row.get("views", 0),
                "watch_min": row.get("estimatedMinutesWatched", 0),
                "avg_view_s": row.get("averageViewDuration", 0),
                "avg_view_pct": row.get("averageViewPercentage", 0),
                "likes": row.get("likes", 0),
                "comments": row.get("comments", 0),
                "shares": row.get("shares", 0),
                "subs_gained": row.get("subscribersGained", 0),
            }

    # audience retention for long-form videos (needs some views to have data)
    for v in videos.values():
        if v["is_short"] or v["stats"]["views"] == 0:
            continue
        try:
            resp = yta.reports().query(
                ids="channel==MINE", startDate=start, endDate=today,
                metrics="audienceWatchRatio,relativeRetentionPerformance",
                dimensions="elapsedVideoTimeRatio", filters=f"video=={v['id']}",
            ).execute()
        except HttpError:
            try:
                resp = yta.reports().query(
                    ids="channel==MINE", startDate=start, endDate=today,
                    metrics="audienceWatchRatio",
                    dimensions="elapsedVideoTimeRatio", filters=f"video=={v['id']}",
                ).execute()
            except HttpError as e:
                print(f"  retention unavailable for {v['id']}: {e.status_code}")
                continue
        rows = rows_as_dicts(resp)
        if rows:
            v["retention"] = [
                {"ratio": r["elapsedVideoTimeRatio"],
                 "watch_ratio": r.get("audienceWatchRatio"),
                 "vs_typical": r.get("relativeRetentionPerformance")}
                for r in rows
            ]
            print(f"  retention: {v['title'][:60]}  ({len(rows)} pts)")

    daily = rows_as_dicts(yta.reports().query(
        ids="channel==MINE", startDate=start, endDate=today,
        metrics="views,estimatedMinutesWatched,subscribersGained,subscribersLost",
        dimensions="day", sort="day", maxResults=366,
    ).execute())

    traffic = rows_as_dicts(yta.reports().query(
        ids="channel==MINE", startDate=start, endDate=today,
        metrics="views,estimatedMinutesWatched",
        dimensions="insightTrafficSourceType", sort="-views",
    ).execute())

    data = {
        "pulledAt": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "range": {"start": start, "end": today},
        "channel": channel,
        "videos": sorted(videos.values(), key=lambda v: v.get("publishedAt") or ""),
        "daily": daily,
        "traffic": traffic,
    }
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    n_ret = sum(1 for v in videos.values() if v["retention"])
    print(f"\nwrote {out}: {len(videos)} videos, {n_ret} retention curves, "
          f"{len(daily)} days, {len(traffic)} traffic sources")


if __name__ == "__main__":
    main()
