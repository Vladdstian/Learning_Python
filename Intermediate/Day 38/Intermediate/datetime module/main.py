import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

print(now)
print(type(now))
print(year)
print(type(year))
print(day_of_the_week)  # 1 is Tuesday
print(month)

year_birth = dt.datetime(year= 1990, month=8, day=1)
print(year_birth)
