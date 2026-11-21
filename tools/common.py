# -*- coding: utf-8 -*-
"""vector_analysis_lab 공용 조각: 스타일, 캐릭터 그림, 말풍선, 페이지 틀."""
import base64, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PACK = pathlib.Path('/home/claude/adminmrobo/ahnboat_lab_explainer/packs/character/character_pack/webp/96')

NAME = {'asst': '하루', 'doc': '박사', 'fly': '초파리 연구원', 'robo': '주판봇',
        'sia': '시아', 'moa': '모아', 'x1': '미공개 X1', 'x2': '미공개 X2', 'x3': '미공개 X3'}

AUTHOR = '글 · 안상선 (<a href="https://adminmrobo.github.io/who_am_i/who_am_i.html">https://adminmrobo.github.io/who_am_i/who_am_i.html</a>) · (주)M-Robo'

EXTRA_CSS = r"""
.dash{display:grid;grid-template-columns:minmax(0,320px) minmax(0,1fr);gap:16px;margin:16px 0}
@media(max-width:860px){.dash{grid-template-columns:minmax(0,1fr)}}
.panel{border:1px solid var(--line);border-radius:16px;padding:14px;background:#fff}
.panel h3{margin:0 0 8px;font-size:16px}
.grp{border-radius:12px;padding:10px 12px;margin:8px 0}
.grp.env{background:#eef8f0;border:1px solid #bfe3c8}.grp.env>b{color:#1e8a4c}
.grp.me{background:#eef2fb;border:1px solid #c5d0ea}.grp.me>b{color:#24345c}
.grp>b{display:block;font-size:13px;margin-bottom:4px}
.grp .sl{grid-template-columns:5.6em minmax(0,1fr) 3.8em}
.grp .btn{min-height:40px;padding:0 12px;font-size:14px}
.score{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:10px 0}
@media(max-width:860px){.score{grid-template-columns:repeat(2,minmax(0,1fr))}}
.score div{border:1px solid var(--line);border-radius:12px;padding:10px 12px;background:#fff;min-width:0}
.score div span{display:block;font-size:12.5px;color:var(--mute)}
.score div b{display:block;font-size:19px;font-variant-numeric:tabular-nums;overflow-wrap:anywhere}
.score div small{font-size:12.5px}
.score .ok{border-color:#9fd4b2;background:#f1faf4}.score .warn{border-color:#f1c27d;background:#fff8ec}
.figs{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px}
@media(max-width:860px){.figs{grid-template-columns:minmax(0,1fr)}}
.figs .fig{min-height:320px}
.figs .cap{font-size:13px;color:var(--mute);margin:4px 2px 0}
.missions{display:grid;gap:8px;margin:12px 0;padding:0;list-style:none}
.missions li{border:1px solid var(--line);border-radius:12px;padding:10px 12px 10px 44px;position:relative;line-height:1.6}
.missions li::before{content:"";position:absolute;left:12px;top:12px;width:20px;height:20px;border-radius:6px;border:2px solid #9aa3b0}
.missions li.done{border-color:#9fd4b2;background:#f1faf4}
.missions li.done::before{background:#1e8a4c;border-color:#1e8a4c}
.missions li.done::after{content:"✓";position:absolute;left:16px;top:9px;color:#fff;font-weight:900}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
.tabs .btn[aria-selected=true]{background:var(--navy);color:#fff;border-color:var(--navy)}
.ctab[hidden]{display:none}
table.cmp{width:100%;border-collapse:collapse;font-size:14px;font-variant-numeric:tabular-nums}
table.cmp th,table.cmp td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:right;white-space:nowrap}
table.cmp th:first-child,table.cmp td:first-child{text-align:left}
table.cmp tr.cur td{background:#eef2fb;font-weight:700}
.dashlink{display:block;border:2px solid var(--teal);border-radius:16px;padding:14px 18px;margin:20px 0;text-decoration:none;color:var(--ink);background:#f3fafb}
.dashlink b{color:var(--teal)}

nav.top{position:sticky;top:0;z-index:20;height:54px;display:flex;align-items:center;gap:14px;overflow-x:auto;white-space:nowrap;padding:0 max(4vw,16px);background:rgba(255,255,255,.92);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);font-size:14px}
nav.top a{text-decoration:none;color:var(--ink)}nav.top a.home{font-weight:900;color:var(--navy)}nav.top a[aria-current]{color:var(--org);font-weight:700}
.crowd{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:10px 0;padding:8px 12px;border:1px dashed #b9c2d0;border-radius:14px;background:#fbfcfe}
.crowd .seat{display:flex;align-items:center;gap:6px;font-size:14px;color:var(--mute)}
.crowd img{width:44px;height:44px;border-radius:10px;image-rendering:pixelated;background:#fff;border:1px solid var(--line)}
.crowd .lab0{font-size:13px;font-weight:700;color:var(--navy);margin-right:4px}
.drnote{border:2px solid var(--c-doc,#7a3fd6);background:#f6f1fd;border-radius:16px;padding:14px 16px;margin:14px 0;display:grid;grid-template-columns:52px minmax(0,1fr);gap:12px;align-items:start}
.drnote img{width:52px;height:52px;border-radius:12px;image-rendering:pixelated;border:1px solid var(--line);background:#fff}
.drnote b.h{display:block;color:#5b2fa8;margin-bottom:2px}
.t.asst div{background:#fdeef5}
.t.x div{background:#f1f2f6;color:var(--mute)}
.toc{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.toc a,.toc div.soon{display:block;border:1px solid var(--line);border-radius:16px;padding:16px 18px;text-decoration:none;color:var(--ink);background:#fff;line-height:1.6}
.toc b.n{display:block;font-size:13px;color:var(--mute);font-weight:500}
.toc .soon{background:var(--soft);color:var(--mute)}
.toc .p0{border-left:6px solid var(--navy)}.toc .p1{border-left:6px solid var(--teal)}.toc .p2{border-left:6px solid var(--org)}.toc .p3{border-left:6px solid #7a3fd6}
@media(max-width:700px){.toc{grid-template-columns:minmax(0,1fr)}}
.cardrow{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:12px 0}
.cardrow div{border:1px solid var(--line);border-radius:14px;padding:12px;background:#fff;line-height:1.55}
.cardrow div b{display:block}.cardrow div span{font-size:14px;color:var(--mute)}
@media(max-width:860px){.cardrow{grid-template-columns:repeat(2,minmax(0,1fr))}}
.nextp{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:30px}
.nextp a{flex:1 1 240px;border:1px solid var(--line);border-radius:14px;padding:12px 16px;text-decoration:none;color:var(--ink)}
.nextp a b{display:block;font-size:13px;color:var(--mute);font-weight:500}
"""

