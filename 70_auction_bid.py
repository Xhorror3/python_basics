#HINT: You can call clear() to clear the output in the console.
from auction_bid_art import logo
print(logo)

bid_dict={}
bid_finished=False

def highest_bidder(bidding_record):
  highest_bid=0
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bid_finished:
  name=input("What's your name?:")
  bid=int(input("What's your bid?: $"))
  bid_dict[name]=bid
  more_bid=input("Are there any other bidders?(yes/no)")
  if more_bid=="no":
    bid_finished=True
    highest_bidder(bid_dict)
  elif more_bid=="yes":

