# Thiết kế giọng theo nhân vật (chỉ thiết kế, chưa code)

Phạm vi: niche `english-it`, tập `tap-01-daily-blocker`. Mục tiêu là cho phép mỗi nhân vật có giọng/tốc độ riêng, đồng thời giữ tương thích ngược với cấu hình một giọng cho toàn bộ tập.

## a) CSV thoại và cấu hình `voice.characters`

### Cột hiện có trong `kich-ban/voice.csv`
Hiện tại các cột là:

`shot,start_target,end_target,speaker,direction,utterance`

- `speaker` đã tồn tại và chứa tên nhân vật (Mai, Linh, Minh). Đây là nguồn để ánh xạ giọng.
- `direction` là ghi chú biểu cảm/tốc độ cho người dựng, chưa phải tham số máy.
- `utterance` là câu tiếng Anh cần tổng hợp.

### Thay đổi CSV (tối thiểu)
Không bắt buộc thêm cột mới nếu `speaker` đã đủ. Nếu muốn rõ ràng hơn, thêm cột `voice_id` và `tempo`:

`shot,start_target,end_target,speaker,direction,utterance,voice_id,tempo`

- `voice_id`: mã giọng trong VieNeu (hoặc tên file WAV nếu dùng Phương án B).
- `tempo`: số thực 0.9–1.1; để trống = 1.0.

Quy tắc tương thích: nếu thiếu `voice_id`/`tempo`, lấy từ `voice.characters` hoặc `voice.vieneu.voice` và tốc độ 1.0.

### Cấu hình `voice.characters` trong `niche.yaml` hoặc `project.yaml`
Ví dụ:

```yaml
voice:
  provider: vieneu
  vieneu:
    mode: v3turbo
    voice: Hải Đăng          # fallback toàn cục
    gap_seconds: 0.3
  characters:
    Linh: { voice: "Ngọc Huyền", tempo: 1.0 }
    Mai:  { voice: "Trúc Ly",    tempo: 0.95 }
    Minh: { voice: "Thái Sơn",   tempo: 1.0 }
  whisper:
    model: small
    language: en
```

- Khóa nhân vật phải khớp tên trong CSV `speaker` (hoặc ánh xạ alias trong code).
- Nếu một nhân vật không có trong `characters`, dùng `voice.vieneu.voice`.
- `tempo` vẫn bị giới hạn 0.9–1.1 theo `apply_tempo`.

## b) Cách `s2_voice.py` chọn giọng theo segment (tương thích ngược)

Hiện tại `synth_vieneu`:
- đọc `sentences` từ plan hoặc `split_sentences(script)`,
- gọi `tts.infer_batch(sentences, voice=voice)` một lần cho một giọng,
- áp `apply_tempo` theo `segment.get('tempo', 1.0)`.

### Thay đổi đề xuất
1. Tạo danh sách `voices_for_segments` song song với `sentences`:
   - nếu có `plan['segments'][i]['voice']` thì dùng;
   - else nếu `voice.characters` có ánh xạ cho speaker của segment thì dùng;
   - else dùng `voice.vieneu.voice`.
2. Vì `infer_batch` của VieNeu nhận một `voice` cho cả batch, cần nhóm các câu cùng giọng:
   - gọi `infer_batch` riêng cho từng nhóm giọng,
   - ghép lại theo thứ tự segment ban đầu.
3. Giữ nguyên `word_timeline`, `save_sentence_timing`, ghép khoảng lặng `gap_seconds` và lưu `voice.wav`.
4. Nếu không có `voice.characters` và không có `voice` trong plan segment, hành vi cũ giữ nguyên: một giọng toàn bộ.

### Rủi ro
- Thứ tự câu phải được bảo toàn sau khi nhóm.
- Nếu một giọng không tồn tại, dừng với lỗi rõ ràng (không tự thay).
- Thời lượng tổng có thể thay đổi nhẹ do khác giọng; vẫn kiểm tra `abs(expected - actual) < 1.0`.

