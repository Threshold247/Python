import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv(".env")

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("TWILIO_TOKEN")

class NotificationManager:
    # price_lower = False
    #
    # for data in flight_data:
    #
    #     if data["price"] < sheet_data["price"] :
    #         will_rain = True
    #
    # if price_lower:
    #     client = Client(account_sid, auth_token)
    #     message = client.messages.create(
    #         body="Bring an umbrella ☔",
    #         from_="+12705149754",
    #         to="+27679646165")
    #     print(message.status)
     pass