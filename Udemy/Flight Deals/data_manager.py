import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv(".env")

today = datetime.now()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = ''
        self.country_id = ''
        self.username = os.getenv("USER_NAME")
        self.password = os.getenv("USER_PASSWORD")
        self.data_endpoint = "https://api.sheety.co/9c07c3a2fc7f67032e447624ddb97123/flightDeals/prices"
        self.data_to_add = {
            "price": {
                "lowestPrice": "1900"
            }
        }

    # This method pulls data from Sheety using the Api
    def get_sheet_data(self):
        response = requests.get(url=self.data_endpoint, auth=(self.username, self.password))
        response.raise_for_status()
        self.data = response.json()['prices']
        data = self.data
        for country in data:
            print(country)

    # This method adds data to Sheety using the Api
    def add_data_to_sheet(self, sheet_id):
        # Read documentation to put data in sheet
        response = requests.put(url=f"{self.data_endpoint}/{sheet_id}", auth=(self.username, self.password),
                                json=self.data_to_add)
        print(response.text)



