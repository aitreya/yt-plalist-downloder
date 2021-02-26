from components.plalist_obj import Playlist
from components.downloader import organiser


def Send_data(play_obj):
    left = organiser(play_obj)
    not_downloaded = len(left)
    if not_downloaded > 0 :
        pass


link = input("Enter the Link of the playlist : ")
instance = Playlist(link)
if instance.is_downloadable:
    if instance.success_rate < 100:
        print(f"The success rate is {instance.success_rate}% and we got f{instance.total_videos}/"
              f"{len(instance.playlist_videos)}\nEnter any key to continue or press 'R' to exit the program")
        if (input()).capitalize() == 'R':
            exit(code='User requested exit .')
        else:
            print(f'Going to download the {len(instance.playlist_videos)} videos')
            Send_data(instance)
    else:
        print("Going to Download all videos")
        Send_data(instance)
else:
    print("the Playlist is not downloadable due to whatever reasons.")