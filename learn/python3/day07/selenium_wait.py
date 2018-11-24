from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

# driver.implicitly_wait(5)

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'form_email'))
)
print(element)

driver.quit()
