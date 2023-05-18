import requests
from twilio.rest import Client

# use api key from open weather
my_api = "1f37375e6fbcffa4d75dfe1e7c7cb27a"
# create variable to store api url
OWA = "https://api.openweathermap.org/data/2.5/forecast"
# parameters for the Clinet
account_sid = "AC8e378b769f646cdbca7253c818014f1b"
auth_token = "8e76a5f5a04b44f9b9ebb2feb8edb550"
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