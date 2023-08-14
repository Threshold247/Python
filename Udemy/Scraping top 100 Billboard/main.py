from bs4 import BeautifulSoup
import requests

# user_input = input("Year you would like to travel to? Type in a date using this format: YYY-MM-DD ")
# URL = f"https://www.billboard.com/charts/hot-100/{user_input}"
# print(URL)
TEST_URL = "https://www.billboard.com/charts/hot-100/2020-01-01"

response = requests.get(TEST_URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

h3_element = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
h3_element_top = soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").getText().strip()

# list comprehension
# get the text and strip the whitespace from each h3 element. only returns 2-100 titles
my_list = [text.getText().strip() for text in h3_element]

# insert the no 1 ranked song into the list
my_list.insert(0, h3_element_top)

# checks the index of each song, adds the index+1 to each song and creates a list
billboard = [f"{my_list.index(songs)+1}. {songs}" for songs in my_list]

# for loop to count each element in the list. append the count + each song title
# count = 0
# for songs in my_list:
#     count += 1
#     billboard.append(f"{count}. {songs}")

print(billboard)


