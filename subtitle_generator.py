import whisper
import srt
import datetime

# Load Whisper model
model = whisper.load_model("medium")  # try 'small' or 'large' as needed

# Transcribe audio
result = model.transcribe("your_audio.mp3", verbose=True)

# Convert segments to SRT subtitles
subs = []
for i, seg in enumerate(result['segments']):
    subs.append(srt.Subtitle(
        index=i + 1,
        start=datetime.timedelta(seconds=seg['start']),
        end=datetime.timedelta(seconds=seg['end']),
        content=seg['text'].strip()
    ))

# Save as .srt file
with open("output.srt", "w", encoding="utf-8") as f:
    f.write(srt.compose(subs))

print("✅ Subtitles saved as output.srt")
