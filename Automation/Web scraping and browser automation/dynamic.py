from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

#set up function
def get_driver():
    options= Options()
    options.add_argument("disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("disable-blink-features=AutomationControlled")


    # Set up the Firefox WebDriver using geckodriver
    driver = webdriver.Firefox(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def split_text(text):
    """Cleans up the output because we could not grab the value directly from the website"""
    output = text.split(": ")
    return float(output[1])

def main():
    driver=get_driver()
    time.sleep(2)
    element=driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    #Use a function to clean up the output, in this case the element
    print(split_text(element.text))
    driver.quit()

main()

# # Close the browser
# driver.quit()