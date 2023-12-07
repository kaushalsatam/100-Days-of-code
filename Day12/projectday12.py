# Number guessing game

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100")
computer_guess = random.randint(1, 100)
# print(f"Pssst, the correct answer is {computer_guess}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 10
if difficulty == 'hard':
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > computer_guess:
        print("Too High")
    elif guess < computer_guess:
        print("Too Low")
    else:
        print(f"You got it, the answer was {computer_guess}")
        break
    attempts -= 1
if attempts == 0:
    print("You've ran out of guesses, you lost.")