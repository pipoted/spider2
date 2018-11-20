# coding=utf-8

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

page = int(input('请输入想要第几页的数据:'))
number = 20

# 构建get参数
data = {
    'start': (page - 1) * number,
    'limit': number,
}

query_string = urllib.parse.urlencode(data)
url += query_string

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode())
