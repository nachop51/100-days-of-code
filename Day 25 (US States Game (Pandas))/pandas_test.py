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

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(type(data["temp"]))  # Similar to a list, actually is a "series"
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg = sum(temp_list) / len(temp_list)
# print(avg)

# Calculates te average
# print(data["temp"].mean())
# Retrieves the max value
# print(data["temp"].max())

# print(data["condition"])
# Both work
# print(data.condition)

# Retrieves one row where the day is Monday
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# Dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# d_dict = pandas.DataFrame(data_dict)
# print(d_dict)
# d_dict.to_csv("new_data.csv")
