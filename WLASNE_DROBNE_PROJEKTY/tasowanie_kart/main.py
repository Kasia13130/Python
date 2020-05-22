import random
colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
figures = ["Ace", "King", "Queen", "Jack", "10", "9"]
allCards = []

for x in colors:

    for y in figures:
        allCards.append(x + y)

random.shuffle(allCards)

print(allCards)