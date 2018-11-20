# coding=utf-8

import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.test(url=url)

# print(response.read().decode())

# with open('baidu.html', 'w', encoding='utf8') as fp:
#     fp.write(response.read().decode())

# print(response.geturl())
# print(dict(response.getheaders()))  # 获取头部信息， 列表中包含元组
# print(response.getcode())
# print(response.readlines())

# with open('baidu_01.html', 'wb') as fp:
#     fp.write(response.read())

image_url = 'http://pic29.nipic.com/20130511/9252150_174018365301_2.jpg'

response = urllib.request.test(image_url)
# 图片只能写入本地二进制格式
# with open('test.jpg', 'wb') as fp:
#     fp.write(response.read())

urllib.request.urlretrieve(image_url, 'xiao.jpg')
