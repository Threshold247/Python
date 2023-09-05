from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

form_url = "http://secure-retreat-92358.herokuapp.com/"

driver.get(url=form_url)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("John")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Doe")
last_name.send_keys(Keys.ENTER)

email = driver.find_element(By.NAME, value="email")
email.send_keys("john.doe@gmail.com")
email.send_keys(Keys.ENTER)

submit_btn = driver.find_element(By.CLASS_NAME, value="btn btn-lg btn-primary btn-block")
submit_btn.click()
