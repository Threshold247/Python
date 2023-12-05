from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


# create a class
class InternetBot:
    # add attributes to class
    def __init__(self):
        firefox_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(
            options=firefox_options)
        self.up = 0
        self.down = 0

    # add a method to get internet speed from specific url
    def get_internet_speed(self, url):
        self.driver.get(url=url)
        # wait 30 secs
        time.sleep(30)
        # find GO button and click on button
        try:
            go_btn = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]"
                                                              "/div[3]/div[1]/a")
            go_btn.click()
            print("go button clicked")
        except NoSuchElementException:
            print("Error cannot find go button")
        # indicate that the webscraper is waiting 50 seconds
        print("Waiting for 50 secs for test to run")
        time.sleep(50)
        # find the download speed element and extract the text attribute
        try:
            download_speed = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]"
                                                                      "/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]"
                                                                      "/div[1]/div/div[2]/span")
            print(f"download speed element found")
            self.down = download_speed.text
            print(self.down)
        except NoSuchElementException:
            print("Could not find download element")

        # find the upload speed element and extract the text attribute
        try:
            upload_speed = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]"
                                                                    "/div[3]/div[3]/div/div[3]/div/div/div[2]/"
                                                                    "div[1]/div[2]/div/div[2]/span")
            print(f"download speed element found")
            self.up = upload_speed.text
            print(self.up)
        except NoSuchElementException:
            print("Could not find upload element")

    def tweet_at_provider(self, down, up):
        pass


