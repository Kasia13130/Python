def main():

    choinka = {'lampki': 'czerwone', 'bombki': 'zlote'}
    koszyk = {'swieconka': 'jajko', 'sos': 'chrzan', 'przyprawa': 'sol'}
    cmentarz = {'znicz': 'okragly', 'kwiaty': 'wiazanka'}

    print(choinka, koszyk, cmentarz)
    lista = [choinka, koszyk, cmentarz]
    print(lista)
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(choinka["lampki"])
    print(koszyk["sos"])


if __name__ == "__main__":
    main()