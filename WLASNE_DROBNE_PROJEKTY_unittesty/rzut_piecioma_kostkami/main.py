import random
min = 1
max = 6

dice = random.randint(min, max)

dices = []
for i in range(5):
    dice = random.choice(range(min, max))

    dices.append(dice)
    dices.sort()
print(dices)