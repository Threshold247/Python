from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
load_dotenv(".env")

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)
t_url = "https://www.tinder.com"

driver.get(url=t_url)
time.sleep(3)
accept_btn = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")
accept_btn.click()

login = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/"
                                            "div[2]/div[2]/a")
login.click()
time.sleep(5)


try:
    Google_button = driver.find_element(By.XPATH, value='//*[@id="c615667929"]')
    Google_button.click()
    time.sleep(5)
except NoSuchElementException:
    print("Error")

try:
    Google_email = driver.find_element(By.ID, value="identifierId")
    # Google_email.send_keys(f"")
except NoSuchElementException:
    print("Cannot find text box element")
