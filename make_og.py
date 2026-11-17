#!/usr/bin/env python3
"""og.png 1200x630 — Puppuccino (2x supersample).
Puppuccino-parlor share art: cream ground, cinnamon ring-halo, monoline cup-and-swirl
with berry cherry, letter-spaced Futura wordmark, sprinkle dashes.
Shop identity only — no builder markers."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
S = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

CREAM = (248, 241, 228); PAPER = (255, 252, 244); INK = (46, 28, 18); SOFT = (110, 84, 67)
CINN = (192, 91, 29); BERRY = (185, 57, 88); SAGE = (117, 131, 91)

def font(paths, size, stroke_ok=False):
    bases = ["/System/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size * S)
                except Exception: pass
    return ImageFont.load_default()

fut = lambda s: font(["Futura.ttc"], s)
futbook = lambda s: font(["Futura.ttc"], s)
geor = lambda s: font(["Georgia.ttf"], s)
geist = lambda s: font(["Georgia Italic.ttf", "Georgia.ttf"], s)

img = Image.new("RGB", (W * S, H * S), CREAM)
d = ImageDraw.Draw(img)

def px(x, y): return (int(x * S), int(y * S))

# cinnamon ring halo behind the art (right side), plus faint berry wash corner
halo = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
hd = ImageDraw.Draw(halo)
cx, cy, R = 950 * S, 315 * S, 0
for i in range(9):
    r = (120 + i * 26) * S
    hd.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(192, 91, 29, 34), width=2 * S)
hd.ellipse((-140 * S, 480 * S, 260 * S, 880 * S), fill=(185, 57, 88, 26))
img = Image.alpha_composite(img.convert("RGBA"), halo).convert("RGB")
d = ImageDraw.Draw(img)

def spaced(cx, y, text, f, fill, ls, sw=0):
    x = cx * S
    if ls:
        widths = [d.textbbox((0, 0), ch, font=f)[2] for ch in text]
        total = sum(widths) + ls * S * (len(text) - 1)
        x -= total / 2
    for ch, cw in zip(text, widths if ls else [0] * len(text)):
        d.text((x + cw / 2, y * S), ch, font=f, fill=fill, anchor="mm", stroke_width=sw * S, stroke_fill=fill)
        if ls: x += cw + ls * S

# left column
lx, tcx = 72, 470
spaced(lx + 4, 64, "SPOKANE VALLEY'S PUPPUCCINO BAR", fut(15), BERRY, 4)

# wordmark: fit width into left area
size = 86
wm = "PUPPUCCINO"
while True:
    f = fut(size)
    bbox = d.textbbox((0, 0), wm, font=f)
    wpx = bbox[2] - bbox[0]
    ls = 5 * S
    if wpx + ls * (len(wm) - 1) < 640 * S or size <= 40: break
    size -= 4
f = fut(size)
x = lx * S
widths = [d.textbbox((0, 0), ch, font=f)[2] for ch in wm]
for ch, cw in zip(wm, widths):
    d.text((x + cw / 2, 128 * S), ch, font=f, fill=INK, anchor="mm", stroke_width=int(1.6 * S), stroke_fill=INK)
    x += cw + ls

spaced(lx + 4, 196, "CUSTOM PUP CUP BAR & PET SHOP", fut(19), (90, 62, 48), 6)

d.text((lx * S, 248 * S), "Frozen pup cups built to order — plus treats,\ntoys and the training gear your dog actually needs.",
       font=geist(24), fill=INK, anchor="la", leading=12 * S)

# sprinkle dashes
yy = 372 * S
xx = lx * S
cols = [(BERRY, 16), (SAGE, 14), (CINN, 18)]
i = 0
while xx < 620 * S:
    c, ln = cols[i % 3]
    d.line((xx, yy + (i % 2) * 8 * S, xx + ln * S, yy + (i % 2) * 8 * S - 4 * S), fill=c, width=4 * S)
    xx += (ln + 14) * S; i += 1

d.text((lx * S, 416 * S), "5802 E Sprague Ave, Spokane Valley, WA 99212", font=fut(21), fill=SOFT, anchor="la")
d.text((lx * S, 448 * S), "(509) 768-1353  ·  puppuccino-demo.up.railway.app", font=fut(17), fill=(150, 118, 96), anchor="la")

# cup-and-swirl art, right side (center ~ (950, 330))
acx, w_ = 950 * S, 2 * S
def line(*pts, fill=INK, wd=5):
    d.line([px(*p) for p in pts], fill=fill, width=int(wd * S), joint="curve")

# cup body (trapezoid with rounded bottom approximated)
cup = [(898, 262), (1002, 262), (992, 448), (908, 448)]
d.polygon([px(*p) for p in [(896, 262), (1004, 262), (994, 452), (906, 452)]], fill=PAPER, outline=INK, width=int(5 * S))
line((916, 300), (911, 430), fill=BERRY, wd=4)
line((984, 300), (989, 430), fill=BERRY, wd=4)
# swirl tiers as stacked top-half ellipses
def tier(cx_, cy_, rx_, ry_):
    box = [(cx_ - rx_) * S, (cy_ - ry_) * S, (cx_ + rx_) * S, (cy_ + ry_) * S]
    d.pieslice(box, 180, 360, fill=PAPER, outline=INK, width=int(5 * S))
tier(950, 262, 62, 34)
tier(950, 226, 50, 27)
tier(950, 197, 38, 20)
tier(950, 175, 26, 14)
# peak curl
line((932, 163), (940, 152), (950, 150), (960, 153), (967, 163), wd=5)
d.ellipse(((950 - 9) * S, (138 - 9) * S, (950 + 9) * S, (138 + 9) * S), fill=BERRY, outline=INK, width=int(3 * S))
# drizzle arcs on tiers
d.arc(((950 - 44) * S, (250 - 12) * S, (950 + 44) * S, (250 + 12) * S), 20, 160, fill=CINN, width=int(3.5 * S))
d.arc(((950 - 34) * S, (214 - 10) * S, (950 + 34) * S, (214 + 10) * S), 20, 160, fill=CINN, width=int(3.5 * S))

# paw badge lower-left of cup
pawx, pawy = 878, 430
pawc = CINN
def ell(cx_, cy_, rx_, ry_):
    d.ellipse(((cx_ - rx_) * S, (cy_ - ry_) * S, (cx_ + rx_) * S, (cy_ + ry_) * S), fill=pawc)
ell(pawx - 12, pawy - 8, 3.6, 4.6); ell(pawx - 4, pawy - 12, 3.6, 4.8)
ell(pawx + 4.5, pawy - 11, 3.4, 4.4); ell(pawx + 11.5, pawy - 4, 3.2, 4.0)
d.pieslice(((pawx - 11) * S, (pawy - 2) * S, (pawx + 11) * S, (pawy + 16) * S), 200, 340, fill=pawc)
d.polygon([px(pawx - 11, pawy + 6), px(pawx + 11, pawy + 6), px(pawx + 8, pawy + 15), px(pawx - 8, pawy + 15)], fill=pawc)

img = img.resize((W, H), Image.LANCZOS)
img.save(OUT, "PNG", optimize=True)
print("og.png ->", OUT, os.path.getsize(OUT), "bytes")
