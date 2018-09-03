#-*- coding: utf-8 -*-
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re



html = urlopen("https://imgur.com/a/3Woti")
soup = BeautifulSoup(html, "html.parser")

# 폴더 만들기
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# url 경로로 이미지 파일 열기
def open_and_save_image(url,foldername, output_img):
    createFolder(foldername)
    response = requests.get(url)
    print(url)
    print(response)
    img = Image.open(BytesIO(response.content))
    img.save('%s/%s.jpg' % (foldername, output_img))
    return

mydivs = soup.findAll("div", {"class": "post-image-container post-image-container--spacer"})








for index, image in enumerate(mydivs):
    open_and_save_image(f"http://i.imgur.com/{image['id']}.jpg", "imur_pictures",f"{index}")
    print(image['id'])



