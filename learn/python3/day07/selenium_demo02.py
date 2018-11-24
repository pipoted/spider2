from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

submit_btn =driver.find_element_by_id('su')
print(type(submit_btn))
# print(submit_btn.get_attribute('value')
driver.save_screenshot('baidu.png')
driver.quit()