import requests
from datetime import datetime
import os
# allows to load environment variables from a file
from dotenv import load_dotenv
load_dotenv(".env")


USER_TOKEN = os.getenv("PIXELA_TOKEN")
USER_NAME = os.getenv("PIXELA_USER")
GRAPH_NAME = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# create user and token profile
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/"
graph_params = {
    "id": "testgraph",
    "name": "habit_tracker",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": USER_TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# delete a graph
# graph_delete_endpoint = f"https://pixe.la/v1/users/shaunt/graphs/testgraph"
# response = requests.delete(url=graph_delete_endpoint,headers=headers)
# print(response.text)
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)



# create a pixel in graph
today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_NAME}"
pixel_config = {
    # use sfrftime to formate date.
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many commits did you do today?"),
}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# update a pixel in graph (choose the correct day to update)
update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_NAME}/{today.strftime('%Y%m%d')}"
pixel_update = {
    "quantity": "2",
}
response = requests.post(url=pixel_endpoint, json=pixel_update, headers=headers)
print(response.text)



