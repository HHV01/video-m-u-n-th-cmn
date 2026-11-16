## 4C. Thiết lập giọng đọc (ElevenLabs hoặc công cụ tương đương)
- Mỗi nhân vật 1 voice cố định, ghi Voice ID vào bảng quản lý (4D). **Không đổi voice giữa các tập.**
- Gợi ý: Linh (nữ trẻ), Minh (nam trầm), Mai (nữ ấm), Sarah (nữ dứt khoát), Trang (nữ rõ ràng), Đức (nam nhẹ), Hải (nam thư thả).
- Giọng tiếng Anh nên chuẩn, tốc độ chậm vừa phải cho người học (khoảng 0.9x). Đoạn công thức đọc chậm hơn.
- Xuất từng câu thành 1 file riêng (`Mai_Shot06.mp3`) để dễ căn chữ ở CapCut.
- Kiểm tra điều khoản thương mại của gói đang dùng trước khi monetize.

## 4D. Thư viện asset và quy ước đặt tên
```
NovaTech_English/
├── 00_Brand/        (logo, avatar, banner, font, bảng màu)
├── 01_Characters/   Minh/ Linh/ Trang/ Duc/ Sarah/ Hai/ Mai/
│                    (6 biểu cảm + 8 pose mỗi người, PNG trong suốt)
├── 02_Backgrounds/  BG-01-A.png ... BG-08-B.png (16 file)
├── 03_Props/        P-01_JiraTicket.png ... P-10
├── 04_Icons/        I-01_Warning.png ... I-12
├── 05_Voices/       (bảng Voice ID + file mẫu)
├── 06_SFX/          typewriter, pop, whoosh, sigh...
├── 07_Music/        (nhạc nền + outro royalty-free, kèm file ghi nguồn/giấy phép)
├── 08_Scripts/      (mỗi video 1 thư mục: spec, bảng shot, voice)
├── 09_Projects/     (file CapCut)
├── 10_Exports/
└── 11_Thumbnails/
```
Quy ước: `Tên_BiểuCảm.png`, `Tên_Pose_P01.png`, `Tên_ShotNN.mp3`, video: `NT-001_Tênngắn_v1`.

Bảng quản lý (Google Sheets) gồm các sheet: **Voices** (nhân vật, voice ID, cài đặt), **Videos** (mã, tên, công thức, ngày đăng, link), **Analytics** (xem 4G).

## 4E. Thông số xuất file
| Loại | Độ phân giải | Khung hình | Định dạng |
|---|---|---|---|
| Short | 1080×1920 (9:16) | 30 fps | MP4 H.264, AAC |
| Video dài | 1920×1080 (16:9) | 30 fps | MP4 H.264, AAC |
| Thumbnail | 1280×720 | — | PNG/JPG < 2MB |

Vùng an toàn Short: chữ cách mép trên/dưới ≥ 15%, tránh vùng nút YouTube ở cạnh phải và phần mô tả ở dưới.
Âm thanh: giọng nói quanh −14 LUFS, nhạc nền thấp hơn giọng ≥ 15 dB (≤ −25 dB), không để clipping.
**Phụ đề:** bật phụ đề/CC tiếng Anh (có thể thêm tiếng Việt cho video dài) để tăng khả năng tiếp cận.

## 4F. Quy trình làm việc hằng tuần (3 Short/tuần)
| Ngày | Việc | Thời gian |
|---|---|---|
| T2 | `/idea` chọn 3 chủ đề từ 4A; `/video` cho 3 video; rà soát kịch bản | 1,5 giờ |
| T3 | Tạo asset thiếu; thu voice 3 video | 2 giờ |
| T4 | Dựng 3 video trong CapCut (duplicate project cũ) | 3 giờ |
| T5 | `/qc`, sửa, tạo thumbnail, đặt lịch đăng | 1,5 giờ |
| T6–CN | Đăng, trả lời comment, ghi số liệu | 1 giờ |

Sau video thứ 3–5, đủ mẫu để rút thời gian dựng xuống rõ rệt.

## 4G. Theo dõi chỉ số và quy tắc điều chỉnh
Ghi sau 48 giờ và 7 ngày: lượt xem, retention trung bình, mốc rớt người xem lớn nhất (giây thứ mấy), CTR thumbnail, comment, share, subscriber mới.

| Hiện tượng | Nguyên nhân hay gặp | Cách sửa |
|---|---|---|
| Rớt mạnh ở 0–3s | Hook yếu | Đổi cảnh mở: biểu cảm mạnh hơn, bỏ chữ, cắt ngắn |
| Rớt ở phần Vấn đề | Dài, chán | Rút còn ≤ 10s, tăng phản ứng nhân vật |
| Rớt trước Payoff | Công thức dài | Rút công thức xuống 3 dòng |
| CTR thấp | Thumbnail/tiêu đề mờ | Từ khóa to hơn, ≤ 5 từ, tương phản cao |
| Xem nhiều nhưng ít sub | Thiếu lý do theo dõi | CTA gắn series: "Next: Code Review" |

