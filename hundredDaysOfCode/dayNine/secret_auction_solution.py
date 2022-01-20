from secret_auction_logo import logo

print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        print("--------------------Supposed to clear but clearing terminal is hard with Python----------------")