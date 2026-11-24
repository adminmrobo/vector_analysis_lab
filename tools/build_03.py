# -*- coding: utf-8 -*-
"""3부 AI·머신러닝 — 자를 잘 고르면 모델이 쉬워진다 (방 13~18 + 대결)"""
from common import *
P = '3부'

DUEL = [
    ('풍력 발전기 날개 끝이 도는 속도를 계산하려면 어느 자?', '가로·세로·높이 자로 x, y를 매번 계산하겠습니다.', '원통 자요! 날개는 축 둘레를 도니까 ρ·φ로 읽으면 한 줄이에요.', 'haru', '도는 물체는 원통 자. 날개 끝 속도 = ρ × 도는 빠르기(1부 방 1의 h = ρ).'),
    ('서울에서 뉴욕까지 비행 거리는?', '지구본 자로 잽니다. 위도·경도 차이에 r sinθ를 챙겨야 해요.', '지도에 자를 대고 곧게 재면 돼요!', 'doc', '평평한 지도 위 직선은 실제 최단 경로가 아닙니다(1부 방 3·4). 공 위의 거리는 지구본 자로.'),
    ('물류 창고 선반의 상자 위치를 기록하려면?', '창고 가운데 기둥을 중심으로 원통 자를 쓰지요.', '가로·세로·높이 자요. 선반이 바둑판처럼 곧게 서 있으니까요.', 'haru', '곧은 선반에는 곧은 자. 모양에 맞는 자를 고르는 것이 핵심입니다(0편 방 A).'),
    ('하루 중 시각(0~23시)을 AI 특성으로 넣으려면?', '시계판 각도로 바꿔 cos·sin 두 숫자로 넣습니다.', '0부터 23까지 숫자 그대로 넣으면 돼요!', 'doc', '23시와 0시는 이웃입니다. 숫자 그대로면 가장 멀어집니다(방 13).'),
    ('두 문장의 뜻이 비슷한지 비교하려면?', '두 화살표 끝 사이 거리로 재면 되겠지요.', '방향(각도)을 봐야 해요. 길이는 문장 길이 따라 달라지니까 코사인으로요!', 'haru', '임베딩 비교는 방향 = 코사인 유사도(방 14). 길이는 뜻과 상관없이 달라질 수 있습니다.'),
]

def duel():
    h = ''
    for i, (q, d, a, win, why) in enumerate(DUEL):
        USED.extend(['doc/E07', 'asst/E07'])
        h += f"""<div class="lab" id="duel{i}" data-win="{win}"><div class="hd"><b>{i+1}판 · {q}</b><span>누구 답이 맞을까요? 눌러서 판정하세요</span></div>
<div class="talk">{T('doc/E07', d)}{T('asst/E07', a)}</div>
<div class="btns"><button class="btn" data-pick="doc">박사가 맞다</button><button class="btn" data-pick="haru">하루가 맞다</button></div>
<div class="read" aria-live="polite" style="display:none"></div></div>"""
    return h

