print("Welcome to the secret auction program.")
bidding_finished = False
bidder_details = {}
highest_bidder, bid_winner = 0, ''
while not bidding_finished: 
   name = input("What is your name?: ")
   bid = int(input("What is your bid?: $"))
   bidder_details[name] = bid
   next_bidder = input("Is there any other user who wants to bid?:\n1-Yes\n2-No\n")
   if next_bidder == '2':
      bidding_finished = True
for i, j in bidder_details.items():
   bid_amount = j
   if bid_amount > highest_bidder:
      highest_bidder = bidder_details
      bid_winner = i
print(f"The bid winner is {bid_winner} with a bid of ${highest_bidder}")