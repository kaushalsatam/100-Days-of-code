# Blind/Secret auction project

import os
from art import logo

# Empty dictionary for storing the records
bid_dict = {}

bidders = True

biggest_bid = 0
winner = ""

# Loop will continue looping until the bidders value becomes False
while bidders:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    # Storing valus in bid_dict dictionary
    bid_dict[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if more_bidders == "yes":
        os.system('cls')
    # if there are no more bidders the the bids (values) of the names (keys) will get compared to the variable bigges_bid
    if more_bidders == "no":
        for bidder in bid_dict:
            # if current_bid gets bigger than the biggest_bid then that bid will become biggest_bid
            # and the bidder will become winner
            current_bid = bid_dict[bidder]
            if current_bid > biggest_bid:
                biggest_bid = current_bid
                winner = bidder
        bidders = False

# biggest_bid = max(bid_dict.values())
# biggest_bid = max(zip(bid_dict.values(), bid_dict.keys()))
# print(f"The winner is {biggest_bid[1]} with a bid of ${biggest_bid[0]}")
print(f"The winner is {winner} with a bid of ${biggest_bid}")