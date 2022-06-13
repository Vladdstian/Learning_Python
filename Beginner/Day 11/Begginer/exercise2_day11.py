# Read the code
# Spot the problems 🐞.
# Modify the code to fix the program.
# The program should tell if a year is leap or not

year = int(input("Which year do you want to check?"))
# TypeError: not all arguments converted during string formatting
# in order to compare the year to an int we should change its type to int

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
