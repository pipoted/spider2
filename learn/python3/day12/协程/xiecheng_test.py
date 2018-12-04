# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-03 12:52'

import greenlet
import time


def go1():
    while True:
        print('hello')
        gr2.switch()
        time.sleep(1)


def go2():
    while True:
        print('world')
        gr1.switch()
        time.sleep(1)


if __name__ == '__main__':
    gr1 = greenlet.greenlet(go1)
    gr2 = greenlet.greenlet(go2)
    gr1.switch()
