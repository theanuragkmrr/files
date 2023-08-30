# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta


from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
notification_manager=NotificationManager()

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_sheet()
# print(sheet_data)

origin_city_iata="LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_sheet()
# print(data_manager.update_sheet())
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=(6 * 30))

# FlightSearch().check_flights(origin_city_code="LON",destination_city_code="PAR",from_date="15/09/2022",to_date="25/09/2022")

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_iata,
        destination["iataCode"],
        from_date="15/09/2022",
        to_date="25/03/2023",
    )
    if flight.price < destination["lowestPrice"]:
        print(destination["city"])
