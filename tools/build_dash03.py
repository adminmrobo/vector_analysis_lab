# -*- coding: utf-8 -*-
"""3부 복습 대시보드 — AI 실험실 (탭 4개, 미션 12개)"""
from common import *
from build_dash01 import scene, sl2
from build_dash02 import COMMON_DASH_JS

TABS = [('sales', '판매 예측', '방 13'), ('words', '단어 나침반', '방 14·15'), ('steps', '학습 걸음', '방 16'), ('prob', '확률과 관계망', '방 17·18')]

def body():
    for k in ['x1/E15', 'x2/E02', 'x3/E04', 'x1/E01', 'x2/E16', 'x3/E01']:
        USED.append(k)
    tabs = ''.join(f'<button class="btn" role="tab" id="tb-{k}" aria-controls="tab-{k}" aria-selected="false">{t} <span style="font-size:12px;opacity:.75">{r}</span></button>' for k, t, r in TABS)
    h = f"""
<header class="hero"><div class="wrap">
<div class="wing">벡터 분석 랩 · 3부 복습 대시보드</div>
<h1>AI 실험실<br>특성 만들기에서 관계망까지</h1>
<p class="sub">3부 여섯 방을 네 개의 가상 실험에서 직접 돌려 봅니다. 초록은 주어진 조건, 파랑은 여러분의 결정입니다. 실험마다 미션 3개, 모두 12개입니다.</p>
<div class="by">{AUTHOR}</div>
</div></header>
<main class="wrap"><section>
{talk(T('asst/E19', '마지막 복습이에요. 이번엔 떨지 않고 성적표를 읽어 볼게요!'))}
{crowd('방청석', [('x1/E15', '<span id="xs1">(조마조마)</span>'), ('x2/E02', '<span id="xs2">(꿀꺽)</span>'), ('x3/E04', '<span id="xs3">(…!)</span>')])}
<details style="margin:10px 0"><summary>이 대시보드의 기호와 약어 풀이</summary><table><tbody><tr><td class="m">RMSE</td><td>빗나간 값을 제곱해 평균 낸 뒤 제곱근</td></tr><tr><td class="m">코사인</td><td>두 화살표 방향이 같은 정도(−1~1)</td></tr><tr><td class="m">RoPE</td><td>자리만큼 화살표를 돌려 위치를 넣는 방법</td></tr><tr><td class="m">rad</td><td>라디안. 180° = 3.14</td></tr><tr><td class="m">밀도</td><td>그 자리의 확률 높이</td></tr><tr><td class="m">GNN</td><td>관계망에서 이웃 값을 섞는 신경망</td></tr></tbody></table></details>
<div class="tabs" role="tablist" aria-label="실험 고르기">{tabs}</div>
<p id="allSum" style="font-weight:700" aria-live="polite"></p>
"""
    h += scene('sales', '아이스크림 회사의 월별 판매 예측 모델을 만듭니다. 같은 직선 모델에 달을 숫자(1~12)로 넣을지, 시계판 두 숫자(cos, sin)로 넣을지 고릅니다(가상 판매).',
               sl2('saAmp', '계절 차이', 20, 80, 5, 60) + sl2('saPk', '가장 잘 팔리는 달', 1, 12, 1, 7),
               '<div class="btns" role="group" aria-label="특성" style="margin-top:0"><button class="btn" id="saN" aria-pressed="true">숫자 특성</button><button class="btn" id="saC" aria-pressed="false">시계 특성</button></div>' + sl2('saM', '확인할 달', 1, 12, 1, 6),
               '월별 실제 판매(막대)와 고른 모델의 예측선', '달마다 빗나간 크기(고른 모델) — 확인할 달 표시',
               ['<b>시계 특성으로 맞히기:</b> 시계 특성을 골라 평균 오차를 0.5 아래로 만드세요.',
                '<b>숫자 특성의 약점:</b> 숫자 특성을 고른 채, 가장 크게 빗나간 달을 "확인할 달"로 찾으세요.',
                '<b>꼭대기가 12월이어도:</b> 가장 잘 팔리는 달을 12월로 바꾸고, 시계 특성의 평균 오차가 0.5 아래인지 확인하세요.'],
               '<a href="03_ai_ml.html#room-13">방 13 달력 시계 특성</a> · <a href="01_everyday.html#room-2">1부 방 2 12월과 1월</a>')
    h += scene('words', '문서 검색팀이 두 문장 화살표(임베딩)의 비슷함을 재고, 언어 모델팀이 단어 위치를 각도로 넣는 방법(RoPE)을 점검합니다.',
               '<p style="font-size:13px;margin:0;color:var(--mute)">문장 A = (3, 4) 고정 · RoPE는 한 자리에 30°</p>',
               sl2('wdA', 'A–B 각도', 0, 180, 1, 40) + sl2('wdL', 'B의 길이', 1, 12, 0.5, 4) + sl2('wdI', '단어 1 자리', 0, 11, 1, 0) + sl2('wdJ', '단어 2 자리', 0, 11, 1, 1),
               '두 문장 화살표와 코사인', '자리만큼 돌린 두 단어 화살표와 겹침 점수',
               ['<b>길이가 달라도 비슷:</b> B의 길이를 8 이상으로 두고, 코사인이 0.96(±0.005)이 되게 각도를 맞추세요.',
                '<b>관계없는 두 문장:</b> 코사인을 0(±0.02)으로 만드세요.',
                '<b>세 자리 떨어진 단어:</b> 두 단어의 겹침 점수가 0이 되도록 자리를 정하세요.'],
               '<a href="03_ai_ml.html#room-14">방 14 임베딩</a> · <a href="03_ai_ml.html#room-15">방 15 RoPE</a>')
    h += scene('steps', '방향만 보는 모델을 학습시킵니다. 가중치 방향을 45° 돌리는 데 몇 걸음이 걸리는지 봅니다. 가중치 감쇠를 켜면 매 걸음 가중치 길이가 5%씩 줄어듭니다.',
               sl2('stLr', '학습률', 0.5, 4, 0.1, 1) + '<div class="btns" role="group" aria-label="가중치 감쇠"><button class="btn" id="stOff" aria-pressed="true">감쇠 끔</button><button class="btn" id="stOn" aria-pressed="false">감쇠 켬(5%)</button></div>',
               sl2('stR', '처음 가중치 길이', 1, 12, 0.5, 8),
               '걸음마다 돈 각도(감쇠 끔·켬 비교)와 45° 목표선', '걸음마다 가중치 길이',
               ['<b>빠른 학습:</b> 감쇠를 끄고 학습률 1에서, 45°까지 20걸음 이하가 되도록 처음 길이를 정하세요.',
                '<b>긴 가중치를 학습률로:</b> 처음 길이를 10으로 두고 감쇠 없이 20걸음 이하가 되게 학습률을 정하세요.',
                '<b>감쇠의 효과:</b> 처음 길이 10, 학습률 1에서 감쇠를 켜고 30걸음 이하로 45°에 닿는지 확인하세요.'],
               '<a href="03_ai_ml.html#room-16">방 16 가중치 길이와 걸음</a> · <a href="00_orientation.html#room-a">0편 방 A 한 걸음 h</a>')
    h += scene('prob', '생성 모델팀은 분포를 늘였을 때 밀도를 고치고, 추천팀은 관계망에서 이웃 값을 섞습니다(그래프 신경망의 기본).',
               sl2('prS', '늘림 배수', 0.5, 3, 0.1, 1.5) + '<div class="btns" role="group" aria-label="축 수"><button class="btn" id="pr1" aria-pressed="true">1축</button><button class="btn" id="pr2" aria-pressed="false">2축</button></div>',
               sl2('prA', '섞는 속도 α', 0.1, 1, 0.1, 0.5) + '<div class="btns"><button class="btn" id="prStep">한 번 섞기</button><button class="btn" id="prReset">처음으로</button></div>',
               '늘어난 상자와 밀도(넓이는 늘 1)', '관계망 다섯 노드의 값',
               ['<b>선을 두 배로:</b> 1축에서 밀도가 0.5가 되게 늘리세요.',
                '<b>넓이를 네 배로:</b> 2축에서 밀도가 0.25가 되게 늘리세요.',
                '<b>지나친 섞임 보기:</b> 관계망을 계속 섞어 다섯 값의 가장 큰 차이를 0.3 아래로 만드세요. 그때 각 노드의 특징은 남아 있나요?'],
               '<a href="03_ai_ml.html#room-17">방 17 늘리면 묽어진다</a> · <a href="03_ai_ml.html#room-18">방 18 GNN</a>')
    h += f"""
<div class="limit" style="margin-top:24px"><b>이 대시보드의 한계</b> 판매는 사인 곡선 하나, 임베딩은 2축, 학습은 "방향만 보는 모델"에 단순한 걸음, 관계망은 다섯 노드로 줄였습니다. 실제 모델은 훨씬 크고 설정이 많습니다. 수치는 교육용 예시입니다.</div>
</section>
<section id="outro"><div class="nextp"><a href="03_ai_ml.html"><b>← 3부 본문</b>AI·머신러닝</a><a href="index.html"><b>목차</b>벡터 분석 랩</a></div></section>
<section id="export"><h2>온톨로지·서지 꾸러미</h2>
<div class="btns"><button class="btn" id="copyPack">꾸러미 복사</button><span id="copyMsg" style="align-self:center;font-size:14px;color:var(--mute)" aria-live="polite"></span></div>
<pre id="pack"></pre></section>
</main>
<footer><div class="wrap">{AUTHOR}<br>원자료: @eeanimation 「Vector Analysis」 4장. 수치는 교육용 예시입니다. 캐릭터: 연구실 식구(fruitfly-lab-expressions).</div></footer>
"""
    return h

