#!/usr/bin/env python
# coding=utf-8

# http://www.renren.com/968662672

from urllib import request
from http.cookiejar import CookieJar
from urllib import parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
data = {
    'email':'15570136250',
    'password':'xzx199110',
}
data = parse.urlencode(data).encode()
login_url = 'http://www.renren.com/relogin.do'

# 1.登录
# 创建一个 cookiejar 对象
cookiejar = CookieJar()
# 使用cookjar创建一个HTTPCookiesProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 使用上一步创建的handler对象创建一个opener
opener = request.build_opener(handler)
# 使用opener发送登录的请求（人人网的账号密码）
req = request.Request(url=login_url,data=data,headers=headers)
opener.open(req)


# 2.访问个人主页
my_home_url = 'http://www.renren.com/968662672'
# 获取个人主页的时候，不用新建一个opener
# 而是应该使用之前的opener，因为之前的opener已经包含了登录所需的cookies信息
req = request.Request(my_home_url, headers=headers)
response = opener.open(req)

with open('download/my_renren.html', 'w', encoding='utf-8') as fp:
    fp.write(response.read().decode())
