'''
import sys      # dla rozpoznawania jaki blad wystapil, nalezy zaimportowac "sys"

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input("How many persons are there in the team? ")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except:
    print("Something went wrong...", sys.exc_info()[0])     # dopisanie odwolania do sys.exc_info()[0], funkcja zwraca
    # tuple o trzech kolumnach, pierwsza kolumna zawiera informacje do jakiego bledu doszlo podczas uruchamiania skryptu

print("Every person should have around ", tasksPerPerson, "tasks")
'''

print("\n")
# cwiczenie

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


# inny zapis
'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10
Pharma at grocery,Amoxicillin,?
Pharmacy 123,Cephalexin,100
Pharmacy 123,Prednisolone Sodium Phosphate
Pharma X,Nystatin,45'''
'''
import sys

file_path = r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\podstawy\cwicz11_1_obsluga_bledu_instr_try\orders2.csv'

with open(file_path, "r") as file:
    for line in file:

        line = line.replace('\n', '')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                  (pharmacy_name, item, amount))
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])

print("Processing finished")'''