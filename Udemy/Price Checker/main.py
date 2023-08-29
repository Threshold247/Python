from bs4 import BeautifulSoup
import requests
from price_mailer import EmailNotify


email_price = EmailNotify()

config = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br"
}

TARGET_PRICE = 3000
TEST_URL = "https://www.loot.co.za/product/instant-pot-duo-plus-9in1-smart-cooker-6l/kjhs-7284-gaa0"
response = requests.get(url=TEST_URL, headers=config)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())
price = soup.select(selector="div div span span span")[-5].getText()

# replace comma in string and convert to an integer
new_price = int(price.replace(",", ""))
print(new_price)

email_notify = EmailNotify()
# checks if website prices is less than target price
if new_price < TARGET_PRICE:
    # runs the notify email method which takes 2 arguments
    email_notify.send_email(price=new_price, url=TEST_URL)
