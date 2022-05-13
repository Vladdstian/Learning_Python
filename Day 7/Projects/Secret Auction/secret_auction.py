# Secret auction project where the program takes your name and bid and stores them into a dictionary
# At the end, it will compare all the bids and print the biggest one / the winner of the auction

# Steps
# 1. start the bid and present the product
# 2. Start loop
# 3. Bid - ask for name and bid
# 4. Store them in a dict
# 5. ask if there are ,ore bidders -> if yes go back to 2, else exit loop
# 6. check for highest bid and print the winner

import os
bids = {}


def add_bid(name, bid):
    bids[name] = bid


print("Welcome to the secret auction program!")
bidding_opened = True
while bidding_opened:
    bidder_name = input("What is your name? \n")
    bid_value = int(input("What is your bid? \n$"))
    add_bid(name=bidder_name, bid=bid_value)
    more_bid = input("Do you want to add more bids? yes or no \n")
    if more_bid == "no":
        bidding_opened = False
    print(os.system('cls'))

biggest_bid = 0
biggest_bidder = ""
for key in bids:
    if bids[key] > biggest_bid:
        biggest_bid = bids[key]
        biggest_bidder = key

print(f"And the winner of the auction is {biggest_bidder} with a {bids[biggest_bidder]}$ bid")
