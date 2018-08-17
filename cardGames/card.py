class card:
    valueChars = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    valueNames = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    patternChars = ["♠", "♥", "♣", "♦"]
    #patternChars = ["<3-", "<3", "<>", "*3"]
    patternNames = ["Spades", "Hearts", "Clubs", "Diamonds"]

    value = None    # 1 - 13
    pattern = None  # 1 - 4

    def __init__(self, value, pattern):
        self.value = value
        self.pattern = pattern


    # Get: ♠, ♥, ♦, ♣
    def getPatternChar(self):
        return self.patternChars[self.pattern -1]
    
    # Get: Spades, Hearts, Clubs, Diamonds
    def getPatternName(self):
        return self.patternNames[self.pattern -1]

    # Get: A, 1, 2.., 10, J, Q, K
    def getValueChar(self):
        return self.valueChars[self.value -1]
    
    # Get: Ace, 1, 2.., 10, Jack, Queen, King
    def getValueName(self):
        return self.valueNames[self.value -1]
    

    def getNames(self):
        return (self.getValueName() + " of " + self.getPatternName())

    def getChars(self):
        return (self.getValueChar() + " " + self.getPatternChar())