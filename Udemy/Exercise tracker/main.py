import os
from datetime import datetime
from dotenv import load_dotenv
import requests
load_dotenv(".env")


today = datetime.now()
username = os.getenv("USER_NAME")
password = os.getenv("USER_PASSWORD")
DATA_ENDPOINT = "https://api.sheety.co/9c07c3a2fc7f67032e447624ddb97123/myWorkoutsApplication/workouts"
# Setup headers
headers = {
    "x-app-id": os.getenv("NUTRITIONX_ID"),
    "x-app-key": os.getenv("NUTRITIONX_KEYS")
}
# generates data for user for each exercise
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
        "query": input("Which exercises did you do?"),
        "gender": "male",
        "weight_kg": 81,
        "height_cm": 181,
        "age": 45
        }
response = requests.post(url=exercise_url, json=params, headers=headers)
response.raise_for_status()
result = response.json()


# read data from sheet

# test = requests.get(url=DATA_ENDPOINT, auth=(username, password))
# data = test.json()
# print(data)

# add data to sheet go through the list of dictionaries and get the values of each key.
for exercise in result['exercises']:
    data = {
       "workout": {
                "date": today.strftime("%m/%d/%Y"),
                "time": today.strftime("%H:%M:%S"),
                "exercise": exercise['name'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories'],
                "id": 4
            }
    }
    response = requests.post(url=DATA_ENDPOINT, json=data, auth=(username, password))
    response.raise_for_status()

