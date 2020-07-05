colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
figures = [
    {"Figure": "Ace", "Power": 14},
    {"Figure": "King", "Power": 13},
    {"Figure": "Queen", "Power": 12},
    {"Figure": "Jack", "Power": 11},
    {"Figure": "10", "Power": 10},
    {"Figure": "9", "Power": 9}]

allCards = []
for color in colors:
    for figure in figures:

        aCard = figure.copy()
        aCard["Color"] = color
        allCards.append(aCard)

import random
random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]

print("Cards of player1:", player1, "\n", "Cards of player2:", player2)


while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)  # dlaczego zero?
    card2 = player2.pop(0)

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        print("Equal! \t %10d \t %2d \t" % (card1["Power"], card2["Power"]) + len(player1) * "*")
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print("Player 1 won! \t %2d \t %2d \t" % (card1["Power"], card2["Power"]) + len(player1) * "*")
    elif card1["Power"] < card2["Power"]:
        player2.append(card1)
        player2.append(card2)
        print("Player 2 won! \t %2d \t %2d \t" % (card1["Power"], card2["Power"]) + len(player1) * "*")

if len(player1) > 0:
    print("Player1 won!")
elif len(player2) > 0:
    print("Player2 won!")