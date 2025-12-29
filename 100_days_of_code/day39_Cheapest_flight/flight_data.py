import requests
import os
from dotenv import load_dotenv
from auth_manager import AuthManager

load_dotenv()
class FlightData:
    #This class is responsible for structuring the flight data.
    FLIGHT_DATA_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    def __init__(self,auth_manager:AuthManager, city_data, date):
        self.token = auth_manager.get_token()

        headers={
            "Authorization":f"Bearer {self.token}"
        }
        params = {
            "originLocationCode": "LON",
            "destinationLocationCode": city_data['iataCode'],
            "departureDate":'2026-02-13',
            "returnDate":'2026-02-28',
            'adults':'1',
            'max':'1'
        }
        self.response = requests.get(url=self.FLIGHT_DATA_ENDPOINT, params=params, headers=headers)

        self.flight =  self.response.json()["data"]['price']['total']