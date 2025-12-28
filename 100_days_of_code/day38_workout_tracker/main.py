import requests
from datetime import datetime

APPID= "app_d40a4a8efee14ef88c7b91a1"
APPKEY= "nix_live_KeCwUF70OP3EtuehIo1Wvr11fZXvtL0v"
BASE_API_URL="https://app.100daysofpython.dev"
SHEETY_ENDPOINT = "https://api.sheety.co/44fe9665755c4d5ac9900bc2f90dfa2d/workoutTracking/workouts"
TOKEN = "Bearer dsdfsjklfsdjfhsk;dj;kfsk;hds"

HEADERS = {
    "x-app-id": APPID,
    "x-app-key": APPKEY,
}

SHEETY_HEADER = {
    "Authorization":TOKEN
}

params = {
  "query": input("Enter your Workout and Duration: "),
  "weight_kg": 77,                  
  "height_cm": 177,                 
  "age": 26,                        
  "gender": "male"
}

response = requests.post(url=f"{BASE_API_URL}/v1/nutrition/natural/exercise", json=params, headers=HEADERS)
data = response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

print(data["exercises"])
exercise = data["exercises"][0]["name"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

sheety_params = {
    "workout":{
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
        }
}

sheety_response = requests.post(url=f"{SHEETY_ENDPOINT}", json=sheety_params, headers=SHEETY_HEADER)