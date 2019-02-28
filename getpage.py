#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

#  URL = 'http://yunqi.qq.com/bk/so2/n10p1'

#  #  print(requests.get(URL).text)
#  content = requests.get(URL).text
#  mytree = etree.HTML(content)

#  book_info = mytree.xpath('//div[@class="book"]/div[@class="book_info"]')
#  for line in book_info:
#  title = line.xpath('.//h3//text()')[-1]
#  #  print(title)
#  url = line.xpath('./h3/a/@href')[-1]
#  print(url)

URL = 'http://yunqi.qq.com/bk/xhyq/21085455.html'
content = requests.get(URL).text
mytree = etree.HTML(content)

title = mytree.xpath('//div[@class="title"]/strong/a/text()')[-1]
#  print(title)
tags = mytree.xpath('//div[@class="tags"]/text()')[0].strip()
#  print(tags)
info = mytree.xpath('//div[@class="info"]//p/text()')
print(info)
