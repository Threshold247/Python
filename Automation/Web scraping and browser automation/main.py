from selenium import webdriver
from selenium.webdriver.firefox.options import Options

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

def main():
    driver=get_driver()
    element=driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    print(element.text)
    driver.quit()

main()

# # Close the browser
# driver.quit()