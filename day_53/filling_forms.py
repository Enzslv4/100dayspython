from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

form_url = 'https://forms.gle/kunijW9YUKtbxu9m8'

def fill_forms(prices_list):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(form_url)
    sleep(1)

    for _ in range(0, len(prices_list) - 1):

        adress_box = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        adress_box.send_keys(prices_list[_][0])

        price_box = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_box.send_keys(prices_list[_][1])

        send_buttom = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
        send_buttom.click()
        
        refresh_buttom = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        refresh_buttom.click()

    driver.close()