import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getcwd())


APPID= os.getenv("APPID")
APPKEY= os.getenv("APPKEY")
BASE_API_URL=os.getenv("BASE_API_URL")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
TOKEN = os.getenv("TOKEN")

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