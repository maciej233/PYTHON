from pytube import YouTube
import sys

link = sys.argv[1]
path = sys.argv[2]

yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd.download(path)
print(f"Name:{yt.title}")