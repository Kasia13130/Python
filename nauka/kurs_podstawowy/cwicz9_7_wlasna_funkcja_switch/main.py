def GiveGeomSeqElement(a1=2, factor=2, index=2):
    # value of 64 elements of a geometric string with the first element 1 and a factor of 2
    value = a1 * pow(factor, index - 1)

    return value

print("Value of 2^64 is:", GiveGeomSeqElement(1, 2, 64))

a1 = 3
factor = 2
maxindex = 10

for i in range(1, maxindex):
    an = GiveGeomSeqElement(a1=a1, factor=factor, index=i)
    print("element", i, "value:", an)

print("\n")

# cwiczenie 3
def GiveFactorForGeomSeq(term, nextterm):
    # determination of the coefficient value by means of two successive values known from the geometric string

    return nextterm / term


print("Factor is:", GiveFactorForGeomSeq(12, 24))

print("\n")

# cwiczenie 4
def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    # okreslenie wartosci wspolczynnika przy znanych dwoch kolejnych wyrazach z ciagu

    sum = (a1 * (1 - pow(factor, n))) / (1 - factor)
    return sum


print("Sum of n elements:", GiveSumOfNElementsGeomSeq(2, 3, 4))