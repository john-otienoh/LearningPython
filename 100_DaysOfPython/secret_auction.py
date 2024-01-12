#from replit import clear
print("Welcome to the secret auction program.")
bidding_finished = False
while not bidding_finished: 
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder_details = {}
    bidder_details[name] = bid
    next_bidder = input("Is there any other user who wants to bid?:\n1-Yes\n2-No\n")
    if next_bidder == 1:
       bidding_finished = False
    else:
        
    print(bidder_details)