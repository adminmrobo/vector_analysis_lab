# -*- coding: utf-8 -*-
"""390·1280px 화면 점검: 가로 넘침, 콘솔 오류, 빈 그림, 스크린샷."""
import sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
pages = sys.argv[1:] or ['index.html', '00_orientation.html', '01_everyday.html']
out = pathlib.Path('/tmp/shots'); out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    for name in pages:
        for w in (390, 1280):
            pg = b.new_page(viewport={'width': w, 'height': 900})
            errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.route('**/fonts.googleapis.com/**', lambda r: r.abort())
            pg.goto((ROOT / name).as_uri())
            pg.wait_for_timeout(700)
            ov = pg.evaluate('document.documentElement.scrollWidth - window.innerWidth')
            empty = pg.evaluate("[...document.images].filter(i=>!i.getAttribute('src')||(i.complete&&i.naturalWidth===0)).map(i=>i.alt||i.dataset.k||i.closest('[data-c]')?.dataset.c||'?')")
            wide = pg.evaluate("""(()=>{const W=window.innerWidth;return [...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>W+1&&!e.closest('.scroll,pre,nav.top')}).slice(0,5).map(e=>e.tagName+'.'+e.className+'#'+e.id)})()""")
            errs = [e for e in errs if 'fonts.g' not in e and 'ERR_FAILED' not in e]
            print(f'{name} @{w}: overflow={ov} empty={empty} wide={wide} errors={errs[:3]}')
            pg.screenshot(path=str(out / f'{name}_{w}.png'), full_page=True)
            pg.close()
    b.close()
