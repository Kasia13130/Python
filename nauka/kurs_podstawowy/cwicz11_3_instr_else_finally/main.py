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

else:
    print("Every person should have around ", tasksPerPerson, "tasks")

finally:
    print("Script finished with/without errors")

'''
print("\n")

# cwiczenie 1
'''
line = input("Price of next curse: ")
filepath = input("Enter file name: ")

file = open(filepath, "w")
file.write(line)
file.close()
'''
# cwiczenie 2
'''
import os

line = input("Price of next curse: ")
filepath = input("Enter file name: ")

try:
    file = open(filepath, "w")
    file.write(line)
    file.close()

except:
    print("Sorry - we have an error. Try again.")
'''

# cwiczenie 3
'''
import os
import sys

line = input("Price of next curse: ")
filepath = input("Enter file name: ")

try:
    file = open(filepath, "w")
    file.write(line)
    file.close()

except FileNotFoundError as e:
    print("Error opening file", filepath, e)
except:
    print("Sorry - we have an error. Try again.", sys.exc_info()[0])

'''

# cwiczenie 4
'''
import sys
line = input("Price of next curse: ")
filepath = input("Enter file name: ")

try:
    file = open(filepath, "w")
    file.write(line)
    file.close()
    value = int(line)
    print("The value saved in file is...", value)

except FileNotFoundError as e:
    print("Error opening file", filepath, e)
except:
    print("Sorry - we have an error. Try again.", sys.exc_info()[0])
    
'''

# cwiczenie 5

import sys
line = input("Price of next curse: ")
filepath = input("Enter file name: ")

try:
    file = open(filepath, "w")
    file.write(line)
    file.close()
    value = int(line)
    print("The value saved in file is...", value)

except FileNotFoundError as e:
    print("Error opening file: ", filepath, e)
except ValueError as e:
    print("The value entered cannot be converted to a number: ", e)
except:
    print("Sorry - we have an error. Try again.", sys.exc_info()[0])
else:
    print("Actions completed successfully")


# inny zapis
'''
line = input('Enter accepted price: ')
filepath = input('Enter filename : ')

file = open(filepath, 'w+')
file.write(line)
file.close()'''
# -------
'''
line = input('Enter accepted price: ')
filepath = input('Enter filename : ')

try:
    file = open(filepath, 'w+')
    file.write(line)
    file.close()
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')'''
# -------
'''
line = input('Enter accepted price: ')
filepath = input('Enter filename : ')

try:
    file = open(filepath, 'w+')
    file.write(line)
    file.close()
except FileNotFoundError as e:
    print('Error opening file', filepath, e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')'''
# ---------
'''
line = input('Enter accepted price: ')
filepath = input('Enter filename : ')

try:
    file = open(filepath, 'w+')
    file.write(line)
    value = int(line)
    file.close()
    print('The value saved in file is', value)
except FileNotFoundError as e:
    print('Error opening file', filepath, e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')'''
# --------
'''
line = input('Enter accepted price: ')
filepath = input('Enter filename : ')

try:
    file = open(filepath, 'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is', value)
except FileNotFoundError as e:
    print('Error opening file', filepath, e)
except ValueError as e:
    print('The value entered cannot be converted to a number', line, e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print('Actions completed successfully')
'''