def main():

    lista = ['czerwony', 'zolty', 'pomaranczowy', 'zielony', 'niebieski', 'szary']
    print(lista)
    # opetator slice
    print(lista[4])
    print(lista[0:])
    print(lista[:0])
    print(lista[:])
    print(lista[0])
    print(lista[1:])
    print(lista[2:])
    print(lista[3:])
    print(lista[:-2])
    print("operator slice z krokiem")
    print(lista[::2])
    print(lista[1::2])
    print(lista[::-1])  # Odwrocenie kolejnosci argumentow
    print(lista[5:3:-1])
    print(lista[-2:-5:-1])


if __name__ == "__main__":
    main()