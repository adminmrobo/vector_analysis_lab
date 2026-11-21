# -*- coding: utf-8 -*-
"""0편 복습 대시보드 — 좌표계 놀이터: 같은 ∇, 세 가지 자"""
from common import *

def body():
    # 미리 쓸 표정 등록(동적 대사용)
    for k in ['asst/E07', 'asst/E10', 'asst/E16', 'asst/E20', 'asst/E15', 'fly/E07', 'fly/E08', 'fly/E10',
              'robo/E09', 'robo/E16', 'robo/E04', 'doc/E08', 'doc/E16', 'doc/E01', 'x1/E15', 'x2/E02', 'x3/E04',
              'x1/E01', 'x2/E16', 'x3/E01', 'sia/E09', 'moa/E09']:
        USED.append(k)
    sl2 = lambda i, l, mn, mx, st, v: f'<div class="sl"><label for="{i}">{l}</label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{v}"><output id="{i}o"></output></div>'
    return f"""
<header class="hero"><div class="wrap">
<div class="wing e">벡터 분석 랩 · 0편 복습 대시보드</div>
<h1>좌표계 놀이터<br>같은 ∇, 세 가지 자</h1>
<p class="sub">0편에서 배운 네 개의 자를 직접 돌려 봅니다. 함수와 화살표 밭을 고르고, 점을 옮기고, 자를 바꿉니다. 기울기·발산·회전·라플라시안을 원자료 카드의 식 그대로 세 자로 계산해, 숫자는 달라도 결과는 같은지 확인합니다.</p>
<div class="by">{AUTHOR}</div>
</div></header>
<main class="wrap">
<section>
<div class="three"><h2>이 대시보드에서 하는 일</h2>
<ol><li><b>시연:</b> "자 바꿔 가며 보기"를 누르면 같은 점을 가로·세로·높이 → 원통 → 지구본 자로 차례로 읽어 줍니다.</li>
<li><b>복습:</b> 아래 미션 3개를 직접 풀면 0편의 핵심(한 걸음 h, 작은 상자 dV, 같은 ∇)이 정리됩니다.</li>
<li><b>확인:</b> 비교표에서 세 자의 결과가 소수 넷째 자리까지 같은지 봅니다. 모든 계산은 원자료 카드 4/4의 일반 식으로 했습니다.</li></ol></div>
{talk(T('asst/E20', '오늘은 복습 시간이에요. 제가 숫자를 읽어 드릴게요… 틀리면 꼭 말해 주세요!'))}
{crowd('방청석', [('x1/E15', '(조마조마)'), ('x2/E02', '(꿀꺽)'), ('x3/E04', '(…!)')])}
<details style="margin:10px 0"><summary>이 대시보드의 기호와 약어 풀이</summary><table><tbody><tr><td class="m">∇f</td><td>기울기. 함수 f가 가장 가파르게 오르는 쪽 화살표</td></tr><tr><td class="m">∇·A</td><td>발산. 화살표 밭 A가 그 자리에서 솟아나는 양</td></tr><tr><td class="m">∇×A</td><td>회전. 그 자리에서 도는 양</td></tr><tr><td class="m">∇²f</td><td>라플라시안. 주변 평균과 나의 차이</td></tr><tr><td class="m">h, h₁h₂h₃</td><td>한 걸음의 실제 길이와 그 곱(작은 상자 배율)</td></tr><tr><td class="m">dV</td><td>작은 상자의 실제 부피</td></tr></tbody></table></details>
</section>

<section id="board">
<div class="dash">
<div class="panel" aria-label="조작판"><h3>조작판</h3>
<div class="grp env"><b>재료 고르기 (함수 · 화살표 밭)</b>
<label for="dF" style="font-size:14px">함수 f (높이 지도)</label>
<select id="dF" class="btn" style="width:100%;margin:4px 0 8px"><option value="0">f = x² + y² (그릇)</option><option value="1">f = r (중심에서 거리)</option><option value="2">f = z (높이)</option><option value="3">f = 1/r (점에서 멀어질수록 작아짐)</option></select>
<label for="dA" style="font-size:14px">화살표 밭 A</label>
<select id="dA" class="btn" style="width:100%;margin:4px 0 0"><option value="0">A = (x, y, z) 샘</option><option value="1">A = (−y, x, 0) 소용돌이</option><option value="2">A = r̂ / r² 점에서 퍼짐</option></select>
</div>
<div class="grp me"><b>내 결정 (자 · 점 위치)</b>
<div class="btns" role="group" aria-label="자 고르기" style="margin-top:0"><button class="btn" id="dC" aria-pressed="true">가로·세로·높이</button><button class="btn" id="dY" aria-pressed="false">원통</button><button class="btn" id="dS" aria-pressed="false">지구본</button></div>
{sl2('dx', 'x (동쪽)', -2, 2, 0.01, 1)}{sl2('dy', 'y (북쪽)', -2, 2, 0.01, 1)}{sl2('dz', 'z (높이)', -2, 2, 0.01, 1.41)}
<div class="btns"><button class="btn" id="dPlay">자 바꿔 가며 보기</button><button class="btn" id="dReset">처음 점으로</button></div>
</div>
</div>
<div style="min-width:0">
<div class="score" id="dScore" aria-live="polite"></div>
<div class="figs">
<div><div class="fig"><svg id="dView" role="img" aria-label="공간좌표 위의 점, 고른 자의 한 걸음 화살표, 기울기 화살표"></svg></div><p class="cap">그림 ① 점과 고른 자의 세 방향(한 걸음 0.3을 2배로), 남색 굵은 화살표 = ∇f(기울기)</p></div>
<div><div class="fig"><svg id="dBars" role="img" aria-label="고른 자로 나눈 기울기 성분 막대"></svg></div><p class="cap">그림 ② 고른 자로 나눈 ∇f 성분. 자를 바꾸면 막대는 바뀌어도 길이(크기)는 같습니다</p></div>
</div>
<div class="scroll" style="margin-top:12px"><table class="cmp" id="dCmp"></table></div>
{talk(T('asst/E07', '<span id="lnHaru">…</span>'), T('robo/E09', '<span id="lnRobo">…</span>'), T('fly/E08', '<span id="lnFly">…</span>'), T('doc/E08', '<span id="lnDoc">…</span>'))}
</div></div>
</section>

<section id="missions">
<h2>미션 3개 — 0편 복습</h2>
<ol class="missions">
<li id="m1"><b>미션 ① 한 걸음 h = 2:</b> 원통 자에서 φ 쪽 한 걸음의 실제 길이(h)가 2가 되는 점을 찾으세요. <span style="color:var(--mute)">(허용 오차 ±0.05, 0편 방 A)</span><details style="margin-top:4px"><summary style="font-size:13px">힌트</summary><span style="font-size:14px">원통 자를 누르고 점을 높이 축에서 2만큼 떨어진 곳(예: x = 2, y = 0)으로 옮기세요. φ 쪽 h = ρ입니다.</span></details></li>
<li id="m2"><b>미션 ② 같은 ∇:</b> 함수를 f = 1/r로 고르고 세 자를 모두 눌러, 라플라시안이 세 자 모두 같은 값(0)인지 확인하세요. <span style="color:var(--mute)">(0편 방 A 풀이)</span><details style="margin-top:4px"><summary style="font-size:13px">힌트</summary><span style="font-size:14px">함수에서 f = 1/r을 고른 뒤 세 자 단추를 한 번씩 누르세요.</span></details></li>
<li id="m3"><b>미션 ③ 납작한 상자:</b> 지구본 자에서 작은 상자 부피(눈금 0.1씩)가 0.0002보다 작아지는 곳을 찾으세요. 중심에서 거리 r은 0.5 이상. <span style="color:var(--mute)">(0편 방 B)</span><details style="margin-top:4px"><summary style="font-size:13px">힌트</summary><span style="font-size:14px">지구본 자에서 x·y를 0 가까이, z를 1 이상으로. sinθ가 0에 가까워집니다.</span></details></li>
</ol>
<p id="mSum" style="font-weight:700" aria-live="polite"></p>
<div class="limit"><b>이 대시보드의 한계</b> 미분은 아주 작은 간격으로 나눠 어림한 값입니다(소수 넷째 자리까지 맞음). 원점(r = 0)이나 높이 축 위(ρ = 0)에서는 각도 쪽 방향이 없어 원통·지구본 자의 식을 쓸 수 없습니다. 숫자는 모두 교육용 예시입니다.</div>
<h3>배운 곳 다시 보기</h3>
<p><a href="00_orientation.html#room-e">입구 방 두 점 사이 거리</a> · <a href="00_orientation.html#room-a">방 A 네 개의 자</a> · <a href="00_orientation.html#room-b">방 B 한 걸음 상자</a> · <a href="dash_01.html">1부 대시보드로</a></p>
</section>

<section id="outro">
{crowd('방청석', [('x1/E01', '<span id="xs1">(…)</span>'), ('x2/E16', '<span id="xs2">(…)</span>'), ('x3/E01', '<span id="xs3">(…)</span>')])}
<div class="nextp"><a href="00_orientation.html"><b>← 0편 본문</b>네 개의 자</a><a href="01_everyday.html"><b>다음 →</b>1부 생활</a></div>
</section>

<section id="export"><h2>온톨로지·서지 꾸러미</h2>
<div class="btns"><button class="btn" id="copyPack">꾸러미 복사</button><span id="copyMsg" style="align-self:center;font-size:14px;color:var(--mute)" aria-live="polite"></span></div>
<pre id="pack"></pre></section>
</main>
<footer><div class="wrap">{AUTHOR}<br>원자료: @eeanimation 「Vector Analysis」 4장 — 기울기·발산·회전·라플라시안 식(카드 4/4 일반형)을 그대로 계산. 캐릭터: 연구실 식구(fruitfly-lab-expressions).</div></footer>
"""

