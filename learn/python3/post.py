# coding=utf-8

import urllib.request
import urllib.parse

# 获取 post url 地址
post_url = 'https://fanyi.baidu.com/sug'
word = input('请输入要查询的英文单词：')
# 构建post表单数据
from_data = {
    'kw': word,
}

# 发送请求的过程
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)
# 处理 post 表单数据
from_data = urllib.parse.urlencode(from_data).encode()
# 发送请求
response = urllib.request.urlopen(request, data=from_data)

print(response.read().decode())
