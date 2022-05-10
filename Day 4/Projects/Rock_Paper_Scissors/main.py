# Make a rock, paper, scissors game.
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
choices = [rock, paper, scissors]
computer_input = random.randint(0, 2)
print("Player: ")
print(choices[user_input])

print("Computer: ")
print(choices[computer_input])

if choices[user_input] == rock:
    if choices[computer_input] == rock:
        print("Draw")
    elif choices[computer_input] == paper:
        print("You loose!")
    else:
        print("You win!")
elif choices[user_input] == paper:
    if choices[computer_input] == rock:
        print("You win!")
    elif choices[computer_input] == paper:
        print("Draw")
    else:
        print("You loose!")
else:
    if choices[computer_input] == rock:
        print("You loose!")
    elif choices[computer_input] == paper:
        print("You win!")
    else:
        print("Draw")
