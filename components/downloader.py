from pytube import YouTube
from datetime import datetime
import os


def downloader(url, tot, *kwargs):
    all_element = (os.listdir(os.getcwd()))
    try:
        yt = YouTube(url)
    except Exception as E:
        print(f"Error in object creation.",end= "  ")
        print(f"({kwargs[0]}/{tot}) ERR : {E}")
        return [url, kwargs[0]]
    filename = f"({kwargs[0]}){yt.title}.mp4"
    if filename in all_element:
        try:
            print(f"({kwargs[0]}/{tot}) Already found {yt.title} {{ {round((os.path.getsize(filename)/(1024*1024)),1)}MB || {datetime.now().strftime('%H:%M:%S')} }}")
        except Exception as e:
            print(f"({kwargs[0]}/{tot}) Already found {yt.title} ")
        return 0
    streams = yt.streams.filter(progressive=True, resolution='720p', type='video')
    print(f"({kwargs[0]}/{tot}) Downloading {yt.title}", end='   -------------------------  ')
    if len(streams) > 0:
        try :
            yt.streams.filter(progressive=True, resolution='720p', type='video').first().download(filename=f"{kwargs}."
                                                                                                       f"{yt.title}")
        except Exception as E :
            print("Err in downloading.")
            return [url, kwargs[0]]
    else:
        try :
            yt.streams.filter(progressive=True, type='video').first().download(filename=f"{kwargs}.{yt.title}")
        except Exception as E :
            print("Err in downloading.")
            return [url, kwargs[0]]
    try:
        print(f"Done  {{ {round((os.path.getsize(filename)/(1024*1024)),1)}MB || {datetime.now().strftime('%H:%M:%S')} }}")
    except Exception as E:
        print("Done")
    return 'Done'


def organiser(ins):
    playlist_name = ins.playlist_name
    all_videos = ins.playlist_videos
    ar = []
    if not os.path.exists(playlist_name):
        try:
            os.mkdir(playlist_name)
        except OSError:
            playlist_name = input('Enter the name of the folder to save files in : ')
            try:
                os.mkdir(playlist_name)
            except OSError:
                organiser(ins)
        os.chdir(playlist_name)
        print(os.getcwd())
    else:
        os.chdir(playlist_name)
    for i, videos in enumerate(all_videos):
        ar.append(downloader(videos, ins.total_videos, (i + 1)))
    ar = [i for i in ar if i != 'Done']
    return ar


if __name__ == '__main__':
    yt = downloader("https://www.youtube.com/watch?v=3iY0figLAwo", 1, 1)
