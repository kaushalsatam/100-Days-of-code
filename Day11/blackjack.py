# BlackJack colution

from art import logo
from os import system
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lost. Opponent has a blackjack."
    elif user_score == 0:
        return "You won. You have a blackjack."
    elif user_score > 21:
        return "You went over, You lost."
    elif computer_score > 21:
        return "Computer went over, You won."
    elif user_score > computer_score:
        return "You won."
    else:
        return "Computer won."

def playGame():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # user cards & computer cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, Type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's cards: {computer_cards}, computer's score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack?\nType 'y' or 'n': ") == 'y':
    system('cls')
    playGame()