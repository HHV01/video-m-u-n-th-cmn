# NovaTech English

Đọc AGENTS.md gốc và AGENTS.md của niche. Các prompt Master Bible được giữ
nguyên trong bible/ và docs/operations.md.

## Vấn đề phát hiện

- Giới hạn hai bối cảnh cần xác nhận cách tính BG-08 bắt buộc.
- Một số prompt thumbnail yêu cầu mô hình ảnh thêm chữ, hướng dựng yêu cầu
  chữ riêng. Giữ nguyên prompt gốc để chủ repo chốt.
- Template để characters trống vì C1–C7 hiện là mã trong Bible, chưa có
  hồ sơ nhân vật YAML và PNG đã duyệt để pipeline tự nạp.
- Render cũ dùng ảnh đầy cảnh và chuyển động chuẩn bị trước. Chưa có
  compositor cho PNG trong suốt, lớp chữ canh theo thoại và nhiều giọng.
  Nên thêm compositor theo shot ID ở đợt sau, sau khi khóa asset.
- TODO(owner) chọn giọng, URL Flow, font, nhạc và thông số từ video tham chiếu.
