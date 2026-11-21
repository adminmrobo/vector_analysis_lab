# 벡터 분석 랩 — 네 개의 자로 읽는 화살표

같은 화살표라도 어떤 자(좌표)로 재느냐에 따라 숫자가 달라집니다. @eeanimation 「Vector Analysis」 인포그래픽 4장(직교·원통·구면·일반 직교곡선좌표)을 생활 → 경제·금융 → AI·머신러닝 순으로 세 번 만나는 연구실 해설입니다.

- 공개 주소: https://adminmrobo.github.io/vector_analysis_lab/
- 글: 안상선 ((주)M-Robo 대표) · https://adminmrobo.github.io/who_am_i/who_am_i.html
- 적용 스킬: 연구실 비전공자판(ai-lab-explainer-plain) · SPACE_COORDINATE_GUIDE

## 구성
| 파일 | 내용 | 상태 |
|---|---|---|
| index.html | 목차 | 완료 |
| 00_orientation.html | 0편 네 개의 자 — 입구 방 · 방 A(h) · 방 B(dV) | 완료 |
| dash_00.html | 0편 복습 대시보드 — 좌표계 놀이터(함수·화살표 밭·자 바꾸기, 기울기·발산·회전·라플라시안 세 자 비교, 미션 3) | 완료 |
| 01_everyday.html | 1부 생활 — 방 1~7 (피자·달력·경도·그린란드·지하철역·환전·사진) | 완료 |
| dash_01.html | 1부 복습 대시보드 — 생활 장면 시뮬레이터(피자 가게·지구 배송센터·역과 환전소·사진 앱, 미션 12) | 완료 |
| 02_economy.html | 2부 경제·금융 — 방 8~12 | 준비 중 |
| 03_ai_ml.html | 3부 AI·머신러닝 — 방 13~18 + 대결 | 준비 중 |

## 챕터마다 복습 대시보드
각 편 본문 끝에서 그 편의 대시보드로 이어집니다. 조작판(초록 = 주어진 조건, 파랑 = 내 결정) → 성적표 4개 → 그림 2개 → 하루·주판봇·초파리·박사 대사(상태에 따라 바뀜) → 미션(조작 전에는 통과 표시 안 함) → 배운 곳 다시 보기. 0편 대시보드는 원자료 카드 4/4의 일반 식으로 세 자를 직접 계산해 결과가 같은지 비교합니다.

## 등장인물 운용
시아·모아가 묻고, 처음 수업을 맡아 긴장한 조수 하루가 답합니다. 미공개 X1~X3는 방청석에서 소리로만 하루를 걱정하고, 초파리 연구원("이걸 눌러 봐")과 주판봇(계산)이 돕고, 박사가 방마다 「박사의 정리」로 묶습니다.

## 만들기
```
python3 tools/build_covers.py   # 임시 표지(글자 없음)
cd tools && for f in build_index build_00 build_01 build_dash00 build_dash01; do python3 $f.py; done && cd ..
python3 tools/check.py          # 390·1280px 넘침·콘솔 오류·빈 그림 점검
```
캐릭터 그림은 ahnboat_lab_explainer 캐릭터 팩(96px)에서 페이지에 쓰는 표정만 골라 넣습니다.

## 출처
원자료 @eeanimation 「Vector Analysis」 1/4~4/4. 수치는 모두 교육용 예시이며 투자·경영 권고가 아닙니다.
