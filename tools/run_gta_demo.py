"""Run the upstream GTA clipping tools using the existing local Whisper model."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import wave

import numpy as np
from faster_whisper import WhisperModel

root = Path.cwd()
episode = root / "projects/tap-02-gta-clip-demo"
os.environ["CLIP_DESK_HOME"] = str(episode / "video")
sys.path.insert(0, str(root / "tools/gtavi-source/scripts"))
import moments
import common

def local_transcribe(wav, directory):
    target = directory / "transcript.json"
    if target.is_file():
        return common.load_json(target)
    with wave.open(str(wav)) as stream:
        audio = np.frombuffer(stream.readframes(stream.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    model = WhisperModel("C:/Users/VNTT/Documents/Codex/models/faster-whisper-tiny.en",
                         device="cpu", compute_type="int8", local_files_only=True)
    segments, _ = model.transcribe(audio, language="en", word_timestamps=True, condition_on_previous_text=False)
    words = [{"w": word.word.strip(), "s": round(float(word.start), 2),
              "e": round(float(word.end), 2)} for segment in segments for word in segment.words or []]
    common.save_json(target, words)
    return words

source = episode / "video/source.mp4"
moments.transcribe = local_transcribe
sys.argv = ["moments.py", str(source), "--top", "3", "--min", "20", "--max", "30"]
moments.main()
job = common.job_dir(str(source))
candidate = common.load_json(job / "candidates.json")
best = max(candidate["candidates"], key=lambda item: item["score"])
print("SELECTED", best, flush=True)
# Relative paths keep FFmpeg's ASS filter paths portable on Windows.
relative = job.relative_to(root).as_posix()
subprocess.run([sys.executable, "tools/gtavi-source/scripts/cut.py", relative,
                "--pick", str(best["n"]), "--layout", "blur", "--hook",
                "GTA VI | JASON & LUCIA", "--captions", "word"], check=True)
clip = job / "edits" / f"clip_{best['n']}.mp4"
result = episode / "video/gta-clip-demo.mp4"
shutil.copy2(clip, result)
subprocess.run([sys.executable, "tools/gtavi-source/scripts/check.py", str(result)], check=True)
metadata = {"source_url": "https://www.youtube.com/watch?v=VQRLujxTm3c",
            "upstream_commit": (root / "tools/gtavi-source/UPSTREAM_COMMIT").read_text().strip(),
            "selected_candidate": best, "output": str(result),
            "scope": "Local technical preview; captions are unreviewed ASR; rights for publication not verified."}
common.save_json(episode / "kich-ban/source-and-result.json", metadata)
print("RESULT", result, flush=True)
