import os
from datetime import datetime
import requests
from dotenv import load_dotenv
from pprint import pprint
load_dotenv(".env")

today = datetime.now()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}
        self.username = os.getenv("USER_NAME")
        self.password = os.getenv("USER_PASSWORD")
        self.data_endpoint = "https://api.sheety.co/9c07c3a2fc7f67032e447624ddb97123/flightDeals/prices"

    # This method pulls data from Sheety using the Api
    def get_sheet_data(self):
        response = requests.get(url=self.data_endpoint, auth=(self.username, self.password))
        response.raise_for_status()
        data = response.json()
        self.data = data['prices']
        pprint(data)
        return self.data

    # add iata codes for each county listed in sheety
    def update_destination_codes(self):
        for city in self.data:
            data_to_add = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.data_endpoint}/{city['id']}", auth=(self.username, self.password),
                                    json=data_to_add)
            print(response.text)

    # This method adds data to Sheety using the Api
    def add_data_to_sheet(self):
        pass
        # Read documentation to put data in sheet
        # price_data =   "price": {
        #         "lowestPrice": "1900"
        #     }
        # }
        # response = requests.put(url=f"{self.data_endpoint}/{self.data['city']['id']}",
        #                               auth=(self.username, self.password),json=price_data)
        # print(response.text)
