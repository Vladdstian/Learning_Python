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
