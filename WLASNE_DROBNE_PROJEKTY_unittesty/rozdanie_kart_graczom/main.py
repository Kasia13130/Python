import random
colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
figures = ["Ace", "King", "Queen", "Jack", "10", "9"]
allCards = []


for x in colors:

    for y in figures:
        allCards.append(x + y)
        player1 = []
        player2 = []
        max = len(allCards)

        for i in range(max):
            if i % 2 == 0:
                player1.append(allCards[i])
            else:
                player2.append(allCards[i])

        random.shuffle(allCards)

print("Cards of player 1: %s \nCards of player 2: %s" % (player1, player2))

# II sposob rozdania
colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
figures = ["Ace", "King", "Queen", "Jack", "10", "9"]
allCards = []

for x in colors:

    for y in figures:
        allCards.append(x + y)
        player1 = allCards[0:11]

        player2 = allCards[12:24]

    random.shuffle(allCards)

print("Cards of player 1: %s" % (player1), "\n", "Cards of player 2: %s" % (player2))