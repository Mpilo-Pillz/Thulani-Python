from art import logo
from game_data import data
import random
# Display art
print(logo)

# Generate random account game data

# Format the account data into a printable format
account_a = random.choice(data)
account_b = random.choice(data)

# check that the accounts are not the same
if account_a == account_b:
    account_b = random.choice(data)
# Ask user for a guess

# Check if user is correct
# Get the follwer count for each account
# Use if statement to check if user is correct

# Give user feedback

# Score keeping

# Make the game repeatable

# Making the account at position b be at position a

# Clear the screen