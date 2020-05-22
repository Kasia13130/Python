def macierz():

    rows, cols = (2, 4)
    tabela = [2, 3, 4, 5], \
             [2, 3, 4, 5]
    print(tabela)
    return


def macierz2():

    import xlrd
    loc2 = ("D:\Dokumenty\Kasia\studia\phyton nauka\moje projekty\kalkulator_naukowy\macierz2.xlsx")
    import numpy
    x = xlrd.open_workbook(loc2)
    sheet = x.sheet_by_index(0)  # indeks 0 oznacza pierwszy arkusz excela
    tab = numpy.zeros((sheet.nrows, sheet.ncols))  # pierwsza to wiersze, a druga to kolumny
    print(tab)  # wyswietli tu tablice z samymi zerami

    for i in range(0, sheet.nrows):  # sprawdzenie ile wierszy ma tablica
        for j in range(0, sheet.ncols):  # sprawdzenie ile kolumn ma tablica w excel
            tab[i, j] = sheet.cell_value(i, j)
    print(tab)  # wyswietli tablice z wartosciami skopiowanymi z excela
    # print(sheet.cell_value(i, j))   # wyswietlenie wymiarow tablicy
    return


def macierz3():

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
    return
