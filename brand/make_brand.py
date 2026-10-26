#!/usr/bin/env python3
"""Regenerate every brand master from code (rebrand 2026-10-26: wordmark is just
"UNDERPOD", no kicker).

Outputs (into brand/):
  logo-480.png, logo-1920.png, logo-3000-cover.png  — square couch badge
  profile-1024.png                                   — YouTube profile (circle-crop-first)
  banner-2560.png                                    — YouTube banner, content in the
                                                       1546x423 device-safe center

The banner's host cluster is media/brand/faces/cluster_cut.png: the three white-outlined
cutouts lifted (with alpha) from media/ep10/ep10-thumbnail-cutouts.png, the same picks the
original Aug 2026 banner used.

usage: python3 brand/make_brand.py [--no-banner]
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FACES = os.path.join(ROOT, "media", "brand", "faces")
BLACK_F = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
BOLD_F = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

ACC = (255, 210, 74, 255)
DARK = (14, 14, 19, 255)
WHITE = (255, 255, 255, 255)
BANNER_BG = (255, 231, 158)
BANNER_GHOST = (255, 229, 148)
WORDMARK = "UNDERPOD"
TAGLINE = "AI  ·  BITCOIN  ·  STABLECOINS"


def font(path, size):
    return ImageFont.truetype(path, int(size))


def fit_font(path, text, max_w, start, draw):
    f = font(path, start)
    while draw.textbbox((0, 0), text, font=f)[2] > max_w and f.size > 8:
        f = font(path, f.size - 2)
    return f


def text_centered(d, cx, y, text, f, fill, **kw):
    bb = d.textbbox((0, 0), text, font=f)
    d.text((cx - (bb[2] + bb[0]) / 2, y - bb[1]), text, font=f, fill=fill, **kw)
    return bb[3] - bb[1]


def text_between(d, cx, y0, y1, text, f, fill):
    """Centre text vertically in the band [y0, y1] (couch bottom to badge edge)."""
    bb = d.textbbox((0, 0), text, font=f)
    h = bb[3] - bb[1]
    return text_centered(d, cx, (y0 + y1) / 2 - h / 2, text, f, fill)


def draw_couch(d, s, cx, top, fill=ACC, outline=DARK):
    """Couch glyph at scale s (1.0 = the 480px badge), horizontally centred on cx."""
    def r(x0, y0, x1, y1, rad, **kw):
        d.rounded_rectangle([(cx + (x0 - 240) * s, top + y0 * s),
                             (cx + (x1 - 240) * s, top + y1 * s)], radius=rad * s, **kw)
    r(118, 0, 362, 110, 26, fill=fill)
    r(78, 44, 138, 160, 22, fill=fill)
    r(342, 44, 402, 160, 22, fill=fill)
    r(130, 88, 238, 154, 14, fill=fill, outline=outline, width=max(1, int(6 * s)))
    r(242, 88, 350, 154, 14, fill=fill, outline=outline, width=max(1, int(6 * s)))
    r(96, 150, 384, 174, 10, fill=fill)
    d.rectangle([(cx + (120 - 240) * s, top + 174 * s), (cx + (146 - 240) * s, top + 198 * s)], fill=fill)
    d.rectangle([(cx + (334 - 240) * s, top + 174 * s), (cx + (360 - 240) * s, top + 198 * s)], fill=fill)


COUCH_H = 198


def make_logo(S):
    """Square badge: dark rounded rect, gold outline, couch, big UNDERPOD."""
    s = S / 480
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([(8 * s, 8 * s), (S - 9 * s, S - 9 * s)], radius=86 * s,
                        fill=(14, 14, 19, 240), outline=ACC, width=max(2, int(7 * s)))
    couch_top = 90 * s
    draw_couch(d, s, S / 2, couch_top)
    f = fit_font(BLACK_F, WORDMARK, S * 0.80, 74 * s, d)
    text_between(d, S / 2, couch_top + COUCH_H * s, S - 9 * s, WORDMARK, f, ACC)
    return img


def make_profile(S=1024):
    """Circle-crop-first: gold square, dark disk with gold ring, couch + wordmark inside."""
    img = Image.new("RGBA", (S, S), ACC)
    d = ImageDraw.Draw(img)
    pad = S * 0.06
    d.ellipse([(pad, pad), (S - pad, S - pad)], fill=DARK, outline=ACC, width=int(S * 0.012))
    s = S / 480 * 0.78
    couch_top = S * 0.26
    draw_couch(d, s, S / 2, couch_top)
    f = fit_font(BLACK_F, WORDMARK, S * 0.60, S * 0.11, d)
    text_between(d, S / 2, couch_top + COUCH_H * s, S - pad - S * 0.05, WORDMARK, f, ACC)
    return img


def outlined(cut, target_h, outline):
    bbox = cut.split()[3].getbbox()
    cut = cut.crop(bbox)
    scale = target_h / cut.height
    img = cut.resize((int(cut.width * scale), int(cut.height * scale)), Image.LANCZOS)
    grown = img.split()[3].filter(ImageFilter.MaxFilter(outline * 2 + 1)).filter(ImageFilter.GaussianBlur(1.2))
    out = Image.composite(Image.new("RGBA", img.size, WHITE), Image.new("RGBA", img.size, (0, 0, 0, 0)), grown)
    out.alpha_composite(img)
    return out


def make_banner(W=2560, H=1440):
    img = Image.new("RGBA", (W, H), BANNER_BG + (255,))
    d = ImageDraw.Draw(img)
    for cx, top in [(2320, 60), (260, 1060)]:
        draw_couch(d, 1.75, cx, top, fill=BANNER_GHOST + (255,), outline=BANNER_BG + (255,))
        gf = font(BLACK_F, 150)
        text_centered(d, cx, top + 420, WORDMARK, gf, BANNER_GHOST + (255,))

    sx0, sy0, sx1, sy1 = (W - 1546) // 2, (H - 423) // 2, (W + 1546) // 2, (H + 423) // 2
    badge = make_logo(400).resize((190, 190), Image.LANCZOS)
    img.alpha_composite(badge, (sx0 + 10, sy0 + 90))

    tx = sx0 + 215
    wf = font(BLACK_F, 120)
    d.text((tx, sy0 + 62), WORDMARK, font=wf, fill=DARK, stroke_width=10, stroke_fill=WHITE)
    tf = font(BOLD_F, 38)
    d.text((tx + 6, sy0 + 228), TAGLINE, font=tf, fill=DARK)
    pf = font(BOLD_F, 30)
    pill = "NEW EPISODES WEEKLY"
    pb = d.textbbox((0, 0), pill, font=pf)
    px, py = tx + 6, sy0 + 300
    d.rounded_rectangle([(px, py), (px + pb[2] + 44, py + pb[3] - pb[1] + 30)], radius=30, fill=DARK)
    d.text((px + 22, py + 15 - pb[1]), pill, font=pf, fill=ACC)

    cluster = Image.open(os.path.join(FACES, "cluster_cut.png")).convert("RGBA")
    ch = 300
    cluster = cluster.resize((int(cluster.width * ch / cluster.height), ch), Image.LANCZOS)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    layer.alpha_composite(cluster, (sx0 + 815, sy1 - 8 - ch))
    layer = layer.crop((0, 0, W, sy1 - 8))
    full = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    full.paste(layer, (0, 0))
    img.alpha_composite(full)
    return img.convert("RGB")


if __name__ == "__main__":
    for S, name in [(480, "logo-480.png"), (1920, "logo-1920.png"), (3000, "logo-3000-cover.png")]:
        make_logo(S).save(os.path.join(HERE, name))
    make_profile().save(os.path.join(HERE, "profile-1024.png"))
    if "--no-banner" not in sys.argv:
        make_banner().save(os.path.join(HERE, "banner-2560.png"))
    print("brand masters regenerated")
