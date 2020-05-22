
i = 1
imax = 10

while i <= imax:
    print(i, "I like Python")
    i += 1
else:
    print("Now i =", i)

print("\n")

# inny przyklad petli
i = 10
imax = 0
while i >= imax:
    print(i, "I like Python")
    i -= 2
else:
    print("Now i =", i)

print("\n")

# cwiczenie
firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print("Row number:", currentRow)
    currentRow += 1

print("\n")

# cwiczenie 2

firstNumber = 1
lastNumber = 13

while firstNumber <= lastNumber:
    print(firstNumber, "kwadrat:", firstNumber ** 2, "szescian:", firstNumber ** 3)
    firstNumber += 1

print("\n")

# cwiczenie 3
firstX = 0
lastX = 16

while firstX <= lastX:
    print("Potega dwojki dla:", firstX, "to", firstX ** 2)
    firstX += 1

print("\n")

# cwiczenie 4

firstSharp = 1
lastSharp = 10

while firstSharp <= lastSharp:
    print(firstSharp * 'x')
    firstSharp += 1
