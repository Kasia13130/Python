'''
filename = "D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_5_zapis_do_pliku_tekstowego\\output.txt"

line = "Europe"
cities = ["London", "Berlin", "Paris", "Warsaw", "Madrid", "Rome"]

file = open(filename, "w")      # pisanie do pliku (write), kazdorazowe uzycie tej funkcji "w" spowoduje wyczyszczenie poprzedniego zapisu i zastapienie go aktualnym

file.write(line)
file.write("\n")
file.writelines(cities)         # wartosci zostana zapisane w jednej linii bez odstepow

file.close()



file = open(filename, "w")

file.write(line)
file.write("\n")

for city in cities:             # po przez petle for cities zostana rozbite na poszczegolne city podzielone przez separator nowej linii
    file.write(city + "\n")

file.close()



file = open(filename, "a")          # dopisanie do pliku wartosci w trybie "a" czyli append
                                    # tryb "a+" do odczytu i zapisu, ale bez czyszczenia poprzedniej zawartosci
file.write(line)
file.write("\n")

for city in cities:
    file.write(city + "\n")

file.close()
                            


file = open(filename, "w+")     # w+ oznacza ze plik zostanie otwarty i do odczytu i do zapisu, czyli mozna ze soba
# mieszac ze soba funkcje piszace i czytajace, tak jak przy samym "w" poprzednia tresc zostala wyczyszczona a na jej
# miejscu powstala inna tresc

file.write(line)
file.write("\n")

for city in cities:
    file.write(city + "\n")

file.close()
'''


print("\n")
# cwiczenie

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


# inny zapis
'''
import os

webaddresses = []
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
while line != '':
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

print(webaddresses)
dirname = os.getcwd()
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname, filename)
file = open(filepath, 'w+')
for webaddress in webaddresses:
    file.write(webaddress + "\n")
file.close()
'''

# cwiczenie 2
'''
import  os

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
'''
# inny zapis
'''
import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')

# cwiczenie 3
import  os

# D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_5_zapis_do_pliku_tekstowego\\adresses.txt
'''
'''
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
        break'''

# inny zapis
'''
import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line+"\n")
    else:
        fileOther.write(line+"\n")
filePL.close()
fileOther.close()
'''