def b64(path):
    return 'data:image/webp;base64,' + base64.b64encode(path.read_bytes()).decode()

def sprite_map(keys):
    out = {}
    for k in sorted(set(keys)):
        who, e = k.split('/')
        p = PACK / who / f'{who}_{e.lower()}.webp'
        if not p.exists():
            raise SystemExit(f'sprite missing: {k}')
        out[k] = b64(p)
    return out

USED = []

def T(key, text, cls=''):
    """말풍선 한 줄. key 예: 'asst/E20'"""
    USED.append(key)
    who = key.split('/')[0]
    c = cls or {'doc': 'edu', 'robo': 'bot', 'fly': 'fly', 'asst': 'asst'}.get(who, '')
    if who.startswith('x'):
        c = 'x'
    return f'<div class="t {c}" data-c="{key}"><div><b>{NAME[who]}</b>{text}</div></div>'

def talk(*lines):
    return '<div class="talk">' + ''.join(lines) + '</div>'

def crowd(label, seats):
    """방청석: seats = [(key, 소리), ...]  미공개 식구는 소리만 낸다."""
    h = f'<div class="crowd" aria-label="방청석"><span class="lab0">{label}</span>'
    for k, s in seats:
        USED.append(k)
        h += f'<span class="seat"><img data-k="{k}" alt="{NAME[k.split("/")[0]]}">{s}</span>'
    return h + '</div>'

def dr(text, key='doc/E16', head='박사의 정리'):
    USED.append(key)
    return f'<div class="drnote"><img data-k="{key}" alt="박사"><div><b class="h">{head}</b>{text}</div></div>'

def quiz(q, opts, ans, ok, no):
    o = ''.join(f'<button class="btn" data-o="{k}">{v}</button>' for k, v in opts)
    return (f'<div class="quiz" data-ans="{ans}"><div class="q">{q}</div><div class="opts">{o}</div>'
            f'<div class="fb" data-ok="{ok}" data-no="{no}" aria-live="polite"></div></div>')

def eqtable(rows):
    r = ''.join(f'<tr><td class="m">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    return ('<details class="eq"><summary>식으로 보면 (몰라도 됩니다)</summary><table><thead><tr><th>식 조각</th>'
            f'<th>읽는 법</th><th>뜻</th></tr></thead><tbody>{r}</tbody></table></details>')

def codebox(lines):
    r = ''.join(f'<tr><td><code>{c}</code></td><td>{m}</td></tr>' for c, m in lines)
    return ('<details><summary>파이썬 코드로 보면 (몰라도 됩니다)</summary><div class="scroll"><table><tbody>'
            f'{r}</tbody></table></div></details>')

NAV = [('index.html', '목차'), ('00_orientation.html', '0편 네 개의 자'), ('dash_00.html', '0편 대시보드'),
       ('01_everyday.html', '1부 생활'), ('dash_01.html', '1부 대시보드'),
       ('02_economy.html', '2부 경제·금융'), ('dash_02.html', '2부 대시보드'),
       ('03_ai_ml.html', '3부 AI·머신러닝'), ('dash_03.html', '3부 대시보드')]

def nav(cur):
    a = '<a class="home" href="index.html">벡터 분석 랩</a>'
    for href, t in NAV:
        cur_attr = ' aria-current="page"' if href == cur else ''
        a += f'<a href="{href}"{cur_attr}>{t}</a>'
    return f'<nav class="top" aria-label="시리즈 목차">{a}</nav>'

