"""Tạo web tĩnh (PWA cài được lên Android/iOS) từ dữ liệu.  Chạy:  python3 build.py

Dữ liệu:  _data.py + _grammar.py (Lớp 1-4) · _data_lop05.py … _data_lop12.py (mỗi file có TOPICS và GRAMMAR)
TOEIC:    _toeic_tu_loai.py, _toeic_ngu_phap.py (Part 5) · _toeic_tu_vung.py (từ vựng) · _toeic_nghe_doc.py (Part 2-4, 6-7)
Kết quả:  index.html, ngu-phap.html, toeic.html, on-tap.html, phu-huynh.html, chu-de/*.html, toeic/*.html,
          manifest.webmanifest, sw.js, icons/
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
main{max-width:1150px;margin:0 auto;padding:20px 16px calc(80px + env(safe-area-inset-bottom))}
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
.pill{position:fixed;right:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:20;background:linear-gradient(90deg,#ffd54f var(--p,0%),#fff var(--p,0%));color:#333;border:2px solid #ffb300;border-radius:22px;padding:7px 14px;font-weight:800;font-size:15px;text-decoration:none;box-shadow:0 4px 12px rgba(0,0,0,.18)}
.pill.met{background:#43a047;color:#fff;border-color:#2e7d32}
.toast{position:fixed;left:50%;top:calc(16px + env(safe-area-inset-top));transform:translateX(-50%);background:#2e7d32;color:#fff;padding:12px 20px;border-radius:16px;font-weight:700;z-index:30;box-shadow:0 6px 18px rgba(0,0,0,.25);max-width:90vw;text-align:center}
.remind{background:#fff3e0;border:2px solid #ffb300;border-radius:16px;padding:12px 16px;margin-bottom:14px;line-height:1.55;font-size:16px}
.parent{background:linear-gradient(135deg,#ff8f00,#ff7aa2)}
.review{background:linear-gradient(135deg,#00897b,#43a047)}
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
.mic{position:absolute;top:8px;left:8px;border:none;background:none;font-size:20px;cursor:pointer;padding:4px;display:none}
.sr .mic{display:block}
.sronly{display:none}.sr .sronly{display:inline}
.rec{animation:pulse 1s infinite}
@keyframes pulse{50%{transform:scale(1.25);filter:drop-shadow(0 0 6px #e53935)}}
.rvban{position:fixed;left:12px;right:12px;bottom:calc(58px + env(safe-area-inset-bottom));z-index:19;background:#d84315;color:#fff;border-radius:16px;padding:11px 16px;font-weight:800;text-decoration:none;text-align:center;box-shadow:0 6px 16px rgba(0,0,0,.25);max-width:560px;margin:0 auto}
.set{background:#fff;border-radius:18px;padding:14px 16px;margin-bottom:16px;box-shadow:0 3px 8px rgba(0,0,0,.06);border-top:6px solid var(--c)}
.sethead{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:10px}
.sethead b{font-size:18px;flex:1;min-width:140px}
.set .btn{border:2px solid var(--c)}
.set .q{box-shadow:none;border:1px solid #eee;border-left-width:7px}
.script{background:#f6f8fb;border-radius:12px;padding:10px 14px;margin-bottom:10px;line-height:1.6;font-size:16px}
.script .say{position:static;font-size:16px}
.passage{background:#fbfaf7;border:1px solid #e8e2d4;border-radius:12px;padding:12px 16px;margin-bottom:12px;line-height:1.65;font-size:16px;overflow-wrap:anywhere}
.passage p{margin:0 0 10px}
.passage h4{margin:12px 0 6px;color:var(--c)}
.passage .blank{min-width:44px;text-align:center;font-weight:800;color:var(--c)}
.opts.one{grid-template-columns:1fr}
.hidopt .q:not(.done) .lt{display:none}
@media (max-width:860px){.cols{grid-template-columns:1fr;gap:0}}
@media (max-width:480px){.chips{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}.chips::-webkit-scrollbar{display:none}.chip{flex:0 0 auto}section[id]{scroll-margin-top:70px}.grid{grid-template-columns:repeat(2,1fr);gap:10px}.card{padding:12px 6px 10px;border-radius:16px}.card .ico{font-size:40px}.card .w{font-size:17px}.card .ipa,.card .vn,.card .m{font-size:13px}.say{top:2px;right:2px;font-size:17px}.mic{top:2px;left:2px;font-size:17px}.topics{grid-template-columns:1fr 1fr;gap:10px}.topic{padding:14px;border-radius:18px}.topic .ico{font-size:38px}.topic .t{font-size:16px}.topic .s{font-size:14px}.topic .n{font-size:12px}nav.pn a{padding:9px 12px;font-size:14px}.opts{grid-template-columns:1fr}.theory{grid-template-columns:1fr}.qt{font-size:16px}}
@media print{.pill,.toast,.say,.toolbar,nav.pn,.chips,.scorebar .btn{display:none}.why{display:block!important}.q{break-inside:avoid}header{border-radius:0}.card,.gram{break-inside:avoid}.cols{grid-template-columns:1fr}}
"""

JS = """
function say(t){if(!('speechSynthesis' in window))return alert('Trình duyệt không hỗ trợ đọc.');
speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t.replace(/→/g,'.').replace(/\\//g,' or '));
u.lang='en-GB';u.rate=0.8;const v=speechSynthesis.getVoices().find(v=>v.lang.startsWith('en'));if(v)u.voice=v;speechSynthesis.speak(u);}
function toggleHide(b){document.body.classList.toggle('hide');b.textContent=document.body.classList.contains('hide')?'👁️ Hiện nghĩa':'🙈 Ẩn nghĩa (tự kiểm tra)';}
document.addEventListener('click',ev=>{const c=ev.target.closest('.card');if(c&&!ev.target.closest('.say,.mic'))c.classList.toggle('show');});
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
if(n&&d===n){if(!z.dataset.rec){z.dataset.rec=1;logQuiz(r,n);}if(r>store(z.dataset.key))store(z.dataset.key,r);
t+=' — '+(r>=n*.8?'🎉 Xuất sắc!':r>=n*.5?'👍 Khá tốt, xem lại câu sai nhé.':'💪 Đọc lại lý thuyết rồi làm lại nhé.');}
const best=store(z.dataset.key);if(best)t+=' · 🏆 Cao nhất: '+best+'/'+n;z.querySelector('.score').textContent=t;}
function resetQuiz(b){const z=b.closest('.quiz');delete z.dataset.rec;z.querySelectorAll('.q').forEach(q=>{q.classList.remove('done','qok','qno');
q.querySelector('.why').hidden=true;q.querySelectorAll('.opts button').forEach(o=>o.classList.remove('right','wrong'));});score(z);z.scrollIntoView({behavior:'smooth'});}
function showAll(b){b.closest('.quiz').querySelectorAll('.q:not(.done)').forEach(q=>{q.classList.add('done');q.querySelector('[data-ok]').classList.add('right');q.querySelector('.why').hidden=false;});}
const LOG='efk:log',CFG='efk:cfg',IDLE=180000;
function ld(k,d){try{return JSON.parse(localStorage.getItem(k))||d;}catch(e){return d;}}
function sv(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
function cfg(){return Object.assign({goal:30,name:'',msg:'',pin:''},ld(CFG,{}));}
function dkey(d){d=d||new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function dayRec(log,d){return log[d]||(log[d]={s:0,p:{},q:[]});}
function esc(t){return String(t).replace(/[&<>"']/g,c=>'&#'+c.charCodeAt(0)+';');}
let lastAct=Date.now();
['pointerdown','keydown','scroll','touchstart','wheel'].forEach(t=>addEventListener(t,()=>{lastAct=Date.now();},{passive:true}));
setInterval(()=>{if(document.hidden||Date.now()-lastAct>IDLE||location.pathname.endsWith('phu-huynh.html'))return;const log=ld(LOG,{}),r=dayRec(log,dkey()),pg=document.documentElement.dataset.page,b=r.s;
r.s+=5;r.p[pg]=(r.p[pg]||0)+5;sv(LOG,log);studyUI(r.s,b);},5000);
function studyUI(s,before){const el=document.getElementById('studyPill');if(!el)return;const c=cfg(),g=c.goal*60;
el.textContent=(s>=g?'✅ ':'⏱️ ')+Math.floor(s/60)+'/'+c.goal+' phút';el.style.setProperty('--p',Math.min(100,s/g*100)+'%');el.classList.toggle('met',s>=g);
if(before!==undefined&&before<g&&s>=g)toast('🎉 Giỏi quá! Hôm nay đã học đủ '+c.goal+' phút!');}
function toast(t,bad){const d=document.createElement('div');d.className='toast';d.textContent=t;if(bad)d.style.background='#e65100';document.body.appendChild(d);setTimeout(()=>d.remove(),5000);}
function logQuiz(r,n){const log=ld(LOG,{});dayRec(log,dkey()).q.push([document.documentElement.dataset.page,r,n]);sv(LOG,log);}
addEventListener('DOMContentLoaded',()=>{const a=document.createElement('a');a.id='studyPill';a.className='pill';
a.href=document.documentElement.dataset.root+'phu-huynh.html';a.title='Thời gian học hôm nay — bấm để xem nhật ký học';document.body.appendChild(a);
const s=(ld(LOG,{})[dkey()]||{s:0}).s;studyUI(s);const b=document.getElementById('remind');
if(b){const c=cfg(),left=c.goal-Math.floor(s/60);if(left>0){b.hidden=false;b.innerHTML='📢 '+(c.msg?'<b>Lời nhắc của bố mẹ:</b> '+esc(c.msg)+'<br>':'')
+'Hôm nay '+(c.name?esc(c.name)+' ':'')+'còn <b>'+left+' phút</b> nữa là đủ mục tiêu '+c.goal+' phút. Cố lên! 💪';}}});
addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('.quiz').forEach(score);
document.querySelectorAll('[data-best]').forEach(el=>{const b=store(el.dataset.best);if(b)el.textContent='🏆 '+b+'/'+el.dataset.n;});});
"""

