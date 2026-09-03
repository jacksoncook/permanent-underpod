#!/usr/bin/env python3
"""Ep 13 extras: the animated LIKE + SUBSCRIBE overlay (alpha .mov) with its
click/bell sound, and the 'Will Smith spaghetti' editor's card.

usage: media/ep12/work/.venv/bin/python episodes/ep13/build_extras.py media/ep13/work <scratchdir>
Rebuilds likesub.mov + sfx_likesub.wav + card_spaghetti.mov into the workdir (media/ is gitignored).
"""
import math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

WORK, SCR = sys.argv[1], sys.argv[2]
W, H, FPS = 1280, 720, 30
ACC = (255, 210, 74, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 51, 255)
BLACK_F = os.path.join(WORK, "arialblack.ttf")
BOLD_F = os.path.join(WORK, "arialbold.ttf")
EMOJI_F = "/System/Library/Fonts/Apple Color Emoji.ttc"
for src, dst in [("Arial Black.ttf", BLACK_F), ("Arial Bold.ttf", BOLD_F)]:
    if not os.path.exists(dst):
        subprocess.run(["cp", f"/System/Library/Fonts/Supplemental/{src}", dst])

font = lambda p, s: ImageFont.truetype(p, s)


def emoji(ch, size):
    f = ImageFont.truetype(EMOJI_F, 160)
    img = Image.new("RGBA", (220, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((110, 110), ch, font=f, embedded_color=True, anchor="mm")
    bb = img.getbbox()
    img = img.crop(bb)
    s = size / max(img.size)
    return img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))), Image.LANCZOS)


def ease_out_cubic(t):
    t = min(1, max(0, t)); return 1 - (1 - t) ** 3


def ease_in_out(t):
    t = min(1, max(0, t)); return t * t * (3 - 2 * t)


