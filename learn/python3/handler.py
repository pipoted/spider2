#!/usr/bin/env python3
# coding=utf-8

import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# 创建一个handler
handler = urllib.request.HTTPHandler()
# 通过一个handler创建一个opener
# opener 就是一个对象，发送请求的时候， 直接使用 opener 的方法即可，不必再使用 urlopen
opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url, headers=headers)

# 发送请求
response = opener.open(request)

print(response.read().decode())
