# Demo nét vẽ trong Studio

Trong bản sao Script, chạy `python run.py studio --port 8788`, mở
http://127.0.0.1:8788 rồi chọn **Demo nét vẽ**. Bấm vào nhân vật để xem
động tác chào và di chuột để tác động lên khăn.

Demo dùng walker và ba mô-đun ink, gait, motion từ
https://github.com/JDhruv14/line-art-animation (commit c43d698).
Các tệp JavaScript được tạo bằng Node stripTypeScriptTypes, với đường dẫn
import chuyển sang tệp .js cùng thư mục. Giấy phép MIT nằm cạnh mã demo.
Studio phục vụ các tệp trực tiếp nên không cần Node để chạy demo.

Phạm vi thử nghiệm là xem SVG tương tác trong Studio. Chưa có bước xuất
video hay kết nối demo với timeline và dữ liệu cảnh của từng tập.
