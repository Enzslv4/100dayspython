from selenium import webdriver

amazon_url = 'https://www.amazon.com'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=chrome_options)
driver.get(amazon_url)