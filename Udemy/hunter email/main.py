import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")

URL = "https://api.hunter.io/v2/email-finder"
params = {
    "domain": "reddit.com",
    "first_name" : "Alexis",
    "last_name": "Ohanian",

}
header = {
    "X-API-KEY": os.getenv("HUNTER_API")
}

response = requests.get(url=URL, params=params, headers=header)
response.raise_for_status()
data = response.json()
print(data["data"]["email"])