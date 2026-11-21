# -*- coding: utf-8 -*-
"""1부 복습 대시보드 — 생활 장면 시뮬레이터 (탭 4개, 미션 12개)"""
from common import *

TABS = [('pizza', '피자 가게·달력', '방 1·2'), ('globe', '지구 배송센터', '방 3·4'),
        ('flow', '역과 환전소', '방 5·6'), ('photo', '사진 윤곽선', '방 7')]

def sl2(i, l, mn, mx, st, v):
    return (f'<div class="sl"><label for="{i}">{l}</label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}">'
            f'<output id="{i}o"></output></div>')

def scene(key, situ, env, me, cap1, cap2, missions, links):
    m = ''.join(f'<li id="{key}m{i+1}">{t}</li>' for i, t in enumerate(missions))
    return f"""
<div class="ctab" id="tab-{key}" role="tabpanel" aria-labelledby="tb-{key}">
<div class="easy"><b>상황</b> {situ}</div>
<div class="dash">
<div class="panel" aria-label="조작판"><h3>조작판</h3>
<div class="grp env"><b>환경 (주어진 조건)</b>{env}</div>
<div class="grp me"><b>내 결정</b>{me}</div>
</div>
<div style="min-width:0">
<div class="score" id="{key}Score" aria-live="polite"></div>
<div class="figs">
<div><div class="fig"><svg id="{key}G1" role="img" aria-label="{cap1}"></svg></div><p class="cap">그림 ① {cap1}</p></div>
<div><div class="fig"><svg id="{key}G2" role="img" aria-label="{cap2}"></svg></div><p class="cap">그림 ② {cap2}</p></div>
</div>
{talk(T('asst/E07', f'<span id="{key}Haru">…</span>'), T('robo/E09', f'<span id="{key}Robo">…</span>'),
      T('fly/E08', f'<span id="{key}Fly">…</span>'), T('doc/E08', f'<span id="{key}Doc">…</span>'))}
</div></div>
<h3>미션</h3><ol class="missions">{m}</ol>
<p style="font-size:14px">배운 곳 다시 보기: {links}</p>
</div>"""

