# Read this code
# Spot the problems 🐞.
# Modify the code to fix the program.
# The code needs to print the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # 'or' means only one of the statements should be true and that is not the
        # scope of the program - change to 'and'
        print("FizzBuzz")
    elif number % 3 == 0:  # continuation of the first 'if' -> change to 'elif'
        print("Fizz")
    elif number % 5 == 0:  # continuation of the first 'if' -> change to 'elif'
        print("Buzz")
    else:
        print(number)  # number shouldn't be in square brackets if we don't want to
