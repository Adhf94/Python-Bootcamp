from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


service = Service(r"C:chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

enter_fname = driver.find_element(By.NAME, "fName")
enter_fname.send_keys("Primer Nombre")
enter_lname = driver.find_element(By.NAME, "lName")
enter_lname.send_keys("Last name")
enter_email = driver.find_element(By.NAME, "email")
enter_email.send_keys("email")
# enter_email.send_keys(Keys.ENTER)
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.send_keys(Keys.ENTER)

driver.quit()
