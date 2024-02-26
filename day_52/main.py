from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

insta_url = 'https://www.instagram.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(insta_url)

email_box = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
email_box.send_keys('email')

passw_box = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
passw_box.send_keys('senha')

enter_box = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
enter_box.click()

sleep(3)

changes_buttom = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
changes_buttom.click()

sleep(1)

notifications_buttom = driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
notifications_buttom.click()

label = driver.find_element(By.XPATH, value='...')
label.sendKeys(Keys.PAGE_DOWN)