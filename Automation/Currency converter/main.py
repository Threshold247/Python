from bs4 import BeautifulSoup
import requests


def get_currency(from_currency,to_currency,amount):
    url = f"https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount={amount}"
    content = requests.get(url).text
    soup=BeautifulSoup(content,"html.parser")
    rate=soup.find("span", class_="ccOutputRslt").get_text()
    rate=float(rate[:-4])
    return rate

from_currency=input("From which currency: ")
to_currency=input("To which currency: ")
amount=input("How much do you want to convert: ")
print(get_currency(from_currency=from_currency,to_currency=to_currency,amount=amount))