def body():
    h = f"""
<header class="hero"><div class="wrap">
<div class="wing">벡터 분석 랩 · 3부 AI·머신러닝</div>
<h1>자를 잘 고르면 모델이 쉬워진다<br>달력 특성·임베딩·RoPE·학습 걸음·흐름 모델·GNN</h1>
<p class="sub">1부와 2부에서 본 장면이 인공지능 안에서 어떻게 쓰이는지 봅니다. 마지막에는 박사와 하루가 "이 문제엔 어느 자?" 대결을 벌이고, 여러분이 심판을 봅니다.</p>
<figure class="cover" style="margin-left:0;margin-right:0"><img src="assets/cover_03.webp" width="1600" height="900" alt="점 구름 구·관계망·시계판 앞에서 자신감을 찾은 하루와 연구실 식구들 (임시 표지)"></figure>
<div class="by">{AUTHOR}</div>
<a class="cta" href="#room-13">방 13부터 들어가기</a>
</div></header>
<main class="wrap">
<section>{three([('무엇을', '시계판 각도·구 위의 방향·회전·1/r 걸음·작은 상자 dV·이웃 평균이 AI 모델 안에서 하는 일을 봅니다.'),
                  ('왜 중요한가', '데이터를 맞는 자로 놓으면 모델이 같은 데이터로 더 잘 배우고, 결과를 덜 틀리게 읽습니다.'),
                  ('업무에서는', '판매 예측 특성 만들기, 문서 검색(임베딩), 언어 모델의 위치 처리, 학습 설정, 생성 모델, 추천·관계망 분석에 씁니다.')],
                 '코드·수식을 몰라도 됩니다. 수치는 교육용 예시입니다. 경사 하강과 GAN의 회전은 <a href="https://adminmrobo.github.io/vector_calculus_lab/">∇ 특별편</a>에서 다룹니다.',
                 [('임베딩', '문장·단어·사진을 화살표(숫자 목록)로 바꾼 것'), ('RoPE', 'Rotary Position Embedding. 단어 자리만큼 화살표를 돌려 위치를 넣는 방법'),
                  ('GNN', 'Graph Neural Network. 관계망(그래프) 위에서 이웃 정보를 섞는 신경망'), ('평균 오차', '이 페이지에서는 빗나간 값을 제곱해 평균 낸 뒤 제곱근(RMSE)'),
                  ('가중치 감쇠', '학습할 때마다 가중치 길이를 조금씩 줄이는 설정(weight decay)'), ('흐름 모델', '쉬운 분포를 늘이고 비틀어 복잡한 분포를 만드는 생성 모델(normalizing flow)'),
                  ('야코비안', '좌표를 바꿀 때 작은 상자가 늘어난 배수. 0편의 dV와 같은 생각'), ('θ, r', '각도(세타), 화살표 길이'), ('α', '섞는 비율(속도)')])}</section>
<section id="opening"><h2>오늘의 장면 — 하루의 마지막 수업</h2>
{talk(T('asst/E19', '마지막 수업이에요. 이번엔 AI라서… 사실 제일 자신 있어요!'),
      T('moa/E12', '선배 표정이 첫날이랑 완전히 달라요!'))}
{crowd('방청석', [('x1/E04', '(오!)'), ('x2/E16', '(끄덕)'), ('x3/E01', '(반짝)')])}
{talk(T('fly/E10', '자신 있을 때가 제일 위험해. 숫자는 끝까지 확인하자.'),
      T('robo/E13', 'AI 숫자는 제 전문! …이라고 말하면 초파리 연구원한테 혼나겠죠?'),
      T('doc/E08', '마지막에 저랑 하루가 대결을 합니다. 독자 여러분이 심판이에요.'))}
<div class="map" style="margin-top:18px">
<a class="f" href="#room-13"><b>방 13</b>달력 시계 특성<span class="why">← 방 2 · 방 8</span></a>
<a class="f" href="#room-14"><b>방 14</b>임베딩은 구 위의 점<span class="why">← 방 3 · 방 12</span></a>
<a class="f" href="#room-15"><b>방 15</b>위치를 각도로(RoPE)<span class="why">← 방 6 · 방 9</span></a>
<a class="f" href="#room-16"><b>방 16</b>가중치가 길어지면 걸음이 작아진다<span class="why">← 0편 방 A의 1/h</span></a>
<a class="f" href="#room-17"><b>방 17</b>늘리면 묽어진다<span class="why">← 0편 방 B · 방 4</span></a>
<a class="f" href="#room-18"><b>방 18</b>이웃 평균으로 다듬기(GNN)<span class="why">← 방 7 · 방 11</span></a>
<a class="e" href="#duel"><b>대결</b>박사 vs 하루<span class="why">이 문제엔 어느 자?</span></a>
</div>
<div class="easy" style="margin-top:16px"><b>30초 복습</b> 도는 데이터는 각도로(방 2·8), 상관은 화살표 사이 각도(방 12), 각도 쪽 한 걸음에는 반지름이 붙는다(0편 방 A), 작은 상자 크기는 h의 곱(0편 방 B), 라플라시안으로 섞으면 이웃을 닮는다(방 11). 앞 부를 건너뛰었어도 방마다 다시 짚습니다.</div>
</section>
"""
    # 방 13
    h += room_head(P, 13, '달력 시계 특성 — 12월과 1월을 이웃으로', ['원자료: 카드 2/4 위쪽 그림 (각도 φ)', '방법: 달 → (cos, sin) 두 숫자', '일상: 아이스크림 월별 판매'])
    h += talk(T('moa/E09', '월별 아이스크림 판매를 예측하는데, 달을 1~12 숫자로 넣으면 왜 잘 안 맞아요?'),
              T('asst/E10', '1부 방 2 기억나요? 숫자 줄에선 12월과 1월이 제일 멀어요. 모델도 그렇게 믿어 버려요.'))
    h += '<div class="pair">' + whybox(
        '가장 단순한 예측 모델은 "숫자가 커지면 판매도 일정하게 커진다(또는 작아진다)"는 직선입니다. 그런데 판매는 7월에 꼭대기를 찍고 다시 내려옵니다.',
        '1부 방 2·2부 방 8에서 도는 데이터는 각도로 보는 것까지 봤습니다. 이번에는 그 각도를 모델에 넣습니다.',
        '달을 시계판 위 점 (cos, sin) 두 숫자로 바꿔 넣습니다. 그러면 같은 직선 모델도 "한 바퀴 도는 모양"을 그릴 수 있습니다.',
        '자를 바꿨을 뿐인데 같은 모델이 훨씬 잘 맞습니다.') + mathbox(
        T('sia/E09', '가상 판매 40, 48, 70, 100, 130, 152, 160, 152, 130, 100, 70, 48로 해 보면요?'),
        '숫자 특성 직선은 1월에서 12월로 갈수록 판매가 조금씩 늘어난다고 봅니다. 시계 특성은 cos 한 숫자에 −60을 곱하고 100을 더하면 열두 달이 정확히 맞습니다.',
        '일차함수, 삼각함수 cos·sin, 평균 오차',
        ['숫자 특성 직선: 판매 ≈ 83.6 + 2.5 × 달 → 평균 오차(RMSE) <b>41.5</b>', '12월 예측 113.8 (실제 48), 1월 예측 86.2 (실제 40) — 크게 틀림', '시계 특성: 판매 = 100 − 60 × cos(각도) → 평균 오차 <b>0</b>', '12월과 1월 특성 거리 0.52 → 모델도 이웃으로 봄'],
        eqtable([('θ = 30° × (달 − 1)', '세타', '달을 시계판 각도로'), ('(cos θ, sin θ)', '—', '모델에 넣는 두 숫자'), ('100 − 60 cos θ', '—', '가상 판매에 딱 맞는 식')]),
        T('asst/E16', '모델을 바꾼 게 아니라 자를 바꿨어요. 그래서 원자료 카드가 중요한 거예요!')) + '</div>'
    h += daily('출근 시간대, 요일, 계절처럼 도는 데이터는 모두 시계판에 놓을 수 있습니다.', '대결 4판에서 "하루 중 시각"을 어느 자로 넣을지 겨룹니다.', '대결에서는')
    h += talk(T('fly/E08', '숫자 특성과 시계 특성을 번갈아 눌러 봐. 그리고 "가장 잘 팔리는 달"도 바꿔 봐.'),
              T('robo/E09', '두 모델의 평균 오차를 바로 계산해 드릴게요!'))
    h += lab(13, '실험 ⑬ 숫자 특성 vs 시계 특성 (가상 판매)', '특성 방식을 바꾸거나 데이터를 바꿔 보세요',
             '<svg id="r13svg" role="img" aria-label="월별 가상 판매 막대와 두 모델의 예측선"></svg>',
             sl('r13amp', '계절 차이', 20, 80, 5, 60) + sl('r13pk', '가장 잘 팔리는 달', 1, 12, 1, 7), 340,
             '<div class="btns" role="group" aria-label="특성 방식"><button class="btn" id="r13n" aria-pressed="false">숫자 특성(1~12)</button><button class="btn" id="r13c" aria-pressed="true">시계 특성(cos, sin)</button></div>')
    h += '<div class="solve"><b>풀이</b> 같은 직선 모델이라도, 시계 특성은 cos·sin 두 숫자의 무게를 조절해 "꼭대기가 몇 월인지"와 "얼마나 출렁이는지"를 모두 나타냅니다. 원통 자의 각도 φ를 특성으로 쓴 것입니다.</div>'
    h += dr('특성 만들기(feature engineering)의 첫 질문은 "이 데이터는 어떤 모양의 자에 놓여 있나"입니다. 도는 데이터를 숫자 줄에 놓으면, 아무리 좋은 모델도 엉뚱한 곳을 이웃으로 봅니다.')
    h += codebox([('np.cos(2*np.pi*(m-1)/12), np.sin(2*np.pi*(m-1)/12)', '달 m을 시계판 두 숫자로')])
    h += '<div class="limit"><b>이 방의 한계</b> 실제 판매는 한 바퀴 모양에 추세·행사·날씨가 겹칩니다. 시계 특성은 그중 "도는 부분"만 잘 잡습니다. 다음은 단어처럼 축이 아주 많은 데이터입니다.</div>'
    h += quiz('하루 중 23시와 1시를 시계판(24시간 = 360°)에 놓으면 사이 각도는?', [('a', '330°'), ('b', '30°'), ('c', '22°')], 'b', '맞아요. 2시간 차이 = 30°, 이웃입니다.', '한 시간에 15°입니다. 23시 → 0시 → 1시, 몇 시간 차이인가요?') + '</section>'

    # 방 14
    h += room_head(P, 14, '임베딩은 구 위의 점 — 길이 말고 방향', ['원자료: 카드 3/4 (지구본 자, r을 1로)', '방법: 코사인 유사도 = 방향만 비교', '일상: 문서 검색'])
    h += talk(T('sia/E09', 'AI가 문장을 화살표(임베딩)로 바꾼다던데, 비슷한 문장을 어떻게 찾아요?'),
              T('asst/E07', '방향을 봐요! 2부 방 12의 상관처럼, 두 화살표 사이 각도의 코사인이요.'))
    h += '<div class="pair">' + whybox(
        '문장·사진·상품을 화살표(임베딩)로 바꾸면 "뜻이 비슷한가"를 숫자로 잴 수 있습니다. 그런데 화살표 길이는 문장 길이나 단어 수에 따라 달라지기도 합니다.',
        '0편 입구 방에서는 두 점 사이 거리로 "닮지 않은 정도"를 쟀습니다. 거리는 길이 차이에도 흔들립니다.',
        '길이를 1로 맞춰(구 위의 점으로 놓고) 방향만 비교합니다. 지구본 자에서 r을 버리고 θ·φ만 보는 것과 같습니다.',
        '두 사람이 같은 곳을 가리키면, 팔 길이가 달라도 같은 곳을 본 것입니다.') + mathbox(
        T('moa/E09', '(3, 4)와 (6, 8)은 거리가 5인데 비슷한 거예요?'),
        '(6, 8)은 (3, 4)를 두 배로 늘린 것이라 방향이 같습니다. 겹침 점수(내적)를 두 길이의 곱으로 나누면 코사인이 나옵니다.',
        '벡터의 내적, 코사인, 피타고라스',
        ['(3,4)·(6,8) = 18 + 32 = 50, 길이 5 × 10 = 50 → 코사인 <b>1</b> (같은 방향)', '두 점 사이 거리는 <b>5</b> — 거리로만 보면 꽤 멀어 보임', '(3,4)와 (4,3): 24 ÷ 25 = <b>0.96</b> (거의 같은 방향)', '직각이면 코사인 0, 반대면 −1'],
        eqtable([('cos θ = (a·b) ÷ (|a||b|)', '코사인 세타', '방향이 얼마나 같은가(−1~1)'), ('a ÷ |a|', '—', '길이를 1로 맞춤 = 구 위의 점')]),
        T('asst/E10', '길이를 지우고 방향만 보면, 짧은 문장과 긴 문장도 공평하게 비교돼요.')) + '</div>'
    h += daily('검색창에 질문을 넣으면, 질문과 방향이 가장 비슷한 문서들이 위에 뜹니다.', '대결 5판에서 "문장 비교는 어느 자?"로 다시 나옵니다.', '대결에서는')
    h += talk(T('fly/E08', '화살표 B의 길이만 바꿔 봐. 거리는 바뀌는데 코사인은?'),
              T('robo/E09', '코사인과 거리를 나란히 계산해 둘게요!'))
    h += lab(14, '실험 ⑭ 방향 vs 거리', 'A = (3, 4)는 고정, B의 각도와 길이를 바꿔 보세요',
             '<svg id="r14svg" role="img" aria-label="두 화살표와 사이 각도, 길이 1 원"></svg>',
             sl('r14a', 'A와 B 사이 각도', 0, 180, 1, 0) + sl('r14l', 'B의 길이', 1, 12, 0.5, 10), 330)
    h += '<div class="solve"><b>풀이</b> 코사인은 길이를 나눠 없애므로 방향만 남습니다. 모든 화살표를 길이 1로 맞추면 끝점이 구 위에 놓이고, 원자료 카드 3/4의 θ·φ만으로 비교하는 셈입니다.</div>'
    h += dr('임베딩 검색에서 "가장 가까운 문서"는 대개 코사인이 가장 큰 문서입니다. 다만 코사인이 높다고 뜻이 같다고 단정하면 안 됩니다. 결과 문서를 사람이 한 번 읽어 확인하세요.')
    h += '<div class="limit"><b>이 방의 한계</b> 실제 임베딩은 축이 수백~수천 개입니다. 그림은 2축으로 줄였습니다. 다음은 화살표를 "돌려서" 위치를 넣는 방법입니다.</div>'
    h += quiz('(1, 0)과 (0, 5)의 코사인 유사도는?', [('a', '0'), ('b', '5'), ('c', '1')], 'a', '맞아요. 겹침 점수 0, 직각이라 코사인 0입니다.', '같은 자리끼리 곱해 더하면 1×0 + 0×5입니다.') + '</section>'

    # 방 15
    h += room_head(P, 15, '위치를 각도로(RoPE) — 떨어진 거리만 남기기', ['원자료: 카드 2/4 (각도 φ로 돌리기)', '방법: 자리마다 같은 각도씩 돌리기', '일상: 문장 속 단어 순서'])
    h += talk(T('moa/E09', '언어 모델은 "개가 사람을 물었다"와 "사람이 개를 물었다"를 어떻게 구별해요?'),
              T('asst/E07', '단어 화살표를 자리 번호만큼 돌려요! 그러면 두 단어가 몇 자리 떨어졌는지가 각도로 남아요.'))
    h += '<div class="pair">' + whybox(
        '문장에서 단어의 순서와 거리가 뜻을 바꿉니다. 모델에 "몇 번째 자리인가"를 알려 줘야 합니다.',
        '1부 방 6·2부 방 9에서 "한 바퀴 돌아 남는 것"을 봤습니다. 이번에는 돌리기 자체를 정보로 씁니다.',
        '자리 번호마다 화살표를 같은 각도씩 돌립니다(예: 한 자리에 30°). 두 단어의 겹침 점수는 각도 차이에만 달려서, 어디에 있든 "몇 자리 떨어졌나"만 남습니다.',
        '시계 두 개의 바늘 각도 차이는, 두 시계를 함께 돌려도 그대로입니다.') + mathbox(
        T('sia/E09', '2번·4번 자리와 5번·7번 자리는 겹침 점수가 같아요?'),
        '두 쌍 모두 두 자리 떨어져서 각도 차이가 60°입니다. 겹침 점수는 cos 60° = 0.5로 같습니다.',
        '회전, 삼각함수 cos, 벡터의 내적',
        ['2번 → 60°, 4번 → 120° → 차이 60° → 겹침 <b>0.5</b>', '5번 → 150°, 7번 → 210° → 차이 60° → 겹침 <b>0.5</b>', '세 자리 떨어지면 90° → 겹침 <b>0</b>', '절대 자리는 사라지고 상대 거리만 남음'],
        eqtable([('q 를 m × 30° 돌림', '—', 'm번째 자리 단어 화살표'), ('겹침 = cos(30° × (n − m))', '—', '두 자리의 차이만으로 정해짐')]),
        T('asst/E16', '돌려도 남는 건 차이뿐! 회전이 이렇게 쓸모 있을 줄이야.')) + '</div>'
    h += daily('두 사람이 같은 회전목마에 타면, 회전목마가 얼마나 돌았든 둘 사이 각도는 그대로입니다.', '실제 언어 모델은 축 두 개씩 묶어 여러 빠르기로 돌립니다(이 페이지는 한 쌍만).', '조금 더')
    h += talk(T('fly/E08', '두 단어를 똑같이 한 자리씩 함께 옮겨 봐. 겹침 점수가 바뀌어?'),
              T('robo/E09', '자리 차이와 겹침 점수를 표로 띄울게요!'))
    h += lab(15, '실험 ⑮ 자리만큼 돌리기', '두 단어의 자리를 바꿔 보세요 · 한 자리에 30°',
             '<svg id="r15svg" role="img" aria-label="두 단어 화살표의 회전과 사이 각도"></svg>',
             sl('r15i', '단어 1 자리', 0, 11, 1, 2) + sl('r15j', '단어 2 자리', 0, 11, 1, 4), 330,
             '<div class="btns"><button class="btn" id="r15both">둘 다 한 자리 뒤로</button></div>')
    h += '<div class="solve"><b>풀이</b> 회전은 길이를 바꾸지 않고 방향만 바꿉니다. 두 화살표를 같은 만큼 더 돌리면 사이 각도는 그대로입니다. 그래서 겹침 점수에는 "떨어진 거리"만 남습니다.</div>'
    h += dr('이 방법(회전 위치 부호화, RoPE)은 여러 언어 모델에서 쓰입니다. 여기서는 축 한 쌍, 한 가지 빠르기로 단순하게 봤어요.')
    h += '<div class="limit"><b>이 방의 한계</b> 한 가지 빠르기로만 돌리면 12자리마다 같은 각도가 되풀이됩니다. 실제로는 여러 빠르기를 섞어 이 문제를 줄입니다. 다음은 학습이 실제로 한 걸음씩 움직이는 모습입니다.</div>'
    h += quiz('한 자리에 30°씩 돌릴 때, 0번과 6번 자리 단어의 겹침 점수는?', [('a', '1'), ('b', '0'), ('c', '−1')], 'c', '맞아요. 180° 차이라 cos 180° = −1.', '여섯 자리 × 30° = 몇 도인가요?') + '</section>'

    # 방 16
    h += room_head(P, 16, '가중치가 길어지면 걸음이 작아진다 — 기울기에 붙는 1/r', ['원자료: 카드 3/4 GRADIENT 줄의 1/r', '방법: 방향만 보는 모델의 학습 걸음', '일상: 큰 원을 돌 때 같은 걸음의 각도'])
    h += talk(T('sia/E09', '같은 학습률인데 어떤 때는 학습이 느려진대요. 0편의 1/r이랑 관계있어요?'),
              T('asst/E15', '어, 이건 저도 헷갈렸는데… 지구본 자 기울기 식을 그대로 보면 돼요!'))
    h += '<div class="pair">' + whybox(
        '정규화 층 바로 앞에 놓인 가중치처럼, 출력이 가중치의 "방향"에만 달려 있고 길이에는 달려 있지 않은 경우가 있습니다. 그런데 학습 속도는 길이에 따라 달라집니다.',
        '0편 방 A에서 각도 쪽 기울기에 1/r이 붙는 것을 봤습니다.',
        '출력이 방향에만 달리면 기울기는 각도 쪽 성분만 있고, 그 크기는 (1/r) × (각도 쪽 변화)입니다. 한 걸음에 도는 각도는 다시 r로 나눠 1/r²이 됩니다. 가중치가 두 배 길면 네 배 느리게 돕니다.',
        '큰 원 둘레를 같은 보폭으로 걸으면, 작은 원보다 조금씩만 돕니다.') + mathbox(
        T('moa/E09', '(3, 4)와 (6, 8)은 출력이 같은데, 걸음은 얼마나 달라요?'),
        '각도 쪽 변화가 1이라고 하면, 기울기 크기는 1 ÷ 길이입니다. 그 걸음으로 도는 각도는 기울기 ÷ 길이입니다.',
        '분수, 호의 길이 = 반지름 × 각도',
        ['길이 5: 기울기 1/5 = <b>0.2</b>, 한 걸음 각도 0.2 ÷ 5 = <b>0.04 rad (2.3°)</b>', '길이 10: 기울기 <b>0.1</b>, 한 걸음 각도 <b>0.01 rad (0.57°)</b> — 4배 느림', '45°(0.785 rad) 도는 데: 길이 5는 <b>약 20걸음</b>, 길이 10은 <b>약 79걸음</b>', '그래서 가중치를 조금씩 줄이는 설정(가중치 감쇠)이 학습 속도에도 영향을 줍니다'],
        eqtable([('∇f = (1/r) ∂f/∂θ e<sub>θ</sub>', '—', '카드 3/4 기울기 식의 θ 쪽 성분'), ('Δθ = 학습률 × |∇f| ÷ r', '—', '한 걸음에 도는 각도 ∝ 1/r²')]),
        T('asst/E10', '식은 0편이랑 똑같았어요. 무서울 게 없었네요!')) + '</div>'
    h += daily('운동장 바깥 줄로 뛰면 같은 걸음으로도 한 바퀴가 오래 걸립니다.', '대시보드 3부 "학습 걸음" 현장에서 가중치 감쇠를 켜고 끄며 걸음 수를 비교합니다.', '대시보드에서는')
    h += talk(T('fly/E08', '길이를 5에서 10으로 바꾸고 "45°까지 걸음 수"를 봐. 몇 배야?'),
              T('robo/E09', '1/r²이니까 길이 두 배면 걸음 수 네 배! 바로 세어 드려요.'))
    h += lab(16, '실험 ⑯ 길이에 따른 학습 걸음', '가중치 길이와 학습률을 바꿔 보세요',
             '<svg id="r16svg" role="img" aria-label="원 위의 가중치와 한 걸음 각도, 45°까지 걸음 수 막대"></svg>',
             sl('r16r', '가중치 길이 r', 1, 12, 0.5, 5) + sl('r16lr', '학습률', 0.5, 2, 0.1, 1), 330)
    h += f"""<div class="ai"><b>AI 판단 코너 — 주판봇의 1초 답, 믿어도 될까?</b>
{T('robo/E16', '가중치가 길면 숫자가 크니까 학습도 더 빨리 되겠죠! 계산 끝!')}
<p>박사는 늘 이렇게 묻습니다. <b>"가정이 맞나? 숫자가 그럴듯한가?"</b> 출력이 방향에만 달린 모델이라면, 위 실험처럼 길이가 두 배일 때 한 걸음에 도는 각도는 <b>4분의 1</b>입니다. "숫자가 크면 빠르다"는 직감은 여기서 거꾸로입니다.</p>
{T('robo/E14', '숫자 크기 말고 어떤 자로 재는지부터 볼게요…')}
</div>"""
    h += '<div class="solve"><b>풀이</b> 원자료 카드 3/4 기울기 식에서 θ 쪽 성분에 붙은 1/r이 학습 속도를 정합니다. 각도로 한 걸음 도는 양은 거기에 다시 1/r이 붙어 1/r²이 됩니다.</div>'
    h += dr('같은 학습률이라도 가중치 길이에 따라 실제 학습 속도가 달라질 수 있습니다. 학습 설정을 읽을 때 "무엇의 크기에 대한 학습률인가"를 함께 보세요. 여기서는 출력이 방향에만 달린 경우로 단순하게 봤어요.')
    h += '<div class="limit"><b>이 방의 한계</b> 실제 최적화 방법(Adam 등)은 걸음 크기를 자동으로 조절해 이 효과가 다르게 나타납니다. 다음은 데이터를 늘이고 줄일 때 확률이 어떻게 바뀌는지입니다.</div>'
    h += quiz('출력이 방향에만 달린 모델에서 가중치 길이가 3배가 되면, 한 걸음에 도는 각도는?', [('a', '3배'), ('b', '1/3'), ('c', '1/9')], 'c', '맞아요. 1/r²이라 1/9입니다.', '기울기에 1/r, 도는 각도에 다시 1/r이 붙습니다.') + '</section>'

    # 방 17
    h += room_head(P, 17, '늘리면 묽어진다 — 생성 모델의 확률 고치기', ['원자료: 네 카드 맨 아래 dV', '방법: 새 밀도 = 옛 밀도 ÷ 늘어난 배수', '일상: 물감에 물 타기'])
    h += talk(T('moa/E09', '그림 만드는 AI가 "단순한 분포를 늘리고 비틀어 복잡하게 만든다"던데, 그럼 확률은 어떻게 돼요?'),
              T('asst/E07', '0편 방 B의 작은 상자요! 상자가 커진 만큼 확률은 묽어져요.'))
    h += '<div class="pair">' + whybox(
        '생성 모델 중 일부(흐름 모델)는 쉬운 분포를 여러 번 늘이고 비틀어 복잡한 데이터 분포를 만듭니다. 이때 "이 점이 나올 확률(밀도)"을 계속 알아야 합니다.',
        '0편 방 B와 1부 방 4에서 작은 상자의 실제 크기(dV)가 자리마다 다르다는 것을 봤습니다.',
        '전체 확률은 늘 1입니다. 상자가 2배로 늘어나면 그 안의 밀도는 1/2이 됩니다. 넓이가 4배면 1/4. 늘어난 배수(야코비안)로 나눠 줍니다.',
        '같은 양의 물감을 두 배 넓은 종이에 펴면 색이 절반으로 옅어집니다.') + mathbox(
        T('sia/E09', '0~1에 고르게 퍼진 확률을 두 배로 늘리면요?'),
        '0~1에서 높이 1이면 넓이(확률 합)가 1입니다. 0~2로 늘리면 넓이 1을 유지하려고 높이가 0.5가 됩니다.',
        '직사각형의 넓이, 비례',
        ['0~1, 높이 1 → 넓이 <b>1</b>', '2배로 늘려 0~2 → 높이 <b>0.5</b> (넓이는 여전히 1)', '가로·세로 모두 2배(넓이 4배) → 높이 <b>1/4</b>', '0편 방 B: 지구본 자 상자 r² sinθ도 같은 "늘어난 배수"'],
        eqtable([('p<sub>새</sub>(z) = p<sub>옛</sub>(x) ÷ |dz/dx|', '—', '늘어난 배수로 나누기'), ('dV = h₁h₂h₃ dq₁dq₂dq₃', '—', '자리마다 다른 늘어난 배수(카드 4/4)')]),
        T('asst/E10', '확률도 dV를 챙겨야 하는구나. 0편이 여기까지 이어질 줄 몰랐어요.')) + '</div>'
    h += daily('풍선에 점을 찍고 불면 점 사이가 벌어지고 색이 옅어집니다.', '2부 방 10의 "전체 합은 그대로"와 같은 생각입니다.', '2부와 비교하면')
    h += talk(T('fly/E08', '늘림 슬라이더를 0.5까지 줄여 봐. 줄이면 밀도는?'),
              T('robo/E09', '넓이는 늘 1이 되게 높이를 맞춰 그릴게요!'))
    h += lab(17, '실험 ⑰ 늘리면 묽어진다', '늘림 배수를 바꾸고 1축/2축을 골라 보세요',
             '<svg id="r17svg" role="img" aria-label="늘어난 상자와 밀도 높이, 넓이는 1"></svg>',
             sl('r17s', '늘림 배수', 0.5, 3, 0.1, 2), 300,
             '<div class="btns" role="group" aria-label="축 수"><button class="btn" id="r17one" aria-pressed="true">1축(선)</button><button class="btn" id="r17two" aria-pressed="false">2축(넓이)</button></div>')
    h += '<div class="solve"><b>풀이</b> 확률 총합 1을 지키려면, 공간이 늘어난 만큼 밀도를 나눠야 합니다. 그 "늘어난 배수"가 원자료 카드의 dV에 들어 있는 h₁h₂h₃입니다.</div>'
    h += dr('생성 모델이 "이 그림이 나올 확률"을 계산할 때도, 비틀고 늘인 만큼을 꼭 고쳐 줍니다. 결과 확률이 1을 넘거나 합이 맞지 않으면 이 단계부터 의심하세요.')
    h += '<div class="limit"><b>이 방의 한계</b> 여기서는 고르게 늘리기만 봤습니다. 실제 흐름 모델은 자리마다 다르게 늘이고 비틀어, 자리마다 다른 배수를 계산합니다. 마지막 방은 이웃과 섞는 AI입니다.</div>'
    h += quiz('넓이가 3배로 늘어나면 밀도는?', [('a', '3배'), ('b', '1/3'), ('c', '그대로')], 'b', '맞아요. 총합 1을 지키려면 1/3입니다.', '같은 양을 세 배 넓은 곳에 펴면?') + '</section>'

    # 방 18
    h += room_head(P, 18, '이웃 평균으로 다듬기(GNN) — 관계망 위의 라플라시안', ['원자료: 네 카드의 SCALAR LAPLACIAN 줄', '방법: 새 값 = 내 값 + α(이웃 평균 − 내 값)', '일상: 친구 추천'])
    h += talk(T('sia/E19', '친구 추천 AI는 내 친구들의 정보를 섞는다던데, 2부 집값 섞기랑 같아요?'),
              T('asst/E16', '똑같아요! 바둑판 대신 친구 관계망 위에서 이웃 평균과 섞는 거예요.'))
    h += '<div class="pair">' + whybox(
        '사람·논문·상품처럼 서로 이어진 데이터(관계망)에서 각 점의 특징을 더 잘 알고 싶습니다. 이웃은 서로 닮는 경향이 있습니다.',
        '1부 방 7은 차이를 찾았고, 2부 방 11은 바둑판 지도에서 섞었습니다.',
        '관계망에서 연결된 이웃의 평균과 섞습니다(그래프 신경망, GNN의 기본 생각). 한두 번 섞으면 이웃 정보가 들어오고, 너무 많이 섞으면 모두 같아져 특징이 사라집니다.',
        '친구들 취향을 조금 참고하면 내 취향 추천이 좋아지지만, 다 따라가면 내 취향이 없어집니다.') + mathbox(
        T('moa/E09', '내 값 5, 이웃 셋이 모두 3이면 한 번 섞은 뒤엔요?'),
        '이웃 평균 3과의 차이 −2의 절반(α = 0.5)만큼 움직입니다. 2부 방 11과 같은 계산입니다.',
        '평균, 일차식, 수열',
        ['이웃 평균 3 − 내 값 5 = <b>−2</b>', 'α = 0.5 → 5 + 0.5 × (−2) = <b>4</b>', '여러 번 섞으면 모든 점이 비슷한 값으로 — <b>지나친 섞임</b>', '그래서 보통 두세 번만 섞습니다'],
        eqtable([('x ← x + α(이웃 평균 − x)', '—', '한 번 섞기(관계망 라플라시안)'), ('L = D − A', '—', '관계망 라플라시안(연결 수 − 연결표), 원어는 접기')]),
        T('asst/E10', '사진 → 집값 → 관계망. 같은 라플라시안이 세 번 나왔어요!')) + '</div>'
    h += daily('동아리 친구들 의견을 듣고 내 생각을 조금 고치는 것과 같습니다.', '대결로 갑니다. 이번에는 여러분이 심판입니다.', '다음은')
    h += talk(T('fly/E08', '"한 번 섞기"를 열 번 눌러 봐. 노드들이 어떻게 돼?'),
              T('robo/E09', '노드 값과 가장 큰 차이를 단계마다 세어 드릴게요!'))
    h += lab(18, '실험 ⑱ 관계망에서 섞기', '섞기를 진행하거나 속도를 바꿔 보세요',
             '<svg id="r18svg" role="img" aria-label="다섯 노드 관계망과 값"></svg>',
             sl('r18a', '섞는 속도 α', 0.1, 1, 0.1, 0.5), 320,
             '<div class="btns"><button class="btn" id="r18step">한 번 섞기</button><button class="btn" id="r18reset">처음으로</button></div>')
    h += '<div class="solve"><b>풀이</b> 관계망 위의 라플라시안은 "연결된 이웃 평균과 나의 차이"입니다. 섞을수록 차이는 줄고, 결국 모든 값이 같아집니다. 정보가 퍼지는 것과 사라지는 것은 같은 계산의 두 얼굴입니다.</div>'
    h += dr('GNN을 쓸 때는 "몇 번 섞을까"가 중요한 설정입니다. 결과 특징들이 지나치게 비슷해졌다면 섞는 횟수부터 확인하세요.')
    h += '<div class="limit"><b>이 방의 한계</b> 실제 GNN은 섞기 전에 특징을 바꾸는 학습 가능한 무게를 곱하고, 이웃마다 다른 무게를 주기도 합니다. 여기서는 평균 섞기만 봤어요.</div>'
    h += quiz('내 값 10, 이웃 평균 4, α = 0.5면 한 번 섞은 뒤 내 값은?', [('a', '7'), ('b', '4'), ('c', '14')], 'a', '맞아요. 10 + 0.5 × (4 − 10) = 7.', '이웃 평균과의 차이(−6)의 절반을 더해 보세요.') + '</section>'

    # 대결
    h += f"""
<section class="room" id="duel">
<div class="wing">대결</div>
<h2>박사 vs 하루 — 이 문제엔 어느 자?</h2>
<p>다섯 판입니다. 판마다 박사와 하루가 답합니다. 여러분이 맞는 쪽을 눌러 심판을 봐 주세요. 맞는 답은 늘 한쪽뿐입니다.</p>
{talk(T('doc/E09', '오늘은 제가 일부러 틀릴 수도 있어요. 심판은 독자 여러분입니다.'), T('asst/E20', '바, 박사님이랑 대결이라니… 그래도 배운 대로 할게요!'))}
{crowd('방청석', [('x1/E15', '(두근두근)'), ('x2/E04', '(…!)'), ('x3/E15', '(꼬옥)')])}
{duel()}
<div class="read" id="duelScore" aria-live="polite">판정을 시작해 주세요.</div>
</section>

<section class="room" id="summary">
<h2>정리 — 시리즈 전체를 한 장으로</h2>
<div class="scroll"><table class="sum"><thead><tr><th>원자료 카드의 개념</th><th>1부 생활</th><th>2부 경제·금융</th><th>3부 AI·머신러닝</th></tr></thead><tbody>
<tr><td>각도 자 φ</td><td>달력 시계판(방 2)</td><td>경기순환시계(방 8)</td><td>달력 시계 특성(방 13)</td></tr>
<tr><td>구 위의 방향</td><td>경도 1도(방 3)</td><td>상관을 각도로(방 12)</td><td>임베딩 코사인(방 14)</td></tr>
<tr><td>회전</td><td>환전 한 바퀴(방 6)</td><td>차익거래(방 9)</td><td>위치를 각도로(방 15)</td></tr>
<tr><td>기울기의 1/h</td><td>피자 테두리(방 1)</td><td>—</td><td>가중치 길이와 걸음(방 16)</td></tr>
<tr><td>작은 상자 dV</td><td>그린란드(방 4)</td><td>자금순환 전체 합(방 10)</td><td>늘리면 묽어진다(방 17)</td></tr>
<tr><td>라플라시안</td><td>사진 윤곽선(방 7)</td><td>집값 확산(방 11)</td><td>GNN 섞기(방 18)</td></tr>
</tbody></table></div>
</section>
<section id="outro"><h2>아웃트로</h2>
{talk(T('asst/E01', '대결도 이겼어요…! 첫날엔 땀만 흘렸는데, 이제 자를 고르는 게 재밌어요.'),
      T('doc/E16', '하루, 3대 2. 제가 일부러 틀린 두 판도 정확히 짚었어요. 이제 수업은 하루에게 맡겨도 되겠어요.'),
      T('sia/E12', '선배, 다음 시리즈도 선배가 해 주세요!'),
      T('moa/E01', '세 부의 표를 다 모으니까 원자료 카드 네 장이 한눈에 보여요.'),
      T('fly/E01', '그래도 숫자는 끝까지 확인. 그게 이 연구실의 규칙이야.'),
      T('robo/E12', '저도 이제 1초 답 전에 자부터 확인합니다!'))}
{crowd('방청석', [('x1/E01', '(짝짝짝)'), ('x2/E16', '(끄덕끄덕)'), ('x3/E01', '(반짝반짝)')])}
<a class="dashlink" href="dash_03.html"><b>3부 복습 대시보드 — AI 실험실 →</b><br>판매 예측·단어 나침반·학습 걸음·확률과 관계망 네 현장을 직접 운영하며 여섯 방을 복습합니다. 미션 12개.</a>
<div class="nextp"><a href="02_economy.html"><b>← 앞</b>2부 경제·금융</a><a href="index.html"><b>목차</b>벡터 분석 랩</a></div>
</section>
"""
    h += tail_sections([('room-13', '주기 특성(cos·sin) · 방 13'), ('room-14', '임베딩·코사인 유사도 · 방 14'), ('room-15', '회전 위치 부호화(RoPE) · 방 15'),
                        ('room-16', '기울기의 1/r · 방 16'), ('room-16', '가중치 길이와 학습 속도 · 방 16'), ('room-17', '흐름 모델·야코비안 · 방 17'),
                        ('room-18', '그래프 라플라시안·GNN · 방 18'), ('room-18', '지나친 섞임 · 방 18'), ('duel', '좌표계 고르기 · 대결')],
                       '원자료: @eeanimation 「Vector Analysis」 인포그래픽 4장. 수치는 교육용 예시입니다. AI 방법들은 학술 주장 없이 널리 알려진 생각을 쉽게 옮긴 것입니다. 캐릭터: 연구실 식구(fruitfly-lab-expressions). 표지는 픽셀아트 표지를 받기 전까지 쓰는 임시 그림입니다.')
    return h

