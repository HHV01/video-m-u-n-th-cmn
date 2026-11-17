"""Kiểm tra bước voice bằng VieNeu giả (không tải model thật)."""
import json, shutil, sys, types, unittest, wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pipeline import s2_voice, s3_scenes
from pipeline.common import PROJECTS, Project, audio_duration


class FakeVieneu:
    """Giả lập API trong README của VieNeu: infer_batch(texts, voice=) -> list[np.float32], save(audio, path)."""
    def __init__(self, **kw): self.kw = kw
    def add_voice(self, name, path): self.voice_added = (name, path)
    def list_preset_voices(self): return [("Mai Anh", "Mai Anh"), ("⭐ Hải Đăng", "Hải Đăng")]
    def infer_batch(self, texts, voice=None):
        return [np.sin(np.linspace(0, 200, int(48000 * (0.05 * len(t))))).astype(np.float32) for t in texts]
    def save(self, audio, path):
        with wave.open(path, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(48000)
            w.writeframes((audio * 32767).astype("<i2").tobytes())


class VieneuStep(unittest.TestCase):
    def setUp(self):
        sys.modules["vieneu"] = types.SimpleNamespace(Vieneu=FakeVieneu)
        self.d = PROJECTS / "_t_vieneu"
        shutil.rmtree(self.d, ignore_errors=True)
        shutil.copytree(PROJECTS / "_template", self.d)
        (self.d / "script.txt").write_text(
            "Đây là câu thứ nhất của kịch bản. Câu thứ hai dài hơn một chút, có dấu phẩy. Câu cuối cùng?", encoding="utf-8")
        self.p = Project("_t_vieneu")
        self.p.settings["review"]["enabled"] = False  # unit tests isolate the voice engine; review gate tested separately

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)
        sys.modules.pop("vieneu", None)

    def test_voice_and_timestamps_are_consistent(self):
        s2_voice.run(self.p)
        words = json.loads(self.p.words.read_text(encoding="utf-8"))
        self.assertEqual(" ".join(w["w"] for w in words).split(), self.p.script.read_text(encoding="utf-8").split())
        self.assertTrue(all(a["end"] <= b["start"] + 1e-6 for a, b in zip(words, words[1:])))   # tăng dần
        timing = json.loads((self.p.voice.parent/'voice.timing.json').read_text(encoding='utf-8'))
        self.assertEqual(self.p.voice.parent, self.p.dir/'video')
        self.assertFalse((self.p.dir/'voice.wav').exists())
        self.assertEqual(timing['timing_kind'], 'sentence_boundaries_word_interpolation')
        self.assertEqual(timing['segments'][-1]['word_end_index'], len(words))
        self.assertNotIn('measured', timing['timing_kind'])
        total = audio_duration(self.p.voice)
        self.assertAlmostEqual(words[-1]["end"], total, delta=0.05)                              # khớp độ dài file
        scenes = s3_scenes.make_scenes(self.p.script.read_text(encoding="utf-8"), words, total, 1, 4)
        self.assertEqual(scenes[-1]["end"], round(total, 3))

    def test_empty_character_map_preserves_legacy_wave(self):
        s2_voice.run(self.p)
        expected = self.p.voice.read_bytes()
        self.p.settings["voice"]["characters"] = {}
        s2_voice.run(self.p, force=True)
        self.assertEqual(self.p.voice.read_bytes(), expected)

    def test_csv_groups_voices_and_restores_audio_order(self):
        calls = []
        class Grouped(FakeVieneu):
            def infer_batch(self, texts, voice=None):
                calls.append((voice, texts))
                level = 0.1 if voice == "Mai Anh" else 0.2
                return [np.full(4800, level, dtype=np.float32) for _ in texts]

        sys.modules["vieneu"] = types.SimpleNamespace(Vieneu=Grouped)
        self.p.script.write_text("First. Second. Third.", encoding="utf-8")
        (self.p.dir / "kich-ban/voice.csv").write_text(
            "shot,speaker,utterance,start_target,end_target,voice_id,tempo\n"
            "02,Mai,First.,0,1,,\n03,Linh,Second.,1,2,Hải Đăng,1.0\n"
            "05,Mai,Third.,2,3,,\n", encoding="utf-8")
        cfg = self.p.settings["voice"]
        cfg["characters"] = {"Mai": {"voice": "Mai Anh"}, "Linh": {"voice": "Mai Anh"}}
        cfg["vieneu"]["gap_seconds"] = 0
        s2_voice.run(self.p)
        self.assertEqual(calls, [("Mai Anh", ["First.", "Third."]), ("Hải Đăng", ["Second."])])
        with wave.open(str(self.p.voice), "rb") as stream:
            samples = np.frombuffer(stream.readframes(stream.getnframes()), dtype="<i2")
        np.testing.assert_array_equal(samples[::4800], [3276, 6553, 3276])

    def test_missing_character_voice_and_invalid_tempo(self):
        cfg = self.p.settings["voice"]
        plan = {"segments": [{"speaker": "Linh", "text": "Ready."}]}
        cfg["characters"] = {"Mai": {"voice": "Mai Anh"}}
        with self.assertRaisesRegex(SystemExit, "Chưa chọn giọng cho nhân vật Linh"):
            s2_voice.character_segments(self.p, plan, None)
        cfg["characters"]["Linh"] = {"voice": "Hải Đăng", "tempo": 1.2}
        with self.assertRaisesRegex(SystemExit, "0.9 đến 1.1"):
            s2_voice.character_segments(self.p, plan, None)

    def test_narrator_ignores_character_overrides_and_slows_quotes(self):
        self.p.settings["voice"].update(mode="narrator", narrator={
            "voice": "Hải Đăng", "tempo": 1.0, "quote_tempo": .9},
            characters={"Mai": {"voice": "Mai Anh"}})
        self.p.script.write_text("First. Second.", encoding="utf-8")
        csv_text = ("shot,speaker,utterance,start_target,end_target,voice_id,tempo,type\n"
                    "02,Mai,First.,0,1,Mai Anh,1.1,\n"
                    "06,Mai,Second.,1,2,Mai Anh,1.0,QUOTE\n")
        clips = s2_voice.character_segments(self.p, None, csv_text)
        self.assertEqual([(s["voice"], s["tempo"]) for s in clips],
                         [("Hải Đăng", 1.0), ("Hải Đăng", .9)])

    def test_unknown_preset_fails_before_inference(self):
        with self.assertRaisesRegex(SystemExit, "không có giọng .*Linh"):
            s2_voice.infer_characters(FakeVieneu(),
                                     [{"speaker": "Linh", "voice": "Unknown", "text": "Ready."}])

    def test_generated_sentence_timing_survives_agent_handoff_gate(self):
        import hashlib
        from pipeline.timeline_review import inspect
        s2_voice.run(self.p)
        s3_scenes.run(self.p)
        scenes = self.p.load_scenes()
        def sha(path):
            with path.open('rb') as stream:
                return hashlib.file_digest(stream, 'sha256').hexdigest()
        manifest = {'executor': 'test fixture, not production approval',
                    'script_sha256': sha(self.p.script), 'voice_sha256': sha(self.p.voice),
                    'scenes_sha256': sha(self.p.scenes_file), 'beats': [
                        {'scene_id': scene['id'], 'anchor_text': scene['text'],
                         'visual_subject': 'test figure', 'visual_action': 'test action',
                         'at_seconds': scene['start'], 'visual_at_seconds': scene['start']}
                        for scene in scenes]}
        (self.p.dir/'storyboard-timing.json').write_text(json.dumps(manifest), encoding='utf-8')
        result = inspect(self.p)
        self.assertTrue(result['approved'], result['blockers'])
        self.assertIn('interpolated', result['evidence']['timing_precision'])

    def test_second_run_is_skipped(self):
        s2_voice.run(self.p)
        t = self.p.voice.stat().st_mtime_ns
        s2_voice.run(self.p)
        self.assertEqual(self.p.voice.stat().st_mtime_ns, t)

    def test_pick_voice_by_number_or_name(self):
        presets = [("Mai Anh", "Mai Anh"), ("⭐ Hải Đăng", "Hải Đăng")]
        self.assertEqual(s2_voice.pick_voice(presets, "2"), "Hải Đăng")
        self.assertEqual(s2_voice.pick_voice(presets, "hải đăng"), "Hải Đăng")
        self.assertEqual(s2_voice.pick_voice(presets, "Mai Anh"), "Mai Anh")
        self.assertIsNone(s2_voice.pick_voice(presets, "99"))
        self.assertIsNone(s2_voice.pick_voice(presets, ""))

    def test_missing_voice_asks_user_to_choose(self):
        self.assertEqual(s2_voice.choose_voice(FakeVieneu(), ask=lambda _: "2"), "Hải Đăng")
        with self.assertRaises(SystemExit) as e:
            s2_voice.choose_voice(FakeVieneu(), ask=lambda _: "")
        self.assertIn("Chưa chọn", str(e.exception))

    def test_wrong_sample_rate_is_caught(self):
        class BadSR(FakeVieneu):
            def save(self, audio, path):
                with wave.open(path, "wb") as w:
                    w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000)   # lưu sai sample rate
                    w.writeframes((audio * 32767).astype("<i2").tobytes())
        sys.modules["vieneu"] = types.SimpleNamespace(Vieneu=BadSR)
        with self.assertRaises(SystemExit):
            s2_voice.run(self.p)


    def test_multi_voice_uses_characters_and_csv_speaker(self):
        class RecordingVieneu(FakeVieneu):
            calls = []
            def infer_batch(self, texts, voice=None):
                RecordingVieneu.calls.append((list(texts), voice))
                return super().infer_batch(texts, voice=voice)
        RecordingVieneu.calls = []
        sys.modules["vieneu"] = types.SimpleNamespace(Vieneu=RecordingVieneu)
        d = PROJECTS / "_t_vieneu_mv"
        shutil.rmtree(d, ignore_errors=True)
        shutil.copytree(PROJECTS / "_template", d)
        (d / "script.txt").write_text("Cau mot. Cau hai.", encoding="utf-8")
        (d / "kich-ban").mkdir(exist_ok=True)
        (d / "kich-ban" / "voice.csv").write_text(
            "shot,start_target,end_target,speaker,direction,utterance,voice_id,tempo\n"
            "01,0,1,Linh,note,Cau mot.,,\n"
            "02,1,2,Minh,note,Cau hai.,,\n",
            encoding="utf-8")
        p = Project("_t_vieneu_mv")
        p.settings["review"]["enabled"] = False
        p.settings["voice"]["characters"] = {
            "Linh": {"voice": "Mai Anh", "tempo": 1.0},
            "Minh": {"voice": "Hải Đăng", "tempo": 1.0},
        }
        s2_voice.run(p)
        voices = [c[1] for c in RecordingVieneu.calls]
        self.assertIn("Mai Anh", voices)
        self.assertIn("Hải Đăng", voices)
        self.assertEqual(len(RecordingVieneu.calls), 2)
        shutil.rmtree(d, ignore_errors=True)
        sys.modules.pop("vieneu", None)

    def test_single_voice_backward_compatible(self):
        class RecordingVieneu(FakeVieneu):
            calls = []
            def infer_batch(self, texts, voice=None):
                RecordingVieneu.calls.append((list(texts), voice))
                return super().infer_batch(texts, voice=voice)
        RecordingVieneu.calls = []
        sys.modules["vieneu"] = types.SimpleNamespace(Vieneu=RecordingVieneu)
        d = PROJECTS / "_t_vieneu_sv"
        shutil.rmtree(d, ignore_errors=True)
        shutil.copytree(PROJECTS / "_template", d)
        (d / "script.txt").write_text("Cau mot. Cau hai.", encoding="utf-8")
        p = Project("_t_vieneu_sv")
        p.settings["review"]["enabled"] = False
        s2_voice.run(p)
        voices = [c[1] for c in RecordingVieneu.calls]
        self.assertEqual(len(set(voices)), 1)
        self.assertEqual(voices[0], p.settings["voice"]["vieneu"]["voice"])
        shutil.rmtree(d, ignore_errors=True)
        sys.modules.pop("vieneu", None)

if __name__ == "__main__":
    unittest.main()
