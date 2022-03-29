from art import logo, vs
from game_data import data
from random import randint

correct_answer = ''
score = 0
print(logo)
option_a = data[randint(0, len(data) - 1)]
option_b = data[randint(0, len(data) - 1)]
game_is_on = True

while game_is_on:
    if option_a['follower_count'] < option_b['follower_count']:
        correct_answer = 'B'
    else:
        correct_answer = 'A'

    print(f"Correct answer {correct_answer}")
    print(f'compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}')
    print(vs)
    print(f'compare B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}')

    user_option = input("Who has more followers? Type 'A' or 'B': ")

    if user_option.upper() == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")
        option_a = option_b
        option_b = data[randint(0, len(data) - 1)]
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_is_on = False
