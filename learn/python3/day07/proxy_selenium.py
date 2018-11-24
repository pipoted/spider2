#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://183.63.90.98:8060')

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://httpbin.org/ip')

# driver.implicitly_wait(5)
# driver.quit()
