# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-03 20:58'

import requests

URL = 'http://www.hshfy.sh.cn/shfy/gweb2017/channel_zx_list.jsp?'
post_data = {
    'ktrqjs': '2019-01-03',
    'ktrqks': '2018-12-03',
    'pagesnum': '1',
    'yzm': 'dqUh',
}


def get_html_post(url: str, data):
    return requests.post(url, data).text


def get_html_get(url):
    return requests.get(url).text


print(get_html_post(URL, post_data))
