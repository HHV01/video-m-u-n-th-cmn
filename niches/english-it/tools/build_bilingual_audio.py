"""Build the local bilingual NT-001 audition for shots 06–08."""
import argparse
import csv
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]


def synthesize(language, manifest, model_dir):
    rows = json.loads(manifest.read_text(encoding="utf-8"))
    if language == "en":
        import soundfile as sf
        from kokoro_onnx import Kokoro

        engine = Kokoro(str(model_dir / "model_quantized.onnx"), str(model_dir / "voices-alt.bin"))
        for row in rows:
            audio, rate = engine.create(row["text"], voice="af_heart", speed=row["tempo"], lang="en-us")
            sf.write(row["output"], audio, rate, subtype="PCM_16")
    else:
        sys.path.insert(0, str(ROOT / "src"))
        from pipeline.s2_voice import infer_characters
        from vieneu import Vieneu

        engine = Vieneu(mode="v3turbo")
        clips = infer_characters(engine, [
            {**row, "speaker": "Narrator", "voice": "Hải Đăng"} for row in rows
        ])
        for row, clip in zip(rows, clips):
            engine.save(clip, row["output"])


def build(project, model_dir):
    with (project / "kich-ban" / "bilingual-voice.csv").open(encoding="utf-8-sig", newline="") as stream:
        rows = [row for row in csv.DictReader(stream) if row["shot"] in {"06", "07", "08"}]
    expected = [("06", "vi"), ("06", "en"), ("07", "vi"), ("08", "en"), ("08", "vi")]
    if [(r["shot"], r["lang"]) for r in rows] != expected:
        raise ValueError("Unexpected NT-001 pilot segment order.")
    python_en = model_dir / ".venv/Scripts/python.exe"
    for required in (python_en, model_dir / "model_quantized.onnx", model_dir / "voices-alt.bin"):
        if not required.is_file():
            raise FileNotFoundError(required)
    output = (project / "video" / "voice-bilingual-06-08").resolve()
    output.mkdir()
    groups = {"vi": [], "en": []}
    for i, row in enumerate(rows, 1):
        row["tempo"] = float(row["tempo"])
        if row["tempo"] != (0.9 if row["lang"] == "en" else 1.0):
            raise ValueError("Expected approved pilot tempos.")
        row["output"] = str(output / f"segment-{i:02}-{row['lang']}.wav")
        groups[row["lang"]].append(row)
    env = {**os.environ, "HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1"}
    for lang, batch in groups.items():
        manifest = output / f"{lang}-segments.json"
        manifest.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding="utf-8")
        interpreter = python_en if lang == "en" else sys.executable
        subprocess.run([str(interpreter), "-B", str(Path(__file__).resolve()), str(project),
                        str(model_dir), "--worker", lang, str(manifest)], check=True, env=env)
    results = []
    for shot, target in [("06", 8), ("07", 3), ("08", 10)]:
        parts = [r["output"] for r in rows if r["shot"] == shot]
        command = ["ffmpeg", "-v", "error", "-n"]
        for path in parts:
            command.extend(["-i", path])
        filters = [
            f"[{i}:a]aresample=48000,aformat=sample_fmts=s16:channel_layouts=mono"
            + (",apad=pad_dur=0.2" if i < len(parts) - 1 else "")
            + f"[a{i}]" for i in range(len(parts))
        ]
        labels = "".join(f"[a{i}]" for i in range(len(parts)))
        graph = ";".join(filters + [f"{labels}concat=n={len(parts)}:v=0:a=1[out]"])
        path = output / f"Shot{shot}.wav"
        subprocess.run(command + ["-filter_complex", graph, "-map", "[out]", "-c:a", "pcm_s16le", str(path)], check=True)
        duration = float(subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(path)], text=True))
        results.append({"shot": shot, "target_seconds": target, "duration_seconds": duration,
                        "suggested_seconds": max(target, duration), "file": path.name})
    (output / "timing.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("model_dir", type=Path)
    parser.add_argument("--worker", nargs=2, metavar=("LANG", "MANIFEST"))
    args = parser.parse_args()
    if args.worker:
        synthesize(args.worker[0], Path(args.worker[1]), args.model_dir)
    else:
        build(args.project, args.model_dir)


if __name__ == "__main__":
    main()
