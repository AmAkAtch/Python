import requests

LAT = -8.340539
LON = 115.091949
API_KEY = ""
URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat":LAT,
    "lon":LON,
    "appid":API_KEY,
    "cnt":4
}

response = requests.get(URL, params=parameters).json()["list"]

for timestamp in response:
    current_condition = timestamp['weather'][0]['id']
    if current_condition < 700:
        print(timestamp['dt_txt'] + " Bring out umbrella - Rain expected ")
