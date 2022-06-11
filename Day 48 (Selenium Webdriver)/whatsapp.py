from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# opens a new chrome tab
driver.get("https://web.whatsapp.com/")

input("Scan the QR Code and press Enter...")

chat = driver.find_element(
    By.XPATH, '//*[@id="pane-side"]/div/div/div/div[11]/div/div/div[2]')

chat.click()

for i in range(10):
    search = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    search.send_keys("message")
    search.send_keys(Keys.ENTER)
