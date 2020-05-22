import os

webaddresses = []
line = input("Enter www adress: ")
i = 0

while i < len(line):
    webaddresses.append(line)
    line = input("Enter www adress: ")

dirname = "D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_5_zapis_do_pliku_tekstowego"
filename = input("Enter file name: ")
filepath = os.path.join(dirname, filename)

file = open(filepath, "w")
for adress in webaddresses:
    file.write(adress + "\n")

file.close()