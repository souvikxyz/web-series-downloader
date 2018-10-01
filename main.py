from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import hashlib
import sys
import requests
import os

file_index = 1
BASE_URL = 'https://www.hoichoi.tv'
URL = raw_input("Series page URL : ")
folder_name = raw_input("Folder Name : ")


'''Moves the chrome window in a virtual display'''
display = Display(visible=0, size=(800, 600))
display.start()

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
driver = webdriver.Chrome(
    executable_path='/var/chromedriver/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(10)


def download_video(video_download_link, file_index):
    '''Downloads the video and saves it'''
    video = requests.get(video_download_link)
    file_name = str(file_index) + '.mp4'
    with open(file_name, 'wb') as f:
        f.write(video.content)


def prepare_video_download_link(video_link, file_index):
    '''Prepares the video download link'''
    driver.get(video_link)
    video_download_link = driver.find_element_by_class_name(
        'vjs-tech').get_attribute("src")
    print "Downloading Video : {}".format(file_index)
    download_video(video_download_link, file_index)


'''Get the list of videos and each of their links'''
page_response = requests.get(URL)
soup = BeautifulSoup(page_response.content, "html.parser")
playlist_content = soup.find_all(class_='list__item__title')

os.chdir('/home/jayjeet/Videos')
os.mkdir(folder_name)
os.chdir(folder_name)

'''Traverse the playlist and downloads videos'''
for video in playlist_content:
    video_link = BASE_URL + video["href"]
    prepare_video_download_link(video_link, file_index)
    file_index += 1

print('Your Webseries is successfully downloaded')

