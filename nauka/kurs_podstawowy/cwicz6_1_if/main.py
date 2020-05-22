age = 22

if age >= 18:
    print("You are adult and you can buy alcohol")
else:
    print("You are too young to buy alcohol")

isDrunk = False
if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we canot sell you alcohol")

isRestrictedArea = False
if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we canot sell you alcohol")

print("\n")

# cwiczenie
min_likes = 500
min_share = 100

like = 630
share = 298

if like >= 500 and share >= 100:
    print("The price is 10 % low")
else:
    print("The price is the same")

print("\n")

# inne rozwiazanie cwiczenia
min_likes1 = 500
min_share1 = 100

like = 630
share = 298

if like >= min_likes1 and share >= min_share1:
    print("The price is 10 % low")
else:
    print("The price is the same")

print("\n")

# cwiczenie 2
isPizzaOrdered = True       # True jesli pizza zostala kupiona
isBigDrinkOrdered = True    # True jesli duzy napoj zostal zamowiony
isWeekend = False            # True jesli jest weekend

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("You get coupon on Burger !")
else:
    print("Plese, buy Pizza or BigDrink on week day")

print("\n")

# cwiczenie 3
diskSize = 100
diskSizeUsed = 90
fileSize = 15

if fileSize <= (diskSize - diskSizeUsed):
    print("File can be downoladed")
else:
    print("No space on disk")