import geom
print("Value of 2^64 is:", geom.GiveGeomSeqElement(1, 2, 64))
a1 = 3
factor = 2
maxindex = 10

for i in range(1, maxindex + 1):
    an = geom.GiveGeomSeqElement(a1=a1, factor=factor, index=i)
    print("element", i, "value:", an)

print("Factor is:", geom.GiveFactorForGeomSeq(12, 24))

print("Sum of n elements:", geom.GiveSumOfNElementsGeomSeq(2, 3, 4))