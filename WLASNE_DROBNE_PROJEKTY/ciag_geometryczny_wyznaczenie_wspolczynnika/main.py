def GiveFactorForGeomSeq(term, nextterm):
    # determination of the coefficient value by means of two successive values known from the geometric string

    return nextterm / term


print("Factor is:", GiveFactorForGeomSeq(12, 24))