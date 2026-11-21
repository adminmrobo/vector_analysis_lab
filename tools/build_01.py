# -*- coding: utf-8 -*-
"""1부 생활 — 같은 1도, 다른 길이 (방 1~7)"""
from common import *

def room_head(n, title, tags):
    t = ''.join(f'<span>{x}</span>' for x in tags)
    return f'<section class="room" id="room-{n}">\n<div class="wing">1부 · 방 {n}</div>\n<h2>{title}</h2>\n<div class="tags">{t}</div>\n'

def mathbox(q, words, school, tries, eq, end):
    li = ''.join(f'<li>{x}</li>' for x in tries)
    return (f'<div class="box math"><h3>시아·모아가 묻고, 하루가 풀어 봅니다</h3>{q}'
            f'<p class="saywords"><b>말로 먼저:</b> {words}</p><p><b>학교 수학으로 보면:</b> {school}</p>'
            f'<div class="try"><b>숫자로 한 번 해 보기</b><ol>{li}</ol></div>{eq}{end}</div>')

def whybox(problem, prev, sol, easy):
    return (f'<div class="box why"><h3>왜 이 방법을 쓰나</h3><p><b>문제:</b> {problem}</p><p><b>앞 방의 한계:</b> {prev}</p>'
            f'<p><b>해법:</b> {sol}</p><div class="easy"><b>쉽게 말하면</b> {easy}</div></div>')

def daily(a, b, blabel='다음 부에서는'):
    return f'<div class="daily"><div><b>일상으로 치면</b>{a}</div><div><b>{blabel}</b>{b}</div></div>'

def lab(n, title, hint, fig, ctl, minh=340, btns=''):
    return (f'<div class="lab"><div class="hd"><b>{title}</b><span>{hint}</span></div>{btns}'
            f'<div class="fig" style="min-height:{minh}px">{fig}</div><div class="ctl">{ctl}</div>'
            f'<div class="read" id="r{n}read" aria-live="polite"></div></div>')

def sl(id_, label, mn, mx, st, v):
    return (f'<div class="sl"><label for="{id_}">{label}</label><input type="range" id="{id_}" min="{mn}" max="{mx}" step="{st}" value="{v}">'
            f'<output id="{id_}o"></output></div>')

