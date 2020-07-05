def main():

    liczby = [2, 4, 6, 8, 10, 12]
    for x in liczby:
        print(x)
    print("\n")

    cyferki = [1, 3, 5, 7, 9, 11]
    for y in range(6):
        print(y)
    print("\n")

    cyferki2 = [1, 2, 3, 4, 5, 6]
    for z in range(2, 4):
        print(z)
    print("\n")

    wartosc = 0
    while wartosc < 10:
        print(wartosc),
        wartosc += 2
    print("\n")

    liczba = 1
    while liczba < 100:
        print(liczba),
        liczba *= 3
    print("\n")

    cos = 2
    while cos < 50:
        print(cos),
        cos **= 2

if __name__ == "__main__":
    main()