PAGE_JS = r"""
// ---- 방 13 ----
{const s=$('r13svg');let mode='c';
 const solve=(X,y)=>{const n=X[0].length,A=Array.from({length:n},()=>Array(n+1).fill(0));X.forEach((r,i)=>{for(let a=0;a<n;a++){for(let b=0;b<n;b++)A[a][b]+=r[a]*r[b];A[a][n]+=r[a]*y[i]}});
  for(let c=0;c<n;c++){let p=c;for(let r=c+1;r<n;r++)if(Math.abs(A[r][c])>Math.abs(A[p][c]))p=r;[A[c],A[p]]=[A[p],A[c]];for(let r=0;r<n;r++)if(r!==c){const f=A[r][c]/A[c][c];for(let k=c;k<=n;k++)A[r][k]-=f*A[c][k]}}return A.map((r,i)=>r[n]/r[i])};
 window.fit13=(amp,pk,md)=>{const m=[...Array(12)].map((_,i)=>i+1),y=m.map(v=>100+amp*Math.cos(2*Math.PI*(v-pk)/12));
  const X=m.map(v=>md==='n'?[1,v]:[1,Math.cos(2*Math.PI*(v-1)/12),Math.sin(2*Math.PI*(v-1)/12)]);const b=solve(X,y);const p=X.map(r=>r.reduce((s,x,i)=>s+x*b[i],0));
  const rm=Math.sqrt(p.reduce((s,v,i)=>s+(v-y[i])**2,0)/12);return{y,p,rm,b}};
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const amp=+$('r13amp').value,pk=+$('r13pk').value;const A=fit13(amp,pk,mode),B=fit13(amp,pk,mode==='n'?'c':'n');
  const x0=40,x1=W-10,y0=14,y1=H-28,bw=(x1-x0)/12,Y=v=>y1-v/190*(y1-y0);let g=`<line x1="${x0}" y1="${y1}" x2="${x1}" y2="${y1}" stroke="#1c2230"/>`;
  A.y.forEach((v,i)=>{g+=`<rect x="${x0+i*bw+3}" y="${Y(v)}" width="${bw-6}" height="${y1-Y(v)}" fill="#c9ddeb" rx="3"/><text x="${x0+i*bw+bw/2}" y="${y1+16}" font-size="11" text-anchor="middle">${i+1}월</text>`});
  const pl=(p,c,d)=>`<polyline points="${p.map((v,i)=>[x0+i*bw+bw/2,Y(v)].join(',')).join(' ')}" fill="none" stroke="${c}" stroke-width="3" ${d?'stroke-dasharray="6 4"':''}/>`;
  g+=pl(B.p,'#9aa3b0',true)+pl(A.p,mode==='n'?'#c0392b':'#1e8a4c');s.innerHTML=g;
  const nn=mode==='n'?A:B,cc=mode==='n'?B:A;
  $('r13read').innerHTML=`지금 고른 모델: <b>${mode==='n'?'숫자 특성':'시계 특성'}</b> (실선) · 평균 오차 <b>${A.rm.toFixed(1)}</b><br>숫자 특성 평균 오차 ${nn.rm.toFixed(1)} · 시계 특성 평균 오차 ${cc.rm.toFixed(1)} · 12월 예측: 숫자 ${nn.p[11].toFixed(1)}, 시계 ${cc.p[11].toFixed(1)} (실제 ${A.y[11].toFixed(1)})`};
 const set=m=>{mode=m;$('r13n').setAttribute('aria-pressed',m==='n');$('r13c').setAttribute('aria-pressed',m==='c');draw()};$('r13n').onclick=()=>set('n');$('r13c').onclick=()=>set('c');
 bindSl('r13amp',v=>v,draw)();bindSl('r13pk',v=>v+'월',draw)();obs(s,draw)}
// ---- 방 14 ----
{const s=$('r14svg');const a0=Math.atan2(4,3);
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const d=+$('r14a').value*D2R,L=+$('r14l').value,A=[3,4],B=[L*Math.cos(a0+d),L*Math.sin(a0+d)];
  const cx=W*0.36,cy=H*0.7,k=Math.min(W/24,H/14);let g=`<circle cx="${cx}" cy="${cy}" r="${k*5}" fill="none" stroke="#c9ced6" stroke-dasharray="4 4"/><text x="${cx+k*5*0.72+4}" y="${cy+k*5*0.72+12}" font-size="11" fill="#5d6676">길이 5 원</text>`;
  g+=`<line x1="${cx-12*k}" y1="${cy}" x2="${cx+12*k}" y2="${cy}" stroke="#eef1f4"/><line x1="${cx}" y1="${cy-12*k}" x2="${cx}" y2="${cy+12*k}" stroke="#eef1f4"/>`;
  const ar=(v,c,l)=>`<line x1="${cx}" y1="${cy}" x2="${cx+v[0]*k}" y2="${cy-v[1]*k}" stroke="${c}" stroke-width="4"/><circle cx="${cx+v[0]*k}" cy="${cy-v[1]*k}" r="6" fill="${c}"/><text x="${cx+v[0]*k+8}" y="${cy-v[1]*k-6}" font-size="13" font-weight="700" fill="${c}">${l}</text>`;
  g+=`<line x1="${cx+A[0]*k}" y1="${cy-A[1]*k}" x2="${cx+B[0]*k}" y2="${cy-B[1]*k}" stroke="#7a3fd6" stroke-width="2" stroke-dasharray="5 4"/>`+ar(A,'#d4691f','A (3, 4)')+ar(B,'#1f7a8c',`B (${B[0].toFixed(1)}, ${B[1].toFixed(1)})`);s.innerHTML=g;
  const dot=A[0]*B[0]+A[1]*B[1],cs=dot/(5*L),dist=Math.hypot(A[0]-B[0],A[1]-B[1]);
  $('r14read').innerHTML=`겹침 점수 ${dot.toFixed(1)} ÷ (5 × ${L}) = 코사인 <b>${cs.toFixed(3)}</b> · 두 끝 사이 거리 <b>${dist.toFixed(2)}</b> (보라 점선)<br>${cs>0.95?'방향이 거의 같습니다 — 비슷한 뜻':cs>0.3?'조금 비슷한 방향':cs>-0.3?'거의 직각 — 서로 관계없음':'반대 방향'}`};
 bindSl('r14a',v=>v+'°',draw)();bindSl('r14l',v=>v.toFixed(1),draw)();obs(s,draw)}
// ---- 방 15 ----
{const s=$('r15svg');
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const i=+$('r15i').value,j=+$('r15j').value,a=i*30*D2R,b=j*30*D2R,dot=Math.cos(b-a);
  const cx=W*0.4,cy=H*0.5,R=Math.min(W,H)*0.36;let g=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#c9ced6"/>`;
  for(let m=0;m<12;m++){const t=m*30*D2R;g+=`<text x="${cx+(R+16)*Math.cos(t)}" y="${cy-(R+16)*Math.sin(t)+4}" font-size="11" text-anchor="middle" fill="#5d6676">${m}</text>`}
  const ar=(t,c,l)=>`<line x1="${cx}" y1="${cy}" x2="${cx+R*Math.cos(t)}" y2="${cy-R*Math.sin(t)}" stroke="${c}" stroke-width="5"/><text x="${cx+R*0.6*Math.cos(t)+6}" y="${cy-R*0.6*Math.sin(t)-6}" font-size="13" font-weight="700" fill="${c}">${l}</text>`;
  g+=ar(a,'#d4691f','단어 1')+ar(b,'#1f7a8c','단어 2');
  const tx=W*0.78;g+=`<text x="${tx}" y="30" font-size="12" font-weight="700" text-anchor="middle">자리 차이 → 겹침</text>`;for(let d=0;d<=6;d++)g+=`<text x="${tx}" y="${52+d*20}" font-size="12" text-anchor="middle" fill="${d===Math.abs(j-i)%12||d===12-Math.abs(j-i)?'#c0392b':'#1c2230'}">${d}자리 → ${Math.cos(d*30*D2R).toFixed(2)}</text>`;
  s.innerHTML=g;$('r15read').innerHTML=`단어 1: ${i}번 자리 → ${i*30}° · 단어 2: ${j}번 자리 → ${j*30}° · 각도 차이 ${((j-i)*30)}° → 겹침 점수 cos = <b>${dot.toFixed(3)}</b><br>자리 차이 ${j-i}만 같으면 어디에 있어도 같은 점수입니다`};
 $('r15both').onclick=()=>{['r15i','r15j'].forEach(id=>{const e=$(id);e.value=Math.min(11,+e.value+1);e.dispatchEvent(new Event('input'))})};
 bindSl('r15i',v=>v+'번',draw)();bindSl('r15j',v=>v+'번',draw)();obs(s,draw)}
// ---- 방 16 ----
{const s=$('r16svg');
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const r=+$('r16r').value,lr=+$('r16lr').value,gr=1/r,dth=lr*gr/r,n=Math.ceil(0.7854/dth);
  const cx=W*0.33,cy=H*0.55,k=Math.min(W*0.3,H*0.42)/12;let g=`<circle cx="${cx}" cy="${cy}" r="${r*k}" fill="none" stroke="#24345c" stroke-width="2"/><circle cx="${cx}" cy="${cy}" r="${5*k}" fill="none" stroke="#c9ced6" stroke-dasharray="3 4"/>`;
  const t0=40*D2R,t1=t0+dth;g+=`<line x1="${cx}" y1="${cy}" x2="${cx+r*k*Math.cos(t0)}" y2="${cy-r*k*Math.sin(t0)}" stroke="#d4691f" stroke-width="4"/><line x1="${cx}" y1="${cy}" x2="${cx+r*k*Math.cos(t1)}" y2="${cy-r*k*Math.sin(t1)}" stroke="#1f7a8c" stroke-width="3" stroke-dasharray="5 3"/>`;
  g+=`<text x="${cx}" y="${H-10}" font-size="12" text-anchor="middle" fill="#5d6676">주황 = 지금 가중치, 청록 점선 = 한 걸음 뒤</text>`;
  const bx=W*0.66,bw=W*0.28,by=30,bh=H-80,mx=200;g+=`<text x="${bx+bw/2}" y="${by-10}" font-size="12" font-weight="700" text-anchor="middle">45°까지 걸음 수</text>`;
  [[5,'길이 5'],[r,'지금'],[10,'길이 10']].forEach(([rr,l],i)=>{const nn=Math.ceil(0.7854/(lr/rr/rr)),hh=Math.min(nn,mx)/mx*bh,x=bx+i*bw/3;g+=`<rect x="${x+6}" y="${by+bh-hh}" width="${bw/3-12}" height="${hh}" fill="${i===1?'#c0392b':'#9aa3b0'}" rx="3"/><text x="${x+bw/6}" y="${by+bh-hh-4}" font-size="12" font-weight="700" text-anchor="middle">${nn}</text><text x="${x+bw/6}" y="${by+bh+16}" font-size="11" text-anchor="middle">${l}</text>`});
  s.innerHTML=g;$('r16read').innerHTML=`길이 r = <b>${r}</b> · 기울기 크기 1/r = <b>${gr.toFixed(3)}</b> · 한 걸음 각도 = ${lr} × ${gr.toFixed(3)} ÷ ${r} = <b>${dth.toFixed(4)} rad (${(dth*R2D).toFixed(2)}°)</b> · 45°까지 약 <b>${n}걸음</b>`};
 bindSl('r16r',v=>v.toFixed(1),draw)();bindSl('r16lr',v=>v.toFixed(1),draw)();obs(s,draw)}
// ---- 방 17 ----
{const s=$('r17svg');let two=false;const set=t=>{two=t;$('r17one').setAttribute('aria-pressed',!t);$('r17two').setAttribute('aria-pressed',t);draw()};$('r17one').onclick=()=>set(false);$('r17two').onclick=()=>set(true);
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const sc=+$('r17s').value,dens=two?1/(sc*sc):1/sc;const x0=40,base=H-40,u=Math.min((W-80)/3.2,(H-80)/2.2);let g=`<line x1="${x0-10}" y1="${base}" x2="${W-10}" y2="${base}" stroke="#1c2230"/>`;
  if(!two){g+=`<rect x="${x0}" y="${base-u}" width="${u}" height="${u}" fill="none" stroke="#9aa3b0" stroke-dasharray="5 4"/><text x="${x0+u/2}" y="${base-u-6}" font-size="11" text-anchor="middle" fill="#5d6676">처음: 폭 1, 높이 1</text>`;
   g+=`<rect x="${x0}" y="${base-u*dens}" width="${u*sc}" height="${u*dens}" fill="#1f7a8c" opacity=".6"/><text x="${x0+u*sc/2}" y="${base-u*dens-8}" font-size="13" font-weight="700" text-anchor="middle" fill="#1f7a8c">높이 ${dens.toFixed(3)}</text>`;
   [0,1,2,3].forEach(v=>g+=`<text x="${x0+v*u}" y="${base+16}" font-size="11" text-anchor="middle">${v}</text>`)}
  else{const cs=u*0.55,ox=x0,oy=base;g+=`<rect x="${ox}" y="${oy-cs}" width="${cs}" height="${cs}" fill="none" stroke="#9aa3b0" stroke-dasharray="5 4"/>`;const c=Math.round(255-200*Math.min(1,dens));
   g+=`<rect x="${ox}" y="${oy-cs*sc}" width="${cs*sc}" height="${cs*sc}" fill="rgb(${c},${Math.round(c*0.9+20)},${Math.round(c*0.5+120)})" stroke="#1f7a8c" stroke-width="2" opacity=".85"/><text x="${ox+cs*sc/2}" y="${oy-cs*sc/2}" font-size="14" font-weight="700" text-anchor="middle" fill="#1c2230">밀도 ${dens.toFixed(3)}</text>`}
  s.innerHTML=g;$('r17read').innerHTML=`${two?'가로·세로 모두':'가로로'} <b>${sc}배</b> 늘림 → 늘어난 배수 ${two?(sc*sc).toFixed(2):sc} → 밀도 <b>${dens.toFixed(3)}</b> · 전체 확률 = ${two?`${(sc*sc).toFixed(2)} × ${dens.toFixed(3)}`:`${sc} × ${dens.toFixed(3)}`} = <b>1</b>`};
 bindSl('r17s',v=>v.toFixed(1)+'배',draw)();obs(s,draw)}
// ---- 방 18 ----
{const s=$('r18svg');const E=[[0,1],[0,2],[0,3],[1,4]],POS=[[0.5,0.5],[0.22,0.25],[0.78,0.25],[0.5,0.85],[0.1,0.62]];let V,st;const init=()=>{V=[5,3,3,3,9];st=0};init();
 const nb=i=>E.filter(e=>e.includes(i)).map(e=>e[0]===i?e[1]:e[0]);
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;let g='';E.forEach(([a,b])=>g+=`<line x1="${POS[a][0]*W}" y1="${POS[a][1]*H}" x2="${POS[b][0]*W}" y2="${POS[b][1]*H}" stroke="#9aa3b0" stroke-width="4"/>`);
  V.forEach((v,i)=>{const t=Math.max(0,Math.min(1,(v-3)/6));g+=`<circle cx="${POS[i][0]*W}" cy="${POS[i][1]*H}" r="28" fill="rgb(${Math.round(36+t*176)},${Math.round(52+t*53)},${Math.round(92-t*61)})"/><text x="${POS[i][0]*W}" y="${POS[i][1]*H+5}" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">${v.toFixed(2)}</text><text x="${POS[i][0]*W}" y="${POS[i][1]*H-34}" font-size="11" text-anchor="middle">${i===0?'나':'이웃 '+i}</text>`});
  s.innerHTML=g;const sp=Math.max(...V)-Math.min(...V);$('r18read').innerHTML=`${st}번 섞음 · 내 값 <b>${V[0].toFixed(2)}</b> (이웃 평균 ${(nb(0).reduce((p,q)=>p+V[q],0)/3).toFixed(2)}) · 가장 큰 차이 <b>${sp.toFixed(2)}</b>${sp<0.3?' — <span class="bad">지나친 섞임: 거의 다 같아졌습니다.</span>':''}`};
 $('r18step').onclick=()=>{const a=+$('r18a').value;const L=V.map((v,i)=>{const n=nb(i);return n.reduce((p,q)=>p+V[q],0)/n.length-v});V=V.map((v,i)=>v+a*L[i]);st++;draw()};
 $('r18reset').onclick=()=>{init();draw()};bindSl('r18a',v=>v.toFixed(1),draw)();obs(s,draw)}
// ---- 대결 ----
{let judged={},right=0;document.querySelectorAll('[id^=duel]').forEach(box=>{if(!box.dataset.win)return;const win=box.dataset.win,rd=box.querySelector('.read');
 box.querySelectorAll('[data-pick]').forEach(b=>b.addEventListener('click',()=>{box.querySelectorAll('[data-pick]').forEach(x=>x.classList.remove('right','wrong'));const ok=b.dataset.pick===win;b.classList.add(ok?'right':'wrong');
  rd.style.display='block';rd.innerHTML=(ok?'<span class="good">판정 정확!</span> ':'<span class="bad">다시 보세요.</span> ')+`이 판은 <b>${win==='doc'?'박사':'하루'}</b> 승. `+box.dataset.why;
  if(!(box.id in judged)){judged[box.id]=ok;}else judged[box.id]=judged[box.id]||ok;
  const n=Object.keys(judged).length,c=Object.values(judged).filter(Boolean).length;$('duelScore').innerHTML=n<5?`${n}판 판정 · 정확한 판정 ${c}개`:`다섯 판 모두 판정! 정확한 판정 ${c} / 5 · 결과 <b>하루 3 : 박사 2 — 하루 승</b>`}))})}
"""

