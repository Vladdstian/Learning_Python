#  OPTION number 1
# with open("weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()
#     new_data = []
#     for line in data:
#         new_line = line.strip("\n")
#         new_data.append(new_line)


# OPTION number 2
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#     print(temperatures)


# OPTION number 3
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

