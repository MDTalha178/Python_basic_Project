from art import logo
import clear
print(logo)



bid = {}

def highest_biddres(bidders_record):
    high_bids = 0
    winner = ""
    for bidder in bidders_record:
        bid_amount = bidders_record[bidder]
        if bid_amount > high_bids:
            high_bids = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of {high_bids}")


bid_finished = False
while bid_finished !=True:
   name = input("Enter your name: ")
   price = int(input("Enter your bid:  $"))
   bid[name] = price

   choice = input("Hey! there is any other bidders Yes or No").lower()
   if choice == "no":
       bid_finished = True
       highest_biddres(bid)
   elif choice == "yes":
       clear()

