import requests

# use api key from open weather
my_api = "1f37375e6fbcffa4d75dfe1e7c7cb27a"
# create variable to store api url
OWA = "https://api.openweathermap.org/data/2.5/forecast"
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
    print("Bring an umbrella")
