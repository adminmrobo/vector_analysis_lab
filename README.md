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
| 01_everyday.html | 1부 생활 — 방 1~7 (피자·달력·경도·그린란드·지하철역·환전·사진) | 완료 |
| 02_economy.html | 2부 경제·금융 — 방 8~12 | 준비 중 |
| 03_ai_ml.html | 3부 AI·머신러닝 — 방 13~18 + 대결 | 준비 중 |

## 등장인물 운용
시아·모아가 묻고, 처음 수업을 맡아 긴장한 조수 하루가 답합니다. 미공개 X1~X3는 방청석에서 소리로만 하루를 걱정하고, 초파리 연구원("이걸 눌러 봐")과 주판봇(계산)이 돕고, 박사가 방마다 「박사의 정리」로 묶습니다.

## 만들기
```
python3 tools/build_covers.py   # 임시 표지(글자 없음)
python3 tools/build_index.py && python3 tools/build_00.py && python3 tools/build_01.py
python3 tools/check.py          # 390·1280px 넘침·콘솔 오류·빈 그림 점검
```
캐릭터 그림은 ahnboat_lab_explainer 캐릭터 팩(96px)에서 페이지에 쓰는 표정만 골라 넣습니다.

## 출처
원자료 @eeanimation 「Vector Analysis」 1/4~4/4. 수치는 모두 교육용 예시이며 투자·경영 권고가 아닙니다.
