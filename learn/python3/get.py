# coding=utf-8
import urllib.parse
import urllib.request

word = input('您想要搜索的内容：')
url = 'http://www.baidu.com/s?'

# 将参数写成一个字典
data = {
    'ie': 'utf-8',
    'wd': word
}

url += urllib.parse.urlencode(data)
print(url)

# 发送请求
response = urllib.request.test(url)

filename = word + '.html'

with open(filename, 'wb') as fp:
    fp.write(response.read())
