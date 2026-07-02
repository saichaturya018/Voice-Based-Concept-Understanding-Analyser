from backend.speech_to_text import transcribe_audio

text = transcribe_audio("data/sample_audio.wav")
print(text)