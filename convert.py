import os
import eyed3
import yaml

def get_audio_titles_and_comments():
    audio_dir = 'audio'
    audio_data = []
    for file in os.listdir(audio_dir):
        if file.endswith('.mp3'):
            file_path = os.path.join(audio_dir, file)
            audio = eyed3.load(file_path)
            title = audio.tag.title if audio and audio.tag else None
            comments = None
            duration = audio.info.time_secs if audio and audio.info else None
            if audio and audio.tag and audio.tag.comments:
                comments = audio.tag.comments[0].text
            size = os.path.getsize(file_path)
            audio_data.append({
                'file': file_path,
                'title': title,
                'comments': comments,
                'duration': duration,
                'size': size,
            })
    return audio_data

def print_audio_data(audio_data):
    for audio in audio_data:
        print(f"Title: {audio['title']}")
        print(f"File: {audio['file']}")
        print(f"Duration: {audio['duration']} seconds")
        print(f"Size: {audio['size']:,} bytes")
        print('-' * 40)

audio_data = get_audio_titles_and_comments()
print_audio_data(audio_data)

audio_info = get_audio_titles_and_comments()

print(yaml.dump(audio_info, allow_unicode=True, sort_keys=False))