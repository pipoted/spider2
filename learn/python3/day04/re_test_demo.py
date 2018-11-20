#!/usr/bin/env python
# coding=utf-8

import re


# text = 'apple price is $299'
# ret = re.search('\$\d+', text)
# print(ret.group())

# text = r'\n'
# print(text)

text = '\\n'
ret = re.match('\\\\n', text)
print(ret.group())
