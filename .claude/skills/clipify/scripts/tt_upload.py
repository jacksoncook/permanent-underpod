#!/usr/bin/env python3
"""Schedule (or post) a manifest's clips on TikTok through TikTok Studio's web uploader.

usage: tt_upload.py <manifest.json> [<manifest.json> ...] [--dry-run] [--headful] [--max N]
       [--cdp http://localhost:9222] [--pause SECONDS] [--slow FACTOR]

manifest.json: {"account": "<tiktok username>", "postHourLocal": 17,
                "items": [{"postOn": "YYYY-MM-DD", "file": "<mp4>", "caption": "<text with #tags>",
                           "postHourLocal": 21}]}   # per-item hour is optional; overrides the manifest default

Every item not yet in <manifest>.results.json is handled in one run: items whose postOn/postHourLocal
is at least 20 minutes away are SCHEDULED in Studio (TikTok allows up to 10 days ahead, so run this
from clipify as soon as the YouTube schedule exists); an item due today whose time has passed is
posted now; an item whose day has passed is skipped and reported for a manual decision.
--dry-run fills everything in, then discards. --max N stops after N uploads.
--cdp URL drives an ALREADY-RUNNING Chrome (started with --remote-debugging-port) through its default
profile instead of the cloned one, so the logged-in human session is used as-is; the browser is left
open. --pause S sleeps a random S..2S seconds between items; --slow F multiplies every in-page wait and the
typing delay by F (Jackson 2026-10-24: "be careful not to trigger bot detection", "go a little slower").

Session: a cloned Chrome profile at ~/.config/clipify-tiktok/chrome-profile (cookies copied from
the Chrome profile that is logged into TikTok). Chrome must be launched with the real keychain
(not Playwright's mock one) or the encrypted cookies are silently dropped. The account check runs
first so a logged-out session fails loudly instead of posting nothing.
"""
import datetime
import json
import os
import re
import sys
import time

PROFILE = os.path.expanduser("~/.config/clipify-tiktok/chrome-profile")
UPLOAD_URL = "https://www.tiktok.com/tiktokstudio/upload?from=webapp"
POSTS_URL = "https://www.tiktok.com/tiktokstudio/content"
ACCOUNT_INFO_URL = "https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=en"
SCHEDULE_LEAD = datetime.timedelta(minutes=20)
SCHEDULE_HORIZON = datetime.timedelta(days=10)
SLOW = 1.0
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]


def main():
    argv = sys.argv[1:]
    valued = {"--max", "--cdp", "--pause", "--slow"}
    args = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] not in valued)]
    flags = {a for a in argv if a.startswith("--")}
    if not args:
        print(__doc__); sys.exit(2)
    max_uploads = int(flags_value("--max", 999))
    cdp = flags_value("--cdp", None)
    pause = float(flags_value("--pause", 0))
    global SLOW
    SLOW = float(flags_value("--slow", 1))
    failures = 0
    for manifest_path in args:
        try:
            run(manifest_path, "--dry-run" in flags, "--headful" in flags, max_uploads, cdp, pause)
        except Exception as e:
            failures += 1
            print(f"FAILED {manifest_path}: {e!r}")
    sys.exit(1 if failures else 0)


def flags_value(name, default):
    for i, a in enumerate(sys.argv):
        if a == name and i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return default


def run(manifest_path, dry, headful, max_uploads, cdp=None, pause=0.0):
    manifest = json.load(open(manifest_path))
    results_path = manifest_path + ".results.json"
    results = json.load(open(results_path)) if os.path.exists(results_path) else {}
    now = datetime.datetime.now()
    slot = manifest.get("postHourLocal", 17)
    plan = []
    for it in sorted(manifest["items"], key=lambda it: (it["postOn"], it.get("postHourLocal", slot))):
        if it["file"] in results:
            continue
        when = datetime.datetime.combine(datetime.date.fromisoformat(it["postOn"]), datetime.time(it.get("postHourLocal", slot), 0))
        if when.date() < now.date():
            print(f"SKIP {it['file']}: postOn {it['postOn']} has passed; decide by hand"); continue
        if when > now + SCHEDULE_HORIZON:
            print(f"later {it['file']}: {it['postOn']} is beyond TikTok's 10-day window"); continue
        plan.append((it, when if when >= now + SCHEDULE_LEAD else None))
    if not plan:
        print(f"{stamp()} {manifest_path}: nothing to do"); return
    plan = plan[:max_uploads]
    for it, when in plan:
        print(f"{stamp()} {it['file']} -> {'schedule ' + when.strftime('%Y-%m-%d %H:%M') if when else 'post now'}")

    import random
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        if cdp:
            browser = pw.chromium.connect_over_cdp(cdp)
            ctx = browser.contexts[0]
        else:
            ctx = pw.chromium.launch_persistent_context(
                PROFILE, channel="chrome", headless=not headful,
                args=["--disable-blink-features=AutomationControlled"],
                ignore_default_args=["--use-mock-keychain"],
                viewport={"width": 1400, "height": 1100})
        try:
            page = ctx.new_page()
            username = check_login(page, manifest.get("account"))
            for n, (it, when) in enumerate(plan):
                if n and pause:
                    nap = random.uniform(pause, 2 * pause)
                    print(f"{stamp()} pausing {nap:.0f}s before the next item"); time.sleep(nap)
                path = os.path.abspath(it["file"])
                if not os.path.exists(path):
                    raise FileNotFoundError(path)
                for attempt in (1, 2):
                    try:
                        url = upload_one(page, path, it["caption"], when, dry, username)
                        break
                    except Exception as e:
                        shot = manifest_path + f".fail-{now.date().isoformat()}-{attempt}.png"
                        page.screenshot(path=shot, full_page=True)
                        print(f"attempt {attempt} failed: {e!r}\nscreenshot: {shot}")
                        if attempt == 2 or not page_is_clean(page):
                            raise
                        nap(page, 5000)
                if dry:
                    print(f"{stamp()} dry run ok: {it['file']}"); continue
                results[it["file"]] = {
                    "postedOn" if when is None else "scheduledFor":
                        now.date().isoformat() if when is None else when.strftime("%Y-%m-%d %H:%M"),
                    "recordedAt": stamp(), "url": url, "caption": it["caption"]}
                json.dump(results, open(results_path, "w"), indent=1, ensure_ascii=False)
                print(f"{stamp()} {'POSTED' if when is None else 'SCHEDULED'} {it['file']} -> {url}")
        finally:
            if cdp:
                page.close()
            else:
                ctx.close()


