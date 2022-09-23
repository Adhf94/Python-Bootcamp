from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(r"C:\Users\Adrian Hurtado\Desktop\100 days python challenge\Day 48\chromedriver.exe")
PROMISED_DOWN = 150
PROMISED_UP = 10
speed_test = "https://www.speedtest.net/es"
TT_USER = "user"
TT_PASS = "password"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(speed_test)
        start_bt = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_bt.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        time.sleep(2)

        log_screen = self.driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        log_screen.click()
        time.sleep(2)
        log_email = self.driver.find_element(By.XPATH,
                                        '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        log_email.send_keys(TT_USER)
        time.sleep(2)
        log_email.send_keys(Keys.ENTER)
        time.sleep(3)

        user_ver = self.driver.find_element(By.XPATH,
                                       '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_ver.send_keys("DummieHose")
        time.sleep(1)
        user_ver.send_keys(Keys.ENTER)
        time.sleep(5)
        pass_input = self.driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(TT_PASS, Keys.ENTER)
        time.sleep(5)
        make_tweet = self.driver.find_element(By.CSS_SELECTOR, '.public-DraftEditor-content[contenteditable=true]')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        time.sleep(1)
        make_tweet.click()
        make_tweet.send_keys(tweet)
        tweet_bt = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_bt.click()
        time.sleep(2)
        self.driver.quit()

