# until now every code I did was procedural programming
# increase in complexity gets very confusing

# Object-Oriented Programming (OOP)
# 1. split a large task into smaller pieces that can be reused
# 2. simplify relationships and make it scalable for larger and complex projects

# How to use OOP
# Example: modelling a restaurant, you have to model each person who works in there (waiter, chef, cleaner, manager)
# This is a class -> To design a waiter model (for example) you need to think about:
#   1. what it has: holding_a_plate = True, tables_responsible = [1,2,3] - these are called attributes
#   2. what it does: def take_order(table, order), def take_payment(amount) - these are called methods
# we can have multiple waiters based on the upper class, and each of them will be objects
# >>> class waiter -> Henry (object1)
#                  -> Sam (object2) ..
# so in Python , the blueprint (the class) is used to create multiple objects
# naming convention for classes in python (Pascal case) - Ex: CarBlueprint() - upper case first letter of each word