def body():
    for k in ['x1/E15', 'x2/E02', 'x3/E04', 'x1/E01', 'x2/E16', 'x3/E01']:
        USED.append(k)
    tabs = ''.join(f'<button class="btn" role="tab" id="tb-{k}" aria-controls="tab-{k}" aria-selected="false">{t} <span style="font-size:12px;opacity:.75">{r}</span></button>' for k, t, r in TABS)
    h = f"""
<header class="hero"><div class="wrap">
<div class="wing">벡터 분석 랩 · 1부 복습 대시보드</div>
<h1>생활 장면 시뮬레이터<br>피자 가게에서 사진 앱까지</h1>
<p class="sub">1부 일곱 방에서 배운 것을 네 개의 가상 현장에서 직접 운영해 봅니다. 초록은 주어진 조건, 파랑은 여러분의 결정입니다. 현장마다 미션 3개, 모두 12개입니다.</p>
<div class="by">{AUTHOR}</div>
</div></header>
<main class="wrap">
<section>
{talk(T('asst/E20', '복습은 제가 진행해요… 성적표 숫자는 제가 읽고, 계산은 주판봇이, 함정은 초파리 연구원이 알려 줄 거예요.'))}
{crowd('방청석', [('x1/E15', '<span id="xs1">(조마조마)</span>'), ('x2/E02', '<span id="xs2">(꿀꺽)</span>'), ('x3/E04', '<span id="xs3">(…!)</span>')])}
<div class="tabs" role="tablist" aria-label="현장 고르기">{tabs}</div>
<p id="allSum" style="font-weight:700" aria-live="polite"></p>
"""
    h += scene('pizza',
               '피자 가게 사장님이 큰 판(반지름 15 cm)을 팔면서도, 손님에게 작은 판(10 cm) 45° 조각과 "같은 만큼"을 주고 싶어 합니다. 그런데 "같은 만큼"이 테두리 빵 길이일까요, 조각 넓이일까요? 옆에서는 달력 데이터를 정리합니다.',
               sl2('pzR', '큰 판 반지름', 12, 20, 1, 15) + '<p style="font-size:13px;margin:4px 0 0;color:var(--mute)">작은 판: 반지름 10 cm, 45° 조각</p>',
               sl2('pzA', '큰 판 조각 각도', 5, 90, 1, 45) + sl2('pzM1', '첫째 달', 1, 12, 1, 6) + sl2('pzM2', '둘째 달', 1, 12, 1, 7),
               '작은 판 45° 조각과 큰 판 조각', '큰 판 조각 각도에 따른 테두리 길이(주황)·넓이(남색)와 목표선',
               ['<b>테두리 맞추기:</b> 큰 판 조각의 테두리 길이를 작은 판 45° 조각(7.85 cm)과 같게 만드세요. (±0.15 cm)',
                '<b>넓이 맞추기:</b> 이번엔 조각 넓이를 작은 판 45° 조각(39.3 cm²)과 같게 만드세요. 각도가 테두리 때와 같나요? (±1 cm²)',
                '<b>달력 함정:</b> 숫자 줄 거리는 10 이상인데 시계판 거리는 0.6 이하인 두 달을 고르세요.'],
               '<a href="01_everyday.html#room-1">방 1 피자 테두리</a> · <a href="01_everyday.html#room-2">방 2 12월과 1월</a> · <a href="00_orientation.html#room-b">0편 방 B 한 걸음 상자</a>')
    h += scene('globe',
               '배송센터를 어느 위도에 세울지 검토합니다. 트럭이 동쪽으로 달린 거리가 경도 몇 도인지, 그 지역 1°×1° 구역이 실제로 얼마나 넓은지, 벽에 붙은 세계 지도가 그 땅을 얼마나 크게 보여 주는지 알아야 합니다.',
               sl2('glLat', '센터 위도', 0, 85, 0.5, 37.5) + '<div class="btns"><button class="btn" data-gl="0">적도</button><button class="btn" data-gl="37.5">서울</button><button class="btn" data-gl="60">60°</button><button class="btn" data-gl="72">그린란드쯤</button></div>',
               sl2('glKm', '동쪽 운행 거리', 0, 300, 0.5, 100),
               '옆에서 본 지구와 그 위도에서 도는 원', '위도별 경도 1도 길이(청록)와 지도 부풀림(주황), 지금 위도 표시',
               ['<b>절반 지점:</b> 경도 1도 길이가 적도(111.2 km)의 절반이 되는 위도를 찾으세요. (±0.5°)',
                '<b>서울 트럭:</b> 위도를 서울(37.5°)에 두고, 트럭이 경도로 정확히 1°만큼 동쪽으로 가도록 운행 거리를 맞추세요. (±0.012°)',
                '<b>지도의 착시:</b> 흔한 세계 지도가 땅을 10배 넘게 부풀려 보여 주는 위도를 찾으세요.'],
               '<a href="01_everyday.html#room-3">방 3 경도 1도</a> · <a href="01_everyday.html#room-4">방 4 그린란드</a>')
    h += scene('flow',
               '도시 교통팀과 환전소를 함께 봅니다. 세 역(A 업무지구·B 주거지·C 환승역)의 한 시간 승하차로 어느 역이 샘이고 배수구인지, 도시 전체로는 합이 맞는지 확인합니다. 환전소에서는 세 환율이 한 바퀴 돌아 맞는지 봅니다(가상 값).',
               '<div class="btns" role="group" aria-label="시간대"><button class="btn" id="flAm" aria-pressed="true">출근 시간</button><button class="btn" id="flPm" aria-pressed="false">퇴근 시간</button></div>'
               '<p style="font-size:13px;margin:6px 0;color:var(--mute)" id="flEnvTxt"></p>'
               '<div class="btns" role="group" aria-label="환율 날짜"><button class="btn" id="flD1" aria-pressed="true">오늘 환율</button><button class="btn" id="flD2" aria-pressed="false">다음 날 환율</button></div>',
               sl2('flOut', 'A역 내린 사람', 0, 2000, 50, 1200) + sl2('flIn', 'A역 탄 사람', 0, 2000, 50, 800) + sl2('flKj', '100엔 = 원', 850, 1050, 0.5, 950),
               '세 역의 순유출(+샘, −배수구)과 도시 전체 합', '원·달러·엔 한 바퀴와 남는 돈',
               ['<b>배수구 만들기:</b> A역을 배수구(−)로 만드세요.',
                '<b>도시 전체 균형:</b> 세 역의 발산을 모두 더하면 0이 되도록 A역 승하차를 맞추세요(도시 밖으로 나가는 사람은 없다고 봅니다). (±10명)',
                '<b>회전 0:</b> "다음 날 환율"을 고르고, 한 바퀴 돌아도 남는 돈이 없도록 100엔 값을 맞추세요. (±1원)'],
               '<a href="01_everyday.html#room-5">방 5 지하철역</a> · <a href="01_everyday.html#room-6">방 6 환전 한 바퀴</a>')
    h += scene('photo',
               '사진 앱의 "윤곽선 찾기" 기능을 조율합니다. 밝기가 주변 평균과 기준값 이상 다르면 윤곽선으로 표시합니다. 사진에 잡음(자글자글한 얼룩)이 섞이면 잡음도 튀는 점처럼 보입니다.',
               sl2('phN', '잡음 세기', 0, 30, 5, 0),
               sl2('phT', '윤곽 기준값', 0, 150, 1, 60),
               '잡음이 섞인 밝기 사진(16×16)', '찾은 윤곽선: 초록 = 맞힘, 빨강 = 잘못 찾음, 회색 = 놓침',
               ['<b>깨끗한 사진:</b> 잡음 0에서 진짜 테두리 70개를 모두 찾고, 잘못 찾은 점은 0개로 만드세요.',
                '<b>잡음 20:</b> 잡음을 20으로 올리고, 잘못 찾은 점이 0개가 되는 기준값을 찾으세요. 놓친 점은 몇 개인가요?',
                '<b>균형 잡기:</b> 잡음 10에서 진짜 테두리의 90% 이상을 찾으면서 잘못 찾은 점은 0개로 만드세요.'],
               '<a href="01_everyday.html#room-7">방 7 사진 윤곽선</a> · <a href="dash_00.html">0편 대시보드(라플라시안 비교표)</a>')
    h += f"""
<div class="limit" style="margin-top:24px"><b>이 대시보드의 한계</b> 모든 숫자는 교육용 예시입니다. 지구는 반지름 6,371 km 공으로, 1°×1° 땅은 작은 네모로 어림했습니다. 환율은 가상 값이며 수수료를 빼고 계산했습니다. 투자·경영 권고가 아닙니다.</div>
</section>
<section id="outro">
<div class="nextp"><a href="01_everyday.html"><b>← 1부 본문</b>같은 1도, 다른 길이</a><a href="02_economy.html"><b>다음 →</b>2부 경제·금융</a></div>
</section>
<section id="export"><h2>온톨로지·서지 꾸러미</h2>
<div class="btns"><button class="btn" id="copyPack">꾸러미 복사</button><span id="copyMsg" style="align-self:center;font-size:14px;color:var(--mute)" aria-live="polite"></span></div>
<pre id="pack"></pre></section>
</main>
<footer><div class="wrap">{AUTHOR}<br>원자료: @eeanimation 「Vector Analysis」 4장. 캐릭터: 연구실 식구(fruitfly-lab-expressions). 수치는 교육용 예시이며 투자·경영 권고가 아닙니다.</div></footer>
"""
    return h

