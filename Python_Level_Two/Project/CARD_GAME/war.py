from random import shuffle
player1_name = input("Enter Player 1 Name: ")
player2_name = input("Enter Player 2 Name: ")
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITE = 'H D S C'.split()

class Deck:
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        shuffle(self.allcards)

    def split_half(self):
        return(self.allcards[:26],self.allcards[26:])

class Hand:
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contain {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

    
card = Deck()
card.shuffle()
print(card.split_half())