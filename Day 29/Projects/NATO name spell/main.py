# This is my first attempt

import pandas

name = input("Please enter your name: ").upper()
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

name_letter_list = []

for lttr in name:
    code = nato_alphabet[nato_alphabet.letter == lttr]
    name_letter_list.append(code.code)

print(name_letter_list)
