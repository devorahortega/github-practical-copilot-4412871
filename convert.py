import os

def get_audio_files():
    audio_dir = 'audio'
    audio_files = []
    for file in os.listdir(audio_dir):
        if file.endswith('.mp3'):
            audio_files.append(os.path.join(audio_dir, file))
    return audio_files

print(get_audio_files())