for i in range(10):     # wyswietlenie liczb od 0 do 9
    print(i)
print("\n")

for i in range(1, 11):      # wyswietlenie liczb od 1 do 10
    print(i)
print("\n")

for i in range(1, 11, 2):   # trzeci parametr jest o tym jak obliczac kolejna wartosc
    print(i)
print("\n")

for i in range(10, 0, -1):      # iteracja malejaca, kolejna wartosc bedzie o jeden mniejsza od poprzedniej (parametr -1)
    print(i)
print("\n")

for i in range(1, 11):
    print(i)
print("\n")

#list = range(10)
#print("List:", list, type(list), id(list))     # lista nie bedzie lista ale range

list = list(range(10))      # skonwertowanie renge do listy
print("List:", list, type(list), id(list))  # wyswietlenie elementow o liscie
# wyciaganie elemetow (slice)
print(list[5:7])    # wyswietlenie elementow od 5 do 6
print(list[5:])     # wyswietlenie wszystkich elementow od 5 do konca
print(list[:-1])    # wyswietlenie wszystkich elementow do przedostatniego
print(list[:])      # wszystkie elementy
print(list[5:-1])   # wyswietlenie elementow od 5 do przedostatniego
print(list[5:-3])   # wyswietlenie elementow od 5 do czwartego od konca
print(list[:8:2])   # wyswietlenie elementow do osmego ale tylko co drugi z nich
print(list[-1:0:-1])    # odwrocenie listy o -1 (-1 to teraz ostatni element z listy czyli 9)
print(list[-1::-1])     # wyswietlenie elementow od konca do samego poczatku i cofanie sie o -1
print("\n")

#list2 = list.copy()    # by zmienic zmienna nalezy dopisac .copy by byl to nowy obiekt
list2 = list[:]     # teraz mozna odwolac sie do nowej listy2
print("List2:", list2, type(list2), id(list2))  # wyswietlenie informacji listy2