Mục tiêu trong tài liệu gốc (retention ≥ 65%, CTR ≥ 6%...) chỉ là tham khảo. Hãy lấy số thật của bạn sau 5–10 video đầu làm chuẩn.

## 4H. Lịch 90 ngày
| Giai đoạn | Việc chính |
|---|---|
| Ngày 1–7 | Tạo 7 nhân vật (A→B), 8 BG, 10 prop, 12 icon, chọn voice, chọn nhạc/SFX, làm avatar/banner |
| Ngày 8–14 | Làm **pilot** (ví dụ mục 13 của Phần 1), đăng, đo số liệu |
| Ngày 15–45 | 3 Short/tuần theo 4A, điều chỉnh Hook/Payoff theo 4G |
| Ngày 46–75 | Thêm 1 video dài/tuần (3 tình huống ghép), bắt đầu playlist theo series 4B |
| Ngày 76–90 | Tổng kết, giữ series hiệu quả, bỏ series kém, cập nhật bible |

## 4I. Nhận diện kênh (còn thiếu trong bản gốc)
- **Tên kênh:** NovaTech English. Kiểm tra trùng tên trên YouTube trước khi chốt.
- **Avatar:** nhân vật Mai hoặc nhóm 3 người, nền trắng, nét 4px.
- **Banner:** khẩu hiệu 1 dòng (ví dụ: "English you can use in tomorrow's stand-up"), 3 nhân vật chính.
- **Font:** 1 font sans-serif đậm cho chữ trên màn hình, giữ cố định toàn kênh.
- **Mô tả kênh:** 2–3 dòng nêu đối tượng, lịch đăng, loạt video.
- **Playlist:** theo 5 series ở 4B.

## 4J. Kiểm soát chất lượng tiếng Anh (quan trọng)
AI có thể viết câu đúng ngữ pháp nhưng chưa tự nhiên. Trước khi thu voice:
1. Đọc to từng câu: người bản ngữ trong ngành IT có nói thế không?
2. Kiểm tra thuật ngữ (staging, rollback, PR, root cause...) dùng đúng ngữ cảnh.
3. Nếu có thể, nhờ một người có tiếng Anh tốt hoặc người bản ngữ duyệt 5 video đầu, sau đó chỉ rà soát ngẫu nhiên.
4. Ghi lại các câu đã duyệt vào sheet "Approved Phrases" để dùng lại.

## 4K. Rủi ro chính sách và bản quyền (cần xác nhận lại theo quy định hiện hành)
- **Nội dung lặp lại, sản xuất hàng loạt:** YouTube có chính sách về nội dung "inauthentic/mass-produced" khi bật kiếm tiền. Mỗi video cần kịch bản, tình huống và giá trị giảng dạy riêng; không chỉ đổi vài chữ trong cùng một khuôn. Hãy đọc chính sách YPP mới nhất trên YouTube Help.
- **Công bố nội dung AI:** YouTube yêu cầu khai báo nội dung bị thay đổi/tổng hợp trông giống thật. Video hoạt hình stick figure thường khác loại này, nhưng hãy kiểm tra form khi tải lên và khai báo nếu được hỏi.
- **Nhạc/SFX:** chỉ dùng nguồn royalty-free (ví dụ YouTube Audio Library hoặc nguồn có giấy phép rõ ràng), lưu giấy phép vào `07_Music`.
- **Ảnh/giọng AI:** xem điều khoản thương mại của từng công cụ (Midjourney, ElevenLabs, v.v.) theo gói bạn đăng ký.
- **Thương hiệu:** không dùng logo/tên thật của công ty (Jira, Slack...) theo cách gây hiểu lầm; prop chỉ mang tính minh họa chung.

## 4L. Mẫu bảng kịch bản (Google Sheets / Excel)
Cột: `# | Thời gian | Nhân vật | Biểu cảm | Pose | BG | Lời thoại | Chữ hiển thị | Icon/Prop | Voice file | SFX | Ghi chú kỹ thuật | Trạng thái (Chưa/Đang/Xong)`
Mỗi video 1 tab; đặt tên tab = mã video (`NT-001`).

## 4M. Còn có thể bổ sung sau này
- Mẫu kịch bản video dài (5–8 phút) chi tiết kèm bài tập "pause và nói thử".
- Bộ nhân vật phụ (khách hàng, CEO, HR) khi kênh đã ổn định.
- Phiên bản Shorts tiếng Việt song ngữ để thử tăng người xem.
- Prompt đo hiệu quả: dán số liệu YouTube Studio vào AI để nhận đề xuất chỉnh Hook/Payoff.
