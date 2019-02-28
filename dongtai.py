#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

url = 'http://www.zjzfcg.gov.cn/purchaseNotice/index.html?_=1546402255489'

driver = webdriver.PhantomJS()
driver.get(url)

print(driver.page_source)

driver.close()
