# new approach
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def menu():
    balance = 0
    game_status = True
    print(logo)
    while game_status:
        actions = {
            1: "Add money",
            2: "Start a new game",
            3: "Show balance",
            4: "Withdraw and quit",
        }
        for key in actions:
            print(f"{key} - {actions[key]}")
        choice = int(input("Choose your action:\n"))
        if choice == 1:
            add_money = float(input("How much money would you like to add? \n"))
            balance += add_money
        elif choice == 2:
            if balance <= 0:
                print("Please add more money in order to start playing!")
            else:
                continue
                # balance = game(balance)
        elif choice == 3:
            print(f"You have ${balance} at the table!")
        else:
            print(f"You have withdrawn ${balance}! Hope you enjoyed your stay!")
            break

