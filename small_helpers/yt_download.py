from pytube import YouTube
import sys

link = sys.argv[1]

yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd.download("/home/vncuser1/videos")
print(f"Name:{yt.title}")