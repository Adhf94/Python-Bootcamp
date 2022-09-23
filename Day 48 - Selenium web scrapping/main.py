from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/Samsung-Unlocked-Smartphone-Intelligent-Graphite/dp/B09BFTMQH9/ref=sr_1_3?crid=3TUV0EV8MHLV3&keywords=samsung+s22+fe&qid=1663284864&sprefix=%2Caps%2C173&sr=8-3")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

search_bar = driver.find_element(By.NAME, "field-keywords")
print(search_bar.get_attribute("nav-input nav-progressive-attribute"))

logo = driver.find_element(By.ID, "nav-logo")
print(logo.size)


#driver.close() <-- cierra una sola tab, mientras que quit, cierra todo el browser.
driver.quit()
