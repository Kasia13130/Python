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
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    stack = []

    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:
            print("War is going on", "\t", card1["Power"], "\t", card2["Power"], "\n")
            stack.append(card1)
            stack.append(card2)

            if len(player1) < 2:
                player2.extend(stack)       # extend to funkcja dodajaca nowa liste do poprzedniej
                player2.extend(player1)
                player1 = []
                print("Player 2 won!", "\t", "Player 1: %2d" % (card1["Power"]), len(player1) * "*", "\t", "Player 2: %2d" % (card2["Power"]), len(player2) * "*", "\n")
                break
            elif len(player2) < 2:
                player1.extend(stack)
                player1.extend(player2)
                player2 = []
                print("Player 1 won!", "\t", "Player 2: %2d" % (card2["Power"]), len(player2) * "*", "\t", "Player 1: %2d" % (card1["Power"]), len(player1) * "*", "\n")
                break
            elif len(player1) >= 2 and len(player2) >= 2:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                print("The war!", "\t", "Player 1: %2d" % (card1["Power"]), len(player1) * "*", "\t", "Player 2: %2d" % (card2["Power"]), len(player2) * "*", "\n")
        else:
            if card1["Power"] > card2["Power"]:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print("Player 1 won!", "\t", "Player 1: %2d" % (card1["Power"]), len(player1) * "*", "\t", "Player 2: %2d" % (card2["Power"]), len(player2) * "*", "\n")
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print("Player 2 won!", "\t", "Player 1: %2d" % (card1["Power"]), len(player2) * "*", "\t", "Player 2: %2d" % (card2["Power"]), len(player1) * "*", "\n")

    else:
        if card1["Power"] > card2["Power"]:
            stack.append(card1)
            stack.append(card2)
            player1.extend(stack)
            print("Player 1 won!", "\t", "Player 1: %2d" % (card1["Power"]), len(player1) * "*", "\t", "Player 2: %2d" % (card2["Power"]), len(player2) * "*", "\n")
        else:
            stack.append(card1)
            stack.append(card2)
            player2.extend(stack)
            print("Player 2 won!", "\t", "Player 1: %2d" % (card1["Power"]), len(player2) * "*", "\t", "Player 2: %2d" % (card2["Power"]), len(player1) * "*", "\n")

if len(player1) > 0:
    print("Player1 WON!")
elif len(player2) > 0:
    print("Player2 WON!")