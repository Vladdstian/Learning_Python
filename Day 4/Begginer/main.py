# Randomisation and Python Lists
# "askpython.com" the best thing when learning python

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
print(fruits[-1])  # restores the last item in the list; -1 means it will start counting down from the end of the list
fruits[1] = "watermelon"  # changes the value of the item at the index 1
fruits.append("apple")  # adds a new item at the END of the list
fruits.extend("pear", "mango", "grapes", "peaches", "cherries")  # adds multiple values at the END of the list
# other functions can be used to work with lists - find info at "docs.python.org"
# Don't memorise all the functions as they are easily available in the documentation

vegetables = ["spinach", "kale", "tomatoes", "Potatoes"]

dirty_dozen = [fruits, vegetables]  # this is a list made out of lists
print(dirty_dozen[0][0])  # will print the first value (strawberry) from the first list(fruits) in dirty dozen

# Python Loops

# 1st loop - FOR loop
for fruit in fruits:
    print(fruit)  # it loops through the fruits list and prints the value of each item/fruit in the list
    print(fruit + " Pie")

even_sum = 0
for numbers in range(0, 101, 2):  # calculates the sum of all even numbers from 0 to 100 (increments by 2)
    even_sum += numbers
print(even_sum)


# Calling and Defining Functions

print()  # this is a function: it is followed by the () and it acts on the "things" that are inside the parenthesis


# this is a custom function
def my_function():
    print("Hello, Vlad")


# to call the custom function
my_function()
