// Tự sinh bởi build.py — không sửa tay
const CACHE = 'efk-1c0e91944b';
const FILES = ["./", "index.html", "ngu-phap.html", "chu-de/01-chao-hoi.html", "chu-de/02-so-dem.html", "chu-de/03-mau-sac-hinh-khoi.html", "chu-de/04-do-dung-hoc-tap.html", "chu-de/05-truong-lop-mon-hoc.html", "chu-de/06-gia-dinh.html", "chu-de/07-co-the-khuon-mat.html", "chu-de/08-dong-vat.html", "chu-de/09-do-an-thuc-uong.html", "chu-de/10-quan-ao.html", "chu-de/11-do-choi.html", "chu-de/12-ngoi-nha.html", "chu-de/13-nghe-nghiep.html", "chu-de/14-thoi-tiet-mua.html", "chu-de/15-ngay-thang-gio.html", "chu-de/16-so-thich-the-thao.html", "chu-de/17-noi-chon.html", "chu-de/18-hoat-dong-hang-ngay.html", "chu-de/19-cam-xuc-tinh-cach.html", "chu-de/20-quoc-gia-thien-nhien.html", "chu-de/21-suc-khoe.html", "chu-de/22-giao-thong.html", "chu-de/23-le-hoi.html", "chu-de/24-ky-nghi.html", "chu-de/25-khu-pho.html", "chu-de/26-truyen-hinh.html", "chu-de/27-nha-tuong-lai.html", "chu-de/28-the-gioi-xanh.html", "chu-de/29-song-khoe.html", "chu-de/30-cong-dong.html", "chu-de/31-phim-anh.html", "chu-de/32-nang-luong.html", "chu-de/33-nong-thon.html", "chu-de/34-phong-tuc.html", "chu-de/35-thien-tai.html", "chu-de/36-khoa-hoc-cong-nghe.html", "chu-de/37-cuoc-song-thanh-pho.html", "chu-de/38-du-lich.html", "chu-de/39-thiet-bi-dien-tu.html", "chu-de/40-chon-nghe.html", "chu-de/41-cuoc-song-gia-dinh.html", "chu-de/42-phat-minh.html", "chu-de/43-binh-dang-gioi.html", "chu-de/44-du-lich-sinh-thai.html", "chu-de/45-song-khoe-song-lau.html", "chu-de/46-khoang-cach-the-he.html", "chu-de/47-nong-len-toan-cau.html", "chu-de/48-di-san.html", "chu-de/49-da-van-hoa.html", "chu-de/50-the-gioi-viec-lam.html", "chu-de/51-tri-tue-nhan-tao.html", "chu-de/52-bao-ton-dong-vat.html", "manifest.webmanifest", "icons/apple-touch-icon.png", "icons/icon-192.png", "icons/icon-512.png", "icons/icon-maskable-512.png"];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(caches.match(e.request, {ignoreSearch: true}).then(hit => hit || fetch(e.request).then(res => {
    if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); }
    return res;
  }).catch(() => caches.match('index.html'))));
});
