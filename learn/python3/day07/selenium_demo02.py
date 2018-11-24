from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')


input_tag = driver.find_element_by_id('kw')
submit_tag = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(input_tag)
actions.send_keys_to_element(input_tag, 'python')
actions.move_to_element(submit_tag)
actions.click(submit_tag)
actions.perform()
