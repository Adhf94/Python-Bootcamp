import requests
from datetime import datetime
import smtplib
import time

MY_LAT = "your lat"
MY_LONG = "Your long"
MY_EMAIL = "your email"
PASSWORD = "your password"

def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT + 5) <= iss_latitude <= (MY_LAT - 5) and (MY_LONG + 5) <= iss_longitude <= (MY_LONG - 5):
        return True
#Your position is within +5 or -5 degrees of the ISS position.

def es_de_noche():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    print(sunrise, sunset, time_now)
    if sunrise <= time_now >= sunset:
        return True


while True:
    time.sleep(60)
    if iss_position() and es_de_noche():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="email",
                                msg="Subject:Iss is over you!\n\nLa iss esta en pasando en este momento por encima de ti.")