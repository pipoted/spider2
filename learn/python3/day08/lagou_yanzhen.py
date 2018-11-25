import pytesseract

from urllib import request
from PIL import Image


def main():
    # url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E9%AA%8C%E8%AF%81%E7%A0%81'

    # request.urlretrieve(url, 'index.jpg')
    image = Image.open('hello.jpg')
    while True:
        text = pytesseract.image_to_string(image)
        print(text)


if __name__ == '__main__':
    main()
