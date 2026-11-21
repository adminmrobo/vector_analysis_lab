# -*- coding: utf-8 -*-
"""0편 오리엔테이션 — 네 개의 자 소개"""
from common import *

FOOT_SRC = ('원자료: @eeanimation 「Vector Analysis」 인포그래픽 4장(1/4 직교좌표 · 2/4 원통좌표 · 3/4 구면좌표 · 4/4 일반 직교곡선좌표). '
            '원자료의 φ·ϕ 혼용을 이 페이지에서는 φ로, 1/4의 굵지 않은 A를 굵은 <b>A</b>로, 4/4의 ē<sub>i</sub>를 e<sub>i</sub>로 바꿉니다.')

def cast_cards():
    rows = [('sia/E13', '시아 (인턴1)', '직관파. 비유부터 꺼내며 하루에게 묻습니다.'),
            ('moa/E09', '모아 (인턴2)', '꼼꼼파. 조건과 예외, 숫자를 다시 묻습니다.'),
            ('asst/E20', '하루 (조수)', '오늘 처음으로 수업을 맡았습니다. 긴장했지만 끝까지 풀어 봅니다.'),
            ('fly/E08', '초파리 연구원', '하루를 돕는 의심 담당. "이걸 눌러 봐"로 실험을 권합니다.'),
            ('robo/E09', '주판봇', '하루를 돕는 계산 담당. 주판알로 숫자를 빨리 냅니다. 가끔 너무 빨라요.'),
            ('doc/E08', '박사', '방이 끝날 때마다 "박사의 정리"로 뜻을 묶어 줍니다.'),
            ('x1/E15', '미공개 X1·X2·X3', '방청석. 말 대신 소리로 하루를 걱정하고 응원합니다.')]
    h = '<div class="cast">'
    for k, n, d in rows:
        USED.append(k)
        h += f'<div><img data-k="{k}" alt="{n}"><span><b>{n}</b>{d}</span></div>'
    return h + '</div>'

