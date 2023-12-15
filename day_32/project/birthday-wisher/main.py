from pandas import *
import smtplib
import datetime as dt

MY_EMAIL = 'enzosilva142002@gmail.com'
MY_PASSW = 'tmnlewjbpogwwsbs'


dates_data = read_csv('day_32/project/birthday-wisher/birthdays.csv')

now = dt.datetime.now()
todays_day = now.day
todays_month = now.month
hour = now.hour

for _ in range(len(dates_data)):
    name = dates_data['name'][_]
    month = dates_data['month'][_]
    day = dates_data['day'][_]
    email = dates_data['email'][_]
    if day == todays_day and month == todays_month:
        if hour == 9:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls() # important to crypt the message
                connection.login(user=MY_EMAIL, password=MY_PASSW)
                connection.sendmail(
                    from_addr=MY_EMAIL, 
                    to_addrs=email, 
                    msg=f'Subject:Good Morning {name}!\n\nHappy Birthday!!!!.'
                )
