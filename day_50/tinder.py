from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

tinder_url = 'https://tinder.com/app/recs'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(tinder_url)

sleep(2)

cookies_buttom = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
cookies_buttom.click()

login_buttom = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]')
login_buttom.click()

sleep(2)

google_auth = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[1]/div/div/div/iframe')
google_auth.click()

sleep(1)

driver.switch_to.window(driver.window_handles[1])
print(driver.title)

email_box = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email_box.send_keys('email')

email_check = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
email_check.click()

# captcha made me give up