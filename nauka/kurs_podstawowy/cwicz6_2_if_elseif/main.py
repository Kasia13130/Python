# I sposob wykorzystanie instrukcji if (mniej odpowiednia)
age = 18
isDrunk = False
isRestrictedArea = True

if age < 18:
    print("You are to young to buy alcohol")
else:
    if isDrunk:
        print("Are you drunk? We cannot sell you alcohol")
    else:
        if isRestrictedArea:
            print("Restracted area. Alcohol is forbidden")
        else:
            print("You can buy alcohol")

print("\n")
# II sposob
if age < 18:
    print("You are to young to buy alcohol")
elif isDrunk:
    print("You are drunk, we canot sell you alcohol")
elif isRestrictedArea:
    print("Restracted area, alcohol is forbidden")
else:
    print("You can buy alcohol")

print("\n")

# cwiczenie
min_like = 500
min_share = 100

num_like = 600
num_share = 250

if num_like >= min_like and num_share >= min_share:
    print("The prizes is -10%")
else:
    if num_like < min_like:
        print("Not enough likes, price is the same")
    else:
        print("We need more shares")

print("\n")

# cwiczenie if, elif, else
min_like = 500
min_share = 100

num_like = 400
num_share = 50

if num_like >= min_like and num_share >= min_share:
    print("The prizes is -10%")
elif num_share < min_share:
    print("Not enough shares, price is the same")
else:
    print("We need more likes")

print("\n")

isPizzaOrdered = True       # True jesli pizza zostala kupiona
isBigDrinkOrdered = True    # True jesli duzy napoj zostal zamowiony
isWeekend = True           # True jesli jest weekend

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("You get coupon on Burger !")
else:
    if isWeekend:
        print("Please buy Pizza or BigDrink in week day")
    else:
        print("You don't have pizza or BigDring in ordered to get burger")


# cwiczenie if, elif, else
if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("You get Burger!")
elif isWeekend:
    print("Promotion on burger is week day only")
else:
    print("You must ordered Pizza or BigDrink to get burger")