from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(r"Your driver root")


USERNAME = 'Gmail'
PASSWORD = 'password'


class InstaFollower:
    def __init__(self,path):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)
        log_path = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        log_path.send_keys(USERNAME)
        time.sleep(1)
        pass_path = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        pass_path.send_keys(PASSWORD)
        time.sleep(1)
        pass_path.send_keys(Keys.ENTER)
        time.sleep(3)

    def find_follower(self):
        search_bar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys("complex")
        time.sleep(3)
        complex_profile = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a/div/div[2]/div[1]/div/div/div[1]')
        complex_profile.click()
        time.sleep(3)

    def follow(self):
        time.sleep(10)
        follower_span = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
        follower_span.click()
        for index in range(1,20):
            time.sleep(3)
            button = self.driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{index}]/div[3]/button")

            if button.text != "Seguir":
                pass
            else:
                print("followed")
                button.click()
                time.sleep(2)
        self.driver.quit()


bot = InstaFollower(service)
bot.login()
bot.find_follower()
bot.follow()
