import requests
import os
from dotenv import load_dotenv
from auth_manager import AuthManager

load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    CITY_SEARCH_ENDPOINT = os.getenv("CITY_SEARCH_ENDPOINT")

    def __init__(self, auth_manager:AuthManager):
        self.token = auth_manager.get_token()

    def find_city_iata_code(self, city:dict):
        headers={
            "Authorization":f"Bearer {self.token}"
        }
        city_search_params = {
            "keyword":city['city'],
            "max":"1" 
        }
        self.city_response = requests.get(url=self.CITY_SEARCH_ENDPOINT, params=city_search_params, headers=headers)
        print(self.city_response.text)
        return self.city_response.json()['data'][0]['iataCode']
