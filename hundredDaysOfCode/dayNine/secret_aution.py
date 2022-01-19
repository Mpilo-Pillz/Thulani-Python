from secret_auction_logo import logo

print(logo)

bids = []
bidder = {}
thereAreMoreBids = True
while thereAreMoreBids:
    biddersName = input("What is your name? ")
    bidingAmount = input("What is your bid? ")
    bidder["name"] = biddersName
    bidder["amount"] = bidingAmount
    bids.append(bidder)
    thereAreMoreBids = False
print(bids)
