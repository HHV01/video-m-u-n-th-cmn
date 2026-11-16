# Giọng và bộ dựng NT-001

## Ưu tiên phần giọng có sẵn

Pipeline đã có VieNeu local và đường nhận file voice WAV/MP3 có sẵn. Cấu hình mặc định đang dùng tiếng Việt, nên chưa xác nhận được chất lượng câu tiếng Anh hoặc ba giọng phân biệt cho Linh, Minh, Mai. Bước đầu là kiểm các giọng hiện có với một câu mẫu. Nếu dùng bản thu hoặc file giọng có sẵn, ghép vào WAV chính và dùng nhánh nhận voice thủ công. Khi đo timestamp cho tập tiếng Anh, cấu hình Whisper theo tiếng Anh và đối chiếu tên riêng như API, DevOps.

## Hai phương án dự phòng nếu giọng hiện có không đạt

- **Piper** chạy local, không tính phí mỗi lượt. Engine GPL-3.0. Kiểm MODEL_CARD và điều khoản thương mại của từng voice model trước khi chọn ba giọng. Gán một model cho Linh, Minh, Mai và xuất WAV riêng từng dòng. [Điều khoản thương mại của Piper](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/COMMERCIAL_USE.md)
- **ElevenLabs** chạy dịch vụ. Gói trả phí có giấy phép thương mại với điều kiện áp dụng của dịch vụ. Gán ba voice ID cố định, gửi từng lời độc lập sau khi được phép và lưu WAV cùng shot ID. [Tài liệu TTS](https://elevenlabs.io/docs/overview/capabilities/text-to-speech) · [Các gói](https://elevenlabs.io/pricing)

Chỉ cân nhắc Piper nếu cần phương án mới và tìm được ba model có giấy phép phù hợp và giọng đủ phân biệt. Cả hai phương án dùng cùng voice CSV. Chuẩn hóa PCM, sample rate và mức âm; chèn khoảng nghỉ theo nhịp, ghép WAV chính, đo lại onset câu/cụm rồi khóa timeline. Nếu thoại dài hơn nhịp dự kiến, chỉnh shot hoặc thu lại; tránh tăng tốc để bù lệch.

## Dựng ghép lớp

Mỗi shot dùng nền cố định, PNG alpha nhân vật/pose, lớp tay hoặc đạo cụ độc lập khi cần, icon và chữ dựng sau. Mọi mốc chữ, icon và SFX gắn shot ID và cue đo từ giọng. Đặt SFX dưới lời, nhạc outro riêng, kiểm vùng an toàn trên màn hình dọc.

- **Tận dụng:** nhánh motion_plan trong s7_render.py và layer_motion.py đã hỗ trợ PNG alpha, icon dưới dạng lớp ảnh, lớp chữ và keyframe. Dùng trực tiếp các lớp này cho shot 08. Giữ tính số frame, FFmpeg, ghép clip, SRT và ghép audio từ renderer hiện tại.
- **Viết mới:** với bản thử, nhập cue trực tiếp vào motion plan và trộn voice/SFX vào WAV bằng FFmpeg trước khi ghép video. Chỉ cân nhắc viết adapter khi cần tự động hóa nhiều tập. Độ khó vừa cho hai bố cục cố định. Tăng lên nếu cần lip-sync chi tiết hoặc nhiều pose quay đầu.
- **MVP:** 11 shot dọc, 2 nền, 3 nhân vật với pose tối thiểu, 2 icon, một font và cue nhập tay sau khi có WAV thật. Thử riêng shot 08 để kiểm alpha, vị trí khớp và cue, sau đó dựng đủ 11 shot theo cùng dữ liệu. Chưa triển khai adapter.
- **Chuyển động bắt buộc:** giữ render.require_object_motion=true. Mỗi shot có motion_plan hợp lệ với lớp đối tượng thực sự di chuyển, hoặc clip hành động phủ đủ thời lượng. Kiểm từng chuyển động chỉ định trong bảng shot, kể cả outro. Zoom/lia toàn khung, đổi phụ đề hoặc ảnh tĩnh không đáp ứng. Chặn shot thiếu asset/keyframe hay clip quá ngắn. Chạy cổng timing và kiểm hình–giọng trên video thật trước khi duyệt.
