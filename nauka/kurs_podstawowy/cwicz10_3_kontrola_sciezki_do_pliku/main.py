# sprawdzenie czy sciezka dostepu do pliku jest poprawna
# I sposob
'''
import os

fileIsOk = False

while not fileIsOk:

    filename = input("Enter path to results file: ")

    if os.path.isfile(filename):
        fileIsOk = True

print("The results file is %s" % (filename))

# II sposob
# by petla mogla sie wykonywac bez przerwy i sprawdzenie czy sciezka jest poprawna

import os

while True:
    filename = input("Enter path to results files: ")

    if os.path.isfile(filename):
        break
    else:
        print("File name is not correct, try again!")

    print("The results file is %s" % (filename))

'''
print("\n")
# cwiczenie
import os
import datetime

data_input_catalog = r"c:\temp\data_input"
data_output_catalog = r"c:\temp\data_output"
today = datetime.date.today()

today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
print(today_output_catalog)

is_input_catalog_ok = not os.path.exists(data_input_catalog) and not os.path.isdir(data_input_catalog)
print(is_input_catalog_ok)

is_output_catalog_ok = not os.path.exists(data_output_catalog) and not os.path.isdir(data_output_catalog)
print(is_output_catalog_ok)

is_today_output_catalog_ok = not os.path.exists(today_output_catalog) and not os.path.isdir(today_output_catalog)
print(is_today_output_catalog_ok)


if is_input_catalog_ok == True and is_output_catalog_ok == True and is_today_output_catalog_ok == True:
    print("Conditions met! We can continue!")

else:

    if (is_input_catalog_ok == False) and (is_output_catalog_ok == False) and (is_today_output_catalog_ok == False):
        print("Error: input_catalog, output_catalog and today_output_catalog not exists!")
    elif (is_input_catalog_ok == False) and (is_today_output_catalog_ok == False):
        print("Error: input_catalog and today_output_catalog not exists!")
    elif (is_output_catalog_ok == False) and (is_today_output_catalog_ok == False):
        print("Error: output_catalog not exist and today_output_catalog exists!")
    elif (is_input_catalog_ok == False) and (is_output_catalog_ok == False):
        print("Error: input_catalog and output_catalog not exists!")
    elif (is_input_catalog_ok == False):
        print("Error: %s not exist!")
    elif (is_output_catalog_ok == False):
        print("Error: output_catalog not exist!")
    elif (is_today_output_catalog_ok == False):
        print("Error: today_output_catalog")

'''
print("\n")

# inny zapis
data_input_catalog = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'

today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))

# checking conflicts

# input folder must exist
is_input_catalog_ok = os.path.isdir(data_input_catalog)

# output folder must exist
is_output_catalog_ok = os.path.isdir(data_output_catalog)

# today output catalog cannot exist
is_today_output_catalog_ok = not (os.path.isdir(today_output_catalog)) and \
                             not (os.path.isfile(today_output_catalog))

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')

    # display detailed error conditions
    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % data_input_catalog)
    if not is_output_catalog_ok:
        print("Output catalog %s must exist!" % data_output_catalog)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)
'''