import requests
import os
from dotenv import load_dotenv

load_dotenv()
class DataManager:
    #This class is responsible for talking to the Google Sheet
    SHEETY_GET_ENDPOINT = "https://api.sheety.co/44fe9665755c4d5ac9900bc2f90dfa2d/flightDeals/prices"
    SHEETY_PUT_ENDPOINT = "https://api.sheety.co/44fe9665755c4d5ac9900bc2f90dfa2d/flightDeals/prices/"
    TOKEN = os.getenv("SHEETY_TOKEN")
    HEADERS = {
        "Authorization":TOKEN
    }

    def __init__(self):
        self.response = requests.get(url=self.SHEETY_GET_ENDPOINT, headers=self.HEADERS).json()
        print(self.response)
        self.list_of_cities = self.response['prices']
        
    def get_city_list(self):
        return self.list_of_cities
    
    def update_row(self,city_data, row):
        body = {
            "price": {
                'iataCode':city_data['iataCode'],  
            }
        }
        self.response = requests.put(url=f"{self.SHEETY_PUT_ENDPOINT}{row}", json=body, headers=self.HEADERS)