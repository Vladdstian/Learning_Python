import pandas

# pandas - a better way of working with CSV files
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

print(data["temp"])  # prints the column and automatically finds the data
