from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
upcoming_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li time")
upcoming_event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li  a")
for thing in upcoming_dates:
    print(thing.text)

for thing2 in upcoming_event_name:
    print(thing2.text)

events_dic = {i: {"time": date.text, "name": text.text} for i, (date, text) in enumerate(zip(upcoming_dates, upcoming_event_name))}

print(events_dic)

driver.quit()
