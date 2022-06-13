import pandas

# pandas - a better way of working with CSV files
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

print(data["temp"])  # prints the column and automatically finds the data
print(type(data))
# 2 primary data structures of panda - Series (1 dimension - column/row/list) and DataFrame (2 dimensions - whole table)
# each data structure has a lot of useful methods

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average = data["temp"].mean()
print(average)

# Get Data in Columns
print(data["condition"])
print(data.condition)  # pandas recognised the column head but it's key sensitive

# Get Data in Row
print(data[data.day == "Monday"])

# Get the maximum temp value
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data_2 = pandas.DataFrame(data_dict)
print(data_2)
data.to_csv("new_data.csv")


