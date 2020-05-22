def main():

    print("\n" + "Odczytanie i wyswietlenie calosci: ")
    tekst = open("wiersz.txt", "r")
    print(tekst.read() + "\n")
    tekst.close()           # odczytanie i wyswietlenie calosci pliku

    print("Wyswietlenie llinijka po linijce:")
    tekst2 = open("wiersz.txt")     # wyswietlenie linijka po linijce, pamietac by r+ nie bylo
    for linia in tekst2:
        print(linia + "\n")
    tekst2.close()

    print("Wyswietlenie konkretnego znaku:")
    import linecache
    wiersz = open("wiersz.txt", "r")
    wiersz = linecache.getline("wiersz.txt", 1)
    print(wiersz[3] + '\n\n')       # wyswietlenie konkretnego znaku z pierwszego wiersza

    print("Wyswietlanie wyraz po wyrazie:")
    wiersz = linecache.getline("wiersz.txt", 2)
    tab = wiersz.split()
    print(tab)
    for x in tab:
        print(x + '\n')

    print("Wyswietlanie znak po znaku:")
    wiersz = linecache.getline("wiersz.txt", 2)
    tab = wiersz.split()
    print(tab[0])
    for y in tab[0]:
        print(y + '\n')

    print("Wyswietlanie znak po znaku:")
    slowo = linecache.getline("wiersz.txt", 2)
    tab = slowo.split()
    print(tab[1])
    for g in tab[1]:
        print(g + '\n')

    print("Pisanie do pliku txt:")
    wiersz3 = open("wiersz3.txt", "w").write("Jest sloneczna pogoda")

    print("Liczenie znakow w tekscie:")
    wiersz = len(open("wiersz.txt", "r").readlines())
    print(wiersz)

    print("Liczenie wyrazow w linii")
    wiersz = linecache.getline("wiersz.txt", 1)
    tab = wiersz.split()
    print(len(tab))

    print("Liczenie znakow linia po linii:")
    wiersz = open("wiersz.txt", "r")
    for znak in wiersz:
        print(len(znak))

    print("Liczenie wyrazow:")
    wiersz = open("wiersz.txt", "r")
    tab = wiersz.read().split()
    print(len(tab))
    wiersz.close()

    print("Liczenie znakow w calym tekscie:")
    wiersz = open("wiersz.txt", "r")
    data = wiersz.read()
    print(len(data))
    wiersz.close()
    '''
    print("Dopisanie linijki na koncu:")
    wiersz = open("wiersz.txt", "a")        # dopisanie linijki na koncu tekstu
    wiersz.write("\n" + "kot" + "\n")
    tekst2.close()


    print("Podzial na linie po przecinku:")
    wiersz = open("wiersz.txt", "r")
    for line in wiersz.readlines():
        line = line.strip()
        parts = line.split(",")
        for part in parts:
            print("",part + "\n")
    wiersz.close()

    print("Podzial na linie i zapis do pliku:")
    wiersz = open("wiersz.txt", "r+")
    wiersz.write(wiersz.read().replace(",", "\n"))
    wiersz.close()

    print("Podzial na wyrazy:")
    wiersz = open("wiersz.txt", "r+")
    wiersz.write(wiersz.read().replace(" ", "   "))
    wiersz.close()


    print("Tablicowanie rzeczy przeczytanych z pliku")
    wiersz = open("wiersz.txt", "r")
    tab = wiersz.read().split()
    print(tab)
    wiersz.close()
    '''

    print("slownikowanie rzeczy przeczytanych z pliku")
    moj_dict = {}
    with open("pogoda.txt", "w") as f:
        moj_dict['d'] = 'sosna'
        moj_dict['k'] = 'roza', 'stokrotka'
        moj_dict['z'] = 'zajac', 'dzik'
        f.write(str(moj_dict))
    print(moj_dict)


    print("Sortowanie stablicowanych rzeczy")       # sortowanie ogolne wyrazow
    wiersz = open("wiersz.txt", "r")
    wyrazy = wiersz.read().split()
    wyrazy.sort()
    for wyraz in wyrazy:
        print(wyraz)
    wiersz.close()

    print("Sortowanie stablicowanych rzeczy")       # sortowanie alfabetyczne z uwzhlednieniem duzych liter
    wiersz = open("wiersz.txt", "r")
    wyrazy = wiersz.read().split()
    wyrazy.sort(key=str.lower)
    for wyraz in wyrazy:
        print(wyraz)
    wiersz.close()

    import linecache
    print("\n" + "Sortowanie stablicowanych rzeczy z danej linii")      # sortowanie ogolne danej linii
    linia4 = linecache.getline("wiersz.txt", 2).split()
    linia4.sort()
    for wyraz in linia4:
        print(wyraz)


    import linecache
    print("\n" + "Sortowanie stablicowanych rzeczy z danej linii")      # sortowanie alfabetyczne z uwaglednieniem
    linia4 = linecache.getline("wiersz.txt", 2).split()                 # duzych liter
    linia4.sort(key=str.lower)
    for wyraz in linia4:
        print(wyraz)

if __name__ == "__main__":
    main()