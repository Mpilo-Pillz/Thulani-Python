from blackjack_art import logo
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
users_hand = []
computers_hand = []
users_score = 0
computers_score = 0

user_first_card = cards[random.randint(0, (len(cards) - 1))]
user_second_card = cards[random.randint(0, (len(cards) - 1))]
computer_second_card = cards[random.randint(0, (len(cards) - 1))]
computer_first_card = cards[random.randint(0, (len(cards) - 1))]

users_hand.append(user_first_card)
users_hand.append(user_second_card)
computers_hand.append(computer_first_card)
computers_hand.append(computer_second_card)

def players_hand(player_score, players_hand):
    for card in players_hand:
        player_score += card
    return player_score

computers_score = players_hand(computers_score, computers_hand)
users_score = players_hand(users_score, users_hand)
print(logo)
print(f"Your cards: {users_hand} Your score: {users_score}")
print(f"-----------DUBUG-----Computers cards: {computers_hand} Computer score: {computers_score}-------------")
print(f"Computers first hand: {computers_hand[0]}")

if int(users_score) > int(computers_score):
    print("You win 😃")
elif int(users_score) < int(computers_score):
    print("You Lose 😭")
else:
    print("It is a Draw 😱")
# Get the winner by random
# add option to hit
#  - append to user score
# Randomly tell computer to hit or not
#  - hit if hand  17 or less
#   - hit id user has hand grater than 9 and is less than 17

# while yes
# terminate on no


