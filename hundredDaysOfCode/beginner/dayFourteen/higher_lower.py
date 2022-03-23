from art import logo, vs
from game_data import data
from random import randint

correct_answer = ''
print(logo)
option_a = data[randint(0, len(data) - 1)]
option_b = data[randint(0, len(data) - 1)]
print(f'compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}')
print(vs)
print(f'compare B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}')

# user_option = input("Who has more followers? Type 'A' or 'B': ")

if option_a['follower_count'] < option_b['follower_count']:
    correct_answer = 'B'
else:
    correct_answer = 'A'

print(correct_answer)