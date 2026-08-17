# Permanent Underpod — Brand Assets

- `logo-3000-cover.png` — 3000×3000, podcast cover art (Apple/Spotify spec). **KEEP the
  square masters — Spotify needs the square shape**; `profile-1024.png` does not replace them.
- `logo-1920.png` — high-res general use (thumbnails, social)
- `logo-480.png` / `logo-ep1-original.png` — as used in the Ep 1 video (corner bug @170px, cards)
- `profile-1024.png` — YouTube profile picture ONLY (circle-crop-first: couch centered in a
  dark disk, gold ring, wordmark inside the circle). Wrong shape for Spotify.
- `banner-2560.png` — YouTube channel banner (2560×1440; all content in the 1546×423 safe center)

**Colors:** accent yellow `#FFD24A` (255,210,74) · badge dark `#0E0E13` (14,14,19)
**Fonts:** Arial Black (wordmark "UNDERPOD") · Arial Bold (kicker "PERMANENT", letter-spaced)

The logo is drawn procedurally (rounded-rect couch badge) — regenerate at any size
with `make_logo()` in `~/.claude/skills/podcast-video-edit/scripts/graphics.py`
(brand config: `~/.claude/skills/podcast-video-edit/examples/ep1_brand.json`).
