# coding=utf-8

import urllib.parse

# image_url = 'http://pic29.nipic.com/20130511/9252150_174018365301_2.jpg'

word = {
    '姓名': '肖'
}

word = urllib.parse.quote(str(word))
wd = urllib.parse.unquote(word)
print(word)
print(wd)
