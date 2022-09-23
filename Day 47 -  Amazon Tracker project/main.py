import requests
from bs4 import BeautifulSoup
import smtplib

camel_url = "https://camelcamelcamel.com/product/B09739LDTM"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}
response = requests.get(camel_url, headers=header)
print(response)

soup = BeautifulSoup(response.content, "lxml")
soup.prettify()
price = soup.find(class_="column small-8 medium-12").get_text().split("\n")
price_without_curreny = float(price[2].split("$")[1])

title = soup.title.get_text().split("|")[0]

my_email = "email"
password = "password"


if price_without_curreny < (price_without_curreny -100):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="@gmail.com",
                            msg=f"Subject:New price!\n\n{title} is now  {price_without_curreny}\n {camel_url}")
