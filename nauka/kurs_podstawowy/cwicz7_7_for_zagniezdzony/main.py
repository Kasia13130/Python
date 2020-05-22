for x in range(1, 6):
    for y in range(1, 6):
        print(x, " * ", y, " = ", x * y)

print("\n")

# wyswietlenie x i y w liniach by bardzie przypominaly tabelke
for x in range(1, 6):
    line = str(x)
    for y in range(1, 6):
        line += "\t" + str(x*y)
    print(line)

print("\n")

# przesuniecie kolumn w tabeli
for x in range(1, 6):
    line = str(x)
    for y in range(1, 6):
        line += ("\t%3d" % (x * y))     # do linii dodany jest odstep jako tabulacja z %3d jako trzy miejsca na wartosc
    print(line)

print("\n")

# cwiczenie
i = 10
for i in range(10, 11):
    j = 1
    line = str(i) + "! = 1"
    for y in range(2, i + 1):
        line += " * " + str(y)
        j *= y
    line += " = " + str(j)
    print(line)

print("\n")

# cwiczenie 2
i = 10
for i in range(2, 11):
    j = 1
    line = str(i) + "! = 1"
    for y in range(2, i + 1):
        line += " * " + str(y)
        j *= y
    line += " = " + str(j)
    print(line)

print("\n")

# inny zapis
x = 10
for i in range(1, x + 1):
    result = 1
    for j in range(1, i + 1):
        result *= j
    print(i, "!", result)

print("\n")

# cwiczenie 3
list_noun = ["dog", "potato", "meal", "icecream", "car"]
list_adj = ["dirty", "big", "hot", "colorful", "fast"]

for noun in list_noun:
    for adj in list_adj:
        print(adj, "-",  noun)
