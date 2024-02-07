import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv("test.env")

# use api key from open weather
my_api = os.getenv("OWA_API_KEY")
# create variable to store api url
OWA = "https://api.openweathermap.org/data/2.5/forecast"
# parameters for the Client
account_sid = os.getenv("account_sid")
auth_token = os.getenv("TWILIO_TOKEN")
# create variable to store longitude
MY_LONG = 18.4232
# create variable to store latitude
MY_LAT = -33.9258
# create parameter variable to add to the end of the request
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 7,
    "appid": my_api,
    "formatted": 0
}

response = requests.get(url=OWA, params=parameters)
response.raise_for_status()
data = response.json()


weather_data = data["list"]

will_rain = False

for weather_id in weather_data:
    item_id = weather_id['weather'][0]['id']
    if item_id < 800:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella ☔",
        from_="+12705149754",
        to="+27679646165")
    print(message.status)

