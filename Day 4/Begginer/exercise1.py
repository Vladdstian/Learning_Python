# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". When you run
# the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our
# testing code to check your work. There are many ways of doing this. But to practice what we learnt in the last
# lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
import random

start_game = (input("Want to toss a coin? Y or N\n")).lower()
if start_game == "y":
    print("Heads" if random.randint(0, 1) == 0 else "Tails")  # short way of including an if statement into a print
else:
    print("Thank you for playing!")
