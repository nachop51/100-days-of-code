from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# opens a new chrome tab
driver.get("https://www.python.org/")

list = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
)

print(list)
events = {}
for i, item in enumerate(list.find_elements(By.TAG_NAME, "li")):
    time = item.find_element(By.TAG_NAME, "time").get_attribute(
        "datetime").split('T')[0]
    # get_attribute("innerHTML") also works
    event_name = item.find_element(By.TAG_NAME, "a").text
    events[i] = {time: event_name}

driver.quit()

print(events)