def body():
    h = f"""
<header class="hero"><div class="wrap">
<div class="wing">벡터 분석 랩 · 1부 생활</div>
<h1>같은 1도, 다른 길이<br>피자·지도·지하철·환전·사진으로 보는 벡터 분석</h1>
<p class="sub">0편에서 본 "한 걸음의 실제 길이"를 생활 장면 일곱 개에서 다시 봅니다. 시아·모아가 묻고, 아직 긴장한 하루가 답하고, 초파리 연구원과 주판봇이 돕고, 박사가 방마다 정리합니다.</p>
<figure class="cover" style="margin-left:0;margin-right:0"><img src="assets/cover_01.webp" width="1600" height="900" alt="피자·지구본·지하철역 도형 앞에서 당황한 하루와 연구실 식구들 (임시 표지)"></figure>
<div class="by">{AUTHOR}</div>
<a class="cta" href="#room-1">방 1부터 들어가기</a>
</div></header>

<main class="wrap">
<section>
<div class="three">
<h2>처음 오신 분께 — 이 페이지를 3줄로</h2>
<ol>
<li><b>무엇을:</b> 원자료 카드 네 장의 개념(한 걸음 h, 작은 상자 dV, 발산, 회전, 라플라시안)을 생활 장면 일곱 개로 봅니다.</li>
<li><b>왜 중요한가:</b> 같은 장면이 2부(경제·금융)와 3부(AI·머신러닝)에서 그대로 다시 나옵니다. 여기서 감을 잡으면 뒤가 쉽습니다.</li>
<li><b>업무에서는:</b> 배송 거리, 지도 넓이, 역 유동 인구, 환전, 사진 윤곽선 검출이 모두 이 계산입니다.</li>
</ol>
<p style="margin:0">코드·수식을 몰라도 됩니다. 수치는 모두 교육용 예시이고, 환율은 가상 값입니다.</p>
<details><summary>이 페이지에 나오는 기호와 약어 풀이</summary>
<table><tbody>
<tr><td class="m">h</td><td>한 걸음의 실제 길이(축척 인자)</td></tr>
<tr><td class="m">ρ, φ</td><td>중심에서 거리(로), 돌아간 각도(파이)</td></tr>
<tr><td class="m">r, θ</td><td>지구 중심에서 거리, 북극에서 내려온 각도(세타). 위도 = 90° − θ</td></tr>
<tr><td class="m">∇·</td><td>발산. 그 자리에서 솟아나면 +(샘), 빨려 들어가면 −(배수구)</td></tr>
<tr><td class="m">∇×</td><td>회전. 한 바퀴 돌았을 때 남는 것</td></tr>
<tr><td class="m">∇²</td><td>라플라시안. 주변 평균과 내 값의 차이</td></tr>
<tr><td>rad</td><td>라디안. 180° = 3.14 rad</td></tr>
</tbody></table></details>
</div>
</section>

<section id="opening">
<h2>오늘의 장면 — 하루의 두 번째 수업</h2>
{talk(T('asst/E15', '0편은 어떻게 넘겼는데… 오늘은 생활 문제래요. 정답이 하나가 아닐 수도 있잖아요?'),
      T('moa/E12', '선배, 어제 진짜 잘했어요! 오늘은 피자부터예요. 배고프면 더 잘 풀려요.'))}
{crowd('방청석', [('x1/E15', '(조마조마)'), ('x2/E02', '(손에 땀)'), ('x3/E04', '(…!)')])}
{talk(T('fly/E10', '막히면 실험부터 눌러 보자. 숫자보다 그림이 먼저야.'),
      T('robo/E13', '계산은 제가 맡습니다. 주판알 준비 완료!'))}
<div class="map" style="margin-top:18px">
<a class="f" href="#room-1"><b>방 1</b>피자 테두리<span class="why">h = ρ, 같은 각도 다른 길이</span></a>
<a class="f" href="#room-2"><b>방 2</b>12월과 1월은 가까울까<span class="why">숫자 줄 대신 시계판</span></a>
<a class="f" href="#room-3"><b>방 3</b>경도 1도는 몇 km<span class="why">h = r sinθ</span></a>
<a class="f" href="#room-4"><b>방 4</b>그린란드가 커 보이는 이유<span class="why">dV = r² sinθ</span></a>
<a class="f" href="#room-5"><b>방 5</b>지하철역은 샘인가<span class="why">발산</span></a>
<a class="f" href="#room-6"><b>방 6</b>환전 한 바퀴<span class="why">회전</span></a>
<a class="f" href="#room-7"><b>방 7</b>사진 윤곽선<span class="why">라플라시안</span></a>
<a class="e" href="#summary"><b>정리</b>일곱 방을 한 장으로<span class="why">2부·3부로 이어지는 표</span></a>
</div>
<div class="easy" style="margin-top:16px"><b>30초 복습 — 0편에서 가져올 것</b> 각도 눈금 한 걸음은 "중심에서 거리"를 곱해야 실제 길이가 됩니다(원통 자 h = ρ, 지구본 자 h = r sinθ). 작은 상자의 실제 크기는 세 h의 곱입니다. <a href="00_orientation.html">0편</a>을 건너뛰었어도 괜찮아요. 방마다 다시 짚습니다.</div>
</section>
"""
    # ---------- 방 1 피자 ----------
    h += room_head(1, '피자 테두리 — 같은 45°, 다른 길이', ['원자료: 카드 2/4 (원통 자) h<sub>φ</sub> = ρ', '방법: 호의 길이 = 반지름 × 각도', '일상: 피자 한 조각'])
    h += talk(T('sia/E19', '선배, 10 cm 피자랑 15 cm 피자를 똑같이 45°로 잘랐어요. 테두리 빵은 똑같이 길어요?'),
              T('asst/E20', '가, 각도가 같으니까… 아, 아니에요. 잠깐만요!'))
    h += '<div class="pair">' + whybox(
        '피자는 둥급니다. 조각 크기를 "몇 도"로 말하지만, 실제로 먹는 테두리 길이는 몇 cm입니다.',
        '0편에서 각도 한 걸음에 "중심에서 거리"가 붙는다는 것만 봤습니다.',
        '원통 자에서 각도 쪽 한 걸음은 h = ρ(반지름)입니다. 테두리 길이 = 반지름 × 각도(rad).',
        '큰 피자는 같은 각도로 잘라도 테두리가 깁니다.') + mathbox(
        T('moa/E09', '45°를 라디안으로 바꾸면 얼마예요?'),
        '각도를 "반지름 몇 개만큼 돌았나"로 재면, 그 숫자에 반지름을 곱한 것이 바로 테두리 길이입니다. 180°가 3.14라서 45°는 그 4분의 1인 0.785입니다.',
        '부채꼴 호의 길이 l = rθ, 호도법',
        ['45° = 3.14 ÷ 4 = <b>0.785 rad</b>', '10 cm 피자: 10 × 0.785 = <b>7.85 cm</b>', '15 cm 피자: 15 × 0.785 = <b>11.78 cm</b> (1.5배)'],
        eqtable([('l = ρ · Δφ', '엘은 로 곱하기 델타 파이', '테두리 길이 = 반지름 × 돌린 각도'), ('h<sub>φ</sub> = ρ', '에이치 파이는 로', '각도 쪽 한 걸음의 실제 길이(카드 2/4)')]),
        T('asst/E10', '반지름이 1.5배면 테두리도 1.5배! 각도만 보면 안 되는 거였어요.')) + '</div>'
    h += daily('피자 가게가 큰 판을 "같은 8조각"으로 잘라도 큰 판 조각이 더 배부릅니다.', '2부 방 8 경기순환시계에서 "반지름 = 경기의 크기, 각도 = 국면"으로 다시 나옵니다.')
    h += talk(T('fly/E08', '반지름 슬라이더를 20까지 밀어 봐. 각도는 그대로 두고.'),
              T('robo/E09', '테두리 길이는 반지름 × 0.785! 바로바로 띄워 드릴게요.'))
    h += lab(1, '실험 ① 두 피자의 45° 조각', '왼쪽은 10 cm 기준 피자, 오른쪽 반지름을 바꿔 보세요',
             '<svg id="r1svg" role="img" aria-label="반지름이 다른 두 피자와 같은 각도의 조각, 테두리 길이"></svg>',
             sl('r1r', '오른쪽 반지름', 5, 20, 1, 15) + sl('r1a', '조각 각도', 10, 90, 5, 45))
    h += '<div class="solve"><b>풀이</b> 각도는 "얼마나 돌았나", 테두리는 "얼마나 갔나"입니다. 둘을 잇는 배율이 반지름이고, 이것이 원자료 카드 2/4의 h<sub>φ</sub> = ρ입니다.</div>'
    h += dr('같은 각도라도 중심에서 멀면 더 멀리 갑니다. 그래서 둥근 자로 기울기를 잴 때는 각도 쪽 변화를 ρ로 나눠 "1 cm당" 값으로 바꿉니다. 원자료 기울기 식의 1/ρ가 바로 그것입니다.')
    h += '<div class="limit"><b>이 방의 한계</b> 피자는 평평한 원이라 반지름 하나로 끝났습니다. 지구처럼 둥근 공 위에서는 "도는 원의 반지름"이 위도마다 달라집니다. 그 전에, 각도 자체가 데이터일 때를 먼저 봅니다.</div>'
    h += quiz('반지름 20 cm 피자를 90°로 잘랐습니다. 테두리 길이는? (90° = 1.57 rad)', [('a', '약 20 cm'), ('b', '약 31.4 cm'), ('c', '약 90 cm')], 'b', '맞아요. 20 × 1.57 = 31.4 cm.', '반지름에 라디안 각도를 곱해 보세요. 20 × 1.57입니다.') + '</section>'

    # ---------- 방 2 달력 ----------
    h += room_head(2, '12월과 1월은 가까울까 — 숫자 줄 대신 시계판', ['원자료: 카드 2/4 위쪽 그림 (돌아가는 각도 φ)', '방법: 각도로 놓기', '일상: 달력'])
    h += talk(T('moa/E09', '아이스크림 판매를 월별로 정리했는데요, 1부터 12로 쓰면 12월과 1월이 제일 멀어요. 이상하지 않아요?'),
              T('asst/E15', '어… 12월 다음이 1월인데… 숫자로는 11이나 떨어져 있네요?!'))
    h += '<div class="pair">' + whybox(
        '달·요일·시각은 한 바퀴 돌면 처음으로 돌아옵니다. 숫자 줄(1~12)에 놓으면 끝과 처음이 가장 멀어집니다.',
        '방 1에서는 각도가 "길이를 바꾸는 배율"이었습니다. 이번에는 각도 자체가 데이터입니다.',
        '달을 시계판 위에 놓습니다. 한 달 = 30°. 그러면 12월과 1월이 이웃이 됩니다. 시계판 위 점은 가로·세로 두 숫자로 적습니다.',
        '달력을 줄자 대신 시계에 걸어 두는 것입니다.') + mathbox(
        T('sia/E09', '시계판에서 두 달 사이 거리는 어떻게 재요?'),
        '반지름 1인 원 위의 두 점 사이 곧은 거리입니다. 두 점이 이루는 각도가 작을수록 가깝습니다. 반대편(180°)이 가장 멀고, 그 거리는 지름 2입니다.',
        '삼각함수 sin·cos, 원 위의 점 (cos θ, sin θ), 두 점 사이 거리',
        ['1월 = 0°, 12월 = 330° → 사이 각도 30°', '시계판 거리 = 2 × sin(15°) = <b>0.52</b>', '12월과 6월(사이 180°): <b>2</b> → 가장 멂', '숫자 줄로는 12월–1월이 <b>11</b>, 12월–6월이 6 (거꾸로!)'],
        eqtable([('(cos θ, sin θ)', '코사인 세타, 사인 세타', '시계판 위 점의 가로·세로 좌표'), ('d = 2 sin(Δθ/2)', '디는 2 사인 델타 세타 나누기 2', '반지름 1인 원 위 두 점 사이 거리')]),
        T('asst/E10', '시계판에 놓으니까 12월과 1월이 딱 붙어요. 순서가 도는 데이터는 각도로!')) + '</div>'
    h += daily('"밤 11시와 새벽 1시"는 두 시간 차이인데, 숫자 23과 1로 쓰면 22 차이가 됩니다.', '3부 방 13에서 판매 예측 모델이 이 시계판 두 숫자(cos·sin)를 특성으로 씁니다.')
    h += talk(T('fly/E08', '두 달을 12월·1월로 놓고, "숫자 줄"과 "시계판"을 번갈아 눌러 봐.'),
              T('robo/E09', '시계판 거리는 2 × sin(반각)! 제가 바로 계산해요.'))
    h += lab(2, '실험 ② 숫자 줄 vs 시계판', '두 달을 고르고 보기 방식을 바꿔 보세요',
             '<svg id="r2svg" role="img" aria-label="숫자 줄 또는 시계판 위의 두 달과 거리"></svg>',
             sl('r2m1', '첫째 달', 1, 12, 1, 12) + sl('r2m2', '둘째 달', 1, 12, 1, 1), 320,
             '<div class="btns" role="group" aria-label="보기 방식"><button class="btn" id="r2line" aria-pressed="false">숫자 줄</button><button class="btn" id="r2clock" aria-pressed="true">시계판</button></div>')
    h += '<div class="solve"><b>풀이</b> 도는 데이터는 숫자 줄에 놓으면 끝과 처음이 갈라집니다. 시계판(원통 자의 φ)에 놓으면 한 바퀴가 자연스럽게 이어집니다.</div>'
    h += dr('여기서 배운 것은 "데이터 모양에 맞는 자를 고른다"입니다. 도는 것은 각도 자로. 실제 판매 예측에서도 달을 숫자 하나 대신 시계판 위 두 숫자로 넣으면, 모델이 연말과 연초를 이웃으로 봅니다.', 'doc/E07')
    h += codebox([('np.cos(2*np.pi*(m-1)/12), np.sin(2*np.pi*(m-1)/12)', '달 m을 시계판 위 가로·세로 두 숫자로 바꾼다')])
    h += '<div class="limit"><b>이 방의 한계</b> 시계판은 평평한 원입니다. 지구처럼 공 모양이면 각도가 둘(위도·경도)이고, 경도 1도의 길이가 위도마다 달라집니다. 방 3으로 갑니다.</div>'
    h += quiz('시계판(반지름 1)에서 3월과 9월 사이 거리는?', [('a', '0.52'), ('b', '1'), ('c', '2')], 'c', '맞아요. 6달 차이 = 180°, 정반대편이라 지름 2입니다.', '6달 차이는 몇 도일까요? 180°면 원의 정반대편입니다.') + '</section>'

    # ---------- 방 3 경도 ----------
    h += room_head(3, '경도 1도는 몇 km — 지구본 자의 h = r sinθ', ['원자료: 카드 3/4 (구면 자) h<sub>φ</sub> = r sinθ', '방법: 위도마다 다른 원', '일상: 지도 앱 거리'])
    h += talk(T('sia/E19', '적도에서 경도 1도가 111 km래요. 서울에서도 111 km예요?'),
              T('asst/E20', '지, 지구는 공이니까… 피자랑 비슷할 것 같은데… 어디가 중심이지?'))
    h += crowd('방청석', [('x1/E15', '(두근)'), ('x2/E09', '(…)'), ('x3/E04', '(꼬옥)')])
    h += '<div class="pair">' + whybox(
        '경도는 지구를 동서로 도는 각도입니다. 그런데 동서로 도는 원의 크기는 적도에서 가장 크고, 북극으로 갈수록 작아집니다.',
        '방 1의 피자는 반지름이 하나였습니다. 지구본에서는 위도마다 "도는 원의 반지름"이 다릅니다.',
        '그 반지름은 지구 반지름 × sinθ (θ는 북극에서 내려온 각도)입니다. 위도로 쓰면 지구 반지름 × cos(위도). 이것이 카드 3/4의 h<sub>φ</sub> = r sinθ입니다.',
        '사과를 가로로 썰면 가운데 단면이 가장 크고, 꼭지 쪽은 작습니다.') + mathbox(
        T('moa/E09', '그럼 서울(북위 37.5°)에서는 경도 1도가 몇 km예요?'),
        '먼저 적도의 1도를 구합니다. 지구 둘레를 360으로 나누면 됩니다. 그다음 그 위도에서 도는 원이 적도 원의 몇 배인지(cos 위도)를 곱합니다.',
        '원의 둘레 2πr, 삼각함수 cos, 위도·경도',
        ['적도: 2 × 3.14 × 6,371 km ÷ 360 = <b>111.2 km</b>', '서울(37.5°): 111.2 × cos 37.5° = 111.2 × 0.79 = <b>88.2 km</b>', '위도 60°: 111.2 × 0.5 = <b>55.6 km</b> (절반)', '북극(90°): 0 km — 모든 경도가 한 점에서 만남'],
        eqtable([('h<sub>φ</sub> = r sinθ', '에이치 파이는 알 사인 세타', '경도 쪽 한 걸음의 실제 길이(카드 3/4)'), ('sinθ = cos(위도)', '—', '북극에서 잰 각도와 위도의 관계'), ('h<sub>θ</sub> = r', '에이치 세타는 알', '위도 1도는 어디서나 약 111 km')]),
        T('asst/E10', '위도 1도는 어디서나 111 km, 경도 1도만 줄어드는 거예요. 북극에선 0!')) + '</div>'
    h += daily('같은 "경도 1도 차이"라도 싱가포르의 두 가게는 111 km, 노르웨이 오슬로 근처는 약 56 km 떨어져 있습니다.', '2부에서 배송·물류비, 3부 방 16에서 "방향만 보는 AI 모델의 걸음"으로 다시 나옵니다.')
    h += talk(T('fly/E08', '위도를 0에서 89까지 천천히 밀어 봐. 1도 길이가 어떻게 줄어?'),
              T('robo/E09', '111.2 × cos(위도)! 서울 단추도 만들어 뒀어요.'))
    h += lab(3, '실험 ③ 위도마다 다른 경도 1도', '위도를 바꿔 보세요 · 단추로 바로 가기',
             '<svg id="r3svg" role="img" aria-label="옆에서 본 지구와 위도선, 그 원의 반지름"></svg>',
             sl('r3lat', '위도', 0, 89, 0.5, 60), 340,
             '<div class="btns" role="group" aria-label="위도 바로 가기"><button class="btn" data-lat="0">적도 0°</button><button class="btn" data-lat="37.5">서울 37.5°</button><button class="btn" data-lat="60">60°</button></div>')
    h += '<div class="solve"><b>풀이</b> 경도 쪽 한 걸음 h<sub>φ</sub>는 "그 위도에서 도는 원의 반지름"입니다. 원자료 카드 3/4의 기울기 식에서 φ 쪽에 1/(r sinθ)가 붙는 까닭입니다.</div>'
    h += dr('지도 위 "1도"를 거리로 바꿀 때는 위도를 꼭 같이 보세요. 실무의 거리 계산(배송 반경, 매장 상권)도 위도·경도 숫자 차이를 그대로 쓰면 북쪽일수록 동서 거리를 크게 잡는 실수를 합니다.')
    h += codebox([('111.2 * np.cos(np.radians(lat))', '위도 lat에서 경도 1도의 길이(km)')])
    h += '<div class="limit"><b>이 방의 한계</b> 길이는 맞췄지만, 땅의 넓이는 아직입니다. 위도 1도 × 경도 1도 땅의 넓이도 위도마다 다르고, 평평한 지도는 이를 크게 틀리게 보여 줍니다. 방 4로 갑니다.</div>'
    h += quiz('위도 60°에서 경도 2도 차이는 대략 몇 km일까요?', [('a', '약 56 km'), ('b', '약 111 km'), ('c', '약 222 km')], 'b', '맞아요. 1도가 55.6 km라 2도는 약 111 km.', '위도 60°에서 경도 1도는 적도의 절반(55.6 km)입니다. 2도면?') + '</section>'

    # ---------- 방 4 그린란드 ----------
    h += room_head(4, '그린란드가 커 보이는 이유 — 작은 땅 상자 dV', ['원자료: 카드 3/4 맨 아래 dV = r² sinθ dr dθ dφ', '방법: 땅 넓이 = h<sub>θ</sub> × h<sub>φ</sub>', '일상: 세계 지도'])
    h += talk(T('moa/E04', '교실 세계 지도에서 그린란드가 아프리카만큼 커 보여요. 정말 그만큼 커요?'),
              T('asst/E15', '어… 지도가 거짓말을 할 리는… 아, 아니 할 수도 있어요!'))
    h += '<div class="pair">' + whybox(
        '공 모양 지구를 평평한 종이에 펴면 어딘가는 늘어납니다. 흔한 세계 지도(메르카토르)는 위도·경도 1도를 어디서나 같은 크기 네모로 그립니다.',
        '방 3에서 경도 1도의 길이가 북쪽일수록 짧아진다는 것을 봤습니다.',
        '위도 1도 × 경도 1도 땅의 실제 넓이 = 111.2 km × (111.2 km × cos 위도). 카드 3/4의 dV에서 바닥 두 변(h<sub>θ</sub>·h<sub>φ</sub>)만 곱한 것입니다.',
        '지도의 네모는 크기가 같아도, 북쪽 네모 속 실제 땅은 작습니다.') + mathbox(
        T('sia/E09', '적도와 위도 60°의 "1도 × 1도 땅"은 넓이가 얼마나 달라요?'),
        '남북 한 변은 어디서나 111.2 km입니다. 동서 한 변은 위도에 따라 줄어듭니다. 그래서 넓이도 cos(위도)배로 줄어듭니다.',
        '직사각형의 넓이, 삼각함수 cos',
        ['적도: 111.2 × 111.2 ≈ <b>12,360 km²</b>', '위도 60° 부근: 111.2 × 55.6 ≈ <b>6,180 km²</b> (절반)', '작은 네모로 어림한 값입니다'],
        eqtable([('dA = r² sinθ dθ dφ', '디에이는 알 제곱 사인 세타 디세타 디파이', '공 표면의 작은 땅 넓이(dV에서 dr을 뺀 것)'), ('r × r sinθ', '—', '남북 한 걸음 × 동서 한 걸음')]),
        T('asst/E10', '북쪽 땅 상자는 작은데 지도에서는 같은 크기로 그리니까 커 보이는 거네요!')) + '</div>'
    h += daily('지도 앱의 축척 막대도 위도에 따라 길이가 바뀝니다. 북쪽으로 스크롤하면 같은 "1 km" 막대가 길어집니다.', '3부 방 17 "늘리면 묽어진다"에서, 데이터를 늘린 만큼 확률을 고치는 계산으로 다시 나옵니다.')
    h += talk(T('fly/E08', '위도를 72°(그린란드 한가운데쯤)에 놓고 "지도에서 부풀린 배수"를 읽어 봐.'),
              T('robo/E09', '실제 넓이는 cos, 지도 위 넓이는 1/cos… 둘을 나누면 부풀린 배수!'))
    h += lab(4, '실험 ④ 지도 위 네모 vs 실제 땅', '위도를 바꿔 보세요',
             '<svg id="r4svg" role="img" aria-label="적도와 고른 위도의 1도 네모: 지도 위 크기와 실제 땅 넓이 비교"></svg>',
             sl('r4lat', '위도', 0, 80, 1, 60), 340)
    h += f"""<div class="ai"><b>AI 판단 코너 — 주판봇의 1초 답, 믿어도 될까?</b>
{T('robo/E16', '지도에서 그린란드가 아프리카랑 비슷하게 보이니까, 넓이도 비슷하겠네요! 계산 끝!')}
<p>박사는 늘 이렇게 묻습니다. <b>"가정이 맞나? 숫자가 그럴듯한가?"</b> 주판봇은 "지도 위 크기 = 실제 크기"라고 가정했습니다. 위 실험에서 위도 72°를 놓으면 그 지도는 넓이를 약 <b>10배</b> 부풀립니다. 실제로 그린란드는 약 217만 km², 아프리카는 약 3,037만 km²로 아프리카가 약 <b>14배</b> 넓습니다.</p>
{T('robo/E14', '지도도 자를 하나 고른 것뿐이었군요… 자의 한 걸음부터 확인할게요.')}
</div>"""
    h += '<div class="solve"><b>풀이</b> 땅 넓이는 두 한 걸음(남북 r, 동서 r sinθ)의 곱입니다. 원자료 카드 3/4의 dV = r² sinθ dr dθ dφ에서 표면만 보면 r² sinθ dθ dφ가 남습니다. 메르카토르 지도는 이 sinθ(= cos 위도)를 지우고 그려서, 위도 φ의 땅을 약 1/cos²(위도)배로 부풀려 보여 줍니다.</div>'
    h += dr('같은 "1도 × 1도"라도 실제 크기는 다릅니다. 지도뿐 아니라 숫자 표에서도 "눈금으로 센 개수"와 "실제 크기"를 구별해야 합니다. 특히 AI가 "비슷해 보인다"고 할 때는 어떤 자로 본 것인지 먼저 확인하세요.')
    h += '<div class="limit"><b>이 방의 한계</b> 지금까지는 자리(위치)의 크기만 봤습니다. 이제 그 자리로 무언가가 들어오고 나가는 흐름을 봅니다. 사람이 드나드는 지하철역으로 갑니다.</div>'
    h += quiz('위도 60°의 "1도 × 1도 땅"은 적도 땅의 몇 배일까요?', [('a', '2배'), ('b', '같음'), ('c', '절반')], 'c', '맞아요. 동서 한 변이 cos 60° = 0.5배라 넓이도 절반입니다.', '남북 한 변은 같고, 동서 한 변만 cos(위도)배로 줄어듭니다.') + '</section>'

    # ---------- 방 5 지하철 ----------
    h += room_head(5, '지하철역은 샘인가 배수구인가 — 발산', ['원자료: 네 카드의 DIVERGENCE 줄 (∇·A)', '방법: 나가는 양 − 들어오는 양', '일상: 출퇴근 지하철'])
    h += talk(T('sia/E09', '아침 업무지구 역에서는 사람이 쏟아져 나오고, 저녁엔 빨려 들어가요. 이것도 벡터 분석이에요?'),
              T('asst/E07', '네! 이건 제가 좀 알아요. 발산이에요. 흐름이 "솟아나는가, 빨려 드는가"예요.'))
    h += '<div class="pair">' + whybox(
        '사람·돈·물의 흐름은 화살표 밭입니다. 어떤 자리가 흐름을 내보내는 곳인지, 빨아들이는 곳인지 숫자 하나로 알고 싶습니다.',
        '방 1~4는 자리의 크기였습니다. 이제 그 자리를 지나가는 흐름을 봅니다.',
        '그 자리를 둘러싼 작은 상자에서 "나가는 양 − 들어오는 양"을 셉니다. +이면 샘, −이면 배수구, 0이면 지나가기만 합니다.',
        '역 출구에 서서 나오는 사람과 들어가는 사람 수를 세는 것입니다.') + mathbox(
        T('moa/E09', '한 시간에 1,200명이 내리고 800명이 탔으면요?'),
        '역을 작은 상자로 보고, 동네 쪽으로 나간 사람에서 역으로 들어온 사람을 뺍니다. 남는 사람이 많으면 역이 동네에 사람을 뿜어내는 샘입니다.',
        '수의 덧셈·뺄셈, 부호(+, −)',
        ['내린 사람(동네로 나감) 1,200명', '탄 사람(역으로 들어옴) 800명', '1,200 − 800 = <b>+400명</b> → 동네 쪽으로 보면 <b>샘</b>'],
        eqtable([('∇·A', '나블라 점 에이(발산)', '작은 상자에서 나가는 양 − 들어오는 양을 부피로 나눈 값'), ('∂A<sub>x</sub>/∂x + …', '—', '카드 1/4: 가로·세로·높이 쪽 변화량의 합'), ('(1/ρ)∂(ρA<sub>ρ</sub>)/∂ρ', '—', '카드 2/4: 둥근 자에서는 상자 크기(ρ)가 같이 들어감')]),
        T('asst/E16', '바깥으로 갈수록 상자가 커지니까, 원통 자 식에 ρ가 들어가는 거예요. 0편 방 B랑 같아요!')) + '</div>'
    h += daily('출근 시간 업무지구 역은 샘, 퇴근 시간에는 배수구가 됩니다.', '2부 방 10 "자금순환의 샘과 배수구"에서 가계·기업·정부의 돈 흐름으로 다시 나옵니다.')
    h += talk(T('fly/E08', '"퇴근 시간" 단추를 눌러 봐. 부호가 어떻게 바뀌어?'),
              T('robo/E09', '나간 사람 빼기 들어온 사람! 화살표 수도 맞춰 그릴게요.'))
    h += lab(5, '실험 ⑤ 역 출구의 화살표', '사람 수를 바꾸거나 시간대 단추를 눌러 보세요',
             '<svg id="r5svg" role="img" aria-label="역을 둘러싼 나가는 화살표와 들어오는 화살표"></svg>',
             sl('r5out', '내린 사람', 0, 2000, 50, 1200) + sl('r5in', '탄 사람', 0, 2000, 50, 800), 320,
             '<div class="btns" role="group" aria-label="시간대"><button class="btn" id="r5am">출근 시간 (업무지구 역)</button><button class="btn" id="r5pm">퇴근 시간 (업무지구 역)</button></div>')
    h += '<div class="solve"><b>풀이</b> 발산은 "그 자리에서 흐름이 새로 생기는가"입니다. 원자료 카드의 DIVERGENCE 줄은 이 계산을 자마다 적은 것입니다. 둥근 자에서는 상자 크기(ρ, r²)가 식 안에 들어갑니다.</div>'
    h += dr('발산이 +인 곳은 흐름의 출발지, −인 곳은 도착지입니다. 역을 다 더하면 도시 전체에서는 나간 사람과 들어온 사람이 같아집니다. 이 "전체 합"의 성질이 2부 자금순환에서 중요해집니다.')
    h += '<div class="limit"><b>이 방의 한계</b> 발산은 흐름이 "생기고 사라지는가"만 봅니다. 흐름이 빙글빙글 도는지는 모릅니다. 돌아서 제자리에 왔는데 무언가 남는 흐름, 환전으로 가 봅니다.</div>'
    h += quiz('어느 역에서 한 시간에 300명이 내리고 1,500명이 탔습니다. 동네 쪽으로 보면 이 역은?', [('a', '샘 (+1,200)'), ('b', '배수구 (−1,200)'), ('c', '0')], 'b', '맞아요. 300 − 1,500 = −1,200, 빨아들이는 배수구입니다.', '나간 사람(내린 사람)에서 들어온 사람(탄 사람)을 빼 보세요.') + '</section>'

    # ---------- 방 6 환전 ----------
    h += room_head(6, '환전 한 바퀴 — 회전', ['원자료: 네 카드의 CURL 줄 (∇×A)', '방법: 한 바퀴 돌아 남는 것', '일상: 해외여행 환전'])
    h += talk(T('moa/E09', '원 → 달러 → 엔 → 원으로 한 바퀴 바꾸면 처음 돈 그대로예요?'),
              T('asst/E20', '네, 네! 처음 돈 그대로일 거예요… 아, 아니다. 직접 해 볼게요!'))
    h += crowd('방청석', [('x1/E15', '(긴장)'), ('x2/E02', '(꿀꺽)'), ('x3/E09', '(…?)')])
    h += '<div class="pair">' + whybox(
        '세 통화를 돌아가며 바꿀 때, 환율끼리 서로 맞지 않으면 한 바퀴 돌아왔을 때 돈이 늘거나 줄어듭니다.',
        '방 5의 발산은 "솟아나는가"만 셌습니다. 빙글 도는 흐름은 발산으로는 보이지 않습니다.',
        '닫힌 길을 한 바퀴 돌며 얻은 것을 모두 더합니다. 0이 아니면 그 흐름에 회전이 있습니다.',
        '산을 한 바퀴 돌아 출발점에 왔는데 높이가 달라졌다면, 그건 언덕이 아니라 계단 착시 그림입니다.') + mathbox(
        T('sia/E09', '가상 환율로 해 보면 어때요? 1달러 = 1,400원, 1달러 = 150엔, 100엔 = 950원이요.'),
        '1,400원을 달러로 바꾸면 1달러, 엔으로 바꾸면 150엔, 다시 원으로 바꾸면 150엔이 몇 원인지 셉니다. 세 환율이 서로 맞으면 처음과 같아야 합니다.',
        '비율과 비례식, 단위 환산',
        ['1,400원 → <b>1달러</b>', '1달러 → <b>150엔</b>', '150엔 → 1.5 × 950 = <b>1,425원</b>', '한 바퀴에 <b>+25원</b> → 회전이 0이 아님', '100엔 = 933.3원이면 딱 1,400원 → 회전 0'],
        eqtable([('∮ A·dl', '한 바퀴 선적분', '닫힌 길을 돌며 얻은 것의 합'), ('∇×A', '나블라 곱하기 에이(회전)', '아주 작은 한 바퀴에서 남는 양'), ('det(…)', '행렬식', '카드 3/4·4/4: 회전을 자의 한 걸음 h와 함께 계산하는 틀')]),
        T('asst/E10', '세 환율이 서로 안 맞으면 한 바퀴에 돈이 남아요. 그게 회전이에요!')) + '</div>'
    h += daily('공항 환전소마다 환율이 조금씩 다른 것도 같은 이야기입니다(실제로는 수수료가 차이를 먹습니다).', '2부 방 9 "차익거래 = 회전"에서 시장이 이 남는 돈을 어떻게 지우는지 봅니다.')
    h += talk(T('fly/E08', '100엔 환율 슬라이더를 움직여서 한 바퀴 이익이 0이 되는 값을 찾아 봐.'),
              T('robo/E09', '1,400 ÷ 150 × 100 = 933.3원! 이 값을 기준선으로 그려 둘게요.'))
    h += lab(6, '실험 ⑥ 세 통화 한 바퀴 (가상 환율)', '세 환율을 바꿔 보세요 · 1,400원에서 출발',
             '<svg id="r6svg" role="img" aria-label="원·달러·엔 세 통화를 잇는 삼각형과 한 바퀴 이익"></svg>',
             sl('r6usd', '1달러 = 원', 1300, 1500, 10, 1400) + sl('r6jpy', '1달러 = 엔', 130, 170, 1, 150) + sl('r6kj', '100엔 = 원', 850, 1050, 1, 950), 330)
    h += '<div class="solve"><b>풀이</b> 한 바퀴 이익이 0이면 세 환율은 "높이 지도" 하나로 설명됩니다(언덕 화살표는 돌지 않는다). 0이 아니면 그런 지도가 없고, 흐름에 회전이 있습니다. 원자료 카드의 CURL 줄은 아주 작은 한 바퀴에서 이것을 잰 식입니다.</div>'
    h += dr('회전이 0이 아니라는 것은 "돌기만 해도 무언가 생긴다"는 신호입니다. 실제 시장에서는 이런 틈이 생기면 누군가 곧바로 돌려서 틈이 사라집니다. 그 이야기가 2부의 차익거래입니다. 숫자는 모두 가상 환율이고, 투자 권고가 아닙니다.')
    h += '<div class="limit"><b>이 방의 한계</b> 수수료와 사고파는 값 차이가 있으면 25원은 금방 사라집니다. 그리고 발산·회전은 흐름을 봤지, 한 자리 값이 주변과 얼마나 다른지는 보지 않았습니다. 사진으로 갑니다.</div>'
    h += quiz('1달러 = 1,500원, 1달러 = 150엔일 때, 한 바퀴 이익이 0이 되는 100엔 값은?', [('a', '900원'), ('b', '1,000원'), ('c', '1,500원')], 'b', '맞아요. 150엔 = 1,500원이라 100엔 = 1,000원.', '150엔이 1,500원과 같아야 합니다. 100엔은 그 3분의 2입니다.') + '</section>'

    # ---------- 방 7 사진 ----------
    h += room_head(7, '사진 윤곽선 — 라플라시안', ['원자료: 네 카드의 SCALAR LAPLACIAN 줄 (∇²f)', '방법: 내 값 − 주변 평균', '일상: 사진 편집 앱의 "선명하게"'])
    h += talk(T('sia/E19', '사진 앱에서 "윤곽선만 보기"를 누르면 테두리만 남아요. 어떻게 알아요?'),
              T('asst/E07', '이건 마지막 카드 줄이에요. 각 점의 밝기를 주변 평균과 비교하면 돼요!'))
    h += '<div class="pair">' + whybox(
        '사진은 밝기 숫자가 격자로 놓인 표입니다. 물체의 테두리는 밝기가 갑자기 바뀌는 곳입니다.',
        '방 5·6은 흐름(화살표)을 봤습니다. 이번에는 값(밝기) 하나만 있는 지도입니다.',
        '각 점의 밝기와 위·아래·왼쪽·오른쪽 네 이웃의 평균을 비교합니다. 차이가 크면 테두리, 0이면 평평한 곳입니다.',
        '단체 사진에서 혼자 튀는 옷 색을 찾는 것과 같습니다.') + mathbox(
        T('moa/E09', '어두운 바탕(50)에 밝은 점(200) 하나가 있으면요?'),
        '이웃 넷의 평균을 구하고, 내 값과의 차이를 봅니다. 둘레가 모두 50이면 평균도 50이고, 200과 150 차이가 납니다. 밝은 네모 안쪽은 이웃도 모두 200이라 차이가 0입니다.',
        '평균, 이차함수의 볼록·오목',
        ['가운데 밝기 200, 이웃 넷 50, 50, 50, 50', '이웃 평균 = <b>50</b>', '차이 200 − 50 = <b>150</b> → 테두리(튀는 점)', '밝은 네모 한가운데: 차이 <b>0</b> → 평평한 곳'],
        eqtable([('∇²f', '나블라 제곱 에프(라플라시안)', '주변 평균과 내 값의 차이에 비례(부호는 평균 − 나)'), ('∂²f/∂x² + ∂²f/∂y²', '—', '카드 1/4: 가로·세로 쪽 휘어짐의 합'), ('(1/r²)∂/∂r(r² ∂f/∂r) + …', '—', '카드 3/4: 둥근 자에서는 상자 크기가 같이 들어감')]),
        T('asst/E16', '밝은 네모의 안쪽은 0, 테두리만 숫자가 남아요. 그래서 윤곽선이에요!')) + '</div>'
    h += daily('사진 앱의 "선명하게"는 이 차이를 원래 사진에 조금 더해 테두리를 또렷하게 만듭니다.', '2부 방 11 "집값은 이웃을 닮아 간다", 3부 방 18 "이웃 평균으로 다듬기(GNN)"로 이어집니다.')
    h += talk(T('fly/E08', '"평균과 차이" 단추를 누르고, 밝은 네모 안쪽과 테두리를 눌러서 숫자를 비교해 봐.'),
              T('robo/E09', '고른 점의 이웃 평균과 차이를 제가 바로 계산할게요!'))
    h += lab(7, '실험 ⑦ 밝기 지도와 윤곽선', '사진 위 점을 누르거나 슬라이더로 고르세요',
             '<svg id="r7svg" role="img" aria-label="밝기 격자 사진과 라플라시안 윤곽선 지도"></svg>',
             sl('r7x', '가로 위치', 0, 10, 1, 2) + sl('r7y', '세로 위치', 0, 10, 1, 2), 360,
             '<div class="btns" role="group" aria-label="보기"><button class="btn" id="r7orig" aria-pressed="true">원래 사진</button><button class="btn" id="r7lap" aria-pressed="false">평균과 차이</button></div>')
    h += '<div class="solve"><b>풀이</b> 라플라시안은 "주변 평균과 나의 차이"입니다. 원자료 카드의 SCALAR LAPLACIAN 줄은 이것을 자마다 적은 식이고, 둥근 자에서는 0편 방 B의 상자 크기가 식 안에 들어갑니다.</div>'
    h += dr('라플라시안이 0인 곳은 "주변과 같은" 평평한 곳, 큰 곳은 튀는 곳입니다. 사진에서는 윤곽선, 데이터에서는 이상치 후보가 됩니다. 단, 튄다고 다 오류는 아닙니다. 왜 튀는지는 사람이 확인해야 합니다.')
    h += codebox([('scipy.ndimage.laplace(img)', '사진 전체에서 "이웃과의 차이"를 한 번에 계산한다')])
    h += '<div class="limit"><b>이 방의 한계</b> 여기서는 가로·세로 이웃만 봤습니다. 실제 사진 처리는 대각선 이웃과 흐림 처리를 함께 씁니다. 잡음이 많으면 잡음도 "튀는 점"으로 보입니다.</div>'
    h += quiz('밝기 100인 점의 이웃 넷이 100, 100, 100, 100입니다. 주변 평균과의 차이는?', [('a', '0 (평평한 곳)'), ('b', '100'), ('c', '400')], 'a', '맞아요. 평균 100, 차이 0이라 윤곽선이 아닙니다.', '이웃 넷의 평균을 먼저 구해 보세요. 모두 100입니다.') + '</section>'

    # ---------- 정리 ----------
    h += f"""
<section class="room" id="summary">
<h2>정리 — 일곱 방을 한 장으로</h2>
<p>같은 장면이 2부·3부에서 다시 나옵니다. 오른쪽 두 줄은 다음 부 예고입니다.</p>
<div class="scroll"><table class="sum"><thead><tr><th>방</th><th>원자료 카드의 개념</th><th>숫자로 한 번</th><th>2부 경제·금융</th><th>3부 AI·머신러닝</th></tr></thead><tbody>
<tr><td>1 피자</td><td>h<sub>φ</sub> = ρ</td><td>7.85 cm → 11.78 cm</td><td>경기순환시계</td><td>—</td></tr>
<tr><td>2 달력</td><td>각도 자 φ</td><td>12월–1월 0.52</td><td>—</td><td>달력 시계 특성</td></tr>
<tr><td>3 경도</td><td>h<sub>φ</sub> = r sinθ</td><td>111.2 → 55.6 km</td><td>상관을 각도로</td><td>가중치 길이와 걸음</td></tr>
<tr><td>4 지도</td><td>dV(표면)</td><td>12,360 → 6,180 km²</td><td>—</td><td>늘리면 묽어진다</td></tr>
<tr><td>5 지하철</td><td>발산</td><td>+400명</td><td>자금순환 샘·배수구</td><td>—</td></tr>
<tr><td>6 환전</td><td>회전</td><td>+25원</td><td>차익거래</td><td>—</td></tr>
<tr><td>7 사진</td><td>라플라시안</td><td>차이 150</td><td>집값 확산</td><td>이웃 평균으로 다듬기</td></tr>
</tbody></table></div>
</section>

<section id="outro">
<h2>아웃트로</h2>
{talk(T('asst/E16', '일곱 방 다 왔어요…! 피자에서 시작해서 사진까지, 결국 "자의 한 걸음"이랑 "주변과 비교하기"였어요.'),
      T('sia/E12', '선배, 이제 하나도 안 떨던데요? 환전 방에서 제일 멋있었어요.'),
      T('moa/E01', '숫자 기록은 다 모았어요. 2부에서 경제 이야기로 다시 꺼내 쓸게요!'),
      T('fly/E01', '그린란드 방에서 주판봇 답을 다시 확인한 거, 그게 오늘 제일 중요한 습관이야.'),
      T('robo/E12', '저도 이제 자의 한 걸음부터 확인합니다!'),
      T('doc/E16', '하루, 잘했어요. 정리 하나만 더 할게요. 모양에 맞는 자를 고르고, 한 걸음의 실제 길이를 챙기고, 흐름은 "솟아나나·도나", 값은 "주변과 다른가"로 봅니다. 2부에서 만나요.'))}
{crowd('방청석', [('x1/E01', '(짝짝짝)'), ('x2/E16', '(끄덕끄덕)'), ('x3/E01', '(반짝반짝)')])}
<a class="dashlink" href="dash_01.html"><b>1부 복습 대시보드 — 생활 장면 시뮬레이터 →</b><br>피자 가게·지구 배송센터·역과 환전소·사진 앱 네 현장을 직접 운영하며 일곱 방을 복습합니다. 미션 12개.</a>
<div class="nextp"><a href="00_orientation.html"><b>← 앞</b>0편 네 개의 자</a><a href="02_economy.html"><b>다음 →</b>2부 경제·금융</a></div>
</section>

<section id="kg">
<h2>지식 색인</h2>
<p>이 페이지의 개념과 나오는 방입니다.</p>
<div class="kg">
<a href="#room-1">호의 길이 · 방 1</a><a href="#room-1">축척 인자 h<sub>φ</sub> = ρ · 방 1</a><a href="#room-2">주기 데이터 · 방 2</a><a href="#room-2">각도 인코딩 · 방 2</a><a href="#room-3">위도·경도 · 방 3</a><a href="#room-3">h<sub>φ</sub> = r sinθ · 방 3</a><a href="#room-4">메르카토르 지도 · 방 4</a><a href="#room-4">면적 요소 · 방 4</a><a href="#room-5">발산 · 방 5</a><a href="#room-5">샘과 배수구 · 방 5</a><a href="#room-6">회전 · 방 6</a><a href="#room-6">삼각 환전 · 방 6</a><a href="#room-7">라플라시안 · 방 7</a><a href="#room-7">윤곽선 검출 · 방 7</a>
</div>
</section>

<section id="export">
<h2>온톨로지·서지 꾸러미</h2>
<p>이 페이지의 개념 관계와 인용 정보입니다. 다른 도구로 옮길 때 복사해 쓰세요.</p>
<div class="btns"><button class="btn" id="copyPack">꾸러미 복사</button><span id="copyMsg" style="align-self:center;font-size:14px;color:var(--mute)" aria-live="polite"></span></div>
<pre id="pack"></pre>
</section>
</main>
<footer><div class="wrap">
{AUTHOR}<br>
원자료: @eeanimation 「Vector Analysis」 인포그래픽 4장. 원자료의 φ·ϕ 혼용을 이 페이지에서는 φ로 씁니다.<br>
교육용 예시값: 피자 반지름, 월별 판매 예, 지하철 승하차 인원, 환율(가상), 사진 밝기. 지구 반지름 6,371 km와 그린란드·아프리카 넓이는 어림값입니다. 투자·경영 권고가 아닙니다. 캐릭터: 연구실 식구(fruitfly-lab-expressions). 표지는 픽셀아트 표지를 받기 전까지 쓰는 임시 그림입니다.
</div></footer>
"""
    return h

