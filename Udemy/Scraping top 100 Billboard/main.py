import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
load_dotenv(".env")


SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_PASSWORD")
SPOTIFY_USERNAME = os.getenv("SPOTIFY_DISPLAY_NAME")
SPOTIFY_URL = "https://api.spotify.com"

sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            show_dialog=True,
            redirect_uri="http://example.com",
            scope="playlist-modify-private",
            cache_path="token.txt"
        )
)
user_id = sp.current_user()["id"]

user_input = input("Year you would like to travel to? Type in a date using this format: YYYY-MM-DD ")
URL = f"https://www.billboard.com/charts/hot-100/{user_input}"

# for test purposes
# TEST_URL = "https://www.billboard.com/charts/hot-100/2020-01-01"

response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

h3_element = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
# OR use the select method
h3_element_select = soup.select("li ul li h3")

# list comprehension
# get the text and strip the whitespace from each h3 element.
my_list = [text.getText().strip() for text in h3_element]

# checks the index of each song, adds the index+1 to each song and creates a list
# billboard = [f"{my_list.index(songs)+1}. {songs}" for songs in my_list]
# print(billboard)

# gets the year from the user input
track_year = user_input.split("-")[0]

# create a track_uri list
song_uri = []

for track in my_list:
    # search through the tracks and return the uri for each track
    result = sp.search(q=f"track:{track} year:{track_year}", type="track")
    try:
        uris = result["tracks"]["items"][0]["uri"]
        song_uri.append(uris)
    except IndexError:
        print(f"{track} not found on Spotify ")

print(song_uri)

# Create a spotify playlist
USER_ID = os.getenv("USER_ID")
# Create a playlist object from the spotify object
playlist = sp.user_playlist_create(user=USER_ID, name=f"{user_input} Billboard 100", public=False,
                                   description="Playlist containing top 100 songs for a specific year")
# Store the playlist id in a variable
playlist_id = playlist["uri"]
# add tracks to the playlist
add_songs_to_playlist = sp.playlist_add_items(playlist_id=playlist_id, items=song_uri, position=None)