## c) Phương án B: nhập file thoại ngoài theo mã shot

Dùng khi giọng được tạo bằng công cụ khác (ElevenLabs, Piper, thu tay).

### Đặt tên file
- Quy ước: `<NhânVật>_<MaShot>.wav` hoặc `<MaShot>_<NhânVật>.wav`, ví dụ `Mai_Shot06.wav`, `Linh_Shot08.wav`.
- Đặt trong `video/voice-shots/` (hoặc thư mục cấu hình `voice.manual_shots_dir`).
- Chỉ chấp nhận WAV (PCM) để ghép đơn giản; MP3 cần chuyển trước.

### Đo thời lượng
- Dùng `ffprobe -show_entries format=duration` cho từng file.
- Ghi thời lượng vào `voice.timing.json` hoặc `voice.shots.json`.

### Cách dựng
- Sắp xếp theo `shot` trong `voice.csv`.
- Ghép các clip theo thứ tự, chèn khoảng lặng theo `gap_seconds` hoặc mốc `start_target`/`end_target`.
- Tạo `voice.wav` tổng và `voice.words.json`:
  - nếu có timestamp Whisper, chạy `transcribe()`;
  - nếu không, dùng thời lượng clip để nội suy từ theo ký tự (như hiện tại).
- Giữ `voice.source.json` để biết nguồn là file ngoài (hash từng clip).

### Ưu điểm
- Linh hoạt giọng, không phụ thuộc VieNeu.
- Nhược điểm: quản lý nhiều file, phải đo thời lượng, dễ lệch nhịp nếu clip quá dài/ngắn.

## d) Thay đổi nhỏ nhất và test cần thêm

### Phương án A (nhiều giọng VieNeu)
- Thay đổi nhỏ nhất:
  - thêm đọc `voice.characters` trong `synth_vieneu`,
  - thêm ánh xạ speaker->voice trong plan segment,
  - nhóm câu cùng giọng trước `infer_batch`.
- Độ khó: vừa.
- Test cần thêm:
  - `test_vieneu.py`: tổng hợp 2 giọng khác nhau, kiểm thứ tự clip và tổng thời lượng.
  - kiểm fallback khi không cấu hình `characters`.
  - kiểm lỗi khi voice không tồn tại.

### Phương án B (file ngoài)
- Thay đổi nhỏ nhất:
  - thêm nhánh `provider: manual-shots` hoặc cờ `voice.manual_shots_dir`,
  - đọc danh sách file, đo ffprobe, ghép clip.
- Độ khó: vừa-cao (xử lý file, timestamp).
- Test cần thêm:
  - ghép 2 clip, kiểm thời lượng tổng,
  - thiếu file -> lỗi rõ ràng,
  - timestamp nội suy khi không có Whisper.

### Test chung
- `test_scene_handoff.py`: giữ tương thích scene handoff.
- `test_script_review.py`: bản duyệt vẫn khớp sau khi đổi voice config.

## e) `voice.whisper.language: en` theo niche, không ảnh hưởng niche cũ

- Niche `english-it` đặt `voice.whisper.language: en` trong `niche.yaml` hoặc `project.yaml`.
- Niche mặc định không có `voice.whisper.language` override, vẫn dùng `vi` từ `config/settings.yaml`.
- Vì cấu hình gộp theo thứ tự `settings.yaml` -> `channel-direction.yaml` -> `niche.yaml` -> `project.yaml.settings`, niche override chỉ áp dụng cho niche đó.
- Khi chạy `transcribe()` (provider manual), đọc `project.settings["voice"]["whisper"]["language"]`, nên niche English dùng `en`, niche cũ dùng `vi`.
- Không cần sửa code nếu đã đọc từ settings; chỉ cần cấu hình.

## Ghi chú
- Chưa code cho đến khi chọn phương án (A hoặc B).
- Không cài engine mới, không tiêu credit trong thiết kế này.
