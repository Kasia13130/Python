def main():

    print("\n" + "Odczytanie i wyswietlenie calosci: ")
    tekst = open("wiersz.txt", "r+")    # odczytanie i wyswietlenie calosci pliku
    print(tekst.read() + "\n")
    tekst.close()  


if __name__ == "__main__":
    main()
