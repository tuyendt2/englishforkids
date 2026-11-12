"""Tạo web tĩnh (PWA cài được lên Android/iOS) từ dữ liệu.  Chạy:  python3 build.py

Dữ liệu:  _data.py + _grammar.py (Lớp 1-4) · _data_lop05.py … _data_lop12.py (mỗi file có TOPICS và GRAMMAR)
TOEIC:    _toeic_tu_loai.py, _toeic_ngu_phap.py
Kết quả:  index.html, ngu-phap.html, toeic.html, chu-de/*.html, toeic/*.html, manifest.webmanifest, sw.js, icons/
"""
import hashlib, html, importlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _data import TOPICS as T1
from _grammar import GRAMMAR as G1

TOPICS, GRAMMAR = list(T1), dict(G1)
_MODULES = [f"_data_lop{g:02d}" for g in range(5, 13)] + ["_data_c1", "_data_c2", "_data_fluent", "_data_native"]
for _name in _MODULES:
    _m = importlib.import_module(_name)
    TOPICS += _m.TOPICS
    GRAMMAR.update(_m.GRAMMAR)
_slugs = [t[0] for t in TOPICS]
assert len(_slugs) == len(set(_slugs)), "Trùng slug chủ đề"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "chu-de")
os.makedirs(OUT, exist_ok=True)
e = html.escape
APP_NAME, SHORT_NAME, THEME = "English for Kids – Lớp 1–12 & Người lớn", "English Kids", "#ff7aa2"

LEVELS = [("tieu-hoc", "🎈 Tiểu học", "Lớp 1 – 5", range(1, 6)),
          ("thcs", "📗 Trung học cơ sở", "Lớp 6 – 9", range(6, 10)),
          ("thpt", "🎓 Trung học phổ thông", "Lớp 10 – 12", range(10, 13)),
          ("nguoi-lon", "🧑‍🎓 Sinh viên & Người lớn", "C1 · C2 · Fluent · Native", range(13, 17))]

# Trình độ người lớn được mã hóa thành "lớp" 13–16 để dùng chung bộ lọc
ADULT = {"C1": 13, "C2": 14, "Fluent": 15, "Native": 16}
ADULT_NAME = {13: "C1 – Advanced (Nâng cao)", 14: "C2 – Proficiency (Thành thạo)",
              15: "Fluent – Lưu loát", 16: "Native – Như người bản xứ"}
CHIP_LABEL = {g: f"Lớp {g}" for g in range(1, 13)} | {v: k for k, v in ADULT.items()}

def grades(g):
    if g in ADULT:
        return [ADULT[g]]
    n = [int(x) for x in re.findall(r"\d+", g)]
    return list(range(n[0], n[-1] + 1))

def level_of(g):
    return next(L for L in LEVELS if grades(g)[0] in L[3])

