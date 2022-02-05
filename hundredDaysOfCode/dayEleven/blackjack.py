from blackjack_art import logo
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
users_hand = []
computers_hand = []
users_score = 0

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


print(logo)
print(f"Your cards: {users_hand} Your score: {players_hand(users_score, users_hand) }")
# print(f"Computers cards: {users_hand} Your score: {users_score}")

