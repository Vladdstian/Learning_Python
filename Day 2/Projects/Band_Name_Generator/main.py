# This small project will generate a name for a band based on input from the user
print("Hello and welcome to my Band Name Generator")
name = input("What is your name?\n").title()
city = input(f"What city did you grew up in {name}?\n").title()
pet_name = input(f"Now, {name}, please give me the name of one of your pets.\n").title() + "s"
band_name = city + " " + pet_name
print(f"{name}, your band name could be {band_name}")