# Namespace Local vs Global scope
enemies = 1  # Global scope - available everywhere at this level


def increase_enemies():
    enemies = 2  # Local Scope - available only inside this function
    print(f"enemies inside function: {enemies}")  # enemies will be printed 2


def increase_enemies_global():
    global enemies  # Global scope - this will tell the function we will work with this particular variable available
    # outside the function - avoid modifying global scope - avoid "global" as much as possible
    enemies = 2
    print(f"enemies inside function: {enemies}")  # enemies will be printed 2


increase_enemies()
print(f"enemies outside function: {enemies}")  # enemies will be printed 1


def increase_enemies_global_v2():
    print(f"enemies inside function: {enemies}")
    return enemies + 1  # will return the same output as the global above, but it's more understandable


enemies = increase_enemies_global_v2()


# In Python there is no such thing as a block scope
# Ex: in an 'if' statement, what is underneath in its block will be available everywhere at that level

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # new_enemy is a global variable in this situation

# a variable inside a function will be available only in that function

# Global Constants
# in order to define global constants, the naming convention in Python says that we should write the constants with
# upper case letters
PI = 3.14159  # example 1 of a global constant
URL = "https://www.google.com"  # example 2 of a global constant