# Luyện nói (nhận giọng nói của trình duyệt), nghe hội thoại nhiều giọng, nhắc giờ ôn từ vựng
JS += r"""
const SRec=window.SpeechRecognition||window.webkitSpeechRecognition,RVC='efk:rvcfg',SRS='efk:srs';
addEventListener('DOMContentLoaded',()=>{if(SRec)document.body.classList.add('sr');});
function norm(s){return String(s).normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/\([^)]*\)/g,' ')
.replace(/[’‘]/g,"'").replace(/[^a-z0-9' ]+/g,' ').replace(/\s+/g,' ').trim();}
function simil(a,b){a=norm(a);b=norm(b);if(!a||!b)return 0;if(a===b||(' '+a+' ').includes(' '+b+' '))return 1;
const m=a.length,n=b.length;let p=Array.from({length:n+1},(_,j)=>j);
for(let i=1;i<=m;i++){const q=[i];for(let j=1;j<=n;j++)q[j]=Math.min(p[j]+1,q[j-1]+1,p[j-1]+(a[i-1]===b[j-1]?0:1));p=q;}
return 1-p[n]/Math.max(m,n);}
let recNow=null;
function hear(target,done){if(!SRec)return done(null,'unsupported');if(recNow){try{recNow.abort();}catch(e){}}
const r=new SRec();recNow=r;r.lang='en-US';r.maxAlternatives=5;r.interimResults=false;let fin=false;
const end=(x,err)=>{if(fin)return;fin=true;recNow=null;done(x,err);};
r.onresult=ev=>{const alts=[...ev.results[0]].map(a=>a.transcript);let best=0,heard=alts[0]||'';
alts.forEach(t=>String(target).split('/').forEach(g=>{const s=simil(t,g);if(s>best){best=s;heard=t;}}));end({score:best,heard});};
r.onerror=ev=>end(null,ev.error);r.onend=()=>end(null,'no-speech');
try{speechSynthesis.cancel();r.start();}catch(e){end(null,'start');}}
function micErr(e){return {unsupported:'Trình duyệt này chưa hỗ trợ nhận giọng nói. Hãy dùng Chrome (Android, máy tính) hoặc Safari (iPhone).',
'not-allowed':'Hãy cho phép ứng dụng dùng micro để luyện nói nhé.','service-not-allowed':'Hãy cho phép ứng dụng dùng micro để luyện nói nhé.',
'no-speech':'Chưa nghe thấy gì — bấm 🎤 rồi nói to, rõ hơn nhé.',network:'Nhận giọng nói cần có mạng Internet.','audio-capture':'Không tìm thấy micro.'}[e]||'Không nghe được, thử lại nhé.';}
const PASS=.75;
function micTry(b){b.classList.add('rec');hear(b.dataset.t,(r,err)=>{b.classList.remove('rec');
if(!r)return toast('🎤 '+micErr(err),1);
if(r.score>=PASS)toast('✅ Chuẩn rồi! Máy nghe được: “'+r.heard+'”');else toast('🤔 Máy nghe thành “'+r.heard+'” — bấm 🔊 nghe mẫu rồi thử lại nhé',1);});}
// Hội thoại: M = giọng nam, W = giọng nữ (đoán theo tên giọng; không đoán được thì đổi cao độ)
let VO=null,playing=null;
if('speechSynthesis' in window)speechSynthesis.addEventListener&&speechSynthesis.addEventListener('voiceschanged',()=>{VO=null;});
function voices(){if(VO)return VO;const vs=speechSynthesis.getVoices().filter(v=>/^en([-_]|$)/i.test(v.lang));if(!vs.length)return null;
const fem=/female|samantha|victoria|karen|moira|tessa|zira|susan|hazel|serena|fiona|allison|ava|kate|libby|sonia|jenny|aria|emma|amy|joanna|salli|kimberly|natasha|catherine|google us english/i,
mal=/\bmale|daniel|alex|fred|david|mark|george|ryan|guy|arthur|oliver|thomas|rishi|aaron|james|eric|brian|matthew|justin|google uk english male/i;
const us=vs.filter(v=>/us/i.test(v.lang)).concat(vs),W=us.find(v=>fem.test(v.name))||us[0],
M=us.find(v=>v!==W&&mal.test(v.name.replace(/female/ig,'')))||us.find(v=>v!==W)||W;return VO={W,M};}
function playLines(b){if(!('speechSynthesis' in window))return alert('Trình duyệt không hỗ trợ đọc.');
const was=playing;speechSynthesis.cancel();if(was===b)return;
const L=JSON.parse(b.dataset.s),vo=voices(),label=b.dataset.l||(b.dataset.l=b.textContent);playing=b;b.textContent='⏹️ Dừng';
const fin=()=>{if(playing===b)playing=null;b.textContent=label;};
L.forEach(([who,t],i)=>{const u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=.9;const v=vo&&(who==='W'?vo.W:vo.M);
if(v){u.voice=v;u.lang=v.lang;}u.pitch=who==='W'?1.15:.85;if(i===L.length-1){u.onend=fin;u.onerror=fin;}speechSynthesis.speak(u);});}
// Nhắc giờ ôn từ vựng (cài đặt ở on-tap.html)
function rvCfg(){return Object.assign({n:2,t:['07:00','19:30'],k:10,mode:'level',lv:'',tp:[],ty:['m','r','l']},ld(RVC,{}));}
function hm2m(s){const [h,m]=String(s).split(':').map(Number);return (h||0)*60+(m||0);}
function nowM(){const d=new Date();return d.getHours()*60+d.getMinutes();}
// Mỗi lượt ôn trọn vẹn được tính cho buổi chưa xong sớm nhất; buổi sau chỉ tính từ (giờ của buổi đó − 60 phút)
function rvSlots(){const c=rvCfg(),ts=c.t.slice(0,c.n).map(hm2m),done=ts.map(()=>false);
((ld(LOG,{})[dkey()]||{}).rv||[]).filter(x=>x[3]).forEach(x=>{const i=done.findIndex((d,j)=>!d&&(j===0||x[0]>=ts[j]-60));if(i>=0)done[i]=true;});
const now=nowM();return ts.map((t,i)=>({t:c.t[i],done:done[i],due:!done[i]&&now>=t}));}
function rvNotify(msg){try{if(!('Notification' in window)||Notification.permission!=='granted'||!navigator.serviceWorker)return;
const root=document.documentElement.dataset.root;navigator.serviceWorker.ready.then(r=>r.showNotification('🔁 English for Kids',
{body:msg,icon:root+'icons/icon-192.png',badge:root+'icons/icon-192.png',tag:'efk-rv',data:{url:root+'on-tap.html'}}));}catch(e){}}
function rvCheck(){if(!ld(RVC,null))return;const due=rvSlots().filter(s=>s.due),onRv=location.pathname.endsWith('on-tap.html');
let b=document.getElementById('rvBan');
if(due.length&&!onRv){if(!b){b=document.createElement('a');b.id='rvBan';b.className='rvban';b.href=document.documentElement.dataset.root+'on-tap.html';document.body.appendChild(b);}
b.textContent='🔔 Đến giờ ôn từ vựng ('+due.map(s=>s.t).join(' · ')+') — bấm để ôn ngay!';}else if(b)b.remove();
const today=dkey(),old=ld('efk:rvn',{}),sent={};Object.keys(old).forEach(k=>{if(k.startsWith(today))sent[k]=1;});
due.forEach(s=>{const id=today+' '+s.t;if(sent[id])return;sent[id]=1;const msg='Đến giờ ôn từ vựng buổi '+s.t+' rồi! ⏰';toast('🔔 '+msg);rvNotify(msg);});
sv('efk:rvn',sent);}
addEventListener('DOMContentLoaded',()=>{rvCheck();setInterval(rvCheck,30000);});
document.addEventListener('visibilitychange',()=>{if(!document.hidden)rvCheck();});
"""

def page(title, color, body, root=""):
    return f"""<!DOCTYPE html>
<html lang="vi" data-root="{root}" data-page="{e(title)}"><head><meta charset="utf-8">
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

def mic_btn(text):
    return f'<button class="mic" title="Luyện nói: bấm rồi đọc to từ này" onclick="micTry(this)" data-t="{e(text)}">🎤</button>'

def cards_html(ws):
    return "".join(
        f'<div class="card">{mic_btn(w)}{say_btn(w)}'
        f'<div class="ico">{ic}</div><div class="w">{e(w)}</div><div class="ipa">{e(ipa)}</div>'
        + (f'<div class="vn">{e(vn)}</div>' if vn else "")
        + f'<div class="m">{e(m)}</div></div>'
        for ic, w, ipa, vn, m in ws)

MIC_LEGEND = '<span class="sronly"> &nbsp;|&nbsp; 🎤 Bấm micro rồi đọc to để luyện phát âm</span>'

# ───────────────────────── Trang chủ đề ─────────────────────────
total = 0
pages = ["index.html", "ngu-phap.html"]
for i, (slug, ico, en, vi, grade, color, words, pats) in enumerate(TOPICS):
    ws, ps = parse(words, 5), parse(pats, 2)
    total += len(ws)
    cards = cards_html(ws)
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
<a class="btn" href="../on-tap.html#t={slug}">🔁 Ôn từ chủ đề này</a>
<button class="btn" onclick="toggleHide(this)">🙈 Ẩn nghĩa (tự kiểm tra)</button>
<button class="btn" onclick="window.print()">🖨️ In</button></div></header>
<main><div class="legend">🔊 Bấm loa để nghe{MIC_LEGEND} &nbsp;|&nbsp; <b>/IPA/</b> = phiên âm quốc tế{' &nbsp;|&nbsp; 🗣️ = phiên âm tiếng Việt (gần đúng)' if has_vn else (' &nbsp;|&nbsp; (n) danh từ · (v) động từ · (adj) tính từ' + (' · (idiom) thành ngữ · (phr v) cụm động từ · (expr) cụm từ cố định · (collocation) kết hợp từ · (slang) tiếng lóng' if grade in ADULT else ''))} &nbsp;|&nbsp; ô xám = nghĩa</div>
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
<a class="btn" href="on-tap.html">🔁 Ôn từ vựng</a>
<a class="btn" href="ngu-phap.html">📐 Tổng hợp ngữ pháp</a>
<a class="btn" href="toeic.html">🎯 Luyện thi TOEIC</a>
<a class="btn" href="phu-huynh.html">👨‍👩‍👧 Nhật ký học</a></div>
<div class="ioshint">📲 <b>Cài lên iPhone/iPad:</b> mở bằng Safari → bấm nút <b>Chia sẻ</b> (⬆️) → chọn <b>“Thêm vào MH chính”</b>.</div>
</header>
<main><div id="remind" class="remind" hidden></div>{chips()}
<a class="special review" href="on-tap.html" style="margin-bottom:14px"><div class="ico">🔁</div><div><b>Ôn từ vựng mỗi ngày</b>Ôn theo lớp hoặc chủ đề, sáng và tối theo giờ bạn chọn. Từ hay sai sẽ xuất hiện nhiều hơn, từ đã thuộc thì thưa dần — có nghe, chọn nghĩa và luyện nói 🎤.</div></a>
<a class="special" href="ngu-phap.html"><div class="ico">📐</div><div><b>Tổng hợp ngữ pháp</b>Công thức, cách dùng và ví dụ cho từng lớp — học xong từ vựng thì ôn ngữ pháp nhé!</div></a>
<a class="special toeic" href="toeic.html" style="margin-top:14px"><div class="ico">🎯</div><div><b>Luyện thi TOEIC</b>Danh từ, động từ, tính từ, trạng từ, giới từ… lý thuyết + bài tập trắc nghiệm kiểu Part 5 có chấm điểm và giải thích.</div></a>
<a class="special parent" href="phu-huynh.html" style="margin-top:14px"><div class="ico">👨‍👩‍👧</div><div><b>Nhật ký học &amp; Góc phụ huynh</b>Mỗi ngày học ít nhất 30 phút ⏱️ — bố mẹ xem lịch sử học, đặt lời nhắc và nhận báo cáo qua Zalo/Messenger.</div></a>
{sections}
<h2>💡 Cách học hiệu quả</h2><div class="tips">
1️⃣ Mỗi ngày học <b>5–7 từ mới</b>: nhìn hình 👀 → bấm 🔊 nghe → đọc to 3 lần 🗣️.<br>
2️⃣ Đọc theo <b>phiên âm IPA</b>; phiên âm tiếng Việt (Tiểu học) chỉ để tham khảo cách đọc gần đúng.<br>
3️⃣ Bấm <b>🙈 Ẩn nghĩa</b> để tự kiểm tra: nhìn từ đoán nghĩa, chạm vào thẻ để xem đáp án.<br>
4️⃣ Học <b>mẫu câu</b> theo cặp hỏi ❓ – đáp 💬, rồi đọc phần <b>📐 ngữ pháp</b> bên cạnh để hiểu vì sao câu được viết như vậy.<br>
5️⃣ Sinh viên &amp; người lớn: bắt đầu từ <b>C1/C2</b> để luyện tiếng Anh học thuật, công việc; học <b>Fluent/Native</b> để nói tự nhiên như người bản xứ.<br>
6️⃣ Mỗi ngày vào <b>🔁 Ôn từ vựng</b> 1–2 lần: app tự chọn từ cần ôn, từ trả lời sai sẽ được hỏi lại nhiều hơn.<br>
7️⃣ Cài ứng dụng về điện thoại 📲 để học cả khi <b>không có mạng</b>. Cuối tuần ôn lại chủ đề cũ 🔁 — <i>Practice makes perfect!</i> 🏆
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
const z=document.querySelector('.quiz');delete z.dataset.rec;score(z);t0=Date.now();scrollTo({top:0,behavior:'smooth'});}
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

# Từ vựng TOEIC theo chủ đề
import _toeic_tu_vung, _toeic_nghe_doc
TOEIC_VOCAB = _toeic_tu_vung.TOPICS
toeic_words = 0
for slug, ico, en, vi, color, words in TOEIC_VOCAB:
    ws = parse(words, 5)
    assert len(ws) == len(words.strip().splitlines()), f"{slug}: có dòng từ vựng sai định dạng"
    toeic_words += len(ws)
    body = f"""<header><div class="big">{ico}</div><h1>{e(en)}</h1><p>Từ vựng TOEIC: {e(vi)}</p>
