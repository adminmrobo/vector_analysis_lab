# -*- coding: utf-8 -*-
"""docs/IMAGE_PROMPTS.md 생성 — 16비트 RPG 픽셀아트 기본 규칙(SPACE_COORDINATE_GUIDE 11-1)"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

HEAD = ("Match the art style, proportions and colors of the attached reference images exactly "
        "(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).")
TAIL = ("Pixel art only: visible square pixels, limited palette, no smooth gradients, no painterly or 3D-render look. "
        "No text, letters, numbers or symbols anywhere in the image; leave any speech bubbles empty. "
        "Keep faces and hands inside the safe area (12% from left and right edges, 10% from top, 18% from bottom). "
        "Keep the bottom-left corner empty. Bright white daytime lab palette with teal, orange and navy accents.")
C = {'sia': "- Sia: young woman, long straight black hair, dark eyes, black maid-style lab uniform with white apron and gray bow.",
     'moa': "- Moa: young woman, long light-brown hair with white frilled headband, mustard maid-style lab cardigan with red striped bow.",
     'doc': "- The professor: middle-aged man, spiky black hair with one white streak, teal glasses, white lab coat over black vest and tie.",
     'haru': "- Haru the assistant: young woman, pink hair with blue streaks in two side buns, lavender hoodie under a white lab coat.",
     'fly': "- The fruit-fly researcher: a fruit fly wearing a blue round helmet with big red compound-eye goggles and cables, transparent wings.",
     'robo': "- The abacus robot: small robot with a beige monitor head showing a simple green face, antenna, abacus-frame body, tank treads.",
     'x': "- X1, X2, X3: three small dark navy-black silhouettes with white dot eyes (one with a pink ribbon, one with a beret and teal glasses, one small cat-eared one with a yellow bell), sitting in a small audience row."}

# (파일, 비율·크기, 쓰는 곳, 장면 영어 문장, 캐릭터)
COVERS = [
 ('cover_index', '16:9 · 1600×900', '목차 표지·og', "A white pixel-art lab classroom. On the front wall hang four large framed cards side by side, each with a simple glowing drawing and no letters: three straight arrows from one point (orange frame), a cylinder with a ring (teal frame), a globe with latitude lines (navy frame), a curved bending grid (purple frame). Haru stands in front of the cards holding a pointer, nervous with a big sweat drop. Sia and Moa sit at student desks raising their hands with curious faces. The fruit-fly researcher hovers near Haru's shoulder whispering a tip; the abacus robot stands beside her flicking abacus beads helpfully. The professor stands at the back door with arms crossed, smiling calmly. In a small audience row at the side, X1, X2, X3 lean forward looking worried.", 'haru sia moa fly robo doc x'),
 ('cover_00', '16:9 · 1600×900', '0편 표지', "The same lab classroom. Haru, still a little tense, explains with one finger raised in front of a carousel-shaped model: an outer horse and an inner horse on the same spoke, the outer one leaving a long orange arc and the inner one a short navy arc. Sia leans forward with sparkling eyes; Moa takes notes. The abacus robot holds up a measuring tape between the two arcs; the fruit-fly researcher points at the longer arc. The professor watches from the side, chin in hand.", 'haru sia moa robo fly doc'),
 ('cover_01', '16:9 · 1600×900', '1부 표지', "A bright lab table with everyday objects: two pizzas of different sizes each with one same-angle slice lifted out, a small globe on a stand, a toy subway station model with tiny people walking out, three coin piles (round, square, oval coins; no symbols) linked in a triangle by glowing arrows, and a small grayscale photo frame with a bright square. Moa holds a pizza slice looking surprised; Haru, flustered with a sweat drop, compares the two crusts; Sia spins the globe thoughtfully. The fruit-fly researcher points at the subway model; the abacus robot calculates next to the coin triangle; the professor nods at the back. X1, X2, X3 peek over the table edge looking worried.", 'moa haru sia fly robo doc x'),
 ('cover_02', '16:9 · 1600×900', '2부 표지', "A pixel-art economic situation room inside the white lab. On the wall: a large round dial split into four pastel quarters with one red hand, a triangle of three coin stacks connected by arrows, and a bar board with orange bars going up and navy bars going down. Haru stands at the dial with a slightly nervous but determined face; Sia points at the coin triangle; Moa holds a clipboard next to the bar board. The abacus robot pushes a cart of coins; the fruit-fly researcher inspects the dial with a magnifier; the professor sits with a cup of tea, pleased. X1, X2, X3 watch from a bench.", 'haru sia moa robo fly doc x'),
 ('cover_03', '16:9 · 1600×900', '3부 표지', "A pixel-art AI room in the white lab. A large translucent sphere floats in the center covered with small teal dots; to the right a network of round nodes linked by lines with one orange node glowing; to the left a clock face marked only by dots. Haru stands confidently in front of the sphere with a big smile, one hand raised like a teacher; Moa and Sia cheer; the fruit-fly researcher gives a thumbs-up; the abacus robot carries a stack of glowing cards; the professor claps proudly. X1, X2, X3 cheer from the audience row.", 'haru moa sia fly robo doc x'),
]
SCENES = [
 ('scene_r_e', '0편 입구 방', "A large pixel-art grid board on the lab wall with two dots and a right triangle between them (a short orange side, a teal side, a dashed navy long side). Sia stands at one dot, Moa at the other, both measuring with a long ruler; Haru holds the ruler's middle, nervously.", 'sia moa haru'),
 ('scene_r_a', '0편 방 A', "A pixel-art carousel seen from slightly above: an outer horse and an inner horse at the same angle on the platform; the outer horse leaves a long glowing orange arc, the inner horse a short navy arc. Sia rides the outer horse smiling; the abacus robot rides the inner horse looking puzzled; Haru watches holding a protractor.", 'sia robo haru'),
 ('scene_r_b', '0편 방 B', "Three small boxes on a lab table, the same number of tick marks on each edge but clearly different sizes: a small cube, a curved wedge-shaped box, and a larger curved box cut from a globe. Moa measures them with a tape; Haru compares them with wide eyes; the fruit-fly researcher points at the biggest one.", 'moa haru fly'),
 ('scene_r1', '1부 방 1 피자', "Two pizzas on a lab table, a small one and a big one, each with one slice of the same angle lifted out. Sia holds the big slice and measures its crust with a tape measure; Haru measures the small crust and looks surprised.", 'sia haru'),
 ('scene_r2', '1부 방 2 달력', "A long straight number line of twelve dots on the left wall and a round clock made of twelve dots on the right wall; on the clock the last dot and the first dot sit side by side and glow. Moa points at the line with a puzzled face; Haru points at the glowing pair on the clock, relieved.", 'moa haru'),
 ('scene_r3', '1부 방 3 경도', "A big pixel globe on a stand with latitude rings; a wide ring near the equator and a small ring near the top are highlighted. Sia stretches a measuring tape along the wide ring; the abacus robot stretches a tiny tape along the small ring; Haru looks back and forth with a sweat drop.", 'sia robo haru'),
 ('scene_r4', '1부 방 4 지도', "A flat world-style map on the wall with equal-size grid squares; beside it a globe where the squares near the top are visibly smaller. The abacus robot proudly points at a huge northern island on the flat map; the fruit-fly researcher holds a magnifier over the globe's small top squares; Moa compares both.", 'robo fly moa'),
 ('scene_r5', '1부 방 5 지하철역', "A pixel-art subway station entrance seen from above, many tiny people walking out in orange arrows and fewer walking in with navy arrows. Haru stands beside the entrance counting with a clicker, looking a bit more confident; Sia counts the other direction.", 'haru sia'),
 ('scene_r6', '1부 방 6 환전', "Three exchange counters arranged in a triangle, each with a different coin pile (round, square, oval coins; no symbols), glowing arrows going around the triangle. Moa walks the loop holding a coin purse that is slightly fuller at the end; Haru follows with a nervous smile; X1, X2, X3 watch from a bench.", 'moa haru x'),
 ('scene_r7', '1부 방 7 사진', "A large grayscale photo frame on the wall made of chunky pixel squares: a bright square and one bright dot on a dark background; next to it a second frame showing only the glowing outline of the square and the dot. Sia looks at the outline frame amazed; Haru explains with a pointer.", 'sia haru'),
 ('scene_r8', '2부 방 8 경기시계', "A big wall dial divided into four pastel quarters with a red dot traveling clockwise along a gray path; next to it a tall spiral tube made of the same path stacked over time. Moa follows the dot with her finger; Haru explains, slightly tense; the professor watches from a chair with tea.", 'moa haru doc'),
 ('scene_r9', '2부 방 9 차익거래', "A busy pixel-art exchange hall: many small identical traders (simple gray figures) rush around a triangle of three coin counters, and the glowing gap between the counters shrinks to a thin line. Sia watches surprised; Haru stands beside a small toll gate bar; the abacus robot calculates.", 'sia haru robo'),
 ('scene_r10', '2부 방 10 자금순환', "Four big jars on a long table, two pouring coins out into a central channel and two collecting coins from it; the channel forms a closed loop with no coins leaking outside. Moa checks the loop with a clipboard; Haru points at the jars; the fruit-fly researcher peeks under the table looking for leaks.", 'moa haru fly'),
 ('scene_r11', '2부 방 11 집값 확산', "A miniature town on a table made of small houses on a five-by-five grid; one tall orange house in the middle with color softly spreading to its neighbors over a few frames shown as a strip of three small boards. Sia raises the tall house; Haru gently mixes colors with a big brush.", 'sia haru'),
 ('scene_r12', '2부 방 12 상관', "A transparent globe on a stand with three colored arrows from its center to its surface (orange, teal, purple). The abacus robot tries to force a fourth bent arrow that does not reach the surface and looks embarrassed; the fruit-fly researcher shakes its head; Moa adjusts the arrows on the globe correctly.", 'robo fly moa'),
 ('scene_r13', '3부 방 13 판매 예측', "An ice-cream stall chart board: twelve bars rising to a peak in the middle and falling again; a red straight line misses the bars, a green wave line follows them. Moa holds an ice cream cone looking at the green line; Haru, confident now, points at the wave; a round clock with twelve dots hangs above.", 'moa haru'),
 ('scene_r14', '3부 방 14 임베딩', "A large glowing sphere covered with small dots; two arrows from the center point in almost the same direction, one short and one long. Sia compares the two arrows with a protractor; Haru smiles and nods.", 'sia haru'),
 ('scene_r15', '3부 방 15 RoPE', "A row of small turntables on a long desk, each holding an arrow turned a little more than the previous one; two turntables are linked by a glowing arc showing the same angle gap as another linked pair further along. Moa turns the turntables; Haru explains with a pointer.", 'moa haru'),
 ('scene_r16', '3부 방 16 학습 걸음', "Two round running tracks on the lab floor, a small inner one and a big outer one; a runner robot takes equal-size steps on each, and on the big track the same steps cover only a tiny angle. The abacus robot runs on the big track sweating; Sia measures the angle; Haru holds a stopwatch.", 'robo sia haru'),
 ('scene_r17', '3부 방 17 흐름 모델', "A rubber sheet with a colored square of paint being stretched on a frame; the stretched square becomes larger and paler. Moa pulls one corner, Sia pulls another; Haru checks that the total paint jar is still full.", 'moa sia haru'),
 ('scene_r18', '3부 방 18 GNN', "A network of five round nodes on a board connected by strings, each node a different color; a second board beside it shows the same network after mixing, with colors closer together, and a third board where all nodes are the same gray. The fruit-fly researcher points worriedly at the all-gray board; Haru holds a paintbrush; Sia compares.", 'fly haru sia'),
 ('scene_duel', '3부 대결', "RPG battle screen layout. The professor on the left and Haru on the right, each holding up a card with a simple coordinate drawing (a turbine with a circle, a globe, a straight shelf grid, a clock, two arrows from one point; no letters). Sia and Moa sit at a judge table in the middle with empty score boards. X1, X2, X3 cheer in the audience below.", 'doc haru sia moa x'),
 ('scene_outro_00', '0편 아웃트로', "Haru wipes her forehead in relief after the first lesson; Sia and Moa clap; the abacus robot bows apologetically; the fruit-fly researcher gives a small nod; X1, X2, X3 clap from the bench.", 'haru sia moa robo fly x'),
 ('scene_outro_01', '1부 아웃트로', "Haru, now smiling, holds a pizza slice and a globe; Sia high-fives her; Moa stacks notes; the professor gives a thumbs-up from the door; X1, X2, X3 cheer.", 'haru sia moa doc x'),
 ('scene_outro_02', '2부 아웃트로', "In the economic situation room, Haru stands proudly by the dial; Moa shows a coin purse that is now exactly even; Sia waves; the abacus robot checks its abacus twice; the professor sips tea, pleased.", 'haru moa sia robo doc'),
 ('scene_outro_03', '3부 아웃트로 (하루 승과 표정 맞춤)', "Haru in a joyful victory pose holding a small trophy shaped like a globe; the professor claps proudly beside her; Sia and Moa cheer; the fruit-fly researcher throws confetti; the abacus robot holds up a glowing card; X1, X2, X3 jump with joy.", 'haru doc sia moa fly robo x'),
]

def block(name, size, use, scene, who):
    chars = '\n'.join(C[w] for w in who.split())
    return f"## {name} — {size} · {use}\n\n```text\n{HEAD}\n\n{scene}\n\nCharacters:\n{chars}\n\n{TAIL}\n```\n\n"

out = """# 그림 생성 지시문 — 벡터 분석 랩 (16비트 RPG 픽셀아트 · 기본 규칙)

