from selenium import webdriver
from selenium.webdriver.common.by import By # important to remember this one, otherwise it wont work

# amazon_url = 'https://www.amazon.com.br/'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)

# driver = webdriver.Edge(options=chrome_options)
# driver.get(amazon_url)

# search_bar = driver.find_element(By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[3]/div/a[3]/div[2]') 
# normal copy/past of the xpath would not work, instead copy the full xpath

# print(search_bar.text)

py_url = 'https://www.python.org/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=chrome_options)
driver.get(py_url)

events_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
#     events_box.pop(0)

# events_dict = {}

# for _ in range(len(events_box) - 1):
#     events_dict[_] = {'time': events_box[_], 'name': events_box[_ + 1]}

# print(events_dict[0]['name'])

events_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

events_dict = {}

events_times = [events_times[i].text for i in range(len(events_times))]
events_names = [events_names[i].text for i in range(len(events_names))]

for i in range(len(events_times)):
    events_dict[i] = {'time': events_times[i], 'name': events_names[i]}

print(events_dict)