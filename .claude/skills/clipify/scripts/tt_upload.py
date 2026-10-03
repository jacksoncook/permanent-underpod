#!/usr/bin/env python3
"""Post the next due short to TikTok through TikTok Studio's web uploader.

usage: tt_upload.py <manifest.json> [<manifest.json> ...] [--dry-run] [--force] [--headful]

manifest.json: {"account": "<tiktok username>", "postHourLocal": 17,
                "items": [{"postOn": "YYYY-MM-DD", "file": "<mp4>", "caption": "<text with #tags>"}]}

Per manifest: posts at most ONE item per run and at most one per local calendar day, never before
postHourLocal: the earliest item whose postOn is today or earlier and is not yet in
<manifest>.results.json. Several manifests with different postHourLocal values give several daily
slots from one LaunchAgent. --force ignores the once-per-day and hour guards (not the results
file). --dry-run fills everything in, then discards.

Session: a cloned Chrome profile at ~/.config/clipify-tiktok/chrome-profile (cookies copied from
the Chrome profile that is logged into TikTok). Chrome must be launched with the real keychain
(not Playwright's mock one) or the encrypted cookies are silently dropped. The account check runs
first so a logged-out session fails loudly instead of posting nothing. Meant to run from a
LaunchAgent at the daily slot; a later same-day run is a free retry.
"""
import datetime
import json
import os
import re
import sys
import time

PROFILE = os.path.expanduser("~/.config/clipify-tiktok/chrome-profile")
UPLOAD_URL = "https://www.tiktok.com/tiktokstudio/upload?from=webapp"
ACCOUNT_INFO_URL = "https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=en"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__); sys.exit(2)
    failures = 0
    for manifest_path in args:
        try:
            run(manifest_path, flags)
        except Exception as e:
            failures += 1
            print(f"FAILED {manifest_path}: {e!r}")
    sys.exit(1 if failures else 0)


def run(manifest_path, flags):
    dry = "--dry-run" in flags
    manifest = json.load(open(manifest_path))
    results_path = manifest_path + ".results.json"
    results = json.load(open(results_path)) if os.path.exists(results_path) else {}
    today = datetime.date.today()
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M %Z")

    posted_today = [k for k, v in results.items() if v.get("postedOn") == today.isoformat()]
    if posted_today and "--force" not in flags:
        print(f"{stamp} {manifest_path}: already posted today ({posted_today[0]})"); return
    slot = manifest.get("postHourLocal", 0)
    if datetime.datetime.now().hour < slot and not (dry or "--force" in flags):
        print(f"{stamp} {manifest_path}: before the {slot}:00 slot"); return
    due = sorted((it for it in manifest["items"]
                  if it["file"] not in results and datetime.date.fromisoformat(it["postOn"]) <= today),
                 key=lambda it: it["postOn"])
    if not due:
        print(f"{stamp} {manifest_path}: nothing due"); return
    item = due[0]
    path = os.path.abspath(item["file"])
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    print(f"{stamp} posting {item['file']} (postOn {item['postOn']}, dry={dry})")

    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(
            PROFILE, channel="chrome", headless="--headful" not in flags,
            args=["--disable-blink-features=AutomationControlled"],
            ignore_default_args=["--use-mock-keychain"],
            viewport={"width": 1400, "height": 1000})
        try:
            url = post(ctx, path, item["caption"], manifest.get("account"), dry)
        except Exception:
            shot = manifest_path + f".fail-{today.isoformat()}.png"
            try:
                ctx.pages[-1].screenshot(path=shot, full_page=True)
                print(f"screenshot: {shot}")
            finally:
                ctx.close()
            raise
        ctx.close()
    if dry:
        print(f"{stamp} dry run complete, discarded"); return
    results[item["file"]] = {"postedOn": today.isoformat(), "postedAt": stamp, "url": url,
                             "caption": item["caption"]}
    json.dump(results, open(results_path, "w"), indent=1, ensure_ascii=False)
    print(f"{stamp} POSTED {item['file']} -> {url}")


