import requests
import os

folder_name = raw_input("folder name : ")


def download_video(video_download_link, file_index):
    '''Downloads the video and saves it'''
    video = requests.get(video_download_link)
    file_name = str(file_index) + '.mp4'
    os.chdir('/home/jayjeet/Videos')
    os.mkdir(folder_name)
    os.chdir(folder_name)
    with open(file_name, 'wb') as f:
        f.write(video.content)


download_video('https://www.youtube.com/watch?v=aDwCCUfNFug', 1)
