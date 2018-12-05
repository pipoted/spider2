# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 11:58'

import requests
import re
from lxml import etree

URL = 'http://wz.sun0769.com/index.php/sheqing?page=30'


def get_number(url):
    page_text = requests.get(url).content.decode('gb2312', errors='ignore')
    my_xml = etree.HTML(page_text)
    num_str = my_xml.xpath('//*[@class="pagination"]/text()')[-1].strip()
    pat = re.compile(r'\d+', re.IGNORECASE)
    data_list = pat.findall(num_str)

    return eval(data_list[0])


def make_url_list(number):
    url_list = []
    url = 'http://wz.sun0769.com/index.php/sheqing?page='
    if number % 30 == 0:
        for i in range(number // 30):
            url_list.append(url + str(i * 30))
    else:
        for i in range(number // 30 + 1):
            url_list.append(url + str(i * 30))

    return url_list


my_list = make_url_list(8000433)
for url in my_list:
    print(url)
