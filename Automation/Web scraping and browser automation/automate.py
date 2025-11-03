
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

#set up function
def get_driver():
    options= Options()
    options.add_argument("disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("disable-blink-features=AutomationControlled")


    # Set up the Firefox WebDriver using geckodriver
    driver = webdriver.Firefox(options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def split_text(text):
    """Cleans up the output because we could not grab the value directly from the website"""
    output = text.split(": ")
    return float(output[1])

def write_file(text):
    #creates a file name based on a date and time
    current_date= datetime.now().strftime('%Y-%m-%d-%H.%M.%S')
    filename =  f"{current_date}.txt"
    print(filename)
    with open(filename, "w") as f:
         f.write(text)


def main():
    driver=get_driver()
    time.sleep(2)
    # finds the user input element
    driver.find_element(by="id", value="id_username").send_keys("automated")
    # finds the password input element
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+ Keys.RETURN)
    time.sleep(2)
    #selects the home element and clicks on it.
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    # create a loop that runs 5 times
    count = 0
    while count<5:
        count+=1
        print(count)
        time.sleep(5)
        #scrape the element
        element=driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        #Use the split text function to clean up the output, in this case the element
        output =str(split_text(element.text))
        # run the write function to create the file name and write the output to the file
        write_file(output)
    driver.quit()

main()

