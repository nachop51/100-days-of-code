from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()),
    options=chrome_options
)
driver.get("https://tinder.com/")
time.sleep(2)
terms = driver.find_element(
    By.XPATH, '//*[@id="t546383398"]/div/div[2]/div/div/div[1]/div[1]/button/span'
).click()
time.sleep(1)
login = driver.find_element(
    By.XPATH, '//*[@id="t546383398"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
).click()
time.sleep(1)
facebook = driver.find_element(
    By.XPATH, '//*[@id="t-1181997678"]/div/div/div[1]/div/div/div[3]/span/div[2]/button'
).click()
time.sleep(2)

# Change the current selenium window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(
    By.NAME, 'email'
).send_keys("your mail")
time.sleep(1)
password = driver.find_element(By.NAME, 'pass').send_keys("your password")
time.sleep(1)
log_in = driver.find_element(By.NAME, 'login').click()
time.sleep(1)
accept_terms = driver.find_element(
    By.XPATH, '//*[@id="mount_0_0_cB"]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div'
).click()
time.sleep(10)
# Get back to the tinder window
tinder_window = driver.window_handles[0]
driver.switch_to.window(tinder_window)

time.sleep(5)
allow_location_button = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
