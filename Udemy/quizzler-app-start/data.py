# add api
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
# create response from request library
response = requests.get("https://opentdb.com/api.php", params=parameters)
# check status
response.raise_for_status()
# store json in variable
test_data = response.json()

question_data = test_data['results']