PAGE_JS = r"""
// ===== 좌표계 계산 (카드 4/4 일반 식) =====
const SYS={C:{name:'가로·세로·높이',q:['x','y','z'],
  toC:q=>q, fromC:p=>p, h:q=>[1,1,1], e:q=>[[1,0,0],[0,1,0],[0,0,1]]},
 Y:{name:'원통',q:['ρ','φ','z'],
  toC:q=>[q[0]*Math.cos(q[1]),q[0]*Math.sin(q[1]),q[2]], fromC:p=>[Math.hypot(p[0],p[1]),Math.atan2(p[1],p[0]),p[2]],
  h:q=>[1,q[0],1], e:q=>[[Math.cos(q[1]),Math.sin(q[1]),0],[-Math.sin(q[1]),Math.cos(q[1]),0],[0,0,1]]},
 S:{name:'지구본',q:['r','θ','φ'],
  toC:q=>[q[0]*Math.sin(q[1])*Math.cos(q[2]),q[0]*Math.sin(q[1])*Math.sin(q[2]),q[0]*Math.cos(q[1])],
  fromC:p=>{const r=Math.hypot(p[0],p[1],p[2]);return[r,r?Math.acos(Math.max(-1,Math.min(1,p[2]/r))):0,Math.atan2(p[1],p[0])]},
  h:q=>[1,q[0],q[0]*Math.sin(q[1])],
  e:q=>{const[r,t,f]=q;return[[Math.sin(t)*Math.cos(f),Math.sin(t)*Math.sin(f),Math.cos(t)],[Math.cos(t)*Math.cos(f),Math.cos(t)*Math.sin(f),-Math.sin(t)],[-Math.sin(f),Math.cos(f),0]]}}};
const FN=[p=>p[0]*p[0]+p[1]*p[1], p=>Math.hypot(p[0],p[1],p[2]), p=>p[2], p=>1/Math.hypot(p[0],p[1],p[2])];
const FNAME=['x² + y²','r','z','1/r'];
const AF=[p=>[p[0],p[1],p[2]], p=>[-p[1],p[0],0], p=>{const r=Math.hypot(p[0],p[1],p[2]);return[p[0]/r**3,p[1]/r**3,p[2]/r**3]}];
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
const d1=(G,q,i,e=1e-4)=>{const a=q.slice(),b=q.slice();a[i]+=e;b[i]-=e;return(G(a)-G(b))/(2*e)};
function calc(S,p,fi,ai){const s=SYS[S],q=s.fromC(p),h=s.h(q),H=h[0]*h[1]*h[2];
 const F=qq=>FN[fi](s.toC(qq));
 const Ai=(qq,i)=>dot(AF[ai](s.toC(qq)),s.e(qq)[i]);
 const hh=(qq,i)=>s.h(qq)[i];const HH=qq=>{const t=s.h(qq);return t[0]*t[1]*t[2]};
 const grad=[0,1,2].map(i=>d1(F,q,i)/h[i]);
 let div=0;for(let i=0;i<3;i++)div+=d1(qq=>HH(qq)/hh(qq,i)*Ai(qq,i),q,i,1e-4);div/=H;
 const c=(i,j,k)=>(d1(qq=>hh(qq,k)*Ai(qq,k),q,j)-d1(qq=>hh(qq,j)*Ai(qq,j),q,k))/(h[j]*h[k]);
 const curl=[c(0,1,2),c(1,2,0),c(2,0,1)];
 let lap=0;for(let i=0;i<3;i++)lap+=d1(qq=>HH(qq)/hh(qq,i)**2*d1(F,qq,i,1e-4),q,i,1e-3);lap/=H;
 return{q,h,H,grad,div,curl,lap,e:s.e(q)}}
const nrm=v=>Math.hypot(v[0],v[1],v[2]);
const toCartVec=(comp,E)=>[0,1,2].map(k=>comp[0]*E[0][k]+comp[1]*E[1][k]+comp[2]*E[2][k]);
// ===== 상태 =====
let sys='C';const seen={C:false,Y:false,S:false};let touched=false;const done=[false,false,false];
const pick=k=>{sys=k;[['dC','C'],['dY','Y'],['dS','S']].forEach(([id,v])=>$(id).setAttribute('aria-pressed',v===k));touched=true;draw()};
$('dC').onclick=()=>pick('C');$('dY').onclick=()=>pick('Y');$('dS').onclick=()=>pick('S');
const P=()=>[+$('dx').value,+$('dy').value,+$('dz').value];
const deg=v=>(v*R2D).toFixed(0)+'°';
const fq=(S,q)=>S==='C'?`(${q.map(v=>v.toFixed(2)).join(', ')})`:S==='Y'?`(${q[0].toFixed(2)}, ${deg(q[1])}, ${q[2].toFixed(2)})`:`(${q[0].toFixed(2)}, ${deg(q[1])}, ${deg(q[2])})`;
const n4=v=>Math.abs(v)<5e-5?'0.0000':v.toFixed(4);
// ===== 그리기 =====
function view(p,R){const s=$('dView');const[W,H]=svgSize(s);if(!W)return;
 const k=Math.min(W/5.4,H/4.6),ox=W*0.5,oy=H*0.55;
 const Pp=v=>[ox+k*(v[1]*0.95-v[0]*0.62),oy-k*(v[2]*0.95+v[0]*0.28+v[1]*0.12)];
 const ln=(a,b,c,w=1.4,d='')=>{const A=Pp(a),B=Pp(b);return`<line x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}" stroke="${c}" stroke-width="${w}" ${d?`stroke-dasharray="${d}"`:''}/>`};
 const ar=(a,b,c,lab,w=4)=>{const A=Pp(a),B=Pp(b),dx=B[0]-A[0],dy=B[1]-A[1],L=Math.hypot(dx,dy);if(L<2)return'';const ux=dx/L,uy=dy/L,hs=Math.min(11,L*.5);
  return`<line x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}" stroke="${c}" stroke-width="${w}"/><polygon points="${B[0]},${B[1]} ${B[0]-hs*ux+hs*.5*uy},${B[1]-hs*uy-hs*.5*ux} ${B[0]-hs*ux-hs*.5*uy},${B[1]-hs*uy+hs*.5*ux}" fill="${c}"/>${lab?`<text x="${B[0]+5}" y="${B[1]-4}" font-size="12" font-weight="700" fill="${c}">${lab}</text>`:''}`};
 let g='';for(let i=-2;i<=2;i+=1){g+=ln([i,-2,0],[i,2,0],'#eef1f4',1)+ln([-2,i,0],[2,i,0],'#eef1f4',1)}
 g+=ln([-2.2,0,0],[2.2,0,0],'#1c2230')+ln([0,-2.2,0],[0,2.2,0],'#1c2230')+ln([0,0,-2],[0,0,2.2],'#1c2230');
 [[2.3,0,0,'x'],[0,2.35,0,'y'],[0,0,2.3,'z']].forEach(v=>{const A=Pp(v);g+=`<text x="${A[0]+3}" y="${A[1]+4}" font-size="13">${v[3]}</text>`});
 g+=ln([p[0],p[1],0],p,'#9aa3b0',1,'3 3')+ln([0,0,0],[p[0],p[1],0],'#9aa3b0',1,'3 3');
 const cols=['#d4691f','#1f7a8c','#7a3fd6'],nm=SYS[sys].q;
 R.e.forEach((e,i)=>{const L=R.h[i]*0.3*2;g+=ar(p,[p[0]+e[0]*L,p[1]+e[1]*L,p[2]+e[2]*L],cols[i],nm[i]+' 쪽',3)});
 const gc=toCartVec(R.grad,R.e),gn=nrm(gc);if(gn>1e-6){const L=Math.min(1.4,0.35*gn)/gn;g+=ar(p,[p[0]+gc[0]*L,p[1]+gc[1]*L,p[2]+gc[2]*L],'#24345c','∇f',5)}
 const A=Pp(p);g+=`<circle cx="${A[0]}" cy="${A[1]}" r="6" fill="#1c2230"/>`;s.innerHTML=g}
function bars(R){const s=$('dBars');const[W,H]=svgSize(s);if(!W)return;const nm=SYS[sys].q,cols=['#d4691f','#1f7a8c','#7a3fd6'];
 const mx=Math.max(1,...R.grad.map(Math.abs),nrm(R.grad));const mid=H*0.5,sc=(H*0.38)/mx,bw=Math.min(70,W/7);
 let g=`<line x1="20" y1="${mid}" x2="${W-10}" y2="${mid}" stroke="#1c2230"/>`;
 const vals=[...R.grad,nrm(R.grad)],labs=[...nm.map(n=>n+' 쪽'),'크기 |∇f|'];
 vals.forEach((v,i)=>{const x=30+i*(W-50)/4,hgt=Math.abs(v)*sc,c=i<3?cols[i]:'#24345c';
  g+=`<rect x="${x}" y="${v>=0?mid-hgt:mid}" width="${bw}" height="${Math.max(1,hgt)}" fill="${c}" opacity="${i<3?.85:1}" rx="3"/><text x="${x+bw/2}" y="${v>=0?mid-hgt-6:mid+hgt+16}" font-size="13" font-weight="700" text-anchor="middle" fill="${c}">${n4(v).replace(/0+$/,'').replace(/\.$/,'')||'0'}</text><text x="${x+bw/2}" y="${H-8}" font-size="12" text-anchor="middle">${labs[i]}</text>`});
 s.innerHTML=g}
// ===== 메인 =====
function draw(){const p=P(),fi=+$('dF').value,ai=+$('dA').value;const rho=Math.hypot(p[0],p[1]),r=Math.hypot(...p);
 const sing=rho<0.02||r<0.05;
 const RS={};for(const k of ['C','Y','S']){RS[k]=(k!=='C'&&sing)?null:calc(k,p,fi,ai)}
 const R=RS[sys]||RS.C;seen[sys]=seen[sys]||(touched&&fi===3);
 // 성적표
 const dV=(sys==='C'?1:sys==='Y'?rho:r*r*Math.sin(SYS.S.fromC(p)[1]))*0.001;
 const mags=Object.values(RS).filter(Boolean).map(x=>nrm(x.grad)),spread=Math.max(...mags)-Math.min(...mags);
 const qn=SYS[sys].q;
 $('dScore').innerHTML=`<div><span>${SYS[sys].name} 자로 읽은 점</span><b>${RS[sys]?fq(sys,R.q):'읽을 수 없음'}</b><small>${qn.join(', ')}</small></div>`+
  `<div class="${RS[sys]&&Math.min(...R.h)<0.05?'warn':''}"><span>한 걸음의 실제 길이 h</span><b>${R.h.map(v=>v.toFixed(2)).join(' · ')}</b><small>${qn.join(' · ')} 쪽</small></div>`+
  `<div class="${dV<0.0002?'warn':''}"><span>작은 상자 dV (눈금 0.1씩)</span><b>${dV.toFixed(5)}</b><small>h₁h₂h₃ × 0.001</small></div>`+
  `<div class="${spread<1e-3?'ok':'warn'}"><span>∇f 크기</span><b>${nrm(R.grad).toFixed(4)}</b><small>${sing?'원통·지구본 자는 이 점에서 쓸 수 없음':spread<1e-3?'세 자 모두 같음 ✓':'차이 '+spread.toExponential(1)}</small></div>`;
 // 비교표
 let t=`<thead><tr><th>자</th><th>좌표</th><th>∇f 성분</th><th>|∇f|</th><th>∇·A</th><th>|∇×A|</th><th>∇²f</th></tr></thead><tbody>`;
 for(const k of ['C','Y','S']){const x=RS[k];if(!x){t+=`<tr><td>${SYS[k].name}</td><td colspan="6">이 점(축 위)에서는 각도 쪽 방향이 없어 쓸 수 없습니다</td></tr>`;continue}
  t+=`<tr class="${k===sys?'cur':''}"><td>${SYS[k].name}</td><td>${fq(k,x.q)}</td><td>(${x.grad.map(n4).join(', ')})</td><td>${n4(nrm(x.grad))}</td><td>${n4(x.div)}</td><td>${n4(nrm(x.curl))}</td><td>${n4(x.lap)}</td></tr>`}
 $('dCmp').innerHTML=t+'</tbody>';
 view(p,R);bars(R);
 // 대사
 const lapS=Object.values(RS).filter(Boolean).map(x=>x.lap),ls=Math.max(...lapS)-Math.min(...lapS);
 $('lnHaru').textContent=`f = ${FNAME[fi]}를 ${SYS[sys].name} 자로 읽었어요. ∇f 성분은 (${R.grad.map(v=>v.toFixed(2)).join(', ')}), 크기는 ${nrm(R.grad).toFixed(3)}이에요.`;
 $('lnRobo').textContent=sing?'앗, 축 위라 각도 쪽 한 걸음이 0이에요. 0으로 나누기는 주판으로도 못 해요!':`세 자로 계산한 라플라시안 차이는 최대 ${ls<5e-5?'0.0000':ls.toFixed(4)}! 발산 ∇·A = ${R.div.toFixed(3)}, 회전 크기 ${nrm(R.curl).toFixed(3)}입니다.`;
 $('lnFly').textContent=r<0.4?'중심에 너무 가까워. 1/r 같은 함수는 숫자가 갑자기 커지니까, 값을 믿기 전에 위치부터 확인해.':sys==='C'?'원통이나 지구본 자를 눌러 봐. 화살표 길이(h)가 달라지는데 ∇f 크기는 그대로인지 봐.':'막대 세 개는 바뀌었지? 그런데 마지막 "크기" 막대도 바뀌었는지 확인해 봐.';
 // 미션
 if(touched){
  if(!done[0]&&sys==='Y'&&RS.Y&&Math.abs(RS.Y.h[1]-2)<=0.05)done[0]=true;
  if(!done[1]&&fi===3&&seen.C&&seen.Y&&seen.S&&ls<1e-3)done[1]=true;
  if(!done[2]&&sys==='S'&&r>=0.5&&dV<0.0002)done[2]=true}
 done.forEach((d,i)=>$('m'+(i+1)).classList.toggle('done',d));const n=done.filter(Boolean).length;
 $('mSum').textContent=`미션 ${n} / 3 통과`+(n===3?' — 0편 복습 끝!':'');
 $('lnDoc').textContent=n===3?'세 미션 모두 통과. 자는 모양에 맞춰 고르고, 한 걸음 h를 챙기면 결과는 같습니다. 1부로 가 봅시다.':n>0?`미션 ${n}개 통과. 표의 맨 오른쪽 세 줄이 같은 숫자인지 계속 확인하세요.`:'자를 바꿔도 표의 |∇f|, ∇·A, ∇²f가 같게 나오는지 보세요. 그게 "같은 ∇, 다른 자"입니다.';
 const sounds=n===3?['(짝짝짝)','(끄덕끄덕)','(반짝반짝)']:n>0?['(휴…)','(오!)','(두근)']:['(조마조마)','(꿀꺽)','(…!)'];
 ['xs1','xs2','xs3'].forEach((id,i)=>$(id).textContent=sounds[i])}
['dx','dy','dz'].forEach(id=>{$(id).addEventListener('input',()=>{touched=true});bindSl(id,v=>v.toFixed(2),draw)()});
['dF','dA'].forEach(id=>$(id).addEventListener('change',()=>{touched=true;if(id==='dF'){seen.C=seen.Y=seen.S=false}draw()}));
$('dReset').onclick=()=>{$('dx').value=1;$('dy').value=1;$('dz').value=1.41;['dx','dy','dz'].forEach(id=>$(id).dispatchEvent(new Event('input')))};
let tm=null;$('dPlay').onclick=()=>{if(tm){clearInterval(tm);tm=null;$('dPlay').textContent='자 바꿔 가며 보기';return}
 const order=['C','Y','S'];let i=order.indexOf(sys);
 if(matchMedia('(prefers-reduced-motion: reduce)').matches){pick(order[(i+1)%3]);return}
 $('dPlay').textContent='멈추기';let n=0;tm=setInterval(()=>{i=(i+1)%3;pick(order[i]);if(++n>=6){clearInterval(tm);tm=null;$('dPlay').textContent='자 바꿔 가며 보기'}},1500)};
obs($('dView'),draw);
"""

