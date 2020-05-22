fibobaciIterations = 20
a1 = 0
a2 = 1
a3 = 0
i = 0

print(str(a1))
print(str(a2))

for i in range(0, 20):
    a3 = a1 + a2
    print(str(a1) + " + " + str(a2) + " = " + str(a3))
    a1 = a2
    a2 = a3

    if a1 == 20:
        break