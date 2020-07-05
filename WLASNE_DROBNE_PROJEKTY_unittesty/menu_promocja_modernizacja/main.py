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

# modernizacja - ciag dalszy

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("You get Burger!")
elif isWeekend:
    print("Promotion on burger is week day only")
else:
    print("You must ordered Pizza or BigDrink to get burger")