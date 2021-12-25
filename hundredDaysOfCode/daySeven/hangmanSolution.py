import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
guess = input("Guess a letter \n").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")