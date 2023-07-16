import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
load_dotenv(".env")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        today = datetime.now()
        current_date = today.strftime("%d/%m/%Y")
        new_day = today.replace(day=16, month=7)
        return_date = new_day.strftime("%d/%m/%Y")
        # print(f"Current Date:{current_date}")
        # print(f"Return Date:{return_date}")
        self.flight_url = "https://api.tequila.kiwi.com/v2/search"
        self.params = {
            "fly_from": "CPT",
            "fly_to": "HND",
            "date_from": current_date,
            "date_to": return_date,
            "curr": "ZAR"
        }
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
        print(f"data:{data}")
        code = (data[0]["code"])
        print(f"code:{code}")
        return code

    def get_flight_data(self):
        response = requests.get(url=self.flight_url, params=self.params, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        pprint(data)
