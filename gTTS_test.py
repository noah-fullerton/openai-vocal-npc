from gtts import gTTS

message = """What are some engaging story hooks for a mysterious village in a fantasy setting?"""

tts = gTTS(message)
tts.save('input.mp3')