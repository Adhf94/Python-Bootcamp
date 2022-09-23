import requests
from project_config import *
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

parametros = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AA_API_KEY,
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

response = requests.get(url=STOCK_ENDPOINT, params=parametros)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_cp = data_list[0]["4. close"]
print(yesterday_cp)

before_yesterday_cp = data_list[1]["4. close"]
print(before_yesterday_cp)

difference = abs(float(yesterday_cp) - float(before_yesterday_cp))
print(difference)
percent_diff = round((difference / float(yesterday_cp)) * 100)
print(percent_diff)

# today = dt.datetime.today()
# print(today)
# yesterday = list(data.keys())[0]
# print(yesterday)

up_down = None
if percent_diff >0:
    up_down = "🔺"
else:
    up_down ="🔻"

if abs(percent_diff) > 1:

    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    NEWS_PARAMS = {
            "apiKey": NEWS_API_KEY,
            "q": (COMPANY_NAME, STOCK),


    }
    response_news = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    response_news.raise_for_status()
    news_data = response_news.json()["articles"]
    articulos = news_data[:3]
    print(articulos)
    for art in articulos:
        account_sid = ACCOUNT_SID
        auth_token = AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+',
            body=f'TSLA: {up_down}{percent_diff}%\n'
                 f'{art["title"]}\n'
                 f'{art["description"]}\n'
                 f'{art["url"]}',
            to='whatsapp:+'
        )

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