PAGE_JS = r"""
const touched={pizza:false,globe:false,flow:false,photo:false};const DONE={pizza:[0,0,0],globe:[0,0,0],flow:[0,0,0],photo:[0,0,0]};
const say=(k,h,r,f,d)=>{$(k+'Haru').textContent=h;$(k+'Robo').textContent=r;$(k+'Fly').textContent=f;$(k+'Doc').textContent=d};
const score=(k,items)=>{$(k+'Score').innerHTML=items.map(([l,v,s,c])=>`<div class="${c||''}"><span>${l}</span><b>${v}</b><small>${s||''}</small></div>`).join('')};
function mission(k,conds){if(touched[k])conds.forEach((c,i)=>{if(c)DONE[k][i]=1});DONE[k].forEach((d,i)=>$(k+'m'+(i+1)).classList.toggle('done',!!d));
 const n=Object.values(DONE).flat().filter(Boolean).length;$('allSum').textContent=`전체 미션 ${n} / 12 통과`+(n===12?' — 1부 복습 끝! 2부에서 만나요.':'');
 const s=n===12?['(짝짝짝)','(끄덕끄덕)','(반짝반짝)']:n>=4?['(휴…)','(오!)','(두근)']:['(조마조마)','(꿀꺽)','(…!)'];['xs1','xs2','xs3'].forEach((id,i)=>$(id).textContent=s[i]);
 return DONE[k].filter(Boolean).length}
const doc=(n,hint)=>n===3?'이 현장 미션 셋 모두 통과. 다른 현장 탭도 열어 보세요.':n?`미션 ${n}개 통과. ${hint}`:hint;
const line=(pts,c,w=2.5)=>`<polyline points="${pts.map(p=>p.join(',')).join(' ')}" fill="none" stroke="${c}" stroke-width="${w}"/>`;
const axis=(x0,y0,x1,y1)=>`<line x1="${x0}" y1="${y1}" x2="${x1}" y2="${y1}" stroke="#1c2230"/><line x1="${x0}" y1="${y0}" x2="${x0}" y2="${y1}" stroke="#1c2230"/>`;
// ========== 탭 ==========
const KEYS=['pizza','globe','flow','photo'];
function openTab(k){KEYS.forEach(t=>{$('tab-'+t).hidden=t!==k;$('tb-'+t).setAttribute('aria-selected',t===k)});try{history.replaceState(null,'','#'+k)}catch(e){}DRAW[k]()}
KEYS.forEach(k=>$('tb-'+k).onclick=()=>openTab(k));
const DRAW={};
// ========== 피자·달력 ==========
DRAW.pizza=()=>{const R=+$('pzR').value,A=+$('pzA').value,m1=+$('pzM1').value,m2=+$('pzM2').value;
 const sc=10*Math.PI/4,sa=0.5*100*Math.PI/4,rad=A*D2R,bc=R*rad,ba=0.5*R*R*rad;
 const dl=Math.abs(m1-m2),dm=Math.min(dl,12-dl),ch=2*Math.sin(dm*15*D2R);
 const g1=$('pizzaG1'),[W,H]=svgSize(g1);if(W){const k=Math.min(W/2/22,(H-60)/2/21);
  const pz=(cx,cy,r,ang,col,lab)=>{const a0=-90*D2R,a1=a0+ang*D2R,Rr=r*k;return`<circle cx="${cx}" cy="${cy}" r="${Rr}" fill="#fde0aa" stroke="#d4691f" stroke-width="4"/><path d="M${cx},${cy} L${cx+Rr*Math.cos(a0)},${cy+Rr*Math.sin(a0)} A${Rr},${Rr} 0 ${ang>180?1:0} 1 ${cx+Rr*Math.cos(a1)},${cy+Rr*Math.sin(a1)} Z" fill="#f0a050" stroke="${col}" stroke-width="3"/><text x="${cx}" y="${cy+Rr+22}" font-size="12" text-anchor="middle">${lab}</text>`};
  g1.innerHTML=pz(W*0.27,H*0.45,10,45,'#24345c','작은 판 10 cm · 45°')+pz(W*0.72,H*0.45,R,A,'#c0392b',`큰 판 ${R} cm · ${A}°`)}
 const g2=$('pizzaG2'),[W2,H2]=svgSize(g2);if(W2){const x0=44,x1=W2-12,y0=14,y1=H2-30,X=a=>x0+(a-5)/(85)*(x1-x0);const mc=20*Math.PI/2,ma=0.5*400*Math.PI/2;
  const Yc=v=>y1-(v/Math.max(mc,1))*(y1-y0)*0.95,Ya=v=>y1-(v/ma)*(y1-y0)*0.95;
  let g=axis(x0,y0,x1,y1);const pc=[],pa=[];for(let a=5;a<=90;a++){pc.push([X(a),Yc(R*a*D2R)]);pa.push([X(a),Ya(0.5*R*R*a*D2R)])}
  g+=`<line x1="${x0}" y1="${Yc(sc)}" x2="${x1}" y2="${Yc(sc)}" stroke="#d4691f" stroke-dasharray="5 4"/><text x="${x1}" y="${Yc(sc)-4}" font-size="11" text-anchor="end" fill="#d4691f">목표 테두리 7.85</text>`;
  g+=`<line x1="${x0}" y1="${Ya(sa)}" x2="${x1}" y2="${Ya(sa)}" stroke="#24345c" stroke-dasharray="5 4"/><text x="${x1}" y="${Ya(sa)+13}" font-size="11" text-anchor="end" fill="#24345c">목표 넓이 39.3</text>`;
  g+=line(pc,'#d4691f')+line(pa,'#24345c')+`<line x1="${X(A)}" y1="${y0}" x2="${X(A)}" y2="${y1}" stroke="#c0392b" stroke-width="2"/>`;
  [5,30,45,60,90].forEach(a=>g+=`<text x="${X(a)}" y="${y1+16}" font-size="11" text-anchor="middle">${a}°</text>`);g2.innerHTML=g}
 score('pizza',[['작은 판 45° 테두리',sc.toFixed(2)+' cm','넓이 '+sa.toFixed(1)+' cm²'],['큰 판 조각 테두리',bc.toFixed(2)+' cm',`${R} × ${rad.toFixed(3)} rad`,Math.abs(bc-sc)<=0.15?'ok':''],
  ['큰 판 조각 넓이',ba.toFixed(1)+' cm²','½ × r² × 각도',Math.abs(ba-sa)<=1?'ok':''],[`${m1}월–${m2}월`,`줄 ${dl} · 시계 ${ch.toFixed(2)}`,'숫자 줄 vs 시계판',dl>=10&&ch<=0.6?'ok':'']]);
 const n=mission('pizza',[Math.abs(bc-sc)<=0.15,Math.abs(ba-sa)<=1,dl>=10&&ch<=0.6]);
 say('pizza',`큰 판 ${A}° 조각은 테두리 ${bc.toFixed(2)} cm, 넓이 ${ba.toFixed(1)} cm²예요. 작은 판은 ${sc.toFixed(2)} cm, ${sa.toFixed(1)} cm²고요.`,
  `테두리는 반지름에 비례, 넓이는 반지름의 제곱에 비례! 그래서 맞추는 각도가 달라요. 반지름 ${R}이면 테두리는 ${(45*10/R).toFixed(1)}°, 넓이는 ${(45*100/R/R).toFixed(1)}°.`,
  dl>=10&&ch>0.6?'숫자 줄로 멀다고 정말 먼 달일까? 시계판 거리도 같이 봐.':Math.abs(bc-sc)<=0.15&&Math.abs(ba-sa)>1?'테두리는 맞췄는데, 손님이 배부른 건 넓이 쪽 아닐까?':'각도 슬라이더를 천천히 움직이면서 그림 ②의 두 선이 목표선과 만나는 곳을 봐.',
  doc(n,'"같은 각도"는 같은 길이도, 같은 넓이도 아닙니다. 무엇을 같게 할지 먼저 정하세요.'))};
['pzR','pzA','pzM1','pzM2'].forEach(id=>{$(id).addEventListener('input',()=>touched.pizza=true);bindSl(id,v=>id==='pzR'?v+' cm':id==='pzA'?v+'°':v+'월',()=>DRAW.pizza())});
// ========== 지구 ==========
const E1=2*Math.PI*6371/360;
DRAW.globe=()=>{const lat=+$('glLat').value,km=+$('glKm').value,c=Math.cos(lat*D2R);const L=E1*c,dlon=L>1e-6?km/L:Infinity,area=E1*E1*c,inf=1/(c*c);
 const g1=$('globeG1'),[W,H]=svgSize(g1);if(W){const cx=W*0.45,cy=H*0.52,R=Math.min(W*0.36,H*0.42),la=lat*D2R,y=cy-R*Math.sin(la),hw=R*c;
  let g=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="#eef6fb" stroke="#24345c" stroke-width="3"/><line x1="${cx}" y1="${cy-R-10}" x2="${cx}" y2="${cy+R+10}" stroke="#5d6676" stroke-dasharray="4 4"/>`;
  g+=`<ellipse cx="${cx}" cy="${cy}" rx="${R}" ry="${R*0.12}" fill="none" stroke="#c9d4de"/><ellipse cx="${cx}" cy="${y}" rx="${Math.max(hw,.5)}" ry="${Math.max(hw*.12,.5)}" fill="none" stroke="#1f7a8c" stroke-width="3"/>`;
  const arc=Math.min(Math.PI*0.9,dlon*D2R);g+=`<path d="M${cx+hw},${y} A${hw},${hw*0.12} 0 0 1 ${cx+hw*Math.cos(arc)},${y+hw*0.12*Math.sin(arc)}" fill="none" stroke="#c0392b" stroke-width="6"/>`;
  g+=`<line x1="${cx}" y1="${y}" x2="${cx+hw}" y2="${y}" stroke="#d4691f" stroke-width="4"/><text x="${cx+hw/2}" y="${y+22}" font-size="12" text-anchor="middle" fill="#d4691f" font-weight="700">도는 원 반지름 ${fmt(6371*c)} km</text>`;
  g+=`<text x="${cx}" y="${cy-R-14}" font-size="12" text-anchor="middle" fill="#5d6676">북극</text>`;g1.innerHTML=g}
 const g2=$('globeG2'),[W2,H2]=svgSize(g2);if(W2){const x0=40,x1=W2-36,y0=14,y1=H2-30,X=a=>x0+a/85*(x1-x0),Y=v=>y1-v/115*(y1-y0),Yi=v=>y1-Math.min(v,30)/30*(y1-y0);
  let g=axis(x0,y0,x1,y1);const p1=[],p2=[];for(let a=0;a<=85;a+=0.5){p1.push([X(a),Y(E1*Math.cos(a*D2R))]);p2.push([X(a),Yi(1/Math.cos(a*D2R)**2)])}
  g+=line(p1,'#1f7a8c',3)+line(p2,'#d4691f',2.5)+`<line x1="${x0}" y1="${Yi(10)}" x2="${x1}" y2="${Yi(10)}" stroke="#d4691f" stroke-dasharray="4 4"/><text x="${x1}" y="${Yi(10)-4}" font-size="11" text-anchor="end" fill="#d4691f">부풀림 10배</text>`;
  g+=`<line x1="${X(lat)}" y1="${y0}" x2="${X(lat)}" y2="${y1}" stroke="#c0392b" stroke-width="2"/><circle cx="${X(lat)}" cy="${Y(L)}" r="5" fill="#1f7a8c"/><circle cx="${X(lat)}" cy="${Yi(inf)}" r="5" fill="#d4691f"/>`;
  [0,30,60,85].forEach(a=>g+=`<text x="${X(a)}" y="${y1+16}" font-size="11" text-anchor="middle">${a}°</text>`);
  g+=`<text x="${x0+4}" y="${y0+10}" font-size="11" fill="#1f7a8c">경도 1도 (km, 위 끝 115)</text><text x="${x1+30}" y="${y0+10}" font-size="11" text-anchor="end" fill="#d4691f">부풀림 (위 끝 30배)</text>`;g2.innerHTML=g}
 score('globe',[['경도 1도 길이',L.toFixed(1)+' km','111.2 × cos(위도)',Math.abs(lat-60)<=0.5?'ok':''],['동쪽 운행 → 경도',isFinite(dlon)?dlon.toFixed(3)+'°':'—',`${km} km ÷ ${L.toFixed(1)} km`,Math.abs(lat-37.5)<=0.5&&Math.abs(dlon-1)<=0.012?'ok':''],
  ['1°×1° 땅 넓이',fmt(area)+' km²','적도 12,364 km² × cos'],['세계 지도 부풀림',inf.toFixed(1)+'배','1 ÷ cos²(위도)',inf>=10?'ok':inf>=4?'warn':'']]);
 const n=mission('globe',[Math.abs(lat-60)<=0.5,Math.abs(lat-37.5)<=0.5&&Math.abs(dlon-1)<=0.012,inf>=10]);
 say('globe',`위도 ${lat}°에서 경도 1도는 ${L.toFixed(1)} km예요. 트럭이 ${km} km 가면 경도로 ${isFinite(dlon)?dlon.toFixed(3):'—'}° 움직여요.`,
  `1°×1° 땅은 ${fmt(area)} km², 적도의 ${(c*100).toFixed(0)}%! 그런데 세계 지도에선 ${inf.toFixed(1)}배로 보여요.`,
  lat>70?'여기선 경도 1도가 아주 짧아. 지도에서 큰 땅이라고 실제로 큰 건 아니야.':'위도를 올리면 그림 ②의 청록 선은 내려가고 주황 선은 올라가. 왜 반대로 움직일까?',
  doc(n,'남북 한 걸음은 어디서나 111.2 km, 동서 한 걸음만 cos(위도)배로 줄어듭니다. 이것이 h = r sinθ입니다.'))};
document.querySelectorAll('[data-gl]').forEach(b=>b.addEventListener('click',()=>{$('glLat').value=b.dataset.gl;$('glLat').dispatchEvent(new Event('input'))}));
['glLat','glKm'].forEach(id=>{$(id).addEventListener('input',()=>touched.globe=true);bindSl(id,v=>id==='glLat'?v+'°':v+' km',()=>DRAW.globe())});
// ========== 역·환전 ==========
let tod='am',day=1;const ENV={am:{B:-900,C:100,t:'출근 시간: B역(주거지) −900명, C역(환승역) +100명'},pm:{B:900,C:-100,t:'퇴근 시간: B역(주거지) +900명, C역(환승역) −100명'}};
const RATES={1:[1400,150],2:[1450,155]};
const setTod=t=>{tod=t;$('flAm').setAttribute('aria-pressed',t==='am');$('flPm').setAttribute('aria-pressed',t==='pm');touched.flow=true;DRAW.flow()};
const setDay=d=>{day=d;$('flD1').setAttribute('aria-pressed',d===1);$('flD2').setAttribute('aria-pressed',d===2);touched.flow=true;DRAW.flow()};
$('flAm').onclick=()=>setTod('am');$('flPm').onclick=()=>setTod('pm');$('flD1').onclick=()=>setDay(1);$('flD2').onclick=()=>setDay(2);
DRAW.flow=()=>{const o=+$('flOut').value,i=+$('flIn').value,kj=+$('flKj').value,e=ENV[tod];$('flEnvTxt').textContent=e.t;
 const A=o-i,sum=A+e.B+e.C;const[u,j]=RATES[day];const won=1400/u*j/100*kj,pr=won-1400,be=u/j*100;
 const g1=$('flowG1'),[W,H]=svgSize(g1);if(W){const vals=[['A역',A],['B역',e.B],['C역',e.C],['합계',sum]],mid=H*0.48,sc=(H*0.38)/2000,bw=Math.min(64,W/7);
  let g=`<line x1="16" y1="${mid}" x2="${W-10}" y2="${mid}" stroke="#1c2230"/><text x="18" y="16" font-size="11" fill="#d4691f">+ 샘 (동네로 내보냄)</text><text x="18" y="${H-24}" font-size="11" fill="#24345c">− 배수구 (빨아들임)</text>`;
  vals.forEach(([l,v],k)=>{const x=40+k*(W-60)/4,hgt=Math.min(Math.abs(v),2000)*sc,c=k===3?(Math.abs(v)<=10?'#1e8a4c':'#7a3fd6'):v>=0?'#d4691f':'#24345c';
   g+=`<rect x="${x}" y="${v>=0?mid-hgt:mid}" width="${bw}" height="${Math.max(1,hgt)}" fill="${c}" rx="3"/><text x="${x+bw/2}" y="${v>=0?mid-hgt-5:mid+hgt+14}" font-size="12" font-weight="700" text-anchor="middle" fill="${c}">${v>0?'+':''}${fmt(v)}</text><text x="${x+bw/2}" y="${H-6}" font-size="12" text-anchor="middle">${l}</text>`});g1.innerHTML=g}
 const g2=$('flowG2'),[W2,H2]=svgSize(g2);if(W2){const P=[[W2*0.18,H2*0.72],[W2*0.5,H2*0.16],[W2*0.82,H2*0.72]],nm=['원','달러','엔'],cl=['#24345c','#1f7a8c','#d4691f'];
  const vv=[`1,400 → ${fmt(won,1)}`,(1400/u).toFixed(3),(1400/u*j).toFixed(1)];let g='';
  [[0,1,'원 → 달러'],[1,2,'달러 → 엔'],[2,0,'엔 → 원']].forEach(([a,b,t])=>{const p=P[a],q=P[b],dx=q[0]-p[0],dy=q[1]-p[1],L=Math.hypot(dx,dy),ux=dx/L,uy=dy/L,s=[p[0]+ux*36,p[1]+uy*36],f=[q[0]-ux*38,q[1]-uy*38];
   g+=`<line x1="${s[0]}" y1="${s[1]}" x2="${f[0]}" y2="${f[1]}" stroke="#5d6676" stroke-width="2.5"/><polygon points="${f[0]},${f[1]} ${f[0]-10*ux+5*uy},${f[1]-10*uy-5*ux} ${f[0]-10*ux-5*uy},${f[1]-10*uy+5*ux}" fill="#5d6676"/><text x="${(s[0]+f[0])/2+uy*14}" y="${(s[1]+f[1])/2-ux*14+4}" font-size="11" text-anchor="middle" fill="#5d6676">${t}</text>`});
  P.forEach((p,k)=>g+=`<circle cx="${p[0]}" cy="${p[1]}" r="30" fill="#fff" stroke="${cl[k]}" stroke-width="3"/><text x="${p[0]}" y="${p[1]+5}" font-size="14" font-weight="700" text-anchor="middle" fill="${cl[k]}">${nm[k]}</text><text x="${p[0]}" y="${p[1]+48}" font-size="12" font-weight="700" text-anchor="middle">${vv[k]}</text>`);
  g+=`<text x="${W2/2}" y="${H2*0.56}" font-size="17" font-weight="900" text-anchor="middle" fill="${Math.abs(pr)<=1?'#1e8a4c':'#c0392b'}">한 바퀴 ${pr>=0?'+':''}${fmt(pr,1)}원</text>`;g2.innerHTML=g}
 score('flow',[['A역 발산',(A>0?'+':'')+fmt(A)+'명',A>0?'샘':A<0?'배수구':'균형',A<0?'ok':''],['세 역 합계',(sum>0?'+':'')+fmt(sum)+'명','들어온 만큼 나갔나',Math.abs(sum)<=10?'ok':'warn'],
  ['한 바퀴 남는 돈',(pr>=0?'+':'')+fmt(pr,1)+'원',`${day===1?'오늘':'다음 날'} 환율`,Math.abs(pr)<=1?'ok':''],['균형 100엔 값',fmt(be,1)+'원',`${fmt(u)} ÷ ${j} × 100`]]);
 const n=mission('flow',[A<0,Math.abs(sum)<=10,day===2&&Math.abs(pr)<=1]);
 say('flow',`A역은 ${A>0?'+':''}${fmt(A)}명, 세 역을 합하면 ${sum>0?'+':''}${fmt(sum)}명이에요. 환전은 한 바퀴에 ${pr>=0?'+':''}${fmt(pr,1)}원 남아요.`,
  `도시 전체 합이 0이 되려면 A역이 ${-(e.B+e.C)>0?'+':''}${fmt(-(e.B+e.C))}명이어야 해요! 균형 100엔 값은 ${fmt(be,1)}원.`,
  Math.abs(sum)>10?'세 역 합이 0이 아니면, 도시 어딘가에서 사람이 생기거나 사라진 거야. 그럴 리가?':Math.abs(pr)>1?'환율이 바뀌면 균형 100엔 값도 바뀌어. "다음 날" 버튼을 눌러 봐.':'좋아. 발산 합 0과 회전 0, 둘 다 "들어온 만큼 나간다"는 이야기야.',
  doc(n,'발산은 "솟아나나", 회전은 "돌면 남나"를 봅니다. 2부에서는 이것이 자금순환과 차익거래가 됩니다.'))};
['flOut','flIn','flKj'].forEach(id=>{$(id).addEventListener('input',()=>touched.flow=true);bindSl(id,v=>id==='flKj'?fmt(v,1)+'원':fmt(v)+'명',()=>DRAW.flow())});
// ========== 사진 ==========
const N=16,BASE=[];for(let y=0;y<N;y++){BASE.push([]);for(let x=0;x<N;x++)BASE[y].push(50)}
for(let y=4;y<=10;y++)for(let x=8;x<=13;x++)BASE[y][x]=200;BASE[3][3]=200;for(let x=2;x<=6;x++)BASE[13][x]=140;
const lapOf=a=>{const v=(x,y)=>(x<0||y<0||x>=N||y>=N)?50:a[y][x];return a.map((row,y)=>row.map((val,x)=>val-(v(x-1,y)+v(x+1,y)+v(x,y-1)+v(x,y+1))/4))};
const L0=lapOf(BASE),TRUE=new Set();L0.forEach((r,y)=>r.forEach((v,x)=>{if(Math.abs(v)>1e-9)TRUE.add(y*N+x)}));
const noise=lev=>{let s=12345;const o=[];for(let i=0;i<N*N;i++){s=(s*1103515245+12345)%2147483648;o.push((s/2147483648*2-1)*lev)}return o};
DRAW.photo=()=>{const lev=+$('phN').value,thr=+$('phT').value,nz=noise(lev);const img=BASE.map((r,y)=>r.map((v,x)=>v+nz[y*N+x]));const L=lapOf(img);
 let tp=0,fp=0;const st=[];for(let y=0;y<N;y++)for(let x=0;x<N;x++){const d=Math.abs(L[y][x])>=thr,t=TRUE.has(y*N+x);st.push(d&&t?1:d?2:t?3:0);if(d&&t)tp++;else if(d)fp++}
 const miss=TRUE.size-tp,rec=tp/TRUE.size;
 const grid=(id,fill)=>{const s=$(id),[W,H]=svgSize(s);if(!W)return;const cs=Math.min((W-16)/N,(H-16)/N),ox=(W-cs*N)/2,oy=(H-cs*N)/2;let g='';
  for(let y=0;y<N;y++)for(let x=0;x<N;x++)g+=`<rect x="${ox+x*cs}" y="${oy+y*cs}" width="${cs-1}" height="${cs-1}" fill="${fill(x,y)}"/>`;s.innerHTML=g};
 grid('photoG1',(x,y)=>{const b=Math.max(0,Math.min(255,Math.round(img[y][x])));return`rgb(${b},${b},${b})`});
 grid('photoG2',(x,y)=>['#ffffff','#1e8a4c','#c0392b','#c9ced6'][st[y*N+x]]);
 score('photo',[['맞힌 테두리',`${tp} / ${TRUE.size}`,'진짜 테두리 중 찾은 수',tp===TRUE.size?'ok':''],['잘못 찾음',fp+'개','잡음을 윤곽으로 착각',fp===0?'ok':'warn'],['놓친 테두리',miss+'개','기준이 높으면 늘어남'],['찾은 비율',(rec*100).toFixed(0)+'%','맞힌 ÷ 70',rec>=0.9?'ok':'']]);
 const n=mission('photo',[lev===0&&tp===TRUE.size&&fp===0,lev===20&&fp===0,lev===10&&rec>=0.9&&fp===0]);
 say('photo',`잡음 ${lev}, 기준값 ${thr}에서 진짜 테두리 ${tp}개를 찾았고, ${fp}개를 잘못 찾았고, ${miss}개를 놓쳤어요.`,
  `깨끗한 사진에서 가장 약한 테두리는 주변 평균과 22.5 차이! 기준값이 그보다 크면 그 점들을 놓쳐요.`,
  fp>0?'빨간 점은 잡음이야. 튄다고 다 테두리는 아니지. 기준값을 올려 봐.':miss>0&&lev>0?'기준을 올리면 잘못 찾음은 줄지만 놓치는 점이 늘어. 둘 다 0은 어려울 수도 있어.':'잡음 슬라이더를 올려서 같은 기준값이 아직도 통하는지 확인해 봐.',
  doc(n,'라플라시안은 "주변 평균과의 차이"일 뿐, 그 차이가 테두리인지 잡음인지는 판단해야 합니다. 3부의 GNN도 같은 고민을 합니다.'))};
['phN','phT'].forEach(id=>{$(id).addEventListener('input',()=>touched.photo=true);bindSl(id,v=>v,()=>DRAW.photo())});
// 시작
KEYS.forEach(k=>obs($(k+'G1'),()=>{if(!$('tab-'+k).hidden)DRAW[k]()}));
const h0=(location.hash||'').slice(1);openTab(KEYS.includes(h0)?h0:'pizza');
"""

