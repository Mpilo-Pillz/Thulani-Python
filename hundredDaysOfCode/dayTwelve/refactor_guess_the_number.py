import random
from art_guess_the_number import logo

def checkGuess(number, user_guess):
    if number > user_guess:
        print("Your guess is too low")
        return True
    elif number < user_guess:
        print("Your guess is too high")
        return True
    else:
        print("You guess is correct. You WIN")
        return False


def play_game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Type 'easy' or 'hard' for difficulty: ")
    number_to_guess = random.randint(0, 100 - 1)
    print(f"The answer is {number_to_guess}")

    number_of_tries_left = 10

    if difficulty == 'hard':
        number_of_tries_left = 5

    game_is_not_over = True

    while game_is_not_over:
        if number_of_tries_left == 0:
            print("GAME OVER! YOU ARE OUT OF GUESSES")
            game_is_not_over = False
        else:
            print(f"You have {number_of_tries_left} attempts remaining to guess the number")
            user_guess = int(input("Make a guess: "))
            game_is_not_over = checkGuess(number_to_guess, user_guess)
            number_of_tries_left -= 1

            if (number_of_tries_left > 0):
                print("Guess again.")

play_game()