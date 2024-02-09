from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

test_url = 'https://secure-retreat-92358.herokuapp.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=chrome_options)
driver.get(test_url)

first_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
first_name.send_keys('Enzo')

last_name = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
last_name.send_keys('Leal')

email_add = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
email_add.send_keys('enzosilva142002@gmail.com')

sign_up_button = driver.find_element(By.XPATH, value='/html/body/form/button')
sign_up_button.send_keys(Keys.ENTER)