<span class="badge">🎯 {len(ws)} từ hay gặp trong đề TOEIC</span>
<div class="toolbar"><a class="btn" href="../toeic.html#tu-vung">🎯 Mục lục TOEIC</a><a class="btn" href="../on-tap.html#t={slug}">🔁 Ôn từ chủ đề này</a>
<button class="btn" onclick="toggleHide(this)">🙈 Ẩn nghĩa (tự kiểm tra)</button><button class="btn" onclick="window.print()">🖨️ In</button></div></header>
<main><div class="legend">🔊 Bấm loa để nghe{MIC_LEGEND} &nbsp;|&nbsp; <b>/IPA/</b> = phiên âm quốc tế &nbsp;|&nbsp; (n) danh từ · (v) động từ · (adj) tính từ · (adv) trạng từ · (phr v) cụm động từ · (expr) cụm từ cố định</div>
<h2>📖 Từ vựng (Vocabulary)</h2><div class="grid">{cards_html(ws)}</div>
<nav class="pn"><a href="../toeic.html#tu-vung">⬅️ Mục lục TOEIC</a><a href="../on-tap.html#t={slug}">🔁 Ôn ngay ➡️</a></nav></main>"""
    with open(os.path.join(TOEIC_OUT, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(page(f"{vi} – Từ vựng TOEIC", color, body, root="../"))
    pages.append(f"toeic/{slug}.html")

# Nghe hiểu (Part 2–4) và Đọc hiểu (Part 6–7)
def shuffled(key, right, wrong):
    opts = [right] + wrong
    assert len(set(opts)) == len(opts), f"Đáp án trùng nhau: {opts}"
    random.Random(hashlib.md5(key.encode()).hexdigest()).shuffle(opts)
    return opts, opts.index(right)

def opts_html(opts, a, hide=False):
    one = " one" if max(len(o) for o in opts) > 38 else ""
    return (f'<div class="opts{one}">' + "".join(
        f'<button onclick="pick(this)"{" data-ok=1" if k == a else ""}>({"ABCD"[k]})'
        + (f' <span class="lt">{e(o)}</span>' if hide else f' {e(o)}') + '</button>' for k, o in enumerate(opts)) + '</div>')

def play_btn(lines, label):
    return f'<button class="btn" onclick="playLines(this)" data-s="{e(json.dumps(lines, ensure_ascii=False))}">{label}</button>'

def quiz_rows(block, cols):
    rows = [[x.strip() for x in l.split("|")] for l in block.strip().splitlines() if l.strip()]
    for r in rows:
        assert len(r) == cols, f"Sai định dạng ({cols} cột): {'|'.join(r)}"
    return rows

def script_lines(script):
    out = []
    for l in script.strip().splitlines():
        who, t = l.split(":", 1)
        assert who.strip() in ("M", "W"), f"Người nói phải là M hoặc W: {l}"
        out.append([who.strip(), t.strip()])
    return out

def passage_html(text, offset):
    out, para = [], []
    def flush():
        if para:
            out.append("<p>" + "<br>".join(para) + "</p>")
            para.clear()
    for l in text.strip().splitlines():
        l = l.strip()
        if not l:
            flush()
        elif l.startswith("### "):
            flush()
            out.append(f"<h4>{e(l[4:])}</h4>")
        else:
            para.append(re.sub(r"\[(\d)\]", lambda m: f'<span class="blank">({int(m.group(1)) + offset})</span>', e(l)))
    flush()
    return "".join(out)

def part_page(P, kind):
    n, html_sets = 0, []
    if P["part"] == 2:
        qs = []
        for k, (q, right, w1, w2, why) in enumerate(quiz_rows(P["items"], 5)):
            n += 1
            opts, a = shuffled(q, right, [w1, w2])
            asker, ans = ("W", "M") if k % 2 == 0 else ("M", "W")
            lines = [[asker, q]] + [[ans, f"{'ABC'[j]}. {o}"] for j, o in enumerate(opts)]
            script = f"🗣️ <b>{e(q)}</b><br>" + "<br>".join(f"({'ABC'[j]}) {e(o)}" for j, o in enumerate(opts))
            qs.append(f'<div class="q"><div class="qt"><b>{n}.</b> {play_btn(lines, "🔊 Nghe câu " + str(n))}</div>{opts_html(opts, a, hide=True)}'
                      f'<div class="why" hidden>{script} {say_btn(q)}<br>✅ <b>({"ABC"[a]}) {e(right)}</b> — {e(why)}</div></div>')
        html_sets.append('<div class="hidopt">' + "".join(qs) + "</div>")
    else:
        for si, S in enumerate(P["sets"]):
            head, qs = "", []
            if kind == "listen":
                lines = script_lines(S["script"])
                name = "Hội thoại" if P["part"] == 3 else "Bài nói"
                tr = "".join(f'<div><b>{"👨" if w == "M" else "👩"} {w}:</b> {e(t)} {say_btn(t)}</div>' for w, t in lines)
                head = (f'<div class="sethead"><b>{name} {si + 1}</b>{play_btn(lines, "🔊 Nghe")}'
                        f'<button class="btn" onclick="const s=this.closest(\'.set\').querySelector(\'.script\');s.hidden=!s.hidden">📜 Lời thoại</button></div>'
                        f'<div class="script" hidden>{tr}</div>')
                rows = quiz_rows(S["quiz"], 6)
            else:
                head = f'<div class="sethead"><b>📄 Văn bản {si + 1}: {e(S["title"])}</b></div><div class="passage">{passage_html(S["text"], n)}</div>'
                rows = quiz_rows(S["quiz"], 5 if P["part"] == 6 else 6)
                if P["part"] == 6:
                    blanks = re.findall(r"\[(\d)\]", S["text"])
                    assert blanks == [str(i + 1) for i in range(len(rows))], f"{P['slug']} văn bản {si+1}: số chỗ trống và số câu hỏi không khớp"
                    rows = [[f"Chọn đáp án cho chỗ trống ({n + i + 1})."] + r for i, r in enumerate(rows)]
            for q, right, *wrong, why in rows:
                n += 1
                opts, a = shuffled(S.get("title", "") + q + right, right, wrong)
                qs.append(f'<div class="q"><div class="qt"><b>{n}.</b> {e(q)}</div>{opts_html(opts, a)}'
                          f'<div class="why" hidden>✅ <b>({"ABCD"[a]}) {e(right)}</b> — {e(why)}</div></div>')
            html_sets.append(f'<div class="set">{head}{"".join(qs)}</div>')
    return n, "".join(html_sets)

listen_read = [("listen", P) for P in _toeic_nghe_doc.LISTEN] + [("read", P) for P in _toeic_nghe_doc.READ]
for kind, P in listen_read:
    n, sets_html = part_page(P, kind)
    P["n"] = n
    total_q += n
    note = ("🎧 Bấm <b>🔊 Nghe</b> để nghe (giọng đọc của trình duyệt, nghe được khi không có mạng nếu máy có sẵn giọng tiếng Anh). "
            + ("Part 2 chỉ nghe, không in sẵn đáp án — đáp án và lời thoại hiện ra sau khi chọn." if P["part"] == 2
               else "Đọc câu hỏi trước rồi mới nghe; bấm 📜 để xem lời thoại sau khi làm.")) if kind == "listen" else \
           "📖 Đọc văn bản rồi chọn đáp án đúng nhất. Làm xong, phần giải thích sẽ hiện ra dưới mỗi câu."
    body = f"""<header><div class="big">{P["ico"]}</div><h1>{e(P["en"])}</h1><p>Luyện thi TOEIC · {e(P["vi"])}</p>
