from Deck import Deck
from Player import Player
import os
import time


# games main functions

def create_and_suffle_deck():
    # function that creates an instance of a deck and then shuffles it
    deck = Deck()
    print(deck)
    time.sleep(1)
    print("\nShuffling deck...")
    # variable that will store the list containing the full deck after shuffle
    shuffled_deck = deck.shuffle()
    time.sleep(1)
    print("\nDone!\n")
    return shuffled_deck


def initial_deal(player1, shuffled_deck):
    # function that will deal cards to players
    # creating an instance of a player for Dealer, assigning 2 cards from the deck
    dealer = Player([shuffled_deck.pop(), shuffled_deck.pop()])
    time.sleep(1)
    # will only print the first card and the second "face down" (X)
    print(f"\n\nDealer: ['{dealer.hand[0]}', 'XX']\n\n")
    # adding two cards to the player's hand
    player1.hand = [shuffled_deck.pop(), shuffled_deck.pop()]
    player1.score = player1.calculate_hand_score(player1.hand)
    time.sleep(1)
    print(f"Player 1 Hand: {player1.hand}")
    print(f"Player 1 Score: {player1.score}\n")
    if player1.score == 21:
        print("Blackjack!\n\n")
    return player1, dealer


def deal_dealers_hand():
    # function that will simulate the dealers play once the player stands
    print("[" + "'" + dealer.hand[0] + "'" + ", XX ]")
    time.sleep(1)
    print(dealer.hand)
    dealer.score = dealer.calculate_hand_score(dealer.hand)
    while dealer.score < player1.score:
        time.sleep(1)
        new_dealer_card = shuffled_deck.pop()
        dealer.hand.append(new_dealer_card)
        print(dealer.hand)
        dealer.score = dealer.calculate_hand_score(dealer.hand)
    print(f"Score: {dealer.score}\n\n")


# main code

game_on = "Y"
while game_on == "Y":
    os.system('cls')
    print("\n\t\tWelcome to Blackjack!\n")
    time.sleep(1)
    # creating an instance of a deck and shuffling it in case player is playing
    # for the first time or if there are less than 10 cards available
    if 'shuffled_deck' not in globals():
        shuffled_deck = create_and_suffle_deck()
    elif len(shuffled_deck) < 10:
        print("Deck is almost over. We need to shuffle again!\n")
        shuffled_deck = create_and_suffle_deck()
    # setting the default betting amount if player hasn't played before
    if 'money' not in globals():
        money = 100
    # check if user has enough money to bet (in case he has kept playing)
    if money == 0:
        print("You don't have any money left!\nGoodbye!")
        game_on = "N"
        break
    # ask for the betting amount
    player1 = Player(money=money)
    player1.set_betting_amount()
    time.sleep(1)
    # deal cards and assign each hand to the player and dealer
    player1, dealer = initial_deal(player1, shuffled_deck)
    # variable that will contain the response from the user to hit or stand
    move = ""
    while move != "S":
        move = input("Press enter to hit, enter 'S' to stand: ").upper()
        if move == "":  # User chose to hit
            print("User chose to hit")
            # a card is then removed from the shuffled deck,
            # appended to the player's hand and then printed
            player1.hand.append(shuffled_deck.pop())
            print(f"Player 1: {player1.hand}\n")
            # now the score needs to be calculated and printed as well
            player1.score = player1.calculate_hand_score(player1.hand)
            print(f"Score: {player1.score}")
            # validates if player exceeded 21 (busted)
            if player1.score > 21:
                print("Busted!")
                print(f"Bet was: {player1.bet}")
                player1.calculate_loss(player1.bet)
                print(f"Money: {player1.money}")
                break
            elif player1.score == 21:
                print("Blackjack!")
        elif move == "S":
            # add a call to a function that will play the dealer's hand and then checks who wins or if there is a tie
            print("User chose to stand")
            deal_dealers_hand()
            if dealer.score > player1.score and dealer.score <= 21:
                print("Player 1 loses!")
                player1.calculate_loss(player1.bet)
            elif dealer.score == player1.score:
                print("It's a tie!")
            else:
                print("Player 1 wins!")
                player1.calculate_win(player1.bet)
    # ask to the player if he would like to contine playing
    while True:
        game_on = input("\nYou want to play again? (Y/N): ").upper()
        if game_on == "Y" or game_on == "N":
            money = player1.money
            break
        else:
            continue
