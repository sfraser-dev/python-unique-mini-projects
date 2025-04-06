import random
from code008_blackjack_art import logo
from bcolors import bcolors as bcols
import sys

class Deck():
    """Class representing a deck of cards."""
    def __init__(self) -> None:
        """Deck constructor"""
        # ('suit', 'rank', blackjack strength/point value)
        self.c2: Card = Card('c', '2', 2)
        self.c3: Card = Card('c', '3', 3)
        self.c4: Card = Card('c', '4', 4)
        self.c5: Card = Card('c', '5', 5)
        self.c6: Card = Card('c', '6', 6)
        self.c7: Card = Card('c', '7', 7)
        self.c8: Card = Card('c', '8', 8)
        self.c9: Card = Card('c', '9', 9)
        self.ct: Card = Card('c', 'T', 10)
        self.cj: Card = Card('c', 'J', 10)
        self.cq: Card = Card('c', 'Q', 10)
        self.ck: Card = Card('c', 'K', 10)
        self.ca: Card = Card('c', 'A', 11)
        self.d2: Card = Card('d', '2', 2)
        self.d3: Card = Card('d', '3', 3)
        self.d4: Card = Card('d', '4', 4)
        self.d5: Card = Card('d', '5', 5)
        self.d6: Card = Card('d', '6', 6)
        self.d7: Card = Card('d', '7', 7)
        self.d8: Card = Card('d', '8', 8)
        self.d9: Card = Card('d', '9', 9)
        self.dt: Card = Card('d', 'T', 10)
        self.dj: Card = Card('d', 'J', 10)
        self.dq: Card = Card('d', 'Q', 10)
        self.dk: Card = Card('d', 'K', 10)
        self.da: Card = Card('d', 'A', 11)
        self.h2: Card = Card('h', '2', 2)
        self.h3: Card = Card('h', '3', 3)
        self.h4: Card = Card('h', '4', 4)
        self.h5: Card = Card('h', '5', 5)
        self.h6: Card = Card('h', '6', 6)
        self.h7: Card = Card('h', '7', 7)
        self.h8: Card = Card('h', '8', 8)
        self.h9: Card = Card('h', '9', 9)
        self.ht: Card = Card('h', 'T', 10)
        self.hj: Card = Card('h', 'J', 10)
        self.hq: Card = Card('h', 'Q', 10)
        self.hk: Card = Card('h', 'K', 10)
        self.ha: Card = Card('h', 'A', 11)
        self.s2: Card = Card('s', '2', 2)
        self.s3: Card = Card('s', '3', 3)
        self.s4: Card = Card('s', '4', 4)
        self.s5: Card = Card('s', '5', 5)
        self.s6: Card = Card('s', '6', 6)
        self.s7: Card = Card('s', '7', 7)
        self.s8: Card = Card('s', '8', 8)
        self.s9: Card = Card('s', '9', 9)
        self.st: Card = Card('s', 'T', 10)
        self.sj: Card = Card('s', 'J', 10)
        self.sq: Card = Card('s', 'Q', 10)
        self.sk: Card = Card('s', 'K', 10)
        self.sa: Card = Card('s', 'A', 11)
        # a deck (list) of card classes
        self.full_deck: list  = [self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.ct,self.cj,self.cq,self.ck,self.ca]
        self.full_deck += [self.d2,self.d3,self.d4,self.d5,self.d6,self.d7,self.d8,self.d9,self.dt,self.dj,self.dq,self.dk,self.da]
        self.full_deck += [self.h2,self.h3,self.h4,self.h5,self.h6,self.h7,self.h8,self.h9,self.ht,self.hj,self.hq,self.hk,self.ha]
        self.full_deck += [self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.st,self.sj,self.sq,self.sk,self.sa]

    def __str__(self) -> str:
        """Deck string dunder."""
        the_str: str = ''
        for card in self.full_deck:
            the_str = the_str + card.shorthand + ' '
        return the_str

