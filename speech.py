import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# List all available voices
voices = engine.getProperty('voices')
print("Available voices:")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} - {voice.languages} - {voice.id}")

# Choose a specific voice by index (change this number after checking your options)
engine.setProperty('voice', voices[0].id)  # You can change 1 to the desired index

# Set speech rate for natural fluency
engine.setProperty('rate', 150)

# LinkedIn pitch script
script = "Real image"

# Save the speech to an MP3 file
engine.save_to_file(script, 'real.mp3')
engine.runAndWait()

print("✅ Audio saved as ai_vs_real_linkedin_pitch_voice_changed_new.mp3")
