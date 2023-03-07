class Deck():
    # class that defines a deck to be used in the game
    def __init__(self):
        # initialization of a full ordered deck with suits and cards
        self.suits = ['C', 'H', 'D', 'S']
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.full_deck = []
        for suit in self.suits:
            for card in self.cards:
                self.full_deck.append(suit + card)

    def __str__(self):
        # string representation that returns the whole deck in a list format
        clubs = []
        hearts = []
        diamonds = []
        spades = []
        for suit in self.suits:
            for card in self.cards:
                if suit == "C":
                    clubs.append(suit + card)
                elif suit == "H":
                    hearts.append(suit + card)
                elif suit == "D":
                    diamonds.append(suit + card)
                else:
                    spades.append(suit + card)
        return ("Here is the full deck: \n\n"
                f"Clubs: {clubs}\n"
                f"Hearts: {hearts}\n"
                f"Diamonds: {diamonds}\n"
                f"Spades: {spades}")

    def shuffle(self):
        # function that shuffles the deck
        deck_as_set = set(self.full_deck)
        return list(deck_as_set)
