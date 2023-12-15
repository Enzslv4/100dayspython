# mail sender

import smtplib
import datetime as dt
import random

MY_EMAIL = 'enzosilva142002@gmail.com'
PASSW = 'tmnlewjbpogwwsbs'
RECEIVER = 'enzslv4@gmail.com'

now = dt.datetime.now()
yr = now.year
month = now.month
week_day = now.weekday()
hour = now.hour
birthday = dt.datetime(year=2002, month=3, day=22)

if week_day == 0:
    if hour == 9:
        with open('day_32/project/start/quotes.txt') as file:
            data = file.readlines()

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls() # important to crypt the message
            connection.login(user=MY_EMAIL, password=PASSW)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs='enzslv4@gmail.com', 
                msg=f'Subject:Good Morning!\n\n{data[random.randint(0, 101)]}.'
            )