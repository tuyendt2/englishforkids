# English for Kids 🎈📚

Từ vựng · Mẫu câu · Ngữ pháp tiếng Anh từ **Lớp 1 đến Lớp 12** (bám theo chủ đề sách Global Success) và cho **sinh viên & người lớn** ở trình độ **C1, C2, Fluent, Native**.
Web tĩnh, cài được lên Android/iOS như một ứng dụng (PWA) và học được khi không có mạng.

- 148 chủ đề · 3.442 từ vựng (IPA, nghĩa tiếng Việt, nút nghe đọc)
  - Lớp 1–4: 20 chủ đề dùng chung · Lớp 5: 10 · Lớp 6–9: 12 mỗi lớp · Lớp 10–12: 10 mỗi lớp (24 từ/chủ đề)
  - Sinh viên & Người lớn: C1, C2, Fluent, Native — 10 chủ đề mỗi trình độ (24 từ/chủ đề), gồm từ học thuật, thành ngữ, cụm động từ, tiếng lóng
- Mỗi chủ đề có mẫu câu hỏi – đáp và một bài ngữ pháp; trang `ngu-phap.html` tổng hợp toàn bộ
- **🎯 Luyện thi TOEIC** (`toeic.html`): 16 bài — từ loại (danh từ, động từ, tính từ, trạng từ, giới từ, liên từ, đại từ, họ từ) và ngữ pháp trọng tâm (thì, bị động, to V/V-ing, mệnh đề quan hệ, so sánh, lượng từ, câu điều kiện & đảo ngữ, từ dễ nhầm). Mỗi bài có lý thuyết + 15 câu trắc nghiệm kiểu Part 5 chấm điểm, giải thích tiếng Việt; thêm đề tổng hợp 30 câu ngẫu nhiên có bấm giờ (241 câu trong ngân hàng)
- **🎯 TOEIC mở rộng:** 10 chủ đề từ vựng TOEIC (240 từ); **nghe** Part 2 (25 câu hỏi – đáp), Part 3 (8 hội thoại), Part 4 (6 bài nói) dùng giọng đọc của trình duyệt (hội thoại có giọng nam/nữ, lời thoại hiện sau khi làm); **đọc** Part 6 (4 đoạn văn, 16 câu) và Part 7 (5 bài đọc, có 1 bài 2 văn bản). Part 1 chưa có vì cần ảnh thật
- **🔁 Ôn từ vựng** (`on-tap.html`): ôn theo lớp/trình độ (Lớp 1–12, C1 → Native, TOEIC) hoặc chọn từng chủ đề; tự chọn số từ mỗi lượt, 1 hoặc 2 buổi bắt buộc mỗi ngày và giờ ôn. Dạng câu hỏi: xem từ → chọn nghĩa, xem nghĩa → chọn từ, nghe → chọn nghĩa, nói 🎤. Lặp lại ngắt quãng: đúng ở 3 ngày khác nhau liên tiếp → giãn lịch (4, 7, 14, 30, 60 ngày); sai → hỏi lại ngay trong lượt, tiếp tục xuất hiện trong ngày và đếm lại từ đầu. Nhắc giờ bằng dải nhắc + thông báo khi app đang mở, và bằng lịch nhắc hằng ngày (.ics / Google Lịch) để nhắc cả khi tắt app. Tiến độ lưu ở `efk:srs`, cài đặt ở `efk:rvcfg`, các lượt ôn ghi vào nhật ký học
- **🎤 Luyện phát âm:** mỗi thẻ từ có nút micro — đọc to, máy nhận giọng nói (Chrome/Safari, cần mạng) và báo đúng hay chưa
- **👨‍👩‍👧 Nhật ký học & Góc phụ huynh** (`phu-huynh.html`): tự tính thời gian học mỗi ngày (chỉ khi app đang mở và có thao tác; dừng sau 3 phút không thao tác), mục tiêu mặc định 30 phút, đồng hồ ⏱️ ở góc màn hình, lịch 30 ngày, chi tiết bài đã học và điểm bài tập. Bố mẹ đặt mã PIN, đổi mục tiêu, viết lời nhắc hiện trên trang chủ; con bấm “Gửi báo cáo” để gửi link nhật ký qua Zalo/Messenger (dữ liệu nén trong link, không cần máy chủ)
- Lọc theo lớp, chế độ ẩn nghĩa để tự kiểm tra, in ra giấy

## Cài lên điện thoại
Mở trang qua **HTTPS** (ví dụ GitHub Pages):
- **Android (Chrome):** bấm nút “📲 Cài ứng dụng” hoặc menu ⋮ → *Cài đặt ứng dụng*.
- **iPhone/iPad (Safari):** nút Chia sẻ ⬆️ → *Thêm vào MH chính*.

## Sửa nội dung
Dữ liệu Lớp 1–4 nằm trong `_data.py` (từ vựng, mẫu câu) và `_grammar.py` (ngữ pháp).
Mỗi lớp từ 5 đến 12 có một file riêng `_data_lop05.py` … `_data_lop12.py`, chứa cả `TOPICS` và `GRAMMAR`.
Phần người lớn nằm trong `_data_c1.py`, `_data_c2.py`, `_data_fluent.py`, `_data_native.py` (cùng định dạng).
Phần TOEIC nằm trong `_toeic_tu_loai.py` và `_toeic_ngu_phap.py` (Part 5; mỗi câu hỏi một dòng `câu có ___|đáp án đúng|sai|sai|sai|giải thích`, build tự xáo vị trí A–D), `_toeic_tu_vung.py` (từ vựng, cùng định dạng thẻ từ) và `_toeic_nghe_doc.py` (Part 2–4, 6–7; định dạng ghi ở đầu file).
Sau khi sửa, chạy:

```bash
python3 build.py
```

Lệnh này tạo lại `index.html`, `ngu-phap.html`, `toeic.html`, `on-tap.html`, `phu-huynh.html`, `chu-de/*.html`, `toeic/*.html`, `manifest.webmanifest`, `sw.js` và `icons/`.
Không sửa tay các file HTML được sinh ra.
