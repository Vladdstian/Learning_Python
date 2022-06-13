import pandas

squirrels = pandas.read_csv("squirrel_count.csv")
gray_squirrels = squirrels["Primary Fur Color"].count()
cinnamon_squirrels = squirrels["Primary Fur Color"].count("Cinnamon")
white_squirrels = squirrels["Primary Fur Color"].count("White")

print(gray_squirrels)
