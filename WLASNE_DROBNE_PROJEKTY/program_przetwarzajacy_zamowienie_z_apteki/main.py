import sys

file_path = r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\podstawy\cwicz11_2_funkcja_except\orders.csv'

with open(file_path, "r") as file:

    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])

            print("Order from drugstore '%s' item '%s' amount '%d'" % (pharmacy_name, item, amount), "\n")
        except ValueError as e:
            print("Sorry - conversion error in the third column to int type. Line: %s " % line, "\n")
        except IndexError as e:
            print("Sorry - error with not enough cell. Line: %s " % line, "\n")
        except:
            print("Problem in line %s" % line)
            print(sys.exc_info()[0], "\n")

print("Processing finished")