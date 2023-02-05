from pytube import Playlist

print("Input link : ")
urlf = input()
playlist = Playlist(urlf)

print('print path : ')
path = input()

for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)