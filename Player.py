class Player():
    # class that defines a Player that starts with $100 to bet
    def __init__(self, hand=[], bet=0, score=0, money=100):
        # hand should be a list of the cards taken from the deck
        self.hand = hand
        self.bet = bet
        self.score = score
        self.money = money

    def set_betting_amount(self):
        while True:
            try:
                self.bet = int(
                    input(f"How much is your bet? (1-{self.money}): ")
                )
                if self.bet > self.money:
                    print("You don't have enough funds!")
                    continue
            except ValueError:
                print("You need to enter a valid number!")
                continue
            else:
                break

    def calculate_hand_score(self, hand):
        # function that calculates the total on a player's hand
        # min and max values in case there is an ace on the hand
        # min will be calculated with ace value as 1 and max with ace value as 11
        # at the end the closest value to 21 without exceeding it, will be returned
        # otherwise, if there was no ace, min and max are equals and any can be returned
        min = 0
        max = 0
        ace_flag = False
        for card in hand:
            if card[1] == "A" and ace_flag is True:
                min += 1
                max += 1
            elif card[1] == "A" and ace_flag is False:
                ace_flag = True
                min += 1
                max += 11
            elif card[1] == "J" or card[1] == "Q" or card[1] == "K":
                min += 10
                max += 10
            elif int(card[1:]) in range(2, 11):
                min += int(card[1:])
                max += int(card[1:])
        if max == min:
            score = min
        elif max <= 21:
            score = max
        elif max > 21:
            score = min
        return score

    def calculate_win(self, win_amount):
        # function that calculates the total amount of money after a win
        self.money += win_amount

    def calculate_loss(self, lost_amount):
        # function that calculates the total amount of money after a loss
        self.money -= lost_amount

