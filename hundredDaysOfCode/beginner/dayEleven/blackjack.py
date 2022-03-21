from blackjack_art import logo
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
users_hand = []
computers_hand = []
users_score = 0
computers_score = 0
black_jack = 21


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

def print_user_hand(users_hand, users_score):
    print(f"Your cards: {users_hand} Your score: {users_score}")

def print_computer_hand(computers_hand, computers_score):
    print(f"-----------DUBUG-----Computers cards: {computers_hand} Computer score: {computers_score}-------------")
    print(f"Computers first hand: {computers_hand[0]}")

computers_score = players_hand(computers_score, computers_hand)
users_score = players_hand(users_score, users_hand)
print(logo)


def black_jack_game(users_score, computers_score):
    game_is_on = True

    while game_is_on:
        print_user_hand(users_hand, users_score)
        print_computer_hand(computers_hand, computers_score)
        hit_user = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit_user.lower() == 'y':
            users_hand.append(cards[random.randint(0, (len(cards) - 1))])
            computers_hand.append(cards[random.randint(0, (len(cards) - 1))])
            computers_score += computers_hand[-1]
            users_score += users_hand[-1]

            if users_score > 21:
                print("You went over, YOU Lose")
                game_is_on = False
                print_user_hand(users_hand, users_score)
                print_computer_hand(computers_hand, computers_score)
                return
            if computers_score > 21:
                print("You WIN,computer over")
                game_is_on = False
                print_user_hand(users_hand, users_score)
                print_computer_hand(computers_hand, computers_score)
                return
            if users_score == black_jack:
                print("You WIN by BLACKJACK")
                game_is_on = False
                print_user_hand(users_hand, users_score)
                print_computer_hand(computers_hand, computers_score)
                return
            if computers_score > 21:
                print("You Lose,computer got BLACKJACK")
                game_is_on = False
                print_user_hand(users_hand, users_score)
                print_computer_hand(computers_hand, computers_score)
                return
            black_jack_game(users_score, computers_score)
        else:
            game_is_on = False
            if users_score == 21:
                print("You win you scored Black Jack 😃")
            elif computers_score == 21:
                print("You lose computer scored Black Jack 😫")
            if int(users_score) > int(computers_score) and users_score <= black_jack:
                print("You win 😃")
            elif int(users_score) < int(computers_score) and computers_score <= black_jack:
                print("You Lose 😭")
            else:
                print("It is a Draw 😱")


black_jack_game(users_score, computers_score)

