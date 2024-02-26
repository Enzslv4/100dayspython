from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

form_url = 'https://forms.gle/kunijW9YUKtbxu9m8'

def fill_forms():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(form_url)