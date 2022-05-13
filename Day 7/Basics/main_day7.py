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

# Nesting
# Dictionaries and Lists can be viewed as a folder and nesting is just a matter of putting one inside the other
# For example. a dictionary can have as keys and list or dictionaries values
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Romania": "Bucharest",
}

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Lyon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
        "total_visits": 5
    },
]


# better to use lists as a main since they are ordered and dictionaries no


# Functions with output
# Function with only 1 return statement
def my_function(a, b):
    return a + b  # this function will have as output the sum of the 2 input numbers
# a function can return only one result, but you can have multiple return statements, for example in "if" conditional


def my_own_funct(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    # the string above is a Docstring, and it is useful to describe the custom function
    # it will appear when calling the function to describe what it does
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result {formatted_f_name}  {formatted_l_name}"

