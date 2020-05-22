'''
file = open("D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\joke.txt.txt", "r")

content = file.read()
print(content)

file.close()
# --------------------------------------------

with open("D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\joke.txt.txt", "r") as file:
    content = file.read()
    print(content)

# -------------------------------------------
with open("D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\joke.txt.txt", "r") as file:
    for line in file:
        print(line)

# ------------------------------------------

file = open("D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\joke.txt.txt", "r")
for line in file.readlines():
    print(line)
file.close()

# ------------------------------------------
file = open("D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\joke.txt.txt", "r")
fragment = file.read(10)
while fragment:
    print(fragment)
    fragment = file.read(10)
file.close()

# ------------------------------------------

file = open("D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\joke.txt.txt", "r")
fragment = file.read(10)
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)
file.close()
'''

print("\n")

# cwiczenie
file_path = (r"D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\orders.csv")

with open(file_path, "r") as file:
    for line in file:
        order = line.replace("\n", "").replace(";", "").split(",")

        if len(order) == 3:
            print("Order from drugstore '%s', item '%s' amount '%s'" % (order[0], order[1], order[2]))
        if len(order) != 3:
            print("Line %s malformed !!!" % (order))
print("\nData processing completed!")


print("\n")
# iiny zapis
'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10'''

file_path = (r"D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\orders2.csv")

with open(file_path, "r") as file:
    for line in file:

        line = line.replace('\n', '')
        order = line.split(',')

        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)

print("Processing finished")