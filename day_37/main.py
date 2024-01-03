import requests
from datetime import datetime

USERNAME = 'enzslv4'
TOKEN = '8rtBwkCKiP'
GRAPH_ID = 'graph1'

today = datetime.now()

pixela_endpoint = 'https://pixe.la/v1/users'

user_param = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Cycling graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ichou'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response1 = requests.post(url=pixela_endpoint, json=user_param, headers=headers)

b = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '5'
}

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixel_data = {
    'date': '20230102',
    'quantity': '45.4'
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)