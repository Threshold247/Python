from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv(".env")

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

linkedIn_url = ("https://www.linkedin.com/jobs/search/?currentJobId=3725795875&f_AL=true&f_WT=2&geoId=104035573"
       "&keywords=python%20engineer&location=South%20Africa&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

driver.get(url=linkedIn_url)

# STEP 2

# find sign in button element
sign_in = driver.find_element(By.XPATH, "/html/body/div[4]/a[1]")
# wait 3 secs for the sign in button to appear
time.sleep(3)
# click on the sign in button
sign_in.click()

# fill out the sign in prompt
# waits for the prompt to appear
time.sleep(3)
# find the email element
email = driver.find_element(By.ID, "username")
# fill out the email element
email.send_keys(os.getenv("EMAIL"))
# find the password element
password = driver.find_element(By.ID, "password")
# fill out the password element
password.send_keys(os.getenv("PASSWORD"))
# find the sign in button
sign_in_btn = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
# click on the button to login
sign_in_btn.click()
print("Sign in success!")

# STEP 3 Find the first job and apply by adding a telephone number

