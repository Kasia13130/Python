def main2():

    print("\n" + "Odczytanie i wyswietlenie calosci: ")
    with open("wiersz.txt", "r+") as t:   # odczytanie i wyswietlenie calosci pliku
        print(t.read() + "\n")
    return

    #tekst.close()


if __name__ == "__main__":
    main2()
