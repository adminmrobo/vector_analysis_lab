# -*- coding: utf-8 -*-
"""2부 복습 대시보드 — 경제 상황실 (탭 4개, 미션 12개)"""
from common import *
from build_dash01 import scene, sl2

TABS = [('cycle', '경기 상황실', '방 8'), ('fx', '환전 데스크', '방 9'), ('fund', '자금순환판', '방 10'), ('town', '동네 지도·포트폴리오', '방 11·12')]

def body():
    for k in ['x1/E15', 'x2/E02', 'x3/E04', 'x1/E01', 'x2/E16', 'x3/E01']:
        USED.append(k)
    tabs = ''.join(f'<button class="btn" role="tab" id="tb-{k}" aria-controls="tab-{k}" aria-selected="false">{t} <span style="font-size:12px;opacity:.75">{r}</span></button>' for k, t, r in TABS)
    h = f"""
<header class="hero"><div class="wrap">
<div class="wing">벡터 분석 랩 · 2부 복습 대시보드</div>
<h1>경제 상황실<br>경기시계에서 포트폴리오까지</h1>
<p class="sub">2부 다섯 방을 네 개의 가상 현장에서 운영해 봅니다. 초록은 주어진 조건, 파랑은 여러분의 결정입니다. 현장마다 미션 3개, 모두 12개입니다. 모든 숫자는 교육용 가상 값입니다.</p>
<div class="by">{AUTHOR}</div>
</div></header>
<main class="wrap"><section>
{talk(T('asst/E15', '경제 상황실은 처음이에요… 성적표는 제가 읽을게요. 이상하면 바로 알려 주세요!'))}
{crowd('방청석', [('x1/E15', '<span id="xs1">(조마조마)</span>'), ('x2/E02', '<span id="xs2">(꿀꺽)</span>'), ('x3/E04', '<span id="xs3">(…!)</span>')])}
<div class="tabs" role="tablist" aria-label="현장 고르기">{tabs}</div>
<p id="allSum" style="font-weight:700" aria-live="polite"></p>
"""
    h += scene('cycle', '경제 상황실에서 가상 경기의 위치를 판단합니다. 경기는 시계 방향으로 회복 → 확장 → 둔화 → 수축을 돕니다. 경기의 크기와 한 바퀴 길이는 그때그때 다릅니다.',
               sl2('cyA', '경기의 크기', 0.3, 2, 0.1, 1.4) + sl2('cyT', '한 바퀴 분기', 8, 16, 1, 12),
               sl2('cyt', '살펴볼 분기', 0, 24, 1, 3),
               '수준·변화 평면 위의 경기 시계와 지나온 길', '수준(추세 대비)의 시간 흐름과 지금 분기',
               ['<b>회복 찾기:</b> 경기가 회복 국면에 있는 분기를 찾으세요.',
                '<b>작은 흔들림:</b> 경기의 크기를 0.5 이하로 줄이고, 둔화 국면인 분기를 찾으세요.',
                '<b>큰 경기의 한 걸음:</b> 한 바퀴 12분기에서, 한 분기(30°) 국면 이동이 실제로 1.0 이상 움직이도록 경기의 크기를 정하세요.'],
               '<a href="02_economy.html#room-8">방 8 경기순환시계</a> · <a href="01_everyday.html#room-1">1부 방 1 피자 테두리</a>')
    h += scene('fx', '환전 데스크에서 세 환율(원·달러·엔)을 점검합니다. 한 바퀴 돌아 남는 돈이 있으면 회전이 있는 것이고, 수수료가 그 틈을 얼마나 덮는지 봅니다(가상 값).',
               '<div class="btns" role="group" aria-label="환율 날짜" style="margin-top:0"><button class="btn" id="fxD1" aria-pressed="true">오늘: 1,400원 · 150엔</button><button class="btn" id="fxD2" aria-pressed="false">다음 날: 1,450원 · 155엔</button></div>',
               sl2('fxK', '100엔 = 원', 900, 980, 0.5, 950) + sl2('fxF', '거래 수수료', 0, 1.2, 0.01, 0),
               '원·달러·엔 한 바퀴와 남는 돈', '100엔 값에 따른 한 바퀴 남는 돈(수수료 뒤)과 0선',
               ['<b>틈의 문턱:</b> 오늘 환율, 100엔 = 950원에서 수수료를 올려 한 바퀴 이익이 막 사라지는 문턱을 찾으세요. (0.55~0.65%)',
                '<b>회전 0:</b> 다음 날 환율에서 수수료 0으로, 한 바퀴 남는 돈이 없게 100엔 값을 맞추세요. (±1원)',
                '<b>이익도 손해도 없는 끝:</b> 오늘 환율, 수수료 0.30%에서 한 바퀴 결과가 ±1원 안이 되는, 균형보다 비싼 100엔 값을 찾으세요.'],
               '<a href="02_economy.html#room-9">방 9 차익거래</a> · <a href="01_everyday.html#room-6">1부 방 6 환전 한 바퀴</a>')
    h += scene('fund', '자금 흐름 보고서를 씁니다. 가계·기업·정부의 순자금(남겨 내보낸 돈 − 끌어다 쓴 돈)을 정하면 해외 부문이 합 0을 맞춥니다(가상, 조 원).',
               '<div class="btns" role="group" aria-label="경기 상황" style="margin-top:0"><button class="btn" id="fuUp" aria-pressed="true">호황 기본값</button><button class="btn" id="fuDn" aria-pressed="false">불황 기본값</button></div><p style="font-size:13px;color:var(--mute);margin:6px 0 0" id="fuTxt"></p>',
               sl2('fuH', '가계', -50, 150, 5, 60) + sl2('fuC', '기업', -150, 50, 5, -120) + sl2('fuG', '정부', -100, 60, 5, 20),
               '네 부문의 순자금(+샘, −배수구)과 합계', '가계부터 차례로 쌓은 누적 합(마지막은 늘 0)',
               ['<b>정부가 샘:</b> 불황 기본값을 고른 뒤, 정부를 샘(+)으로 만드세요.',
                '<b>해외 없이 균형:</b> 해외 부문이 메우는 양이 0이 되게 맞추세요. (±2조)',
                '<b>가계가 빌리는 해:</b> 가계를 배수구(−)로 만들면서, 해외가 메우는 양은 30조 이하로 두세요.'],
               '<a href="02_economy.html#room-10">방 10 자금순환</a> · <a href="01_everyday.html#room-5">1부 방 5 지하철역</a>')
    h += scene('town', '부동산 연구팀이 한 동네의 급등이 주변으로 번지는 모습(라플라시안 섞기)을 보고, 투자팀은 세 자산의 상관이 함께 말이 되는지 점검합니다(가상 값).',
               '<div class="btns" role="group" aria-label="처음 지도" style="margin-top:0"><button class="btn" id="toA" aria-pressed="true">한 동네 급등</button><button class="btn" id="toB" aria-pressed="false">두 동네 급등</button></div>',
               sl2('toAl', '섞는 속도 α', 0.1, 1, 0.1, 0.5) + '<div class="btns"><button class="btn" id="toStep">한 단계 섞기</button><button class="btn" id="toReset">처음으로</button></div>'
               + sl2('toQ', '자산1–2 각도', 0, 180, 1, 30) + sl2('toB13', '상관 1–3', -1, 1, 0.05, 0.9) + sl2('toC', '상관 2–3', -1, 1, 0.05, 0.5),
               '동네 지도(억 원) — 오를수록 주황, 내릴수록 남색', '세 자산 화살표: 자산1·2 각도와 자산3이 놓일 자리',
               ['<b>고르게 하기:</b> 가장 비싼 동네와 싼 동네의 차이를 0.2억 이하로 줄이세요.',
                '<b>반반 섞기:</b> 자산1·2 상관을 0으로 만들어 반반 섞은 분산이 0.5가 되게 하세요. (각도 88~92°)',
                '<b>함께 말이 되는 음의 상관:</b> 상관 2–3을 −0.5 이하로 두면서도 세 상관의 확인 값이 0 이상이 되게 하세요.'],
               '<a href="02_economy.html#room-11">방 11 집값 확산</a> · <a href="02_economy.html#room-12">방 12 상관을 각도로</a>')
    h += f"""
<div class="limit" style="margin-top:24px"><b>이 대시보드의 한계</b> 경기는 사인 곡선 하나로, 환율은 세 통화로, 자금순환은 네 부문으로, 집값은 "이웃을 닮는 힘" 하나로 단순하게 봤습니다. 모든 숫자는 교육용 가상 값이며 투자·정책 판단의 근거가 아닙니다.</div>
</section>
<section id="outro"><div class="nextp"><a href="02_economy.html"><b>← 2부 본문</b>경제·금융</a><a href="03_ai_ml.html"><b>다음 →</b>3부 AI·머신러닝</a></div></section>
<section id="export"><h2>온톨로지·서지 꾸러미</h2>
<div class="btns"><button class="btn" id="copyPack">꾸러미 복사</button><span id="copyMsg" style="align-self:center;font-size:14px;color:var(--mute)" aria-live="polite"></span></div>
<pre id="pack"></pre></section>
</main>
<footer><div class="wrap">{AUTHOR}<br>원자료: @eeanimation 「Vector Analysis」 4장. 숫자는 교육용 가상 값이며 투자·정책 권고가 아닙니다. 캐릭터: 연구실 식구(fruitfly-lab-expressions).</div></footer>
"""
    return h

