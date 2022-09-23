import requests
SHEET_ENDPOINT = "Sheety endpoint"
auth_header = {
    "Authorization": "your token"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEET_ENDPOINT, params=auth_header)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{SHEET_ENDPOINT}/{city['id']}",
                                    params=auth_header,
                                    json=new_data)
            print(response.text)