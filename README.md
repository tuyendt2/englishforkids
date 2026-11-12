# English for Kids 🎈📚

Từ vựng · Mẫu câu · Ngữ pháp tiếng Anh từ **Lớp 1 đến Lớp 12** (bám theo chủ đề sách Global Success).
Web tĩnh, cài được lên Android/iOS như một ứng dụng (PWA) và học được khi không có mạng.

- 52 chủ đề · 882 từ vựng (IPA, nghĩa tiếng Việt, nút nghe đọc)
- Mỗi chủ đề có mẫu câu hỏi – đáp và một bài ngữ pháp; trang `ngu-phap.html` tổng hợp toàn bộ
- Lọc theo lớp, chế độ ẩn nghĩa để tự kiểm tra, in ra giấy

## Cài lên điện thoại
Mở trang qua **HTTPS** (ví dụ GitHub Pages):
- **Android (Chrome):** bấm nút “📲 Cài ứng dụng” hoặc menu ⋮ → *Cài đặt ứng dụng*.
- **iPhone/iPad (Safari):** nút Chia sẻ ⬆️ → *Thêm vào MH chính*.

## Sửa nội dung
Dữ liệu nằm trong `_data.py` (Lớp 1–4), `_data_lop5_9.py`, `_data_lop10_12.py` và `_grammar.py`.
Sau khi sửa, chạy:

```bash
python3 build.py
```

Lệnh này tạo lại `index.html`, `ngu-phap.html`, `chu-de/*.html`, `manifest.webmanifest`, `sw.js` và `icons/`.
Không sửa tay các file HTML được sinh ra.
