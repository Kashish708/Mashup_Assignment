# Example file name: 101556.py

import sys
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def main():
    # ------------------ ARGUMENT CHECK ------------------
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("Error: NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 10:
        print("Error: NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("Error: AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    os.makedirs("downloads", exist_ok=True)
    os.makedirs("trimmed", exist_ok=True)

    # ------------------ DOWNLOAD VIDEOS ------------------
    print("Downloading videos...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch{num_videos}:{singer} songs"])
    except Exception as e:
        print("Download error:", e)
        sys.exit(1)

    # ------------------ TRIM AUDIO ------------------
    print("Trimming audio files...")
    combined = AudioSegment.empty()

    for file in os.listdir("downloads"):
        if file.endswith(".mp3"):
            try:
                audio = AudioSegment.from_mp3(f"downloads/{file}")
                trimmed = audio[:duration * 1000]
                combined += trimmed
            except Exception as e:
                print(f"Skipping {file}:", e)

    if len(combined) == 0:
        print("No audio files processed.")
        sys.exit(1)

    # ------------------ MERGE & EXPORT ------------------
    combined.export(output_file, format="mp3")
    print(f"✅ Mashup created successfully: {output_file}")

if __name__ == "__main__":
    main()
