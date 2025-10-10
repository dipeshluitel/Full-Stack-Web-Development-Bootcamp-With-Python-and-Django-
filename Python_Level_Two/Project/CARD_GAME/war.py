from random import shuffle
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

class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        draw_card = self.hand.remove_card()
        print("{} has placed: {}\n".format(self.name,draw_card))
        return draw_card
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
        
    def still_has_card(self):
        """
        Return true if player still has card left
        """
        return len(self.hand.cards) !=0 
    
print("Welcome to War, Let's begin...")
    
card = Deck()
card.shuffle()
half1, half2 = card.split_half()

comp = Player("computer",Hand(half1))

name = input("Enter Player 1 Name: ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_card() and comp.still_has_card():
    total_rounds+=1
    print("Time for a new round!")
    print("Here are the current standing")
    print(f"{user.name} has the count: {str(len(user.hand.cards))}")
    print(f"{comp.name} has the count: {str(len(comp.hand.cards))}")
    print("Play a Card!")

    print("\n")

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count+=1

        print("War")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
         if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
         else:
            comp.hand.add(table_cards)

print(f"Game over, number of rounds {str(total_rounds)}")
print(f"A war happened {str(war_count)} time")

print(f" {user.name} still has cards: {user.still_has_card()}")
print(f" Computer still has cards: {comp.still_has_card()}")