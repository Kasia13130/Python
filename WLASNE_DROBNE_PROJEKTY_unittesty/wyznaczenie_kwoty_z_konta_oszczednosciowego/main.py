initialCapital = 20000
percent = 0.03
maxTimeYears = 10
i = 1

while i <= maxTimeYears:
    initialCapital = initialCapital + (initialCapital * percent)

    print("Money after %2d year is: %8d" % (i, initialCapital))

    i += 1

print("All money earn in bank after %2d years is: %5d" % (10, initialCapital))