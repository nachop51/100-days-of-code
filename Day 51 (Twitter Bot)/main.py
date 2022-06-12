from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

PROMISED_DOWN = 120
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()),
            options=chrome_options
        )
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        ).click()
        time.sleep(35)
        self.down = float(self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text)
        time.sleep(1)
        self.up = float(self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        ).text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(5)
        self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[2]'
        ).click()
        time.sleep(3)
        google_window = self.driver.window_handles[1]
        self.driver.switch_to.window(google_window)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="identifierId"]'
                                 ).send_keys("your mail here")
        time.sleep(1)
        self.driver.find_element(By.XPATH,)


internet = InternetSpeedTwitterBot()

internet.get_internet_speed()
print(internet.down, internet.up)
internet.tweet_at_provider()
