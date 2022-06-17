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
    file = open("a_file.txt")  # file error
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])  # key error
except FileNotFoundError:  # having only an except will catch all errors
    file = open("a_file.txt", "w")
    file.write("Something")
    print("There was a file not found error")
except KeyError as error_message:
    print(f"There was key error. The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise
    file.close()
    print("File was closed.")



