from pytube import YouTube
from moviepy.editor import *

# Replace the URL with the one you want to download
url = "https://youtu.be/YwEKIl3qQzA"

# Create a YouTube object and get the video stream
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory
video_file = stream.download()

# Convert the video to MP3 using moviepy
video = VideoFileClip(video_file)
audio_file = video.audio.write_audiofile(f"{yt.title}.mp3")

# Delete the original video file
video.close()
os.remove(video_file)
