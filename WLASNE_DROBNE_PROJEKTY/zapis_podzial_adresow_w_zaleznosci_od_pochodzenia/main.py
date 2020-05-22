import os

# D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_5_zapis_do_pliku_tekstowego\\adresses.txt

x = True
while x:
    filename = input("Enter dir: ")
    if not os.path.isfile(filename):
        print("The dir is not correct")
    elif os.path.isfile(filename):
        x = False
        webaddresses = []
        file = open(filename, "r")

        for adress in file:
            webaddresses.append(adress.rstrip("\n"))

        file.close()

        webs_pl = "D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_5_zapis_do_pliku_tekstowego\\webs_pl.txt"
        p = open(webs_pl, "w")

        webs_other = "D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_5_zapis_do_pliku_tekstowego\\webs_other.txt"
        o = open(webs_other, "w")

        for line in webaddresses:
            if line.endswith(".pl"):
                p.write(line + "\n")
            else:
                o.write(line + "\n")

        p.close()
        o.close()
        break