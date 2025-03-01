from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the Chrome WebDriver (adjust the path to where you have ChromeDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Define URLs
login_url = 'https://yourgymwebsite.com/login'
booking_url = 'https://yourgymwebsite.com/book_class'

# Step 1: Open the gym website login page
driver.get(login_url)
time.sleep(2)  # Wait for the page to load

# Step 2: Login (you'll need to adjust these element locators based on the website's structure)
username_field = driver.find_element(By.ID, 'username')  # Replace with actual field ID or name
password_field = driver.find_element(By.ID, 'password')  # Replace with actual field ID or name
login_button = driver.find_element(By.ID, 'login_button')  # Replace with actual button ID

# Enter login credentials
username_field.send_keys('your_username')  # Replace with your actual username
password_field.send_keys('your_password')  # Replace with your actual password
login_button.click()

time.sleep(5)  # Wait for login to complete

# Step 3: Navigate to the class booking page
driver.get(booking_url)
time.sleep(3)  # Wait for the booking page to load

# Step 4: Find available classes
# Assuming there is a list of classes displayed on the page, find and interact with them
class_list = driver.find_elements(By.CLASS_NAME, 'class-item')  # Replace with the actual class name

# Iterate through the available classes and book the first one
for gym_class in class_list:
    class_name = gym_class.find_element(By.CLASS_NAME, 'class-name').text  # Replace with actual class name
    class_time = gym_class.find_element(By.CLASS_NAME, 'class-time').text  # Replace with actual class time

    print(f"Available Class: {class_name} at {class_time}")

    # Example: Click on the first available class (you can customize this logic)
    gym_class.click()

    # Step 5: Book the class (this will depend on the website's form/button structure)
    book_button = driver.find_element(By.ID, 'book_button')  # Replace with actual booking button ID
    book_button.click()

    print("Class booked successfully!")
    break  # You can remove this if you want to book multiple classes

# Optional: Wait and close the browser
time.sleep(3)
driver.quit()
