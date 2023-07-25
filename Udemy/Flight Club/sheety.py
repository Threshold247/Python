import os
import requests
from dotenv import load_dotenv
load_dotenv(".env")

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
USER_NAME = os.getenv("USER_NAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}
        self.username = USER_NAME
        self.password = USER_PASSWORD
        self.data_endpoint = "https://api.sheety.co/9c07c3a2fc7f67032e447624ddb97123/flightDeals/users"

    # def update_destination_codes(self):
    #     for city in self.data:
    #         data_to_add = {
    #             "price": {
    #                 "iataCode": city["iataCode"]
    #             }
    #         }
    #         response = requests.put(url=f"{self.data_endpoint}/{city['id']}", auth=(self.username, self.password),
    #                                 json=data_to_add)
    #         print(response.text)

    def add_user(self, first, last, email):
        data_to_add = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email
            }
        }
        response = requests.post(url=f"{self.data_endpoint}", auth=(self.username, self.password),
                                 json=data_to_add)
        print(response.text)

