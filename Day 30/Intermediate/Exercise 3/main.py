# list comprehension exercise
# print the common numbers from the 2 lists provided

list_1 = "file1.txt"
list_2 = "file2.txt"

with open(list_1, "r") as data_1:
    list_1 = data_1.readlines()
with open(list_2, "r") as data_2:
    list_2 = data_2.readlines()

# 1st try
# new_list_1 = []
# new_list_2 = []
#
# for item in list_1:
#     new_list_1.append(int(item.strip("\n")))
# for item in list_2:
#     new_list_2.append(int(item.strip("\n")))
#
# result = [n for n in new_list_2 if n in new_list_1]
# print(new_list_2)
# print(new_list_1)


# 2nd try
result = [int(n.strip("\n")) for n in list_1 if n in list_2]

print(result)




