import os           # For interacting with the operating system (file paths, listing directories)
import eyed3        # For reading ID3 metadata from MP3 files
import yaml         # For writing data in YAML format

def get_audio_files():
    audio_dir = 'audio'  # The folder where your MP3 files are stored
    audio_files = []     # List to hold info about each audio file
    for file in os.listdir(audio_dir):  # Loop through all files in the audio directory
        if file.endswith('.mp3'):       # Only process files that end with .mp3
            file_path = os.path.join(audio_dir, file)  # Get the full path to the file
            audio = eyed3.load(file_path)              # Load the MP3 file and its metadata
            duration = audio.info.time_secs if audio and audio.info else None  # Get duration in seconds, if available
            size = os.path.getsize(file_path)          # Get the file size in bytes
            audio_files.append({
                'path': file_path,      # Full path to the audio file
                'filename': file,       # Just the file name
                'duration': duration,   # Duration of the audio in seconds
                'size': size            # File size in bytes
            })
    return audio_files  # Return the list of audio file info

audio_files = get_audio_files()  # Call the function to get the audio file info

# Write the list of audio file info to a YAML file called episodes.yaml
with open('episodes.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(audio_files, f, allow_unicode=True, sort_keys=False)