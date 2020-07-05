def main():

    from math import sqrt, exp, expm1, log, log1p, log10, pow, acos, asin
    from math import atan2, cos, sin, tan, erf
    import xlrd
    loc = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz.xlsx")
    loc2 = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz2.xlsx")
    import numpy

    while True:

        print("\n")
        print("Mozliwe dzialania i funkcje matematyczne: dodawanie (+), roznica (-), mnozenie (*), dzielenie (/), pierwiastek (sqrt)")
        print("potegowanie (exp), potegowanie x do -1 (expm1), logarytmowanie (log), logarytm naturalny (ln), logarytm dziesietny (log10)")
        print("moc, arc cos, arc sin, atan2, cos, sin, tan, funkcja bledu")
        print("macierz", "macierz2", "macierz3")

        napis = input()
        if "koniec" == napis:
            break

        x = int(input())
        y = int(input())

        # podstawowe dzialania
        # dodawanie

        if "+" == napis:
            print("dodawanie: " + str(x + y))

        # roznica
        elif "-" == napis:
            print("roznica: " + str(x - y))

        # mnozenie
        elif "*" == napis:
            print("mnozenie: " + str(x * y))

        # dzielenie
        elif "/" == napis:
            try:
                print("dzielenie: " + str(x / y))
            except:
                print("Nie dziel przez zero cholero")

        # pierwiastkowanie
        elif "sqrt" == napis:
            try:
                print("pierwiastek z x: " + str(sqrt(x)))
            except:
                print("pierwiastki stopni parzystych z liczb ujemnych nie istniea")
            try:
                print("pierwiastek z y: " + str(sqrt(y)))
            except:
                print("pierwiastki stopni parzystych z liczb ujemnych nie istnieja")

        # potegowanie
        elif "exp" == napis:
            print("potegowanie x: " + str(exp(x)))
            print("potegowanie y: " + str(exp(y)))

        # potegowanie do -1
        elif "expm1" == napis:
            print("potegownaie x do -1: " + str(expm1(x)))
            print("potegowanie y do -1: " + str(expm1(y)))

        # logarytmowanie
        elif "log" == napis:
            try:
                print("logarytmowanie x: " + str(log(x)))
            except:
                print("logarytmowanie musi byc >0 i rozne od 1")
            try:
                print("logarytmowanie y: " + str(log(y)))
            except:
                print("logarytmowanie musi byc >0 i rozne od 1")

        # logarytm naturalny z jeden plus tablica wejsciowa
        elif "ln" == napis:
            try:
                print("logarytm naturalny: " + str(log1p(x)))
            except:
                print("logarym naturalny musi miec x>0")
            try:
                print("logarytm naturalny: " + str(log1p(y)))
            except:
                print("logarym naturalny musi miec y>0")

        # logarytmowanie dziesietne
        elif "log10" == napis:
            try:
                print("logarytm dziesietny: " + str(log10(x)))
            except:
                print("logarytm dziesietny: " + str(log10(y)))

        # obliczenie mocy
        elif "moc" == napis:
            print("Moc: " + str(pow(x, y)))

        # zrwaca arc cos w radianach, przedzial -1 do 1
        elif "arc cos" == napis:
            try:
                print("arc cos w radianach: " + str(acos(x)))
            except:
                print("Tylko w przedziale -1 do 1")

            try:
                print("arc cos w radianach: " + str(acos(y)))
            except:
                print("Tylko w przedziale -1 do 1")

        # zwraca arc sin w radianach, przedzial -1 do 1
        elif "arc sin" == napis:
            try:
                print("arc sin w radianach: " + str(asin(x)))
            except:
                print("Tylko w przedziale -1 do 1")

            try:
                print("arc sin w radianach: " + str(asin(y)))
            except:
                print("Tylko w przedziale -1 do 1")

        # zwraca wynik w radianach; Metoda atan2 zwraca wartosc liczbowa
        # pomiedzy -pi a pi, reprezentujaca kat theta punktu (x, y).
        # Kat ten, mierzony w radianach, zostal utworzony przez
        # dodatnia os OX i punkt (x,y) , z obrotem w kierunku przeciwnym
        # do ruchu wskazowek zegara.
        elif "atan2" == napis:
            print("atan2 w radianach: " + str(atan2(x, y)))

        # zwraca cos x, y radianow
        elif "cos" == napis:
            print("cos x w radianach: " + str(cos(x)))
            print("cos y w radianach: " + str(cos(y)))

        # zwraca sin x radianow
        elif "sin" == napis:
            print("sin x w radianach: " + str(sin(x)))
            print("sin x w radianach: " + str(sin(y)))

        # zrwaca tan x radianow
        elif "tan" == napis:
            print("tan x w radianach: " + str(tan(x)))
            print("tan x w radianach: " + str(tan(y)))

        # zwraca funkcje bledu na x, y
        elif "funkcja bledu" == napis:
            print("funkcja bledu na x: " + str(erf(x)))
            print("funkcja bledu na y: " + str(erf(y)))

        # macierz
        elif "macierz" == napis:
            rows, cols = (2, 4)
            tabela = [2, 3, 4, 5], \
                     [2, 3, 4, 5]
            print(tabela)

        # macierz2
        elif "macierz2" == napis:
            x = xlrd.open_workbook(loc2)
            sheet = x.sheet_by_index(0)  # indeks 0 oznacza pierwszy arkusz excela
            tab = numpy.zeros((sheet.nrows, sheet.ncols))  # pierwsza to wiersze, a druga to kolumny
            print(tab)   # wyswietli tu tablice z samymi zerami



            for i in range(0, sheet.nrows):  # sprawdzenie ile wierszy ma tablica
                for j in range(0, sheet.ncols):  # sprawdzenie ile kolumn ma tablica w excel
                    tab[i, j] = sheet.cell_value(i, j)
            print(tab)    # wyswietli tablice z wartosciami skopiowanymi z excela
                    # print(sheet.cell_value(i, j))   # wyswietlenie wymiarow tablicy

        # macierz3
        elif "macierz3" == napis:
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            print(sheet.cell_value(0, 0))
            print(sheet.nrows)
            print(sheet.ncols)

            for i in range(0, sheet.nrows):
                for j in range(0, sheet.ncols):
                    print(sheet.cell_value(i, j))

if __name__ == "__main__":
    main()