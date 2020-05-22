import random

myNumbers = []

while len(myNumbers) < 7:               # losujemy liczby az do konca listy myNumbers czyli 7
    newNumber = random.randint(1, 49)   # funkcja randint losuje liczby lacznie z tymi ktore ma w zakresie

    if newNumber in myNumbers:          # jesli liczba, ktora zostala wylosowana powtorzy sie to losowanie
        print("Eliminated: ", newNumber)    # ma przebiegac dalej
        continue

    myNumbers.append(newNumber)         # wylosowana liczba zostaje przypisana do listy myNumbers

print("Those numbers will win:", myNumbers)

print("\n")

# cwiczenie - karty

print("\n")

colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
figures = ["Ace", "King", "Queen", "Jack", "10", "9"]
allCards = []

for x in colors:

    for y in figures:
        allCards.append(x + y)

random.shuffle(allCards)

print(allCards)

print("\n")


# inny zapis
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))

print(allCards)

import random

random.shuffle(allCards)
print(allCards)

print("\n")


# rozdanie graczom - I sposob
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

print("\n")


# inny zapis
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))

print(allCards)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

max = len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

print("\n")


# rozdanie kart - II sposob
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

print("\n")


# inny zapis
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))

print(allCards)

import random

random.shuffle(allCards)

player1 = allCards[:12]
player2 = allCards[12:]

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

