from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re






# 폴더 만들기
# create folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Cannot Create Directory.' + directory)


# url 경로로 이미지 파일 열기
# use url to open image file
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img



# cropping the image
def crop(input_img, foldername, output_img):
    width, height = input_img.size
    if height > 430:
        area = (0, 0, 640, 430) #(가로시작, 세로시작, 가로끝, 세로끝) #(width start, height start, width end, height end)
        cropped_img = input_img.crop(area)
        cropped_img.save('%s/%s.jpg' % (foldername, output_img))
        print('cropping: %s' % input_img)



def maincode(url):
    createFolder('data')
    url = urlopen(url)
    soup = BeautifulSoup(url, "html.parser")
    # create folder same as the title of the webpage
    title = soup.find('title').text
    title = re.sub('[-=.#/?:$}]', '', title) #removing special characters
    directory = f'data/{title}'
    createFolder(directory)

    # find images
    tags = soup.findAll('img')
    for index, image in enumerate(tags):
        try:
            compare = image['alt']
        except:
            compare = None
            print('not found')
        if compare != None: # get only car images want
            if compare == "차량사진" or compare == "차량 썸네일 사진":
                input_img = open_image(image['src'])
                crop(input_img, title, index)


if __name__ == "__main__":
    maincode("http://www.bobaedream.co.kr/cyber/CyberCar_view?no=692954&gubun=I")