class Card():
    """Class representing a single playing card."""
    def __init__(self, suit: str, rank: str, simple_strength_value: int) -> None:
        """Card constructor."""
        self.suit: str = suit
        self.rank: str= rank
        self.simple_strength_value: int = simple_strength_value
        self.shorthand: str = f'{self.suit}{self.rank}'

    def __str__(self) -> str:
        """Card string dunder,"""
        return self.shorthand

class Hand():
    """Class representing the blackjack hand of the player or dealer."""
    def __init__(self, owner: str, card1: Card, card2: Card) -> None:
        """Hand constructor,"""
        self.owner: str = owner
        self.the_cards: list = [card1, card2]
        self.score: int = 0
        self.aces_counter: int = 0
        for c in self.the_cards:
            self.score += c.simple_strength_value
            if c.simple_strength_value == 11:   # ace
                self.aces_counter += 1

    def __str__(self) -> str:
        """Hand string dunder."""
        str1: str = (f"{(self.owner).title()}'s hand: ")
        str2: str =''
        for c in self.the_cards:
            str2 += str(c) 
            str2 += ' '
        match self.owner:
            case "player":
                str3: str = f"{str1}{bcols.WARNING}{str2}{bcols.ENDC}(score: {self.score})"
            case "dealer":
                str3: str = f"{str1}{bcols.OKBLUE}{str2}{bcols.ENDC}(score: {self.score})"
            case _: 
                print(f"{bcols.FAIL}Error: unknown owner", file=sys.stderr)
                sys.exit()

        return str3

    def twist(self, new_card: Card) -> None:
        """Method representing a player twisting in balckjack."""
        self.the_cards.append(new_card)
        # handle aces
        if new_card.rank == 'A':
            self.aces_counter += 1
        self.score += new_card.simple_strength_value
    
    def adjust_score_for_aces(self) -> None:
        """Method to account for aces (can be 1 or 11) when calculating the score."""
        while self.score > 21 and self.aces_counter > 0:
            self.score -= 10
            self.aces_counter -= 1

class Money():
    """Class to keep track of the player's money."""
    def __init__(self, amount: int) -> None:
        self.amount: int = amount
    
    def __str__(self) -> str:
        """Money dunder."""
        return (f'${self.amount}')
    
    def decrease_amount(self, bet_size: int) -> None:
        """Method to decrease the player's money."""
        self.amount -= bet_size
        print(f'\n----------\n\nPlayer has ${self.amount}')
        if self.amount > 0:
            print(f'Bet per game is ${bet_size}')

    def increase_amount(self, bet_size: int, double_win: str = "") -> None:
        """Method to increase the player's money."""
        self.amount += bet_size
        if double_win == "double_size":
            bet_size /= 2   # player gets double winnings for hitting blackjack
        print(f'\n----------\n\nPlayer has ${self.amount}')
        print(f'Bet per game is ${bet_size}')

def human_play_blackjack(hand: Hand, deck: Deck) -> int:
    """Function to implement the player playing blackjack."""
    hand.adjust_score_for_aces()
    print(hand)

    if hand.score >= 21:
        return hand.score

    # human gameplay loop
    while True:
        # checking user input loop
        while True:
            try: # possibly an exception from this block
                stick_or_twist: str = input("Stick 's' or twist 't'? ").lower()
                if stick_or_twist == 's' or stick_or_twist == 't': 
                    break
            except Exception as e: # handle exception if thrown
                print(e)
                continue
            else: # if no exception thrown, exceute this block
                print(f"{bcols.FAIL}input either 's' to stick or 't' to twist{bcols.ENDC}")
                continue

        if stick_or_twist == 's':
            return hand.score
        else:
            hand.twist(deck.full_deck.pop())
            hand.adjust_score_for_aces()
            print(hand)
            if hand.score >= 21:
                return hand.score

def dealer_play_blackjack(hand: Hand, deck: Deck) -> int:
    """Function to implement the dealer playing blackjack."""
    hand.adjust_score_for_aces()
    print(hand)

    # dealer gameplay loop
    while True:
        if hand.score >= 17:
            return hand.score
        hand.twist(deck.full_deck.pop())
        hand.adjust_score_for_aces()
        print(hand)

