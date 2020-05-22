import math
def GiveGeomSeqElement(a1=2, factor=2, index=2):
    # value of 64 elements of a geometric string with the first element 1 and a factor of 2
    value = a1 * pow(factor, index - 1)
    return value

def GiveFactorForGeomSeq(term, nextterm):
    # determining the coefficient value with two consecutive values known from withinz ciagu
    return nextterm / term

def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    # okreslenie wartosci wspolczynnika przy znanych dwoch kolejnych wyrazach z ciagu
    sum = (a1 * (1 - pow(factor, n))) / (1 - factor)
    return sum
