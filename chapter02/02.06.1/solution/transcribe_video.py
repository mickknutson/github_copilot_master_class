# Description: Transcribe an Youtube video to a text file using OpenAI Whisper.

import os
import ssl
from pytube import YouTube
import whisper


# Create .tmp directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create an unverified SSL context
ssl._create_default_https_context = ssl._create_unverified_context

# Download the YouTube video
video_url = "https://www.youtube.com/watch?v=gRTBRV2_S5Q"
video_file = "./tmp/video.mp4"

youtube = YouTube(video_url)
video = youtube.streams.get_highest_resolution()
video.download(filename=video_file)

# Transcribe the downloaded video using OpenAI Whisper
model = whisper.load_model("base")
result = model.transcribe(video_file)
print(result["text"])
