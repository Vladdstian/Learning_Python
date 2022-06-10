# list and dictionary comprehension
# it is unique to python language
# very used and easy to read
# case when you create a list from a list

# new_list = [new_item for item in list]

# Example 1
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

# Example 2 - with range function
new_list_2 = [n*2 for n in range(1, 5)]
print(new_list_2)

# Example 3 - if condition
names = ["Alex", "Beth", "Vlad", "Dave", "Eleanor", "Freddie", "Caroline"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

caps_names = [name.upper() for name in names if len(name) > 5]
print(caps_names)
