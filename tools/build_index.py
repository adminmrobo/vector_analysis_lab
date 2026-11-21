# -*- coding: utf-8 -*-
"""목차 index.html"""
from common import *

def body():
    cast = [('sia/E13', '시아 (인턴1)', '하루에게 묻는 직관파'), ('moa/E09', '모아 (인턴2)', '하루에게 묻는 꼼꼼파'),
            ('asst/E20', '하루 (조수)', '처음 수업을 맡아 긴장했지만 끝까지 풀어 봄'), ('fly/E08', '초파리 연구원', '"이걸 눌러 봐"로 돕는 의심 담당'),
            ('robo/E09', '주판봇', '숫자를 1초 만에 내는 계산 담당'), ('doc/E08', '박사', '방마다 정리'),
            ('x1/E15', '미공개 X1·X2·X3', '방청석에서 하루를 걱정하는 소리')]
    c = '<div class="cast">'
    for k, n, d in cast:
        USED.append(k)
        c += f'<div><img data-k="{k}" alt="{n}"><span><b>{n}</b>{d}</span></div>'
    c += '</div>'
    return f"""
<header class="hero"><div class="wrap">
<div class="wing e">연구실 해설 시리즈 · 좌표축 위의 그릇 특별편</div>
<h1>벡터 분석 랩<br>네 개의 자로 읽는 화살표</h1>
<p class="sub">같은 화살표라도 어떤 자(좌표)로 재느냐에 따라 숫자가 달라집니다. 피자·지도·환전에서 먼저 느끼고, 경제·금융에서 한 번 더 보고, 인공지능·머신러닝에서 마무리합니다.</p>
<figure class="cover" style="margin-left:0;margin-right:0"><img src="assets/cover_index.webp" width="1600" height="900" alt="네 장의 좌표 카드 앞에 선 긴장한 하루와 연구실 식구들, 방청석의 미공개 X1~X3 (임시 표지)"></figure>
<div class="by">{AUTHOR}</div>
<a class="cta" href="00_orientation.html">0편부터 시작하기</a>
</div></header>
<main class="wrap">
<section>
<div class="three">
<h2>처음 오신 분께 — 이 시리즈를 3줄로</h2>
<ol>
<li><b>무엇을:</b> @eeanimation 「Vector Analysis」 카드 네 장(직교·원통·구면·일반 좌표)의 기울기·발산·회전·라플라시안을 봅니다.</li>
<li><b>어떻게:</b> 같은 개념을 생활(1부) → 경제·금융(2부) → AI·머신러닝(3부) 순으로 세 번 만납니다.</li>
<li><b>누구와:</b> 시아·모아가 묻고, 처음 수업을 맡은 조수 하루가 답하고, 초파리 연구원과 주판봇이 돕고, 박사가 정리합니다.</li>
</ol>
<p style="margin:0">코드·수식을 몰라도 됩니다. 수치는 모두 교육용 예시입니다.</p>
</div>
</section>
<section>
<h2>목차</h2>
<div class="toc">
<a class="p0" href="00_orientation.html"><b class="n">0편 오리엔테이션</b>네 개의 자 — 하루의 첫 수업<br><span style="font-size:14px;color:var(--mute)">입구 방(두 점 사이 거리) · 방 A 네 개의 자와 h · 방 B 한 걸음 상자 dV</span></a>
<a class="p1" href="01_everyday.html"><b class="n">1부 생활 · 방 1~7</b>같은 1도, 다른 길이<br><span style="font-size:14px;color:var(--mute)">피자 테두리 · 12월과 1월 · 경도 1도 · 그린란드 · 지하철역(발산) · 환전 한 바퀴(회전) · 사진 윤곽선(라플라시안)</span></a>
<a class="p0" href="dash_00.html"><b class="n">0편 복습 대시보드</b>좌표계 놀이터 — 같은 ∇, 세 가지 자<br><span style="font-size:14px;color:var(--mute)">함수·화살표 밭·자를 바꿔 기울기·발산·회전·라플라시안 비교 · 미션 3개</span></a>
<a class="p1" href="dash_01.html"><b class="n">1부 복습 대시보드</b>생활 장면 시뮬레이터<br><span style="font-size:14px;color:var(--mute)">피자 가게·지구 배송센터·역과 환전소·사진 앱 · 미션 12개</span></a>
<a class="p2" href="02_economy.html"><b class="n">2부 경제·금융 · 방 8~12</b>1부에서 본 장면이 시장에서<br><span style="font-size:14px;color:var(--mute)">경기순환시계 · 차익거래 = 회전 · 자금순환의 샘과 배수구 · 집값 확산 · 상관을 각도로</span></a>
<a class="p2" href="dash_02.html"><b class="n">2부 복습 대시보드</b>경제 상황실<br><span style="font-size:14px;color:var(--mute)">경기 상황실 · 환전 데스크 · 자금순환판 · 동네 지도와 포트폴리오 · 미션 12개</span></a>
<a class="p3" href="03_ai_ml.html"><b class="n">3부 AI·머신러닝 · 방 13~18 + 대결</b>자를 잘 고르면 모델이 쉬워진다<br><span style="font-size:14px;color:var(--mute)">달력 시계 특성 · 임베딩 · RoPE · 가중치 길이와 걸음 · 늘리면 묽어진다 · GNN · 박사 vs 하루</span></a>
<a class="p3" href="dash_03.html"><b class="n">3부 복습 대시보드</b>AI 실험실<br><span style="font-size:14px;color:var(--mute)">판매 예측 · 단어 나침반 · 학습 걸음 · 확률과 관계망 · 미션 12개</span></a></div>
</div>
</section>
<section>
<h2>등장인물</h2>
{c}
{talk(T('asst/E20', '여러분, 저 오늘 처음으로 수업해요… 같이 끝까지 가 주실 거죠?'))}
{crowd('방청석', [('x1/E15', '(조마조마)'), ('x2/E02', '(꿀꺽)'), ('x3/E04', '(…!)')])}
</section>
<section>
<h2>같은 장면, 세 번</h2>
<div class="scroll"><table class="sum"><thead><tr><th>원자료 카드의 개념</th><th>1부 생활</th><th>2부 경제·금융</th><th>3부 AI·머신러닝</th></tr></thead><tbody>
<tr><td>한 걸음의 실제 길이 h</td><td>피자 테두리 · 경도 1도</td><td>경기순환시계 · 상관을 각도로</td><td>달력 시계 특성 · 가중치 길이와 걸음</td></tr>
<tr><td>작은 상자 dV</td><td>그린란드</td><td>—</td><td>늘리면 묽어진다</td></tr>
<tr><td>발산</td><td>지하철역</td><td>자금순환</td><td>—</td></tr>
<tr><td>회전</td><td>환전 한 바퀴</td><td>차익거래</td><td>위치를 각도로(RoPE)</td></tr>
<tr><td>라플라시안</td><td>사진 윤곽선</td><td>집값 확산</td><td>이웃 평균으로 다듬기(GNN)</td></tr>
</tbody></table></div>
<p style="margin-top:14px">함께 보면 좋은 곳: <a href="https://adminmrobo.github.io/vector_calculus_lab/">∇ 특별편</a> · <a href="https://adminmrobo.github.io/nabla_field_lab/">같은 ∇, 다른 현장</a> · <a href="https://adminmrobo.github.io/optimization_3d_map/">좌표축 위의 그릇</a></p>
</section>
<section id="export">
<h2>온톨로지·서지 꾸러미</h2>
<div class="btns"><button class="btn" id="copyPack">꾸러미 복사</button><span id="copyMsg" style="align-self:center;font-size:14px;color:var(--mute)" aria-live="polite"></span></div>
<pre id="pack"></pre>
</section>
</main>
<footer><div class="wrap">
{AUTHOR}<br>
원자료: @eeanimation 「Vector Analysis」 인포그래픽 4장. 캐릭터: 연구실 식구(fruitfly-lab-expressions). 표지는 픽셀아트 표지를 받기 전까지 쓰는 임시 그림입니다.
</div></footer>
"""

PACK_DATA = {"series": "벡터 분석 랩 — 네 개의 자로 읽는 화살표", "author": "안상선 ((주)M-Robo)",
             "url": "https://adminmrobo.github.io/vector_analysis_lab/",
             "parts": ["00_orientation.html", "dash_00.html", "01_everyday.html", "dash_01.html", "02_economy.html", "dash_02.html", "03_ai_ml.html", "dash_03.html"],
             "source": "@eeanimation, Vector Analysis infographic 1/4–4/4",
             "cite": "안상선 (2026). 벡터 분석 랩 — 네 개의 자로 읽는 화살표. https://adminmrobo.github.io/vector_analysis_lab/"}

if __name__ == '__main__':
    n = page('index.html', '벡터 분석 랩 — 네 개의 자로 읽는 화살표',
             '피자·지도·환전에서 경제·금융, 인공지능까지. 원자료 카드 네 장의 좌표와 ∇를 하루의 첫 수업으로 배웁니다.',
             'assets/og/index.webp', body(), '', PACK_DATA, ['좌표계', '축척 인자', '발산', '회전', '라플라시안'])
    print('index bytes', n)
