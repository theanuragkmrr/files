import requests

from flight_data import FlightData
tequila_endpoint="https://tequila-api.kiwi.com"
tequila_key="ZI0o_BgdvbCCyGODwhGio6-RqPztokbL"

class FlightSearch:

    def get_destination_code(self,city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        location_endpoint=f"{tequila_endpoint}/locations/query"
        headers={
            "apikey":tequila_key
        }
        query={
            "term":city_name,
            "location_types":"city"
        }
        response=requests.get(url=location_endpoint,params=query,headers=headers)
        results=response.json()["locations"]
        code=results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_date, to_date):
        headers = {"apikey": tequila_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from":from_date,
            "date_to":to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{tequila_endpoint}/v2/search",
            headers=headers,
            params=query,
        )
        # data=response.json()["data"][0]
        try:
            data = response.json()["data"][0]
        except (IndexError,AttributeError):
            print(f"No flights found for {destination_city_code}.")
            return None
        except AttributeError:
            print("There is no such attribute")
            return None
        flight_data=FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][0]["local_arrival"].split("T")[0]
        )
        print(f"{flight_data.destination_city}:£{flight_data.price}")
        return flight_data

# FlightSearch().check_flights("LON","PAR")

# f=FlightSearch().check_flights(origin_city_code="LON",destination_city_code="TYO",from_date="15/09/2022",to_date="20/09/2022")
# if f.price < 10000:
#     print("Happy")