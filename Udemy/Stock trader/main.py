import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv(".env")


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "5min",
    "apikey": os.getenv("STOCK_API_KEY")
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": os.getenv("NEWS_API_KEY")
}
auth_token = os.getenv("TWILIO_TOKEN")
account_sid = os.getenv("TWILIO_SID")
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python
#  dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# create response
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
# raise status if unsuccessful
response.raise_for_status()
# convert data to json, access the Time series key and value
stock_data = response.json()["Time Series (5min)"]
# create list comprehension to make it easier to navigate
time_series = [value for (key, value) in stock_data.items()]
yesterday_closing_stock_price = float(time_series[0]["4. close"])
print(yesterday_closing_stock_price)


# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_stock_price = float(time_series[-1]["4. close"])


# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive
#  difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(day_before_yesterday_stock_price-yesterday_closing_stock_price)


# TODO 4. - Work out the percentage difference in price between closing price yesterday
#  and closing price the day before yesterday.
percentage_diff = float((diff/yesterday_closing_stock_price)*100)
print(percentage_diff)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff > 0:
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()
    news_data = response.json()['articles']
    articles = news_data

    first_three_articles = articles[3:6]


# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
#  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# brief : Headline: Article title: n\Brief description
new_list = [f"Headline: {article['title']},\nBrief {article['description']}" for article in first_three_articles]
print(new_list)

# TODO 9. - Send each article as a separate message via Twilio.
client = Client(account_sid, auth_token)
for article in new_list:
    message = client.messages.create(
        body=f"{article}\n",
        from_="+12705149754",
        to="+27679646165")
    print(message.status)


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

