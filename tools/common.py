# -*- coding: utf-8 -*-
"""vector_analysis_lab 공용 조각: 스타일, 캐릭터 그림, 말풍선, 페이지 틀."""
import base64, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PACK = pathlib.Path('/home/claude/adminmrobo/ahnboat_lab_explainer/packs/character/character_pack/webp/96')

NAME = {'asst': '하루', 'doc': '박사', 'fly': '초파리 연구원', 'robo': '주판봇',
        'sia': '시아', 'moa': '모아', 'x1': '미공개 X1', 'x2': '미공개 X2', 'x3': '미공개 X3'}

AUTHOR = '글 · 안상선 (<a href="https://adminmrobo.github.io/who_am_i/who_am_i.html">https://adminmrobo.github.io/who_am_i/who_am_i.html</a>) · (주)M-Robo'

EXTRA_CSS = r"""
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

NAV = [('index.html', '목차'), ('00_orientation.html', '0편 네 개의 자'), ('01_everyday.html', '1부 생활')]

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