COMMON_JS = r"""
const $=id=>document.getElementById(id);
const fill=()=>{document.querySelectorAll('.t[data-c]').forEach(t=>{if(t.querySelector(':scope>img'))return;const k=t.dataset.c;const im=document.createElement('img');im.src=SP[k]||'';im.alt='';im.setAttribute('aria-hidden','true');t.prepend(im)});
 document.querySelectorAll('img[data-k]').forEach(im=>{im.src=SP[im.dataset.k]||''})};
fill();
document.querySelectorAll('.quiz').forEach(q=>{const fb=q.querySelector('.fb');q.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
 q.querySelectorAll('button').forEach(x=>x.classList.remove('right','wrong'));const ok=b.dataset.o===q.dataset.ans;b.classList.add(ok?'right':'wrong');fb.textContent=ok?fb.dataset.ok:fb.dataset.no}))});
const bindSl=(id,fmt,cb)=>{const el=$(id),o=$(id+'o');const f=()=>{o.textContent=fmt(+el.value);cb()};el.addEventListener('input',f);return f};
const svgSize=s=>{const r=s.getBoundingClientRect();return[r.width,r.height]};
const obs=(el,fn)=>{const ro=new ResizeObserver(()=>fn());ro.observe(el);return ro};
const D2R=Math.PI/180,R2D=180/Math.PI;
const fmt=(v,d=0)=>v.toLocaleString('ko-KR',{minimumFractionDigits:d,maximumFractionDigits:d});
if($('copyPack')){$('pack').textContent=JSON.stringify(PACK,null,2);$('copyPack').addEventListener('click',()=>{try{navigator.clipboard.writeText($('pack').textContent).then(()=>$('copyMsg').textContent='복사했습니다.',()=>$('copyMsg').textContent='아래 글을 직접 선택해 복사해 주세요.')}catch(e){$('copyMsg').textContent='아래 글을 직접 선택해 복사해 주세요.'}})}
"""

def page(fname, title, desc, og_img, body, page_js, pack, teaches):
    css = (ROOT / 'tools/base.css').read_text(encoding='utf-8') + EXTRA_CSS
    css = css.replace('PICTURE: 방마다 직접 움직이는 실험 패널(3D 로봇 팔, 드론 지도, 옵션 가격 언덕)',
                      'PICTURE: 방마다 직접 움직이는 실험 패널(SVG)')
    css = re.sub(r'/\* VOICE:.*?\*/', '/* VOICE: 낮의 연구실 — 하루의 첫 수업. IDEA: 같은 화살표, 네 개의 자. COLOUR: 흰 바탕, 틸·주황·남색 */', css, flags=re.S)
    sp = sprite_map(USED)
    ld = {"@context": "https://schema.org", "@type": "LearningResource", "name": title, "inLanguage": "ko",
          "author": {"@type": "Person", "name": "안상선", "affiliation": "(주)M-Robo"},
          "teaches": teaches, "isPartOf": "벡터 분석 랩 — 네 개의 자로 읽는 화살표"}
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&family=Noto+Serif:ital@1&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{css}</style>
</head>
<body>
{nav(fname)}
{body}
<script>
{{
const SP={json.dumps(sp)};
const PACK={json.dumps(pack, ensure_ascii=False)};
{COMMON_JS}
{page_js}
}}
</script>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding='utf-8')
    USED.clear()
    return len(html.encode())


# ---------- 본문 방 조각 (1~3부 공용) ----------
def room_head(part, n, title, tags):
    t = ''.join(f'<span>{x}</span>' for x in tags)
    return f'<section class="room" id="room-{n}">\n<div class="wing">{part} · 방 {n}</div>\n<h2>{title}</h2>\n<div class="tags">{t}</div>\n'

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

def three(items, note):
    li = ''.join(f'<li><b>{a}:</b> {b}</li>' for a, b in items)
    return f'<div class="three"><h2>처음 오신 분께 — 이 페이지를 3줄로</h2><ol>{li}</ol><p style="margin:0">{note}</p></div>'

def tail_sections(kg_links, foot):
    kg = ''.join(f'<a href="#{h}">{t}</a>' for h, t in kg_links)
    return f"""
<section id="kg"><h2>지식 색인</h2><p>이 페이지의 개념과 나오는 방입니다.</p><div class="kg">{kg}</div></section>
<section id="export"><h2>온톨로지·서지 꾸러미</h2><p>이 페이지의 개념 관계와 인용 정보입니다. 다른 도구로 옮길 때 복사해 쓰세요.</p>
<div class="btns"><button class="btn" id="copyPack">꾸러미 복사</button><span id="copyMsg" style="align-self:center;font-size:14px;color:var(--mute)" aria-live="polite"></span></div>
<pre id="pack"></pre></section>
</main>
<footer><div class="wrap">{AUTHOR}<br>{foot}</div></footer>
"""
