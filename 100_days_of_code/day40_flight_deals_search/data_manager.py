import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/44fe9665755c4d5ac9900bc2f90dfa2d/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/44fe9665755c4d5ac9900bc2f90dfa2d/flightDeals/users"


class DataManager:

    def __init__(self):
        self._token = os.getenv("SHEETY_TOKEN")
        self.destination_data = {}
        self.users_data = {}
        self.headers = {
            "Authorization":self._token
        }

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_users_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        self.users_data = data["users"]
        return self.users_data

    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)
