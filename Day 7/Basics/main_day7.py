# Dictionaries - allow to group together and tag related pieces of information
# Key - Value pairs
# the key is the identifications - like the letter in an actual dictionary

dictionary_example = {"Bug": "An error in a program that prevents the program from running as expected"}
# dictionary = {Key1 : Value1, Key2 : Value2, etc.}

# proper writing of a dictionary for a better readability of the code
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])  # retrieve the value linked to this particular Key

# adding a new key-value pair to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Edit an item in the dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a computer
for key in programming_dictionary:
    print(key)  # loops through the keys of the dictionary
    print(programming_dictionary[key])  # loops through the values


# usually, in real life a dictionary is created empty and pairs are added like above
# the creation of a dictionary (below) is also used to clear all the items inside it - delete everything
programming_dictionary = {}

