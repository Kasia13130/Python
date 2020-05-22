def GiveGeomSeqElement(a1=2, factor=2, index=2):
    # value of 64 elements of a geometric string with the first element 1 and a factor of 2
    value = a1 * pow(factor, index - 1)

    return value

print("Value of 2^64 is:", GiveGeomSeqElement(1, 2, 64))