> 화풍(필수): 모든 표지·장면 그림은 **16비트 RPG 픽셀아트**. 애니메이션 일러스트체·수채화·3D 렌더로 받지 않는다(SPACE_COORDINATE_GUIDE 11-1).
> 참고 그림: fruitfly-lab-expressions 캐릭터 그림만 첨부(박사·하루·초파리 연구원·주판봇·시아·모아·X1~X3). 다른 화풍 그림은 첨부하지 않는다.
> 받는 순서: ① cover_index를 먼저 받아 화풍 확인 → ② 그 그림을 참고 그림으로 함께 올려 같은 비율끼리 3~5장씩 요청(표지 4장 → 0편 장면 → 1부 → 2부 → 3부 → 대결·아웃트로).
> 이야기 설정: 조수 하루가 처음 수업을 맡아 긴장(0편·1부: 땀방울) → 조금 덜 떪(2부) → 자신감(3부, 대결 승). 시아·모아가 질문, 미공개 X1~X3는 방청석에서 걱정하다가 응원, 초파리 연구원·주판봇이 돕고, 박사가 정리.
> 아래 각 블록은 **그대로 복사해 붙이는 완성 문구**다(첫 줄 화풍 문구 + 장면 + 캐릭터 + 끝 문구).

## 받은 그림 픽셀 확인표 (받을 때마다)
- [ ] 네모난 픽셀이 보인다(확대했을 때 계단 모양 가장자리) · 굵은 어두운 외곽선, 2~3단 음영, 작은 하이라이트
- [ ] 부드러운 그라데이션·붓 질감·3D 렌더 느낌이 없다
- [ ] 캐릭터 얼굴·머리색이 기준 그림과 같다 · 하루 표정이 편에 맞다(0·1부 긴장 → 3부 자신감)
- [ ] 그림 안에 글자·숫자·기호가 없다(말풍선은 비움)
- [ ] 얼굴·손이 안전 영역 안, 왼쪽 아래 모서리 비어 있음
- 어긋나면: 같은 요청문 + "Redraw as strict 16-bit RPG pixel art, same composition"으로 다시 받는다. 표정만 틀리면 캐릭터 저장소의 표정 그림을 첨부해 "표정만 편집"으로 요청.

