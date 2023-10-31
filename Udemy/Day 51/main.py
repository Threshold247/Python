from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
load_dotenv(".env")

# setup Firefox options
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)
# open url
X_url = "https://twitter.com/i/flow/login"
driver.get(url=X_url)
# wait 3 seconds
time.sleep(3)


try:
    login_box = driver.find_element(By.XPATH, value="html/body/div/div/div/div[1]/div/div/div/div "
                                                    "/div/div/div[2]/div[2]/div/div/div[2]/"
                                                    "div[2]/div/div/div/div[5]/label/div/div[2]" 
                                                    "/div/input")

    login_box.send_keys(os.getenv("TWITTER_EMAIL"))
except NoSuchElementException:
    print("Could not find login element")
time.sleep(3)

try:
    next_btn = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]"
                                                   "/div/div/div[2]/div[2]/div/div/div/div[6]/div")
    next_btn.click()
except NoSuchElementException:
    print("Could not find btn element")

time.sleep(3)
try:
    password_input = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]"
                                                         "/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label"
                                                         "/div/div[2]/div[1]/input")
    password_input.send_keys(os.getenv("TWITTER_PASSWORD"))

except NoSuchElementException:
    print("Could not find password input box")