def check_login(page, account):
    page.goto("https://www.tiktok.com/", wait_until="domcontentloaded", timeout=60000)
    info = page.request.get(ACCOUNT_INFO_URL).json()
    username = (info.get("data") or {}).get("username")
    if not username or (account and username != account):
        raise RuntimeError(f"TikTok session is not logged in as {account!r} (got {username!r}); "
                           f"re-clone the Chrome profile cookies")
    print(f"logged in as @{username}")
    return username


def upload_one(page, path, caption, when, dry, username):
    page.goto(UPLOAD_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("input[type=file]", state="attached", timeout=60000)
    page.set_input_files("input[type=file]", path)
    wait_for_text(page, re.compile(r"Uploaded"), 180)
    dismiss_popups(page)

    editor = page.locator("[contenteditable=true]").first
    editor.click()
    page.keyboard.press("Meta+A")
    page.keyboard.press("Backspace")
    nap(page, 300)
    type_caption(page, caption)
    nap(page, 1000)
    dismiss_popups(page)
    got = normalize(editor.inner_text())
    if got != normalize(caption):
        raise RuntimeError(f"caption mismatch:\n want {caption!r}\n got  {got!r}")

    if when is not None:
        set_schedule(page, when)

    if "Everyone" not in page.locator("body").inner_text():
        raise RuntimeError("audience selector does not show Everyone; refusing to post")

    if dry:
        page.get_by_role("button", name="Discard", exact=True).click()
        confirm = page.get_by_role("button", name=re.compile(r"^(Discard|Confirm)$"))
        if confirm.count():
            confirm.last.click()
        nap(page, 1500)
        return None

    try:
        wait_for_text(page, re.compile(r"No issues found"), 90)
    except TimeoutError:
        print("content check still running; continuing")
    page.get_by_role("button", name="Schedule" if when else "Post", exact=True).last.click()
    nap(page, 1500)
    confirm = page.get_by_role("button", name=re.compile(r"^(Post now|Schedule|Continue)$"))
    if confirm.count() and confirm.last.is_visible():
        confirm.last.click()
    wait_for_posts_list(page, caption, 120)
    return post_url(page, username, caption)


def page_is_clean(page):
    """A retry is safe only if the failed attempt left nothing in flight: Studio bounced to the posts list
    or never got past the file picker. An upload page with a filled caption or a schedule set is not retried."""
    body = page.locator("body").inner_text()
    return "/tiktokstudio/content" in page.url or "Uploaded" not in body


def set_schedule(page, when):
    page.locator("input[value=schedule]").check(force=True)
    nap(page, 1200)
    allow = page.get_by_role("button", name="Allow", exact=True)
    if allow.count() and allow.first.is_visible():
        allow.first.click()
        nap(page, 1200)
    time_input, date_input = (page.locator(".scheduled-picker input.TUXTextInputCore-input").nth(i) for i in (0, 1))

    time_input.click()
    nap(page, 600)
    page.locator("span.tiktok-timepicker-left", has_text=re.compile(rf"^{when:%H}$")).first.click()
    nap(page, 300)
    page.locator("span.tiktok-timepicker-right", has_text=re.compile(rf"^{when:%M}$")).first.click()
    nap(page, 600)
    page.keyboard.press("Escape")
    nap(page, 400)

    date_input.click()
    nap(page, 600)
    for _ in range(3):
        month = page.locator(".month-title").first.inner_text().strip()
        year = page.locator(".year-title").first.inner_text().strip()
        if month == MONTHS[when.month - 1] and year == str(when.year):
            break
        page.locator("span.arrow").last.click()
        nap(page, 500)
    page.locator("span.day.valid", has_text=re.compile(rf"^{when.day}$")).first.click()
    nap(page, 600)
    page.keyboard.press("Escape")
    nap(page, 400)

    got = (time_input.input_value(), date_input.input_value())
    want = (when.strftime("%H:%M"), when.strftime("%Y-%m-%d"))
    if got != want:
        raise RuntimeError(f"schedule mismatch: want {want} got {got}")
    print(f"scheduled for {want[1]} {want[0]} local")


def type_caption(page, caption):
    """Hashtags must be PICKED from Studio's suggestion dropdown: a typed "#tag" left as text is not a hashtag
    (Jackson, 2026-10-24: every clip through Ep 20 shipped that way). Clicking the exact-match row turns the word
    into a mention entity and inserts the trailing space itself; Enter does not select, it adds a newline."""
    words = caption.split(" ")
    for i, word in enumerate(words):
        last = i == len(words) - 1
        if word.startswith("#") and len(word) > 1:
            page.keyboard.type(word, delay=int(15 * SLOW))
            row = hashtag_row(page, word)
            if row is None:
                page.keyboard.press("Backspace")
                nap(page, 400)
                page.keyboard.type(word[-1], delay=int(15 * SLOW))
                row = hashtag_row(page, word)
            if row is None:
                raise RuntimeError(f"no dropdown match for {word}; refusing to post it as plain text")
            row.click()
            nap(page, 700)
            if last:
                page.keyboard.press("Backspace")
            continue
        page.keyboard.type(word + ("" if last else " "), delay=int(15 * SLOW))
        nap(page, 80)
    linked = page.locator("[data-testid=mentionText]").count()
    wanted = sum(1 for w in words if w.startswith("#") and len(w) > 1)
    if linked < wanted:
        raise RuntimeError(f"only {linked} of {wanted} hashtags linked")


def hashtag_row(page, word, seconds=8):
    """The suggestion dropdown renders a beat after typing stops and sometimes not at all on the first try."""
    deadline = time.time() + seconds * SLOW
    row = page.locator(".hashtag-suggestion-item", has=page.get_by_text(word, exact=True)).first
    while time.time() < deadline:
        if row.count():
            return row
        page.wait_for_timeout(250)
    return None


def wait_for_text(page, pattern, seconds):
    deadline = time.time() + seconds
    while time.time() < deadline:
        if pattern.search(page.locator("body").inner_text()):
            return
        nap(page, 1000)
    raise TimeoutError(f"timed out waiting for {pattern.pattern!r}")


def wait_for_posts_list(page, caption, seconds):
    """Studio redirects to /tiktokstudio/content after posting or scheduling; the new row shows the caption."""
    deadline = time.time() + seconds
    head = normalize(caption)[:40]
    next_reload = time.time() + 30
    while time.time() < deadline:
        if "/tiktokstudio/content" in page.url and head in normalize(page.locator("body").inner_text()):
            return
        if time.time() > next_reload:
            page.goto(POSTS_URL, wait_until="domcontentloaded", timeout=60000)
            next_reload = time.time() + 30
        nap(page, 1000)
    raise TimeoutError("no Studio posts-list row with this caption; check Studio before retrying")


def post_url(page, username, caption):
    """Match the caption to its row on the Studio posts list; rows paginate 10 at a time, newest first."""
    head = normalize(caption)[:40]
    for _ in range(3):
        page.goto(POSTS_URL, wait_until="domcontentloaded", timeout=60000)
        nap(page, 5000)
        for _ in range(8):
            for row in studio_rows(page):
                if head in row["text"]:
                    return "https://www.tiktok.com" + row["href"]
            scroll_list(page)
        nap(page, 5000)
    return f"https://www.tiktok.com/@{username} (row link not found yet)"


def scroll_list(page):
    """The posts list is virtualized (about ten rows rendered at a time); scroll its container a page."""
    page.evaluate("""() => { for (const el of document.querySelectorAll('*')) {
      const cs = getComputedStyle(el);
      if ((cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 50) el.scrollTop += el.clientHeight; } }""")
    nap(page, 1500)


def studio_rows(page):
    """Each row holds one /video/ link and its own 'Everyone' privacy cell; climb to that cell's container."""
    return page.evaluate("""() => {
      const out = [], seen = new Set();
      for (const a of document.querySelectorAll("a[href*='/video/']")) {
        const href = a.getAttribute('href');
        if (seen.has(href)) continue;
        let el = a, hops = 0;
        while (el && hops < 12 && !(el.innerText || '').includes('Everyone')) { el = el.parentElement; hops++; }
        const text = el ? (el.innerText || '').replace(/\\s+/g, ' ').trim() : '';
        if (!el || text.length > 600) continue;
        seen.add(href);
        out.push({href, text});
      }
      return out;
    }""")


def dismiss_popups(page):
    for name in ("Cancel", "Got it"):
        btn = page.get_by_role("button", name=name, exact=True)
        if btn.count() and btn.first.is_visible():
            btn.first.click()
            nap(page, 500)


def nap(page, ms):
    page.wait_for_timeout(int(ms * SLOW))


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def stamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


if __name__ == "__main__":
    main()
