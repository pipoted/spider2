# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-03 13:02'

import gevent
import time


def showwait(name, n):
    for i in range(n):
        print(name, '等待了', i + 1, '秒')
        gevent.sleep(1)


# showwait('xiao', 10)
# showwait('li', 10)

g1 = gevent.spawn(showwait, 'xiao', 10)
g2 = gevent.spawn(showwait, 'li', 10)
g3 = gevent.spawn(showwait, 'zhang', 10)

g1.join()
g2.join()
g3.join()
