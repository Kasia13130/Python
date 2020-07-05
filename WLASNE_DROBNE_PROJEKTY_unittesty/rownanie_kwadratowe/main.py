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