# ───────────────────────── CSS / JS ─────────────────────────
CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:'Segoe UI','Nunito',system-ui,Arial,sans-serif;background:#fffaf2;color:#333;overflow-x:hidden}
header{padding:calc(24px + env(safe-area-inset-top)) 16px 22px;text-align:center;color:#fff;background:var(--c);border-radius:0 0 32px 32px;box-shadow:0 6px 18px rgba(0,0,0,.12)}
header .big{font-size:60px;line-height:1}
header h1{margin:8px 0 4px;font-size:clamp(26px,6vw,34px)}
header p{margin:0;font-size:17px;opacity:.95}
.badge{display:inline-block;background:#fff;color:var(--c);font-weight:700;border-radius:20px;padding:3px 12px;font-size:14px;margin-top:8px}
main{max-width:1150px;margin:0 auto;padding:20px 16px calc(60px + env(safe-area-inset-bottom))}
h2{font-size:23px;margin:28px 0 14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
h2 small{font-size:15px;font-weight:600;color:#888}
.toolbar{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:14px}
.btn{border:none;background:#fff;color:var(--c);font-weight:700;padding:8px 16px;border-radius:20px;cursor:pointer;font-size:15px;text-decoration:none;box-shadow:0 2px 6px rgba(0,0,0,.12);font-family:inherit}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(205px,1fr));gap:16px}
.card{background:#fff;border-radius:20px;padding:16px 12px 14px;text-align:center;border:3px solid var(--c);box-shadow:0 4px 10px rgba(0,0,0,.06);position:relative;transition:transform .15s}
.card:hover{transform:translateY(-4px) rotate(-1deg)}
.card .ico{font-size:52px;line-height:1.1}
.card .w{font-size:21px;font-weight:800;color:var(--c);margin:6px 0 4px;overflow-wrap:anywhere}
.card .ipa{font-family:'Lucida Sans Unicode','Arial Unicode MS',sans-serif;color:#555;font-size:15px;overflow-wrap:anywhere}
.card .vn{color:#e65100;font-size:15px;margin-top:2px}
.card .vn::before{content:'🗣️ '}
.card .m{margin-top:8px;background:#f3f3f3;border-radius:12px;padding:6px;font-weight:700;font-size:16px}
.say{position:absolute;top:8px;right:8px;border:none;background:none;font-size:20px;cursor:pointer;padding:4px}
.hide .m{color:transparent;background:repeating-linear-gradient(45deg,#ddd,#ddd 6px,#eee 6px,#eee 12px)}
.hide .card:hover .m,.hide .card.show .m{color:#333;background:#f3f3f3}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}
.cols>section>h2{margin-top:28px}
.pat{background:#fff;border-left:8px solid var(--c);border-radius:16px;padding:14px 18px;margin-bottom:12px;box-shadow:0 3px 8px rgba(0,0,0,.05)}
.pat .en{font-size:18px;font-weight:700}
.pat .en .q{color:var(--c)}
.pat .vi{color:#666;margin-top:4px;font-style:italic}
.pat .say,.gram .say{position:static;font-size:17px}
.gram{background:#fff;border:3px solid var(--c);border-radius:20px;padding:16px 18px;margin-bottom:14px;box-shadow:0 3px 8px rgba(0,0,0,.05)}
.gram h3{margin:0 0 10px;color:var(--c);font-size:19px}
.gram h3 a{color:inherit}
.gram .tag{display:inline-block;font-size:13px;font-weight:700;background:var(--c);color:#fff;border-radius:10px;padding:2px 8px;margin-right:6px;vertical-align:middle}
.f{font-family:ui-monospace,'Cascadia Mono',Consolas,monospace;background:#fff6e0;border:1.5px dashed #f0c060;border-radius:10px;padding:7px 10px;margin:6px 0;font-size:15px;font-weight:600;overflow-wrap:anywhere}
.gram ul{margin:8px 0;padding-left:20px;color:#555;line-height:1.55}
.ex{border-top:1px dashed #ddd;padding:7px 0}
.ex .en{font-weight:700}
.ex .vi{color:#666;font-style:italic;font-size:15px}
.legend{background:#fff;border:2px dashed var(--c);border-radius:16px;padding:10px 16px;font-size:15px}
nav.pn{display:flex;justify-content:space-between;margin-top:30px;gap:10px}
nav.pn a{background:var(--c);color:#fff;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:700}
.chips{display:flex;gap:8px;flex-wrap:wrap;position:sticky;top:0;z-index:5;background:#fffaf2;padding:10px 0;margin:0 -2px}
.chip{border:2px solid #ff7aa2;background:#fff;color:#d6336c;border-radius:20px;padding:6px 13px;font-weight:700;cursor:pointer;font-size:15px;font-family:inherit}
.chip.on{background:#ff7aa2;color:#fff}
.topics{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px}
.topic{display:block;text-decoration:none;color:#fff;border-radius:24px;padding:18px;box-shadow:0 6px 14px rgba(0,0,0,.12);transition:transform .15s;text-shadow:0 1px 2px rgba(0,0,0,.25)}
.topic:hover{transform:scale(1.04)}
.topic .ico{font-size:48px}
.topic .t{font-size:20px;font-weight:800;margin-top:6px}
.topic .s{font-size:16px;opacity:.95}
.topic .n{margin-top:10px;font-size:14px;background:rgba(255,255,255,.25);display:inline-block;padding:3px 10px;border-radius:12px}
section[id]{scroll-margin-top:130px}
h3.sub{font-size:18px;margin:20px 0 10px;color:#555;border-left:5px solid #ff7aa2;padding-left:10px}
h3.sub small{font-size:14px;font-weight:600;color:#999}
.special{display:flex;gap:16px;align-items:center;background:linear-gradient(135deg,#7c4dff,#ff7aa2);color:#fff;text-decoration:none;border-radius:24px;padding:18px 22px;box-shadow:0 6px 14px rgba(0,0,0,.12)}
.special .ico{font-size:46px}
.special b{font-size:21px;display:block}
.tips{background:#fff;border-radius:20px;padding:16px 22px;box-shadow:0 3px 8px rgba(0,0,0,.06);line-height:1.7}
.install{display:none}
.ioshint{display:none;background:#fff;color:#333;border-radius:16px;padding:10px 14px;margin:12px auto 0;max-width:420px;font-size:15px;text-shadow:none}
[hidden]{display:none!important}
.toeic{background:linear-gradient(135deg,#1565c0,#00acc1)}
.theory{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px;align-items:start}
.famwrap{overflow-x:auto;background:#fff;border-radius:16px;box-shadow:0 3px 8px rgba(0,0,0,.06)}
.fam{width:100%;border-collapse:collapse;font-size:15px}
.fam th{background:var(--c);color:#fff;text-align:left;padding:9px 12px;position:sticky;top:0}
.fam td{padding:7px 12px;border-top:1px solid #eee;white-space:nowrap}
.fam tr:nth-child(even) td{background:#fafafa}
.scorebar{position:sticky;top:0;z-index:5;background:#fffaf2;padding:10px 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.scorebar .score{font-weight:800;font-size:17px;flex:1;min-width:200px}
.scorebar .btn{border:2px solid var(--c)}
.q{background:#fff;border-radius:16px;padding:14px 16px;margin-bottom:12px;box-shadow:0 3px 8px rgba(0,0,0,.05);border-left:7px solid #ddd}
.q.qok{border-left-color:#2e7d32}.q.qno{border-left-color:#c62828}
.qt{font-size:17px;line-height:1.5}
.blank{display:inline-block;min-width:70px;border-bottom:2px solid var(--c)}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.opts button{text-align:left;border:2px solid #ddd;background:#fafafa;border-radius:12px;padding:9px 12px;font:inherit;font-size:16px;cursor:pointer;color:#333}
.opts button:hover{border-color:var(--c)}
.q.done .opts button{cursor:default}
.opts button.right{background:#e8f5e9;border-color:#2e7d32;color:#1b5e20;font-weight:700}
.opts button.wrong{background:#ffebee;border-color:#c62828;color:#b71c1c;text-decoration:line-through}
.why{margin-top:10px;background:#fff6e0;border-radius:10px;padding:8px 12px;font-size:15px;line-height:1.5}
.why .say{position:static;font-size:16px}
.why a{color:inherit}
.best{margin-left:6px}.best:empty{display:none}
.theory .f{font-family:inherit;font-weight:700}
@media (max-width:860px){.cols{grid-template-columns:1fr;gap:0}}
@media (max-width:480px){.chips{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}.chips::-webkit-scrollbar{display:none}.chip{flex:0 0 auto}section[id]{scroll-margin-top:70px}.grid{grid-template-columns:repeat(2,1fr);gap:10px}.card{padding:12px 6px 10px;border-radius:16px}.card .ico{font-size:40px}.card .w{font-size:17px}.card .ipa,.card .vn,.card .m{font-size:13px}.say{top:2px;right:2px;font-size:17px}.topics{grid-template-columns:1fr 1fr;gap:10px}.topic{padding:14px;border-radius:18px}.topic .ico{font-size:38px}.topic .t{font-size:16px}.topic .s{font-size:14px}.topic .n{font-size:12px}nav.pn a{padding:9px 12px;font-size:14px}.opts{grid-template-columns:1fr}.theory{grid-template-columns:1fr}.qt{font-size:16px}}
@media print{.say,.toolbar,nav.pn,.chips,.scorebar .btn{display:none}.why{display:block!important}.q{break-inside:avoid}header{border-radius:0}.card,.gram{break-inside:avoid}.cols{grid-template-columns:1fr}}
"""

JS = """
function say(t){if(!('speechSynthesis' in window))return alert('Trình duyệt không hỗ trợ đọc.');
speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t.replace(/→/g,'.').replace(/\\//g,' or '));
u.lang='en-GB';u.rate=0.8;const v=speechSynthesis.getVoices().find(v=>v.lang.startsWith('en'));if(v)u.voice=v;speechSynthesis.speak(u);}
function toggleHide(b){document.body.classList.toggle('hide');b.textContent=document.body.classList.contains('hide')?'👁️ Hiện nghĩa':'🙈 Ẩn nghĩa (tự kiểm tra)';}
document.addEventListener('click',ev=>{const c=ev.target.closest('.card');if(c&&!ev.target.closest('.say'))c.classList.toggle('show');});
if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register(document.documentElement.dataset.root+'sw.js').catch(()=>{}));
let deferredPrompt;
addEventListener('beforeinstallprompt',ev=>{ev.preventDefault();deferredPrompt=ev;document.querySelectorAll('.install').forEach(b=>b.style.display='inline-block');});
function installApp(){if(!deferredPrompt)return;deferredPrompt.prompt();deferredPrompt.userChoice.finally(()=>{deferredPrompt=null;document.querySelectorAll('.install').forEach(b=>b.style.display='none');});}
addEventListener('DOMContentLoaded',()=>{const ios=/iphone|ipad|ipod/i.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
const standalone=navigator.standalone||matchMedia('(display-mode: standalone)').matches;const h=document.querySelector('.ioshint');if(h&&ios&&!standalone)h.style.display='block';});
function filterGrade(btn){document.querySelectorAll('.chip').forEach(c=>c.classList.toggle('on',c===btn));const g=btn.dataset.g;
document.querySelectorAll('[data-g]').forEach(el=>{if(el.classList.contains('chip'))return;el.hidden=g!=='all'&&!(' '+el.dataset.g+' ').includes(' '+g+' ');});
document.querySelectorAll('[data-sec]').forEach(s=>{s.hidden=!s.querySelector('[data-g]:not([hidden])');});}
function store(k,v){try{if(v===undefined)return +localStorage.getItem('toeic:'+k)||0;localStorage.setItem('toeic:'+k,v);}catch(e){return 0;}}
function pick(b){const q=b.closest('.q');if(q.classList.contains('done'))return;const ok=!!b.dataset.ok;
q.classList.add('done',ok?'qok':'qno');b.classList.add(ok?'right':'wrong');q.querySelector('[data-ok]').classList.add('right');
q.querySelector('.why').hidden=false;score(q.closest('.quiz'));}
function score(z){const n=z.querySelectorAll('.q').length,d=z.querySelectorAll('.q.done').length,r=z.querySelectorAll('.q.qok').length;
let t='✅ Đúng '+r+'/'+n+' · đã làm '+d+'/'+n;
if(n&&d===n){if(r>store(z.dataset.key))store(z.dataset.key,r);
t+=' — '+(r>=n*.8?'🎉 Xuất sắc!':r>=n*.5?'👍 Khá tốt, xem lại câu sai nhé.':'💪 Đọc lại lý thuyết rồi làm lại nhé.');}
const best=store(z.dataset.key);if(best)t+=' · 🏆 Cao nhất: '+best+'/'+n;z.querySelector('.score').textContent=t;}
function resetQuiz(b){const z=b.closest('.quiz');z.querySelectorAll('.q').forEach(q=>{q.classList.remove('done','qok','qno');
q.querySelector('.why').hidden=true;q.querySelectorAll('.opts button').forEach(o=>o.classList.remove('right','wrong'));});score(z);z.scrollIntoView({behavior:'smooth'});}
function showAll(b){b.closest('.quiz').querySelectorAll('.q:not(.done)').forEach(q=>{q.classList.add('done');q.querySelector('[data-ok]').classList.add('right');q.querySelector('.why').hidden=false;});}
addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('.quiz').forEach(score);
document.querySelectorAll('[data-best]').forEach(el=>{const b=store(el.dataset.best);if(b)el.textContent='🏆 '+b+'/'+el.dataset.n;});});
"""

def page(title, color, body, root=""):
    return f"""<!DOCTYPE html>
<html lang="vi" data-root="{root}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="theme-color" content="{color}">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="{root}icons/icon-192.png">
<link rel="apple-touch-icon" href="{root}icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{SHORT_NAME}">
<style>:root{{--c:{color}}}{CSS}</style><script>{JS}</script></head>
<body>{body}</body></html>"""

def parse(block, n):
    return [[x.strip() for x in l.split("|")] for l in block.strip().splitlines() if l.strip() and len(l.split("|")) == n]

def say_btn(text):
    return f'<button class="say" title="Nghe" onclick="say(this.dataset.t)" data-t="{e(text)}">🔊</button>'

def grammar_html(slug, link=None, tag=None, text=None, icon="📐 "):
    """Chuyển khối ngữ pháp thành HTML. link/tag dùng cho trang tổng hợp; text dùng cho bài TOEIC."""
    out, cur = [], None
    def close():
        if cur is not None:
            notes = f"<ul>{''.join(cur['notes'])}</ul>" if cur["notes"] else ""
            out.append(f'<div class="gram"><h3>{cur["h"]}</h3>{"".join(cur["f"])}{notes}{"".join(cur["ex"])}</div>')
    for line in (text if text is not None else GRAMMAR.get(slug, "")).strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("## "):
            close()
            title = e(line[3:])
            if link:
                title = f'<a href="{link}">{title}</a>'
            if tag:
                title = f'<span class="tag">{e(tag)}</span>{title}'
            cur = {"h": icon + title if not tag else title, "f": [], "notes": [], "ex": []}
        elif cur is None:
            continue
        elif line.startswith("= "):
            cur["f"].append(f'<div class="f">{e(line[2:])}</div>')
        elif line.startswith("- "):
            cur["notes"].append(f"<li>{e(line[2:])}</li>")
        elif "|" in line:
            en_s, vi_s = [x.strip() for x in line.split("|", 1)]
            cur["ex"].append(f'<div class="ex"><div class="en">{e(en_s)} {say_btn(en_s)}</div><div class="vi">🇻🇳 {e(vi_s)}</div></div>')
    close()
    return "".join(out)

missing = [t[0] for t in TOPICS if t[0] not in GRAMMAR]
if missing:
    print("⚠️  Chưa có ngữ pháp cho:", ", ".join(missing))

# ───────────────────────── Trang chủ đề ─────────────────────────
total = 0
pages = ["index.html", "ngu-phap.html"]
for i, (slug, ico, en, vi, grade, color, words, pats) in enumerate(TOPICS):
    ws, ps = parse(words, 5), parse(pats, 2)
    total += len(ws)
    cards = "".join(
        f'<div class="card">{say_btn(w)}'
        f'<div class="ico">{ic}</div><div class="w">{e(w)}</div><div class="ipa">{e(ipa)}</div>'
        + (f'<div class="vn">{e(vn)}</div>' if vn else "")
        + f'<div class="m">{e(m)}</div></div>'
        for ic, w, ipa, vn, m in ws)
    pat_html = ""
    for en_s, vi_s in ps:
        parts = [e(x.strip()) for x in en_s.split("→")]
        en_h = parts[0] if len(parts) == 1 else f'<span class="q">❓ {parts[0]}</span><br>💬 ' + " ".join(parts[1:])
        pat_html += f'<div class="pat"><div class="en">{en_h} {say_btn(en_s)}</div><div class="vi">🇻🇳 {e(vi_s)}</div></div>'
    gram = grammar_html(slug)
    has_vn = any(vn for _, _, _, vn, _ in ws)
    prev = f'<a href="{TOPICS[i-1][0]}.html">⬅️ {e(TOPICS[i-1][3])}</a>' if i else '<span></span>'
    nxt = f'<a href="{TOPICS[i+1][0]}.html">{e(TOPICS[i+1][3])} ➡️</a>' if i + 1 < len(TOPICS) else '<span></span>'
    lvl = level_of(grade)
    body = f"""<header><div class="big">{ico}</div><h1>{e(en)}</h1><p>Chủ đề {i+1}: {e(vi)}</p>
<span class="badge">📘 {e(grade if grade not in ADULT else "Trình độ " + grade)} · {len(ws)} từ · {len(ps)} mẫu câu · ngữ pháp</span>
<div class="toolbar"><a class="btn" href="../index.html#{lvl[0]}">🏠 Trang chủ</a>
<a class="btn" href="../ngu-phap.html">📐 Ngữ pháp</a>
<button class="btn" onclick="toggleHide(this)">🙈 Ẩn nghĩa (tự kiểm tra)</button>
<button class="btn" onclick="window.print()">🖨️ In</button></div></header>
<main><div class="legend">🔊 Bấm loa để nghe &nbsp;|&nbsp; <b>/IPA/</b> = phiên âm quốc tế{' &nbsp;|&nbsp; 🗣️ = phiên âm tiếng Việt (gần đúng)' if has_vn else (' &nbsp;|&nbsp; (n) danh từ · (v) động từ · (adj) tính từ' + (' · (idiom) thành ngữ · (phr v) cụm động từ · (expr) cụm từ cố định · (collocation) kết hợp từ · (slang) tiếng lóng' if grade in ADULT else ''))} &nbsp;|&nbsp; ô xám = nghĩa</div>
<h2>📖 Từ vựng (Vocabulary)</h2><div class="grid">{cards}</div>
<div class="cols"><section><h2>💬 Mẫu câu (Sentence patterns)</h2>{pat_html}</section>
<section><h2>📐 Ngữ pháp (Grammar)</h2>{gram or '<p>Đang cập nhật…</p>'}</section></div>
<nav class="pn">{prev}{nxt}</nav></main>"""
    with open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(page(f"{en} – {vi}", color, body, root="../"))
    pages.append(f"chu-de/{slug}.html")

# Xóa trang chủ đề cũ không còn trong dữ liệu (đổi tên / xóa chủ đề)
for f in os.listdir(OUT):
    if f.endswith(".html") and f"chu-de/{f}" not in pages:
        os.remove(os.path.join(OUT, f))
        print("🗑️  Đã xóa trang cũ:", f)

# ───────────────────────── Bộ lọc lớp ─────────────────────────
def chips():
    return ('<div class="chips"><button class="chip on" data-g="all" onclick="filterGrade(this)">Tất cả</button>'
            + "".join(f'<button class="chip" data-g="{g}" onclick="filterGrade(this)">{CHIP_LABEL[g]}</button>' for g in range(1, 17))
            + "</div>")

# ───────────────────────── Trang chủ ─────────────────────────
def subgroup(g):
    """Nhóm con trong mỗi cấp: chủ đề dùng chung nhiều lớp (Lớp 1–4) hoặc từng lớp riêng."""
    gs = grades(g)
    if gs[0] in ADULT_NAME:
        return ADULT_NAME[gs[0]]
    return "Lớp 1 – 4 (dùng chung)" if len(gs) > 1 or gs[0] < 5 else f"Lớp {gs[0]}"

sections = ""
for key, name, rng, _ in LEVELS:
    items = [(i, t) for i, t in enumerate(TOPICS) if level_of(t[4])[0] == key]
    groups = {}
    for i, t in items:
        groups.setdefault(subgroup(t[4]), []).append((i, t))
    body = ""
    for gname, gitems in groups.items():
        tiles = "".join(
            f'<a class="topic" data-g="{" ".join(map(str, grades(g)))}" style="background:{c}" href="chu-de/{s}.html"><div class="ico">{ic}</div>'
            f'<div class="t">{i+1}. {e(en)}</div><div class="s">{e(vi)}</div>'
            f'<div class="n">📘 {e(g)} · {len(parse(w,5))} từ</div></a>'
            for i, (s, ic, en, vi, g, c, w, p) in gitems)
        gw = sum(len(parse(t[6], 5)) for _, t in gitems)
        body += f'<div data-sec><h3 class="sub">{gname} <small>{len(gitems)} chủ đề · {gw} từ</small></h3><div class="topics">{tiles}</div></div>'
    nw = sum(len(parse(t[6], 5)) for _, t in items)
    sections += f'<section data-sec id="{key}"><h2>{name} <small>{rng} · {len(items)} chủ đề · {nw} từ</small></h2>{body}</section>'

index = f"""<header><div class="big">🎈📚🌈</div><h1>English for Kids</h1>
<p>Từ vựng · Mẫu câu · Ngữ pháp tiếng Anh — Lớp 1 đến Lớp 12, Sinh viên &amp; Người lớn (C1 → Native)</p>
<span class="badge">⭐ {len(TOPICS)} chủ đề · {total} từ vựng · {len(GRAMMAR)} bài ngữ pháp</span>
<div class="toolbar"><button class="btn install" onclick="installApp()">📲 Cài ứng dụng</button>
<a class="btn" href="ngu-phap.html">📐 Tổng hợp ngữ pháp</a>
<a class="btn" href="toeic.html">🎯 Luyện thi TOEIC</a></div>
<div class="ioshint">📲 <b>Cài lên iPhone/iPad:</b> mở bằng Safari → bấm nút <b>Chia sẻ</b> (⬆️) → chọn <b>“Thêm vào MH chính”</b>.</div>
</header>
<main>{chips()}
<a class="special" href="ngu-phap.html"><div class="ico">📐</div><div><b>Tổng hợp ngữ pháp</b>Công thức, cách dùng và ví dụ cho từng lớp — học xong từ vựng thì ôn ngữ pháp nhé!</div></a>
<a class="special toeic" href="toeic.html" style="margin-top:14px"><div class="ico">🎯</div><div><b>Luyện thi TOEIC</b>Danh từ, động từ, tính từ, trạng từ, giới từ… lý thuyết + bài tập trắc nghiệm kiểu Part 5 có chấm điểm và giải thích.</div></a>
{sections}
<h2>💡 Cách học hiệu quả</h2><div class="tips">
1️⃣ Mỗi ngày học <b>5–7 từ mới</b>: nhìn hình 👀 → bấm 🔊 nghe → đọc to 3 lần 🗣️.<br>
2️⃣ Đọc theo <b>phiên âm IPA</b>; phiên âm tiếng Việt (Tiểu học) chỉ để tham khảo cách đọc gần đúng.<br>
3️⃣ Bấm <b>🙈 Ẩn nghĩa</b> để tự kiểm tra: nhìn từ đoán nghĩa, chạm vào thẻ để xem đáp án.<br>
4️⃣ Học <b>mẫu câu</b> theo cặp hỏi ❓ – đáp 💬, rồi đọc phần <b>📐 ngữ pháp</b> bên cạnh để hiểu vì sao câu được viết như vậy.<br>
5️⃣ Sinh viên &amp; người lớn: bắt đầu từ <b>C1/C2</b> để luyện tiếng Anh học thuật, công việc; học <b>Fluent/Native</b> để nói tự nhiên như người bản xứ.<br>
6️⃣ Cài ứng dụng về điện thoại 📲 để học cả khi <b>không có mạng</b>. Cuối tuần ôn lại chủ đề cũ 🔁 — <i>Practice makes perfect!</i> 🏆
</div></main>"""
with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(page(APP_NAME, THEME, index))

# ───────────────────────── Trang tổng hợp ngữ pháp ─────────────────────────
gsec = ""
for key, name, rng, _ in LEVELS:
    items = [(i, t) for i, t in enumerate(TOPICS) if level_of(t[4])[0] == key and t[0] in GRAMMAR]
    blocks = "".join(
        f'<div data-g="{" ".join(map(str, grades(t[4])))}" style="--c:{t[5]}">'
        + grammar_html(t[0], link=f"chu-de/{t[0]}.html", tag=f"{t[4]} · {t[1]} {t[3]}") + "</div>"
        for i, t in items)
    gsec += f'<section data-sec id="{key}"><h2>{name} <small>{rng} · {len(items)} bài</small></h2>{blocks}</section>'
gpage = f"""<header><div class="big">📐</div><h1>Tổng hợp ngữ pháp</h1>
<p>English Grammar — Lớp 1 đến Lớp 12 · C1 → Native</p><span class="badge">📘 {len(GRAMMAR)} bài · mỗi bài gắn với một chủ đề từ vựng</span>
<div class="toolbar"><a class="btn" href="index.html">🏠 Trang chủ</a><a class="btn" href="toeic.html">🎯 Luyện thi TOEIC</a><button class="btn" onclick="window.print()">🖨️ In</button></div></header>
<main>{chips()}{gsec}</main>"""
with open(os.path.join(ROOT, "ngu-phap.html"), "w", encoding="utf-8") as f:
    f.write(page("Ngữ pháp – English for Kids", "#7c4dff", gpage))

# ───────────────────────── Luyện thi TOEIC ─────────────────────────
import random
import _toeic_tu_loai, _toeic_ngu_phap
TOEIC_GROUPS = [(m.GROUP, m.LESSONS) for m in (_toeic_tu_loai, _toeic_ngu_phap)]
TOEIC = [L for _, ls in TOEIC_GROUPS for L in ls]
TOEIC_OUT = os.path.join(ROOT, "toeic")
os.makedirs(TOEIC_OUT, exist_ok=True)
TEST_N = 30

def parse_quiz(L):
    """Trả về list (câu hỏi, [4 đáp án đã xáo], vị trí đúng, giải thích). Kiểm tra định dạng."""
    out = []
    for line in L["quiz"].strip().splitlines():
        f = [x.strip() for x in line.split("|")]
        assert len(f) == 6, f"{L['slug']}: sai định dạng câu hỏi: {line}"
        q, right, *wrong, why = f
        assert q.count("___") == 1, f"{L['slug']}: câu hỏi phải có đúng một ___: {q}"
        assert len({right, *wrong}) == 4, f"{L['slug']}: đáp án trùng nhau: {line}"
        opts = [right] + wrong
        random.Random(hashlib.md5(q.encode()).hexdigest()).shuffle(opts)
        out.append((q, opts, opts.index(right), why))
    return out

def blank(q):
    return e(q).replace("___", '<span class="blank"></span>')

def q_html(n, q, opts, a, why, link=""):
    btns = "".join(f'<button onclick="pick(this)"{" data-ok=1" if k == a else ""}>({"ABCD"[k]}) {e(o)}</button>'
                   for k, o in enumerate(opts))
    return (f'<div class="q"><div class="qt"><b>{n}.</b> {blank(q)}</div><div class="opts">{btns}</div>'
            f'<div class="why" hidden>✅ <b>({"ABCD"[a]}) {e(opts[a])}</b> — {e(why)} {say_btn(q.replace("___", opts[a]))}{link}</div></div>')

def scorebar(extra=""):
    return (f'<div class="scorebar"><span class="score"></span>{extra}'
            '<button class="btn" onclick="showAll(this)">👀 Xem đáp án</button>'
            '<button class="btn" onclick="resetQuiz(this)">🔄 Làm lại</button></div>')

total_q, bank = 0, []
for i, L in enumerate(TOEIC):
    qs = parse_quiz(L)
    total_q += len(qs)
    for q, opts, a, why in qs:
        bank.append({"q": blank(q), "o": [e(o) for o in opts], "a": a, "w": e(why),
                     "s": e(q.replace("___", opts[a])), "l": e(L["vi"]), "u": L["slug"]})
    fam = ""
    if L.get("families"):
        rows = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in parse(L["families"], 4))
        fam = (f'<h2>🌳 Bảng họ từ <small>{len(parse(L["families"], 4))} họ từ hay gặp</small></h2><div class="famwrap"><table class="fam">'
               f'<tr><th>Danh từ (n)</th><th>Động từ (v)</th><th>Tính từ (adj)</th><th>Trạng từ (adv)</th></tr>{rows}</table></div>')
    quiz = "".join(q_html(n + 1, *x) for n, x in enumerate(qs))
    prev = f'<a href="{TOEIC[i-1]["slug"]}.html">⬅️ {e(TOEIC[i-1]["vi"])}</a>' if i else '<a href="../toeic.html">⬅️ Mục lục TOEIC</a>'
    nxt = f'<a href="{TOEIC[i+1]["slug"]}.html">{e(TOEIC[i+1]["vi"])} ➡️</a>' if i + 1 < len(TOEIC) else '<a href="de-tong-hop.html">📝 Đề tổng hợp ➡️</a>'
    body = f"""<header><div class="big">{L["ico"]}</div><h1>{e(L["en"])}</h1><p>Luyện thi TOEIC · Bài {i+1}: {e(L["vi"])}</p>
<span class="badge">🎯 Lý thuyết + {len(qs)} câu luyện tập kiểu Part 5</span>
<div class="toolbar"><a class="btn" href="../toeic.html">🎯 Mục lục TOEIC</a><a class="btn" href="../index.html">🏠 Trang chủ</a>
<a class="btn" href="#bai-tap">✍️ Làm bài tập</a><button class="btn" onclick="window.print()">🖨️ In</button></div></header>
<main><h2>📚 Lý thuyết</h2><div class="theory">{grammar_html(None, text=L["theory"], icon="📌 ")}</div>
{fam}
<section id="bai-tap"><h2>✍️ Bài tập <small>Chọn đáp án đúng nhất (A), (B), (C) hoặc (D)</small></h2>
<div class="quiz" data-key="{L["slug"]}">{scorebar()}{quiz}</div></section>
<nav class="pn">{prev}{nxt}</nav></main>"""
    with open(os.path.join(TOEIC_OUT, L["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(page(f"{L['vi']} – Luyện thi TOEIC", L["color"], body, root="../"))
    pages.append(f"toeic/{L['slug']}.html")

# Đề tổng hợp: chọn ngẫu nhiên TEST_N câu từ toàn bộ ngân hàng mỗi lần làm
TEST_JS = """const BANK=%s,N=%d;let t0=0;
function newTest(){const a=BANK.slice();for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]];}
document.getElementById('qs').innerHTML=a.slice(0,N).map((x,i)=>'<div class="q"><div class="qt"><b>'+(i+1)+'.</b> '+x.q+'</div><div class="opts">'
+x.o.map((o,k)=>'<button onclick="pick(this)"'+(k===x.a?' data-ok=1':'')+'>('+'ABCD'[k]+') '+o+'</button>').join('')
+'</div><div class="why" hidden>✅ <b>('+'ABCD'[x.a]+') '+x.o[x.a]+'</b> — '+x.w+' <button class="say" title="Nghe" onclick="say(this.dataset.t)" data-t="'+x.s+'">🔊</button>'
+'<br>📚 Ôn lại: <a href="'+x.u+'.html">'+x.l+'</a></div></div>').join('');
score(document.querySelector('.quiz'));t0=Date.now();scrollTo({top:0,behavior:'smooth'});}
setInterval(()=>{const z=document.querySelector('.quiz');if(!t0||z.querySelectorAll('.q.done').length===N)return;
const s=Math.floor((Date.now()-t0)/1000);document.getElementById('timer').textContent='⏱️ '+String(s/60|0).padStart(2,'0')+':'+String(s%%60).padStart(2,'0');},1000);
addEventListener('DOMContentLoaded',newTest);""" % (json.dumps(bank, ensure_ascii=False), TEST_N)
body = f"""<header><div class="big">📝</div><h1>TOEIC Part 5 – Đề tổng hợp</h1>
<p>{TEST_N} câu ngẫu nhiên từ ngân hàng {total_q} câu · mỗi lần bấm “Đề mới” là một đề khác</p>
<span class="badge">⏱️ Thi thật: khoảng 10–12 phút cho 30 câu Part 5</span>
<div class="toolbar"><a class="btn" href="../toeic.html">🎯 Mục lục TOEIC</a><a class="btn" href="../index.html">🏠 Trang chủ</a></div></header>
<main><div class="quiz" data-key="de-tong-hop">{scorebar('<b id="timer">⏱️ 00:00</b><button class="btn" onclick="newTest()">🔀 Đề mới</button>')}<div id="qs"></div></div>
<nav class="pn"><a href="{TOEIC[-1]["slug"]}.html">⬅️ {e(TOEIC[-1]["vi"])}</a><a href="../toeic.html">🎯 Mục lục TOEIC</a></nav></main>
<script>{TEST_JS}</script>"""
with open(os.path.join(TOEIC_OUT, "de-tong-hop.html"), "w", encoding="utf-8") as f:
    f.write(page("Đề tổng hợp – Luyện thi TOEIC", "#1565c0", body, root="../"))
pages.append("toeic/de-tong-hop.html")

for f in os.listdir(TOEIC_OUT):
    if f.endswith(".html") and f"toeic/{f}" not in pages:
        os.remove(os.path.join(TOEIC_OUT, f))
        print("🗑️  Đã xóa trang cũ:", f)

# Mục lục TOEIC
tsec, n = "", 0
for gname, ls in TOEIC_GROUPS:
    tiles = ""
    for L in ls:
        n += 1
        k = len(L["quiz"].strip().splitlines())
        tiles += (f'<a class="topic" style="background:{L["color"]}" href="toeic/{L["slug"]}.html"><div class="ico">{L["ico"]}</div>'
                  f'<div class="t">{n}. {e(L["vi"])}</div><div class="s">{e(L["en"])}</div>'
                  f'<div class="n">✍️ {k} câu</div><span class="n best" data-best="{L["slug"]}" data-n="{k}"></span></a>')
    tsec += f'<section><h2>{gname} <small>{len(ls)} bài</small></h2><div class="topics">{tiles}</div></section>'
tpage = f"""<header><div class="big">🎯</div><h1>Luyện thi TOEIC</h1>
<p>Từ loại · Ngữ pháp trọng tâm · Bài tập trắc nghiệm kiểu Part 5 có giải thích</p>
<span class="badge">📘 {len(TOEIC)} bài · {total_q} câu luyện tập · đề tổng hợp ngẫu nhiên</span>
<div class="toolbar"><a class="btn" href="index.html">🏠 Trang chủ</a><a class="btn" href="toeic/de-tong-hop.html">📝 Làm đề tổng hợp</a></div></header>
<main><a class="special toeic" href="toeic/de-tong-hop.html"><div class="ico">📝</div><div><b>Đề tổng hợp {TEST_N} câu</b>Trộn ngẫu nhiên từ tất cả các bài, có bấm giờ — làm sau khi đã học xong các bài bên dưới.</div></a>
{tsec}
<h2>💡 Mẹo làm Part 5 (Incomplete Sentences)</h2><div class="tips">
1️⃣ <b>Nhìn đáp án trước</b>: 4 đáp án cùng gốc khác đuôi (decide / decision / decisive / decisively) → câu hỏi <b>từ loại</b>, chỉ cần xem từ đứng trước và sau chỗ trống.<br>
2️⃣ Đáp án là các thì / dạng của cùng một động từ → tìm <b>trạng từ thời gian</b>, chủ ngữ số ít/số nhiều, có tân ngữ hay không (chủ động / bị động).<br>
3️⃣ Đáp án là because / because of / although / despite → xem sau chỗ trống là <b>mệnh đề</b> (liên từ) hay <b>danh từ</b> (giới từ).<br>
4️⃣ Câu từ loại làm trong <b>10–15 giây</b>; câu cần dịch nghĩa để sau. Không bỏ trống câu nào — TOEIC không trừ điểm câu sai.<br>
5️⃣ Mỗi ngày làm 1 bài, chép lại câu sai vào sổ. Điểm cao nhất của từng bài được lưu trên máy của bạn 🏆.
</div></main>"""
with open(os.path.join(ROOT, "toeic.html"), "w", encoding="utf-8") as f:
    f.write(page("Luyện thi TOEIC – English for Kids", "#1565c0", tpage))
pages.append("toeic.html")

# ───────────────────────── Icon ─────────────────────────
ICONS = os.path.join(ROOT, "icons")
os.makedirs(ICONS, exist_ok=True)

def make_icons():
    from PIL import Image, ImageDraw, ImageFont
    def font(size):
        for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                  "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
                  "/Library/Fonts/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf"]:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        return ImageFont.load_default(size=size)

    def draw(size, pad_ratio, rounded):
        s = 1024
        img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
        bg = Image.new("RGBA", (s, s))
        top, bot = (255, 122, 162), (124, 77, 255)
        px = bg.load()
        for y in range(s):
            t = y / (s - 1)
            col = tuple(int(top[k] + (bot[k] - top[k]) * t) for k in range(3)) + (255,)
            for x in range(s):
                px[x, y] = col
        mask = Image.new("L", (s, s), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, s - 1, s - 1], radius=220 if rounded else 0, fill=255)
        img.paste(bg, (0, 0), mask)
        d = ImageDraw.Draw(img)
        inner = s * (1 - 2 * pad_ratio)
        f1, f2 = font(int(inner * 0.36)), font(int(inner * 0.13))
        cx = s / 2
        d.text((cx, s * 0.44), "ABC", font=f1, fill="white", anchor="mm", stroke_width=6, stroke_fill=(90, 40, 160))
        d.text((cx, s * 0.66), "LỚP 1–12", font=f2, fill=(255, 245, 200), anchor="mm")
        for (x, y, r) in [(0.22, 0.2, 26), (0.8, 0.24, 18), (0.78, 0.8, 22)]:
            d.ellipse([s * x - r, s * y - r, s * x + r, s * y + r], fill=(255, 230, 120))
        return img.resize((size, size), Image.LANCZOS)

    draw(192, 0.08, True).save(os.path.join(ICONS, "icon-192.png"))
    draw(512, 0.08, True).save(os.path.join(ICONS, "icon-512.png"))
    draw(512, 0.18, False).save(os.path.join(ICONS, "icon-maskable-512.png"))
    draw(180, 0.08, False).convert("RGB").save(os.path.join(ICONS, "apple-touch-icon.png"))

if not os.path.exists(os.path.join(ICONS, "icon-512.png")):
    make_icons()
icon_files = sorted("icons/" + f for f in os.listdir(ICONS) if f.endswith(".png"))

# ───────────────────────── Manifest + Service worker ─────────────────────────
manifest = {
    "name": APP_NAME, "short_name": SHORT_NAME, "lang": "vi",
    "description": "Từ vựng, mẫu câu và ngữ pháp tiếng Anh từ Lớp 1 đến Lớp 12, cho sinh viên và người lớn trình độ C1 đến Native — học cả khi không có mạng.",
    "start_url": "./index.html", "scope": "./", "display": "standalone", "orientation": "any",
    "background_color": "#fffaf2", "theme_color": THEME,
    "icons": [
        {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        {"src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}
with open(os.path.join(ROOT, "manifest.webmanifest"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)

precache = ["./"] + pages + ["manifest.webmanifest"] + icon_files
h = hashlib.sha1()
for p in pages + ["manifest.webmanifest"] + icon_files:
    with open(os.path.join(ROOT, p), "rb") as f:
        h.update(f.read())
SW = f"""// Tự sinh bởi build.py — không sửa tay
const CACHE = 'efk-{h.hexdigest()[:10]}';
const FILES = {json.dumps(precache, ensure_ascii=False)};
self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(caches.match(e.request, {{ignoreSearch: true}}).then(hit => hit || fetch(e.request).then(res => {{
    if (res.ok) {{ const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); }}
    return res;
  }}).catch(() => caches.match('index.html'))));
}});
"""
with open(os.path.join(ROOT, "sw.js"), "w", encoding="utf-8") as f:
    f.write(SW)

print(f"OK: {len(TOPICS)} chủ đề, {total} từ, {len(GRAMMAR)} bài ngữ pháp, TOEIC {len(TOEIC)} bài / {total_q} câu, {len(precache)} file được cache offline")
