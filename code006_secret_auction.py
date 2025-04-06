import os
from code006_secret_auction_art import logo
from bcolors import bcolors as bcols

def clear() -> None:
    """Cross-platform clear screen function"""
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record: dict) -> None:
    """Find highest bidder from the dictionary."""
    highest_bid = 0
    winner = ""
    # bidding_record = {"Alice": 123, "Bob": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe winner of the auction is {bcols.OKGREEN}{winner}{bcols.ENDC} with a bid of {bcols.OKGREEN}${highest_bid}{bcols.ENDC}.\n")

bids = {}   # dictionary of bids
bidding_finished = False

if __name__ == "__main__":
    """Main function."""

    print(logo)

    while not bidding_finished:
        while True:
            try:
                name = input("\nWhat is your name?: ")
                if type(name) == str:
                    break
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{bcols.FAIL}Please input a your name.{bcols.ENDC}.")
                continue

        while True:
            try:
                price = int(input(f"\n{name}, what is your bid?: $"))
                if type(price) == int:
                    break
            except ValueError as ve:
                print(ve)
                continue
            else:
                print(f"{bcols.FAIL}Please input your bid as an integer.{bcols.ENDC}")
                continue

        bids[name] = price
        while True:
            try: 
                should_continue = input("\nAre there any other bidders? Type 'yes' ('y') or 'no' ('n'): ").lower()
                if should_continue == "no" or should_continue == "n":
                    bidding_finished = True
                    find_highest_bidder(bids)
                    break
                elif should_continue == "yes" or should_continue == "y":
                    clear()
                    break
            except Exception as e:
                print(e)
                continue
            else: 
                print(f"{bcols.FAIL}Please type 'yes', 'y', 'no' or 'n'{bcols.ENDC}")
                continue