PAGE_JS = r"""
const SV=(t,a,inner='')=>`<${t} ${Object.entries(a).map(([k,v])=>`${k}="${v}"`).join(' ')}>${inner}</${t}>`;
// ---- 방 1 피자 ----
{const s=$('r1svg');
 const pizza=(cx,cy,R,rr,ang,col,lab)=>{const a0=-90*D2R,a1=a0+ang*D2R;
  let g=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="#fde0aa" stroke="#d4691f" stroke-width="5"/>`;
  g+=`<path d="M${cx},${cy} L${cx+R*Math.cos(a0)},${cy+R*Math.sin(a0)} A${R},${R} 0 ${ang>180?1:0} 1 ${cx+R*Math.cos(a1)},${cy+R*Math.sin(a1)} Z" fill="#f0a050" stroke="#c0392b" stroke-width="2"/>`;
  g+=`<path d="M${cx+R*Math.cos(a0)},${cy+R*Math.sin(a0)} A${R},${R} 0 0 1 ${cx+R*Math.cos(a1)},${cy+R*Math.sin(a1)}" fill="none" stroke="${col}" stroke-width="8" stroke-linecap="round"/>`;
  const L=rr*ang*D2R,am=(a0+a1)/2;g+=`<text x="${cx+(R+22)*Math.cos(am)}" y="${cy+(R+22)*Math.sin(am)}" font-size="15" font-weight="700" fill="${col}" text-anchor="middle">${L.toFixed(2)} cm</text>`;
  g+=`<text x="${cx}" y="${cy+R+28}" font-size="13" text-anchor="middle" fill="#1c2230">${lab}</text>`;return g};
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const r=+$('r1r').value,a=+$('r1a').value;const k=Math.min(W/2/23,(H-70)/2/21);
  s.innerHTML=pizza(W*0.27,H*0.46,10*k,10,a,'#24345c','기준 피자 반지름 10 cm')+pizza(W*0.72,H*0.46,r*k,r,a,'#c0392b',`반지름 ${r} cm`);
  const rad=a*D2R;$('r1read').innerHTML=`${a}° = <b>${rad.toFixed(3)} rad</b> · 기준 피자 테두리 10 × ${rad.toFixed(3)} = <b>${(10*rad).toFixed(2)} cm</b> · 반지름 ${r} cm 피자 테두리 ${r} × ${rad.toFixed(3)} = <b>${(r*rad).toFixed(2)} cm</b> (기준의 ${(r/10).toFixed(1)}배)`};
 bindSl('r1r',v=>v+' cm',draw)();bindSl('r1a',v=>v+'°',draw)();obs(s,draw)}
// ---- 방 2 달력 ----
{const s=$('r2svg');let mode='clock';
 const setM=m=>{mode=m;$('r2line').setAttribute('aria-pressed',m==='line');$('r2clock').setAttribute('aria-pressed',m==='clock');draw()};
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const m1=+$('r2m1').value,m2=+$('r2m2').value;
  const dline=Math.abs(m1-m2),dm=Math.min(dline,12-dline),chord=2*Math.sin(dm*15*D2R);let g='';
  if(mode==='line'){const x0=30,x1=W-30,y=H/2,X=m=>x0+(m-1)*(x1-x0)/11;g+=`<line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="#1c2230" stroke-width="2"/>`;
   for(let m=1;m<=12;m++)g+=`<circle cx="${X(m)}" cy="${y}" r="${m===m1||m===m2?9:5}" fill="${m===m1?'#c0392b':m===m2?'#1f7a8c':'#9aa3b0'}"/><text x="${X(m)}" y="${y+28}" font-size="13" text-anchor="middle" fill="#1c2230">${m}월</text>`;
   g+=`<path d="M${X(m1)},${y-18} Q${(X(m1)+X(m2))/2},${y-80} ${X(m2)},${y-18}" fill="none" stroke="#d4691f" stroke-width="3"/><text x="${(X(m1)+X(m2))/2}" y="${y-60}" font-size="15" font-weight="700" text-anchor="middle" fill="#d4691f">거리 ${dline}</text>`}
  else{const cx=W/2,cy=H/2,R=Math.min(W,H)*0.36,P=m=>{const t=(90-(m-1)*30)*D2R;return[cx+R*Math.cos(t),cy-R*Math.sin(t)]};
   g+=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#c9ced6" stroke-width="2"/>`;
   for(let m=1;m<=12;m++){const p=P(m),q=[cx+(R+22)*(p[0]-cx)/R,cy+(R+22)*(p[1]-cy)/R];g+=`<circle cx="${p[0]}" cy="${p[1]}" r="${m===m1||m===m2?9:5}" fill="${m===m1?'#c0392b':m===m2?'#1f7a8c':'#9aa3b0'}"/><text x="${q[0]}" y="${q[1]+5}" font-size="13" text-anchor="middle" fill="#1c2230">${m}월</text>`}
   const a=P(m1),b=P(m2);g+=`<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="#d4691f" stroke-width="3.5"/><text x="${cx}" y="${cy+6}" font-size="15" font-weight="700" text-anchor="middle" fill="#d4691f">거리 ${chord.toFixed(2)}</text>`}
  s.innerHTML=g;
  $('r2read').innerHTML=`${m1}월과 ${m2}월 · 숫자 줄 거리 <b>${dline}</b> · 시계판(반지름 1) 사이 각도 ${dm*30}° → 거리 2 × sin(${dm*15}°) = <b>${chord.toFixed(2)}</b>${dline>=6&&dm<=2?' — <span class="good">숫자 줄로는 멀지만 시계판으로는 이웃입니다.</span>':''}`};
 $('r2line').onclick=()=>setM('line');$('r2clock').onclick=()=>setM('clock');
 bindSl('r2m1',v=>v+'월',draw)();bindSl('r2m2',v=>v+'월',draw)();obs(s,draw)}
// ---- 방 3 경도 ----
{const s=$('r3svg');const E1=2*Math.PI*6371/360;
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const lat=+$('r3lat').value,la=lat*D2R;const cx=W*0.4,cy=H*0.52,R=Math.min(W*0.32,H*0.42);
  let g=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="#eef6fb" stroke="#24345c" stroke-width="3"/><line x1="${cx}" y1="${cy-R-14}" x2="${cx}" y2="${cy+R+14}" stroke="#5d6676" stroke-dasharray="4 4"/>`;
  g+=`<text x="${cx+6}" y="${cy-R-18}" font-size="12" fill="#5d6676">북극</text>`;
  [0,30,60].forEach(l=>{const y=cy-R*Math.sin(l*D2R),hw=R*Math.cos(l*D2R);g+=`<ellipse cx="${cx}" cy="${y}" rx="${hw}" ry="${hw*0.12}" fill="none" stroke="#c9d4de"/>`});
  const y=cy-R*Math.sin(la),hw=R*Math.cos(la);
  g+=`<ellipse cx="${cx}" cy="${y}" rx="${Math.max(hw,0.5)}" ry="${Math.max(hw*0.12,0.5)}" fill="none" stroke="#1f7a8c" stroke-width="3"/>`;
  g+=`<line x1="${cx}" y1="${cy}" x2="${cx+R*Math.cos(la)}" y2="${y}" stroke="#7a3fd6" stroke-width="2"/><line x1="${cx}" y1="${y}" x2="${cx+hw}" y2="${y}" stroke="#d4691f" stroke-width="5"/>`;
  g+=`<text x="${cx+hw/2}" y="${y+20}" font-size="13" font-weight="700" text-anchor="middle" fill="#d4691f">도는 원의 반지름</text>`;
  g+=`<line x1="${cx}" y1="${cy}" x2="${cx+R}" y2="${cy}" stroke="#9aa3b0" stroke-dasharray="3 3"/><text x="${cx-R*0.95}" y="${cy+18}" font-size="12" fill="#5d6676">적도 반지름 6,371 km</text>`;
  const bx=W*0.78,bw=W*0.16,bh=H*0.7,by=H*0.12;const v=E1*Math.cos(la);
  g+=`<rect x="${bx}" y="${by}" width="${bw}" height="${bh}" fill="#f5f7fa" stroke="#e2e6ec"/><rect x="${bx}" y="${by+bh*(1-v/E1)}" width="${bw}" height="${bh*v/E1}" fill="#1f7a8c"/>`;
  g+=`<text x="${bx+bw/2}" y="${by-6}" font-size="12" text-anchor="middle" fill="#1c2230">경도 1도</text><text x="${bx+bw/2}" y="${by+bh*(1-v/E1)-6}" font-size="14" font-weight="700" text-anchor="middle" fill="#1f7a8c">${v.toFixed(1)} km</text>`;
  s.innerHTML=g;
  $('r3read').innerHTML=`위도 <b>${lat}°</b> (북극에서 θ = ${(90-lat).toFixed(1)}°) · 도는 원의 반지름 = 6,371 × cos ${lat}° = <b>${fmt(6371*Math.cos(la),0)} km</b><br>경도 1도 = 111.2 × ${Math.cos(la).toFixed(3)} = <b>${v.toFixed(1)} km</b> · 위도 1도는 어디서나 약 111.2 km`};
 document.querySelectorAll('[data-lat]').forEach(b=>b.addEventListener('click',()=>{$('r3lat').value=b.dataset.lat;$('r3lat').dispatchEvent(new Event('input'))}));
 bindSl('r3lat',v=>v+'°',draw)();obs(s,draw)}
// ---- 방 4 지도 ----
{const s=$('r4svg');const A0=Math.pow(2*Math.PI*6371/360,2);
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const lat=+$('r4lat').value,c=Math.cos(lat*D2R);
  const u=Math.min(W*0.13,H*0.2);let g='';
  const col=(x,title,mapH,real,colr)=>{let t=`<text x="${x+u/2}" y="22" font-size="13" text-anchor="middle" fill="#1c2230" font-weight="700">${title}</text>`;
   t+=`<rect x="${x}" y="40" width="${u}" height="${u}" fill="none" stroke="#9aa3b0" stroke-width="2" stroke-dasharray="5 4"/><text x="${x}" y="${40+u+16}" font-size="12" fill="#5d6676">점선 = 지도 위 1°×1°</text>`;
   const side=u*Math.sqrt(real);t+=`<rect x="${x+(u-side)/2}" y="${40+(u-side)/2}" width="${side}" height="${side}" fill="${colr}" opacity=".8"/>`;return t};
  g+=col(W*0.08,'적도 0°',1,1,'#1f7a8c');g+=col(W*0.5,`위도 ${lat}°`,1,c*c,'#c0392b');
  const by=60+u+40,bw=W*0.84,bx=W*0.08;
  g+=`<text x="${bx}" y="${by}" font-size="13" fill="#1c2230">실제 땅 넓이 (적도 = 막대 끝)</text><rect x="${bx}" y="${by+8}" width="${bw}" height="16" fill="#eef1f4"/><rect x="${bx}" y="${by+8}" width="${bw*c}" height="16" fill="#c0392b"/>`;
  g+=`<text x="${bx}" y="${by+50}" font-size="13" fill="#1c2230">지도가 부풀린 배수</text><rect x="${bx}" y="${by+58}" width="${bw}" height="16" fill="#eef1f4"/><rect x="${bx}" y="${by+58}" width="${Math.min(bw,bw*(1/(c*c))/40)}" height="16" fill="#d4691f"/><text x="${bx+Math.min(bw,bw*(1/(c*c))/40)+6}" y="${by+71}" font-size="12" fill="#d4691f">${(1/(c*c)).toFixed(1)}배 (막대 끝 = 40배)</text>`;
  g+=`<text x="${W*0.08}" y="${by+100}" font-size="12" fill="#5d6676">빨간 네모 = 같은 지도 네모에 담긴 실제 땅의 크기</text>`;
  s.innerHTML=g;
  $('r4read').innerHTML=`위도 <b>${lat}°</b>의 1°×1° 땅 ≈ 12,360 × cos ${lat}° = <b>${fmt(A0*c,0)} km²</b> (적도의 ${(c*100).toFixed(0)}%)<br>흔한 세계 지도(메르카토르)는 이 땅을 약 <b>${(1/(c*c)).toFixed(1)}배</b> 크게 보여 줍니다 (1 ÷ cos²${lat}°)`};
 bindSl('r4lat',v=>v+'°',draw)();obs(s,draw)}
// ---- 방 5 지하철 ----
{const s=$('r5svg');
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const o=+$('r5out').value,i=+$('r5in').value,net=o-i;const cx=W/2,cy=H/2,R=Math.min(W,H)*0.13;
  let g=`<circle cx="${cx}" cy="${cy}" r="${R*2.6}" fill="none" stroke="#c9ced6" stroke-dasharray="5 5"/><text x="${cx}" y="${cy-R*2.6-8}" font-size="12" text-anchor="middle" fill="#5d6676">작은 상자(역 둘레)</text>`;
  g+=`<rect x="${cx-R}" y="${cy-R*0.7}" width="${2*R}" height="${1.4*R}" rx="10" fill="#e6f3f5" stroke="#1f7a8c" stroke-width="3"/><text x="${cx}" y="${cy+5}" font-size="14" font-weight="700" text-anchor="middle" fill="#1f7a8c">역</text>`;
  const n=16;for(let k=0;k<n;k++){const t=k/n*2*Math.PI+0.1;const outL=R*2.2*o/2000,inL=R*2.2*i/2000;
   const a=[cx+R*1.2*Math.cos(t),cy+R*1.2*Math.sin(t)];
   if(outL>2){const b=[a[0]+outL*Math.cos(t),a[1]+outL*Math.sin(t)];g+=`<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="#d4691f" stroke-width="3"/><circle cx="${b[0]}" cy="${b[1]}" r="3.5" fill="#d4691f"/>`}
   const t2=t+Math.PI/n;const c0=[cx+(R*1.25+inL)*Math.cos(t2),cy+(R*1.25+inL)*Math.sin(t2)],c1=[cx+R*1.25*Math.cos(t2),cy+R*1.25*Math.sin(t2)];
   if(inL>2)g+=`<line x1="${c0[0]}" y1="${c0[1]}" x2="${c1[0]}" y2="${c1[1]}" stroke="#24345c" stroke-width="3"/><circle cx="${c1[0]}" cy="${c1[1]}" r="3.5" fill="#24345c"/>`}
  g+=`<text x="14" y="${H-14}" font-size="12" fill="#d4691f">주황 = 내려서 동네로 나감</text><text x="${W-14}" y="${H-14}" font-size="12" text-anchor="end" fill="#24345c">남색 = 역으로 들어와 탐</text>`;
  s.innerHTML=g;const kind=net>0?'<span class="good">샘(+)</span> — 동네에 사람을 뿜어냅니다':net<0?'<span class="bad">배수구(−)</span> — 동네에서 사람을 빨아들입니다':'0 — 지나가기만 합니다';
  $('r5read').innerHTML=`나간 사람 ${fmt(o)}명 − 들어온 사람 ${fmt(i)}명 = <b>${net>0?'+':''}${fmt(net)}명</b> → ${kind}`};
 const setv=(a,b)=>{$('r5out').value=a;$('r5in').value=b;['r5out','r5in'].forEach(id=>$(id).dispatchEvent(new Event('input')))};
 $('r5am').onclick=()=>setv(1500,300);$('r5pm').onclick=()=>setv(300,1500);
 bindSl('r5out',v=>fmt(v)+'명',draw)();bindSl('r5in',v=>fmt(v)+'명',draw)();obs(s,draw)}
// ---- 방 6 환전 ----
{const s=$('r6svg');
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const u=+$('r6usd').value,j=+$('r6jpy').value,kj=+$('r6kj').value;
  const S=1400,usd=S/u,yen=usd*j,won=yen/100*kj,pr=won-S,be=u/j*100;
  const A=[W*0.5,H*0.15],B=[W*0.82,H*0.72],C=[W*0.18,H*0.72];
  const node=(p,t,v,c)=>`<circle cx="${p[0]}" cy="${p[1]}" r="34" fill="#fff" stroke="${c}" stroke-width="3"/><text x="${p[0]}" y="${p[1]+5}" font-size="15" font-weight="700" text-anchor="middle" fill="${c}">${t}</text><text x="${p[0]}" y="${p[1]+52}" font-size="13" font-weight="700" text-anchor="middle" fill="#1c2230">${v}</text>`;
  const edge=(p,q,t)=>{const dx=q[0]-p[0],dy=q[1]-p[1],L=Math.hypot(dx,dy),ux=dx/L,uy=dy/L,a=[p[0]+ux*40,p[1]+uy*40],b=[q[0]-ux*42,q[1]-uy*42];
   return`<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="#5d6676" stroke-width="2.5"/><polygon points="${b[0]},${b[1]} ${b[0]-10*ux+5*uy},${b[1]-10*uy-5*ux} ${b[0]-10*ux-5*uy},${b[1]-10*uy+5*ux}" fill="#5d6676"/><text x="${(a[0]+b[0])/2+uy*16}" y="${(a[1]+b[1])/2-ux*16+4}" font-size="12" text-anchor="middle" fill="#5d6676">${t}</text>`};
  let g=edge(C,A,'원 → 달러')+edge(A,B,'달러 → 엔')+edge(B,C,'엔 → 원');
  g+=node(C,'원',`${fmt(S)} → ${fmt(won,1)}`,'#24345c')+node(A,'달러',`${usd.toFixed(3)}`,'#1f7a8c')+node(B,'엔',`${yen.toFixed(1)}`,'#d4691f');
  const col=Math.abs(pr)<0.5?'#1e8a4c':pr>0?'#c0392b':'#7a3fd6';
  g+=`<text x="${W/2}" y="${H*0.62}" font-size="18" font-weight="900" text-anchor="middle" fill="${col}">한 바퀴 ${pr>=0?'+':''}${fmt(pr,1)}원</text>`;
  s.innerHTML=g;
  $('r6read').innerHTML=`1,400원 → ${usd.toFixed(3)}달러 → ${yen.toFixed(1)}엔 → <b>${fmt(won,1)}원</b> · 한 바퀴 <b>${pr>=0?'+':''}${fmt(pr,1)}원</b>${Math.abs(pr)<0.5?' — <span class="good">회전 0: 세 환율이 서로 맞습니다.</span>':' — <span class="bad">회전이 0이 아닙니다.</span>'}<br>이 두 환율과 맞는 100엔 값: ${fmt(u,0)} ÷ ${j} × 100 = <b>${fmt(be,1)}원</b>`};
 bindSl('r6usd',v=>fmt(v)+'원',draw)();bindSl('r6jpy',v=>v+'엔',draw)();bindSl('r6kj',v=>fmt(v)+'원',draw)();obs(s,draw)}
// ---- 방 7 사진 ----
{const s=$('r7svg'),N=11;let mode='orig';const img=[];
 for(let y=0;y<N;y++){img.push([]);for(let x=0;x<N;x++)img[y].push(50)}
 img[2][2]=200;for(let y=4;y<=8;y++)for(let x=5;x<=9;x++)img[y][x]=200;
 const v=(x,y)=>(x<0||y<0||x>=N||y>=N)?50:img[y][x];
 const avg=(x,y)=>(v(x-1,y)+v(x+1,y)+v(x,y-1)+v(x,y+1))/4;
 const setM=m=>{mode=m;$('r7orig').setAttribute('aria-pressed',m==='orig');$('r7lap').setAttribute('aria-pressed',m==='lap');draw()};
 let cs=1,ox=0,oy=0;
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const sx=+$('r7x').value,sy=+$('r7y').value;cs=Math.min((W-20)/N,(H-20)/N);ox=(W-cs*N)/2;oy=(H-cs*N)/2;let g='';
  for(let y=0;y<N;y++)for(let x=0;x<N;x++){let f;if(mode==='orig'){const b=Math.round(v(x,y));f=`rgb(${b},${b},${b})`}else{const d=v(x,y)-avg(x,y);const t=Math.min(1,Math.abs(d)/150);f=d>0?`rgba(192,57,43,${0.1+t*0.9})`:d<0?`rgba(36,52,92,${0.1+t*0.9})`:'#ffffff'}
   g+=`<rect x="${ox+x*cs}" y="${oy+y*cs}" width="${cs-1}" height="${cs-1}" fill="${f}" data-x="${x}" data-y="${y}" style="cursor:pointer"/>`;
   if(mode==='lap'&&cs>28){const d=v(x,y)-avg(x,y);if(d)g+=`<text x="${ox+x*cs+cs/2}" y="${oy+y*cs+cs/2+4}" font-size="${Math.min(12,cs/3)}" text-anchor="middle" fill="#fff" pointer-events="none">${d>0?'+':''}${Math.round(d)}</text>`}}
  g+=`<rect x="${ox+sx*cs-2}" y="${oy+sy*cs-2}" width="${cs+3}" height="${cs+3}" fill="none" stroke="#d4691f" stroke-width="4"/>`;
  s.innerHTML=g;const me=v(sx,sy),a=avg(sx,sy),d=me-a;
  $('r7read').innerHTML=`고른 점 (가로 ${sx}, 세로 ${sy}) · 내 밝기 <b>${me}</b> · 이웃 넷 ${v(sx,sy-1)}, ${v(sx,sy+1)}, ${v(sx-1,sy)}, ${v(sx+1,sy)} → 평균 <b>${a}</b><br>내 값 − 주변 평균 = <b>${d>0?'+':''}${d}</b> → ${d===0?'평평한 곳 (윤곽선 아님)':Math.abs(d)>=100?'<span class="bad">크게 튀는 점</span>':'<span class="good">윤곽선(테두리)</span>'} <span style="font-size:14px;color:#5d6676">사진 바깥은 바탕 밝기 50으로 봅니다.</span>`};
 s.addEventListener('click',e=>{const t=e.target;if(t.dataset&&t.dataset.x!==undefined){$('r7x').value=t.dataset.x;$('r7y').value=t.dataset.y;['r7x','r7y'].forEach(id=>$(id).dispatchEvent(new Event('input')))}});
 $('r7orig').onclick=()=>setM('orig');$('r7lap').onclick=()=>setM('lap');
 bindSl('r7x',v=>v,draw)();bindSl('r7y',v=>v,draw)();obs(s,draw)}
"""

