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

pandas.read_csv("weather_data.csv",)
