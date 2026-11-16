# Cấu hình nhiều niche

Tập mặc định tiếp tục dùng projects/. Tập có niche dùng niches/<id>/projects/.
Mỗi tập giữ project.yaml, README.md, hinh/, video/ và kich-ban/.

## Tạo niche

1. Tạo niches/<id>/niche.yaml và khai báo niche_id trùng tên thư mục.
   ID chỉ có chữ thường ASCII, số và gạch nối.
2. Tạo AGENTS.md của niche. AGENTS.md gốc vẫn có hiệu lực.
3. Thêm bible/ và templates/ nếu cần. Template mặc định là projects/_template/.
4. Chạy công cụ kiểm tra cục bộ.

```powershell
python run.py niches list
python run.py doctor --niche english-it
python run.py new tap-01-daily-blocker --niche english-it
python run.py doctor tap-01-daily-blocker --niche english-it --json
```

Thứ tự chọn là --niche, biến môi trường NICHE, rồi niche_id trong project.yaml.
Nếu không chọn rõ và tên tập tồn tại trong projects/, hồ sơ tại đó được xét trước.
Nếu chưa có tập mặc định, CLI tìm tập cùng tên khai báo niche_id trong cây niches/.
Nếu trùng tên giữa nhiều niche, dùng --niche. Trường niche cũ vẫn dành cho nội dung.
dedupe và motion nhận đường dẫn trực tiếp như trước; --niche kiểm tra ID ở hai lệnh này.

Cấu hình áp theo thứ tự config/settings.yaml, config/channel-direction.yaml,
niche.yaml, rồi project.yaml.settings. Bản đồ hợp nhất đệ quy, danh sách thay
toàn bộ. Với tập mặc định, chỉ settings.yaml và project.yaml.settings được gộp
như trước. Playwright dùng .flow-profile riêng dưới mỗi niche. flow_gen độc lập
thêm ID niche vào đường dẫn out và profile, kể cả khi chỉ định thư mục gốc riêng.
Ví dụ mặc định: out/english-it/state.json và ~/.flow_gen_profile/english-it.
Khi dùng CDP, phiên Chrome do người vận hành mở cần dùng đúng hồ sơ riêng.

Tệp phát sinh trong projects/ của từng niche bị Git loại trừ. Commit cấu hình,
Bible và template. Không dùng doctor --fix trong kiểm tra offline.

## Để sau

- Bộ chọn niche và quản lý tập trong Studio.
- Di chuyển các tập khoa học hiện có.
- Kiểm thử Google Flow thật, chọn URL dự án, giọng tiếng Anh và thông số
  hình/tiếng từ tài liệu tham chiếu.
- Bộ dựng ghép PNG trong suốt, nền, chữ theo lời và nhiều giọng cho NovaTech.
