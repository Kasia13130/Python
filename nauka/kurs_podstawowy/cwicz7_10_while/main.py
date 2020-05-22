# cwiczenie 1
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
i = 1

while i <= maxTimeYears:
    initialCapital = initialCapital + (initialCapital * percent)

    print("Money after %2d year is: %8d" % (i, initialCapital))

    i += 1

print("All money earn in bank after %2d years is: %5d" % (10, initialCapital))

# rozpoczecie od pierwszego roku
# roczny kapital, czyli pomnozenie miesiecy przez poczatkowy kapital i oprocentowanie
# roczny kapital pomnozony przez ilosc lat
# dodanie do oszczednosci do kapitalu wplaconego

print("\n")

# cwiczenie 1 - inne rozwiazanie
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)

print("\n")


# cwiczenie 2
number = 20730906
i = 0

while 0 < number:
    i = i + number % 10
    number = number // 10

print("Sum of 20730906 is: ", i)

print("\n")


# cwiczenie 2 - inne rozwiazanie
number=20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber >0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits)

print("\n")


# cwiczenie 3
words = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''

listOfWords = words.replace("\n", " ").split(" ")
wordLenght = 6
shortWords = 0
longWords = 0
i = 0

while i < len(listOfWords):
    if len(listOfWords[i]) > wordLenght:
        longWords = longWords + 1
    else:
        shortWords = shortWords + 1

    i += 1
print("Longer words than 'wordLenght' is: ", shortWords)
print("Shorter words than 'wordLenght' is: ", longWords)
print(len(listOfWords))
print(listOfWords)

print("\n")


# cwiczenie 3 - inne rozwiazanie

text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
listOfWords = text.replace('\n', ' ').split(' ')
wordLength = 6
i = 0
shortWords = 0
longWords = 0
while i < len(listOfWords):
    if len(listOfWords[i]) > wordLength:
        longWords += 1
    else:
        shortWords += 1

    i += 1
print("Words shorter than ", wordLength, ":", shortWords)
print("Words longer than ", wordLength, ":", longWords)
