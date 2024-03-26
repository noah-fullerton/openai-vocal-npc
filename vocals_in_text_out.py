from pathlib import Path
from openai import OpenAI
import os

# read variables from .env file
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# create OpenAI client with key from .env
client = OpenAI(
  api_key=key
)

def transcribe_input_audio(input_filepath: str):
    audio_file= open(input_filepath, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    print(transcript)
    return str(transcript)

def create_text_response(text_input: str):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text_input}
        ])
    text_to_be_spoken = response.choices[0].message.content
    print(text_to_be_spoken)
    return (text_to_be_spoken)

def create_audio_response(transcript: str):
    speech_file_path = Path(__file__).parent / "output.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=transcript
    )
    response.write_to_file(speech_file_path)


def main():
    text = transcribe_input_audio("input.mp3")
    response = create_text_response(text)
    create_audio_response(response)
    


if __name__ == "__main__":
    main()