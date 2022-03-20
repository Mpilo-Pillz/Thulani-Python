from random import randint

# Function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    else:
        print(f"You got it. The answer was {answer}.")
print("Welcome to the guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# Choose random number between 1 and 100
answer = randint(1, 100)
# Make function to set difficulty
# Let the user guess a number
guess = int(input("Make a guess:"))

# Track the number of tunrs and reduce by 1 if they get it wrong
# Repeat the guessing functionality if they get it wrong