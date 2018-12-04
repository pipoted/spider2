# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 11:20'

import gevent
import time
from gevent import monkey

monkey.patch_all()
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp?'


def download(url, start, end, file):
    driver = webdriver.Chrome()
    driver.get(url)
    gevent.sleep(10)

    for i in range(start, end):
        js = 'javascript:goPage("' + str(i) + '")'
        driver.execute_script(js)
        print('js is run', i)
        gevent.sleep(10)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find(name='table', attrs={'id': 'report'})
        trs = table.find('tr').find_next_siblings()

        for tr in trs:
            tds = trs.find_all('td')
            line_str = ''
            for td in tds:
                line_str += td
                line_str += ' # '

            line_str += '\r\n'
            print(line_str)
            file.write(line_str.encode('utf-8'))

    driver.quit()


file = open('save.txt', 'wb')
gevent.joinall([
    gevent.spawn(download, URL, 1, 2, file),
    gevent.spawn(download, URL, 2, 4, file),
    gevent.spawn(download, URL, 4, 8, file),
    gevent.spawn(download, URL, 8, 10, file),
    gevent.spawn(download, URL, 10, 12, file),
])
file.close()
