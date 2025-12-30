from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from auth_manager import AuthManager
from notification_manager import NotificationManager
import os
from dotenv import load_dotenv

load_dotenv()

# Define Functions
def find_and_update_iat_codes(cities):
    for city in cities:
        try:
            city['iataCode']
        except KeyError:
            iataCode = search_flight.find_city_iata_code(city)
            city["iataCode"] = iataCode
            data.update_row(city_data=city, row=city['id'])

#Create objects
auth_manager = AuthManager(client_id=os.getenv("API_KEY"),client_secret=os.getenv("API_SECRET"),token_url=os.getenv("TOKEN_URL"))
auth_manager.authenticate()
# data = DataManager()
search_flight = FlightSearch(auth_manager)


#Start working with Data
# cities = data.get_city_list()
cities = [{'city': 'Ahmedabad', 'iataCode': 'AMD', 'lowestPrice': 10000, 'id': 2}]
find_and_update_iat_codes(cities)

flight_data_list = []
for city in cities:
    flight_data = FlightData(city_data=city, date='2026-02-13', auth_manager=auth_manager)
    flight_data_list.append(flight_data)
    print(flight_data.get_flight())