## 저장 이름·크기·반영
| 파일 | 비율·크기 | 쓰는 곳 |
|---|---|---|
"""
for n, s, u, _, _ in COVERS:
    out += f"| assets/{n}.webp | {s} | {u} (지금은 임시 대체 표지) |\n"
for n, u, _, _ in SCENES:
    out += f"| assets/{n}.webp | 3:2 · 1200×800 | {u} |\n"
out += """
- 표지 5장은 같은 이름으로 바꾸면 바로 반영된다. og·썸네일은 `tools/build_covers.py`의 `save()`와 같은 크기(og 1200×630, 썸네일 600×400)로 다시 자른다.
- 장면 그림은 받은 뒤 각 방 제목 아래에 `<figure>`로 넣는다(그림이 없을 때 빈 자리를 만들지 않기 위해 지금은 넣지 않음). 한 편 합계 600KB 이하 WebP.
- 받은 뒤 ahnboat_lab_cover_status 명부에 등록.

"""
for n, s, u, sc, who in COVERS:
    out += block(n, s, u, sc, who)
for n, u, sc, who in SCENES:
    out += block(n, '3:2 · 1200×800', u, sc, who)
(ROOT / 'docs/IMAGE_PROMPTS.md').write_text(out, encoding='utf-8')
print('prompts', len(COVERS) + len(SCENES))


# ── 지식 색인 다시 덧붙이기 (kg/pages/, ai-lab-retrofit autokg) ──
# 빌드가 페이지를 다시 쓰면 덧붙인 #kg가 사라지므로 빌드 끝에서 다시 덧붙인다. kg/reapply.py가 없으면 아무것도 하지 않는다.
if __name__ == "__main__":
    import os as _os, sys as _sys, subprocess as _sp
    _r = _os.path.dirname(_os.path.abspath(__file__))
    for _i in range(3):
        if _os.path.exists(_os.path.join(_r, "kg", "reapply.py")): break
        _r = _os.path.dirname(_r)
    if _os.path.exists(_os.path.join(_r, "kg", "reapply.py")):
        _sp.run([_sys.executable, _os.path.join(_r, "kg", "reapply.py"), _r])
