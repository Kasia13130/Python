# filename = input("Enter filename: ")
# print("The file name is: %s" % (filename))
'''
while True:
    filesizeStr = input("Enter the max file size (MB): ")   # pobranie napisu z konsoli

    if filesizeStr.isdecimal():     # jezeli pobrana wartosc z konsoli jest napisem to trzeba ja przekonwertowac na liczbe
        filesizeInt = int(filesizeStr)      # konwersja na liczbe
        break

print("The max size is %d" % (filesizeInt))

print("Size in KB is %d" % (filesizeInt * 1024))

print("\n")
'''

# cwiczenie 1

import math


a = input("Enter value a: ")
b = input("Enter value b: ")
c = input("Enter value c: ")


if ((a.isalpha()) or (b.isalpha()) or (c.isalpha())):
    print("a, b, c must be digit")

else:
    if ((a.isdecimal()) or (b.isdecimal()) or (c.isdecimal())):
        a = int(a)
        b = int(b)
        c = int(c)

        if a == 0:
            print("a == 0")
        else:
            delta = (b * b) - (4 * a * c)

            if delta < 0:
                print("No solution")
            elif delta == 0:
                x1 = (-b - math.sqrt(delta)) / 2 * a
                print("One solution: %.2f" % (x1))
            elif delta > 0:
                x1 = (-b - math.sqrt(delta)) / (2 * a)
                x2 = (-b + math.sqrt(delta)) / (2 * a)
                print("Two solution: x1: %.2f and x2: %.2f" % (x1, x2))

'''
print("\n")

# inny zapis

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


print('This program solves equation ax^2+bx+c = 0')
print('Enter the values for a, b and c:')

a_str = input('a=')
b_str = input('b=')
c_str = input('c=')

if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print("a, b and c need to be int!")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)

    if a == 0:
        print('a cannot be 0!')
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print("there is no solution")
        elif delta == 0:
            x1 = -b / (2 * a)
            print("there is one solution: %.2f" % (x1))
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print("there are two solutions: %.2f and %.2f" % (x1, x2))
'''
