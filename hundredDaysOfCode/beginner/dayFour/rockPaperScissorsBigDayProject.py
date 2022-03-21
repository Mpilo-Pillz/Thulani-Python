import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_selection = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
computer_selection = random.randint(0, 2)

if user_selection == 0:
    print("You chose: Rock\n" + rock)

if computer_selection == 0:
    print("Computer chose: Rock\n" + rock)

if user_selection == 1:
    print("You chose: Paper\n" + paper)

if computer_selection == 1:
    print("Computer chose: Paper\n" + paper)

if user_selection == 2:
    print("You chose: Scissors\n" + scissors)

if computer_selection == 2:
    print("Computer chose: Scissors\n" + scissors)

else:
    print("INVALID INPUT!") # Not getting triggered

#     Computer selects Rock
if user_selection == 0 and computer_selection == 0:
    print("It is a DRAW: Both chose Rock it!")

elif user_selection == 1 and computer_selection == 0:
    print("YOU WIN! Paper beats rock")

elif user_selection == 2 and computer_selection == 0:
    print("YOU LOOSE! Rock beats scissors")

# computer selects paper
elif user_selection == 0 and computer_selection == 1:
    print("YOU Loose! Rock beats paper")

elif user_selection == 1 and computer_selection == 1:
    print("It is a DRAW: Both chose Paper!")

elif user_selection == 2 and computer_selection == 1:
    print("YOU WIN! Scissors beats Paper")

# computer selects scissors
elif user_selection == 0 and computer_selection == 2:
    print("YOU WIN! Rock beats Scissors")

elif user_selection == 1 and computer_selection == 2:
    print("YOU LOSE! Scissors beats Paper")

elif user_selection == 2 and computer_selection == 2:
    print("It is a DRAW: Both chose Scissors!")