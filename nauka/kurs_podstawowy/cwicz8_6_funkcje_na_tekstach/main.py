line = "this IS a very STRANGE text"
print(line.capitalize())    # tekst rozpocznie sie od duzej litery
print(line.title())         # kazde slowo zacznie sie od wielkiej litery
print(line.upper())         # wszystkie litery duze
print(line.lower())         # wszystkie litery male
print(line.swapcase())      # kazda duza literke zamienia na mala, a kazda mala na duza
print(line.casefold())
line = "der Fluß"
print(line.lower())
print(line.casefold())      # rozpoznaje znak ß i zamienia na ss
line = "ŻÓŁĆ"
print(line.lower())
print(line.casefold())      # nie zmienia polskich znaków na zwykle
print(line.replace("Ż", "Z").replace("Ó", "O").replace("Ł", "L").replace("Ć", "C").lower())
# tylko replace mozna zamienic polskie znaki na zwykle

print("\n")
line = "this IS a very STRENGE text"
print(line.count("e"))
print(line.find("e"))       # pozycja na ktorej jest "e" od lewej
print(line.rfind("e"))      # pozycja na ktorej jest "e" od prawej
print(line.index("e"))
print(line.rindex("e"))
print(line.find("p"))       # jesli literki nie ma to zostanie zwrocone -1
#print(line.index("p"))     # szukanie indeksu literki "p" zwroci blad poniewaz tekst jej nie zawiera
print("e" in line)          # zwraca wartosc logiczna czy dana literka znajduje sie w tekscie
print("p" in line)

print("\n")
line = "this IS a very STRENGE text"
print(line.startswith("this"))      # sprawdzenie czy tekst zaczyna sie od slowa "this
print(line.startswith("THIS"))
print(line.endswith("text"))        # sprawdzenie czy tekst konczy sie na wyraz "text"
line = """this is a long text
that spans multiple lines
but ahould be somehow presented in python"""
print(line)
print(line.count("\n"))             # znalezienie "\n" w tekscie

print("\n")
import string                       # importowanie funckji napisu
print(string.ascii_letters)         # wyswietlenie liter z tablicy ASCII
print(string.digits)                # wyswietlenie liczb z tablicy ASCII

print("\n")
line = "this is the end of this lesson"
print(line.split(" "))              # podzielenie testu ze wzgledu na spacje
list = line.split(" ")              # przypisanie do listy tekstu podzielonego ze wzgledu na spacje
print(list)
print(" ".join(list))               # przylaczenie do cudzyslowiu listy by powstal tekst

print("\n")
# cwiczenie 1
poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

poem = poem.split("\n")
print(poem)
i = 0

for i in range(len(poem) - 8):
    poem[i] += "\n" + poem[i + 8]
    print(poem[i])

print("\n")

# inny zapis
poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''
lines = poem.split('\n')

for i in range(8):
    print(lines[i])
    print(lines[i + 8])