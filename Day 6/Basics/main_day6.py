# functions with inputs
input_name = input("What is your name?")


# calling the function without the inputs will return an error
# the "name" variable in () is also called a PARAMETER
# the function can have as many parameters as we want to
def greet(name, location):
    print(f"Hello {name}")
    print(f"How do you do today {name}?")
    print(f"What is the weather today in {location}?")


# the input_name variable inside the () that is used to call the function is called an ARGUMENT
# in this case those arguments are POSITIONAL ARGUMENTS, because we haven't specified anywhere which particular
# parameter we want to associate these pieces of data with
greet(input_name, "Barcelona")

# using key-value pairs these arguments turn into KEYWORD ARGUMENTS
# same result as the previous call of the function
greet(location="Barcelona", name=input_name)

