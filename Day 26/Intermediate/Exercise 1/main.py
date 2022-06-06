# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_file_path = "./Input/Names/invited_names.txt"
letter_file_path = "./Input/Letters/starting_letter.txt"

with open(name_file_path, "r") as name_file:
    names_list = name_file.readlines()

print(names_list)

with open(letter_file_path, "r") as letter_file:
    letter = letter_file.read()

letter_count = 0
for name in names_list:
    guest_name = name.strip("\n")
    new_letter = letter.replace("[name]", guest_name)
    letter_location = f"./Output/ReadyToSend/letter_for_{guest_name}.txt"
    with open(letter_location, "x") as lttr:
        lttr.write(str(new_letter))
    letter_count += 1
