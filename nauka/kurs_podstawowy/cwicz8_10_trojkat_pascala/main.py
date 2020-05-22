numbers = [1]

print(numbers)

for i in range(5):
    newNumbers = [1]

    position = 0
    while position < len(numbers) - 1:
        newNumbers.append(numbers[position] + numbers[position + 1])
        position += 1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    print(numbers)

print("\n")

# gra w wojne
'''
aCard = {"Figure": "King", "Power": 12}
print(aCard)
print(aCard["Figure"])
print(aCard["Power"])
aCard["Color"] = "Heart"
print(aCard["Color"])
'''

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

print("\n")

# inny zapis

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace', 'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10', 'Power': 10},
    {'Figure': '9', 'Power': 9}]

allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        # print('=EQUAL \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        # print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    else:
        player2.append(card2)
        player2.append(card1)
        # print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')
