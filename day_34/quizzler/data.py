import requests


response = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
response.raise_for_status()
questions_data = response.json()['results']
