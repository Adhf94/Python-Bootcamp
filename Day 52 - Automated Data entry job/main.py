import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import lxml
import json


zillow = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.54662550878906%2C%22east%22%3A-122.32003249121094%2C%22south%22%3A37.69125507932883%2C%22north%22%3A37.859232413339626%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
gg_form_url = 'Your form link'
service = Service(r"Your driver root")

header = {
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
response = requests.get(zillow, headers=header)
zillow_data = response.text

soup = BeautifulSoup(zillow_data, "lxml")

javascript_data = soup.find('script', {'data-zrr-shared-data-key': 'mobileSearchPageStore'}).text
json_data = json.loads(javascript_data.split('--')[1])
filter_data = json_data["cat1"]["searchResults"]['listResults']

links = soup.find_all(name="a", class_="property-card-link")


all_links = []
property_links = [link['detailUrl'] for link in filter_data]
for linkss in property_links:
    if "http" not in linkss:
        repaired_link = "https://zillow.com" + linkss
        all_links.append(repaired_link)
    else:
        all_links.append(linkss)

print(len(all_links))
all_prices = []
for property in range(len(all_links)):
    try:
        price = filter_data[property]['units'][0]['price'].strip('$/mo+')
        all_prices.append(price)
    except KeyError:
        price = filter_data[property]['price'].strip('$/mo+')
        all_prices.append(price)

print(len(all_prices), "prices")
all_address = []
for index in range(len(all_links)):
        address = filter_data[index]['address']
        all_address.append(address)

print(len(all_address), 'addresses')

driver = webdriver.Chrome(service=service)

# for asset in range(len(filter_data)):
#     driver.get(gg_form_url)
#     time.sleep(2)
#     address_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     address_input.send_keys(all_address[asset])
#     time.sleep(1)
#     price_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     price_input.send_keys(all_prices[asset])
#     time.sleep(1)
#     link_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     link_input.send_keys(all_links[asset])
#     time.sleep(1)
#     send_bt = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
#     send_bt.click()
#     time.sleep(1)

driver.get('google forms gmail url')
time.sleep(1)
email_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email_input.send_keys('@gmail.com')
time.sleep(1)
email_input.send_keys(Keys.ENTER)
#Needs propper gmail login verification
driver.quit()