from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

wiki_url = 'https://en.wikipedia.org/wiki/Main_Page'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=chrome_options)
driver.get(wiki_url)

articles_count = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]')

articles_count.click()


# Find element by Link Text

bots = driver.find_element(By.LINK_TEXT, value='Bots')
bots.click()


# Type something on a text box

search_bloom = driver.find_element(By.LINK_TEXT, value='Search')
search_bloom.click()

search_box = driver.find_element(By.NAME, value='search')
search_box.send_keys('Python')


# To hit a key

search_box.send_keys(Keys.ENTER)