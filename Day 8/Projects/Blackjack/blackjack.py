# https://games.washingtonpost.com/games/blackjack/

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


# def start_game():

def back_menu(balance):
    answer = input("Press 'b' to go back to the main menu or 'q' to quit")
    if answer == 'b':
        return True
    else:
        withdraw(balance)
        return False


def menu():
    balance = 0
    game_status = True
    while game_status:
        print(logo)
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
            add_money(balance)
            game_status = back_menu(balance)
        elif choice == 2:
            if balance <= 0:
                print("Please add more money in order to start playing!")
            else:
                break
                # start_game()
        elif choice == 3:
            print(f"You have ${balance} at the table!")
            game_status = back_menu(balance)
        else:
            balance = withdraw(balance)
            break


menu()
