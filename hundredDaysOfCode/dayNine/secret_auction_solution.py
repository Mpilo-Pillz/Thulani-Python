from secret_auction_logo import logo

print(logo)

bids = {}
biffing_finished = False

while not biffing_finished:
    name = input("What is your name?")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        biffing_finished = True