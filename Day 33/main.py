import requests
import datetime as dt

LNG = -69.92483520507812
LAT = 18.448442459106445
parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")
sunrise_hour = sunrise[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")
sunset_hour = sunset[1].split(":")[0]
print(sunrise_hour, sunset_hour)
current_day = dt.datetime.now().hour

print(current_day)