<span class="badge">🎯 {n} câu luyện tập · có giải thích tiếng Việt</span>
<div class="toolbar"><a class="btn" href="../toeic.html">🎯 Mục lục TOEIC</a><a class="btn" href="../index.html">🏠 Trang chủ</a>
<a class="btn" href="#bai-tap">✍️ Làm bài tập</a></div></header>
<main><div class="theory">{grammar_html(None, text=P["tips"], icon="📌 ")}</div>
<section id="bai-tap"><h2>✍️ Bài tập</h2><div class="legend">{note}</div><br>
<div class="quiz" data-key="{P["slug"]}">{scorebar()}{sets_html}</div></section>
<nav class="pn"><a href="../toeic.html">⬅️ Mục lục TOEIC</a><a href="de-tong-hop.html">📝 Đề Part 5 tổng hợp ➡️</a></nav></main>"""
    with open(os.path.join(TOEIC_OUT, P["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(page(f"{P['en']} – Luyện thi TOEIC", P["color"], body, root="../"))
    pages.append(f"toeic/{P['slug']}.html")

for f in os.listdir(TOEIC_OUT):
    if f.endswith(".html") and f"toeic/{f}" not in pages:
        os.remove(os.path.join(TOEIC_OUT, f))
        print("🗑️  Đã xóa trang cũ:", f)

# Mục lục TOEIC
def tile(n, slug, ico, vi, en, color, label, best=None):
    b = f'<span class="n best" data-best="{slug}" data-n="{best}"></span>' if best else ""
    return (f'<a class="topic" style="background:{color}" href="toeic/{slug}.html"><div class="ico">{ico}</div>'
            f'<div class="t">{n}. {e(vi)}</div><div class="s">{e(en)}</div><div class="n">{label}</div>{b}</a>')

tsec, n = "", 0
tiles = ""
for k, (slug, ico, en, vi, color, words) in enumerate(TOEIC_VOCAB):
    tiles += tile(k + 1, slug, ico, vi, en, color, f"📖 {len(parse(words, 5))} từ")
tsec += f'<section id="tu-vung"><h2>{_toeic_tu_vung.GROUP} <small>{len(TOEIC_VOCAB)} chủ đề · {toeic_words} từ</small></h2><div class="topics">{tiles}</div></section>'
for gname, ls in TOEIC_GROUPS:
    tiles = ""
    for L in ls:
        n += 1
        k = len(L["quiz"].strip().splitlines())
        tiles += tile(n, L["slug"], L["ico"], L["vi"], L["en"], L["color"], f"✍️ {k} câu · Part 5", k)
    tsec += f'<section><h2>{gname} <small>{len(ls)} bài</small></h2><div class="topics">{tiles}</div></section>'
for gname, kind in ((_toeic_nghe_doc.LISTEN_GROUP, "listen"), (_toeic_nghe_doc.READ_GROUP, "read")):
    tiles = "".join(tile(f"Part {P['part']}", P["slug"], P["ico"], P["vi"], P["en"], P["color"], f"✍️ {P['n']} câu", P["n"])
                    for kk, P in listen_read if kk == kind)
    tsec += f'<section id="{kind}"><h2>{gname}</h2><div class="topics">{tiles}</div></section>'
tpage = f"""<header><div class="big">🎯</div><h1>Luyện thi TOEIC</h1>
<p>Từ vựng · Từ loại · Ngữ pháp · Nghe (Part 2–4) · Đọc (Part 5–7) — có chấm điểm và giải thích</p>
<span class="badge">📘 {toeic_words} từ vựng · {len(TOEIC) + len(listen_read)} bài · {total_q} câu luyện tập</span>
<div class="toolbar"><a class="btn" href="index.html">🏠 Trang chủ</a><a class="btn" href="on-tap.html#lv=17">🔁 Ôn từ vựng TOEIC</a><a class="btn" href="toeic/de-tong-hop.html">📝 Làm đề tổng hợp</a></div></header>
<main><a class="special toeic" href="toeic/de-tong-hop.html"><div class="ico">📝</div><div><b>Đề tổng hợp {TEST_N} câu</b>Trộn ngẫu nhiên từ tất cả các bài, có bấm giờ — làm sau khi đã học xong các bài bên dưới.</div></a>
{tsec}
<p class="legend">ℹ️ Part 1 (mô tả tranh) cần ảnh chụp thật nên chưa có ở đây. Các bài nghe dùng giọng đọc của trình duyệt: giọng có thể khác giọng trong đề thi thật, nhưng đủ để luyện nghe ý chính và chi tiết.</p>
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

# ───────────────────────── Nhật ký học & Góc phụ huynh ─────────────────────────
# Dữ liệu nằm trong localStorage của máy học (efk:log, efk:cfg). Báo cáo gửi phụ huynh là một link
# chứa dữ liệu ở phần #r=… nên không cần máy chủ.
PARENT_CSS = """
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}
.stat{background:#fff;border-radius:18px;padding:14px 16px;box-shadow:0 3px 8px rgba(0,0,0,.06);text-align:center}
.stat b{display:block;font-size:30px;color:var(--c)}
.stat span{color:#666;font-size:15px}
.bar{height:10px;background:#eee;border-radius:6px;overflow:hidden;margin-top:8px}
.bar i{display:block;height:100%;background:var(--c)}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;background:#fff;border-radius:18px;padding:12px;box-shadow:0 3px 8px rgba(0,0,0,.06)}
.cal .h{text-align:center;font-weight:700;color:#888;font-size:13px}
.cal button{border:none;border-radius:10px;padding:6px 2px;font:inherit;font-size:12px;cursor:pointer;background:#eee;color:#555;min-height:46px;line-height:1.25}
.cal button b{display:block;font-size:15px}
.cal button.ok{background:#43a047;color:#fff}.cal button.part{background:#ffca28}.cal button.no{background:#ffcdd2;color:#b71c1c}
.cal button.today{outline:3px solid var(--c);outline-offset:1px}
.cal span.f{visibility:hidden}
.legend2{display:flex;gap:14px;flex-wrap:wrap;font-size:14px;color:#555;margin-top:8px}
.legend2 i{display:inline-block;width:14px;height:14px;border-radius:4px;vertical-align:-2px;margin-right:4px}
.day{background:#fff;border-radius:16px;padding:12px 16px;margin-bottom:10px;box-shadow:0 3px 8px rgba(0,0,0,.05);border-left:7px solid #ddd}
.day.ok{border-left-color:#43a047}.day.part{border-left-color:#ffca28}.day.no{border-left-color:#e53935}
.day .top{display:flex;justify-content:space-between;gap:8px;font-weight:800;flex-wrap:wrap}
.day ul{margin:6px 0 0;padding-left:20px;color:#555;font-size:15px;line-height:1.55}
.panel{background:#fff;border-radius:18px;padding:16px 18px;box-shadow:0 3px 8px rgba(0,0,0,.06);line-height:1.6}
.panel label{display:block;font-weight:700;margin-top:10px}
.panel input,.panel select,.panel textarea{width:100%;font:inherit;font-size:16px;padding:9px 12px;border:2px solid #ddd;border-radius:12px;margin-top:4px;background:#fff}
.panel .btn{border:2px solid var(--c);margin-top:12px;margin-right:6px}
.panel .btn.solid{background:var(--c);color:#fff}
.note{color:#777;font-size:14px}
.rbanner{background:#e3f2fd;border:2px solid #1e88e5;border-radius:16px;padding:12px 16px;margin-bottom:14px}
"""

