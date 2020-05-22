def GiveGeomSeqElement(a1=2, factor=2, index=2):
    # value of 64 elements of a geometric string with the first element 1 and a factor of 2
    value = a1 * pow(factor, index - 1)

    return value

a1 = 3
factor = 2
maxindex = 10

for i in range(1, maxindex):
    an = GiveGeomSeqElement(a1=a1, factor=factor, index=i)
    print("element", i, "value:", an)

