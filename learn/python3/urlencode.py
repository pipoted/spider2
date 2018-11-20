# coding=utf-8

import urllib.parse

url = 'http://www.baidu.com/index.html'

data = {
    'name': '肖',
    'age': 21,
    'sex': 'male'
}

query_string = urllib.parse.urlencode(query=data)

print(query_string)
