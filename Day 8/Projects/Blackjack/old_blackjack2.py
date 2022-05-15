import random


def calc_total(card_list):
    card_sum = 0
    for card in card_list:
        card_sum += card
    return card_sum


def computer_draw(card_list):
    cards_sum = calc_total(computer_cards)
    if cards_sum < 17:
        new_card = random.choice(cards)
        print(f"Opponent draws {new_card} from the deck.")
        computer_cards.append(new_card)
        computer_draw(computer_cards)
    else:
        print(f"Opponent cards: {card_list}. Total sum: {cards_sum}.")
        return cards_sum


bid_opt = {
        1: 10,
        2: 15,
        3: 20,
        4: "All-In",
    }
for bids in bid_opt:
    print(f"{bids} - ${bid_opt[bids]}")
choice = int(input("What is your option? 1, 2, 3, 4? \n"))

balance = 100
player_cards = []
player_score = 1
computer_cards = []
computer_score = 1

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# start
player_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
computer_card_show = random.choice(computer_cards)

# print status
print(f"Your cards: {player_cards}")
print(f"Opponents cards: {computer_card_show}, ?")

player_cards_sum = calc_total(player_cards)
if player_cards_sum == 21:
    print("You have a Blackjack! You win!")
else:
    while True:
        print(f"You have a total of {player_cards_sum}")
        decision = int(input("would you like to: 1 - Draw another card or 2 - Pass\n"))
        if decision == 1:
            new_card = random.choice(cards)
            print(f"You draw {new_card} from the deck!")
            player_cards.append(new_card)
            # check again for total sum
            player_cards_sum = calc_total(player_cards)
            if player_cards_sum > 21:
                print("Bust")
                break
            else:
                continue
        else:
            print(f"Opponents cards: {computer_cards}")
            break

player_cards_sum = calc_total(player_cards)
if player_cards_sum <= 21:
    computer_cards_sum = computer_draw(computer_cards)
else:
    computer_cards_sum = calc_total(computer_cards)

if player_cards_sum == computer_cards_sum:
    print("Draw")
elif computer_cards_sum == 21:
    print("Blackjack")
elif player_cards_sum == 21:
    print("Blackjack")
elif computer_cards_sum < player_cards_sum:
    print("You win!")
elif player_cards_sum < computer_cards_sum:
    print("You loose!")