def post(ctx, path, caption, account, dry):
    page = ctx.new_page()
    page.goto("https://www.tiktok.com/", wait_until="domcontentloaded", timeout=60000)
    info = page.request.get(ACCOUNT_INFO_URL).json()
    username = (info.get("data") or {}).get("username")
    if not username or (account and username != account):
        raise RuntimeError(f"TikTok session is not logged in as {account!r} (got {username!r}); "
                           f"re-clone the Chrome profile cookies")
    print(f"logged in as @{username}")

    page.goto(UPLOAD_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("input[type=file]", state="attached", timeout=60000)
    page.set_input_files("input[type=file]", path)
    wait_for_text(page, re.compile(r"Uploaded"), 180)
    print("upload complete")
    dismiss_popups(page)

    editor = page.locator("[contenteditable=true]").first
    editor.click()
    page.keyboard.press("Meta+A")
    page.keyboard.press("Backspace")
    page.wait_for_timeout(300)
    type_caption(page, caption)
    page.wait_for_timeout(1000)
    dismiss_popups(page)
    got = normalize(editor.inner_text())
    if got != normalize(caption):
        raise RuntimeError(f"caption mismatch:\n want {caption!r}\n got  {got!r}")
    print("caption set")

    body = page.locator("body").inner_text()
    if "Everyone" not in body:
        raise RuntimeError("audience selector does not show Everyone; refusing to post")

    if dry:
        page.get_by_role("button", name="Discard", exact=True).click()
        confirm = page.get_by_role("button", name=re.compile(r"^(Discard|Confirm)$"))
        if confirm.count():
            confirm.last.click()
        page.wait_for_timeout(1500)
        return None

    try:
        wait_for_text(page, re.compile(r"No issues found"), 90)
        print("content check passed")
    except TimeoutError:
        print("content check still running; posting anyway")
    page.get_by_role("button", name="Post", exact=True).click()
    page.wait_for_timeout(1500)
    post_now = page.get_by_role("button", name="Post now", exact=True)
    if post_now.count() and post_now.first.is_visible():
        post_now.first.click()
    wait_for_posts_list(page, caption, 120)
    print("post confirmed on the Studio posts list")
    return latest_post_url(page, username)


def type_caption(page, caption):
    """Type word by word so each hashtag's suggestion dropdown closes on the following space."""
    for word in caption.split(" "):
        page.keyboard.type(word, delay=15)
        if word.startswith("#"):
            page.wait_for_timeout(600)
        page.keyboard.type(" ", delay=15)
        page.wait_for_timeout(80)
    page.keyboard.press("Backspace")


def wait_for_text(page, pattern, seconds):
    deadline = time.time() + seconds
    while time.time() < deadline:
        if pattern.search(page.locator("body").inner_text()):
            return
        page.wait_for_timeout(1000)
    raise TimeoutError(f"timed out waiting for {pattern.pattern!r}")


def wait_for_posts_list(page, caption, seconds):
    """Studio redirects to /tiktokstudio/content after a successful post; the new row shows the caption."""
    deadline = time.time() + seconds
    head = normalize(caption)[:40]
    while time.time() < deadline:
        if "/tiktokstudio/content" in page.url and head in normalize(page.locator("body").inner_text()):
            return
        page.wait_for_timeout(1000)
    raise TimeoutError("no Studio posts-list row with this caption after posting; check Studio before retrying")


def dismiss_popups(page):
    for name in ("Cancel", "Got it"):
        btn = page.get_by_role("button", name=name, exact=True)
        if btn.count() and btn.first.is_visible():
            btn.first.click()
            page.wait_for_timeout(500)


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def latest_post_url(page, username):
    """The Studio posts list links each row to /@user/video/<id>; the public profile lags by minutes."""
    for _ in range(12):
        page.goto("https://www.tiktok.com/tiktokstudio/content", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(5000)
        for a in page.locator(f"a[href*='/@{username}/video/']").all():
            return "https://www.tiktok.com" + a.get_attribute("href")
        page.wait_for_timeout(10000)
    return f"https://www.tiktok.com/@{username} (video link not yet visible)"


if __name__ == "__main__":
    main()
