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

# Card deck and balance
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
balance = 0


def calc_total(card_list):
    card_sum = 0
    for card in card_list:
        card_sum += card
    return card_sum


def check_winner(p_score, c_score):
    if p_score > 21:
        return "C"
    elif c_score > 21:
        return "P"
    elif p_score < c_score:
        return "C"
    elif c_score < p_score:
        return "P"
    else:
        return "D"


def start_game(player_balance):
    # Choose the bid before starting the game
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
        bid = player_balance
    else:
        bid = bid_opt[choice]

    # Draw cards
    player_cards = []
    computer_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    # calculate score
    player_score = calc_total(player_cards)

    # show cards
    while True:
        if player_score == 21:
            print("You have Blackjack!")
            game_status = "P"
            break
        else:
            player_draw_round = True
            while player_draw_round:
                # Check score
                if player_score <= 21:
                    print(f"Your cards: {player_cards}, current score: {player_score}")
                    print(f"Computer's first card: {computer_cards[0]}")
                    draw_choice = int(input("Do you want to continue? \n1 - Draw card\n2 - Stay\n"))
                    if draw_choice == 1:
                        new_card = random.choice(cards)
                        player_cards.append(new_card)
                        print(f"You draw {new_card} from the deck.")
                        player_score = calc_total(player_cards)
                    else:
                        player_draw_round = False
                else:
                    player_draw_round = False
            break
    print(f"Your final cards: {player_cards}, final score: {player_score}")
    # computer draw
    while True:
        computer_score = calc_total(computer_cards)
        if computer_score < 17:
            new_card = random.choice(cards)
            print(f"Computer draws {new_card} from the deck.")
            computer_cards.append(new_card)
            continue
        else:
            print(f"Computers final cards: {computer_cards}. Total sum: {computer_score}.\n")
            break

    game_status = check_winner(player_score, computer_score)

    if game_status == "P":
        print("Player wins!")
        player_balance += bid
        print(f"Your balance is now {player_balance}\n\n\n")
    elif game_status == "C":
        print("Computer wins!")
        player_balance -= bid
        print(f"Your balance is now {player_balance}\n\n\n")
    else:
        print("Draw\n\n\n")
    return player_balance


def menu(player_balance):
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
            player_balance += add_money
            print("\n\n\n")
        elif choice == 2:
            if player_balance <= 10:
                print("Please add more money in order to start playing!")
            else:
                player_balance = start_game(player_balance)
        elif choice == 3:
            print(f"You have ${player_balance} at the table!\n\n\n")
        else:
            print(f"You have withdrawn ${player_balance}! Hope you enjoyed your stay!")
            break


menu(balance)
# Took way more than it should have
