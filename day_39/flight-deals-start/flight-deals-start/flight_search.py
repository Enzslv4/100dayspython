from data_manager import DataManager

AFFIL_ID = 'enzosilvaflightsearch'
API_KEY = 'drBktvu7lzxCsBmhEsohzM9RYmXsS4nv'

sheety = DataManager()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.data = sheety.data

    def check_data(self):
        for _ in range(6):
            if self.data['prices'][_]['iataCode'] == '':
                self.data['prices'][_]['iataCode'] = 'TESTING'

        sheety.update_sheet(self.data)