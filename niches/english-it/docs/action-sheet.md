# Kiểm tra trước khi dựng NT-001

Action sheet lấy nội dung từ bảng shot và voice CSV. Mã pose là ánh xạ kỹ thuật sang P01–P08. Shot 02 có đủ Linh, Minh, Mai trong hồ sơ, nhưng biểu cảm của Linh và Minh chưa chỉ định, giữ unspecified. Ô vật cầm rỗng vì hồ sơ không xác nhận có vật cầm. Công cụ kiểm người nói theo CSV và dàn nhân vật, cũng như danh sách vật/icon phải rời giữa hai shot. Kiểm tra này không nhìn được nhân vật vẽ sai, mặt quay sai, đạo cụ dính trong PNG hay nhép miệng lệch. Cần duyệt hình thật trước khi dựng.

Chạy từ gốc repo: `python niches/english-it/tools/check_action_sheet.py niches/english-it/projects/tap-01-daily-blocker`.

Quy ước tập mẫu dưới hinh/assets: backgrounds/BG-02-A.png, characters/C7-P06-focused.png, props/formula-card.png, icons/I-01.png. Công cụ in tên đầy đủ theo shot. Nền có thể đặc. Nhân vật, đạo cụ và icon phải có cả vùng trong suốt và vùng nhìn thấy. Vật/nhãn dựng riêng có thể cung cấp dưới dạng PNG alpha theo cùng quy ước. Giữ PNG nhân vật sạch đạo cụ rời.

## Shot 06–08

Chỉ sau khi chốt giọng và có asset, so sánh riêng mốc nháp 22–44 giây (22 giây) bằng cùng giọng, bố cục và nội dung. Bản A dùng cách căn hiện tại với chuyển động đối tượng hợp lệ. Bản B căn theo lời đo được, đổi pose theo shot, Mai giữ P06 ở shot 06 và khung vuông X/Y/Z sáng lần lượt lúc đọc tên từng chữ. Shot 07 giữ thẻ mờ, shot 08 nhấn ba cụm thoại tương ứng. Chờ duyệt đoạn này trước khi mở rộng toàn bộ 11 shot.

Renderer đã có lớp ảnh PNG, lớp chữ, opacity và keyframe hold, đủ để bật/tắt ba lớp PNG khung vuông tại các mốc nhập tay. Chưa có bước tự ánh xạ mốc từ voice sang keyframe. Bản thử dùng mốc đã đối chiếu audio nhập trực tiếp; chỉ cần viết adapter nếu muốn tự động hóa. Không rig tay. Bố trí khung ở vùng Mai chỉ và dùng highlight dẫn mắt.

Giữ require_object_motion. Renderer nhận motion_plan hoặc clip hành động có đủ thời lượng. Motion plan hỗ trợ dịch vị trí, đổi kích thước/tỉ lệ và opacity từng lớp ảnh; có rig stick_character nhưng không dùng đợt này. Tách các pose vào các lớp ảnh để thay sprite khi cần. Gate kỹ thuật hiện kiểm sự hiện diện plan/clip và tính hợp lệ cấu trúc, không tự chứng minh có chuyển động thực. Bản dựng cần chuyển động đối tượng đọc được trong từng shot, ví dụ thẻ, bút, icon hoặc lớp nhân vật dịch/chuyển pose trong shot. Đổi pose ở điểm cắt, zoom/lia toàn khung hoặc chữ hiện đơn thuần không đủ. Highlight có thể dùng khung riêng, kết hợp dịch chuyển lớp khung giữa các ô để có chuyển động đối tượng rõ ràng.

Giữ tempo trong 0.9–1.1. Thoại vượt mốc thì kéo shot hoặc chia ở chỗ ngắt tự nhiên, không tăng tốc đoạn cuối. Chưa tạo ảnh, giọng hay video.
