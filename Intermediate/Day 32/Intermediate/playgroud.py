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
