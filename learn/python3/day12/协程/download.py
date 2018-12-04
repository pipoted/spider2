# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-03 13:34'

import gevent
import gevent.monkey
from urllib import request

gevent.monkey.patch_all()  # 自动切换


def download(url: str):
    print('start', url)
    data = request.urlopen(url).read()
    print('len', len(data), url)


gevent.joinall([
    gevent.spawn(download, 'http://www.baidu.com'),
    gevent.spawn(download, 'http://www.qq.com'),
    gevent.spawn(download, 'http://www.163.com'),
    gevent.spawn(download, 'http://www.sina.com'),
])
