import os
import requests
import shutil

from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

url = "https://walklikejesus.files.wordpress.com/2020/05/new_heaven_earth.2jpg.jpg"

r =  requests.get(url, stream=True)
r.raise_for_status()

download_file(url, DOWNLOADS_DIR, fname='flower.jpeg')