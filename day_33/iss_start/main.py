import requests
from datetime import datetime
import smtplib
from time import sleep

MY_LAT = -12.953976 # Your latitude
MY_LONG = -38.459612 # Your longitude
MY_POS = (-12.953976, -38.459612)

MY_EMAIL = 'enzosilva142002@gmail.com'
PASSW = 'tmnlewjbpogwwsbs'
RECEIVER = 'enzslv4@gmail.com'

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# requirements:
req_1 = -8 >= iss_latitude >= -18
req_2 = -34 >= iss_longitude >= -44
req_3 = time_now.hour >= sunset or time_now.hour <= sunrise
messages = 0

while True:
    sleep(10000)
    if req_1 and req_2 and req_3:
        if messages < 1:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                        connection.starttls() # important to crypt the message
                        connection.login(user=MY_EMAIL, password=PASSW)
                        connection.sendmail(
                            from_addr=MY_EMAIL, 
                            to_addrs='enzslv4@gmail.com', 
                            msg=f'Subject:Look Up!\n\n The ISS station is passing right now!'
                        )
            messages += 1
        else:
            break

