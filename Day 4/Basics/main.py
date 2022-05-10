# Randomisation and Python Lists
# "ask python.com" the best thing when learning python

import random  # import the module of random
import my_module  # import the module that I created

print(my_module.pi)  # imports the variable that I created in the custom module

random_integer = random.randint(100, 500)  # it will provide a random number between 100 and 500
random_float = random.random()  # creates a random float between [0 and 1) but never 1.0
random2_float = 5 * random.random()
# random function that provides a float will never return a value bigger than 0.99... so if we want a random value in
# the range of [0, 5) we will have to multiply that function to get the wanted result
print(random_integer)
print(random_float)
print(random2_float)
print(random2_float)  # discovered shortcut to duplicate: select what you want and Ctrl+D

# Data structures : Lists
fruits = ["strawberry", "apple"]  # example of a list
print(fruits[0])  # restores the first item in the list in the order that was saved

