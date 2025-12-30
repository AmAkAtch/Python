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
        self.headers={
            "Authorization":f"Bearer {self.token}"
        }
        self.params = {
            "originLocationCode": "LON",
            "destinationLocationCode": city_data['iataCode'],
            "departureDate":'2026-02-13',
            "returnDate":'2026-02-28',
            'adults':'1',
            'max':'1'
        }
        self.response = requests.get(url=self.FLIGHT_DATA_ENDPOINT, params=self.params, headers=self.headers)
        data = self.response.json()["data"][0]

        self.flight = {
            "offer_id": data["id"],
            "price": {
                "total": data["price"]["grandTotal"],
                "currency": data["price"]["currency"]
            },
            "seats_available": data["numberOfBookableSeats"],
            "itineraries": []
        }
        # Extract itineraries
        for idx, itinerary in enumerate(data["itineraries"]):
            segments = []
            for seg in itinerary["segments"]:
                segments.append({
                    "from": seg["departure"]["iataCode"],
                    "to": seg["arrival"]["iataCode"],
                    "departure": seg["departure"]["at"],
                    "arrival": seg["arrival"]["at"],
                    "airline": seg["carrierCode"],
                    "flight_number": seg["number"],
                    "duration": seg["duration"]
                })
            self.flight["itineraries"].append({
                "direction": "Outbound" if idx == 0 else "Return",
                "segments": segments
            })

    def get_flight(self):
        """Return the structured flight object"""
        return self.flight