PARENT_JS = r"""
const DOW=['CN','T2','T3','T4','T5','T6','T7'];
let DATA,CF,REP=null,TODAY;
function hsh(s){let h=7;for(const c of String(s))h=(h*31+c.charCodeAt(0))>>>0;return 'h'+h;}
function parseKey(k){const [y,m,d]=k.split('-').map(Number);return new Date(y,m-1,d);}
function lastDays(n){const out=[],t=parseKey(TODAY);for(let i=n-1;i>=0;i--){const d=new Date(t);d.setDate(t.getDate()-i);out.push(dkey(d));}return out;}
function mins(k){return Math.floor(((DATA[k]||{}).s||0)/60);}
function cls(k){const m=mins(k);return m>=CF.goal?'ok':m>0?'part':'no';}
function lbl(k){const d=parseKey(k);return DOW[d.getDay()]+' '+d.getDate()+'/'+(d.getMonth()+1);}
function streak(){let n=0;const days=lastDays(400).reverse();for(let i=0;i<days.length;i++){if(mins(days[i])>=CF.goal)n++;else if(i>0)break;}return n;}
function topPages(k,n){const p=(DATA[k]||{}).p||{};return Object.entries(p).sort((a,b)=>b[1]-a[1]).slice(0,n);}
const b64e=u=>{let s='';u.forEach(c=>s+=String.fromCharCode(c));return btoa(s).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');};
const b64d=t=>Uint8Array.from(atob(t.replace(/-/g,'+').replace(/_/g,'/')),c=>c.charCodeAt(0));
async function pipe(u,S){return new Uint8Array(await new Response(new Blob([u]).stream().pipeThrough(new S('deflate-raw'))).arrayBuffer());}
async function pack(o){const u=new TextEncoder().encode(JSON.stringify(o));
if(window.CompressionStream){try{return 'z'+b64e(await pipe(u,CompressionStream));}catch(e){}}return 'j'+b64e(u);}
async function unpack(t){let u=b64d(t.slice(1));if(t[0]==='z')u=await pipe(u,DecompressionStream);return JSON.parse(new TextDecoder().decode(u));}
async function load(){REP=null;const m=location.hash.match(/^#r=(.+)$/);
if(m){try{const o=await unpack(m[1]);REP=o;DATA=o.d;CF={goal:o.g,name:o.n};TODAY=dkey(new Date(o.t));return;}
catch(e){alert('Link báo cáo bị lỗi hoặc bị cắt mất. Hãy nhờ con gửi lại.');}}
DATA=ld(LOG,{});CF=cfg();TODAY=dkey();}
async function render(){await load();const who=CF.name||'con';const g=CF.goal;
document.getElementById('who').textContent=CF.name?'của '+CF.name:'';
document.getElementById('rbanner').hidden=!REP;
if(REP)document.getElementById('rbanner').innerHTML='📩 Đây là <b>báo cáo '+esc(who)+' gửi lúc '+new Date(REP.t).toLocaleString('vi-VN')+'</b>. Số liệu tính đến lúc gửi. <a href="#" onclick="location.hash=\'\';return false">Xem nhật ký trên máy này</a>';
['sharebox','settings'].forEach(id=>document.getElementById(id).hidden=!!REP);
const t=mins(TODAY),d7=lastDays(7),d30=lastDays(30);
const met7=d7.filter(k=>mins(k)>=g).length,sum7=d7.reduce((a,k)=>a+mins(k),0),miss=d7.filter(k=>k!==TODAY&&mins(k)===0).length;
document.getElementById('stats').innerHTML=
'<div class="stat"><b>'+t+'/'+g+'′</b><span>'+(REP?'Ngày gửi báo cáo':'Hôm nay')+(t>=g?' ✅':' ⏳')+'</span><div class="bar"><i style="width:'+Math.min(100,t/g*100)+'%"></i></div></div>'
+'<div class="stat"><b>🔥 '+streak()+'</b><span>ngày liên tiếp đạt mục tiêu</span></div>'
+'<div class="stat"><b>'+met7+'/7</b><span>ngày đạt trong 7 ngày qua</span></div>'
+'<div class="stat"><b>'+sum7+'′</b><span>tổng thời gian 7 ngày · TB '+Math.round(sum7/7)+'′/ngày</span></div>';
const w=document.getElementById('warn');
w.hidden=!(t<g||miss);w.innerHTML='⚠️ '+(t<g?(REP?'Ngày gửi':'Hôm nay')+' '+esc(who)+' mới học <b>'+t+'/'+g+' phút</b>. ':'')+(miss?'Có <b>'+miss+' ngày</b> trong tuần qua không học. ':'')+(REP?'':'Bố mẹ có thể đặt lời nhắc ở phần ⚙️ Cài đặt bên dưới.');
// Lịch 5 tuần, bắt đầu từ thứ Hai
const start=parseKey(d30[0]);start.setDate(start.getDate()-((start.getDay()+6)%7));
let cal=['T2','T3','T4','T5','T6','T7','CN'].map(x=>'<div class="h">'+x+'</div>').join(''),d=new Date(start);
while(dkey(d)<=TODAY){const k=dkey(d),m=mins(k);
cal+='<button class="'+cls(k)+(k===TODAY?' today':'')+'" onclick="showDay(\''+k+'\')"><b>'+d.getDate()+'</b>'+(m?m+'′':'–')+'</button>';d.setDate(d.getDate()+1);}
document.getElementById('cal').innerHTML=cal;
document.getElementById('days').innerHTML=lastDays(14).reverse().map(dayHTML).join('');
if(!REP)settingsUI();}
function dayHTML(k){const r=DATA[k]||{s:0,p:{},q:[]},m=mins(k),c=cls(k);
const pages=topPages(k,6).map(([p,s])=>esc(p.split(' – ')[0])+' <span class="note">('+Math.max(1,Math.round(s/60))+'′)</span>').join(' · ');
const qz=(r.q||[]).map(q=>'📝 '+esc(q[0].split(' – ')[0])+': <b>'+q[1]+'/'+q[2]+'</b>').join(' · ');
const hm=m=>String(m/60|0).padStart(2,'0')+':'+String(m%60).padStart(2,'0');
const rv=(r.rv||[]).map(x=>hm(x[0])+' '+esc(x[4]||'')+': <b>'+x[1]+'/'+x[2]+'</b>'+(x[3]?'':' <span class="note">(dừng giữa chừng)</span>')).join(' · ');
return '<div class="day '+c+'" id="d-'+k+'"><div class="top"><span>'+lbl(k)+(k===TODAY?' (hôm nay)':'')+'</span><span>'+(c==='ok'?'✅ ':c==='part'?'⏳ ':'❌ ')+(m?m+' phút':'Không học')+'</span></div>'
+(pages||qz||rv?'<ul>'+(pages?'<li>📖 '+pages+'</li>':'')+(qz?'<li>'+qz+'</li>':'')+(rv?'<li>🔁 Ôn từ '+rv+'</li>':'')+'</ul>':'')+'</div>';}
function showDay(k){const el=document.getElementById('d-'+k);if(el){el.scrollIntoView({behavior:'smooth',block:'center'});return;}
const box=document.getElementById('oneday');box.innerHTML=dayHTML(k);box.hidden=false;box.scrollIntoView({behavior:'smooth',block:'center'});}
// Báo cáo gửi phụ huynh
async function report(){const days={};lastDays(30).forEach(k=>{const r=DATA[k];if(!r||!r.s)return;
days[k]={s:r.s,p:Object.fromEntries(topPages(k,4).map(([p,s])=>[p.split(' – ')[0],s])),q:(r.q||[]).slice(-8).map(q=>[q[0].split(' – ')[0],q[1],q[2]]),rv:(r.rv||[]).slice(-6)};});
const o={n:CF.name,g:CF.goal,t:Date.now(),d:days};
const url=location.href.split('#')[0]+'#r='+(await pack(o)),g=CF.goal,d7=lastDays(7);
const text='📊 Nhật ký học tiếng Anh'+(CF.name?' của '+CF.name:'')+' (7 ngày qua)\n'
+'Mục tiêu: '+g+' phút/ngày · Đạt '+d7.filter(k=>mins(k)>=g).length+'/7 ngày · 🔥 '+streak()+' ngày liên tiếp\n'
+d7.slice().reverse().map(k=>(mins(k)>=g?'✅ ':mins(k)?'⏳ ':'❌ ')+lbl(k)+': '+mins(k)+' phút'+(((DATA[k]||{}).rv||[]).filter(x=>x[3]).length?' · 🔁 ôn từ '+DATA[k].rv.filter(x=>x[3]).length+' lượt':'')).join('\n');
return {url,text};}
async function shareReport(){const r=await report();const box=document.getElementById('shareout');
if(navigator.share){try{await navigator.share({title:'Nhật ký học tiếng Anh',text:r.text+'\n\nXem chi tiết:',url:r.url});return;}catch(e){if(e.name==='AbortError')return;}}
box.value=r.text+'\n\nXem chi tiết: '+r.url;box.hidden=false;box.select();
try{await navigator.clipboard.writeText(box.value);toast('📋 Đã sao chép báo cáo — dán vào Zalo/Messenger để gửi bố mẹ');}catch(e){}}
// Cài đặt có mã PIN
let unlocked=false;
function settingsUI(){const c=cfg(),box=document.getElementById('settings-body');
if(c.pin&&!unlocked){box.innerHTML='<p>🔒 Phần này dành cho bố mẹ. Nhập mã PIN để thay đổi mục tiêu, lời nhắc hoặc xóa lịch sử.</p>'
+'<label>Mã PIN<input id="pin" type="password" inputmode="numeric" maxlength="8" autocomplete="off"></label><button class="btn solid" onclick="unlock()">🔓 Mở khóa</button>';return;}
box.innerHTML=(c.pin?'':'<p class="note">👋 Lần đầu sử dụng: bố mẹ hãy đặt <b>mã PIN</b> để con không tự đổi mục tiêu hay xóa lịch sử.</p>')
+'<label>Tên của con<input id="s-name" maxlength="30" value="'+esc(c.name)+'" placeholder="Ví dụ: Bin"></label>'
+'<label>Mục tiêu mỗi ngày<select id="s-goal">'+[15,20,30,45,60,90].map(m=>'<option value="'+m+'"'+(m===c.goal?' selected':'')+'>'+m+' phút</option>').join('')+'</select></label>'
+'<label>Lời nhắc hiện trên trang chủ của con<textarea id="s-msg" rows="2" maxlength="200" placeholder="Ví dụ: Con nhớ học đủ 30 phút trước khi xem TV nhé! ❤️">'+esc(c.msg)+'</textarea></label>'
+'<label>'+(c.pin?'Đổi mã PIN (để trống nếu giữ nguyên)':'Đặt mã PIN (4–8 số)')+'<input id="s-pin" type="password" inputmode="numeric" maxlength="8" autocomplete="new-password"></label>'
+'<button class="btn solid" onclick="saveSettings()">💾 Lưu cài đặt</button>'+(c.pin?'<button class="btn" onclick="lock()">🔒 Khóa lại</button>':'')
+'<button class="btn" onclick="clearLog()">🗑️ Xóa lịch sử học</button>';}
function unlock(){if(hsh(document.getElementById('pin').value)===cfg().pin){unlocked=true;settingsUI();}else toast('❌ Mã PIN không đúng');}
function lock(){unlocked=false;settingsUI();}
function saveSettings(){const c=cfg(),pin=document.getElementById('s-pin').value.trim();
if(pin&&!/^\d{4,8}$/.test(pin))return toast('Mã PIN phải gồm 4–8 chữ số');
if(!c.pin&&!pin)return toast('Bố mẹ hãy đặt mã PIN trước khi lưu');
c.name=document.getElementById('s-name').value.trim();c.goal=+document.getElementById('s-goal').value;c.msg=document.getElementById('s-msg').value.trim();
if(pin)c.pin=hsh(pin);sv(CFG,c);unlocked=false;toast('✅ Đã lưu cài đặt');render();studyUI((ld(LOG,{})[dkey()]||{s:0}).s);}
function clearLog(){if(confirm('Xóa toàn bộ lịch sử học trên máy này? Không thể hoàn tác.')){sv(LOG,{});toast('Đã xóa lịch sử');render();}}
addEventListener('DOMContentLoaded',render);addEventListener('hashchange',render);
"""

ppage = f"""<header><div class="big">👨‍👩‍👧</div><h1>Nhật ký học <span id="who"></span></h1>
<p>Mỗi ngày học ít nhất 30 phút — bố mẹ xem lịch sử, đặt lời nhắc và nhận báo cáo</p>
<div class="toolbar"><a class="btn" href="index.html">🏠 Trang chủ</a><a class="btn" href="#sharebox">📤 Gửi báo cáo</a><a class="btn" href="#settings">⚙️ Cài đặt</a></div></header>
<main><div id="rbanner" class="rbanner" hidden></div><div id="warn" class="remind" hidden></div>
<div class="cards" id="stats"></div>
<h2>📅 Lịch học 30 ngày qua</h2><div class="cal" id="cal"></div>
<div class="legend2"><span><i style="background:#43a047"></i>Đạt mục tiêu</span><span><i style="background:#ffca28"></i>Có học, chưa đủ</span><span><i style="background:#ffcdd2"></i>Không học</span><span>Bấm vào một ngày để xem chi tiết</span></div>
<div id="oneday" hidden style="margin-top:12px"></div>
<h2>📋 Chi tiết 14 ngày gần nhất</h2><div id="days"></div>
<section id="sharebox"><h2>📤 Gửi báo cáo cho bố mẹ</h2><div class="panel">
Bấm nút dưới đây để gửi nhật ký học qua <b>Zalo, Messenger, tin nhắn…</b> Bố mẹ mở đường link sẽ thấy lịch học và chi tiết từng ngày, không cần cài đặt hay đăng nhập.
<br><button class="btn solid" onclick="shareReport()">📤 Gửi báo cáo</button>
<textarea id="shareout" rows="6" hidden readonly style="margin-top:10px"></textarea></div></section>
<section id="settings"><h2>⚙️ Cài đặt dành cho bố mẹ</h2><div class="panel" id="settings-body"></div>
<p class="note">ℹ️ Thời gian chỉ được tính khi ứng dụng đang mở trên màn hình và con có thao tác (bấm, cuộn, nghe…). Nếu không thao tác quá 3 phút thì dừng tính giờ.
Lịch sử được lưu ngay trên máy con học; nếu xóa dữ liệu trình duyệt hoặc đổi máy thì lịch sử sẽ mất.</p></section>
</main><style>{PARENT_CSS}</style><script>{PARENT_JS}</script>"""
with open(os.path.join(ROOT, "phu-huynh.html"), "w", encoding="utf-8") as f:
    f.write(page("Nhật ký học – Góc phụ huynh", "#ff8f00", ppage))
