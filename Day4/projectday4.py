# Rock Paper Scissor

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if your_choice >= len(choices):
    print("Invalid choice. You Lose.")
else:
    print(f"You chose: \n {choices[your_choice]}")

computer_choice = random.randint(0, 2)

print(f"Computer chose: \n{choices[computer_choice]}")

if your_choice == computer_choice:
    print("It's a Draw!")
elif (your_choice == 0 and computer_choice == 1) or (your_choice == 1 and computer_choice == 2) or (your_choice == 2 and computer_choice == 0):
    print("You Lose.")
elif (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice == 1):
    print("You Win!!")
else:
    print("Choose appropriate choice to play. Try again.")