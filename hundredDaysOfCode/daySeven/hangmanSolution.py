import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(f"Psst the word is {chosen_word}")

display = []
word_length = len(chosen_word)

for _ in chosen_word:
    display += "_"
print(display)

guess = input("Guess a letter \n").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

