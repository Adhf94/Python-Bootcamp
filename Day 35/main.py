import requests
from twilio.rest import Client

account_sid = "account sid"
auth_token = "auth token"


MY_API_KEY = "api_key"
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": "your lat",
    "lon": "your long",
    "appid": MY_API_KEY,
}

response = requests.get(OMW_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for every_3h in range(0, 4):
    condition_code = weather_data["list"][every_3h]["weather"][0]["id"]
    print(condition_code)
    if condition_code < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+',
        body='Va a llover, busca un paraguas.',
        to='whatsapp:+'
    )
    print(message.sid)
