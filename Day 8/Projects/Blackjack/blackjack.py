# https://games.washingtonpost.com/games/blackjack/
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


def add_money(balance):
    money = float(input("How much money would you like to add? \n"))
    return balance + money


def withdraw(balance):
    print(f"You have withdrawn ${balance}. Hope you enjoyed your stay!")
    return 0


def bid(balance):
    bid_opt = {
        1: 10,
        2: 15,
        3: 20,
        4: "All-In",
    }
    for bids in bid_opt():
        print(f"{bids} - ${bid_opt[bids]}")
    choice = int(input("What is your option? 1, 2, 3, 4? \n"))
    if choice == 4:
        return balance
    else:
        return bid_opt[choice]


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def game(balance):
    value = bid(balance)
    player = []
    computer = []
    while balance != 0:
        player.append(deal_cards())
        player.append(deal_cards())
        computer.append(deal_cards())
        computer.append(deal_cards())
        print("Would you like to: 1 - Draw another card, 2 - pass")
        if 1:
            player.append(deal_cards())
        else:

    return balance


def back_menu(balance):
    answer = input("Press 'b' to go back to the main menu or 'q' to quit")
    if answer == 'b':
        print("\n\n\n")
        return True
    else:
        withdraw(balance)
        return False


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
            balance = add_money(balance)
            game_status = back_menu(balance)
        elif choice == 2:
            if balance <= 0:
                print("Please add more money in order to start playing!")
            else:
                balance = game(balance)
        elif choice == 3:
            print(f"You have ${balance} at the table!")
            continue
        else:
            balance = withdraw(balance)
            break


menu()