COMMON_DASH_JS = r"""
const touched={};const DONE={};KEYS.forEach(k=>{touched[k]=false;DONE[k]=[0,0,0]});
const say=(k,h,r,f,d)=>{$(k+'Haru').textContent=h;$(k+'Robo').textContent=r;$(k+'Fly').textContent=f;$(k+'Doc').textContent=d};
const score=(k,items)=>{$(k+'Score').innerHTML=items.map(([l,v,s,c])=>`<div class="${c||''}"><span>${l}</span><b>${v}</b><small>${s||''}</small></div>`).join('')};
function mission(k,conds){if(touched[k])conds.forEach((c,i)=>{if(c)DONE[k][i]=1});DONE[k].forEach((d,i)=>$(k+'m'+(i+1)).classList.toggle('done',!!d));
 const tot=KEYS.length*3,n=Object.values(DONE).flat().filter(Boolean).length;$('allSum').textContent=`전체 미션 ${n} / ${tot} 통과`+(n===tot?' — 복습 끝!':'');
 const s=n===tot?['(짝짝짝)','(끄덕끄덕)','(반짝반짝)']:n>=4?['(휴…)','(오!)','(두근)']:['(조마조마)','(꿀꺽)','(…!)'];['xs1','xs2','xs3'].forEach((id,i)=>$(id).textContent=s[i]);
 return DONE[k].filter(Boolean).length}
const doc=(n,hint)=>n===3?'이 현장 미션 셋 모두 통과. 다른 현장 탭도 열어 보세요.':n?`미션 ${n}개 통과. ${hint}`:hint;
const line=(pts,c,w=2.5)=>`<polyline points="${pts.map(p=>p.join(',')).join(' ')}" fill="none" stroke="${c}" stroke-width="${w}"/>`;
const axis=(x0,y0,x1,y1)=>`<line x1="${x0}" y1="${y1}" x2="${x1}" y2="${y1}" stroke="#1c2230"/><line x1="${x0}" y1="${y0}" x2="${x0}" y2="${y1}" stroke="#1c2230"/>`;
function openTab(k){KEYS.forEach(t=>{$('tab-'+t).hidden=t!==k;$('tb-'+t).setAttribute('aria-selected',t===k)});try{history.replaceState(null,'','#'+k)}catch(e){}DRAW[k]()}
KEYS.forEach(k=>$('tb-'+k).onclick=()=>openTab(k));
const DRAW={};
const bindT=(k,id,f)=>{$(id).addEventListener('input',()=>touched[k]=true);bindSl(id,f,()=>DRAW[k]())};
const press=(ids,on)=>ids.forEach(id=>$(id).setAttribute('aria-pressed',id===on));
"""

