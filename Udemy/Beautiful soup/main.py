from bs4 import BeautifulSoup
import requests

# with open("website.html", mode="r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# anchor_tags = soup.select(selector="a")
# for item in anchor_tags:
#     print(item.get('href'))

url = "https://news.ycombinator.com/front"

resp = requests.get(url)
website = resp.text
soup = BeautifulSoup(website, "html.parser")

title_tag = soup.find(name="span", class_="titleline")
test = title_tag.find(name="a")
article_text = test.getText()
article_link = test.get("href")
article_vote = soup.find(name="span", class_="score").string


article_texts = []
article_links = []

titles_tag = soup.find_all(name="span", class_="titleline")
for article_tags in titles_tag:
    # get the text from the span tag
    article_texts.append(article_tags.getText())
    # drills further down to the anchor tag
    a_tags = article_tags.find("a")
    # extracts the href from the anchor tag
    article_links.append(a_tags.attrs.get("href"))

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# getting the highest/largest number in the list
highest_number = max(article_scores)
print(highest_number)
# getting index/position of the item in array
highest_index = (article_scores.index(highest_number))
print(highest_index)

# return article text, link with highest rank
print(article_texts[highest_index])
print(article_links[highest_index])
print(article_scores[highest_index])
