import random
from art_guess_the_number import logo

print(logo)
# print("I'm thinking of a number between 1 and 100: ")

number_to_guess = random.randint(0, 100 - 1)

number_of_tries_left = 10
difficulty = input("Type 'easy' or 'hard' for difficulty: ")

if difficulty == 'hard':
    number_of_tries_left = 5

game_is_not_over = number_of_tries_left > 0

# def checkGuess(number, user_guess):
#     if number > user_guess:
#         return "Your guess is too low"
#     elif number < user_guess:
#         return "Your guess is too high"
#     else:
#         return "You guess is correct. You WIN"

while game_is_not_over:
    user_guess = int(input("I'm thinking of a number between 1 and 100: "))
    print(f"The answer is {number_to_guess}")
    if number_of_tries_left == 0:
        game_is_not_over = False
    if number_to_guess > user_guess:
        number_of_tries_left -= 1
        print(f"number of guesses left: {number_of_tries_left}")
        print("Your guess is too Low")
    elif number_to_guess < user_guess:
        number_of_tries_left -= 1
        print(f"number of guesses left: {number_of_tries_left}")
        print("Your guess is too High")
    else:
        print("You guess is correct. You WIN")
        game_is_not_over = False
