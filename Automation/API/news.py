import requests

# create function to take country and language set to English by default to access top headlines by country
def get_news(country,lang='en'):
    # get api key from newsapi.org
    api = "ff08d95f4a3743f38370e51d2462ea10"
    # construct url with link and arguments
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api}'
    #request url dictionary
    r=requests.get(url)
    #convert object to json
    content =r.json()
    print(content)
    # navigate into through dictionary to articles key
    articles = content['articles']
    # loop through the values and extracts the title for each article
    for article in articles:
        print(article['title'])


get_news("us")
