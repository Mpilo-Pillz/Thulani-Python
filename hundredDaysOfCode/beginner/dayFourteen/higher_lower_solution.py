from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Format the account data into a printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
# Display art
print(logo)

# Generate random account game data
account_a = random.choice(data)
account_b = random.choice(data)

# check that the accounts are not the same
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Compare B: {format_data(account_b)}")

# Ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct
# Get the follwer count for each account
# Use if statement to check if user is correct

# Give user feedback

# Score keeping

# Make the game repeatable

# Making the account at position b be at position a

# Clear the screen