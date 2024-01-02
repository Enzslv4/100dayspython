# rain alert
import os
import requests
from twilio.rest import Client


#------------------------ TWILIO CONFIGS ------------------------#

account_sid = 'AC6d5202cc63d426e612d82efb949a22bd'
auth_token = 'f5afe5a8bdde29913fdc625391bd1782'
client = Client(account_sid, auth_token)
text = 'Bring an unbrella!'

def send_sms():
    message = client.messages.create(
            from_='+14803861954',
            body=f'{text}',
            to='MY NUMBER'      # Actually not working because of obvious reasons
        )
    print(message.status)


#------------------------ WEATHER API ------------------------#

api_key = '3b1f57d3d2371b652cd3c970942a792b'
site = 'https://api.openweathermap.org/data/2.5/forecast'

weather_params = {
    'lat': -12.953876,
    'lon': -38.459767,
    'cnt': 4,
    'appid': api_key
}

response = requests.get(url=site, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data['list'][0]['weather'][0]['id']

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    send_sms()
