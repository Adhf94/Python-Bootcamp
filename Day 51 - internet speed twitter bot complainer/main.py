from internet_speed_checker import InternetSpeedTwitterBot
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\Adrian Hurtado\Desktop\100 days python challenge\Day 48\chromedriver.exe")
bot = InternetSpeedTwitterBot(service)
bot.get_internet_speed()
bot.tweet_at_provider()