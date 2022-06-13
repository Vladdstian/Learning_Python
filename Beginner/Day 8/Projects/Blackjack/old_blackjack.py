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
    for bids in bid_opt:
        print(f"{bids} - ${bid_opt[bids]}")
    choice = int(input("What is your option? 1, 2, 3, 4? \n"))
    if choice == 4:
        return balance
    else:
        return bid_opt[choice]


def check_total(card_list):
    cards_sum = 0
    for item in card_list:
        cards_sum += item
    if cards_sum > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
        check_total(card_list)
    elif cards_sum > 21:
        return 0
    else:
        return cards_sum


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def computer_draw(computer_cards):
    cards_sum = check_total(computer_cards)
    if cards_sum < 17:
        computer_cards.append(deal_cards())
        computer_draw(computer_cards)
    else:
        return cards_sum


def check_winner(p1, p2):
    if p1 > 21:
        print("You loose!")
    elif p2 > 21:
        print("Computer lost")
    if p2 < p1 <= 21:
        print(f"You have {p1} points. You win!")
    else:
        print(f"Computer has {p2} points. You loose!")


def card_round(balance):
    player = []
    computer = []
    player.append(deal_cards())
    player.append(deal_cards())
    computer.append(deal_cards())
    computer.append(deal_cards())
    player_total = check_total(player)
    print(f"Your total is {player_total}.")
    while True:
        decision = int(input("would you like to: 1 - Draw another card or 2 - Pass"))
        if decision == 1:
            player.append(deal_cards())
            continue
        else:
            computer_total = computer_draw(computer)
            break


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
            check_total(player)
        else:
            if check_total(computer) >= 17:
                check_winner()
            else:
                computer.append(deal_cards())
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