def check_for_two_card_21(hand: Hand) -> bool:
    """Function to test if the first two dealt cards hit blackjack (21)."""
    if len(hand.the_cards) == 2 and hand.score == 21:
        return True
    else:
        return False

if __name__ == '__main__':
    """Main function."""
    # player's money
    player_money: Money = Money(10)
    bet_per_game: int = 2

    # keep playing games of blackjack loop
    play_again_loop: bool = True
    while play_again_loop == True:
        # print the blackjack logo
        print(logo)
        print("Let's play blackjack!")
        print("Dealer hits until 17")
        print("Aces count as 1 or 11\n\n----------\n")
        print(f"Player has ${player_money.amount}")
        print(f"Bet per game is ${bet_per_game}\n\n----------\n")
        # get a deck of cards and shuffle it
        deck: Deck = Deck()
        random.shuffle(deck.full_deck)
        # deal the first two cards to player and the dealer (hide one of the dealer's cards)
        card_one: Card = deck.full_deck.pop()
        card_two: Card = deck.full_deck.pop()
        card_three: Card = deck.full_deck.pop()
        card_four: Card = deck.full_deck.pop()
        player_hand: Hand = Hand('player', card_one, card_three)
        dealer_hand: Hand = Hand('dealer', card_two, card_four)
        # show one of the dealer's cards
        print(f"Dealer's hand: {bcols.OKBLUE}{dealer_hand.the_cards[0].shorthand} XX{bcols.ENDC}\n\n----------\n")

        # checking to see if player wins immediately for having blackjack
        player_immediate_21: bool = check_for_two_card_21(player_hand)
        dealer_immediate_21: bool = check_for_two_card_21(dealer_hand)
        if player_immediate_21 == True:
            if dealer_immediate_21 == True:
                print(f'{bcols.OKCYAN}Player and dealer both get immediate blackjack - draw{bcols.ENDC}')
            else:
                print(f'{bcols.OKGREEN}Player gets blackjack - player wins double!{bcols.ENDC}')
                player_money.increase_amount(bet_per_game*2, "double_size")
            continue

        human_score: int = human_play_blackjack(player_hand, deck)
        print(f"{(player_hand.owner).title()}'s final score is: {bcols.WARNING}{player_hand.score}{bcols.ENDC}\n----------\n")
        if (human_score) > 21:
            print(f'{bcols.FAIL}Player bust - dealer wins!{bcols.ENDC}')
            player_money.decrease_amount(bet_per_game)
        else:
            dealer_score: int = dealer_play_blackjack(dealer_hand, deck)
            print(f"{(dealer_hand.owner).title()}'s final score is: {bcols.OKBLUE}{dealer_hand.score}{bcols.ENDC}\n----------\n")
            if dealer_score > 21:
                print(f'{bcols.OKGREEN}Dealer bust - player wins!{bcols.ENDC}')
                player_money.increase_amount(bet_per_game)

        if human_score <= 21 and dealer_score <= 21:
            print(f'\n--------\nPlayer has {bcols.WARNING}{player_hand.score}{bcols.ENDC}')
            print(f'Dealer has {bcols.OKBLUE}{dealer_hand.score}{bcols.ENDC}')
            if (human_score > dealer_score):
                print(f'{bcols.OKGREEN}Player wins!{bcols.ENDC}')
                player_money.increase_amount(bet_per_game)
            else:
                print(f'{bcols.FAIL}Dealer wins!{bcols.ENDC}')
                player_money.decrease_amount(bet_per_game)

        if player_money.amount < bet_per_game:
            print(f"{bcols.FAIL}Player doesn't have enough money to play - the casino always wins - bye!{bcols.ENDC}\n")
            break
        print('')
        # checking user input loop to see if they want to continue playing
        while True:
            try: # possibly an exception from this block
                again: str = input("Do you want to play again? 'y' or 'n': ").lower()
                if again == 'y' or again == 'n':
                    break
            except Exception as e: # handle exception if thrown 
                print(e) 
                continue
            else: # if no exception thrown, execute this block
                print(f'{bcols.FAIL}please input y or n{bcols.ENDC}') 
                continue

        if again == 'n':
            play_again_loop = False
