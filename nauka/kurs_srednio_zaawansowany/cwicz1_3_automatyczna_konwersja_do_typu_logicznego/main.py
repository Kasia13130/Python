# automatyczna konwersja typu na typ logiczny, jesli w wartosci przy zmiennej jest cokolwiek wpisane to zostanie
# zwrocona wartosc logiczna True
# jesli wartosc przy zmiennej jest pusta czyli "" lub 0 to wartosc True sie nie wyswietli, czyli oznacze to blad badz
# wartosc False
isOk = True
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = "True"
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = "OK"
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = "PyCharm"
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = 1
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = 0
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = ""
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = [1, 2, 3]
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = [0, 0, 0]
print("Variable isOk: ", isOk, type(isOk))
if isOk:
    print("TRUE")

isOk = [0, 0, 0]
print("Variable isOk: ", isOk, type(isOk))
if isOk[0]:
    print("TRUE")

listOfErrors = [0, 0, 0]
print("Variable isOk: ", listOfErrors, type(listOfErrors))
if listOfErrors:
    print("TRUE")

listOfErrors = [100, 101, 102]
print("Variable isOk: ", listOfErrors, type(listOfErrors))
if listOfErrors:
    print("TRUE")

listOfErrors = [100, 101, 102]
print("Variable isOk: ", listOfErrors, type(listOfErrors))
if listOfErrors:
    print("TRUE")

listOfErrors = [100, 101, 102]
print("Variable isOk: ", listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0:
    print("TRUE")