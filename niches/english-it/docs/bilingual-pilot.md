# NT-001 · Đoạn thử song ngữ 06–08

Từ gốc repo chạy `python niches/english-it/tools/build_bilingual_audio.py <thư mục tập> <thư mục môi trường Kokoro>`. Đầu vào là kich-ban/bilingual-voice.csv. Nhóm segment theo lang, dùng lại infer_characters cho VieNeu tiếng Việt. Worker Kokoro dùng Python trong môi trường riêng, model ONNX và voicepack đã tải cục bộ. Kokoro af_heart dùng en-US và speed=0.9 trực tiếp khi tổng hợp. FFmpeg ghép theo thứ tự CSV, chuẩn hóa 48 kHz mono và chèn 0,2 giây giữa hai segment cùng shot. Công cụ từ chối thư mục đầu ra đã tồn tại.

Kokoro model và voicepack chính thức được công bố theo [Apache 2.0](https://huggingface.co/hexgrad/Kokoro-82M). [Wrapper kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) dùng MIT. Chưa đối chiếu điều khoản riêng cho bản ONNX đã chuyển đổi và gói voice đã đóng lại.

[Faster Whisper](https://github.com/SYSTRAN/faster-whisper#word-level-timestamps) có word_timestamps=True. Chạy riêng trên WAV segment tiếng Anh và cộng offset từ các segment đầu shot. Chưa chạy trên máy này vì môi trường repo thiếu faster_whisper. Renderer hiện nhận keyframe theo giây. Chưa tự chuyển word timestamps sang highlight. Bản nhỏ nhất là đối chiếu mốc X/Y/Z trên waveform hoặc ASR, rồi nhập ba mốc vào keyframe hold của lớp khung.

Giữ render.require_object_motion=true ở cả A và B. Pose P06 giữ nguyên. Bản A dùng căn hiện tại kèm chuyển động đối tượng. Bản B dùng highlight theo lời và các lớp khung/thẻ có chuyển động riêng. Zoom và lia toàn khung không tính. Chỉ dựng sau khi đủ asset đã kiểm nội dung, alpha và kích thước theo bố cục 9:16. Nền cần đủ vùng phủ sau crop. Sprite và icon kiểm theo kích thước hiển thị, giữ tỉ lệ gốc và kiểm cắt mép.
