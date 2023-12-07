# Hangman game

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

words_list = ['Banana', 'Python', 'Datascience', 'Django', 'Javascript', 'Java', 'Spring', 'GOAT', 'Virat', 'Camel', 'Ronaldo', 'Burger', 'Messi']

random_word = random.choice(words_list)

# testing code
print(random_word)

# random_word_list = []
# for l in random_word:
#     random_word_list.append(l)

# # testing code
# print(random_word_list)

blank_list = []
for blank in range(0, len(random_word)):
        blank_list.append('_')

end_of_game = False
stage = len(stages) - 1


while not end_of_game:
    players_guess = input("Guess the letter that can be in the this word: ").lower()
    
    # print(blank_list)
    for letter in range(0, len(random_word)):
        if players_guess == random_word[letter].lower():
            blank_list[letter] = players_guess
    print(stages[stage])
    stage -= 1
    
    if '_' not in blank_list:
        end_of_game = True
        print("You've won!")
