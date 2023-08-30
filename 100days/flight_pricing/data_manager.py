import requests

sheety_endpoint="https://api.sheety.co/37064721d56e971c8b3ddbdca9c7090b/flightDeals/prices"

class DataManager:
    def __init__(self):
       self.destination_data={}

    def get_sheet(self):
        response=requests.get(sheety_endpoint,auth=("qwer","1234"))
        data=response.json()
        self.destination_data=data["prices"]
        return self.destination_data

    def update_sheet(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response=requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data, auth=("qwer", "1234"))
            print(response.text)

# print(DataManager().get_sheet())