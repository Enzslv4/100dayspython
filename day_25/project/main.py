# learning panda library
import csv # library that reads csv files
import pandas # do the same but with more complex data

# with open('day_25/project/weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# with open('day_25/project/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

data = pandas.read_csv('day_25/project/weather_data.csv')

print(data)
print(data['temp']) # cara, isso é de fuder