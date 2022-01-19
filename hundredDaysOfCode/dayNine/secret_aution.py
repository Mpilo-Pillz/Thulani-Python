from secret_auction_logo import logo

print(logo)

# bids = []
bidders = {}
highestBid = 0
highestBidder = ""
thereAreMoreBids = True
while thereAreMoreBids:
    biddersName = input("What is your name? ")
    bidingAmount = input("What is your bid? ")
    bidders[biddersName] = bidingAmount

    isThereMoreBids = input("Are there any more bidders?")

    if isThereMoreBids.lower() == "no":
        thereAreMoreBids = False
print(bidders)

for bidder in bidders:
    # print(bidders[bidder])
    if int(bidders[bidder]) > highestBid:
        highestBid = int(bidders[bidder])
        highestBidder = bidder

print(f"{highestBidder} has the highest bid, bidding R{highestBid} per hour as the amount")
