from pprint import pprint
import requests


url = 'https://api.sheety.co/cac48d28565d514017f9877cdebf5dba/flightDeals/prices'
header = {
    'Authorization': 'Bearer 3cKkfrHr2yFiDPYXHsh8FJ513fpBef44',
}


response =requests.get(url, headers=header)
data = response.json()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = data
    
    def update_sheet(self, new_dict):
        body = {
            'price': new_dict
        }

        response = requests.post(url, json=body, headers=header)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            json_data = response.json()
            # Do something with your data
            print(json_data["price"])
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            print(response.text)

        