def ease_out_back(t):
    t = min(1, max(0, t)); c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def shadow(size, radius, blur, alpha):
    pad = blur * 3
    img = Image.new("RGBA", (size[0] + 2 * pad, size[1] + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(img).rounded_rectangle([pad, pad, pad + size[0], pad + size[1]],
                                          radius=radius, fill=(0, 0, 0, alpha))
    return img.filter(ImageFilter.GaussianBlur(blur)), pad


def cursor(scale=1.0):
    s = int(40 * scale)
    img = Image.new("RGBA", (s + 6, s + 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pts = [(2, 2), (2, s), (s * 0.30, s * 0.74), (s * 0.48, s + 4), (s * 0.62, s - 2),
           (s * 0.44, s * 0.62), (s * 0.78, s * 0.62)]
    d.polygon(pts, fill=WHITE, outline=(20, 20, 24, 255), width=2)
    return img


THUMB = emoji("👍", 62)
BELL = emoji("🔔", 60)
BIG_THUMB = emoji("👍", 200)

# --- timeline (frames) ---
N = 180
T_IN0, T_IN1 = 0, 14
T_LIKE, T_SUB, T_BELL = 40, 78, 112
T_CUR_OUT0, T_CUR_OUT1 = 122, 142
T_OUT0, T_OUT1 = 165, 180

PW, PH, PR = 700, 118, 59
PX = (W - PW) // 2
PY_FINAL = 566

LIKE_C = (PX + 92, PY_FINAL + PH // 2)
SUB_BOX = (PX + 176, PY_FINAL + 27, PX + 520, PY_FINAL + PH - 27)
BELL_C = (PX + 610, PY_FINAL + PH // 2)

rng = np.random.default_rng(13)
PARTS = [(rng.uniform(0, 2 * math.pi), rng.uniform(70, 150), rng.uniform(4, 9)) for _ in range(16)]
BELL_PARTS = [(rng.uniform(-2.6, -0.5), rng.uniform(50, 110), rng.uniform(3, 6)) for _ in range(9)]

os.makedirs(f"{SCR}/ls", exist_ok=True)


def cursor_pos(i):
    if i < T_IN1:
        return None
    if i <= T_LIKE:
        t = ease_in_out((i - T_IN1) / (T_LIKE - T_IN1))
        x0, y0 = W + 40, H + 40
        return (x0 + (LIKE_C[0] - x0) * t, y0 + (LIKE_C[1] - y0) * t)
    if i <= T_SUB:
        t = ease_in_out((i - T_LIKE - 10) / (T_SUB - T_LIKE - 10))
        sx, sy = (SUB_BOX[0] + SUB_BOX[2]) / 2, (SUB_BOX[1] + SUB_BOX[3]) / 2
        return (LIKE_C[0] + (sx - LIKE_C[0]) * t, LIKE_C[1] + (sy - LIKE_C[1]) * t)
    if i <= T_BELL:
        t = ease_in_out((i - T_SUB - 8) / (T_BELL - T_SUB - 8))
        sx, sy = (SUB_BOX[0] + SUB_BOX[2]) / 2, (SUB_BOX[1] + SUB_BOX[3]) / 2
        return (sx + (BELL_C[0] - sx) * t, sy + (BELL_C[1] - sy) * t)
    if i <= T_CUR_OUT1:
        t = ease_in_out((i - T_CUR_OUT0) / (T_CUR_OUT1 - T_CUR_OUT0)) if i >= T_CUR_OUT0 else 0
        return (BELL_C[0] + 140 * t, BELL_C[1] + 260 * t)
    return None


for i in range(N):
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if i < T_IN1:
        py = H + 20 + (PY_FINAL - H - 20) * ease_out_back(i / T_IN1)
    elif i >= T_OUT0:
        py = PY_FINAL + (H + 20 - PY_FINAL) * ease_in_out((i - T_OUT0) / (T_OUT1 - T_OUT0))
    else:
        py = PY_FINAL
    dy = py - PY_FINAL
    sh, pad = shadow((PW, PH), PR, 14, 150)
    frame.alpha_composite(sh, (PX - pad, int(py) - pad + 10))
    panel = Image.new("RGBA", (PW, PH), (0, 0, 0, 0))
    d = ImageDraw.Draw(panel)
    d.rounded_rectangle([0, 0, PW - 1, PH - 1], radius=PR, fill=(14, 14, 19, 222),
                        outline=(255, 210, 74, 200), width=3)
    d.rounded_rectangle([4, 4, PW - 5, PH // 2], radius=PR - 4, fill=(255, 255, 255, 12))
    frame.alpha_composite(panel, (PX, int(py)))
    d = ImageDraw.Draw(frame)

    # LIKE
    liked = i >= T_LIKE
    pop = 1.0
    if T_LIKE <= i < T_LIKE + 12:
        u = (i - T_LIKE) / 12
        pop = 1 + 0.38 * math.sin(u * math.pi)
    r = int(42 * pop)
    cx, cy = LIKE_C[0], LIKE_C[1] + dy
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ACC if liked else (44, 44, 52, 255),
              outline=ACC, width=3)
    th = THUMB.resize((int(THUMB.width * pop), int(THUMB.height * pop)), Image.LANCZOS)
    frame.alpha_composite(th, (int(cx - th.width / 2), int(cy - th.height / 2)))
    if T_LIKE <= i < T_LIKE + 20:
        u = (i - T_LIKE) / 20
        for ang, dist, sz in PARTS:
            px = cx + math.cos(ang) * dist * ease_out_cubic(u)
            pyy = cy + math.sin(ang) * dist * ease_out_cubic(u) + 40 * u * u
            s = sz * (1 - u)
            a = int(255 * (1 - u))
            d.ellipse([px - s, pyy - s, px + s, pyy + s], fill=(255, 210, 74, a))

    # SUBSCRIBE
    subbed = i >= T_SUB
    x0, y0, x1, y1 = SUB_BOX
    y0 += dy; y1 += dy
    press = 1.0
    if T_SUB <= i < T_SUB + 6:
        press = 0.94
    bw, bh = (x1 - x0) * press, (y1 - y0) * press
    bx0, by0 = (x0 + x1) / 2 - bw / 2, (y0 + y1) / 2 - bh / 2
    d.rounded_rectangle([bx0, by0, bx0 + bw, by0 + bh], radius=int(bh / 2),
                        fill=(40, 40, 46, 255) if subbed else RED,
                        outline=ACC if subbed else RED, width=3)
    label = "SUBSCRIBED" if subbed else "SUBSCRIBE"
    f = font(BLACK_F, 30 if subbed else 34)
    bb = d.textbbox((0, 0), label, font=f)
    tw = bb[2] - bb[0]
    check_w = 34 if subbed else 0
    tx = (x0 + x1) / 2 - (tw + check_w) / 2 - bb[0]
    ty = (y0 + y1) / 2 - (bb[3] - bb[1]) / 2 - bb[1]
    d.text((tx, ty), label, font=f, fill=ACC if subbed else WHITE)
    if subbed:
        cx0 = tx + bb[0] + tw + 12
        cy = (y0 + y1) / 2
        d.line([(cx0, cy), (cx0 + 8, cy + 9), (cx0 + 22, cy - 11)], fill=ACC, width=5, joint="curve")
    if T_SUB <= i < T_SUB + 22:
        u = (i - T_SUB) / 22
        rx, ry = (x1 - x0) / 2 + 60 * u, (y1 - y0) / 2 + 60 * u
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        d.rounded_rectangle([mx - rx, my - ry, mx + rx, my + ry], radius=int(ry),
                            outline=(255, 210, 74, int(220 * (1 - u))), width=3)

    # BELL
    bx, by = BELL_C[0], BELL_C[1] + dy
    rung = i >= T_BELL
    ang = 0.0
    if T_BELL <= i < T_BELL + 36:
        u = (i - T_BELL) / 36
        ang = 28 * math.sin(u * math.pi * 3.5) * (1 - u)
    br = 42
    d.ellipse([bx - br, by - br, bx + br, by + br], fill=(44, 44, 52, 255),
              outline=ACC, width=3)
    bell = BELL.rotate(ang, resample=Image.BICUBIC, expand=True)
    frame.alpha_composite(bell, (int(bx - bell.width / 2), int(by - bell.height / 2)))
    if rung:
        d.ellipse([bx + 24, by - 36, bx + 40, by - 20], fill=RED)
    if T_BELL <= i < T_BELL + 18:
        u = (i - T_BELL) / 18
        for a0, dist, sz in BELL_PARTS:
            px = bx + math.cos(a0) * dist * ease_out_cubic(u)
            pyy = by + math.sin(a0) * dist * ease_out_cubic(u)
            s = sz * (1 - u)
            d.ellipse([px - s, pyy - s, px + s, pyy + s], fill=(255, 210, 74, int(255 * (1 - u))))

    # kicker above the pill
    if T_IN1 <= i < T_OUT0:
        a = int(255 * min(1, (i - T_IN1) / 8))
        f = font(BOLD_F, 22)
        k = "F R E E   ·   T A K E S   2   S E C O N D S   ·   H E L P S   T H E   P O D"
        bb = d.textbbox((0, 0), k, font=f)
        d.text((W / 2 - (bb[2] - bb[0]) / 2, py - 34), k, font=f, fill=(255, 210, 74, a))

    cp = cursor_pos(i)
    if cp is not None:
        clicking = any(t <= i < t + 4 for t in (T_LIKE, T_SUB, T_BELL))
        cur = cursor(0.85 if clicking else 1.0)
        frame.alpha_composite(cur, (int(cp[0]), int(cp[1])))

    frame.save(f"{SCR}/ls/f{i:04d}.png")

subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-framerate", str(FPS),
                "-i", f"{SCR}/ls/f%04d.png", "-c:v", "qtrle", "-pix_fmt", "argb",
                os.path.join(WORK, "likesub.mov")], check=True)

# --- sound: three soft clicks + a bell ding, in one 6 s file ---
SR = 48000
buf = np.zeros(int(6.0 * SR), np.float32)

def add(t0, sig):
    i0 = int(t0 * SR); n = min(len(sig), len(buf) - i0)
    buf[i0:i0 + n] += sig[:n]

def click(f0=1500, dur=0.045, amp=0.35):
    t = np.arange(int(dur * SR)) / SR
    env = np.exp(-t * 90)
    return (amp * env * np.sin(2 * np.pi * f0 * t) + 0.12 * env * rng.standard_normal(len(t))).astype(np.float32)

def ding(t0f=1760.0, dur=0.9, amp=0.28):
    t = np.arange(int(dur * SR)) / SR
    env = np.exp(-t * 4.5)
    s = np.sin(2 * np.pi * t0f * t) + 0.5 * np.sin(2 * np.pi * t0f * 2.76 * t) * np.exp(-t * 8) \
        + 0.3 * np.sin(2 * np.pi * t0f * 5.4 * t) * np.exp(-t * 14)
    return (amp * env * s).astype(np.float32)

add(T_IN0 / FPS + 0.1, click(900, 0.06, 0.22))
add(T_LIKE / FPS, click(1500))
add(T_SUB / FPS, click(1100))
add(T_BELL / FPS, click(1600, 0.03, 0.25))
add(T_BELL / FPS + 0.02, ding())
buf = np.clip(buf, -0.8, 0.8)
with wave.open(os.path.join(WORK, "sfx_likesub.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((buf * 32767).astype(np.int16).tobytes())

# --- the spaghetti card ---
src = "/Users/jcook/Personal/permanent-underpod/media/ep13/work/src/jackson_720.mp4"
bg_png = os.path.join(WORK, "bg_spaghetti.png")
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", "998.5", "-i", src,
                "-frames:v", "1", bg_png], check=True)
img = Image.open(bg_png).convert("RGB").resize((W, H)).filter(ImageFilter.GaussianBlur(22))
img = Image.blend(img, Image.new("RGB", (W, H), (10, 10, 14)), 0.6).convert("RGBA")
d = ImageDraw.Draw(img)
sp = emoji("🍝", 170)
img.alpha_composite(sp, ((W - sp.width) // 2, 118))
def center(y, text, f, fill):
    bb = d.textbbox((0, 0), text, font=f)
    d.text(((W - bb[2] + bb[0]) / 2, y), text, font=f, fill=fill)
center(318, "WILL SMITH EATING SPAGHETTI", font(BLACK_F, 52), ACC)
d.line([(W / 2 - 220, 392), (W / 2 + 220, 392)], fill=ACC, width=3)
center(412, "[ video not provided to the editor ]", font(BOLD_F, 34), (235, 235, 235, 255))
center(478, "— Claude, who was told \"cut this by the way\" and did", font(BOLD_F, 24), (170, 170, 178, 255))
img.convert("RGB").save(os.path.join(WORK, "png_spaghetti.png"))
dur = 3.4
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-loop", "1", "-t", str(dur), "-i", os.path.join(WORK, "png_spaghetti.png"),
                "-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=mono",
                "-filter_complex",
                f"[0:v]fps=30,format=yuv420p,fade=t=in:st=0:d=0.4,fade=t=out:st={dur-0.5}:d=0.5[v]",
                "-map", "[v]", "-map", "1:a", "-c:v", "h264_videotoolbox", "-b:v", "10M",
                "-c:a", "pcm_s16le", "-shortest", os.path.join(WORK, "card_spaghetti.mov")], check=True)
print("wrote likesub.mov, sfx_likesub.wav, card_spaghetti.mov")
