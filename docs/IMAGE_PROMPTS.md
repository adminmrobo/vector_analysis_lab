# 그림 생성 지시문 — 벡터 분석 랩 (16비트 RPG 픽셀아트)

> 화풍 규칙(필수): 모든 표지·장면 그림은 **16비트 RPG 픽셀아트**. 참고 그림은 fruitfly-lab-expressions 캐릭터 그림만 첨부.
> 받는 순서: ① cover_index를 먼저 받아 화풍 확인 → ② 그 그림을 참고로 함께 올려 cover_00·cover_01을 한 대화에서 요청.
> 지금 저장소의 assets/cover_*.webp는 **임시 대체 표지**(글자 없음)다. 픽셀 표지를 받으면 같은 이름으로 바꾸고 `og/`·`thumbs/`는 tools/build_covers.py의 save()와 같은 크기로 다시 자른다.
> 이야기 설정: 조수 하루가 처음으로 수업을 맡아 긴장(땀방울), 시아·모아가 질문, 미공개 X1~X3가 방청석에서 걱정, 초파리 연구원·주판봇이 돕고, 박사가 정리.

## 받은 그림 픽셀 확인표
- [ ] 네모난 픽셀이 보인다 · 굵은 어두운 외곽선, 2~3단 음영
- [ ] 부드러운 그라데이션·3D 렌더 느낌이 없다
- [ ] 캐릭터 얼굴·머리색이 기준 그림과 같다 · 그림 안에 글자·숫자·기호가 없다
- [ ] 얼굴·손이 안전 영역 안, 왼쪽 아래 모서리 비어 있음
- 어긋나면 같은 요청문 + "Redraw as strict 16-bit RPG pixel art, same composition".

## 저장 이름·크기
| 파일 | 비율·크기 | 쓰는 곳 |
|---|---|---|
| assets/cover_index.webp | 16:9 · 1600×900 | 목차 표지·og |
| assets/cover_00.webp | 16:9 · 1600×900 | 0편 표지 |
| assets/cover_01.webp | 16:9 · 1600×900 | 1부 표지 |

## cover_index — 16:9 · 1600×900 · 목차 표지

```text
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).

A white pixel-art lab classroom. On the front wall hang four large framed cards side by side, each with a simple glowing drawing and no letters: three straight arrows from one point (orange frame), a cylinder with a ring (teal frame), a globe with latitude lines (navy frame), a curved bending grid (purple frame). Haru stands in front of the cards holding a pointer, nervous with a big sweat drop. Sia and Moa sit at student desks raising their hands with curious faces. The fruit-fly researcher hovers near Haru's shoulder whispering a tip; the abacus robot stands beside her flicking abacus beads helpfully. The professor stands at the back door with arms crossed, smiling calmly. In a small audience row at the side, X1, X2, X3 lean forward looking worried.

Characters:
- Haru the assistant: young woman, pink hair with blue streaks in two side buns, lavender hoodie under a white lab coat.
- Sia: young woman, long straight black hair, dark eyes, black maid-style lab uniform with white apron and gray bow.
- Moa: young woman, long light-brown hair with white frilled headband, mustard maid-style lab cardigan with red striped bow.
- The fruit-fly researcher: a fruit fly wearing a blue round helmet with big red compound-eye goggles and cables, transparent wings.
- The abacus robot: small robot with a beige monitor head showing a simple green face, antenna, abacus-frame body, tank treads.
- The professor: middle-aged man, spiky black hair with one white streak, teal glasses, white lab coat over black vest and tie.
- X1, X2, X3: three small dark navy-black silhouettes with white dot eyes (one with a pink ribbon, one with a beret and teal glasses, one small cat-eared one with a yellow bell), sitting in an audience row.

Pixel art only: visible square pixels, limited palette, no smooth gradients, no painterly or 3D-render look. No text, letters, numbers or symbols anywhere in the image; leave any speech bubbles empty. Keep faces and hands inside the safe area (12% from left and right edges, 10% from top, 18% from bottom). Keep the bottom-left corner empty. Bright white daytime lab palette with teal, orange and navy accents.
```

## cover_00 — 16:9 · 1600×900 · 0편 네 개의 자

```text
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).

The same lab classroom. Haru, still a little tense, explains with one finger raised in front of a carousel-shaped model: an outer horse and an inner horse on the same spoke, the outer one leaving a long orange arc and the inner one a short navy arc. Sia leans forward with sparkling eyes; Moa takes notes. The abacus robot holds up a measuring tape between the two arcs; the fruit-fly researcher points at the longer arc. The professor watches from the side, chin in hand.

Characters:
- Haru the assistant: young woman, pink hair with blue streaks in two side buns, lavender hoodie under a white lab coat.
- Sia: young woman, long straight black hair, dark eyes, black maid-style lab uniform with white apron and gray bow.
- Moa: young woman, long light-brown hair with white frilled headband, mustard maid-style lab cardigan with red striped bow.
- The abacus robot: small robot with a beige monitor head showing a simple green face, antenna, abacus-frame body, tank treads.
- The fruit-fly researcher: a fruit fly wearing a blue round helmet with big red compound-eye goggles and cables, transparent wings.
- The professor: middle-aged man, spiky black hair with one white streak, teal glasses, white lab coat over black vest and tie.

Pixel art only: visible square pixels, limited palette, no smooth gradients, no painterly or 3D-render look. No text, letters, numbers or symbols anywhere in the image; leave any speech bubbles empty. Keep faces and hands inside the safe area (12% from left and right edges, 10% from top, 18% from bottom). Keep the bottom-left corner empty. Bright white daytime lab palette with teal, orange and navy accents.
```

## cover_01 — 16:9 · 1600×900 · 1부 생활

```text
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights).

A bright lab table scene with everyday objects: two pizzas of different sizes each with one same-angle slice lifted out, a small globe on a stand, a toy subway station model with tiny people walking out, three coin piles (round, square, oval coins; no symbols) linked in a triangle by glowing arrows, and a small grayscale photo frame with a bright square. Moa holds a pizza slice with a surprised face; Haru, flustered with a sweat drop, compares the two crusts; Sia spins the globe thoughtfully. The fruit-fly researcher points at the subway model; the abacus robot calculates on its abacus next to the coin triangle; the professor nods at the back. X1, X2, X3 peek over the table edge looking worried.

Characters:
- Moa: young woman, long light-brown hair with white frilled headband, mustard maid-style lab cardigan with red striped bow.
- Haru the assistant: young woman, pink hair with blue streaks in two side buns, lavender hoodie under a white lab coat.
- Sia: young woman, long straight black hair, dark eyes, black maid-style lab uniform with white apron and gray bow.
- The fruit-fly researcher: a fruit fly wearing a blue round helmet with big red compound-eye goggles and cables, transparent wings.
- The abacus robot: small robot with a beige monitor head showing a simple green face, antenna, abacus-frame body, tank treads.
- The professor: middle-aged man, spiky black hair with one white streak, teal glasses, white lab coat over black vest and tie.
- X1, X2, X3: three small dark navy-black silhouettes with white dot eyes (one with a pink ribbon, one with a beret and teal glasses, one small cat-eared one with a yellow bell), sitting in an audience row.

Pixel art only: visible square pixels, limited palette, no smooth gradients, no painterly or 3D-render look. No text, letters, numbers or symbols anywhere in the image; leave any speech bubbles empty. Keep faces and hands inside the safe area (12% from left and right edges, 10% from top, 18% from bottom). Keep the bottom-left corner empty. Bright white daytime lab palette with teal, orange and navy accents.
```

