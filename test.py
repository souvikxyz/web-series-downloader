import requests
import os

def download_video(video_download_link,filename):
    video = requests.get(video_download_link)
    file_ = str(filename) + '.mp4'
    os.chdir('/home/jayjeet/Videos')
    with open(file_,'wb') as f:
        f.write(video.content)

download_video('https://www.youtube.com/watch?v=aDwCCUfNFug',1)

