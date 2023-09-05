from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

python_url = "https://python.org"

driver.get(url=python_url)
upcoming_events = driver.find_elements(By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")

my_time = []
my_name = []
for item in upcoming_events:
    test_split = item.text.split("\n", maxsplit=1)
    my_time.append(test_split[0])
    my_name.append(test_split[1])

my_dict = dict(zip(my_time, my_name))

events = {}
count = -1
for (key, value) in my_dict.items():
    count+=1
    events[count] = {
        "time": key,
        "name": value
    }
print(events)

driver.close()
