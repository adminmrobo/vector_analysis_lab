# -*- coding: utf-8 -*-
"""대체 표지(글자 없음): 픽셀풍 표지를 받기 전까지 쓰는 임시 그림.
흰 바탕 + 네 개의 자(직교·원통·구·휜 격자) 아이콘 + 연구실 식구 192px 그림."""
import math, pathlib
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
P192 = pathlib.Path('/home/claude/adminmrobo/ahnboat_lab_explainer/packs/character/character_pack/webp/192')
W, H = 1600, 900
NAVY, TEAL, ORG, RED, GRID = (36, 52, 92), (31, 122, 140), (212, 105, 31), (192, 57, 43), (234, 238, 244)

def spr(who, e, h):
    im = Image.open(P192 / who / f'{who}_{e}.webp').convert('RGBA')
    s = h / im.height
    return im.resize((max(1, int(im.width * s)), h), Image.NEAREST)

def base():
    im = Image.new('RGB', (W, H), (255, 255, 255))
    d = ImageDraw.Draw(im)
    for x in range(0, W, 32):
        d.line([(x, 0), (x, H)], fill=(246, 248, 251))
    for y in range(0, H, 32):
        d.line([(0, y), (W, y)], fill=(246, 248, 251))
    return im, d

def frame(d, box, col):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, 18, outline=col, width=6, fill=(255, 255, 255))
    d.rectangle((x0 + 6, y0 + 6, x1 - 6, y0 + 22), fill=col)

def icon(d, kind, cx, cy, s):
    if kind == 'cart':
        for (dx, dy), c in [((s, 0.35 * s), ORG), ((-0.8 * s, 0.45 * s), TEAL), ((0, -s), NAVY)]:
            d.line([(cx, cy), (cx + dx, cy + dy)], fill=c, width=9)
            d.ellipse((cx + dx - 9, cy + dy - 9, cx + dx + 9, cy + dy + 9), fill=c)
    elif kind == 'cyl':
        d.ellipse((cx - s, cy + 0.25 * s, cx + s, cy + 0.75 * s), outline=TEAL, width=8)
        d.ellipse((cx - s, cy - 0.95 * s, cx + s, cy - 0.45 * s), outline=TEAL, width=6)
        d.line([(cx - s, cy - 0.7 * s), (cx - s, cy + 0.5 * s)], fill=TEAL, width=6)
        d.line([(cx + s, cy - 0.7 * s), (cx + s, cy + 0.5 * s)], fill=TEAL, width=6)
        d.line([(cx, cy + 0.5 * s), (cx + 0.75 * s, cy + 0.66 * s)], fill=ORG, width=8)
    elif kind == 'sph':
        d.ellipse((cx - s, cy - s, cx + s, cy + s), outline=NAVY, width=8)
        d.ellipse((cx - s, cy - 0.3 * s, cx + s, cy + 0.3 * s), outline=NAVY, width=4)
        d.ellipse((cx - 0.35 * s, cy - s, cx + 0.35 * s, cy + s), outline=NAVY, width=4)
        d.line([(cx, cy), (cx + 0.55 * s, cy - 0.6 * s)], fill=RED, width=8)
    else:
        for i in range(-2, 3):
            pts = [(cx - s + t * 2 * s / 20, cy + i * 0.38 * s + 0.25 * s * math.sin(t / 20 * math.pi)) for t in range(21)]
            d.line(pts, fill=ORG, width=5)
            pts = [(cx + i * 0.38 * s + 0.2 * s * math.sin(t / 20 * math.pi), cy - s + t * 2 * s / 20) for t in range(21)]
            d.line(pts, fill=TEAL, width=5)

def cards(d, y0, y1, xs):
    cols = [ORG, TEAL, NAVY, (122, 63, 214)]
    kinds = ['cart', 'cyl', 'sph', 'gen']
    for i, x in enumerate(xs):
        frame(d, (x, y0, x + 250, y1), cols[i])
        icon(d, kinds[i], x + 125, (y0 + y1) / 2 + 10, 70)

PENDING = []

