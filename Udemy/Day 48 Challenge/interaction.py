from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(
    options=firefox_options
)

Wiki_url = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(url=Wiki_url)
# find article count using Xpath
articles = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[3]/main/div[3]/div[3]"
                                               "/div[1]/div[1]/div/div[3]/a[1]")
# find article count using CSS selector
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# clicking on a link
# article_count.click()

# content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()
search_bar = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)


