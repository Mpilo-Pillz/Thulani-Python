from random import randint
from art_guess_the_number import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# turns = 0
# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """ Checks answer against guess and returns number og guesses remaining """
    if guess > answer:
        print("Too High")
        # global turns
        # turns -= 1
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
        # turns -= 1
    else:
        print(f"You got it. The answer was {answer}.")

# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the number guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Choose random number between 1 and 100
    answer = randint(1, 100)
    print(f"Psst, the answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")


# Track the number of tunrs and reduce by 1 if they get it wrong

game()