PACK_DATA = {"page": "벡터 분석 랩 3부 — AI·머신러닝", "author": "안상선 ((주)M-Robo)",
             "url": "https://adminmrobo.github.io/vector_analysis_lab/03_ai_ml.html",
             "concepts": ["주기 특성", "임베딩", "코사인 유사도", "RoPE", "가중치 길이", "가중치 감쇠", "흐름 모델", "야코비안", "GNN", "그래프 라플라시안", "지나친 섞임"],
             "relations": [["주기 특성", "쓴다", "원통 자 각도"], ["코사인 유사도", "쓴다", "구 위의 방향"], ["RoPE", "쓴다", "회전"],
                           ["학습 속도", "비례", "1/r²"], ["흐름 모델 밀도", "나눈다", "늘어난 배수(dV)"], ["GNN", "쓴다", "그래프 라플라시안"]],
             "example_values": {"숫자 특성 RMSE": 41.5, "시계 특성 RMSE": 0, "cos((3,4),(4,3))": 0.96, "RoPE 두 자리 차이": 0.5, "r=5 걸음": 20, "r=10 걸음": 79, "늘림 2배 밀도": 0.5, "GNN 한 번": 4},
             "duel": "하루 3 : 박사 2",
             "cite": "안상선 (2026). 벡터 분석 랩 3부 — AI·머신러닝. https://adminmrobo.github.io/vector_analysis_lab/03_ai_ml.html"}

if __name__ == '__main__':
    import math
    assert math.ceil(0.7854 / (1 / 25)) == 20 and math.ceil(0.7854 / (1 / 100)) == 79
    assert abs(24 / 25 - 0.96) < 1e-9 and abs(math.cos(math.radians(60)) - 0.5) < 1e-9
    b = body()
    import re as _re
    b = b.replace('data-win="', 'data-why="" data-win="')
    for i, (_, _, _, _, why) in enumerate(DUEL):
        b = b.replace(f'<div class="lab" id="duel{i}" data-why=""', f'<div class="lab" id="duel{i}" data-why="{why}"')
    n = page('03_ai_ml.html', '벡터 분석 랩 3부 — 달력 특성·임베딩·RoPE·학습 걸음·흐름 모델·GNN',
             '원자료 카드 네 장의 각도·구면 방향·회전·1/r·dV·라플라시안이 AI 모델 안에서 하는 일. 마지막은 박사 vs 하루 "이 문제엔 어느 자?" 대결.',
             'assets/og/03.webp', b, PAGE_JS, PACK_DATA, ['주기 특성', '임베딩', 'RoPE', '학습 속도', '흐름 모델', 'GNN'])
    print('03 bytes', n)


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
