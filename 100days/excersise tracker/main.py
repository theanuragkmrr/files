import requests
from datetime import datetime


APIKEY = "058ad31c8d12123d7f36b55b9ea23ae1"
APPID = "478a1777"

sheet_endpoint="https://api.sheety.co/37064721d56e971c8b3ddbdca9c7090b/myWorkouts/workouts"
exe_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
exe_text= input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APPID,
    "x-app-key": APIKEY,
}

params={
 "query":exe_text,
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":22
}


response=requests.post(exe_endpoint,json=params,headers=headers)
result=response.json()
print(result)

TODAY=datetime.now().strftime("%d/%m/%Y")
time_now=datetime.now().strftime("%X")


for exe in result["exercises"]:

    sheety_params={
        "workout":
            {
                "date": TODAY,
                "time": time_now,
                "exercise": exe["name"].title(),
                "duration": exe["duration_min"],
                "calories": exe["nf_calories"],

            }


    }
    sheet_res=requests.post(sheet_endpoint,json=sheety_params,auth=("hello","hellohaipass"))

    print(sheet_res.text)