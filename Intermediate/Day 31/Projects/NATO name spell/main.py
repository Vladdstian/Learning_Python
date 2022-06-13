# This is my second attempt using list comprehension and pandas looping

import pandas

name = input("Please enter your name: ").upper()
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# 1st attempt using pandas looping
name_letter_list = []
for n_letter in name:
    for (index, row) in nato_alphabet.iterrows():
        if row.letter == n_letter:
            name_letter_list.append(row.code)

# 2nd attempt combining everything I know - if this works I am a genius
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
# nato_dict = {"A": "Alfa", "B": "Bravo" ...}
nato_list_from_word = [nato_dict[letter] for letter in name]

print(nato_list_from_word)
# I am not a genius - i did multiple try-outs :(

print(name_letter_list)
# 1st attempt works fine and everything is ordered
