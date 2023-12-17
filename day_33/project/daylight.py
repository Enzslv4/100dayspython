import requests
import datetime as dt

PARAMETERS = {
    'lat': -12.953976,
    'lng': -38.459612,
    'formatted': 0
}

class DayLight():

    def __init__(self):
        self.response = requests.get(url='https://api.sunrise-sunset.org/json', params=PARAMETERS)
        self.response.raise_for_status()
        self.data = self.response.json()

        self.sunrise = self.data['results']['sunrise'].split('T')[1].split(':')[0]

        self.sunset = self.data['results']['sunset'].split('T')[1].split(':')[0]

        self.hour = dt.datetime.now().hour
