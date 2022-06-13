# Indentation is very important in Python - it acts and looks like a folder with the files inside it
def my_func():  # folder
    print("Hello")  # file inside the folder; inside the def block


print("World")  # same directory as the folder ; not indented

# each functions that require a block and indentation will be treated accordingly
# if there is a for loop inside the custom function it's block will be indented in regard to the for statement
# SPACES ARE THE PREFERRED INDENTATION IN PYTHON

#  While Loops
x = 5
y = 3
while x >= y:  # will run until x is decremented and the statement is no longer correct/TRUE
    print(x)
    x -= 1

# For loops are used when we want to iterate over something, and we have a fixed number of iterations that we "know"
# while loops are used when we want to increment/ decrement - used improperly (when the while statement will always be
# true) will create an infinite loop and the program might crash

