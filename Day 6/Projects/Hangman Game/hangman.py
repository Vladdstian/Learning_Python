# Everybody knows Hangman
# If you're from another planet here is a link to how it is played:
# https://en.wikipedia.org/wiki/Hangman_(game)
# the basic idea of the game was implemented. I will not go further than this since the point is not to do UI, but to
# learn Python
import random


# this function will check if a list is equal to a string
# A simpler solution is possible, but I chose to do a function to learn and understand better
def check_if_same(a_list, a_string):
    equal_score = 0
    for a_item in a_list:
        for b_item in a_string:
            if a_item == b_item:
                equal_score += 1
            else:
                continue
    if equal_score == len(a_string):
        return True
    else:
        return False


words_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(words_list).lower()
display = []

for letter in chosen_word:
    display.append("_")

lives = 5
hidden_word = ""

while True:
    guess_letter = (input("Please guess a letter:")).lower()
    if guess_letter in chosen_word:
        word_len = 0
        while word_len != len(chosen_word):
            if guess_letter == chosen_word[word_len]:
                display[word_len] = guess_letter
                word_len += 1
            else:
                word_len += 1
        print(display)
        if check_if_same(display, chosen_word):
            # can also be checked if there is no "_" is in display
            # this removes the need of another function and many lines of code
            print("You've won!")
            break
    else:
        if lives != 0:
            lives -= 1
            print(f"You have {lives} lives remaining")
        else:
            print("You've lost!")