def body():
    h = f"""
<header class="hero"><div class="wrap">
<div class="wing e">벡터 분석 랩 · 0편 오리엔테이션</div>
<h1>네 개의 자로 읽는 화살표<br>하루의 첫 수업</h1>
<p class="sub">같은 화살표도 어떤 자로 재느냐에 따라 숫자가 달라집니다. 가로·세로·높이 자, 원통 자, 지구본 자, 휜 격자 자. 원자료 카드 네 장을 조수 하루가 처음으로 설명합니다.</p>
<figure class="cover" style="margin-left:0;margin-right:0"><img src="assets/cover_00.webp" width="1600" height="900" alt="네 장의 좌표 카드 앞에서 설명을 시작하는 하루와 연구실 식구들 (임시 표지)"></figure>
<div class="by">{AUTHOR}</div>
<a class="cta" href="#room-e">입구 방부터 들어가기</a>
</div></header>

<main class="wrap">

<section>
<div class="three">
<h2>처음 오신 분께 — 이 페이지를 3줄로</h2>
<ol>
<li><b>무엇을:</b> 위치를 읽는 자(좌표) 네 가지와, 자마다 다른 "한 걸음의 실제 길이"를 봅니다.</li>
<li><b>왜 중요한가:</b> 둥근 물체, 지구, 시계처럼 도는 데이터는 맞는 자를 고르면 계산이 짧고 정확해집니다.</li>
<li><b>업무에서는:</b> 지도 거리, 환율, 사진, 판매 예측, AI의 단어 비교까지 이 요령 위에서 돌아갑니다(1~3부).</li>
</ol>
<p style="margin:0">코드·수식을 몰라도 됩니다. 식은 "몰라도 됩니다" 상자 안에만 있고, 나머지는 슬라이더를 움직이며 봅니다.</p>
<details><summary>이 페이지에 나오는 기호와 약어 풀이</summary>
<table><tbody>
<tr><td class="m">∇</td><td>나블라. "어느 쪽으로 얼마나 가파른가"를 재는 화살표 도구</td></tr>
<tr><td class="m">x, y, z</td><td>가로·세로·높이 자(직교좌표)</td></tr>
<tr><td class="m">ρ, φ, z</td><td>원통 자. 중심축에서 거리(로), 돌아간 각도(파이), 높이</td></tr>
<tr><td class="m">r, θ, φ</td><td>지구본 자(구면좌표). 중심에서 거리, 꼭대기에서 내려온 각도(세타), 돌아간 각도</td></tr>
<tr><td class="m">h</td><td>한 걸음의 실제 길이(축척 인자). 자의 눈금 하나가 실제로 몇 m인지</td></tr>
<tr><td class="m">dV</td><td>작은 상자의 실제 부피(부피 요소)</td></tr>
<tr><td>rad</td><td>라디안. 각도를 "반지름 몇 개만큼 돌았나"로 재는 단위. 180° = 3.14 rad</td></tr>
</tbody></table></details>
</div>
</section>

<section>
<h2>등장인물</h2>
{cast_cards()}
</section>

<section id="opening">
<h2>오늘의 장면 — 하루가 수업을 맡은 날</h2>
{talk(T('doc/E08', '오늘 네 장 카드 수업은 하루가 맡아요. 저는 방이 끝날 때마다 정리만 하겠습니다.'),
      T('asst/E20', '제, 제가요? 기울기·발산·회전 식이 카드마다 다 다르게 생겼는데요…'),
      T('sia/E19', '하루 선배 수업이라니 기대돼요! 모르는 건 바로바로 물어봐도 되죠?'))}
{crowd('방청석', [('x1/E15', '(조마조마)'), ('x2/E02', '(꿀꺽)'), ('x3/E04', '(…!)')])}
{talk(T('fly/E10', '걱정 마. 막히면 내가 "이걸 눌러 봐"로 실험을 열어 줄게.'),
      T('robo/E13', '계산은 제 주판에 맡기세요! 숫자는 1초면 나옵니다.'),
      T('moa/E12', '하루 선배, 힘내세요! 차도 준비해 뒀어요.'))}
<p>처음 보셔도 괜찮습니다. 하루도 오늘이 처음입니다. 여기서 한 번 멈춰도 괜찮아요.</p>
</section>

<section>
<h2>왜 이 페이지를 만들었나</h2>
<p>원자료 카드 네 장은 기울기·발산·회전·라플라시안을 좌표마다 나란히 적었습니다. 뜻은 같은데, 원통·지구본 자에서는 1/ρ, r² sinθ 같은 배율이 붙어 식 모양이 달라집니다.</p>
<p>그 배율은 하나의 질문에서 나옵니다. <b>"눈금 한 걸음이 실제로 얼마인가?"</b> 0편에서 이 질문을 손으로 잡고, 1부 생활 → 2부 경제·금융 → 3부 AI·머신러닝으로 같은 장면을 세 번 다시 봅니다.</p>
</section>

<section>
<h2>큰 그림 — 시리즈 지도</h2>
<div class="map">
<a class="e" href="#room-e"><b>0편 · 입구 방</b>자와 각도기가 있는 방<span class="why">점 사이 거리 = 피타고라스</span></a>
<a class="e" href="#room-a"><b>0편 · 방 A</b>네 개의 자<span class="why">자마다 한 걸음의 길이가 다르다</span></a>
<a class="e" href="#room-b"><b>0편 · 방 B</b>한 걸음 상자<span class="why">같은 0.1씩이라도 부피가 다르다</span></a>
<a class="f" href="01_everyday.html"><b>1부 생활</b>피자·지도·환전·사진<span class="why">쉬운 장면에서 먼저 느끼기</span></a>
</div>
<div class="easy" style="margin-top:16px"><b>30초 복습 — ∇ 네 형제</b> ① <b>기울기</b>: 가장 가파른 오르막 쪽 화살표 ② <b>발산</b>: 그 자리에서 솟아나는가(샘), 빨려 들어가는가(배수구) ③ <b>회전</b>: 한 바퀴 돌았을 때 남는 것이 있는가 ④ <b>라플라시안</b>: 내 값과 주변 평균의 차이. 자세히는 <a href="https://adminmrobo.github.io/vector_calculus_lab/01_differential.html">∇ 특별편 ①편</a>에 있습니다. 몰라도 이 페이지를 따라올 수 있어요.</div>
</section>
"""
    # ---------------- 입구 방 ----------------
    h += f"""
<section class="room" id="room-e">
<div class="wing e">입구 방</div>
<h2>자와 각도기가 있는 방 — 두 사람 사이의 거리</h2>
<div class="tags"><span>원자료: 카드 1/4 (가로·세로·높이 자)</span><span>방법: 피타고라스 정리</span><span>일상: 키와 몸무게</span></div>
{talk(T('sia/E09', '하루 선배, 저랑 모아는 얼마나 "닮았어요"? 숫자 하나로 말할 수 있어요?'),
      T('asst/E15', '어, 음… 키와 몸무게를 가로·세로 자로 놓으면… 될 것 같아요!'))}
<div class="pair">
<div class="box why"><h3>왜 이 방법을 쓰나</h3>
<p><b>문제:</b> 사람·상품·문장을 비교하려면 "얼마나 먼가"를 숫자 하나로 말해야 합니다.</p>
<p><b>해법:</b> 키를 가로 자, 몸무게를 세로 자로 놓으면 한 사람이 점 하나가 됩니다. 두 점 사이 거리가 "닮지 않은 정도"입니다.</p>
<p><b>이 자의 좋은 점:</b> 눈금 간격이 어디서나 같습니다. 한 걸음은 늘 1입니다(카드 1/4의 h₁ = h₂ = h₃ = 1).</p>
<div class="easy"><b>쉽게 말하면</b> 모눈종이 위 두 점을 자로 재는 일입니다.</div></div>
<div class="box math"><h3>시아·모아가 묻고, 하루가 풀어 봅니다</h3>
{T('moa/E09', '가로로 3, 세로로 4 떨어져 있으면 거리는 7이에요?')}
<p class="saywords"><b>말로 먼저:</b> 가로로 가고 세로로 가는 길은 직각삼각형의 두 변입니다. 바로 가는 길은 빗변이라 두 변의 합보다 짧습니다. 빗변의 제곱은 두 변 제곱의 합입니다.</p>
<p><b>학교 수학으로 보면:</b> 두 점 사이의 거리, 피타고라스 정리</p>
<div class="try"><b>숫자로 한 번 해 보기</b><ol><li>시아 (160 cm, 50 kg), 모아 (163 cm, 54 kg)</li><li>가로 차이 3, 세로 차이 4</li><li>거리 = √(3² + 4²) = √25 = <b>5</b> (7이 아니에요)</li></ol></div>
{eqtable([('d = √(Δx² + Δy²)', '디는 루트 델타 엑스 제곱 더하기 델타 와이 제곱', '두 점 사이 거리'), ('Δ', '델타', '두 값의 차이')])}
{T('asst/E10', '휴, 첫 문제는 맞혔어요. 바로 가면 5만큼이에요!')}
</div></div>
<div class="daily"><div><b>일상으로 치면</b>지도에서 골목길로 가면 7, 직선으로 가면 5입니다.</div><div><b>AI·머신러닝에서는</b>가장 가까운 이웃 찾기(KNN), 단어를 점으로 놓기(임베딩)가 모두 이 거리에서 출발합니다.</div></div>
{talk(T('fly/E08', '슬라이더로 모아 점을 옮겨서 거리가 0이 되는 곳을 찾아 봐.'),
      T('robo/E09', '차이를 제곱해서 더하고 루트! 주판으로 바로 계산해 드릴게요.'))}
<div class="lab"><div class="hd"><b>실험 ① 키·몸무게 방의 두 점</b><span>슬라이더로 모아의 점을 옮겨 보세요</span></div>
<div class="fig" style="min-height:330px"><svg id="resvg" role="img" aria-label="키와 몸무게 좌표평면 위 시아와 모아의 점, 직각삼각형"></svg></div>
<div class="ctl">
<div class="sl"><label for="reh">모아 키</label><input type="range" id="reh" min="150" max="175" step="1" value="163"><output id="reho"></output></div>
<div class="sl"><label for="rew">모아 몸무게</label><input type="range" id="rew" min="40" max="65" step="1" value="54"><output id="rewo"></output></div>
</div>
<div class="read" id="reread" aria-live="polite"></div></div>
<div class="solve"><b>풀이</b> 가로·세로 자는 눈금 한 걸음이 어디서나 1이라, 차이를 그대로 제곱해 더하면 됩니다. 원자료 카드 1/4의 식에 배율이 하나도 붙지 않은 까닭입니다.</div>
{dr('거리 5는 "두 사람이 키·몸무게로 보면 이만큼 다르다"는 뜻입니다. 단, 키(cm)와 몸무게(kg)는 단위가 달라요. 단위를 어떻게 맞추느냐에 따라 거리가 바뀝니다. 이 이야기는 3부에서 다시 만납니다.')}
<div class="limit"><b>이 방의 한계</b> 피자처럼 둥글거나 지구처럼 휜 것은 가로·세로 자로 적으면 식이 길어집니다. 둥근 것에는 둥근 자가 필요합니다. 방 A로 갑니다.</div>
{quiz('가로 차이 6, 세로 차이 8인 두 점의 거리는?', [('a', '14'), ('b', '10'), ('c', '48')], 'b', '맞아요. √(36 + 64) = √100 = 10.', '두 차이를 각각 제곱해서 더한 뒤 루트를 씌워 보세요.')}
</section>
"""
    # ---------------- 방 A ----------------
    h += f"""
<section class="room" id="room-a">
<div class="wing e">방 A</div>
<h2>네 개의 자 — 같은 점, 다른 숫자, 다른 한 걸음</h2>
<div class="tags"><span>원자료: 카드 1/4 · 2/4 · 3/4 · 4/4 위쪽 그림과 "scale factors" 줄</span><span>방법: 축척 인자 h</span><span>일상: 주소 읽는 법</span></div>
{talk(T('moa/E09', '카드 네 장 맨 위에 h가 다 달라요. 1, ρ, r sinθ… 이게 뭐예요?'),
      T('asst/E20', '그, 그게… 자 눈금 하나가 실제로 몇 m인지예요. 직접 보여 드릴게요!'))}
<div class="cardrow">
<div><b>카드 1/4 · 가로·세로·높이 자</b><span>(x, y, z) · h = 1, 1, 1</span></div>
<div><b>카드 2/4 · 원통 자</b><span>(ρ, φ, z) · h = 1, ρ, 1</span></div>
<div><b>카드 3/4 · 지구본 자</b><span>(r, θ, φ) · h = 1, r, r sinθ</span></div>
<div><b>카드 4/4 · 휜 격자 자(일반)</b><span>(q₁, q₂, q₃) · h₁, h₂, h₃</span></div>
</div>
<div class="pair">
<div class="box why"><h3>왜 이 방법을 쓰나</h3>
<p><b>문제:</b> 같은 점도 "동쪽 1, 북쪽 1, 위로 1.41"이라 할 수도 있고 "중심에서 2, 꼭대기에서 45°, 돌아서 45°"라 할 수도 있습니다.</p>
<p><b>앞 방의 한계:</b> 가로·세로 자는 둥근 것을 적기 불편합니다.</p>
<p><b>해법:</b> 모양에 맞는 자를 고르고, 자마다 "눈금 한 걸음이 실제로 얼마인지(h)"를 같이 적어 둡니다. 거리 쪽 눈금은 그대로 1이지만, 각도 쪽 눈금은 중심에서 멀수록 길어집니다.</p>
<div class="easy"><b>쉽게 말하면</b> 같은 집 주소를 도로명으로도, 위도·경도로도 쓸 수 있습니다. 다만 "1 바뀔 때 몇 m"는 주소 방식마다 다릅니다.</div></div>
<div class="box math"><h3>시아·모아가 묻고, 하루가 풀어 봅니다</h3>
{T('sia/E09', '각도를 0.3 돌리면 0.3 m 움직이는 거 아니에요?')}
<p class="saywords"><b>말로 먼저:</b> 각도는 "얼마나 돌았나"이지 "얼마나 갔나"가 아닙니다. 중심에서 멀리 있을수록 같은 각도에 더 많이 갑니다. 그래서 각도 쪽 한 걸음에는 "중심에서 거리"가 배율로 붙습니다.</p>
<p><b>학교 수학으로 보면:</b> 부채꼴 호의 길이 = 반지름 × 각도(rad), 공간좌표, 삼각함수</p>
<div class="try"><b>숫자로 한 번 해 보기</b> 점 (1, 1, 1.41)에서 눈금 0.3씩 움직이면<ol><li>가로·세로·높이 자: 0.3, 0.3, 0.3 m</li><li>원통 자: ρ = 1.41이라 0.3, <b>1.41 × 0.3 = 0.42</b>, 0.3 m</li><li>지구본 자: r = 2, θ = 45°라 0.3, <b>2 × 0.3 = 0.6</b>, <b>2 × sin45° × 0.3 = 0.42</b> m</li></ol></div>
{eqtable([('hᵢ = |∂r/∂qᵢ|', '에이치 아이', '눈금 qᵢ를 조금 바꿀 때 실제 위치가 움직이는 길이의 배율(카드 4/4 맨 위)'),
          ('ρ = √(x² + y²)', '로', '높이 축에서 떨어진 거리'), ('r = √(x² + y² + z²)', '알', '중심에서 떨어진 거리'),
          ('θ', '세타', '꼭대기(z축)에서 내려온 각도'), ('φ', '파이', '바닥에서 돌아간 각도')])}
{T('asst/E10', '같은 0.3인데 0.3, 0.42, 0.6… 자마다 한 걸음이 달라요!')}
</div></div>
<div class="daily"><div><b>일상으로 치면</b>회전목마 바깥 말은 같은 각도를 돌아도 안쪽 말보다 더 멀리 달립니다.</div><div><b>AI·머신러닝에서는</b>단어·사진을 점으로 놓을 때도 "방향(각도)"과 "길이"를 나눠 읽는 경우가 많습니다(3부 방 14·16).</div></div>
{talk(T('fly/E08', '자 버튼을 바꿔 가며 화살표 세 개의 길이를 봐. 점도 옮겨 봐.'),
      T('robo/E16', '각도 쪽 화살표 길이는 제가 계산해서 바로 띄울게요!'))}
<div class="lab"><div class="hd"><b>실험 ② 같은 점, 세 가지 자로 읽기</b><span>카드 4/4는 이 셋을 묶은 일반형 · 화살표 = 눈금 0.3 한 걸음의 실제 길이</span></div>
<div class="btns" role="group" aria-label="자 고르기"><button class="btn" id="raC" aria-pressed="true">가로·세로·높이</button><button class="btn" id="raY" aria-pressed="false">원통</button><button class="btn" id="raS" aria-pressed="false">지구본</button></div>
<div class="fig" style="min-height:380px"><svg id="rasvg" role="img" aria-label="공간좌표 위의 점과 고른 자의 세 방향 한 걸음 화살표"></svg></div>
<div class="ctl">
<div class="sl"><label for="rax">x (동쪽)</label><input type="range" id="rax" min="0.2" max="2" step="0.01" value="1"><output id="raxo"></output></div>
<div class="sl"><label for="ray">y (북쪽)</label><input type="range" id="ray" min="0.2" max="2" step="0.01" value="1"><output id="rayo"></output></div>
<div class="sl"><label for="raz">z (높이)</label><input type="range" id="raz" min="0" max="2" step="0.01" value="1.41"><output id="razo"></output></div>
</div>
<div class="read" id="raread" aria-live="polite"></div></div>
<div class="ai"><b>AI 판단 코너 — 주판봇의 1초 답, 믿어도 될까?</b>
{T('robo/E16', '지구본 자에서 φ를 0.3 돌렸어요. 움직인 거리는 0.3 × r = 0.6 m! 계산 끝!')}
<p>박사는 늘 이렇게 묻습니다. <b>"가정이 맞나? 숫자가 그럴듯한가?"</b> φ는 바닥에서 도는 각도라, 도는 원의 반지름은 r이 아니라 높이 축에서의 거리 r sinθ입니다. 점 (1, 1, 1.41)에서는 2 × sin45° × 0.3 = <b>0.42 m</b>가 맞습니다. 위 실험에서 지구본 자를 누르고 φ 쪽 화살표 숫자를 직접 확인해 보세요.</p>
{T('robo/E14', '앗, 꼭대기 쪽으로 갈수록 도는 원이 작아지는구나… 다시 계산했어요!')}
</div>
<div class="solve"><b>풀이</b> 원자료 카드의 기울기 식에서 1/ρ, 1/r, 1/(r sinθ)가 붙는 까닭이 이것입니다. 기울기는 "실제로 1 m 갈 때 얼마나 오르나"인데, 각도 눈금 한 걸음은 1 m가 아니라 h만큼이라 h로 나눠 줍니다. 카드 4/4의 기울기 식 ∑ eᵢ (1/hᵢ) ∂f/∂qᵢ가 네 장을 하나로 묶은 모양입니다.</div>
{dr('자는 모양에 맞춰 고르되, 한 걸음의 실제 길이 h를 꼭 같이 들고 다니세요. h만 알면 카드 2/4·3/4의 긴 식은 카드 4/4 한 줄에서 모두 나옵니다.')}
<div class="limit"><b>이 방의 한계</b> 꼭대기(θ = 0)나 높이 축 위(ρ = 0)에서는 각도 쪽 h가 0이 되어 방향을 말할 수 없습니다. 지구의 북극에서 "동쪽"이 없는 것과 같습니다. 그리고 걸음 길이가 다르면 "작은 상자의 부피"도 달라집니다. 방 B로 갑니다.</div>
{quiz('원통 자에서 높이 축에서 3 m 떨어진 점의 φ를 0.2 rad 돌리면 실제로 몇 m 움직일까요?', [('a', '0.2 m'), ('b', '0.6 m'), ('c', '3.2 m')], 'b', '맞아요. h = ρ = 3이라 3 × 0.2 = 0.6 m.', '각도 쪽 한 걸음에는 중심축에서의 거리 ρ가 곱해집니다. 3 × 0.2를 계산해 보세요.')}
</section>
"""
    # ---------------- 방 B ----------------
    h += f"""
<section class="room" id="room-b">
<div class="wing e">방 B</div>
<h2>한 걸음 상자 — 같은 0.1씩이라도 부피가 다르다</h2>
<div class="tags"><span>원자료: 네 카드 맨 아래 dV 줄</span><span>방법: 부피 요소 dV = h₁h₂h₃ dq₁dq₂dq₃</span><span>일상: 아파트 평면도</span></div>
{talk(T('moa/E04', '카드 맨 아래 dV도 다 달라요. dx dy dz, ρ dρ dφ dz, r² sinθ dr dθ dφ…'),
      T('asst/E09', '방 A의 한 걸음 세 개를 곱한 거예요. …맞죠? 맞을 거예요!'))}
{crowd('방청석', [('x1/E15', '(두근두근)'), ('x2/E09', '(…)'), ('x3/E04', '(꼬옥)')])}
<div class="pair">
<div class="box why"><h3>왜 이 방법을 쓰나</h3>
<p><b>문제:</b> 넓이·부피·확률을 모두 더하려면, 눈금을 조금씩 나눈 작은 상자의 실제 크기를 알아야 합니다.</p>
<p><b>앞 방의 한계:</b> 한 걸음 길이가 방향마다, 자리마다 다르다는 것만 봤습니다.</p>
<p><b>해법:</b> 작은 상자의 세 변이 각각 h₁dq₁, h₂dq₂, h₃dq₃이므로 부피는 세 변의 곱입니다(카드 4/4 맨 아래).</p>
<div class="easy"><b>쉽게 말하면</b> 평면도의 눈금 개수만 곱하면 넓이가 안 나옵니다. 눈금 하나가 몇 m인지 바꿔서 곱해야 진짜 넓이가 나옵니다.</div></div>
<div class="box math"><h3>시아·모아가 묻고, 하루가 풀어 봅니다</h3>
{T('sia/E09', '그럼 지구본 자의 r² sinθ는 어디서 나와요?')}
<p class="saywords"><b>말로 먼저:</b> 지구본 자의 세 한 걸음은 1, r, r sinθ였습니다. 셋을 곱하면 r × r sinθ = r² sinθ입니다. 원통 자는 1 × ρ × 1 = ρ입니다. 외울 필요 없이 방 A의 h 세 개를 곱하면 됩니다.</p>
<p><b>학교 수학으로 보면:</b> 직육면체의 부피 = 가로 × 세로 × 높이</p>
<div class="try"><b>숫자로 한 번 해 보기</b> 점 (1, 1, 1.41)에서 눈금을 0.1씩 나누면<ol><li>가로·세로·높이 자: 0.1³ = <b>0.001</b></li><li>원통 자: ρ = 1.41 → 1.41 × 0.001 = <b>0.00141</b></li><li>지구본 자: r = 2, θ = 45° → 4 × 0.707 × 0.001 = <b>0.00283</b></li></ol></div>
{eqtable([('dV = h₁h₂h₃ dq₁dq₂dq₃', '디 브이', '작은 상자의 실제 부피(카드 4/4)'), ('ρ dρ dφ dz', '로 디로 디파이 디제트', '원통 자의 상자(카드 2/4)'), ('r² sinθ dr dθ dφ', '알 제곱 사인 세타 …', '지구본 자의 상자(카드 3/4)')])}
{T('asst/E19', '같은 "0.1씩"인데 지구본 자 상자가 세 배 가깝게 커요! 제가 맞혔어요!')}
</div></div>
<div class="daily"><div><b>일상으로 치면</b>지도에서 같은 "위도 1도 × 경도 1도" 땅도 적도와 북쪽 나라의 넓이가 다릅니다(1부 방 4).</div><div><b>AI·머신러닝에서는</b>데이터를 늘리거나 줄여 바꾸면 확률 밀도도 그만큼 고쳐야 합니다(3부 방 17).</div></div>
{talk(T('fly/E08', '거리 슬라이더와 각도 슬라이더를 끝까지 밀어 봐. 꼭대기에서는 상자가 어떻게 돼?'),
      T('robo/E09', '세 자의 상자 부피를 막대로 나란히 세워 드릴게요!'))}
<div class="lab"><div class="hd"><b>실험 ③ 한 걸음 상자 비교</b><span>눈금 0.1씩 나눈 작은 상자의 실제 부피</span></div>
<div class="fig" style="min-height:300px"><svg id="rbsvg" role="img" aria-label="세 가지 자의 작은 상자 부피 막대그래프"></svg></div>
<div class="ctl">
<div class="sl"><label for="rbr">중심에서 거리 r</label><input type="range" id="rbr" min="0.5" max="3" step="0.1" value="2"><output id="rbro"></output></div>
<div class="sl"><label for="rbt">꼭대기에서 각도 θ</label><input type="range" id="rbt" min="0" max="180" step="1" value="45"><output id="rbto"></output></div>
</div>
<div class="read" id="rbread" aria-live="polite"></div></div>
<div class="solve"><b>풀이</b> 가로·세로·높이 자의 상자는 어디서나 0.001로 같습니다. 원통·지구본 자의 상자는 중심에서 멀수록 커지고, 꼭대기(θ = 0°, 180°)에서는 0이 됩니다. 그래서 둥근 것의 부피·확률을 더할 때 ρ나 r² sinθ를 곱해 줍니다.</div>
{dr('dV는 "눈금으로 센 크기"를 "실제 크기"로 바꾸는 환율입니다. 1부에서는 지도 넓이로, 3부에서는 AI가 확률을 고치는 계산으로 다시 만납니다. 오늘 하루 선배, 두 방을 잘 넘겼어요.')}
<div class="limit"><b>이 방의 한계</b> 원자료 카드는 자의 눈금선이 서로 직각인 경우(직교)만 다룹니다. 눈금선이 비스듬한 자는 상자가 기울어져 곱셈만으로는 부피가 나오지 않습니다. 이 시리즈도 직각인 자만 씁니다.</div>
{quiz('원통 자에서 중심축에서 2 m인 곳의 작은 상자(눈금 0.1씩) 부피는?', [('a', '0.001'), ('b', '0.002'), ('c', '0.2')], 'b', '맞아요. ρ = 2를 곱해 2 × 0.001 = 0.002.', '원통 자의 상자는 ρ × 0.1 × 0.1 × 0.1입니다.')}
</section>

<section class="room" id="fix">
<h2>원자료와 다르게 쓴 곳</h2>
<p>네 장의 공식은 모두 검산했고 계산이 틀린 곳은 없습니다. 기호만 아래처럼 맞춰 씁니다.</p>
<div class="scroll"><table><thead><tr><th>원자료</th><th>이 시리즈</th><th>이유</th></tr></thead><tbody>
<tr><td>카드 2/4·3/4의 φ와 ϕ 혼용</td><td>φ 하나로</td><td>같은 각도를 두 글자로 쓰면 다른 것으로 보입니다</td></tr>
<tr><td>카드 1/4의 ∇·A, ∇×A (A가 굵지 않음)</td><td>굵은 <b>A</b></td><td>화살표(벡터)는 모두 굵게 씁니다</td></tr>
<tr><td>카드 4/4 설명문 ē<sub>i</sub>, 공식 e<sub>i</sub></td><td>e<sub>i</sub></td><td>같은 단위 화살표입니다</td></tr>
</tbody></table></div>
</section>

<section id="summary">
<h2>정리 — 0편을 한 장으로</h2>
<div class="scroll"><table class="sum"><thead><tr><th>자</th><th>좌표</th><th>한 걸음의 실제 길이 h</th><th>작은 상자 dV</th></tr></thead><tbody>
<tr><td>가로·세로·높이 (1/4)</td><td>x, y, z</td><td>1, 1, 1</td><td>dx dy dz</td></tr>
<tr><td>원통 (2/4)</td><td>ρ, φ, z</td><td>1, ρ, 1</td><td>ρ dρ dφ dz</td></tr>
<tr><td>지구본 (3/4)</td><td>r, θ, φ</td><td>1, r, r sinθ</td><td>r² sinθ dr dθ dφ</td></tr>
<tr><td>휜 격자 (4/4)</td><td>q₁, q₂, q₃</td><td>h₁, h₂, h₃</td><td>h₁h₂h₃ dq₁dq₂dq₃</td></tr>
</tbody></table></div>
</section>

<section id="outro">
<h2>아웃트로</h2>
{talk(T('asst/E16', '끝까지 했어요! 자를 고르고 h만 챙기면 되는 거였어요.'),
      T('sia/E12', '선배 설명, 회전목마 얘기가 제일 쏙 들어왔어요.'),
      T('moa/E01', '다음은 피자랑 환전이죠? 기록 다 모아 뒀어요.'),
      T('fly/E01', '주판봇 계산도 한 번은 의심하는 습관, 잊지 말자.'),
      T('robo/E12', '1부에서는 더 정확하게 튕겨 보겠습니다!'))}
{crowd('방청석', [('x1/E01', '(짝짝짝)'), ('x2/E16', '(끄덕끄덕)'), ('x3/E01', '(반짝)')])}
<a class="dashlink" href="dash_00.html"><b>0편 복습 대시보드 — 좌표계 놀이터 →</b><br>함수·화살표 밭·점·자를 바꿔 가며 기울기·발산·회전·라플라시안이 세 자에서 같은 값인지 직접 확인합니다. 미션 3개.</a>
<div class="nextp"><a href="index.html"><b>← 목차</b>벡터 분석 랩</a><a href="01_everyday.html"><b>다음 →</b>1부 생활 — 같은 1도, 다른 길이</a></div>
</section>

<section id="kg">
<h2>지식 색인</h2>
<p>이 페이지의 개념과 나오는 방입니다.</p>
<div class="kg">
<a href="#room-e">두 점 사이 거리 · 입구 방</a><a href="#room-e">직교좌표 · 입구 방</a><a href="#room-a">원통좌표 · 방 A</a><a href="#room-a">구면좌표 · 방 A</a><a href="#room-a">일반 직교곡선좌표 · 방 A</a><a href="#room-a">축척 인자 h · 방 A</a><a href="#room-a">기울기의 1/h · 방 A</a><a href="#room-b">부피 요소 dV · 방 B</a><a href="#fix">원자료 표기 · 다르게 쓴 곳</a>
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
{FOOT_SRC}<br>
설명용 예시: 시아·모아의 키·몸무게, 점 (1, 1, 1.41). 캐릭터: 연구실 식구(fruitfly-lab-expressions). 표지는 픽셀아트 표지를 받기 전까지 쓰는 임시 그림입니다.
</div></footer>
"""
    return h

