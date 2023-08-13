import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())


film_titles = soup.find_all(name="h3", class_="title")
my_list = [film.getText() for film in film_titles]
movie_list = my_list[::-1]


with open("movie_list.txt", mode="w") as file:
    for movie in movie_list:
        try:
            file.write(f"{movie}\n")
        except UnicodeError as e:
            print(e)
            continue