PAGE_JS = "const KEYS=['sales','words','steps','prob'];" + COMMON_DASH_JS + r"""
// ===== 판매 =====
const solveLS=(X,y)=>{const n=X[0].length,A=Array.from({length:n},()=>Array(n+1).fill(0));X.forEach((r,i)=>{for(let a=0;a<n;a++){for(let b=0;b<n;b++)A[a][b]+=r[a]*r[b];A[a][n]+=r[a]*y[i]}});
 for(let c=0;c<n;c++){let p=c;for(let r=c+1;r<n;r++)if(Math.abs(A[r][c])>Math.abs(A[p][c]))p=r;[A[c],A[p]]=[A[p],A[c]];for(let r=0;r<n;r++)if(r!==c){const f=A[r][c]/A[c][c];for(let k=c;k<=n;k++)A[r][k]-=f*A[c][k]}}return A.map((r,i)=>r[n]/r[i])};
const fit=(amp,pk,md)=>{const m=[...Array(12)].map((_,i)=>i+1),y=m.map(v=>100+amp*Math.cos(2*Math.PI*(v-pk)/12));const X=m.map(v=>md==='n'?[1,v]:[1,Math.cos(2*Math.PI*(v-1)/12),Math.sin(2*Math.PI*(v-1)/12)]);
 const b=solveLS(X,y),p=X.map(r=>r.reduce((s,x,i)=>s+x*b[i],0)),e=p.map((v,i)=>v-y[i]);return{y,p,e,rm:Math.sqrt(e.reduce((s,v)=>s+v*v,0)/12)}};
let saMode='n';$('saN').onclick=()=>{saMode='n';press(['saN','saC'],'saN');touched.sales=true;DRAW.sales()};$('saC').onclick=()=>{saMode='c';press(['saN','saC'],'saC');touched.sales=true;DRAW.sales()};
DRAW.sales=()=>{const amp=+$('saAmp').value,pk=+$('saPk').value,mm=+$('saM').value,F=fit(amp,pk,saMode),worst=F.e.map(Math.abs).indexOf(Math.max(...F.e.map(Math.abs)))+1;
 const g1=$('salesG1'),[W,H]=svgSize(g1);if(W){const x0=30,x1=W-8,y0=12,y1=H-24,bw=(x1-x0)/12,Y=v=>y1-v/190*(y1-y0);let g='';F.y.forEach((v,i)=>g+=`<rect x="${x0+i*bw+2}" y="${Y(v)}" width="${bw-4}" height="${y1-Y(v)}" fill="#c9ddeb" rx="2"/><text x="${x0+i*bw+bw/2}" y="${y1+14}" font-size="10" text-anchor="middle">${i+1}</text>`);
  g+=`<polyline points="${F.p.map((v,i)=>[x0+i*bw+bw/2,Y(v)].join(',')).join(' ')}" fill="none" stroke="${saMode==='n'?'#c0392b':'#1e8a4c'}" stroke-width="3"/>`;g1.innerHTML=g}
 const g2=$('salesG2'),[W2,H2]=svgSize(g2);if(W2){const x0=30,x1=W2-8,mid=H2/2,bw=(x1-x0)/12,sc=(H2*0.42)/90;let g=`<line x1="${x0}" y1="${mid}" x2="${x1}" y2="${mid}" stroke="#1c2230"/>`;
  F.e.forEach((v,i)=>{const hh=Math.min(Math.abs(v),90)*sc;g+=`<rect x="${x0+i*bw+3}" y="${v>=0?mid-hh:mid}" width="${bw-6}" height="${Math.max(1,hh)}" fill="${i+1===mm?'#d4691f':'#9aa3b0'}"/><text x="${x0+i*bw+bw/2}" y="${H2-6}" font-size="10" text-anchor="middle">${i+1}</text>`});g2.innerHTML=g}
 score('sales',[['고른 특성',saMode==='n'?'숫자(1~12)':'시계(cos, sin)','같은 직선 모델'],['평균 오차',F.rm.toFixed(1),'작을수록 좋음',F.rm<0.5?'ok':F.rm>20?'warn':''],[`${mm}월 빗나감`,(F.e[mm-1]>=0?'+':'')+F.e[mm-1].toFixed(1),`예측 ${F.p[mm-1].toFixed(1)} · 실제 ${F.y[mm-1].toFixed(1)}`,saMode==='n'&&mm===worst?'ok':''],['가장 크게 빗나간 달',worst+'월','고른 모델 기준']]);
 const n=mission('sales',[saMode==='c'&&F.rm<0.5,saMode==='n'&&mm===worst&&F.rm>1,saMode==='c'&&pk===12&&F.rm<0.5]);
 say('sales',`${saMode==='n'?'숫자':'시계'} 특성 모델의 평균 오차는 ${F.rm.toFixed(1)}이에요. ${mm}월은 ${F.e[mm-1].toFixed(1)}만큼 빗나갔어요.`,`가장 크게 빗나간 달은 ${worst}월! 시계 특성이면 꼭대기가 몇 월이든 cos·sin 무게만 바꾸면 돼요.`,
  saMode==='n'?'숫자 특성은 12월과 1월을 가장 먼 사이로 봐. 그림 ②에서 양 끝 막대를 봐.':'오차가 0이라고 실제 데이터에서도 0일까? 이건 사인 곡선 하나로 만든 가상 데이터야.',
  doc(n,'모델을 바꾸기 전에 자(특성)를 먼저 바꿔 보세요.'))};
['saAmp','saPk','saM'].forEach(id=>bindT('sales',id,v=>id==='saAmp'?v:v+'월'));
// ===== 단어 =====
DRAW.words=()=>{const d=+$('wdA').value*D2R,L=+$('wdL').value,i=+$('wdI').value,j=+$('wdJ').value,a0=Math.atan2(4,3),B=[L*Math.cos(a0+d),L*Math.sin(a0+d)],cs=(3*B[0]+4*B[1])/(5*L),dist=Math.hypot(3-B[0],4-B[1]),rp=Math.cos((j-i)*30*D2R);
 const g1=$('wordsG1'),[W,H]=svgSize(g1);if(W){const cx=W*0.4,cy=H*0.68,k=Math.min(W/26,H/15);const ar=(v,c,l)=>`<line x1="${cx}" y1="${cy}" x2="${cx+v[0]*k}" y2="${cy-v[1]*k}" stroke="${c}" stroke-width="4"/><circle cx="${cx+v[0]*k}" cy="${cy-v[1]*k}" r="5" fill="${c}"/><text x="${cx+v[0]*k+6}" y="${cy-v[1]*k-6}" font-size="12" font-weight="700" fill="${c}">${l}</text>`;
  g1.innerHTML=`<line x1="${cx-12*k}" y1="${cy}" x2="${cx+12*k}" y2="${cy}" stroke="#eef1f4"/><line x1="${cx}" y1="${cy-12*k}" x2="${cx}" y2="${cy+12*k}" stroke="#eef1f4"/>`+ar([3,4],'#d4691f','A')+ar(B,'#1f7a8c','B')}
 const g2=$('wordsG2'),[W2,H2]=svgSize(g2);if(W2){const cx=W2/2,cy=H2/2,R=Math.min(W2,H2)*0.36;let g=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#c9ced6"/>`;for(let m=0;m<12;m++){const t=m*30*D2R;g+=`<text x="${cx+(R+14)*Math.cos(t)}" y="${cy-(R+14)*Math.sin(t)+4}" font-size="10" text-anchor="middle" fill="#5d6676">${m}</text>`}
  [[i,'#d4691f','단어 1'],[j,'#1f7a8c','단어 2']].forEach(([p,c,l])=>{const t=p*30*D2R;g+=`<line x1="${cx}" y1="${cy}" x2="${cx+R*Math.cos(t)}" y2="${cy-R*Math.sin(t)}" stroke="${c}" stroke-width="5"/><text x="${cx+R*0.55*Math.cos(t)+5}" y="${cy-R*0.55*Math.sin(t)-5}" font-size="12" font-weight="700" fill="${c}">${l}</text>`});g2.innerHTML=g}
 score('words',[['A–B 코사인',cs.toFixed(3),'방향만 비교',Math.abs(cs-0.96)<=0.005&&L>=8?'ok':''],['A–B 거리',dist.toFixed(2),'길이 차이에도 흔들림'],['RoPE 자리 차이',(j-i)+'자리',`${(j-i)*30}°`],['RoPE 겹침 점수',rp.toFixed(3),'cos(30° × 차이)',Math.abs(rp)<0.01?'ok':'']]);
 const n=mission('words',[Math.abs(cs-0.96)<=0.005&&L>=8,Math.abs(cs)<=0.02,Math.abs(rp)<0.01]);
 say('words',`코사인 ${cs.toFixed(3)}, 거리 ${dist.toFixed(2)}예요. 단어 두 개는 ${j-i}자리 떨어져서 겹침 ${rp.toFixed(3)}이에요.`,`코사인 0.96은 각도 약 16°예요. 겹침 0은 자리 차이 3이나 9!`,
  L>=8&&cs>0.9?'거리는 꽤 먼데 코사인은 높지? 검색에선 어느 쪽을 믿어야 할까?':'단어 두 개를 함께 한 자리씩 옮겨도 겹침 점수가 그대로인지 확인해 봐.',
  doc(n,'뜻은 방향으로, 순서는 회전 각도 차이로 담습니다.'))};
['wdA','wdL','wdI','wdJ'].forEach(id=>bindT('words',id,v=>id==='wdA'?v+'°':id==='wdL'?v.toFixed(1):v+'번'));
// ===== 학습 걸음 =====
let stWd=false;$('stOff').onclick=()=>{stWd=false;press(['stOff','stOn'],'stOff');touched.steps=true;DRAW.steps()};$('stOn').onclick=()=>{stWd=true;press(['stOff','stOn'],'stOn');touched.steps=true;DRAW.steps()};
const sim=(r0,lr,wd)=>{let th=0,r=r0;const A=[0],Rr=[r0];for(let n=1;n<=300;n++){th+=lr/(r*r);r*=1-wd;A.push(th);Rr.push(r);if(th>=0.7854)return{n,A,Rr}}return{n:Infinity,A,Rr}};
DRAW.steps=()=>{const lr=+$('stLr').value,r0=+$('stR').value,S0=sim(r0,lr,0),S1=sim(r0,lr,0.05),S=stWd?S1:S0;
 const g1=$('stepsG1'),[W,H]=svgSize(g1);if(W){const x0=34,x1=W-10,y0=14,y1=H-26,N=Math.min(120,Math.max(S0.A.length,S1.A.length)),X=n=>x0+n/N*(x1-x0),Y=v=>y1-Math.min(v,1.2)/1.2*(y1-y0);
  let g=axis(x0,y0,x1,y1)+`<line x1="${x0}" y1="${Y(0.7854)}" x2="${x1}" y2="${Y(0.7854)}" stroke="#d4691f" stroke-dasharray="5 4"/><text x="${x1}" y="${Y(0.7854)-4}" font-size="11" text-anchor="end" fill="#d4691f">45°</text>`;
  g+=line(S0.A.slice(0,N+1).map((v,n)=>[X(n),Y(v)]),'#9aa3b0',2.5)+line(S1.A.slice(0,N+1).map((v,n)=>[X(n),Y(v)]),'#1e8a4c',2.5);
  g+=`<text x="${x0+6}" y="${y0+12}" font-size="11" fill="#9aa3b0">회색 = 감쇠 끔</text><text x="${x0+6}" y="${y0+26}" font-size="11" fill="#1e8a4c">초록 = 감쇠 켬</text><text x="${x1}" y="${y1+16}" font-size="11" text-anchor="end">${N}걸음</text>`;g1.innerHTML=g}
 const g2=$('stepsG2'),[W2,H2]=svgSize(g2);if(W2){const x0=34,x1=W2-10,y0=14,y1=H2-26,N=Math.min(120,S.Rr.length-1)||1,X=n=>x0+n/N*(x1-x0),Y=v=>y1-v/12*(y1-y0);
  g2.innerHTML=axis(x0,y0,x1,y1)+line(S.Rr.slice(0,N+1).map((v,n)=>[X(n),Y(v)]),'#24345c',3)+`<text x="${x0+6}" y="${y0+12}" font-size="11">가중치 길이 (위 끝 12)</text>`}
 const fmtN=v=>isFinite(v)?v+'걸음':'300걸음 넘음';
 score('steps',[['45°까지 (감쇠 끔)',fmtN(S0.n),`한 걸음 ${(lr/r0/r0*R2D).toFixed(2)}°`,!stWd&&S0.n<=20?'ok':''],['45°까지 (감쇠 켬)',fmtN(S1.n),'길이가 줄며 빨라짐',stWd&&S1.n<=30?'ok':''],['첫 걸음 기울기',(1/r0).toFixed(3),'1/r'],['마지막 길이',S.Rr[Math.min(S.Rr.length-1,isFinite(S.n)?S.n:300)].toFixed(2),stWd?'감쇠 켬':'감쇠 끔']]);
 const n=mission('steps',[!stWd&&Math.abs(lr-1)<0.01&&S0.n<=20,!stWd&&r0===10&&S0.n<=20,stWd&&r0===10&&Math.abs(lr-1)<0.01&&S1.n<=30]);
 say('steps',`처음 길이 ${r0}, 학습률 ${lr}에서 45°까지 ${fmtN(S.n)}이에요.`,`한 걸음 각도는 학습률 ÷ r²! 길이 ${r0}이면 ${(lr/r0/r0).toFixed(4)} rad예요.`,
  stWd?'감쇠로 길이가 줄면 걸음이 커져. 하지만 길이가 너무 작아지면 걸음이 지나치게 커질 수도 있어.':'학습률만 올리면 해결될까? 길이를 줄이는 것과 무엇이 다른지 그림 ②를 봐.',
  doc(n,'방향만 보는 모델에서는 "학습률"과 "가중치 길이"가 함께 실제 속도를 정합니다.'))};
['stLr','stR'].forEach(id=>bindT('steps',id,v=>v.toFixed(1)));
// ===== 확률·관계망 =====
let pr2=false;$('pr1').onclick=()=>{pr2=false;press(['pr1','pr2'],'pr1');touched.prob=true;DRAW.prob()};$('pr2').onclick=()=>{pr2=true;press(['pr1','pr2'],'pr2');touched.prob=true;DRAW.prob()};
const PE=[[0,1],[0,2],[0,3],[1,4]],PP=[[0.5,0.5],[0.22,0.25],[0.78,0.25],[0.5,0.85],[0.12,0.62]];let PV=[5,3,3,3,9],pSt=0;
const pNb=i=>PE.filter(e=>e.includes(i)).map(e=>e[0]===i?e[1]:e[0]);
$('prStep').onclick=()=>{const a=+$('prA').value,L=PV.map((v,i)=>{const n=pNb(i);return n.reduce((p,q)=>p+PV[q],0)/n.length-v});PV=PV.map((v,i)=>v+a*L[i]);pSt++;touched.prob=true;DRAW.prob()};
$('prReset').onclick=()=>{PV=[5,3,3,3,9];pSt=0;DRAW.prob()};
DRAW.prob=()=>{const s=+$('prS').value,dens=pr2?1/(s*s):1/s,sp=Math.max(...PV)-Math.min(...PV);
 const g1=$('probG1'),[W,H]=svgSize(g1);if(W){const base=H-30,u=Math.min((W-50)/3.2,(H-50)/2.2);let g=`<line x1="20" y1="${base}" x2="${W-10}" y2="${base}" stroke="#1c2230"/><rect x="30" y="${base-u*(pr2?1:1)}" width="${u}" height="${u}" fill="none" stroke="#9aa3b0" stroke-dasharray="5 4"/>`;
  if(!pr2)g+=`<rect x="30" y="${base-u*dens}" width="${u*s}" height="${u*dens}" fill="#1f7a8c" opacity=".6"/><text x="${30+u*s/2}" y="${base-u*dens-6}" font-size="12" font-weight="700" text-anchor="middle" fill="#1f7a8c">밀도 ${dens.toFixed(3)}</text>`;
  else{const cs=u*0.55;g+=`<rect x="30" y="${base-cs*s}" width="${cs*s}" height="${cs*s}" fill="#1f7a8c" opacity="${Math.max(0.12,Math.min(0.9,dens*0.6))}"/><text x="${30+cs*s/2}" y="${base-cs*s/2}" font-size="13" font-weight="700" text-anchor="middle">밀도 ${dens.toFixed(3)}</text>`}g1.innerHTML=g}
 const g2=$('probG2'),[W2,H2]=svgSize(g2);if(W2){let g='';PE.forEach(([a,b])=>g+=`<line x1="${PP[a][0]*W2}" y1="${PP[a][1]*H2}" x2="${PP[b][0]*W2}" y2="${PP[b][1]*H2}" stroke="#9aa3b0" stroke-width="4"/>`);
  PV.forEach((v,i)=>{const t=Math.max(0,Math.min(1,(v-3)/6));g+=`<circle cx="${PP[i][0]*W2}" cy="${PP[i][1]*H2}" r="24" fill="rgb(${Math.round(36+t*176)},${Math.round(52+t*53)},${Math.round(92-t*61)})"/><text x="${PP[i][0]*W2}" y="${PP[i][1]*H2+5}" font-size="13" font-weight="700" text-anchor="middle" fill="#fff">${v.toFixed(2)}</text>`});g2.innerHTML=g}
 score('prob',[['늘어난 배수',(pr2?s*s:s).toFixed(2)+'배',pr2?'가로 × 세로':'가로'],['밀도',dens.toFixed(3),'전체 확률은 늘 1',(Math.abs(dens-0.5)<0.005&&!pr2)||(Math.abs(dens-0.25)<0.005&&pr2)?'ok':''],['섞은 횟수',pSt+'번',`α = ${(+$('prA').value).toFixed(1)}`],['다섯 값 가장 큰 차이',sp.toFixed(2),sp<0.3?'지나친 섞임':'',sp<0.3?'warn':'']]);
 const n=mission('prob',[!pr2&&Math.abs(dens-0.5)<0.005,pr2&&Math.abs(dens-0.25)<0.005,sp<0.3]);
 say('prob',`늘림 ${s}배${pr2?'(2축)':''}라서 밀도는 ${dens.toFixed(3)}이에요. 관계망은 ${pSt}번 섞어 가장 큰 차이가 ${sp.toFixed(2)}예요.`,`밀도 × 늘어난 배수 = 1, 언제나! 관계망은 섞을 때마다 차이가 줄어요.`,
  sp<0.3?'다 비슷해졌어. 추천 시스템이라면 모든 사람에게 같은 걸 추천하게 될 거야.':'2축으로 바꾸면 같은 늘림 배수에서 밀도가 얼마나 더 묽어지는지 봐.',
  doc(n,'늘린 만큼 나누고, 섞는 횟수는 적당히. 둘 다 "전체를 지키며 자리마다 고치는" 계산입니다.'))};
$('prS').addEventListener('input',()=>touched.prob=true);bindSl('prS',v=>v.toFixed(1)+'배',()=>DRAW.prob())();bindSl('prA',v=>v.toFixed(1),()=>DRAW.prob())();
KEYS.forEach(k=>obs($(k+'G1'),()=>{if(!$('tab-'+k).hidden)DRAW[k]()}));
const h0=(location.hash||'').slice(1);openTab(KEYS.includes(h0)?h0:'sales');
"""

PACK_DATA = {"page": "벡터 분석 랩 3부 복습 대시보드 — AI 실험실", "author": "안상선 ((주)M-Robo)",
             "url": "https://adminmrobo.github.io/vector_analysis_lab/dash_03.html",
             "scenes": {"sales": "주기 특성", "words": "코사인 유사도·RoPE", "steps": "1/r² 학습 걸음·가중치 감쇠", "prob": "야코비안 밀도·GNN 섞기"},
             "missions": 12,
             "cite": "안상선 (2026). 벡터 분석 랩 3부 복습 대시보드. https://adminmrobo.github.io/vector_analysis_lab/dash_03.html"}

if __name__ == '__main__':
    n = page('dash_03.html', '벡터 분석 랩 3부 대시보드 — AI 실험실',
             '판매 예측·단어 나침반·학습 걸음·확률과 관계망 네 실험에서 주기 특성, 코사인, RoPE, 1/r² 걸음, 밀도 고치기, GNN 섞기를 직접 돌려 봅니다. 미션 12개.',
             'assets/og/03.webp', body(), PAGE_JS, PACK_DATA, ['주기 특성', '임베딩', 'RoPE', '학습 속도', '흐름 모델', 'GNN'])
    print('dash03 bytes', n)
