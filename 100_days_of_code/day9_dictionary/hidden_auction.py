print("Welcome to the Hidden auction")
print("*****************************")

auction_bids = {}
continue_bids = True

def get_bidding_details():
    bidder_name = input("Enter your Alias: ")
    bidding_amount = int(input("Enter bidding Amount: "))
    auction_bids[bidder_name] = bidding_amount

while continue_bids:
    get_bidding_details()
    print("You Bid was Made successfully")
    user_choice = input("Is there a next bidder type 'yes' or 'no'?: ").lower()

    if user_choice == "yes":
        print("\n"*100)
    else:
        print("\n"*100)
        continue_bids = False;
        print("Thanks for making Bids...")

        highest_bidder = ""
        max_bid = 0

        for key in auction_bids:
            if max_bid < auction_bids[key]:
                max_bid=auction_bids[key]
                highest_bidder = key

        print(f'Highest Bidder of the auciton is {highest_bidder} with Bid worth {max_bid}')             

        
    