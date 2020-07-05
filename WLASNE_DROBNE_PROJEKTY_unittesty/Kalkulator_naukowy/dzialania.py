def dodawanie():

    x = int(input())
    y = int(input())

    # podstawowe dzialania
    # dodawanie

    print("dodawanie: " + str(x + y))
    return


def roznica():

    x = int(input())
    y = int(input())

    print("roznica: " + str(x - y))
    return


def mnozenie():

    x = int(input())
    y = int(input())

    print("mnozenie: " + str(x * y))
    return


def dzielenie():

    x = int(input())
    y = int(input())

    try:
        print("dzielenie: " + str(x / y))
    except:
        print("Nie dziel przez zero cholero")
    return


def sqrt():

    from math import sqrt

    x = int(input())
    y = int(input())

    try:
        print("pierwiastek z x: " + str(sqrt(x)))
    except:
        print("pierwiastki stopni parzystych z liczb ujemnych nie istniea")
    try:
        print("pierwiastek z y: " + str(sqrt(y)))
    except:
        print("pierwiastki stopni parzystych z liczb ujemnych nie istnieja")
    return


def exp():
    from math import exp

    x = int(input())
    y = int(input())

    print("potegowanie x: " + str(exp(x)))
    print("potegowanie y: " + str(exp(y)))
    return


def expm1():

    from math import expm1

    x = int(input())
    y = int(input())

    print("potegownaie x do -1: " + str(expm1(x)))
    print("potegowanie y do -1: " + str(expm1(y)))
    return


def log():

    from math import log

    x = int(input())
    y = int(input())

    try:
        print("logarytmowanie x: " + str(log(x)))
    except:
        print("logarytmowanie musi byc >0 i rozne od 1")
    try:
        print("logarytmowanie y: " + str(log(y)))
    except:
        print("logarytmowanie musi byc >0 i rozne od 1")
    return


def ln():
    from math import log1p

    x = int(input())
    y = int(input())

    try:
        print("logarytm naturalny: " + str(log1p(x)))
    except:
        print("logarym naturalny musi miec x>0")
    try:
        print("logarytm naturalny: " + str(log1p(y)))
    except:
        print("logarym naturalny musi miec y>0")
    return


def log10():

    from math import log10

    x = int(input())
    y = int(input())

    try:
        print("logarytm dziesietny: " + str(log10(x)))
    except:
        print("logarytm dziesietny: " + str(log10(y)))
    return


def moc():

    from math import pow

    x = int(input())
    y = int(input())

    print("Moc: " + str(pow(x, y)))
    return


def acos():

    from math import acos

    x = int(input())
    y = int(input())

    try:
        print("arc cos w radianach: " + str(acos(x)))
    except:
        print("Tylko w przedziale -1 do 1")

    try:
        print("arc cos w radianach: " + str(acos(y)))
    except:
        print("Tylko w przedziale -1 do 1")
    return

def asin():

    from math import asin

    x = int(input())
    y = int(input())

    try:
        print("arc sin w radianach: " + str(asin(x)))
    except:
        print("Tylko w przedziale -1 do 1")

    try:
        print("arc sin w radianach: " + str(asin(y)))
    except:
        print("Tylko w przedziale -1 do 1")
    return


def atan2():

    from math import atan2

    x = int(input())
    y = int(input())

    print("atan2 w radianach: " + str(atan2(x, y)))
    return


def cos():

    from math import cos

    x = int(input())
    y = int(input())

    print("cos x w radianach: " + str(cos(x)))
    print("cos y w radianach: " + str(cos(y)))
    return


def sin():

    from math import sin

    x = int(input())
    y = int(input())

    print("sin x w radianach: " + str(sin(x)))
    print("sin x w radianach: " + str(sin(y)))
    return


def tan():

    from math import tan

    x = int(input())
    y = int(input())

    print("tan x w radianach: " + str(tan(x)))
    print("tan x w radianach: " + str(tan(y)))
    return


def erf():

    from math import erf

    x = int(input())
    y = int(input())

    print("funkcja bledu na x: " + str(erf(x)))
    print("funkcja bledu na y: " + str(erf(y)))
    return


