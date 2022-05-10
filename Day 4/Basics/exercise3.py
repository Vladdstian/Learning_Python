# You are going to write a program that will mark a spot with an X.
# # This map contains a nested list. When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# solution 1
# position_as_int = int(position)
# first_coord = int(position_as_int % 10 - 1)
# second_coord = int((position_as_int - position_as_int % 10) / 10 - 1)
# treasure_map[first_coord][second_coord] = "X "

# solution 2 - better solution - less code
treasure_map[int(position[1])-1][int(position[0])-1] = "X "

print(f"{row1}\n{row2}\n{row3}")
