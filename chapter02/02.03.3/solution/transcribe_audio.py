# Description: Transcribe an audio file to a text file using OpenAI Whisper.

import os
import ssl
import whisper

# Create an unverified SSL context
ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("base")
result = model.transcribe("./audio.mp3")
print(result["text"])
