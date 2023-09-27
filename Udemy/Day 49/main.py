from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv(".env")

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

linkedIn_url = ("https://www.linkedin.com/jobs/search/?currentJobId=3725795875&f_AL=true&f_WT=2&geoId=104035573"
                "&keywords=python%20engineer&location=South%20Africa&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE"
                "&refresh=true")

driver.get(url=linkedIn_url)

# STEP 2

# find sign in button element
sign_in = driver.find_element(By.XPATH, "/html/body/div[4]/a[1]")
# wait 3 secs for the sign-in button to appear
time.sleep(5)
# click on the sign-in button
sign_in.click()

# fill out the sign-in prompt
# waits for the prompt to appear
time.sleep(5)
# find the email element
email = driver.find_element(By.ID, "username")
# fill out the email element
email.send_keys(os.getenv("EMAIL"))
# find the password element
password = driver.find_element(By.ID, "password")
# fill out the password element
password.send_keys(os.getenv("PASSWORD"))
# find the sign-in button
sign_in_btn = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
# click on the button to login
sign_in_btn.click()
print("Sign in success!")

# STEP 3 Find the first job and apply by adding a telephone number
# wait  5 secs for prompt to appear
time.sleep(5)
# find the first job on the list
first_job_ele = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/"
                                              "li[1]/div")
# select the the element
first_job_ele.click()
# wait 3 seconds for the job to appear
time.sleep(3)
# find easy apply button element
easy_apply_btn = driver.find_element(By.CLASS_NAME, value= "jobs-apply-button--top-card")
# click on the easy apply button
easy_apply_btn.click()
# wait 5 seconds
time.sleep(5)
# find the mobile number text input box
mobile_number = driver.find_element(By.CLASS_NAME, value="artdeco-text-input--input")
# enter a number in the mobile text field
mobile_number.send_keys("0219000000")

# find the Apply button element
next_btn = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]"
                                                    "/button/span")
# click on the Bext button
next_btn.click()
# wait 5 seconds
time.sleep(5)
# click on the Next button again
next_btn.click()

# find the Cancel button element
cancel_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/button/li-icon")
# click the Cancel button
cancel_button.click()
# wait 3 seconds
time.sleep(3)

# find the Discard button element
discard_btn = driver.find_element(By.XPATH, value="/html/body/div[3]/div[2]/div/div[3]/button[1]")
# click on the Discard button
discard_btn.click()
