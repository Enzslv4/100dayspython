# working with APIs

'''
Codes from HTTP:

1xx - Hold On
2xx - Here you go
3xx - Go away
4xx - You screwed up
5xx - I screwed up

'''
import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')

# response.status_code: gets the code from the http

response.raise_for_status()  # automatically shows the error, if its not 200

data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_pos = (float(longitude), float(latitude))

print(iss_pos)