PACK_DATA = {"page": "벡터 분석 랩 1부 복습 대시보드 — 생활 장면 시뮬레이터", "author": "안상선 ((주)M-Robo)",
             "url": "https://adminmrobo.github.io/vector_analysis_lab/dash_01.html",
             "scenes": {"pizza": "h = ρ, 넓이 ½r²θ, 각도 인코딩", "globe": "h = r sinθ, 면적 요소, 메르카토르 부풀림",
                        "flow": "발산과 전체 합, 회전과 차익", "photo": "라플라시안 윤곽선과 잡음"},
             "missions": 12,
             "cite": "안상선 (2026). 벡터 분석 랩 1부 복습 대시보드. https://adminmrobo.github.io/vector_analysis_lab/dash_01.html"}

if __name__ == '__main__':
    n = page('dash_01.html', '벡터 분석 랩 1부 대시보드 — 생활 장면 시뮬레이터',
             '피자 가게·지구 배송센터·역과 환전소·사진 앱 네 현장에서 한 걸음 h, 면적 요소, 발산, 회전, 라플라시안을 직접 운영하며 복습합니다. 미션 12개.',
             'assets/og/01.webp', body(), PAGE_JS, PACK_DATA, ['축척 인자', '면적 요소', '발산', '회전', '라플라시안'])
    print('dash01 bytes', n)