PACK_DATA = {"page": "벡터 분석 랩 0편 복습 대시보드 — 좌표계 놀이터", "author": "안상선 ((주)M-Robo)",
             "url": "https://adminmrobo.github.io/vector_analysis_lab/dash_00.html",
             "computes": ["gradient", "divergence", "curl", "scalar Laplacian"], "systems": ["직교", "원통", "구면"],
             "method": "카드 4/4 일반 직교곡선좌표 식 + 중심 차분",
             "missions": ["원통 자 h_φ = 2", "f = 1/r 라플라시안 세 자 동일", "구면 자 dV < 0.0002"],
             "cite": "안상선 (2026). 벡터 분석 랩 0편 복습 대시보드. https://adminmrobo.github.io/vector_analysis_lab/dash_00.html"}

if __name__ == '__main__':
    n = page('dash_00.html', '벡터 분석 랩 0편 대시보드 — 좌표계 놀이터',
             '함수와 화살표 밭을 고르고 점과 자를 바꿔, 기울기·발산·회전·라플라시안이 세 자에서 같은 값인지 직접 확인하는 복습 대시보드.',
             'assets/og/00.webp', body(), PAGE_JS, PACK_DATA, ['좌표계', '축척 인자', '기울기', '발산', '회전', '라플라시안'])
    print('dash00 bytes', n)
