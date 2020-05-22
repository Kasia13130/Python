myvar = "Hello PyCharm!"
myvar2 = myvar
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print("Is value the same?", myvar == myvar2)    # sprawdzenie czy obie wartosci sa sobie rowne
print("Are the variable the same?", myvar is myvar2)    # sprawdzenie czy obie zmienne sa takie same
print(id(myvar), id(myvar2))    # wyswietlenie miejsca w pamieci komputera, czyli adresy komorek w pamieci komputera

print("\n")
myvar = "Hello PyCharm!"
myvar2 = myvar + "!!"       # kazda zmiana wartosci powoduje zapis w innej komorce pamieci komputera
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print("Is value the same?", myvar == myvar2)
print("Are the variable the same?", myvar is myvar2)
print(id(myvar), id(myvar2))

print("\n")
#myvar = "Hello PyCharm!"
myvar2 = myvar2[:-2]    # nawet gdy wartosci zmiennych ponownie beda takie same, to zmienne nie sa juz takie same
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print("Is value the same?", myvar == myvar2)    # ta sama wartosc
print("Are the variable the same?", myvar is myvar2)    # rozne zmienne
print(id(myvar), id(myvar2))    # inne komorki w pamieci komputera