pages.append("phu-huynh.html")

# ───────────────────────── Ôn từ vựng (lặp lại ngắt quãng) ─────────────────────────
# Tiến độ từng từ lưu ở localStorage efk:srs {id: {c, d, n, w, s}}
#   c = số ngày khác nhau liên tiếp trả lời đúng · d = ngày gần nhất được tính · n = ngày đến hạn ôn
#   w = tổng số lần sai · s = số lần đã hỏi.  Đúng ở 3 ngày khác nhau liên tiếp (c ≥ 3) → giãn lịch ôn.
LEVEL_OPTS = [(g, f"Lớp {g}") for g in range(1, 13)] + [(v, ADULT_NAME[v]) for v in range(13, 17)] + [(17, "TOEIC")]
bank_topics = []
for slug, ico, en, vi, grade, color, words, pats in TOPICS:
    bank_topics.append([slug, ico, vi, en, grades(grade), [[w, ipa, m, ic] for ic, w, ipa, vn, m in parse(words, 5)]])
for slug, ico, en, vi, color, words in TOEIC_VOCAB:
    bank_topics.append([slug, ico, vi, en, [17], [[w, ipa, m, ic] for ic, w, ipa, vn, m in parse(words, 5)]])
BANK = {"L": LEVEL_OPTS, "T": bank_topics}

REVIEW_CSS = """
.rvwrap{max-width:720px;margin:0 auto}
.slots{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.slot{background:#fff;border-radius:18px;padding:12px 14px;box-shadow:0 3px 8px rgba(0,0,0,.06);text-align:center;border:3px solid #eee}
.slot b{display:block;font-size:24px}.slot span{color:#666;font-size:14px}
.slot.done{border-color:#43a047}.slot.due{border-color:#e53935;background:#fff5f5}
.go{display:block;width:100%;margin-top:14px;font-size:20px!important;padding:14px!important;background:var(--c)!important;color:#fff!important}
.rvq{background:#fff;border-radius:22px;padding:18px;box-shadow:0 6px 16px rgba(0,0,0,.08);text-align:center}
.rvq .prog{height:10px;background:#eee;border-radius:6px;overflow:hidden;margin-bottom:12px}.rvq .prog i{display:block;height:100%;background:var(--c);transition:width .3s}
.rvq .meta{display:flex;justify-content:space-between;color:#777;font-size:14px;font-weight:700}
.rvq .ask{color:#777;margin:10px 0 4px;font-weight:700}
.rvq .big{font-size:clamp(28px,8vw,40px);font-weight:800;color:var(--c);overflow-wrap:anywhere}
.rvq .ico2{font-size:56px;line-height:1.1}
.rvq .ipa{color:#555;font-family:'Lucida Sans Unicode','Arial Unicode MS',sans-serif}
.rvq .opts button{text-align:center;font-weight:700}
.rvq .say{position:static;font-size:26px}
.bigmic{font-size:44px;border:none;background:#fff3e0;border-radius:50%;width:96px;height:96px;cursor:pointer;margin:12px auto;display:block;box-shadow:0 3px 10px rgba(0,0,0,.15)}
.fb{margin-top:14px;border-radius:16px;padding:12px 14px;line-height:1.6}
.fb.ok{background:#e8f5e9}.fb.no{background:#ffebee}
.fb .w{font-size:22px;font-weight:800}
.row{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:12px}
.row .btn{border:2px solid var(--c)}
.chk{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:6px}
.chk label{display:flex!important;align-items:center;gap:6px;font-weight:600!important;margin:0!important}
.chk input{width:auto!important;margin:0!important}
.tplist{max-height:280px;overflow:auto;border:2px solid #eee;border-radius:12px;padding:8px 10px;margin-top:6px}
.tplist label{display:flex!important;gap:8px;align-items:center;font-weight:600!important;margin:4px 0!important}
.tplist input{width:auto!important;margin:0!important}
.times{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.hard li{margin:3px 0}
"""

