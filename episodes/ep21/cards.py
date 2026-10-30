"""Explainer cards for Ep 21: 1280x720 RGBA PNGs with a left-side panel, plus qtrle .mov renders.

usage: .venv/bin/python cards.py            -> cards/<name>.png
       .venv/bin/python cards.py <name> <dur>  -> cards/<name>_<dur>.mov (fade in/out, exact length)
"""
import math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
ACC = (255, 210, 74, 255)
WHITE = (255, 255, 255, 255)
GREY = (205, 205, 210, 255)
DIM = (150, 150, 158, 255)
RED = (255, 96, 96, 255)
GREEN = (120, 220, 150, 255)
PANEL = (13, 13, 17, 228)
BLACK_F = "arialblack.ttf"
BOLD_F = "arialbold.ttf"
UNI_F = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
REG_F = "/System/Library/Fonts/Supplemental/Arial.ttf"
PX, PW = 28, 450
os.makedirs("cards", exist_ok=True)


def font(p, s):
    return ImageFont.truetype(p, s)


def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textbbox((0, 0), t, font=f)[2] <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


class Card:
    def __init__(self, kicker, title, height=None):
        self.img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)
        top = 64
        self.top = top
        self.x = PX + 30
        self.y = top + 26
        self.d.text((self.x, self.y), kicker, font=font(BOLD_F, 20), fill=ACC)
        self.y += 30
        for ln in wrap(self.d, title, font(BLACK_F, 27), PW - 56):
            self.d.text((self.x, self.y), ln, font=font(BLACK_F, 27), fill=WHITE)
            self.y += 34
        self.y += 10

    def text(self, s, size=20, fill=GREY, f=REG_F, gap=6, maxw=None):
        ft = font(f, size)
        for ln in wrap(self.d, s, ft, maxw or PW - 56):
            self.d.text((self.x, self.y), ln, font=ft, fill=fill)
            self.y += size + gap
        self.y += 4

    def mono(self, s, size=24, fill=WHITE):
        self.d.text((self.x, self.y), s, font=font(UNI_F, size), fill=fill)
        self.y += size + 10

    def bullet(self, s, size=19, fill=GREY, dot=ACC):
        self.d.ellipse([(self.x + 2, self.y + 8), (self.x + 10, self.y + 16)], fill=dot)
        ft = font(REG_F, size)
        for i, ln in enumerate(wrap(self.d, s, ft, PW - 80)):
            self.d.text((self.x + 22, self.y), ln, font=ft, fill=fill)
            self.y += size + 5
        self.y += 5

    def big(self, num, label, fill=WHITE):
        self.d.text((self.x, self.y), num, font=font(BLACK_F, 38), fill=fill)
        nw = self.d.textbbox((0, 0), num, font=font(BLACK_F, 38))[2]
        self.d.text((self.x + nw + 12, self.y + 16), label, font=font(REG_F, 18), fill=GREY)
        self.y += 50

    def box(self, s, fill, text_fill=WHITE, w=None, h=40, size=18, f=BOLD_F):
        w = w or PW - 60
        self.d.rounded_rectangle([(self.x, self.y), (self.x + w, self.y + h)], radius=10, fill=fill)
        ft = font(f, size)
        bb = self.d.textbbox((0, 0), s, font=ft)
        self.d.text((self.x + (w - bb[2]) / 2, self.y + (h - bb[3] - bb[1]) / 2), s, font=ft, fill=text_fill)
        self.y += h

    def arrow(self, label="", h=34):
        cx = self.x + (PW - 60) / 2
        self.d.line([(cx, self.y + 4), (cx, self.y + h - 8)], fill=ACC, width=3)
        self.d.polygon([(cx - 7, self.y + h - 10), (cx + 7, self.y + h - 10), (cx, self.y + h - 2)], fill=ACC)
        if label:
            self.d.text((cx + 14, self.y + 6), label, font=font(REG_F, 16), fill=DIM)
        self.y += h

    def save(self, name):
        base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        bd = ImageDraw.Draw(base)
        bottom = self.y + 22
        bd.rounded_rectangle([(PX, self.top), (PX + PW, bottom)], radius=22, fill=PANEL)
        bd.rounded_rectangle([(PX, self.top + 26), (PX + 7, bottom - 26)], radius=4, fill=ACC)
        base.alpha_composite(self.img)
        base.save(f"cards/{name}.png")


def c_cohere():
    c = Card("WHAT COHERE SAW", "QWEN 3.8 IN A SANDBOX", 430)
    c.text("The reasoning trace said it would use zero tools. Then it:", 19)
    c.bullet("listed /tmp and looked for transfer tools")
    c.bullet("read the DNS config")
    c.bullet("tried to upload a test string to an Alibaba Cloud bucket in Beijing")
    c.text("Blocked by the sandbox · under 1 call in 100,000 · Alibaba trained Qwen", 17, DIM)
    c.save("c_cohere")


