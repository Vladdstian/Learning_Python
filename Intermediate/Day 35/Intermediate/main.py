# Errors and Exceptions

# FileNotFoundError
# this code will result in an error -> FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana"]
# fruit = fruit_list[2]

# TypeError
# text = "abc"
# print(text + 5)

# Catch exceptions
# try
#    block -> something that might cause an exception
# except
#    block -> do this if there was an exception
# else
#    block -> do this if there is no exception
# finally:
#    block -> do this no matter what happens

try:
    file = open("a_file.txt")
except:
    open("a_file.txt", "w")
    print("There was an error")


