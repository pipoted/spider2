# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 15:28'

import PIL
from PIL import Image
from PIL import ImageDraw

image = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
# image.show()

draw = ImageDraw.Draw(image, mode='RGB')
draw.text([0, 0], 'hello world', 'red')

with open('code.png', 'wb') as fp:
    image.save(fp, format='png')
