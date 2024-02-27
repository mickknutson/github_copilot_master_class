# Describe: Function to use openai whisper to write out the transcript of an audio file to a text file.
import os
from openai import OpenAI

client = OpenAI()

def transcribe_audio(audio_file, output_file):

        # Create .tmp directory if it does not exist
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    # Load the audio file
    audio = client.audio.from_file(audio_file)

    # Transcribe the audio using OpenAI Whisper
    response = openai.Whisper.transcribe(audio)

    # Write the transcript to the output file
    with open(output_file, 'w') as file:
        file.write(response['transcript'])

# Usage example
audio_file = './audio.mp3'
output_file = './tmp/transcript.txt'
transcribe_audio(audio_file, output_file)
