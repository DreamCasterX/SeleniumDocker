#!/usr/bin/python3


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

selenium_grid = "http://localhost:4444/wd/hub"
url = "https://www.browserstack.com/"


def Edge():
    from selenium.webdriver.edge.options import Options
    opts = Options()
    opts.add_argument('--ignore-ssl-errors=yes')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--disable-notifications')
    print("Test Started")
    driver = webdriver.Remote(command_executor=selenium_grid, options=opts)
    time.sleep(3)
    driver.maximize_window()
    time.sleep(5)
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Get started free')]").click()
    time.sleep(10)
    driver.close()
    driver.quit()
    print("TEST is DONE!!")
    
def Chrome():
    from selenium.webdriver.chrome.options import Options
    opts = Options()
    opts.add_argument('--ignore-ssl-errors=yes')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--disable-notifications')
    print("Test Started")
    driver = webdriver.Remote(command_executor=selenium_grid, options=opts)
    time.sleep(3)
    driver.maximize_window()
    time.sleep(5)
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Get started free')]").click()
    time.sleep(10)
    driver.close()
    driver.quit()
    print("TEST is DONE!!")

def Firefox():
    from selenium.webdriver.firefox.options import Options
    opts = Options()
    opts.add_argument('--ignore-ssl-errors=yes')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--disable-notifications')
    print("Test Started")
    driver = webdriver.Remote(command_executor=selenium_grid, options=opts)
    time.sleep(3)
    driver.maximize_window()
    time.sleep(5)
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Get started free')]").click()
    time.sleep(10)
    driver.close()
    driver.quit()
    print("TEST is DONE!!")
    
    
while True:
    flavor = input("Run your test on browser: \n(1)Edge  (2)Chrome  (3)Firefox \n")
    if flavor == "1":
        Edge()
    if flavor == "2":
        Chrome()
    if flavor == "3":
        Firefox()
    if flavor == "Q" or "q":
        break
    else:
        continue
