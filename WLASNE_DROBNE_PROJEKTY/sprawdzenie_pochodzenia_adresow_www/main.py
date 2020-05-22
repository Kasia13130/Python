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

        for line in webaddresses:
            if line.endswith(".pl"):
                print("The adress: %s is from Poland" % line)
            else:
                print("The adress: %s is not from Poland" % line)
        break