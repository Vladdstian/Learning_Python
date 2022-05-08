# earn to take input from the user and to use variables
name = input("What is your name?\n").lower().capitalize()
input(f"Well, {name}, do you know how to take input from a user?")
print(f"I will tell you my dear {name}.")
print("You just have to use the function input() built into Python")
print("It's that easy!")
print(f'And, {name}, keep it a secret but you can assign it to a variable and use it whenever you want in your code')

# variable naming rules
print("""to name the variables, in python there are some rules:
* you cannot use the built-in functions of Python as names for your variables
* the name of a variable can have multiple names but they should be separated in Python with '_'
* you can have numbers in the names of variables, but they shouldn't start with a number""")

# primitive data types learned: strings, integer (int), floating point number (float), boolean (bool)
string_example = "this is a string"
string2_example = '123'  # this is also a string
int_example = 123  # this is an int
float_example = 3.14159  # this is a float example and a bit of PI's value
float2_example = 734_529.687  # did you know a big number can be separated by underscore "_" ?
bool_example = True  # this is a bool example - it can have 2 values only: either True or False
print(float2_example)

# Type error, Type checking and Type conversion
type(int_example)  # this function will result in class 'int' because it is of type integer
str(float2_example)  # this function will convert the variable from a float to a string
# to change a data type into another data type we use this function data_type_we_want(data_type_we_have)


# string manipulation
len(string_example)  # gives the length of a string - using another data type like int will give an error
string_example[0]  # string subscripting - will return the letter at the index 0 inside the []
