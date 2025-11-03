import requests

# create function to take topic, from date, to date. language set to English by default
def get_news(topic, from_date, to_date, lang='en'):
    # get api key from newsapi.org
    api = "ff08d95f4a3743f38370e51d2462ea10"
    # construct url with link and arguments
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={lang}&apiKey={api}'
    #request url dictionary
    r=requests.get(url)
    #convert object to json
    content =r.json()
    #check if content dictionary is created as date cannot be too far back
    print(content)
    # navigate into through dictionary to articles key
    articles = content['articles']
    # loop through the values and extracts the author for each article
    for article in articles:
        print(article['author'])


get_news("entertainment","2025-9-30","2025-9-31")