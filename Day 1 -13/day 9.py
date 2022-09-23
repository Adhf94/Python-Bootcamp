logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


bids={}
biddig_finished = False

def higest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for person in bidding_record:
        bid_amount = bidding_record[person]
        if bid_amount > highest_bid:
            highest_bid  = bid_amount
            winner = person
    print(f"The winner is {winner} with a bid of $ {highest_bid}")
    


while not biddig_finished:
    print(logo)
    bidder= input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    bids[bidder] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "no":
        biddig_finished = True
        higest_bidder(bids)
    elif should_continue == "yes":
        bidding_finished = False
