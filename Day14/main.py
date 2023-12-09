# Higher or Lower game (My solution)

import random
from os import system
from game_data import data
from art import logo, vs


option_a = random.choice(data)
option_b = random.choice(data)
while option_b == option_a:
    option_b = random.choice(data)
current_score = 0

game_running = True

while game_running:
    print(logo)

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    comparison = input("Who has more followers? Type 'A' or 'B': ").lower()

    if comparison == 'a':
        if option_a['follower_count'] > option_b['follower_count']:
            current_score += 1
            system('cls')
            print(f"You're right!, Current score: {current_score}")
            option_a = option_b
            option_b = random.choice(data)
            while option_a == option_b:
                option_b = random.choice(data)
        else:
            print(f"You're wrong!, Current score: {current_score}")
            game_running = False
    elif comparison == 'b':
        if option_b['follower_count'] > option_a['follower_count']:
            current_score += 1
            system('cls')
            print(f"You're right!, Current score: {current_score}")
            option_a = option_b
            option_b = random.choice(data)
            while option_a == option_b:
                option_b = random.choice(data)
        else:
            print(f"You're wrong!, Current score: {current_score}")
            game_running = False
    else:
        print("Please choose correct option.")
        game_running = False
    