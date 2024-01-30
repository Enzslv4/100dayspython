# Amazon price checking bot

import smtplib
import requests
from bs4 import BeautifulSoup

item_url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
MY_EMAIL = 'enzosilva142002@gmail.com'
PASSW = 'tmnlewjbpogwwsbs'
RECEIVER = 'enzslv4@gmail.com'

response = requests.get(item_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
price = float(soup.find(class_="a-offscreen").get_text().split('$')[1])

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() # important to crypt the message
        connection.login(user=MY_EMAIL, password=PASSW)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs='enzslv4@gmail.com', 
            msg=f'Subject:Price checking\n\n Your product is now available for less then $100!'
        )