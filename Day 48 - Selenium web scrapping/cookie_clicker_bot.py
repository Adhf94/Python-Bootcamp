from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

service = Service(r"C:chromedriver.exe")
driver = webdriver.Chrome(service=service)




driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
select_language = driver.find_element(By.ID, "langSelect-EN")
select_language.click()

time.sleep(5)
big_cookie = driver.find_element(By.ID, "bigCookie")
big_cookie.click()

time.sleep(5)


def clicker():
    for click in range(1, 50):
        time.sleep(0.2)
        big_cookie.click()

clicker()

raw_clicker_price = driver.find_element(By.ID, "productPrice0")
clicker_price = int(raw_clicker_price.text)
clicker_button = driver.find_element(By.ID, "product0")
raw_grandma_price = driver.find_element(By.ID, "productPrice0")
grandma_price = int(raw_clicker_price.text)

grandma_button = driver.find_element(By.ID, "product1")
while True:
    raw_score = driver.find_element(By.ID, "cookies")
    score = int(raw_score.text.split(" ")[0])
    time.sleep(1)
    if score > clicker_price:
        time.sleep(1)
        clicker_button.click()
    elif score > grandma_price:
        time.sleep(1)
        grandma_button.click()
    clicker()
