import os
clear = lambda: os.system('cls')

bids = {}
bididng_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bididng_finished:
    name = input("What is your name")
    price = int(input("What is your bid"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type yes or no")
    if should_continue == "no":
        bididng_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()