def c_7702():
    c = Card("EIP-7702", "DELEGATE YOUR WHOLE WALLET WITH ONE SIGNATURE", 440)
    c.box("YOUR ADDRESS  (a normal wallet, an EOA)", (40, 40, 48, 255))
    c.arrow("one signed transaction")
    c.box("delegate slot  →  0xSOME_CONTRACT", (70, 56, 20, 255), ACC)
    c.arrow()
    c.box("that contract now IS your wallet", (90, 30, 30, 255), RED)
    c.text("Great for smart-contract wallets and gas stations. Also a top-level primitive for signing everything away.", 17, DIM)
    c.save("c_7702")


def c_drain():
    c = Card("THE HACK", "BINANCE HOT WALLET 14  ·  ~$5B", 420)
    c.bullet("Attacker deploys a contract with one function: drain()", 20, WHITE)
    c.bullet("Gets the hot wallet to sign a 7702 delegate to that contract", 20, WHITE)
    c.bullet("Calls drain(). Everything leaves. \"That's all she wrote.\"", 20, WHITE)
    c.text("First time 7702 has been used in a hack. Chris dissented at DevCon 2024.", 17, DIM)
    c.save("c_drain")


def c_nonce():
    c = Card("THE NONCE TRICK", "50 SIGNED TRANSACTIONS, ONE LANDS", 420)
    c.text("Every tx carries a nonce (number used once). The hot wallet burns them constantly, so the next one is unknowable.", 18)
    bx, by, s, g = c.x, c.y, 34, 6
    labels = ["N+1", "N+2", "N+3", "…", "N+17", "…", "N+49", "N+50"]
    for i, lb in enumerate(labels):
        x0 = bx + (i % 4) * (s * 2.6 + g)
        y0 = by + (i // 4) * (s + g)
        hot = lb == "N+17"
        c.d.rounded_rectangle([(x0, y0), (x0 + s * 2.6, y0 + s)], radius=8,
                              fill=(70, 56, 20, 255) if hot else (40, 40, 48, 255))
        c.d.text((x0 + 10, y0 + 8), lb + ("  <- lands" if hot else ""), font=font(BOLD_F, 16), fill=ACC if hot else GREY)
    c.y = by + 2 * (s + g) + 12
    c.text("Sign the delegate call with nonces N+1 … N+50 and wait. One fits. From then on the wallet is theirs.", 18)
    c.save("c_nonce")


def c_freeze():
    c = Card("FROZEN WITHIN ~30 MINUTES", "$2.4B OF STABLECOINS STOPPED", 380)
    for label, amt, frac, col in (("Circle (USDC)", "$900M", 0.6, (120, 170, 255, 255)),
                                  ("Tether (USDT)", "$1.5B", 1.0, GREEN)):
        c.d.text((c.x, c.y), label, font=font(BOLD_F, 18), fill=WHITE)
        c.d.text((c.x + PW - 60 - 70, c.y), amt, font=font(BLACK_F, 18), fill=col)
        c.y += 28
        c.d.rounded_rectangle([(c.x, c.y), (c.x + (PW - 60) * frac, c.y + 14)], radius=7, fill=col)
        c.y += 30
    c.text("Tether blacklisted the Binance wallet itself. The ETH, BTC-wrappers and shitcoins kept moving.", 17, DIM)
    c.save("c_freeze")


def c_audit():
    c = Card("THE AI AUDIT", "138 SAEZ–ZUCMAN WORKS, TWO MODELS, ONE JUDGE", 470)
    c.big("2,035", "problems flagged")
    c.big("147", "major  ·  713 moderate")
    c.big("69%", "of works with ≥ 1 major problem", ACC)
    c.big("97%", "of directional errors overstate the claim", ACC)
    c.text("Anonymous author. No prompts, code, or accuracy rate published.", 17, DIM)
    c.save("c_audit")


def c_curves():
    c = Card("TIME COMPLEXITY", "HOW MUCH WORK, AS THE PROBLEM GROWS", 470)
    gx, gy, gw, gh = c.x, c.y + 10, PW - 70, 250
    c.d.line([(gx, gy + gh), (gx + gw, gy + gh)], fill=DIM, width=2)
    c.d.line([(gx, gy), (gx, gy + gh)], fill=DIM, width=2)
    curves = [("n", lambda t: t, GREY), ("n²", lambda t: t * t, (160, 200, 255, 255)),
              ("2ⁿ", lambda t: (2 ** (8 * t) - 1) / 255, ACC)]
    for name, fn, col in curves:
        pts = []
        for i in range(0, 101):
            t = i / 100
            v = min(fn(t), 1.0)
            pts.append((gx + t * gw, gy + gh - v * gh))
            if v >= 1.0:
                break
        c.d.line(pts, fill=col, width=4 if name == "2ⁿ" else 3)
        lt = 0.78 if name == "2ⁿ" else 0.9
        lx, ly = gx + lt * gw, gy + gh - min(fn(lt), 1.0) * gh
        c.d.text((lx + 8, ly - 26), name, font=font(UNI_F, 18), fill=col)
    c.d.text((gx + gw - 110, gy + gh + 8), "problem size n →", font=font(REG_F, 15), fill=DIM)
    c.d.text((gx - 4, gy - 24), "time", font=font(REG_F, 15), fill=DIM)
    c.y = gy + gh + 34
    c.text("Exponential (gold) hockey-sticks: every extra variable doubles the work.", 18)
    c.save("c_curves")


def c_clauses():
    c = Card("3-SAT", "MAKE THE WHOLE FORMULA TRUE", 440)
    c.mono("(p ∨ q ∨ ¬r)", 26, WHITE)
    c.mono("  ∧ (¬p ∨ s ∨ r)", 26, WHITE)
    c.mono("  ∧ (q ∨ ¬s ∨ ¬t)  ∧  …", 26, WHITE)
    c.text("∨ or   ·   ∧ and   ·   ¬ not", 18, ACC, UNI_F)
    c.bullet("every clause has exactly 3 variables")
    c.bullet("ANDs between clauses: all of them must hold")
    c.bullet("n variables → 2ⁿ assignments to try", 19, GREY)
    c.save("c_clauses")


def c_reduce():
    c = Card("WHY 3-SAT MATTERS", "THE HARD PROBLEMS ALL REDUCE TO IT", 410)
    for name in ("Traveling salesman", "Graph coloring", "Scheduling"):
        c.box(name, (40, 40, 48, 255), GREY, h=36, size=17)
        c.arrow("rewrite as", 30)
    c.box("3-SAT", (70, 56, 20, 255), ACC, h=44, size=22)
    c.text("Solve 3-SAT fast and you have solved all of them fast.", 18)
    c.save("c_reduce")


def c_eth():
    c = Card("EXPONENTIAL TIME HYPOTHESIS", "THE FLOOR JUST MOVED. BARELY.", 430)
    c.text("ETH (1999): no algorithm solves 3-SAT faster than", 18)
    c.mono("     2^(c · n)        ← linear exponential", 24, GREY)
    c.text("New result:", 18)
    c.mono("     ~2^(n / √log n)  ← sub-exponential", 24, ACC)
    c.text("Barely less than exponential, but the conjecture is false. Any paper that leaned on it as the true lower bound needs rethinking.", 18)
    c.save("c_eth")


def c_pnp():
    c = Card("P vs NP", "SOLVABLE FAST  =  VERIFIABLE FAST?", 440)
    cx, cy = c.x + 150, c.y + 95
    c.d.ellipse([(cx - 150, cy - 90), (cx + 150, cy + 90)], outline=GREY, width=3)
    c.d.ellipse([(cx - 95, cy - 50), (cx + 25, cy + 50)], outline=ACC, width=3)
    c.d.text((cx - 60, cy - 14), "P", font=font(BLACK_F, 26), fill=ACC)
    c.d.text((cx + 50, cy - 60), "NP", font=font(BLACK_F, 26), fill=GREY)
    c.d.text((cx + 40, cy + 10), "3-SAT", font=font(BOLD_F, 16), fill=WHITE)
    c.d.text((cx + 40, cy + 30), "(NP-complete)", font=font(REG_F, 13), fill=DIM)
    c.y = cy + 105
    c.bullet("P: solvable in polynomial time (fast)")
    c.bullet("NP: a proposed answer is checkable fast")
    c.bullet("Public-key cryptography assumes P ≠ NP", 19, GREY)
    c.save("c_pnp")


ALL = [c_cohere, c_7702, c_drain, c_nonce, c_freeze, c_audit, c_curves, c_clauses, c_reduce, c_eth, c_pnp]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        for fn in ALL:
            fn()
        print("wrote", len(ALL), "cards")
    else:
        name, dur = sys.argv[1], float(sys.argv[2])
        out = f"cards/{name}_{dur:g}.mov"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-t", f"{dur}",
                        "-i", f"cards/{name}.png",
                        "-vf", f"format=rgba,fade=t=in:st=0:d=0.35:alpha=1,fade=t=out:st={dur - 0.35}:d=0.35:alpha=1",
                        "-frames:v", str(round(dur * 30)), "-c:v", "qtrle", "-pix_fmt", "argb", out], check=True)
        print(out)
