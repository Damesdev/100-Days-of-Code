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
from replit import clear

#HINT: You can call clear() to clear the output in the console.
bids = {}
def add_new_bid(bidder_name, bid_price):
  bids[bidder_name] = bid_price

end_bidding = False
print(logo)
while end_bidding == False:
  #name of bidder
  name = input("What is your name? ")

  #bidder's price
  price = int(input("What is your bid? $"))

  #add to dictionary 'bids'
  add_new_bid(name,price)

  #Checking if more bidders with error saving
  correct_bidders_response = False

  while correct_bidders_response == False:
    more_bidders = input("Are there any other bidders? Type 'Yes' or 'No'\n").lower()
  #Clear console for next bidder information
    if more_bidders == 'yes':
      clear()
      correct_bidders_response = True
  # Find highest bidder after last bidder entered.
    elif more_bidders == 'no':
      highest_bid = 0
      highest_bidder = ''
      for bidder in bids:
        set_bid = int(bids[bidder])
        if set_bid > highest_bid:
          highest_bidder = bidder
          highest_bid = set_bid
      clear()
      print(f"Congratulations {highest_bidder} you won with a bet of ${highest_bid}!")
      correct_bidders_response = True
      end_bidding = True
    else:
      print("That is not a valid option")