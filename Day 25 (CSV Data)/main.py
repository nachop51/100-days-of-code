# with open("weather_data.csv") as file:
#     lines = file.readlines()
# file.close()

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv",)
# print(data)
print(type(data))
print(type(data["temp"]))  # Similar to a list, actually is a "series"
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg = sum(temp_list) / len(temp_list)
print(avg)





