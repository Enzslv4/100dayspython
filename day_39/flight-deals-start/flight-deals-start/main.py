from flight_search import FlightSearch
import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
test = FlightSearch()

test.check_data()
data_dict = test.data
print(data_dict)