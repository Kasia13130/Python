for candidate in range(2, 31):
    for divider in range(2, candidate):
        if candidate % divider == 0:
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))

# wyswietla sie tylko wartosci, ktore maja wiecej niz dwa naturalne dzielniki

print("\n")

for candidate in range(2, 31):
    for divider in range(2, candidate):
        if candidate % divider == 0:
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break

# break spowoduje przerwanie warunku if, czyli zakonczy poszukiwania kolejnych dzielnikow dla dalej wartosci, zostanie
# zerwana petla wewnetrzna

print("\n")

# wyswietlenie liczb piwerwszych oraz innych o wiekszej liczbie dzielnikow

for candidate in range(2, 31):
    isPrime = True
    for divider in range(2, candidate):

        if candidate % divider == 0:
            isPrime = False
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break
    if isPrime:
        print("%2d is prime!" % (candidate))

# instrukacja break powoduje, ze jesli liczba nie jest pierwsza to wewnetrzna petla sie skonczy a dzialanie programu
# przejdzie do piwerwszej petli by zbadac kolejna wartosc

print("\n")

for candidate in range(2, 31):

    for divider in range(2, candidate):

        if candidate % divider == 0:
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break
    else:
        print("%2d is prime!" % (candidate))

# else dla wewnetrznego for, else nie bedzie wykonywane jesli wewnetrzna petla for zostala przerwana przez instrukcje
# break, natomiast gdy instrukcja for nie zostala zerwana to instrukcja else zostanie wykonana, dla liczb NIE
# piwerwszych wykouje sie instrukcja break, natomiast dla liczb pierwszych uruchamia sie instrukcja else

print("\n")

# cwiczenie
text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or ' \
       'machine system. The device preserves the input power and simply trades off forces against movement to obtain ' \
       'a desired amplification in the output force. The model for this is the law of the lever. Machine ' \
       'components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism ' \
       'transmits power without adding to or subtracting from it. This means the ideal mechanism does not include ' \
       'a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. ' \
       'The performance of a real system relative to this ideal.'

words = text.split(" ")
print(words)
short_text = ""
counter = 0
for word in words:
    short_text += word + " "
    counter += 1

    if counter >= 20:
        print(short_text)
        break


print("\n")

# cwiczenie 2
definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
    ]

for definition in definitions:      # iteracja po calej liscie definicji
    #print(definition)
    short_text = ""                 # przypisanie tekstu do zmiennej skorconej
    counter = 0
    words = definition.split(" ")

    for word in words:              # iteracja po slowach w tekscie
        short_text += word + " "    # przypisanie do zmiennej pobranego slowa w cudzyslowiu
        counter += 1                # licznik slow

        if counter >= 20:
            print(short_text)
            break

print("\n")