i = 10
for i in range(2, 11):
    j = 1
    line = str(i) + "! = 1"
    for y in range(2, i + 1):
        line += " * " + str(y)
        j *= y
    line += " = " + str(j)
    print(line)