import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv(".env")

TWILIO_ACCOUNT_SID = os.getenv("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_TOKEN")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+12705149754",
            to="+27679646165")
        print(message.sid)