PACK_DATA = {
    "page": "벡터 분석 랩 1부 — 같은 1도, 다른 길이", "author": "안상선 ((주)M-Robo)",
    "url": "https://adminmrobo.github.io/vector_analysis_lab/01_everyday.html",
    "source": "@eeanimation, Vector Analysis infographic 1/4–4/4",
    "concepts": ["축척 인자", "호의 길이", "주기 데이터 각도 표현", "위도별 경도 길이", "면적 요소", "메르카토르 왜곡", "발산", "회전", "라플라시안", "윤곽선 검출"],
    "relations": [["피자 테두리", "보여 준다", "h_φ = ρ"], ["경도 1도", "보여 준다", "h_φ = r sinθ"],
                  ["메르카토르 왜곡", "까닭", "면적 요소 r² sinθ"], ["지하철역 승하차", "보여 준다", "발산"],
                  ["삼각 환전", "보여 준다", "회전"], ["윤곽선 검출", "쓴다", "라플라시안"],
                  ["달력 시계판", "이어진다", "3부 달력 시계 특성"], ["삼각 환전", "이어진다", "2부 차익거래"]],
    "example_values": {"피자 45°": [7.85, 11.78], "12월-1월 시계판 거리": 0.52, "경도 1도 km": {"0°": 111.2, "37.5°": 88.2, "60°": 55.6},
                       "1°×1° 넓이 km²": {"0°": 12364, "60°": 6182}, "환전 한 바퀴 원": 25, "사진 점 차이": 150},
    "cite": "안상선 (2026). 벡터 분석 랩 1부 — 같은 1도, 다른 길이. https://adminmrobo.github.io/vector_analysis_lab/01_everyday.html"
}