def cast(im, items, y_bottom, x0=200, x1=1560):
    """캐릭터는 픽셀화하지 않고 원래 도트 그대로(1배 192px 또는 1/2배 96px) 마지막에 얹는다."""
    SMALL = ('x1', 'x2', 'x3', 'fly', 'robo')
    sp = []
    for who, e, h, _ in items:
        img = Image.open(P192 / who / f'{who}_{e}.webp').convert('RGBA')
        if who in SMALL:
            img = img.resize((img.width // 2, img.height // 2), Image.NEAREST)
        sp.append(img)
    total = sum(t.width for t in sp)
    gap = max(8, (x1 - x0 - total) / max(1, len(sp) - 1))
    x = x0 + max(0, (x1 - x0 - total - gap * (len(sp) - 1)) / 2)
    for t in sp:
        PENDING.append((t, (int(x), int(y_bottom - t.height))))
        x += t.width + gap

def pixelate(im, f=4, colors=40):
    small = im.resize((W // f, H // f), Image.BOX).quantize(colors=colors, method=Image.Quantize.MEDIANCUT).convert('RGB')
    return small.resize((W, H), Image.NEAREST)

def save(im, name):
    im = pixelate(im)
    for t, pos in PENDING:
        im.paste(t, pos, t)
    PENDING.clear()
    im.save(ROOT / 'assets' / f'{name}.webp', 'WEBP', quality=86)
    if name == 'cover_index':
        im.resize((1200, 630), Image.LANCZOS).save(ROOT / 'assets/og/index.webp', 'WEBP', quality=82)
    th = im.crop((200, 0, 1550, 900)).resize((600, 400), Image.LANCZOS)
    th.save(ROOT / 'assets/thumbs' / f'{name.replace("cover_", "")}.webp', 'WEBP', quality=80)
    im.resize((1200, 630), Image.LANCZOS).save(ROOT / 'assets/og' / f'{name.replace("cover_", "")}.webp', 'WEBP', quality=82)

# 목차 표지: 네 장의 카드 앞, 긴장한 하루와 식구들
im, d = base()
cards(d, 120, 420, [250, 560, 870, 1180])
cast(im, [('x1', 'e15', 150, 260), ('x2', 'e02', 165, 380), ('x3', 'e04', 110, 510),
          ('sia', 'e09', 250, 640), ('asst', 'e20', 270, 830), ('moa', 'e12', 245, 1040),
          ('doc', 'e08', 290, 1230), ('fly', 'e08', 130, 1420), ('robo', 'e09', 210, 1440)], 760)
save(im, 'cover_index')

# 0편: 네 개의 자 소개 — 하루가 카드 앞에서 설명 시작
im, d = base()
cards(d, 110, 410, [430, 720, 1010, 1300])
cast(im, [('asst', 'e07', 300, 240), ('sia', 'e19', 240, 560), ('moa', 'e09', 235, 760),
          ('robo', 'e13', 200, 980), ('fly', 'e10', 130, 1180), ('doc', 'e09', 270, 1320)], 770)
save(im, 'cover_00')

# 1부: 생활 — 피자·지구본·지하철역 상징(도형)과 식구들
im, d = base()
d.ellipse((260, 140, 560, 440), fill=(253, 224, 170), outline=ORG, width=10)
d.pieslice((260, 140, 560, 440), -60, -15, fill=(240, 160, 80), outline=RED, width=6)
d.ellipse((680, 150, 960, 430), outline=NAVY, width=9)
for k in (-0.6, -0.2, 0.2, 0.6):
    y = 290 + k * 140
    half = 140 * math.sqrt(1 - k * k)
    d.line([(820 - half, y), (820 + half, y)], fill=TEAL, width=4)
d.ellipse((770, 150, 870, 430), outline=TEAL, width=4)
d.rounded_rectangle((1080, 200, 1380, 400), 30, outline=TEAL, width=8)
for i in range(5):
    d.line([(1110 + i * 60, 420), (1140 + i * 60, 480)], fill=ORG, width=7)
    d.line([(1140 + i * 60, 180), (1110 + i * 60, 120)], fill=NAVY, width=7)
cast(im, [('x1', 'e15', 140, 250), ('x2', 'e02', 155, 360), ('x3', 'e04', 100, 480),
          ('moa', 'e04', 240, 600), ('asst', 'e15', 265, 790), ('sia', 'e09', 245, 990),
          ('fly', 'e08', 130, 1180), ('robo', 'e09', 205, 1290), ('doc', 'e07', 270, 1400)], 780)
save(im, 'cover_01')
print('covers ok')

# 2부: 경제 — 경기시계·동전 삼각형·막대
im, d = base()
cx, cy, R = 400, 290, 150
for i, c in enumerate([(230, 243, 245), (234, 246, 238), (253, 240, 230), (244, 238, 249)]):
    d.pieslice((cx - R, cy - R, cx + R, cy + R), 180 + 90 * i, 270 + 90 * i, fill=c, outline=NAVY, width=4)
d.line([(cx, cy), (cx + 100, cy + 100)], fill=RED, width=10)
for i, (x, y) in enumerate([(820, 400), (960, 160), (1100, 400)]):
    d.ellipse((x - 55, y - 55, x + 55, y + 55), fill=(255, 236, 170), outline=ORG, width=8)
d.line([(820, 400), (960, 160), (1100, 400), (820, 400)], fill=TEAL, width=6)
for i, hgt in enumerate([180, -140, -60, 20]):
    x = 1240 + i * 70
    y0 = 300
    d.rectangle((x, min(y0, y0 - hgt), x + 50, max(y0, y0 - hgt)), fill=ORG if hgt > 0 else NAVY)
d.line([(1220, 300), (1540, 300)], fill=(28, 34, 48), width=4)
cast(im, [('x1', 'e15', 140, 0), ('x2', 'e09', 150, 0), ('x3', 'e04', 100, 0), ('sia', 'e19', 240, 0), ('asst', 'e15', 265, 0),
          ('moa', 'e09', 245, 0), ('fly', 'e10', 130, 0), ('robo', 'e09', 205, 0), ('doc', 'e07', 270, 0)], 780)
save(im, 'cover_02')

# 3부: AI — 점 구름 구·관계망·시계판
im, d = base()
cx, cy, R = 420, 290, 170
d.ellipse((cx - R, cy - R, cx + R, cy + R), outline=NAVY, width=8)
for k in range(60):
    a = k * 2.399
    rr = R * math.sqrt((k + 0.5) / 60)
    d.ellipse((cx + rr * math.cos(a) - 6, cy + rr * math.sin(a) - 6, cx + rr * math.cos(a) + 6, cy + rr * math.sin(a) + 6), fill=TEAL)
nodes = [(820, 200), (950, 140), (1060, 240), (930, 330), (800, 380), (1100, 390)]
for a, b in [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (2, 5), (3, 5)]:
    d.line([nodes[a], nodes[b]], fill=(154, 163, 176), width=5)
for i, (x, y) in enumerate(nodes):
    d.ellipse((x - 26, y - 26, x + 26, y + 26), fill=ORG if i == 3 else (255, 255, 255), outline=NAVY, width=6)
d.ellipse((1250, 140, 1510, 400), outline=(122, 63, 214), width=8)
for m in range(12):
    t = math.radians(90 - m * 30)
    d.ellipse((1380 + 115 * math.cos(t) - 9, 270 - 115 * math.sin(t) - 9, 1380 + 115 * math.cos(t) + 9, 270 - 115 * math.sin(t) + 9), fill=(122, 63, 214))
d.line([(1380, 270), (1380, 175)], fill=RED, width=8)
cast(im, [('x1', 'e01', 140, 0), ('x2', 'e16', 150, 0), ('x3', 'e01', 100, 0), ('moa', 'e19', 240, 0), ('asst', 'e16', 270, 0),
          ('sia', 'e12', 245, 0), ('fly', 'e08', 130, 0), ('robo', 'e13', 205, 0), ('doc', 'e16', 270, 0)], 780)
save(im, 'cover_03')
print('covers 02 03 ok')
