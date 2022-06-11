from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# opens a new chrome tab
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.XPATH, '/html/body/form/input[1]')
lname = driver.find_element(By.XPATH, '/html/body/form/input[2]')
email = driver.find_element(By.XPATH, '/html/body/form/input[3]')

fname.send_keys("John")
lname.send_keys("Doe")
email.send_keys("johndoe@gmail.com")

signup = driver.find_element(By.XPATH, '/html/body/form/button')
signup.click()
