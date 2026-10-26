# Underpod — Brand Assets

Regenerate everything with `python3 brand/make_brand.py` (Pillow; needs the Ep 10 face
cluster at `media/brand/faces/cluster_cut.png` for the banner). Rebranded 2026-10-26: the
wordmark is just "UNDERPOD", no kicker.

- `logo-3000-cover.png` — 3000×3000, podcast cover art (Apple/Spotify spec). **KEEP the
  square masters — Spotify needs the square shape**; `profile-1024.png` does not replace them.
- `logo-1920.png` — high-res general use (thumbnails, social)
- `logo-480.png` — corner bug @170px, cards (`logo-ep1-original.png` is the Ep 1 original)
- `profile-1024.png` — YouTube profile picture ONLY (circle-crop-first: couch centered in a
  dark disk, gold ring, wordmark inside the circle). Wrong shape for Spotify.
- `banner-2560.png` — YouTube channel banner (2560×1440; all content in the 1546×423 safe center)

**Colors:** accent yellow `#FFD24A` (255,210,74) · badge dark `#0E0E13` (14,14,19) ·
banner bg `#FFE79E` (255,231,158)
**Fonts:** Arial Black (wordmark "UNDERPOD") · Arial Bold (tagline "AI · BITCOIN · STABLECOINS")

The in-pipeline logo (`graphics.py make_logo()`) draws the same badge per episode from
brand.json: `"show": "UNDERPOD"`, `"show_main": "UNDERPOD"`, no `show_kicker`.
