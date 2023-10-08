from selenium import webdriver
from selenium.webdriver.common.by import By
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
# list_of_upgrades = get the list of items prices on the right side panel
list = driver.find_elements(By.CSS_SELECTOR, value="#store div")
# list comprehension to create a list of ids
list_of_ids = [item.get_attribute("id") for item in list]


timeout = time.time() + 5
five_min = time.time() + (60*5) # 5minutes

while True:

    cookie_btn.click()

    if time.time() > timeout:

        # check which upgrades can be bought
        list_of_prices = []
        # create a list. go through the list and extract the text
        # find the upgrade ids
        list_of_price_ids = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        for price in list_of_price_ids:
            convert_price = price.text
            # if the length of the price is equal to zero, exclude it.
            if convert_price != "":
                # split the text on "-", use the second part, strip the whitespace,
                # replace the commas in the number and convert to an integer
                cost = int(convert_price.split("-")[1].strip().replace(",", ""))
                # add the elements to the empty list
                list_of_prices.append(cost)
        # find the money id and get the cookie count
        cookies_money = driver.find_element(By.ID, value="money").text
        if "," in cookies_money:
            cookies_money = cookies_money.replace(",", "")
        cookie_cost = int(cookies_money)

        # combine the 2 upgrade lists into a dictionary.
        combined_dict = dict(zip(list_of_ids, list_of_prices))

        cookie_upgrades = {}
        for ids, prices in combined_dict.items():
            if cookie_cost > prices:
                cookie_upgrades[prices] = ids
        print(cookie_upgrades)
        # Purchase the most expensive affordable upgrade
        upgrade_list = sorted(cookie_upgrades)
        print(upgrade_list[-1])

        purchase_id = cookie_upgrades[upgrade_list[-1]]
        print(purchase_id)

        driver.find_element(By.ID, value=purchase_id).click()

        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    # if time.time() > five_min:
    #     cookie_per_s = driver.find_element(By.ID, value="cps").text
    #     print(cookie_per_s)
    #     break