REVIEW_JS = r"""
const B=__BANK__;
let ST={},SES=null,ONE=null;
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]];}return a;}
function addDays(k,n){const [y,m,d]=k.split('-').map(Number);return dkey(new Date(y,m-1,d+n));}
function clean(m){return m.replace(/^\([^)]*\)\s*/,'');}
function wcls(m){const r=m.match(/^\(([^)]*)\)/);return r?r[1]:'';}
function lvName(v){const x=B.L.find(l=>l[0]==v);return x?x[1]:'';}
function topicsOf(c){if(c.mode==='topic'&&c.tp.length)return B.T.filter(t=>c.tp.includes(t[0]));return B.T.filter(t=>t[4].includes(+c.lv));}
function wordsOf(ts){const o=[];ts.forEach(t=>t[5].forEach(w=>o.push({t,w,id:t[0]+'|'+w[0]})));return o;}
function scopeName(c){if(ONE)return ONE[1]+' '+ONE[2];if(c.mode==='topic'&&c.tp.length){const ts=topicsOf(c);return ts.length===1?ts[0][1]+' '+ts[0][2]:ts.length+' chủ đề ('+lvName(c.lv)+')';}return lvName(c.lv);}
function interval(s){const base=s.c<3?1:[4,7,14,30,60][Math.min(s.c-3,4)];return s.c>=3&&s.w>=3?Math.max(2,Math.round(base/2)):base;}
function grade(id,ok){const today=dkey(),s=ST[id]||{c:0,d:'',n:today,w:0,s:0};s.s++;
if(ok){if(s.d!==today){s.c++;s.d=today;s.n=addDays(today,interval(s));}}else{s.c=0;s.w++;s.d=today;s.n=today;}
ST[id]=s;sv(SRS,ST);}
function stage(id){const s=ST[id];return !s?'new':s.c>=3?'ok':'lrn';}
// Chọn từ: từ đến hạn (sai nhiều trước) → từ mới (để dành ~30% cho từ mới) → nếu vẫn thiếu thì lấy từ chưa đến hạn
function pickWords(words,k){const today=dkey(),due=[],fresh=[],later=[];
words.forEach(x=>{const s=ST[x.id];if(!s)fresh.push(x);else if(s.n<=today)due.push(x);else later.push(x);});
const by=(a,b)=>(ST[b.id].w-ST[a.id].w)||(ST[a.id].n<ST[b.id].n?-1:ST[a.id].n>ST[b.id].n?1:0);
due.sort(by);later.sort((a,b)=>((ST[a.id].c>=3)-(ST[b.id].c>=3))||by(a,b));
const nDue=Math.min(due.length,Math.max(k-Math.min(fresh.length,Math.ceil(k*.3)),0));
return due.slice(0,nDue).concat(fresh,due.slice(nDue),later).slice(0,k);}
function save(c){c.t=c.t.slice(0,2);if(c.t[1]&&hm2m(c.t[1])<hm2m(c.t[0]))c.t.reverse();sv(RVC,c);}
// ── Phiên ôn ──
function start(kind){const c=rvCfg();ST=ld(SRS,{});let ts=ONE?[ONE]:topicsOf(c);
if(!ts.length){toast('Hãy chọn lớp/trình độ hoặc chủ đề muốn ôn ở phần ⚙️ Cài đặt trước nhé',1);document.getElementById('caidat').scrollIntoView({behavior:'smooth'});return;}
const pool=wordsOf(ts);let list;
if(kind==='hard'){list=pool.filter(x=>ST[x.id]&&ST[x.id].w>0).sort((a,b)=>ST[b.id].w-ST[a.id].w).slice(0,c.k);if(!list.length)return toast('Chưa có từ nào trả lời sai trong phạm vi này 👍');}
else list=pickWords(pool,c.k);
let ty=c.ty.filter(t=>t!=='s'||SRec);if(!ty.length)ty=['m'];
SES={q:shuffle(list.slice()).map(x=>({x,ty:ty[Math.random()*ty.length|0]})),i:0,ok:0,n:list.length,bad:[],pool,first:{},tries:0};
document.getElementById('home').hidden=true;const se=document.getElementById('ses');se.hidden=false;ask();se.scrollIntoView({behavior:'smooth'});}
function opts(x,field){const val=w=>field==='m'?clean(w[2]):w[0],right=val(x.w),seen=new Set([right]),out=[right];
let src=x.t[5].filter(w=>w!==x.w);if(src.length<6)src=src.concat(SES.pool.map(p=>p.w));
shuffle(src.slice()).some(w=>{const v=val(w);if(!seen.has(v)){seen.add(v);out.push(v);}return out.length===4;});
return shuffle(out).map(v=>({v,ok:v===right}));}
function ask(){const Q=SES.q[SES.i],x=Q.x,[w,ipa,m,ic]=x.w,el=document.getElementById('ses');SES.tries=0;SES.lock=false;
let top='',body='';
if(Q.ty==='m'){top='<div class="ask">Từ này nghĩa là gì?</div><div class="big">'+esc(w)+'</div><div class="ipa">'+esc(ipa)+(wcls(m)?' · ('+esc(wcls(m))+')':'')+'</div><button class="say" onclick="say(\''+jsq(w)+'\')">🔊</button>';body=optsHTML(opts(x,'m'));}
else if(Q.ty==='r'){top='<div class="ask">Chọn từ tiếng Anh đúng:</div><div class="ico2">'+ic+'</div><div class="big" style="font-size:26px">'+esc(clean(m))+'</div>'+(wcls(m)?'<div class="ipa">('+esc(wcls(m))+')</div>':'');body=optsHTML(opts(x,'w'));}
else if(Q.ty==='l'){top='<div class="ask">Nghe và chọn nghĩa đúng:</div><button class="say" style="font-size:60px" onclick="say(\''+jsq(w)+'\')">🔊</button><div class="note">Bấm loa để nghe lại</div>';body=optsHTML(opts(x,'m'));setTimeout(()=>say(w),250);}
else{top='<div class="ask">Nói từ tiếng Anh có nghĩa là:</div><div class="ico2">'+ic+'</div><div class="big" style="font-size:26px">'+esc(clean(m))+'</div>';
body='<button class="bigmic" id="bm" onclick="speakTry()">🎤</button><div class="note" id="sm">Bấm 🎤 rồi nói to · còn 3 lượt</div><div class="row"><button class="btn" onclick="answer(false)">🙈 Không biết</button></div>';}
el.innerHTML='<div class="rvq"><div class="meta"><span>'+(SES.i+1)+'/'+SES.q.length+'</span><span>✅ '+SES.ok+'</span><span>'+esc(scopeName(rvCfg()))+'</span></div>'
+'<div class="prog"><i style="width:'+(SES.i/SES.q.length*100)+'%"></i></div>'+top+body+'<div id="fb"></div></div>'
+'<div class="row"><button class="btn" onclick="quit()">⏹️ Dừng ôn</button></div>';}
function jsq(t){return esc(t).replace(/\\/g,'\\\\').replace(/&#39;/g,"\\'");}
function optsHTML(o){SES.o=o;return '<div class="opts">'+o.map((x,k)=>'<button onclick="choose('+k+',this)">'+esc(x.v)+'</button>').join('')+'</div>';}
function choose(k,b){if(SES.lock)return;const ok=SES.o[k].ok;b.classList.add(ok?'right':'wrong');
document.querySelectorAll('.rvq .opts button').forEach((x,j)=>{if(SES.o[j].ok)x.classList.add('right');});answer(ok);}
function speakTry(){if(SES.lock)return;const Q=SES.q[SES.i],b=document.getElementById('bm'),sm=document.getElementById('sm');b.classList.add('rec');sm.textContent='Đang nghe… hãy nói ngay';
hear(Q.x.w[0],(r,err)=>{b.classList.remove('rec');if(SES.lock)return;
if(!r){sm.textContent=micErr(err);if(err==='not-allowed'||err==='unsupported'||err==='network')setTimeout(()=>answer(false,true),1500);return;}
if(r.score>=PASS)return answer(true,false,r.heard);SES.tries++;const left=3-SES.tries;
if(left<=0)return answer(false,false,r.heard);sm.textContent='Máy nghe thành “'+r.heard+'” — thử lại · còn '+left+' lượt';});}
function answer(ok,skip,heard){if(SES.lock)return;SES.lock=true;const Q=SES.q[SES.i],x=Q.x,[w,ipa,m,ic]=x.w;
if(!skip){grade(x.id,ok);if(!(x.id in SES.first)){SES.first[x.id]=ok;if(ok)SES.ok++;else SES.bad.push(x);}
if(!ok&&!Q.again)SES.q.splice(Math.min(SES.i+4,SES.q.length),0,{x,ty:Q.ty==='s'?'m':Q.ty,again:true});}
const s=ST[x.id]||{c:0};
document.getElementById('fb').innerHTML='<div class="fb '+(ok?'ok':'no')+'">'+(ok?'✅ Đúng rồi!':skip?'⏭️ Bỏ qua câu nói':'❌ Chưa đúng — từ này sẽ được hỏi lại')
+(heard?'<br><span class="note">Máy nghe được: “'+esc(heard)+'”</span>':'')
+'<div class="w">'+ic+' '+esc(w)+' <button class="say" onclick="say(\''+jsq(w)+'\')">🔊</button></div><div class="ipa">'+esc(ipa)+'</div><div>'+esc(m)+'</div>'
+(ok&&s.c>=3?'<div class="note">🌟 Đã đúng '+s.c+' ngày liên tiếp — từ này sẽ ít xuất hiện hơn</div>':ok&&s.c?'<div class="note">Đúng '+s.c+'/3 ngày liên tiếp</div>':'')
+'</div><div class="row"><button class="btn solid" id="nx" onclick="next()">Tiếp ➡️</button></div>';
say(w);const bt=document.getElementById('nx');bt.focus();if(ok)SES.auto=setTimeout(next,1800);}
function next(){clearTimeout(SES.auto);if(!SES.lock)return;SES.i++;if(SES.i<SES.q.length)ask();else finish(true);}
addEventListener('keydown',ev=>{if(ev.key==='Enter'&&SES&&SES.lock&&document.getElementById('nx')){ev.preventDefault();next();}});
function quit(){clearTimeout(SES.auto);if(Object.keys(SES.first).length&&confirm('Dừng ôn? Kết quả các từ đã làm vẫn được lưu, nhưng lượt này chưa được tính là một buổi ôn.'))finish(false);else if(!Object.keys(SES.first).length)home();}
function finish(full){const n=Object.keys(SES.first).length,log=ld(LOG,{}),r=dayRec(log,dkey());
if(n){(r.rv=r.rv||[]).push([nowM(),SES.ok,n,full&&n>0?1:0,scopeName(rvCfg())]);sv(LOG,log);}
const sl=rvSlots(),left=sl.filter(s=>!s.done).length;
document.getElementById('ses').innerHTML='<div class="rvq"><div class="ico2">'+(SES.ok>=n*.8?'🏆':SES.ok>=n*.5?'👍':'💪')+'</div><div class="big" style="font-size:30px">Đúng '+SES.ok+'/'+n+'</div>'
+(full?'<p>'+(left?'Hôm nay còn <b>'+left+' buổi ôn</b> bắt buộc ('+sl.filter(s=>!s.done).map(s=>s.t).join(', ')+').':'🎉 Đã hoàn thành các buổi ôn hôm nay!')+'</p>':'<p>Đã dừng giữa chừng.</p>')
+(SES.bad.length?'<div class="fb no" style="text-align:left"><b>Từ cần ôn thêm:</b><ul class="hard">'+SES.bad.map(x=>'<li>'+x.w[3]+' <b>'+esc(x.w[0])+'</b> — '+esc(x.w[2])+'</li>').join('')+'</ul></div>':'')
+'<div class="row"><button class="btn solid" onclick="start()">🔁 Ôn thêm lượt nữa</button><button class="btn" onclick="home()">🏠 Về trang ôn tập</button></div></div>';
SES=null;rvCheck();if(full&&!left)toast('🎉 Giỏi quá! Đã hoàn thành các buổi ôn hôm nay');}
function home(){SES=null;document.getElementById('ses').hidden=true;document.getElementById('home').hidden=false;render();scrollTo({top:0});}
// ── Trang chính ──
function render(){const c=rvCfg(),set=!!ld(RVC,null);ST=ld(SRS,{});
const sl=rvSlots(),names=c.n===1?['Hôm nay']:['Buổi sáng','Buổi tối'];
document.getElementById('slots').innerHTML=set?sl.map((s,i)=>'<div class="slot '+(s.done?'done':s.due?'due':'')+'"><span>'+names[i]+'</span><b>'+s.t+'</b><span>'+(s.done?'✅ Đã ôn':s.due?'⏰ Đến giờ ôn!':'⏳ Chưa đến giờ')+'</span></div>').join('')
:'<div class="remind">👋 Chào bạn! Hãy chọn <b>lớp hoặc chủ đề</b>, số từ mỗi lần và giờ ôn ở phần <a href="#caidat">⚙️ Cài đặt</a> bên dưới. App sẽ nhắc bạn ôn mỗi ngày.</div>';
const today=(ld(LOG,{})[dkey()]||{}).rv||[];
document.getElementById('todaylog').innerHTML=today.length?'Hôm nay đã ôn '+today.length+' lượt: '+today.map(x=>String(x[0]/60|0).padStart(2,'0')+':'+String(x[0]%60).padStart(2,'0')+' ('+x[1]+'/'+x[2]+')').join(' · '):'';
const ts=ONE?[ONE]:topicsOf(c),pool=wordsOf(ts),td=dkey();let nw=0,lr=0,ok=0,due=0;
pool.forEach(x=>{const s=ST[x.id];if(!s)nw++;else{if(s.c>=3)ok++;else lr++;if(s.n<=td)due++;}});
document.getElementById('scope').innerHTML=ts.length?'📚 Đang ôn: <b>'+esc(scopeName(c))+'</b> · '+pool.length+' từ'+(ONE?' · <a href="#" onclick="ONE=null;history.replaceState(null,\'\',location.pathname);render();return false">Quay lại phạm vi đã cài đặt</a>':''):'📚 Chưa chọn phạm vi ôn';
document.getElementById('stats').innerHTML=[['🆕',nw,'từ mới'],['📖',lr,'đang học'],['🌟',ok,'đã thuộc (đúng 3 ngày)'],['⏰',due,'cần ôn hôm nay']].map(a=>'<div class="stat"><b>'+a[0]+' '+a[1]+'</b><span>'+a[2]+'</span></div>').join('')
+(pool.length?'<div class="stat" style="grid-column:1/-1"><div class="bar"><i style="width:'+(ok/pool.length*100)+'%"></i></div><span>Đã thuộc '+Math.round(ok/pool.length*100)+'% phạm vi này</span></div>':'');
const hard=pool.filter(x=>ST[x.id]&&ST[x.id].w>0).sort((a,b)=>ST[b.id].w-ST[a.id].w).slice(0,10);
document.getElementById('hard').innerHTML=hard.length?'<ul class="hard">'+hard.map(x=>'<li>'+x.w[3]+' <b>'+esc(x.w[0])+'</b> — '+esc(x.w[2])+' <span class="note">(sai '+ST[x.id].w+' lần'+(ST[x.id].c?', đã đúng lại '+ST[x.id].c+' ngày':'')+')</span></li>').join('')+'</ul>':'<p class="note">Chưa có từ nào trả lời sai 👍</p>';
document.getElementById('hardbtn').hidden=!hard.length;
document.getElementById('gobtn').textContent='▶️ Bắt đầu ôn '+Math.min(c.k,pool.length||c.k)+' từ';settings();}
function settings(){const c=rvCfg(),box=document.getElementById('rvset');
const lv='<label>Lớp / trình độ<select id="r-lv" onchange="setLv(this.value)"><option value="">— Chọn —</option>'+B.L.map(l=>'<option value="'+l[0]+'"'+(l[0]==c.lv?' selected':'')+'>'+esc(l[1])+'</option>').join('')+'</select></label>';
const ts=c.lv?B.T.filter(t=>t[4].includes(+c.lv)):[];
const tp=c.lv?'<label>Ôn theo<div class="chk"><label><input type="radio" name="r-mode" value="level"'+(c.mode!=='topic'?' checked':'')+' onchange="setF(\'mode\',\'level\')"> Cả lớp / trình độ ('+wordsOf(ts).length+' từ)</label>'
+'<label><input type="radio" name="r-mode" value="topic"'+(c.mode==='topic'?' checked':'')+' onchange="setF(\'mode\',\'topic\')"> Chọn chủ đề</label></div></label>'
+(c.mode==='topic'?'<div class="tplist">'+ts.map(t=>'<label><input type="checkbox" value="'+t[0]+'"'+(c.tp.includes(t[0])?' checked':'')+' onchange="setTp(this)"> '+t[1]+' '+esc(t[2])+' <span class="note">('+t[5].length+' từ)</span></label>').join('')+'</div>':''):'';
box.innerHTML=lv+tp
+'<label>Số từ mỗi lần ôn<select onchange="setF(\'k\',+this.value)">'+[5,10,15,20,25,30,40,50].map(k=>'<option'+(k===c.k?' selected':'')+'>'+k+'</option>').join('')+'</select></label>'
+'<label>Số buổi ôn bắt buộc mỗi ngày<select onchange="setF(\'n\',+this.value)"><option value="1"'+(c.n===1?' selected':'')+'>1 buổi</option><option value="2"'+(c.n===2?' selected':'')+'>2 buổi (sáng và tối)</option></select></label>'
+'<div class="times"><label>'+(c.n===1?'Giờ ôn':'Giờ buổi sáng')+'<input type="time" value="'+c.t[0]+'" onchange="setT(0,this.value)"></label>'
+(c.n===2?'<label>Giờ buổi tối<input type="time" value="'+(c.t[1]||'19:30')+'" onchange="setT(1,this.value)"></label>':'')+'</div>'
+'<label>Dạng câu hỏi<div class="chk">'+[['m','👀 Xem từ → chọn nghĩa'],['r','🇻🇳 Xem nghĩa → chọn từ'],['l','🔊 Nghe → chọn nghĩa'],['s','🎤 Nói từ tiếng Anh'+(SRec?'':' (máy này chưa hỗ trợ)')]]
.map(a=>'<label><input type="checkbox" value="'+a[0]+'"'+(c.ty.includes(a[0])?' checked':'')+' onchange="setTy(this)"> '+a[1]+'</label>').join('')+'</div></label>'
+'<p class="note">Cài đặt được lưu ngay khi thay đổi.</p>';}
function upd(f){const c=rvCfg();f(c);save(c);ONE=null;render();rvCheck();}
function setF(k,v){upd(c=>{c[k]=v;if(k==='n'&&v===2&&!c.t[1])c.t[1]='19:30';});}
function setLv(v){upd(c=>{c.lv=v?+v:'';c.tp=[];c.mode='level';});}
function setTp(el){upd(c=>{c.tp=c.tp.filter(x=>x!==el.value);if(el.checked)c.tp.push(el.value);});}
function setTy(el){upd(c=>{c.ty=c.ty.filter(x=>x!==el.value);if(el.checked)c.ty.push(el.value);if(!c.ty.length){c.ty=['m'];toast('Cần ít nhất một dạng câu hỏi',1);}});}
function setT(i,v){if(!v)return;upd(c=>{c.t[i]=v;});}
// ── Nhắc nhở ──
async function askNotify(){if(!('Notification' in window))return toast('Trình duyệt này không hỗ trợ thông báo. Hãy dùng “Thêm vào lịch” bên dưới.',1);
const p=await Notification.requestPermission();notifyUI();if(p==='granted'){rvNotify('Đã bật thông báo nhắc giờ ôn 👍');}else toast('Chưa được cho phép thông báo',1);}
function notifyUI(){const el=document.getElementById('nstate');if(!('Notification' in window)){el.textContent='❌ Trình duyệt này không hỗ trợ thông báo (trên iPhone cần cài app ra màn hình chính, iOS 16.4 trở lên).';return;}
el.textContent=Notification.permission==='granted'?'✅ Đã bật thông báo':Notification.permission==='denied'?'❌ Thông báo đang bị chặn — mở cài đặt trình duyệt để cho phép':'Chưa bật';}
function icsStamp(d){return d.toISOString().replace(/[-:]/g,'').split('.')[0]+'Z';}
function slotNames(c){return c.n===1?['Ôn từ vựng tiếng Anh']:['Ôn từ vựng tiếng Anh – buổi sáng','Ôn từ vựng tiếng Anh – buổi tối'];}
function plus15(t){const m=hm2m(t)+15;return String((m/60|0)%24).padStart(2,'0')+String(m%60).padStart(2,'0');}
function calFile(){const c=rvCfg(),url=location.href.split('#')[0],d=dkey().replace(/-/g,''),now=icsStamp(new Date()),nm=slotNames(c);
const ev=c.t.slice(0,c.n).map((t,i)=>['BEGIN:VEVENT','UID:efk-on-tap-'+i+'-'+Date.now()+'@english-for-kids','DTSTAMP:'+now,'DTSTART:'+d+'T'+t.replace(':','')+'00','DTEND:'+d+'T'+plus15(t)+'00',
'RRULE:FREQ=DAILY','SUMMARY:🔁 '+nm[i],'DESCRIPTION:Mở app English for Kids để ôn từ: '+url,'URL:'+url,'BEGIN:VALARM','ACTION:DISPLAY','DESCRIPTION:Đến giờ ôn từ vựng!','TRIGGER:PT0M','END:VALARM','END:VEVENT'].join('\r\n'));
const s=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//English for Kids//On tap//VI','CALSCALE:GREGORIAN','METHOD:PUBLISH',...ev,'END:VCALENDAR'].join('\r\n');
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([s],{type:'text/calendar'}));a.download='nhac-on-tu-vung.ics';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove();},1000);}
function gcal(){const c=rvCfg(),url=location.href.split('#')[0],d=dkey().replace(/-/g,''),nm=slotNames(c);
document.getElementById('glinks').innerHTML=c.t.slice(0,c.n).map((t,i)=>'<a class="btn" target="_blank" rel="noopener" href="https://calendar.google.com/calendar/render?action=TEMPLATE&text='+encodeURIComponent('🔁 '+nm[i])
+'&dates='+d+'T'+t.replace(':','')+'00/'+d+'T'+plus15(t)+'00&recur='+encodeURIComponent('RRULE:FREQ=DAILY')+'&details='+encodeURIComponent('Mở app English for Kids để ôn từ: '+url)+'">📆 Google Lịch: '+t+'</a>').join('');}
function fromHash(){const h=location.hash,t=h.match(/^#t=([\w-]+)/),l=h.match(/^#lv=(\d+)/);ONE=null;
if(t){ONE=B.T.find(x=>x[0]===t[1])||null;}
if(l&&!rvCfg().lv){const c=rvCfg();c.lv=+l[1];c.mode='level';save(c);}}
addEventListener('DOMContentLoaded',()=>{fromHash();render();notifyUI();gcal();});
addEventListener('hashchange',()=>{if(!SES){fromHash();render();}});
"""

