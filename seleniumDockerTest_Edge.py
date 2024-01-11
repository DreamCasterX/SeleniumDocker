#!/usr/bin/python3

from selenium import webdriver
import time

from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By




opts = Options()
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-notifications')


print("Test Started")


driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=opts)
time.sleep(3)
driver.maximize_window()
time.sleep(5)


driver.get("https://www.browserstack.com/")
time.sleep(5)

driver.find_element(By.XPATH, "//*[contains(text(), 'Get started free')]").click()
time.sleep(10)

driver.close()
driver.quit()
print("TEST is DONE!!")
