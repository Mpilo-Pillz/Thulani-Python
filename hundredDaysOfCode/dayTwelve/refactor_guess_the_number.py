import random
from art_guess_the_number import logo

def checkGuess(number, user_guess):
    if number > user_guess:
        return "Your guess is too low"
    elif number < user_guess:
        return "Your guess is too high"
    else:
        return "You guess is correct. You WIN"


def play_game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Type 'easy' or 'hard' for difficulty: ")
    number_to_guess = random.randint(0, 100 - 1)
    print(f"The answer is {number_to_guess}")

    number_of_tries_left = 10

    if difficulty == 'hard':
        number_of_tries_left = 5

    game_is_not_over = number_of_tries_left > 0

    while game_is_not_over:
        if number_of_tries_left == 0:
            game_is_not_over = False
            print("GAME OVER! YOU ARE OUT OF GUESSES")
        # else:

        print(f"You have {number_of_tries_left} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        # print(f"The answer is {number_to_guess}")
        print(checkGuess(number_to_guess, user_guess))
        print("Guess again.")
        number_of_tries_left -= 1

play_game()