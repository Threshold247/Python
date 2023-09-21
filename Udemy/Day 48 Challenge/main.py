from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

python_url = "https://python.org"

driver.get(url=python_url)

# get a list of the event date text
event_date = [item.text for item in driver.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/"
                                                                         "div[2]/div/ul/li/time")]
# get a list of the event description text
event_name = [item.text for item in driver.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/"
                                                                         "div[2]/div/ul/li/a")]
# combine the lists and create a dictionary
my_dict = dict(zip(event_name, event_date))

events = {}
count = -1
for (key, value) in my_dict.items():
    count += 1
    # create a dictionary with the key is the count+1 and the value is the key,value pair of my_dict
    events[count] = {
        "time": value,
        "name": key
    }
print(events)

driver.close()
