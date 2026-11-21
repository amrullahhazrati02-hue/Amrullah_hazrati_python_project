
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
again = True

while again:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))

    bids[name] = price

    other_bidders = input("Are there any other bidders? yes/no: ").lower()

    if other_bidders == "no":
        again = False
        find_highest_bidder(bids)

    elif other_bidders == "yes":
        print("\n" * 20)
