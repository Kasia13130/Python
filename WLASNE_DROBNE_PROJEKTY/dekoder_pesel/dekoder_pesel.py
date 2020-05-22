def main():

    import dzien

    while True:

        pesel = input()

        if "koniec" == pesel:
            break

        if len(pesel) == 11:

            if pesel[2] == '8':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "18" + pesel[0] + pesel[1] + "r.")
            elif pesel[2] == '9':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "18" + pesel[0] + pesel[1] + "r.")
            elif pesel[2] == '0':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "19" + pesel[0] + pesel[1] + "r.")
            elif pesel[2] == '1':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "19" + pesel[0] + pesel[1] + "r.")
            elif pesel[2] == '2':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "20" + pesel[0] + pesel[1] + "r.")
            elif pesel[3] == '3':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "20" + pesel[0] + pesel[1] + "r.")
            elif pesel[3] == '4':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "21" + pesel[0] + pesel[1] + "r.")
            elif pesel[3] == '5':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "21" + pesel[0] + pesel[1] + "r.")
            elif pesel[3] == '6':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "22" + pesel[0] + pesel[1] + "r.")
            elif pesel[3] == '7':
                print((dzien.dzien(pesel)) + "-" + pesel[3] + "-" + "22" + pesel[0] + pesel[1] + "r.")

            if pesel[9] == '0':
                print("kobieta")
            elif pesel[9] == '2':
                print("kobieta")
            elif pesel[9] == '4':
                print("kobieta")
            elif pesel[9] == '6':
                print("kobieta")
            elif pesel[9] == '8':
                print("kobieta")

            if pesel[9] == '1':
                print("mężczyzna")
            elif pesel[9] == '3':
                print("mężczyzna")
            elif pesel[9] == '5':
                print("mężczyzna")
            elif pesel[9] == '7':
                print("mężczyzna")
            elif pesel[9] == '9':
                print("mężczyzna")

        else:
            print("Błąd, wpisz jeszcze raz")

if __name__ == "__main__":
    main()

