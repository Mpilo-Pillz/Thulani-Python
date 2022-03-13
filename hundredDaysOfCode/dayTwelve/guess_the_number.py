import random
from art_guess_the_number import logo

print(logo)
# print("I'm thinking of a number between 1 and 100: ")

number_to_guess = random.randint(0, 100 - 1)
number_of_tries_left = 10
difficulty = input("Type 'easy' or 'hard' for difficulty")

if difficulty == 'hard':
    number_of_tries_left = 5

user_guess = input("I'm thinking of a number between 1 and 100: ")

def checkGuess(number, user_guess):
    if number > user_guess:
        return "Your guess is too high"
    elif number < user_guess:
        return "Your guess is too low"
    else:
        return "You guess is correct"