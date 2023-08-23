from bs4 import BeautifulSoup
import cloudscraper
import requests

scraper = cloudscraper.create_scraper()

# config = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image "
#               "/ avif, image / webp, * / *;q = 0.8",
#     "Accept-Encoding": "gzip, deflate, br"
# }

URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = scraper.get(url=URL)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="aok-offscreen").getText()
print(price)
new_price = price.split("$")
convert_price = float(new_price[1])
print(convert_price)
