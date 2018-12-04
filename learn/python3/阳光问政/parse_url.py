# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 11:58'

import requests
import re

URL = 'http://wz.sun0769.com/index.php/sheqing?page='


def get_url(url):
    return requests.get(url).content.decode(encoding='gb2312', errors='ignore')


def get_post_number(func: function, url: str):
    page_html: str = func(url)
    num = int(re.search(r'.*共(\d)条记录.*', page_html))
