import datetime
from data_manager import DataManager
import datetime as dt
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

tomorrow = dt.datetime.now() + datetime.timedelta(days=1)
to_date = dt.datetime.now() + dt.timedelta(days=(6*30))

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_iata_codes()


for destination in sheet_data:
    flight = flight_search.get_fly_data(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=to_date,
    )

    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_message(message=f"Low price alert! Only £{flight.price} to fly from " \
                                                 f"{flight.origin_city}-{flight.origin_airport} to " \
                                                 f"{flight.destination_city}-{flight.destination_airport}, " \
                                                 f"from {flight.out_date} to {flight.return_date}."
        )

