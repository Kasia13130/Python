def wartosc():

    print("\n")

    for i in range(15):
        yield i * 3


for liczba in wartosc():
    print(liczba)
print("\n")

# kazda wartosc od 0 do 15 jest mnozona przez 3, a wynik wyswietlany przy drugiej petli


if __name__ == "__main__":
    wartosc()


def wznowienia():

    print("Wstrzymuje dzialanie")
    yield 5
    print("Wznowienie dzialania" + "\n")

    print("Wstrzymuje dzialanie")
    yield 6
    print("Wznowienie dzialania" + "\n")

    print("Wstrzymuje dzialanie")
    yield 7
    print("Wznowienie dzialania" + "\n")


for i in wznowienia():
    print("Zwroc wartosc: " + str(i))

# zwraca wartosc, ktora wystapi przy konkretnym wstrzymaniu generatora


if __name__ == "__main__":
    wznowienia()


def ret():
    for x in range(10):
        if x == 5:
            return
        else:
            yield x


for x in ret():
    print(x)
print("\n")


if __name__ == "__main__":
    ret()
# wykonanie petli for od 0 do 10 w ktorej wykonuje sie warunek if gdzie wartosc x gdy jest rowna 5 zwraca wartosc,
# natomiast gdy sa wartosci ponizej 5 slowo kluczowe yield generatora wykonuje nadal funkcje przechodząc do petli for
# by nastepnie przejsc do kolenej wartosci na poczatku instrukcji


def parzyste():

    i = 0
    while True:
        yield i
        i = i + 2


gen = parzyste()
type(gen)
print(str(gen))

print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

print("\n")

if __name__ == "__main__":
    parzyste()

# przypisanie wartosci poczatkowej do zmiennej i, przejscie do petli True (program sie wykonnuje dopoki kryteria sa
# spelniane), przejscie do instrukcji yield, przypisanie obiegtu do generatora, przejscie do pierwszej pozycji w
# generetorze, czyli przypisanie do rownania i = i+2 wartosci wyznaczonej z pozycji __next__ a nastepnie przejscie do
# yield by przypisac kolejna wartosc itd


def elementy():

    elements = [x * 2 for x in range(6)]
    print(elements)
    print("\n")


if __name__ == "__main__":
    elementy()
# zwraca wartosci od 0 do 6 pomnozone przez 2, a nastepnie wyswietla je w liscie


def elementy2():

    elements = (x * 2 for x in range(6))
    print(elements)

    print(next(elements))
    print(next(elements))
    print(next(elements))
    print(next(elements))
    print("\n")


if __name__ == "__main__":
    elementy2()
# zwraca objekt generatora, a nastepnie pozycje kazdego elementu z rownania z zakresu 6 liczb


def f(x):

    print(str(type(x)))


f(x for x in range(6))

'''
if __name__ == "__main__":
    f(x)
'''
# instrukcja zwraca klase: generator.

