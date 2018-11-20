# coding=utf-8

import urllib.parse
import urllib.request

url = 'http://www.baidu.com/'

# response = urllib.request.urlopen(url)
# print(response.read().decode())

# 自己要伪装的头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())
