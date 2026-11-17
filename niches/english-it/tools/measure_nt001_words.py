import json,subprocess,re,hashlib
from pathlib import Path
from faster_whisper import WhisperModel
import numpy as np
p=Path("niches/english-it/projects/tap-01-daily-blocker/video/voice-bilingual-06-08")
m=WhisperModel(r"C:\Users\VNTT\Documents\Codex\models\faster-whisper-tiny.en",device="cpu",compute_type="int8",local_files_only=True)
def duration(path):
 return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",str(path)],text=True))
records=[]
for shot,name,targets,offset in [("06","segment-02-en.wav",{"x","y","z"},duration(p/"segment-01-vi.wav")+.2),("08","segment-04-en.wav",{"blocked","because","need"},0)]:
 path=p/name
 pcm=subprocess.check_output(["ffmpeg","-v","error","-i",str(path),"-ac","1","-ar","16000","-f","f32le","-"])
 segs,_=m.transcribe(np.frombuffer(pcm,dtype="<f4"),language="en",word_timestamps=True,condition_on_previous_text=False)
 words=[dict(word=w.word.strip(),start=w.start,end=w.end) for seg in segs for w in seg.words]
 seconds=duration(path)
 records.append(dict(shot=shot,file=name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),ffprobe_seconds=seconds,estimated_last_word_end=words[-1]["end"],tail_seconds=round(seconds-words[-1]["end"],6),shot_offset_seconds=offset,words=words,anchors=[w for w in words if re.sub(r"[^a-z]","",w["word"].lower()) in targets]))
(p/"word-timing-tiny-en.json").write_text(json.dumps(records,indent=2)+"\n",encoding="utf-8")
for record in records:
 print({k:v for k,v in record.items() if k!="words"})
 print(" ".join(w["word"] for w in record["words"]))
