#!/usr/bin/env python3
# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# driver.get('https://www.douban.com/')
driver.execute_script('window.open("https://www.douban.com/")')
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])
print(driver.current_url)
driver.implicitly_wait(5)
driver.quit()
