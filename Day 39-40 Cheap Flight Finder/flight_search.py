import requests
import datetime as dt
from flight_data import FlightData

search_api_key = "API KEY"
tequila_endpoind = "https://tequila-api.kiwi.com"

today = dt.datetime.today().strftime("%d/%m/%Y")
to_date = dt.datetime.today() + dt.timedelta(days=15)
to_date = to_date.strftime("%d/%m/%Y")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        loc_endpoint = f"{tequila_endpoind}/locations/query"
        headers = {"apikey": search_api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=loc_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_fly_data(self, origin_city_code, destination_code, from_time, to_time):
        fly_endpoint = f"{tequila_endpoind}/v2/search"
        headers = {"apikey": search_api_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(fly_endpoint, headers=headers, params=query)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No Flights found for {destination_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: libras:{flight_data.price}")
        return flight_data
