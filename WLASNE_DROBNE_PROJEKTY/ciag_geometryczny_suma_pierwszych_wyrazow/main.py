def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    # okreslenie wartosci wspolczynnika przy znanych dwoch kolejnych wyrazach z ciagu

    sum = (a1 * (1 - pow(factor, n))) / (1 - factor)
    return sum


print("Sum of n elements:", GiveSumOfNElementsGeomSeq(2, 3, 4))