from pydub import AudioSegment
from pydub.playback import play

def play_audio(file_path):
    sound = AudioSegment.from_file(file_path)
    play(sound)

# Usage
play_audio("output1.mp3")