rpage = f"""<header><div class="big">🔁</div><h1>Ôn từ vựng mỗi ngày</h1>
<p>Sáng và tối, theo lớp hoặc chủ đề — từ hay sai sẽ gặp lại nhiều hơn</p>
<div class="toolbar"><a class="btn" href="index.html">🏠 Trang chủ</a><a class="btn" href="#caidat">⚙️ Cài đặt</a><a class="btn" href="#nhac">🔔 Nhắc giờ</a><a class="btn" href="phu-huynh.html">👨‍👩‍👧 Nhật ký học</a></div></header>
<main><div class="rvwrap"><div id="ses" hidden></div><div id="home">
<div class="slots" id="slots"></div><p class="note" id="todaylog"></p>
<div class="panel"><div id="scope"></div>
<button class="btn go" id="gobtn" onclick="start()">▶️ Bắt đầu ôn</button>
<div class="row"><button class="btn" id="hardbtn" onclick="start('hard')" hidden>🎯 Chỉ ôn từ hay sai</button></div>
<p class="note">Có thể ôn bất cứ lúc nào, bao nhiêu lần cũng được. Mỗi lượt ôn trọn vẹn được tính cho buổi bắt buộc chưa xong.</p></div>
<h2>📊 Tiến độ</h2><div class="cards" id="stats"></div>
<h2>❗ Từ hay sai</h2><div class="panel" id="hard"></div>
<section id="caidat"><h2>⚙️ Cài đặt ôn tập</h2><div class="panel" id="rvset"></div></section>
<section id="nhac"><h2>🔔 Nhắc giờ ôn</h2><div class="panel">
<b>1. Thông báo của ứng dụng</b> — <span id="nstate"></span><br>
<button class="btn solid" onclick="askNotify()">🔔 Bật thông báo</button>
<p class="note">Khi đến giờ, app hiện thông báo và dải nhắc màu cam trên mọi trang. Vì app chạy không cần máy chủ, thông báo chỉ hiện được khi app đang mở (hoặc chạy nền). Để chắc chắn được nhắc cả khi đã tắt app, hãy dùng cách 2.</p>
<b>2. Thêm lịch nhắc hằng ngày vào điện thoại</b> (nhắc đúng giờ cả khi tắt app)<br>
<button class="btn solid" onclick="calFile()">📅 Tải lịch nhắc (iPhone, Outlook, Lịch Android)</button>
<div class="row" id="glinks" style="justify-content:flex-start"></div>
<p class="note">iPhone: mở trang này bằng Safari, bấm “Tải lịch nhắc” → “Thêm tất cả”. Android: dùng nút Google Lịch (mỗi buổi một nút) → Lưu. Đổi giờ ôn thì xóa lịch cũ và thêm lại.</p></div></section>
<h2>💡 Cách app chọn từ để ôn</h2><div class="tips">
1️⃣ Mỗi lượt lấy trước các <b>từ đến hạn ôn</b> (từ sai nhiều xếp đầu), sau đó là <b>từ mới</b> (luôn dành khoảng 30% cho từ mới).<br>
2️⃣ Trả lời <b>sai</b>: từ đó được hỏi lại ngay trong lượt, và tiếp tục xuất hiện ở các lượt sau trong ngày và ngày mai.<br>
3️⃣ Trả lời <b>đúng</b>: mỗi ngày chỉ tính một lần. Đúng <b>3 ngày khác nhau liên tiếp</b> → từ được coi là đã thuộc 🌟 và giãn ra 4, 7, 14, 30, 60 ngày mới hỏi lại. Sai một lần là đếm lại từ đầu.<br>
4️⃣ Từ đã sai từ 3 lần trở lên thì dù đã thuộc vẫn được hỏi lại sớm hơn (khoảng cách giảm một nửa).<br>
5️⃣ Câu nói 🎤: máy nghe và so với từ đúng; có 3 lượt thử. Nhận giọng nói cần mạng Internet.
</div></div></div></main>
<style>{PARENT_CSS}{REVIEW_CSS}</style><script>{REVIEW_JS.replace("__BANK__", json.dumps(BANK, ensure_ascii=False, separators=(",", ":")))}</script>"""
with open(os.path.join(ROOT, "on-tap.html"), "w", encoding="utf-8") as f:
    f.write(page("Ôn từ vựng – English for Kids", "#00897b", rpage))
pages.append("on-tap.html")

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
self.addEventListener('notificationclick', e => {{
  e.notification.close();
  const url = new URL((e.notification.data && e.notification.data.url) || 'on-tap.html', self.location).href;
  e.waitUntil(clients.matchAll({{type: 'window', includeUncontrolled: true}}).then(ws => {{
    const w = ws.find(c => c.url.split('#')[0] === url);
    return w ? w.focus() : clients.openWindow(url);
  }}));
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

print(f"OK: {len(TOPICS)} chủ đề, {total} từ, {len(GRAMMAR)} bài ngữ pháp, TOEIC {len(TOEIC) + len(listen_read)} bài / {total_q} câu / {toeic_words} từ, {len(precache)} file được cache offline")
