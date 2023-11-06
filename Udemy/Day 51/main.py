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

# Exercise 1 Login to Twitter

# open url
X_url = "https://twitter.com/i/flow/login"
driver.get(url=X_url)
# wait 10 seconds
time.sleep(10)

# complete login screen
try:
    # find email address text box element
    login_box = driver.find_element(By.XPATH, value="html/body/div/div/div/div[1]/div/div/div/div "
                                                    "/div/div/div[2]/div[2]/div/div/div[2]/"
                                                    "div[2]/div/div/div/div[5]/label/div/div[2]"
                                                    "/div/input")
    # enter email address
    login_box.send_keys(os.getenv("TWITTER_EMAIL"))
except NoSuchElementException:
    print("Could not find login element")
# wait 5 secs
time.sleep(5)

# find next button element and click on it
try:
    next_btn = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]"
                                                   "/div/div/div[2]/div[2]/div/div/div/div[6]/div")
    next_btn.click()
except NoSuchElementException:
    print("Could not find btn element")
# wait 5 secs
time.sleep(5)

# enter password into password input text box and click on next btn
try:
    password_input = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]"
                                                         "/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label"
                                                         "/div/div[2]/div[1]/input")
    password_input.send_keys(os.getenv("TWITTER_PASSWORD"))
    password_next_btn = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/"
                                                            "div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]"
                                                            "/div/div/div")
    password_next_btn.click()
except NoSuchElementException:
    print("Could not find password input box")
