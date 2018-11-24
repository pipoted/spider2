from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

for cookie in driver.get_cookies():
    print(cookie)


print(driver.get_cookie('PSTM'))

driver.delete_cookie('PSTM')

print(driver.get_cookie('PSTM'))
driver.quit()
