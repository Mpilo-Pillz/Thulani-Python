from secret_auction_logo import logo

print(logo)

bids = []
bidder = {}
thereAreMoreBids = True
while thereAreMoreBids:
    biddersName = input("What is your name? ")
    bidingAmount = input("What is your bid? ")
    bidder[biddersName] = bidingAmount

    isThereMoreBids = input("Are there any more bidders?")

    if isThereMoreBids.lower() == "no":
        thereAreMoreBids = False
print(bidder)
