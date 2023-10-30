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
# wait 3 seconds for window to render
time.sleep(3)
# find accept button
accept_btn = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")
# click on accept cookies button
accept_btn.click()

# find login button
login = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/"
                                            "div[2]/div[2]/a")
# click on login button
login.click()
# wait 5 seconds for window to render
time.sleep(5)

# click on google button
try:
    Google_button = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div[1]/div/div/div[2]'
                                                        '/div[2]/span/div[1]/div')
    # click on Google button
    Google_button.click()
    # wait 5 seconds for window to render
    time.sleep(5)
# if the element is not found
except NoSuchElementException:
    print("Error")

# Switching to different windows

# Main window
driver.switch_to.window(driver.window_handles[0])
# prints the title of the Main window
print("Main window title = " + driver.title)

# Second window
driver.switch_to.window(driver.window_handles[1])
# prints the title of the second window
print("Second window title = " + driver.title)
time.sleep(3)

try:
    Google_email = driver.find_element(By.ID, value="identifierId")
    Google_email.send_keys(os.getenv("EMAIL"))
except NoSuchElementException:
    print("Cannot find text box element")

try:
    next_btn = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]"
                                                   "/div/div[1]/div/div/button/span")
    next_btn.click()
except NoSuchElementException:
    print("Cannot find next button element")

