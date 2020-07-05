def GiveGeomSeqElement(a1=1, factor=2, index=2):
    # value of 64 elements of a geometric string with the first element 1 and a factor of 2
    value = a1 * pow(factor, (index - 1))
    print("Value of {}^{} is: {}".format(factor, index, value))
    return value



