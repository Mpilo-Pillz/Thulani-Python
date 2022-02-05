from blackjack_art import logo
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
users_hand = []
users_score = 0

user_first_card = cards[random.randint(0, (len(cards) - 1))]
user_second_card = cards[random.randint(0, (len(cards) - 1))]
users_hand.append(user_first_card)
users_hand.append(user_second_card)

for card in users_hand:
    users_score += card

print(logo)
print(len(cards))
print(f"Your cards: {users_hand} Your score: {users_score}")
print(user_first_card )
print(user_second_card )
