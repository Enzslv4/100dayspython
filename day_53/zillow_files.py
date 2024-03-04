import requests
from bs4 import BeautifulSoup

zillow_url = 'https://appbrewery.github.io/Zillow-Clone/'

def find_places():
    response = requests.get(zillow_url)
    zillow_text = response.text

    soup = BeautifulSoup(zillow_text, 'html.parser')
    prices_objs = soup.find_all(name='ul', class_='List-c11n-8-84-3-photo-cards')
    prices_list = prices_objs[0].getText().split('Save this home')
    new_prices_list = []
    for _ in range(0, len(prices_list) - 1):
        new_prices_list.append(prices_list[_].replace("\n", '')[34:].split('/')[0].split(', CA '))
        new_prices_list[_][1] = new_prices_list[_][1].replace(' ', '').split('$')[-1]
        if '+' in new_prices_list[_][1]:
            new_prices_list[_][1] = new_prices_list[_][1].split('+')[0]
        if '|' in new_prices_list[_][0]:
            new_prices_list[_][0] = new_prices_list[_][0].replace(' |', ',')

    return new_prices_list