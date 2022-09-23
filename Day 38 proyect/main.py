import requests
import datetime as dt
import os

GENDER = "male"
WEIGHT_KG = 92
HEIGHT_CM = 1.82
AGE = 28


APP_ID = os.environ["NUTRITION_APP_ID"]
API_KEY = os.environ["NUTRITION_API_KEY"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header_auth = os.environ["TOKEN"]

exercise_text = input("What you did today ?").lower()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}
auth_headers = {
    'Content-Type': 'application/json',
    "Authorization": header_auth,
}
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, headers=headers, json=params)
response.raise_for_status()
data = response.json()
print(data)

excercise = str(data["exercises"][0]["name"]).title()
calories = round(data["exercises"][0]["nf_calories"])
duration = round(data["exercises"][0]["duration_min"])

today = dt.datetime.today().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")
print(excercise, duration, calories, today, time)

newRowEndpoint = os.environ["SHEET ENDPOINT"]

for excercises in data["exercises"]:
    rowData = {
        "myWorkoutsWorkout": {
            "date": today,
            "time": time,
            "exercise": excercise,
            "duration": duration,
            "calories": calories,
        }
    }
    post_excercise_data = requests.post(f"{newRowEndpoint}", json=rowData, headers=auth_headers)
    post_excercise_data.raise_for_status()




my_sheety_endpoint = "sheety endpoint"
response2 = requests.get(f"{my_sheety_endpoint}", headers=auth_headers)
response2.raise_for_status()
my_csv = response2.json()
print(my_csv)