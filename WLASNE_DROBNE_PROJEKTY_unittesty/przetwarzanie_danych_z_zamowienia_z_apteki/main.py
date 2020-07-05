import sys

file_path = r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\podstawy\cwicz11_1_obsluga_bledu_instr_try\orders.csv'

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])

            print("Order from drugstore '%s' item '%s' amount '%d'" % (pharmacy_name, item, amount), "\n")
        except:
            print("Problem in line %s" % line)
            print(sys.exc_info()[0], "\n")

print("Processing finished")