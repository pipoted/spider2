# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 09:56'

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get('http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp?zd=splc')
time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'lxml')
table = soup.find(name='table', attrs={'id': 'report'})
trs = table.find('tr').find_next_siblings()

for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.text)

driver.quit()
