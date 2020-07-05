def main():

    lista = dict(zip(["zielony", "bombka", "lampki"], ["choinka", "okragla", "biale"]))

    print(lista)
    print(lista["bombka"])


if __name__ == "__main__":
    main()

# zip()Funkcja Pythona tworzy iterator, ktory agreguje elementy z dwoch lub wiecej iteratorow.
# Mozna uzyc wynikowego iteratora do szybkiego i spojnego rozwiazywania typowych problemow programistycznych,
# takich jak tworzenie slownikow.