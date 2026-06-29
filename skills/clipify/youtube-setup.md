# YouTube upload — one-time setup

`yt_upload.py` uploads to YouTube with the **Data API v3**, which requires OAuth
credentials tied to *your* Google account. This is a one-time setup (~10 min). All
secrets live **outside any git repo**, in `~/.config/clipify-youtube/`.

## 1. Create a Google Cloud project + enable the API

1. Go to <https://console.cloud.google.com/> and create a project (e.g.
   "permanent-underpod-uploader").
2. **APIs & Services → Library → search "YouTube Data API v3" → Enable.**

## 2. Configure the OAuth consent screen

1. **APIs & Services → OAuth consent screen.**
2. User type: **External** → Create.
3. Fill app name + your email (support + developer contact). Save through the steps.
4. **Scopes:** you can skip adding scopes here (the script requests
   `youtube.upload` at runtime).
5. **Test users:** add the Google account that owns the YouTube channel you'll
   upload to. *(In "Testing" mode only test users can authorize — that's fine.)*

> **Heads-up on "Testing" mode:** refresh tokens for an app in *Testing* expire
> after **7 days**, so you'll re-do the browser auth weekly. To avoid that, later
> click **Publish app** on the consent screen (no Google verification is needed for
> a personal app using only the `youtube.upload` scope on your own channel).

## 3. Create the OAuth client (Desktop)

1. **APIs & Services → Credentials → Create credentials → OAuth client ID.**
2. Application type: **Desktop app** → Create.
3. **Download JSON.** Save it as:
   ```
   ~/.config/clipify-youtube/client_secret.json
   ```
   ```bash
   mkdir -p ~/.config/clipify-youtube
   mv ~/Downloads/client_secret_*.json ~/.config/clipify-youtube/client_secret.json
   chmod 600 ~/.config/clipify-youtube/client_secret.json
   ```

## 4. Install the Python libraries (once)

```bash
python3 -m venv ~/.config/clipify-youtube/.venv
~/.config/clipify-youtube/.venv/bin/pip install \
  google-api-python-client google-auth-oauthlib google-auth-httplib2
```

## 5. First run = authorize once

The first real upload opens a browser to authorize the channel. Pick the account
you added as a test user → "Continue" past the unverified-app warning (it's your own
app) → allow. A cached token is written to `~/.config/clipify-youtube/token.json`
(chmod 600). After that, uploads are non-interactive until the token expires.

```bash
# dry-run needs no auth and no libs — validates the manifest:
~/.config/clipify-youtube/.venv/bin/python scripts/yt_upload.py manifest.json --dry-run
# real upload (first time triggers the browser):
~/.config/clipify-youtube/.venv/bin/python scripts/yt_upload.py manifest.json
```

## Gotchas

- **Unverified channel → uploads stuck private.** If the channel has never been
  verified, the API locks *all* uploaded videos to private and scheduled publish
  won't fire. Verify by phone at <https://www.youtube.com/verify> (YouTube Studio →
  Settings → Channel → Feature eligibility).
- **Quota.** Each upload costs ~1600 units of the default 10,000/day → ~6 uploads/day.
  Request more in the Cloud console if you need it.
- **Scheduling.** `publishAt` (RFC3339 UTC) only works when `privacyStatus=private`;
  the script enforces that. Convert your local (Pacific) time to UTC first
  (PDT = UTC−7, PST = UTC−8). e.g. 10:00 AM PDT → `17:00:00Z`.
- **Never commit** `client_secret.json` or `token.json`. The repo `.gitignore`
  excludes them defensively, but they belong in `~/.config/clipify-youtube/`.
