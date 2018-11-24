# coding=utf-8

# from selenium import webdriver
# import time

# driver = webdriver.Chrome()
# # driver.get('https://www.baidu.com')
# driver.get('https://www.douban.com/')

# # input_tag = driver.find_element_by_id('kw')
# # input_tag = driver.find_element_by_name('wd')
# # input_tag = driver.find_element_by_class_name('s_ipt')
# # input_tag = driver.find_element_by_xpath('//input[@id="kw"]')

# remember_btn = driver.find_element_by_name('remember')
# remember_btn.click()
# # input_tag.send_keys('python')

# # time.sleep(2)
# # input_tag.clear()
# time.sleep(2)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
# driver.get('http://www.dobai.cn/')

# select_btn = Select(driver.find_element_by_name('jumpMenu'))
# select_btn.select_by_index(1)


from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

input_tag = driver.find_element_by_id('kw')
input_tag.send_keys('python')

submit_tag = driver.find_element_by_id('su')
submit_tag.click()
