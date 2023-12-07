# Hangman game

# required import statements
import random
import hangman
import hangman_words
import os

print(hangman.logo)

stages = hangman.stages
lives = len(stages) - 1 # 6
words_list = hangman_words.word_list

# will choose random word from the list
random_word = random.choice(words_list)

# testing code
print("shhhh, the word is " + random_word)

# this blank list will get filled with blank letters, list will be of size of that randomly generated word
blank_list = []
for blank in range(0, len(random_word)):
        blank_list.append('_')

end_of_game = False

# while loop will run until game is not over; if end_of_game becomes True loop will be terminated.
while not end_of_game:
    players_guess = input("Guess a letter: ").lower()
    # command to clear console
    os.system('cls')
    
    # condition if the player guesses already guessed letter
    if players_guess in blank_list:
         print(f"You've already guessed the letter \"{players_guess}\".")

    # loop to fill the list containing blank letters with the guessed letter if it is correct
    for letter in range(0, len(random_word)):
        if players_guess == random_word[letter].lower():
            blank_list[letter] = players_guess

    # condition if player loses
    if players_guess not in random_word:
        print(f"This letter {players_guess} doesn't belong to the word.")
        print(stages[lives])
        lives -= 1
        if lives < 0:
            end_of_game = True
            print("You've lost!")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(blank_list)}")

    # condition if player wins
    if '_' not in blank_list:
         end_of_game = True
         print("You've won!")
