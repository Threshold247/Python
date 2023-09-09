from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

# store the url
cookie_url = "http://orteil.dashnet.org/experiments/cookie/"
# access the url
driver.get(url=cookie_url)
# find the cookie id
cookie_btn = driver.find_element(By.ID, value="cookie")
# find the money id
cookies_money = driver.find_element(By.ID, value="money").text
# list_of_upgrades = get the list of items prices on the right side panel
list = driver.find_elements(By.CSS_SELECTOR, value="#store div")
# list comprehension to create a list of ids
list_of_ids = [item.get_attribute("id") for item in list]

# find the upgrade ids
list_of_price_ids = driver.find_elements(By.CSS_SELECTOR, value="#store b")

list_of_prices = []
# create a list a new. go through the list and extract the text
for price in list_of_price_ids:
    convert_price = price.text
    # if the length of the price is equal to zero, exclude it.
    if len(convert_price) != 0:
        # split the text on "-", use the second part, strip the whitespace, replace the commas in the number and convert
        # an integer
        cost = int(convert_price.split("-")[1].strip().replace(",", ""))
        # add the elements to the empty list
        list_of_prices.append(cost)

# combine the 2 upgrade lists into a dictionary.
combined_dict = dict(zip(list_of_ids, list_of_prices))




# while True:
#     cookie_btn.click()
#     # timer = time.time() + 5

