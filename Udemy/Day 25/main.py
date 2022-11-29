# with open("weather_data.csv") as data:
#     weather_data = data.readlines()
#     for item in weather_data:
#         stripped_item = item.strip()
#         print(stripped_item)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         row_data = row[1]
#         if row_data != 'temp':
#             int_data = int(row_data)
#             temperatures.append(int_data)
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
temp_data = data["temp"].tolist()
# print(max(temp_data))
average_temp = (sum(temp_data))/(len(temp_data))
print(f'Example 1 {average_temp}')
# OR

# use Panda method for series
print(f'Example 2 {data.temp.mean()}')

# Pulling data per row
# Data frame reference temperature column with condition equal to the max temp in the column i.e. check for the max temp
print(data[data.temp == data.temp.max()])


def fahrenheit(temp):
    return (temp * 1.8) + 32


monday_data = data[data.day == "Monday"]
print(monday_data)
print(fahrenheit(temp=monday_data.temp))