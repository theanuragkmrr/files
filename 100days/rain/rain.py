import requests

api_key="14fa8649fd5577a30f0eb15afc0f1f1c"


weather={
    "lat":51.51,
    "lon":-0.13,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}


response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=weather)
response.raise_for_status()
data=response.json()
print(data)






