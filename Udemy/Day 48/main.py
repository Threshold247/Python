from selenium import webdriver
from selenium.webdriver.common.by import By


firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

# driver.get("https://www.loot.co.za/product/instant-pot-duo-plus-9in1-smart-cooker-6l/kjhs-7284-gaa0")
# price = driver.find_element(By.CLASS_NAME, value="price").text
# print(price)
# driver.quit()

amazon_url = ("https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG/ref=sr_1_3?"
              "keywords=instant%2Bpot&qid=1693809339&sprefix=Instant%2BPo%2Caps%2C358&sr=8-3&th=1")
driver.get(amazon_url)
# dollar_price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# dollar_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The full price is ${dollar_price}.{dollar_fraction}")
path_dir = driver.find_element(By.CSS_SELECTOR, value=".navFooterMoreOnAmazon > tbody:nth-child(1) "
                                                      ">tr:nth-child(9) > td:nth-child(7) > a:nth-child(1)")

print(path_dir.text)
driver.close()
