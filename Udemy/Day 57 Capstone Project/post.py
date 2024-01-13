import requests


# create a class which gets a response from an api.
class Post:
    def __init__(self, url):
        self.data = requests.get(url=url)
        response = self.data.json()
        # generate a list from the key called data, access the value which is a list
        self.list = response['data']