def macierz_dodawanie():

    import xlrd
    loc2 = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz2.xlsx")
    import numpy
    x = xlrd.open_workbook(loc2)
    sheet2 = x.sheet_by_index(0)  # indeks 0 oznacza pierwszy arkusz excela
    tab = numpy.zeros((sheet2.nrows, sheet2.ncols))  # pierwsza to wiersze, a druga to kolumny

    for i in range(0, sheet2.nrows):  # sprawdzenie ile wierszy ma tablica
        for j in range(0, sheet2.ncols):  # sprawdzenie ile kolumn ma tablica w excel
            tab[i, j] = sheet2.cell_value(i, j)

    # print(sheet.cell_value(i, j))   # wyswietlenie wymiarow tablicy
    # druga macierz
    loc = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    tab2 = numpy.zeros((sheet.nrows, sheet.ncols))
    '''
    print(sheet.cell_value(0, 0))
    print(sheet.nrows)
    print(sheet.ncols)
    '''
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            tab2[i, j] = sheet.cell_value(i, j)

    try:
        print(numpy.add(tab, tab2))
        return
    except:
        print("macierze nie sa sobie rowne")


def odejmowanie_macierzy():

    import xlrd
    loc2 = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz2.xlsx")
    import numpy
    x = xlrd.open_workbook(loc2)
    sheet2 = x.sheet_by_index(0)  # indeks 0 oznacza pierwszy arkusz excela
    tab = numpy.zeros((sheet2.nrows, sheet2.ncols))  # pierwsza to wiersze, a druga to kolumny

    for i in range(0, sheet2.nrows):  # sprawdzenie ile wierszy ma tablica
        for j in range(0, sheet2.ncols):  # sprawdzenie ile kolumn ma tablica w excel
            tab[i, j] = sheet2.cell_value(i, j)

    loc = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    tab2 = numpy.zeros((sheet.nrows, sheet.ncols))
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            tab2[i, j] = sheet.cell_value(i, j)

    try:
        print(numpy.subtract(tab, tab2))
        return
    except:
        print("Macierze nie sa sobie rowne")

def mnozenie_macierzy():

    import xlrd
    loc2 = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz2.xlsx")
    import numpy
    x = xlrd.open_workbook(loc2)
    sheet2 = x.sheet_by_index(0)  # indeks 0 oznacza pierwszy arkusz excela
    tab = numpy.zeros((sheet2.nrows, sheet2.ncols))  # pierwsza to wiersze, a druga to kolumny

    for i in range(0, sheet2.nrows):  # sprawdzenie ile wierszy ma tablica
        for j in range(0, sheet2.ncols):  # sprawdzenie ile kolumn ma tablica w excel
            tab[i, j] = sheet2.cell_value(i, j)

    loc = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    tab2 = numpy.zeros((sheet.nrows, sheet.ncols))
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            tab2[i, j] = sheet.cell_value(i, j)

    try:
        print(tab * tab2)
        return
    except:
        print("Macierze nie sa sobie rowne")


def mnozenie_macierzy_1_przez_liczbe():

    z = int(input())
    import xlrd
    loc2 = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz2.xlsx")
    import numpy
    x = xlrd.open_workbook(loc2)
    sheet2 = x.sheet_by_index(0)  # indeks 0 oznacza pierwszy arkusz excela
    tab = numpy.zeros((sheet2.nrows, sheet2.ncols))  # pierwsza to wiersze, a druga to kolumny

    for i in range(0, sheet2.nrows):  # sprawdzenie ile wierszy ma tablica
        for j in range(0, sheet2.ncols):  # sprawdzenie ile kolumn ma tablica w excel
            tab[i, j] = sheet2.cell_value(i, j)

        print(z * tab)
        return


def mnozenie_macierzy_2_przez_liczbe():

    z = int(input())
    import xlrd
    import numpy
    loc = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    tab2 = numpy.zeros((sheet.nrows, sheet.ncols))
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            tab2[i, j] = sheet.cell_value(i, j)

    print(z * tab2)
    return


def transpozycja_macierzy_1():

    import xlrd
    loc2 = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz2.xlsx")
    import numpy
    x = xlrd.open_workbook(loc2)
    sheet2 = x.sheet_by_index(0)  # indeks 0 oznacza pierwszy arkusz excela
    tab = numpy.zeros((sheet2.nrows, sheet2.ncols))  # pierwsza to wiersze, a druga to kolumny

    for i in range(0, sheet2.nrows):  # sprawdzenie ile wierszy ma tablica
        for j in range(0, sheet2.ncols):  # sprawdzenie ile kolumn ma tablica w excel
            tab[i, j] = sheet2.cell_value(i, j)

    print(tab.T)
    return


def transpozycja_macierzy_2():

    import xlrd
    import numpy
    loc = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    tab2 = numpy.zeros((sheet.nrows, sheet.ncols))
    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            tab2[i, j] = sheet.cell_value(i, j)

    print(tab2.T)
    return
'''
import xlrd
    loc = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    print(sheet.cell_value(0, 0))
    print(sheet.nrows)
    print(sheet.ncols)

    for i in range(0, sheet.nrows):
        for j in range(0, sheet.ncols):
            print(sheet.cell_value(i, j))
'''