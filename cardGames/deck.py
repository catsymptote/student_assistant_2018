import card
import random

class deck:
    cards = []

    def __init__(self):
        None


    def sortValue(self):
        for i in range(len(self.cards) - 1):
            for j in range(len(self.cards) - 1):
                # Check if value is bigger
                if (self.cards[j].value > self.cards[j + 1].value):
                    # Card swap
                    tmp = self.cards[j]
                    self.cards[j] = self.cards[j + 1]
                    self.cards[j + 1] = tmp


    def sortPattern(self):
        for i in range(len(self.cards) - 1):
            for j in range(len(self.cards) - 1):
                # Check if pattern is bigger
                if (self.cards[j].pattern > self.cards[j + 1].pattern):
                    # Card swap
                    tmp = self.cards[j]
                    self.cards[j] = self.cards[j + 1]
                    self.cards[j + 1] = tmp


    def sortFull(self):
        # Sort pattern
        self.sortPattern()

        # Sort values within pattern
        for i in range(len(self.cards) - 1):
            for j in range(len(self.cards) - 1):
                # Check if patterns are the same
                if (self.cards[j].pattern == self.cards[j + 1].pattern):
                    # Check if value is ordered
                    if (self.cards[j].value > self.cards[j + 1].value):
                        # Card swap
                        tmp = self.cards[j]
                        self.cards[j] = self.cards[j + 1]
                        self.cards[j + 1] = tmp


    def shuffle(self):
        tmpCards = []
        while (len(self.cards) > 0):
            rand = random.randint(0, len(self.cards) - 1)
            tmpCards.append(self.cards[rand])
            del self.cards[rand]
        self.cards = tmpCards


    # Reset deck.
    def fill(self):
        for pattern in range(1, 4+1):
            for value in range(1, 13+1):
                self.cards.append(card.card(value, pattern))


    def clear(self):
        del self.cards[:]


    # Initialize new card, and place on top of deck.
    def addCard(self, value, pattern):
        self.cards.append(card.card(value, pattern))


    # Returns and remove top card from deck.
    def getCard(self):
        return self.cards.pop()

    # Return, but do not remove, the top card.
    def showCard(self):
        return (self.cards[len(self.cards) - 1])

    # Prints the entire deck. mostly for debug purposes.
    def printDeck(self):
        for i in range(len(self.cards)):
            print(self.cards[i].getChars())


"""
dck = deck()
dck.printDeck()
dck.shuffle()
print()
dck.printDeck()
"""