# Write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2-digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true_value = 0
love_value = 0
combined_names = (name1 + name2).upper()
# print(combined_names)

if "T" in combined_names:
    true_value += combined_names.count("T")
if "R" in combined_names:
    true_value += combined_names.count("R")
if "U" in combined_names:
    true_value += combined_names.count("U")
if "E" in combined_names:
    true_value += combined_names.count("E")
# print(true_value)

if "L" in combined_names:
    love_value += combined_names.count("L")
if "O" in combined_names:
    love_value += combined_names.count("O")
if "V" in combined_names:
    love_value += combined_names.count("V")
if "E" in combined_names:
    love_value += combined_names.count("E")
# print(love_value)

total_value = str(true_value) + str(love_value)
total_as_int = int(total_value)

if total_as_int < 10 or total_as_int > 90:
    print(f"Your score is {total_as_int}, you go together like coke and mentos.")
elif 40 < total_as_int < 50:
    print(f"Your score is {total_as_int}, you are alright together.")
else:
    print(f"Your score is {total_as_int}.")
