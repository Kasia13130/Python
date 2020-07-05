
class DekodowanieDnia:
    def dzien(pesel):

        if ((int(pesel[4]) * 10) + int(pesel[5])) <= 28:  # mnożymy pierwszą pozycję przez 10 by nadać jej pozycję pierwszą w całej liczbie
            return (str(pesel[4] + pesel[5]))
        elif ((int(pesel[4]) * 10) + int(pesel[5])) <= 29:
            return (str(pesel[4] + pesel[5]))
        elif ((int(pesel[4]) * 10) + int(pesel[5])) <= 30:
            return (str(pesel[4] + pesel[5]))
        elif ((int(pesel[4]) * 10) + int(pesel[5])) <= 31:
            return (str(pesel[4] + pesel[5]))
        else:
            print("Błąd, zły dzień")
            return
