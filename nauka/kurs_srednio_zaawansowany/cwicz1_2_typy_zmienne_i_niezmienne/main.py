# kazda zmienna jest identyfikowana przez pewien identyfikator, pewna liczbe, krora mowi gdzie znajduje sie wartosc
# tej zmiennej
# zmienne mozna zmieniac, ale sa takie ktore mozna zmieniac oraz takie ktorych nie mozna zmieniac
number = 10
print("Variable number:", number, id(number))
number += 2
print("Variable number:", number, id(number))
# zmienna typu int jest niezmienna !!!! (immutable)


print("\n")
text = "Africa"
print("Variable text:", text, id(text))
text += " is hot"
print("Variable text:", text, id(text))
# zmienna string jest niezmienna !!! (immutable)


print("\n")
list = [1, 2, 3]
print("Variable list", list, id(list))
list.append(4)
print("Variable list", list, id(list))
# zmienna (mutable)


print("\n")
list2 = list
print("Variable list2:", list2, id(list2))
list2.append(5)
print("Variable list", list, id(list))
print("Variable list2:", list2, id(list2))


print("\n")
list3 = list.copy()
print("Variable list", list, id(list))
print("Variable list3:", list3, id(list3))
list3.append(6)
print("Variable list", list, id(list))
print("Variable list3", list3, id(list3))

