isPizzaOrdered = True       # True jesli pizza zostala kupiona
isBigDrinkOrdered = True    # True jesli duzy napoj zostal zamowiony
isWeekend = False            # True jesli jest weekend

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("You get coupon on Burger !")
else:
    print("Plese, buy Pizza or BigDrink on week day")