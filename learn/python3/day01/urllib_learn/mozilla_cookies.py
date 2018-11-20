#!/usr/bin/env python
# coding=utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar

# TODO
cookiejar = MozillaCookieJar('cookies.txt')
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

# response = opener.open('http://www.baidu.com/')
# response = opener.open('http://httpbin.org/cookies/set?course=abc')
response = opener.open('http://httpbin.org/cookies')
# cookiejar.save(ignore_discard=True)

for cookie in cookiejar:
    print(cookie)
