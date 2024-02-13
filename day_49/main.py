from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

linkedin_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3787106406&distance=25&f_AL=true&geoId=104263468&keywords=python%20developer&location=Salvador%2C%20Bahia%2C%20Brasil&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=chrome_options)
driver.get(linkedin_url)

sleep(2)

login_buttom = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
login_buttom.click()

email_box = driver.find_element(By.XPATH, value='/html/body/div/main/div[2]/div[1]/form/div[1]/input')
email_box.send_keys('email')

pasw_box = driver.find_element(By.XPATH, value='/html/body/div/main/div[2]/div[1]/form/div[2]/input')
pasw_box.send_keys('senha')

enter_buttom = driver.find_element(By.XPATH, value='/html/body/div/main/div[2]/div[1]/form/div[3]/button')
enter_buttom.click()

sleep(3)

apply_button = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button")
apply_button.click()