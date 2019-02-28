#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = 'https://www.cyzone.cn/event/488608.html'

content = requests.get(url).text
my_tree = etree.HTML(content)

show_title = ''.join(my_tree.xpath('//div[@class="show_title"]/h1//text()'))
print(show_title)
