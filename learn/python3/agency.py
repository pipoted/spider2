#!/usr/bin/env python
# coding=utf-8

import urllib.request
import urllib.parse

# ['113.108.242.36:47713', '122.237.107.173:80', '61.135.217.7:80', '106.75.226.36:808', '210.22.176.146:32153', '58.53.128.83:3128', '27.17.45.90:43411', '123.7.61.8:53281'] 
# 183.15.172.23:61430
# 创建一个handler
handler = urllib.request.ProxyHandler({
    'http':'183.15.172.23:61430',
})
# 创建一个opener
opener = urllib.request.build_opener(handler)

url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)
response = opener.open(request)
with open('ip.txt', 'wb') as fp:
    fp.write(response.read())
    

