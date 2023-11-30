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

# data = pandas.read_csv('day_25/project/weather_data.csv')
'''
print(data)
print(data['temp']) # cara, isso é de fuder
'''

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data['temp'].tolist()

# average_temp = sum(temp_list) / len(temp_list)

# print(f'{average_temp:.2f}')

# another method way more easy to get a average from a series:

# print(data['temp'].mean()) # KKKKKKKKK

# print(data['temp'].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# temp_in_celsius = monday.temp 
# temp_in_fahrenheit = temp_in_celsius * 1.8 + 32

# print(temp_in_celsius, '\n', temp_in_fahrenheit)

data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

# to init a dataframe(something that you want to manipulate in pandas), do this:

data = pandas.DataFrame(data_dict)

# print(data) # mt foda, mds
data.to_csv('new_data.csv') # muuuuuito legal