PAGE_JS = r"""
// ---- 입구 방 ----
{const s=$('resvg');
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const mh=+$('reh').value,mw=+$('rew').value,sh=160,sw=50;
  const x0=48,y0=H-36,kx=(W-80)/(175-150),ky=(H-60)/(65-40);const X=v=>x0+(v-150)*kx,Y=v=>y0-(v-40)*ky;
  let g='';for(let v=150;v<=175;v+=5)g+=`<line x1="${X(v)}" y1="${Y(40)}" x2="${X(v)}" y2="${Y(65)}" stroke="#eef1f4"/><text x="${X(v)}" y="${y0+18}" font-size="12" text-anchor="middle" fill="#5d6676">${v}</text>`;
  for(let v=40;v<=65;v+=5)g+=`<line x1="${X(150)}" y1="${Y(v)}" x2="${X(175)}" y2="${Y(v)}" stroke="#eef1f4"/><text x="${x0-8}" y="${Y(v)+4}" font-size="12" text-anchor="end" fill="#5d6676">${v}</text>`;
  g+=`<text x="${W-10}" y="${y0-6}" font-size="12" text-anchor="end" fill="#5d6676">키 (cm)</text><text x="${x0+4}" y="16" font-size="12" fill="#5d6676">몸무게 (kg)</text>`;
  g+=`<line x1="${X(sh)}" y1="${Y(sw)}" x2="${X(mh)}" y2="${Y(sw)}" stroke="#d4691f" stroke-width="3"/><line x1="${X(mh)}" y1="${Y(sw)}" x2="${X(mh)}" y2="${Y(mw)}" stroke="#1f7a8c" stroke-width="3"/>`;
  g+=`<line x1="${X(sh)}" y1="${Y(sw)}" x2="${X(mh)}" y2="${Y(mw)}" stroke="#24345c" stroke-width="3.5" stroke-dasharray="6 4"/>`;
  g+=`<circle cx="${X(sh)}" cy="${Y(sw)}" r="8" fill="#5a5a6e"/><text x="${X(sh)-10}" y="${Y(sw)+22}" font-size="13" fill="#5a5a6e" font-weight="700">시아</text>`;
  g+=`<circle cx="${X(mh)}" cy="${Y(mw)}" r="8" fill="#93651a"/><text x="${X(mh)+10}" y="${Y(mw)-8}" font-size="13" fill="#93651a" font-weight="700">모아</text>`;
  s.innerHTML=g;const dx=mh-sh,dy=mw-sw,d=Math.hypot(dx,dy);
  $('reread').innerHTML=`가로(키) 차이 <b>${Math.abs(dx)}</b> · 세로(몸무게) 차이 <b>${Math.abs(dy)}</b> → 거리 √(${dx*dx} + ${dy*dy}) = <b>${d.toFixed(2)}</b>${d===0?' — 두 점이 겹쳤어요. 이 두 축으로는 똑같은 사람입니다.':''}`};
 bindSl('reh',v=>v+' cm',draw)();bindSl('rew',v=>v+' kg',draw)();obs(s,draw)}
// ---- 방 A ----
{const s=$('rasvg');let sys='C';const step=0.3;
 const pick=k=>{sys=k;[['raC','C'],['raY','Y'],['raS','S']].forEach(([id,v])=>$(id).setAttribute('aria-pressed',v===k));draw()};
 const add=(a,b,t=1)=>[a[0]+b[0]*t,a[1]+b[1]*t,a[2]+b[2]*t];
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const x=+$('rax').value,y=+$('ray').value,z=+$('raz').value;
  const k=Math.min(W/3.9,H/2.75),ox=W*0.42,oy=H*0.86;
  const P=p=>[ox+k*(p[1]*0.95-p[0]*0.62),oy-k*(p[2]*0.95+p[0]*0.28+p[1]*0.12)];
  const ln=(a,b,c,w=1.5,d='')=>{const A=P(a),B=P(b);return`<line x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}" stroke="${c}" stroke-width="${w}" ${d?`stroke-dasharray="${d}"`:''}/>`};
  const ar=(a,b,c,lab)=>{const A=P(a),B=P(b),dx=B[0]-A[0],dy=B[1]-A[1],L=Math.hypot(dx,dy)||1,ux=dx/L,uy=dy/L,hs=Math.min(11,L*.5);
   return`<line x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}" stroke="${c}" stroke-width="4"/><polygon points="${B[0]},${B[1]} ${B[0]-hs*ux+hs*.5*uy},${B[1]-hs*uy-hs*.5*ux} ${B[0]-hs*ux-hs*.5*uy},${B[1]-hs*uy+hs*.5*ux}" fill="${c}"/><text x="${B[0]+6}" y="${B[1]-4}" font-size="13" font-weight="700" fill="${c}">${lab}</text>`};
  let g='';for(let i=0;i<=2;i+=0.5){g+=ln([i,0,0],[i,2,0],'#eef1f4',1)+ln([0,i,0],[2,i,0],'#eef1f4',1)}
  g+=ln([0,0,0],[2.3,0,0],'#1c2230',1.4)+ln([0,0,0],[0,2.3,0],'#1c2230',1.4)+ln([0,0,0],[0,0,2.2],'#1c2230',1.4);
  [[2.35,0,0,'x'],[0,2.4,0,'y'],[0,0,2.28,'z']].forEach(q=>{const A=P(q);g+=`<text x="${A[0]+4}" y="${A[1]+4}" font-size="14" fill="#1c2230">${q[3]}</text>`});
  const p=[x,y,z];g+=ln([x,y,0],p,'#9aa3b0',1,'3 3')+ln([0,0,0],[x,y,0],'#9aa3b0',1,'3 3')+ln([0,0,0],p,'#c9ced6',1,'2 4');
  const rho=Math.hypot(x,y),r=Math.hypot(x,y,z),ph=Math.atan2(y,x),th=Math.acos(z/r);
  let E,hh,names;
  if(sys==='C'){E=[[1,0,0],[0,1,0],[0,0,1]];hh=[1,1,1];names=['x 쪽','y 쪽','z 쪽']}
  else if(sys==='Y'){E=[[Math.cos(ph),Math.sin(ph),0],[-Math.sin(ph),Math.cos(ph),0],[0,0,1]];hh=[1,rho,1];names=['ρ 쪽','φ 쪽','z 쪽'];
   const c=[];for(let i=0;i<=48;i++){const t=i/48*2*Math.PI;c.push(P([rho*Math.cos(t),rho*Math.sin(t),z]))}g+=`<polyline points="${c.map(q=>q.join(',')).join(' ')}" fill="none" stroke="#1f7a8c" stroke-width="1.2" stroke-dasharray="4 4"/>`}
  else{E=[[Math.sin(th)*Math.cos(ph),Math.sin(th)*Math.sin(ph),Math.cos(th)],[Math.cos(th)*Math.cos(ph),Math.cos(th)*Math.sin(ph),-Math.sin(th)],[-Math.sin(ph),Math.cos(ph),0]];hh=[1,r,r*Math.sin(th)];names=['r 쪽','θ 쪽','φ 쪽'];
   const c=[],m=[];for(let i=0;i<=48;i++){const t=i/48*2*Math.PI;c.push(P([rho*Math.cos(t),rho*Math.sin(t),z]));const u=i/48*Math.PI;m.push(P([r*Math.sin(u)*Math.cos(ph),r*Math.sin(u)*Math.sin(ph),r*Math.cos(u)]))}
   g+=`<polyline points="${c.map(q=>q.join(',')).join(' ')}" fill="none" stroke="#24345c" stroke-width="1.2" stroke-dasharray="4 4"/><polyline points="${m.map(q=>q.join(',')).join(' ')}" fill="none" stroke="#c0392b" stroke-width="1.2" stroke-dasharray="4 4"/>`}
  const cols=['#d4691f','#1f7a8c','#7a3fd6'];
  E.forEach((e,i)=>{g+=ar(p,add(p,e,hh[i]*step*2),cols[i],names[i])});
  const A=P(p);g+=`<circle cx="${A[0]}" cy="${A[1]}" r="6" fill="#1c2230"/>`;
  s.innerHTML=g;
  const coord=sys==='C'?`(x, y, z) = (${x.toFixed(2)}, ${y.toFixed(2)}, ${z.toFixed(2)})`:sys==='Y'?`(ρ, φ, z) = (${rho.toFixed(2)}, ${(ph*R2D).toFixed(0)}°, ${z.toFixed(2)})`:`(r, θ, φ) = (${r.toFixed(2)}, ${(th*R2D).toFixed(0)}°, ${(ph*R2D).toFixed(0)}°)`;
  $('raread').innerHTML=`이 자로 읽은 점: <b>${coord}</b><br>눈금 0.3 한 걸음의 실제 길이: ${names.map((n,i)=>`${n} <b>${(hh[i]*step).toFixed(2)} m</b> (h = ${hh[i].toFixed(2)})`).join(' · ')}<br><span style="font-size:14px;color:#5d6676">화살표는 보기 좋게 2배로 그렸습니다. 길이의 비율은 그대로입니다.</span>`};
 $('raC').onclick=()=>pick('C');$('raY').onclick=()=>pick('Y');$('raS').onclick=()=>pick('S');
 ['rax','ray','raz'].forEach(id=>bindSl(id,v=>v.toFixed(2),draw)());obs(s,draw)}
// ---- 방 B ----
{const s=$('rbsvg');
 const draw=()=>{const[W,H]=svgSize(s);if(!W)return;const r=+$('rbr').value,th=+$('rbt').value*D2R,rho=r*Math.sin(th);
  const v=[0.001,rho*0.001,r*r*Math.sin(th)*0.001],lab=['가로·세로·높이','원통 (ρ = '+rho.toFixed(2)+')','지구본 (r² sinθ = '+(r*r*Math.sin(th)).toFixed(2)+')'],cols=['#d4691f','#1f7a8c','#24345c'];
  const mx=0.009,bw=Math.min(120,(W-80)/4),base=H-40,top=26;let g=`<line x1="40" y1="${base}" x2="${W-10}" y2="${base}" stroke="#1c2230"/>`;
  [0.002,0.004,0.006,0.008].forEach(t=>{const y=base-(base-top)*t/mx;g+=`<line x1="40" y1="${y}" x2="${W-10}" y2="${y}" stroke="#eef1f4"/><text x="36" y="${y+4}" font-size="11" text-anchor="end" fill="#5d6676">${t}</text>`});
  v.forEach((val,i)=>{const x=60+i*(W-80)/3,hgt=(base-top)*Math.min(val,mx)/mx;g+=`<rect x="${x}" y="${base-hgt}" width="${bw}" height="${hgt}" fill="${cols[i]}" opacity=".85" rx="4"/><text x="${x+bw/2}" y="${base-hgt-6}" font-size="14" font-weight="700" text-anchor="middle" fill="${cols[i]}">${val.toFixed(5)}</text><text x="${x+bw/2}" y="${base+18}" font-size="12" text-anchor="middle" fill="#1c2230">${lab[i]}</text>`});
  s.innerHTML=g;
  $('rbread').innerHTML=`중심에서 <b>${r.toFixed(1)}</b>, 꼭대기에서 <b>${(th*R2D).toFixed(0)}°</b>인 점 (중심축에서 거리 ρ = ${rho.toFixed(2)})<br>작은 상자 부피: 가로·세로·높이 <b>0.00100</b> · 원통 <b>${v[1].toFixed(5)}</b> · 지구본 <b>${v[2].toFixed(5)}</b>${Math.sin(th)<0.02?' — <span class="bad">꼭대기라 상자가 납작해져 부피가 0에 가깝습니다.</span>':''}`};
 bindSl('rbr',v=>v.toFixed(1),draw)();bindSl('rbt',v=>v+'°',draw)();obs(s,draw)}
"""

