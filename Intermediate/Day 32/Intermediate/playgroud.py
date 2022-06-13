# Advanced Python arguments

# keyword arguments
# def my_function(a,b,c):
#   do this with a
#   then do this with b
#   finally do this with c

# keyword arguments with default values
# all the arguments are optional and when you want to call the function you are not required to provide any of them
# def my_function(a=1,b=2,c=3):
#   do this with a
#   then do this with b
#   finally do this with c

# functions that can take any number of arguments
# def add(*args):  -> this function takes as many arguments as you want.
# the * is very important and args is just a naming convention that all python devs might use it
# for n in args:
#   print(n)
# Example: playground add function

# functions that can take any number of key-word arguments
# Example: playground calculate function


# function with unlimited arguments
# when calling this function any number of arguments can be added
def add(*args):  # the args is represented by a tuple
    result = 0
    for item in args:
        result += item
    return result


print(add(3, 5, 6, 3, 2, 6, 78, 4, 3))


def calculate(n, **kwargs):  # the kwargs is basically a dictionary
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]  # if make is not provided this line will return an error
        self.model = kw.get("model")  # if model is not provided this line will return NONE and no error
        self.seats = kw.get("seats")
#       .... -> more can be added


my_car = Car(make="nissan", model="gtr")
print(my_car.model)
