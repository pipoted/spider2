#!/usr/bin/env python
# coding=utf-8


import re


# 分组
text = 'apple`s price $99, orange`s price is $10'
ret = re.search('.*(\$\d+).*(\$\d+)', text)
# print(ret.group())
# print(ret.group(1, 2))
print(ret.groups())
