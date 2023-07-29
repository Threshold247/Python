from pprint import pprint
import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")

BASE_URL = "https://api.sheety.co/"
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
PROJECT = "flightDeals"
SHEET = "prices"
SHEETY_PRICES_ENDPOINT = f"{SHEETY_TOKEN}/{PROJECT}/{SHEET}"
URL = BASE_URL+SHEETY_PRICES_ENDPOINT
USER_NAME = os.getenv("USER_NAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=URL, auth=(USER_NAME, USER_PASSWORD))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{URL}/{city['id']}",
                json=new_data
            )
            print(response.text)
