#!/usr/bin/env python
# coding=utf-8

import re


# findall函数
text = 'apple`s price , orange`s price is 10.20'
# ret = re.findall('\$\d+', text)
# print(ret)


# sub函数
# ret = re.sub('\$\d+', '0', text)
# print(ret)


# split函数
# ret = re.split(' ', text)
# print(ret)


# compile
r = re.compile('\d+\.?\d*')
ret = re.search(r, text)
print(ret.group())