PACK_DATA = {
    "@context": {"schema": "https://schema.org/", "rel": "https://adminmrobo.github.io/vector_analysis_lab/rel#"},
    "page": "벡터 분석 랩 0편 — 네 개의 자 소개", "author": "안상선 ((주)M-Robo)",
    "url": "https://adminmrobo.github.io/vector_analysis_lab/00_orientation.html",
    "source": "@eeanimation, Vector Analysis infographic 1/4–4/4",
    "concepts": ["직교좌표", "원통좌표", "구면좌표", "일반 직교곡선좌표", "축척 인자", "부피 요소", "기울기", "두 점 사이 거리"],
    "relations": [["축척 인자", "정한다", "기울기의 1/h"], ["축척 인자", "곱하면", "부피 요소"],
                  ["원통좌표", "축척 인자", "1, ρ, 1"], ["구면좌표", "축척 인자", "1, r, r sinθ"],
                  ["직교좌표", "축척 인자", "1, 1, 1"], ["일반 직교곡선좌표", "묶는다", "직교·원통·구면"]],
    "cite": "안상선 (2026). 벡터 분석 랩 0편 — 네 개의 자 소개. https://adminmrobo.github.io/vector_analysis_lab/00_orientation.html"
}

if __name__ == '__main__':
    b = body()
    n = page('00_orientation.html', '벡터 분석 랩 0편 — 네 개의 자, 하루의 첫 수업',
             '같은 화살표도 어떤 자로 재느냐에 따라 숫자가 달라집니다. 원자료 카드 네 장의 한 걸음 길이 h와 작은 상자 dV를 직접 움직여 봅니다.',
             'assets/og/00.webp', b, PAGE_JS, PACK_DATA,
             ['직교좌표', '원통좌표', '구면좌표', '축척 인자', '부피 요소'])
    print('00 bytes', n)