PAGE_JS = "const KEYS=['cycle','fx','fund','town'];" + COMMON_DASH_JS + r"""
// ===== 경기 =====
const phase=(x,y)=>x>=0&&y>=0?'확장':x>=0?'둔화':y<0?'수축':'회복';
const cyPt=(t,A,T)=>{const w=2*Math.PI*t/T;return[A*Math.sin(w+Math.PI/4),A*Math.cos(w+Math.PI/4)]};
DRAW.cycle=()=>{const A=+$('cyA').value,T=+$('cyT').value,t=+$('cyt').value,p=cyPt(t,A,T),r=Math.hypot(...p),ang=Math.atan2(p[1],p[0])*R2D,ph=phase(...p),step=r*2*Math.PI/T;
 const g1=$('cycleG1'),[W,H]=svgSize(g1);if(W){const cx=W/2,cy=H/2,k=Math.min(W,H)*0.22;let g='';
  [['회복',-1,-1,'#e6f3f5'],['확장',1,-1,'#eaf6ee'],['둔화',1,1,'#fdf0e6'],['수축',-1,1,'#f4eef9']].forEach(([n,sx,sy,c])=>{g+=`<rect x="${sx<0?cx-2*k:cx}" y="${sy<0?cy-2*k:cy}" width="${2*k}" height="${2*k}" fill="${c}"/><text x="${cx+sx*k*1.5}" y="${cy+sy*k*1.6}" font-size="13" font-weight="700" text-anchor="middle" fill="#5d6676">${n}</text>`});
  g+=`<line x1="${cx-2*k}" y1="${cy}" x2="${cx+2*k}" y2="${cy}" stroke="#1c2230"/><line x1="${cx}" y1="${cy-2*k}" x2="${cx}" y2="${cy+2*k}" stroke="#1c2230"/>`;
  const pts=[];for(let u=0;u<=t;u+=0.25){const q=cyPt(u,A,T);pts.push([cx+q[0]*k,cy-q[1]*k])}g+=line(pts,'#9aa3b0',2);
  g+=`<line x1="${cx}" y1="${cy}" x2="${cx+p[0]*k}" y2="${cy-p[1]*k}" stroke="#d4691f" stroke-width="3"/><circle cx="${cx+p[0]*k}" cy="${cy-p[1]*k}" r="8" fill="#c0392b"/>`;g1.innerHTML=g}
 const g2=$('cycleG2'),[W2,H2]=svgSize(g2);if(W2){const x0=34,x1=W2-10,y0=14,y1=H2-26,mid=(y0+y1)/2,X=u=>x0+u/24*(x1-x0),Y=v=>mid-v/2.1*(y1-y0)/2;
  let g=axis(x0,y0,x1,y1)+`<line x1="${x0}" y1="${mid}" x2="${x1}" y2="${mid}" stroke="#c9ced6" stroke-dasharray="4 4"/><text x="${x0+4}" y="${mid-4}" font-size="11" fill="#5d6676">추세</text>`;
  const pts=[];for(let u=0;u<=24;u+=0.25)pts.push([X(u),Y(cyPt(u,A,T)[0])]);g+=line(pts,'#1f7a8c',3)+`<line x1="${X(t)}" y1="${y0}" x2="${X(t)}" y2="${y1}" stroke="#c0392b" stroke-width="2"/><circle cx="${X(t)}" cy="${Y(p[0])}" r="6" fill="#c0392b"/>`;
  [0,6,12,18,24].forEach(u=>g+=`<text x="${X(u)}" y="${y1+16}" font-size="11" text-anchor="middle">${u}분기</text>`);g2.innerHTML=g}
 score('cycle',[['수준 · 변화',`${p[0].toFixed(2)} · ${p[1].toFixed(2)}`,'추세 대비 · 방향'],['반지름 · 각도',`${r.toFixed(2)} · ${ang.toFixed(0)}°`,'경기의 크기 · 국면 각도'],['국면',ph,'시계 방향으로 돎',ph==='회복'?'ok':''],['한 분기 실제 이동',step.toFixed(2),`${r.toFixed(2)} × 360°/${T}`,step>=1?'ok':'']]);
 const n=mission('cycle',[ph==='회복',A<=0.5&&ph==='둔화',T===12&&step>=1]);
 say('cycle',`${t}분기는 ${ph} 국면이에요. 반지름 ${r.toFixed(2)}, 각도 ${ang.toFixed(0)}°예요.`,`한 분기에 ${(360/T).toFixed(0)}°씩 돌아요. 실제 이동은 ${r.toFixed(2)} × ${(2*Math.PI/T).toFixed(3)} = ${step.toFixed(2)}!`,
  A<0.6?'경기가 작으면 국면이 바뀌어도 실제 변화는 작아. 국면 이름만 보고 놀라지 마.':'그림 ②에서 꼭대기(수준이 가장 높을 때)가 어느 국면인지 맞혀 봐. 확장과 둔화의 경계야.',
  doc(n,'각도는 국면, 반지름은 크기입니다. 둘을 함께 읽어야 경기 판단이 됩니다.'))};
['cyA','cyT','cyt'].forEach(id=>bindT('cycle',id,v=>id==='cyA'?v.toFixed(1):id==='cyT'?v+'분기':v));
// ===== 환전 =====
let fxDay=1;const FXR={1:[1400,150],2:[1450,155]};
$('fxD1').onclick=()=>{fxDay=1;press(['fxD1','fxD2'],'fxD1');touched.fx=true;DRAW.fx()};$('fxD2').onclick=()=>{fxDay=2;press(['fxD1','fxD2'],'fxD2');touched.fx=true;DRAW.fx()};
DRAW.fx=()=>{const[u,j]=FXR[fxDay],kj=+$('fxK').value,f=+$('fxF').value/100,BAL=u/j*100;const ratio=kj/BAL,ff=(1-f)**3,net=1400*(ratio*ff-1),pr=1400*(ratio-1),thr=1-Math.pow(1/Math.max(ratio,1e-9),1/3);
 const g1=$('fxG1'),[W,H]=svgSize(g1);if(W){const P=[[W*0.18,H*0.7],[W*0.5,H*0.16],[W*0.82,H*0.7]],nm=['원','달러','엔'],cl=['#24345c','#1f7a8c','#d4691f'],vv=[`1,400 → ${fmt(1400+net,1)}`,(1400/u).toFixed(3),(1400/u*j).toFixed(1)];let g='';
  [[0,1],[1,2],[2,0]].forEach(([a,b])=>{const p=P[a],q=P[b],dx=q[0]-p[0],dy=q[1]-p[1],L=Math.hypot(dx,dy),ux=dx/L,uy=dy/L,s=[p[0]+ux*34,p[1]+uy*34],e=[q[0]-ux*36,q[1]-uy*36];g+=`<line x1="${s[0]}" y1="${s[1]}" x2="${e[0]}" y2="${e[1]}" stroke="#5d6676" stroke-width="2.5"/><polygon points="${e[0]},${e[1]} ${e[0]-10*ux+5*uy},${e[1]-10*uy-5*ux} ${e[0]-10*ux-5*uy},${e[1]-10*uy+5*ux}" fill="#5d6676"/>`});
  P.forEach((p,k)=>g+=`<circle cx="${p[0]}" cy="${p[1]}" r="28" fill="#fff" stroke="${cl[k]}" stroke-width="3"/><text x="${p[0]}" y="${p[1]+5}" font-size="14" font-weight="700" text-anchor="middle" fill="${cl[k]}">${nm[k]}</text><text x="${p[0]}" y="${p[1]+46}" font-size="12" font-weight="700" text-anchor="middle">${vv[k]}</text>`);
  g+=`<text x="${W/2}" y="${H*0.55}" font-size="16" font-weight="900" text-anchor="middle" fill="${Math.abs(net)<=1?'#1e8a4c':net>0?'#c0392b':'#7a3fd6'}">수수료 뒤 ${net>=0?'+':''}${fmt(net,1)}원</text>`;g1.innerHTML=g}
 const g2=$('fxG2'),[W2,H2]=svgSize(g2);if(W2){const x0=40,x1=W2-10,y0=14,y1=H2-26,X=v=>x0+(v-900)/80*(x1-x0),Y=v=>(y0+y1)/2-Math.max(-60,Math.min(60,v))/60*(y1-y0)/2;
  let g=axis(x0,y0,x1,y1)+`<line x1="${x0}" y1="${Y(0)}" x2="${x1}" y2="${Y(0)}" stroke="#1c2230" stroke-dasharray="4 4"/>`;const pts=[];for(let v=900;v<=980;v+=1)pts.push([X(v),Y(1400*(v/BAL*ff-1))]);g+=line(pts,'#d4691f',3);
  g+=`<line x1="${X(BAL)}" y1="${y0}" x2="${X(BAL)}" y2="${y1}" stroke="#1e8a4c" stroke-dasharray="3 3"/><text x="${X(BAL)+4}" y="${y0+10}" font-size="11" fill="#1e8a4c">균형 ${BAL.toFixed(1)}</text><circle cx="${X(kj)}" cy="${Y(net)}" r="6" fill="#c0392b"/>`;
  [900,940,980].forEach(v=>g+=`<text x="${X(v)}" y="${y1+16}" font-size="11" text-anchor="middle">${v}원</text>`);g+=`<text x="${x0-4}" y="${Y(50)+4}" font-size="11" text-anchor="end">+50</text><text x="${x0-4}" y="${Y(-50)+4}" font-size="11" text-anchor="end">−50</text>`;g2.innerHTML=g}
 score('fx',[['한 바퀴 비율',ratio.toFixed(4),'1이면 회전 0',Math.abs(pr)<=1?'ok':''],['로그 합(회전)',Math.log(ratio).toFixed(4),'0이면 높이 지도 하나'],['수수료 뒤 남는 돈',(net>=0?'+':'')+fmt(net,1)+'원',`수수료 ${(f*100).toFixed(2)}% × 3번`,Math.abs(net)<=1?'ok':net>0?'warn':''],['틈을 덮는 수수료',ratio>1?(thr*100).toFixed(2)+'%':'—','이보다 비싸면 이익 없음']]);
 const n=mission('fx',[fxDay===1&&Math.abs(kj-950)<0.01&&f*100>=0.55&&f*100<=0.65&&net<=0,fxDay===2&&f===0&&Math.abs(pr)<=1,fxDay===1&&Math.abs(f*100-0.3)<0.005&&kj>BAL&&Math.abs(net)<=1]);
 say('fx',`한 바퀴 비율 ${ratio.toFixed(4)}, 수수료를 세 번 내고 나면 ${net>=0?'+':''}${fmt(net,1)}원이에요.`,`이 틈을 덮으려면 수수료 ${ratio>1?(thr*100).toFixed(2)+'%':'(틈 없음)'}면 돼요. 균형 100엔 값은 ${BAL.toFixed(1)}원!`,
  net>1?'남는 돈이 있다고 바로 돌리면 안 돼. 실제로는 환율이 움직이는 동안 손해를 볼 수도 있어.':'수수료가 있으면 균형 근처에 "아무도 손대지 않는 띠"가 생겨. 그림 ②에서 0선 근처를 봐.',
  doc(n,'회전 0은 "가격들이 서로 앞뒤가 맞는다"는 뜻입니다. 수수료는 작은 회전을 그냥 두게 만듭니다.'))};
['fxK','fxF'].forEach(id=>bindT('fx',id,v=>id==='fxK'?fmt(v,1)+'원':v.toFixed(2)+'%'));
// ===== 자금순환 =====
const FU={up:[60,-120,20,'호황: 기업이 투자를 늘려 크게 빌리고, 세금이 잘 걷혀 정부는 샘'],dn:[120,-30,-80,'불황: 가계가 아끼고 기업은 투자를 줄이며, 정부가 지출을 늘려 배수구']};
const fuSet=k=>{const v=FU[k];$('fuH').value=v[0];$('fuC').value=v[1];$('fuG').value=v[2];$('fuTxt').textContent=v[3];press(['fuUp','fuDn'],k==='up'?'fuUp':'fuDn');fuMode=k;['fuH','fuC','fuG'].forEach(id=>$(id).dispatchEvent(new Event('input')))};
let fuMode='up';$('fuUp').onclick=()=>{touched.fund=true;fuSet('up')};$('fuDn').onclick=()=>{touched.fund=true;fuSet('dn')};$('fuTxt').textContent=FU.up[3];
DRAW.fund=()=>{const h=+$('fuH').value,c=+$('fuC').value,g0=+$('fuG').value,f=-(h+c+g0),vals=[['가계',h],['기업',c],['정부',g0],['해외',f]];
 const g1=$('fundG1'),[W,H]=svgSize(g1);if(W){const mid=H*0.5,sc=(H*0.4)/200,bw=Math.min(56,W/8);let g=`<line x1="14" y1="${mid}" x2="${W-10}" y2="${mid}" stroke="#1c2230"/>`;
  [...vals,['합계',0]].forEach(([l,v],i)=>{const x=24+i*(W-40)/5,hh=Math.min(Math.abs(v),200)*sc,col=i===4?'#1e8a4c':i===3?'#7a3fd6':v>=0?'#d4691f':'#24345c';g+=`<rect x="${x}" y="${v>=0?mid-hh:mid}" width="${bw}" height="${Math.max(1,hh)}" fill="${col}" rx="3"/><text x="${x+bw/2}" y="${v>=0?mid-hh-5:mid+hh+14}" font-size="12" font-weight="700" text-anchor="middle" fill="${col}">${v>0?'+':''}${v}</text><text x="${x+bw/2}" y="${H-6}" font-size="12" text-anchor="middle">${l}</text>`});g1.innerHTML=g}
 const g2=$('fundG2'),[W2,H2]=svgSize(g2);if(W2){const mid=H2*0.5,sc=(H2*0.4)/250,bw=Math.min(56,W2/7);let acc=0,g=`<line x1="14" y1="${mid}" x2="${W2-10}" y2="${mid}" stroke="#1c2230"/>`;
  vals.forEach(([l,v],i)=>{const x=24+i*(W2-40)/4,a0=acc;acc+=v;const yA=mid-a0*sc,yB=mid-acc*sc;g+=`<rect x="${x}" y="${Math.min(yA,yB)}" width="${bw}" height="${Math.max(1,Math.abs(yB-yA))}" fill="${v>=0?'#d4691f':'#24345c'}" opacity=".85"/><text x="${x+bw/2}" y="${yB+(v>=0?-5:14)}" font-size="11" text-anchor="middle">누적 ${acc}</text><text x="${x+bw/2}" y="${H2-6}" font-size="12" text-anchor="middle">${l}</text>`});g2.innerHTML=g}
 score('fund',[['가계',(h>0?'+':'')+h+'조',h>=0?'샘':'배수구'],['기업',(c>0?'+':'')+c+'조',c>=0?'샘':'배수구'],['정부',(g0>0?'+':'')+g0+'조',g0>=0?'샘':'배수구',g0>0?'ok':''],['해외가 메움',(f>0?'+':'')+f+'조','네 부문 합 = 0',Math.abs(f)<=2?'ok':Math.abs(f)>60?'warn':'']]);
 const n=mission('fund',[fuMode==='dn'&&g0>0,Math.abs(f)<=2,h<0&&Math.abs(f)<=30]);
 say('fund',`가계 ${h>0?'+':''}${h}, 기업 ${c>0?'+':''}${c}, 정부 ${g0>0?'+':''}${g0}조라서 해외가 ${f>0?'+':''}${f}조로 맞춰요.`,`누적 막대 마지막은 언제나 0이에요. 발산 정리 그대로!`,
  Math.abs(f)>60?'해외가 너무 크게 메우고 있어. 실제라면 오래 이어질 수 있을지 의심해 봐야 해.':'한 부문이 샘이 되면, 다른 어딘가는 반드시 배수구가 돼. 누가 그 역할을 맡는지 봐.',
  doc(n,'부문 하나만 보지 말고 "합이 0이 되도록 누가 메우는가"를 함께 보세요.'))};
['fuH','fuC','fuG'].forEach(id=>bindT('fund',id,v=>(v>0?'+':'')+v+'조'));
// ===== 동네·포트폴리오 =====
const TN=5;let TG,tStep=0,tMode='A';const tInit=()=>{TG=[];for(let y=0;y<TN;y++){TG.push([]);for(let x=0;x<TN;x++)TG[y].push(5)}if(tMode==='A'){TG[2][2]=6;TG[0][4]=4}else{TG[1][1]=6;TG[3][3]=6;TG[4][0]=4}tStep=0};tInit();
const tNb=(x,y)=>{const a=[];[[1,0],[-1,0],[0,1],[0,-1]].forEach(([dx,dy])=>{const X=x+dx,Y=y+dy;if(X>=0&&Y>=0&&X<TN&&Y<TN)a.push(TG[Y][X])});return a.reduce((p,q)=>p+q,0)/a.length};
$('toA').onclick=()=>{tMode='A';press(['toA','toB'],'toA');tInit();touched.town=true;DRAW.town()};$('toB').onclick=()=>{tMode='B';press(['toA','toB'],'toB');tInit();touched.town=true;DRAW.town()};
$('toStep').onclick=()=>{const a=+$('toAl').value,L=TG.map((r,y)=>r.map((v,x)=>tNb(x,y)-v));TG=TG.map((r,y)=>r.map((v,x)=>v+a*L[y][x]));tStep++;touched.town=true;DRAW.town()};
$('toReset').onclick=()=>{tInit();DRAW.town()};
DRAW.town=()=>{const all=TG.flat(),spread=Math.max(...all)-Math.min(...all);const q=+$('toQ').value*D2R,a=Math.cos(q),b=+$('toB13').value,c=+$('toC').value,det=1+2*a*b*c-a*a-b*b-c*c,vh=(1+a)/2;
 const g1=$('townG1'),[W,H]=svgSize(g1);if(W){const cs=Math.min((W-16)/TN,(H-16)/TN),ox=(W-cs*TN)/2,oy=(H-cs*TN)/2;let g='';
  for(let y=0;y<TN;y++)for(let x=0;x<TN;x++){const v=TG[y][x],d=Math.max(-1,Math.min(1,v-5)),u=Math.abs(d);const col=d>=0?`rgb(${Math.round(238-u*26)},${Math.round(241-u*136)},${Math.round(245-u*214)})`:`rgb(${Math.round(238-u*202)},${Math.round(241-u*189)},${Math.round(245-u*153)})`;
   g+=`<rect x="${ox+x*cs}" y="${oy+y*cs}" width="${cs-2}" height="${cs-2}" rx="6" fill="${col}"/><text x="${ox+x*cs+cs/2-1}" y="${oy+y*cs+cs/2+5}" font-size="${Math.min(14,cs/3.3)}" font-weight="700" text-anchor="middle" fill="${u>0.35?'#fff':'#1c2230'}">${v.toFixed(2)}</text>`}g1.innerHTML=g}
 const g2=$('townG2'),[W2,H2]=svgSize(g2);if(W2){const cx=W2/2,cy=H2*0.55,R=Math.min(W2,H2)*0.32;let g=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="none" stroke="#c9ced6" stroke-dasharray="4 4"/>`;
  const ar=(v,col,l)=>{const X=cx+v[0]*R,Y=cy-v[1]*R;return`<line x1="${cx}" y1="${cy}" x2="${X}" y2="${Y}" stroke="${col}" stroke-width="4"/><circle cx="${X}" cy="${Y}" r="6" fill="${col}"/><text x="${X+8}" y="${Y-6}" font-size="12" font-weight="700" fill="${col}">${l}</text>`};
  g+=ar([1,0],'#d4691f','자산1')+ar([Math.cos(q),Math.sin(q)],'#1f7a8c','자산2');
  if(det>=-1e-9&&Math.sin(q)>1e-6)g+=ar([b,(c-a*b)/Math.sin(q)],'#7a3fd6','자산3 그림자');else if(det<-1e-9)g+=`<text x="${cx}" y="${H2-10}" font-size="13" font-weight="700" text-anchor="middle" fill="#c0392b">자산3을 놓을 진짜 자리가 없습니다</text>`;g2.innerHTML=g}
 score('town',[['동네 값 차이',spread.toFixed(3)+'억',`${tStep}단계 섞음`,spread<=0.2?'ok':''],['자산1·2 상관',a.toFixed(3),`cos ${(q*R2D).toFixed(0)}°`],['반반 섞은 분산',vh.toFixed(3),'(1 + 상관) ÷ 2',Math.abs(vh-0.5)<0.02?'ok':''],['세 상관 확인 값',det.toFixed(3),'0 이상이면 말이 됨',det>=-1e-9?'ok':'warn']]);
 const n=mission('town',[spread<=0.2,Math.abs(q*R2D-90)<=2,c<=-0.5&&det>=-1e-9]);
 say('town',`동네 차이는 ${spread.toFixed(3)}억, 자산1·2 상관은 ${a.toFixed(2)}, 세 상관 확인 값은 ${det.toFixed(3)}이에요.`,`2–3 상관이 될 수 있는 범위는 ${Math.cos(Math.min(Math.PI,q+Math.acos(b))).toFixed(2)} ~ ${Math.cos(Math.abs(q-Math.acos(b))).toFixed(2)}예요!`,
  spread<0.02?'너무 섞었어. 이제 모든 동네가 같아서 어디가 특별했는지 알 수 없어.':det<0?'숫자 하나하나는 −1~1인데 함께는 말이 안 돼. 자산1과 셋의 각도부터 다시 봐.':'2–3 상관을 크게 음수로 만들려면 자산2와 자산3이 자산1을 사이에 두고 반대쪽에 있어야 해.',
  doc(n,'섞기는 차이를 줄이지만 특징도 지웁니다. 상관은 각도로 보면 함께 말이 되는지 바로 보입니다.'))};
$('toAl').addEventListener('input',()=>touched.town=true);bindSl('toAl',v=>v.toFixed(1),()=>DRAW.town())();
['toQ','toB13','toC'].forEach(id=>bindT('town',id,v=>id==='toQ'?v+'°':v.toFixed(2)));
KEYS.forEach(k=>obs($(k+'G1'),()=>{if(!$('tab-'+k).hidden)DRAW[k]()}));
const h0=(location.hash||'').slice(1);openTab(KEYS.includes(h0)?h0:'cycle');
"""

PACK_DATA = {"page": "벡터 분석 랩 2부 복습 대시보드 — 경제 상황실", "author": "안상선 ((주)M-Robo)",
             "url": "https://adminmrobo.github.io/vector_analysis_lab/dash_02.html",
             "scenes": {"cycle": "원통 자 경기시계", "fx": "회전·수수료 문턱", "fund": "발산 정리", "town": "라플라시안 섞기·상관 각도"},
             "missions": 12, "note": "교육용 가상 값",
             "cite": "안상선 (2026). 벡터 분석 랩 2부 복습 대시보드. https://adminmrobo.github.io/vector_analysis_lab/dash_02.html"}

if __name__ == '__main__':
    n = page('dash_02.html', '벡터 분석 랩 2부 대시보드 — 경제 상황실',
             '경기 상황실·환전 데스크·자금순환판·동네 지도와 포트폴리오 네 현장에서 원통 자·회전·발산·라플라시안·상관 각도를 직접 운영하며 복습합니다. 미션 12개.',
             'assets/og/02.webp', body(), PAGE_JS, PACK_DATA, ['경기순환', '차익거래', '자금순환', '확산', '상관'])
    print('dash02 bytes', n)
