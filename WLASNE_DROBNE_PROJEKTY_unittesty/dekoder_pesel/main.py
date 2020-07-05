
import main2


class NumerPesel:

    def getInput(text):
        return input(text)

    def pesel():

        var = 1
        while var:

            pesel = NumerPesel.getInput("Please enter your pesel: ")

            if pesel == '94042503033':
                var = 0
                return False

            if "koniec" == pesel:
                break

            if len(pesel) == 11:

                if pesel[2] == '8':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "18" + pesel[0] + pesel[1] + "r.")
                elif pesel[2] == '9':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "18" + pesel[0] + pesel[1] + "r.")
                elif pesel[2] == '0':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "19" + pesel[0] + pesel[1] + "r.")
                elif pesel[2] == '1':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "19" + pesel[0] + pesel[1] + "r.")
                elif pesel[2] == '2':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "20" + pesel[0] + pesel[1] + "r.")
                elif pesel[3] == '3':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "20" + pesel[0] + pesel[1] + "r.")
                elif pesel[3] == '4':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "21" + pesel[0] + pesel[1] + "r.")
                elif pesel[3] == '5':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "21" + pesel[0] + pesel[1] + "r.")
                elif pesel[3] == '6':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "22" + pesel[0] + pesel[1] + "r.")
                elif pesel[3] == '7':
                    print((main2.DekodowanieDnia.dzien(pesel)) + "-" + pesel[3] + "-" + "22" + pesel[0] + pesel[1] + "r.")

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

            var = 0

        return True


if __name__ == "__main__":
    NumerPesel.pesel()

