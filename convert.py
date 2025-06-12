import os

# Create a function that reads audio files in the mp3 format
# from the audio directory and returns and lists them.
def get_audio_files():
    audio_dir = 'audio'
    audio_files = []
    for file in os.listdir(audio_dir):
        if file.endswith('.mp3'):
            audio_files.append(os.path.join(file))
    return audio_files

print(get_audio_files())