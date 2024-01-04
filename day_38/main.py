import requests
import json

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
USERNAME = 'enzslv4'
TOKEN = '8rtBwkCKiP'
GRAPH_ID = 'graph1'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': 'your_app_id_here',
    'x-app-key': 'your_app_key_here'
}

data = {
    'query': 'swam for 1 hour'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# You can access the response content using response.text
print(response.text)