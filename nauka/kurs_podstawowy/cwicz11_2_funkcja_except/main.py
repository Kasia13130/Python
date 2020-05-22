'''
import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input("How many persons are there in the team? ")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except ValueError as e:
    print("Sorry - you need to enter an integer number:", e)

except ZeroDivisionError as e:
    print("Sorry - you need to enter value > 0:", e)

except:
    print("Something went wrong...", sys.exc_info()[0])

print("Every person should have around ", tasksPerPerson, "tasks")
'''

print("\n")
# cwiczenie
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


print("\n")
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

file_path = r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\podstawy\cwicz11_2_funkcja_except\orders2.csv'

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

        except ValueError as e:
            print("Problem with conversion. Check whether the amount is correct. Line: %s" % line)

        except IndexError as e:
            print(
                "Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: %s" % line)

        except:
            print("General error: %s" % sys.exc_info()[0])

print("Processing finished")'''