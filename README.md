# English for Kids 🎈📚

Từ vựng · Mẫu câu · Ngữ pháp tiếng Anh từ **Lớp 1 đến Lớp 12** (bám theo chủ đề sách Global Success) và cho **sinh viên & người lớn** ở trình độ **C1, C2, Fluent, Native**.
Web tĩnh, cài được lên Android/iOS như một ứng dụng (PWA) và học được khi không có mạng.

- 148 chủ đề · 3.442 từ vựng (IPA, nghĩa tiếng Việt, nút nghe đọc)
  - Lớp 1–4: 20 chủ đề dùng chung · Lớp 5: 10 · Lớp 6–9: 12 mỗi lớp · Lớp 10–12: 10 mỗi lớp (24 từ/chủ đề)
  - Sinh viên & Người lớn: C1, C2, Fluent, Native — 10 chủ đề mỗi trình độ (24 từ/chủ đề), gồm từ học thuật, thành ngữ, cụm động từ, tiếng lóng
- Mỗi chủ đề có mẫu câu hỏi – đáp và một bài ngữ pháp; trang `ngu-phap.html` tổng hợp toàn bộ
- Lọc theo lớp, chế độ ẩn nghĩa để tự kiểm tra, in ra giấy

## Cài lên điện thoại
Mở trang qua **HTTPS** (ví dụ GitHub Pages):
- **Android (Chrome):** bấm nút “📲 Cài ứng dụng” hoặc menu ⋮ → *Cài đặt ứng dụng*.
- **iPhone/iPad (Safari):** nút Chia sẻ ⬆️ → *Thêm vào MH chính*.

## Sửa nội dung
Dữ liệu Lớp 1–4 nằm trong `_data.py` (từ vựng, mẫu câu) và `_grammar.py` (ngữ pháp).
Mỗi lớp từ 5 đến 12 có một file riêng `_data_lop05.py` … `_data_lop12.py`, chứa cả `TOPICS` và `GRAMMAR`.
Phần người lớn nằm trong `_data_c1.py`, `_data_c2.py`, `_data_fluent.py`, `_data_native.py` (cùng định dạng).
Sau khi sửa, chạy:

```bash
python3 build.py
```

Lệnh này tạo lại `index.html`, `ngu-phap.html`, `chu-de/*.html`, `manifest.webmanifest`, `sw.js` và `icons/`.
Không sửa tay các file HTML được sinh ra.
