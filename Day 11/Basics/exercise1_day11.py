# Read this the code
# Spot the problems 🐞.
# Modify the code to fix the program.
# The program should answer if a number is even or odd

number = int(input("Which number do you want to check?"))
# on line 8 instead of equality comparison "==", assignment "=" is used
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

