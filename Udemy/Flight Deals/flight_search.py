from flight_data import FlightData
import os
import requests
from dotenv import load_dotenv
load_dotenv(".env")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_url = "https://api.tequila.kiwi.com/v2/search"
        self.headers = {
            "apikey": os.getenv("KIWI_TOKEN"),
            "Content-Type": "application/json"
        }

    def get_country_code(self, city_name):
        flight = "https://api.tequila.kiwi.com/locations/query"
        query = {
            "term": city_name,
            "location_types": "city",
            "active_only": "true"
        }
        response = requests.get(url=flight, params=query, headers=self.headers)
        response.raise_for_status()
        data = response.json()['locations']
        # print(f"data:{data}")
        code = (data[0]["code"])
        # print(f"code:{code}")
        return code

    def get_flight_data(self, departure_city_code, arrival_city_code, date_from, date_to):
        query = {
            "fly_from": departure_city_code,
            "fly_to": arrival_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "ZAR"
        }
        response = requests.get(url=self.flight_url, params=query, headers=self.headers)
        response.raise_for_status()

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {arrival_city_code}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            departure_city=data['route'][0]["cityFrom"],
            departure_airport=data['route'][0]["flyFrom"],
            destination_city=data['route'][0]["cityTo"],
            destination_airport=data['route'][0]["flyTo"],
            out_date= data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0]
        )
        print(f"Flight Alert! Pay R{flight_data.price} to fly from {flight_data.departure_city}-{departure_city_code} "
              f"to{flight_data.destination_city}-{arrival_city_code} from {flight_data.out_date} "
              f"to {flight_data.return_date}")
        return flight_data
