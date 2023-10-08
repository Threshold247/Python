from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

form_url = "http://secure-retreat-92358.herokuapp.com/"

driver.get(url=form_url)

# Enter text in the First Name text box and submit
first_name = driver.find_element(By.NAME, value="fName")  # find the element
first_name.send_keys("John")  # enter the text in box

# Enter text in the Last Name text box and submit
last_name = driver.find_element(By.NAME, value="lName")  # find the element
last_name.send_keys("Doe")  # enter the text in box


# Enter text in the email address text box and submit using a chaining method
driver.find_element(By.NAME, value="email").send_keys("john.doe@gmail.com")

# click on the submit button
driver.find_element(By.CSS_SELECTOR, value=".btn").click()

driver.quit()
