from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time


FB_USER = "email"
FB_PASS = "password"
service = Service(r"C:chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://tinder.com/")
time.sleep(2)

login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(2)
fb_login = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]")
fb_login.click()
time.sleep(2)
#Para cambiar de ventanas, se usa el window_handle, el cual se maneja como una lista

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
fb_login_user = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
fb_login_user.send_keys(FB_USER)
time.sleep(2)
fb_login_pass = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
time.sleep(2)
fb_login_pass.send_keys(FB_PASS)
time.sleep(2)
fb_login_pass.send_keys(Keys.ENTER)

#switching back window
driver.switch_to.window(base_window)
time.sleep(5)

#cookies allow
cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()
time.sleep(5)
#location access
loc_access = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
loc_access.click()
time.sleep(5)
#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
notifications_button.click()
time.sleep(10)

#swipe like
for n in range(10):
    time.sleep(5)
    try:
        print("like")
        ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    except NoSuchElementException:
        time.sleep(5)
        print("Not Found")
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    else:
        print("interests window")
        time.sleep(5)
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    # try:
    #     time.sleep(5)
    #     print("called")
    #     like_button = driver.find_element(By.XPATH,
    #         '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
    #     like_button.click()
    # # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    # except ElementClickInterceptedException:
    #     try:
    #         match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
    #         match_popup.click()
    #     #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
    #     except NoSuchElementException:
    #         time.sleep(10)
    # else:
    #     try:
    #         time.sleep(10)
    #         print("called2")
    #         like_button = driver.find_element(By.XPATH,
    #                                           '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
    #
    #         like_button.click()
    #     except NoSuchElementException:
    #         time.sleep(10)
    #         print("called3")
    #         like_button = driver.find_element(By.XPATH,
    #                                           '/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[4]/button')
    #
    #         like_button.click()
driver.quit()