if __name__ == '__main__':
    import math
    assert abs(10 * math.pi / 4 - 7.854) < 1e-3 and abs(15 * math.pi / 4 - 11.781) < 1e-3
    assert abs(2 * math.sin(math.radians(15)) - 0.5176) < 1e-3
    e1 = 2 * math.pi * 6371 / 360
    assert abs(e1 - 111.19) < 0.01 and abs(e1 * math.cos(math.radians(37.5)) - 88.2) < 0.1 and abs(e1 * 0.5 - 55.6) < 0.05
    assert abs(e1 ** 2 - 12364) < 2 and abs(1 / math.cos(math.radians(72)) ** 2 - 10.5) < 0.1
    assert abs(150 / 100 * 950 - 1425) < 1e-9 and abs(1400 / 150 * 100 - 933.33) < 0.01
    b = body()
    n = page('01_everyday.html', '벡터 분석 랩 1부 — 같은 1도, 다른 길이',
             '피자 테두리, 달력, 경도 1도, 세계 지도, 지하철역, 환전, 사진 윤곽선. 원자료 카드 네 장의 한 걸음 h·dV·발산·회전·라플라시안을 생활 장면 일곱 개로 봅니다.',
             'assets/og/01.webp', b, PAGE_JS, PACK_DATA,
             ['축척 인자', '부피 요소', '발산', '회전', '라플라시안', '위도·경도', '메르카토르 지도'])
    print('01 bytes', n)
