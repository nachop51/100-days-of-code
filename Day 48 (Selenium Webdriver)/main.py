from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
timeout = 300
counter = time.time() + 3
timeout_start = time.time()


print()

while time.time() < timeout_start + timeout:
    cookie.click()
    if time.time() > counter:
        store = driver.find_element(By.XPATH, '//*[@id="store"]')
        items = store.find_elements(By.CSS_SELECTOR, "div")
        items.pop()
        for item in reversed(items):
            print(item.get_attribute('class'))
            if "grayed" not in item.get_attribute('class'):
                item.click()
        counter = time.time() + 3

cookie_per_s = driver.find_element_by_id("cps").text
print(cookie_per_s)
