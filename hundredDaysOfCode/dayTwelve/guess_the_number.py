from art_guess_the_number import logo

print(logo)
print("I'm thinking of a number between 1 and 100")

def checkGuess(number, user_guess):
    if number > user_guess:
        return "Your guess is too high"
    elif number < user_guess:
        return "Your guess is too low"
    else:
        return "You guess is correct"