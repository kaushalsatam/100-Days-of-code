# Blackjack capstone project
"""My first solution"""

# 2-10 face value
# K, Q, J = 10
# A = 11 or 1

from os import system
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start_state = True

while start_state:
    your_cards = []

    computer_cards = []
    start = input("Do you want to play a game of Blackjack?\nType 'y' or 'n': ")
    system('cls')
    if start == 'n':
        start_state = False
        break

    print(logo)

    # Actual logic

    # Your first 2 cards
    for i in range(0, 2):
        random_card = random.choice(cards)
        your_cards.append(random_card)

    # Computer's first 2 cards(Dealer)
    # computer_first_card = random.choice(cards)
    # computer_second_card = random.choice(cards)

    for k in range(0, 2):
        random_card = random.choice(cards)
        computer_cards.append(random_card)
    computer_first_card = computer_cards[0]

    if sum(your_cards) > 21:
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's cards: {computer_cards}, computer's current score: {sum(computer_cards)}")
        print("You Lost.")
        break
    if sum(your_cards) == 21 and len(your_cards) == 2:
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's cards: {computer_cards}, computer's current score: {sum(computer_cards)}")
        print("BlackJack")
        break
    
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {computer_first_card}")


    another_card_choice = True
    while another_card_choice:
        another_card = input("Type 'y' to get another card, Type 'n' to pass: ")
        if another_card == "n":
            while sum(computer_cards) <= sum(your_cards):
                computer_next_card = random.choice(cards)
                computer_cards.append(computer_next_card)
            if sum(computer_cards) > 21:
                print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
                print(f"Computer's cards: {computer_cards}, computer's current score: {sum(computer_cards)}")
                print("You Won.")
            else:
                print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
                print(f"Computer's cards: {computer_cards}, computer's current score: {sum(computer_cards)}")
                print("You Lost.")
            another_card_choice = False
            break
        random_card = random.choice(cards)
        your_cards.append(random_card)
        if sum(your_cards) > 21:
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Computer's cards: {computer_cards}, computer's current score: {sum(computer_cards)}")
            print("You lost.")
            break
        elif sum(your_cards) == 21:
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Computer's cards: {computer_cards}, computer's current score: {sum(computer_cards)}")
            print("BlackJack")
            break
        else:
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Computer's first card: {computer_first_card}")
    if sum(your_cards) > sum(computer_cards) and sum(your_cards) <= 21:
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's cards: {computer_cards}, computer's current score: {sum(computer_cards)}")
        print("You Won.")