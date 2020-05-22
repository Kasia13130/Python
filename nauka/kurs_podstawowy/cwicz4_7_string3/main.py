somethinglikeNumber = "1000"
print(somethinglikeNumber)
print(somethinglikeNumber + "1")
print(int(somethinglikeNumber) + int(1))

# sprawdzenie typu wartosci
print(type(somethinglikeNumber))
print(type(int(somethinglikeNumber) + 1))
print("\n")

article = '''Monty Python (also collectively known as the Pythons)[2][3] are a British surreal comedy group who 
created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. 
Forty-five episodes were made over four series. The Python phenomenon developed from the television series into 
something larger in scope and impact, including touring stage shows, films, numerous albums, 
several books and musicals.'''
print(article.upper())
print("\n")

print(article.lower().replace("monty", "flying"))
print("\n")

print(article.split(" "))

howMany = "Python"
value = article.find(howMany)
print("word Python appears " + str(value) + " times")
# inny zapis
print("word Python appears ", article.lower().count("python"), " times")
print("\n")

print("to print the \ you need to put \ twice in your text like this: \\")
print("\n")

print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")
print("\n")

# kalkulator walut
amountPLN = 234
print("cur\texchange\tamount\nUSD\t3.65\t\t" + str(int(amountPLN) / int(3.65)) + "\nEUR\t4.23\t\t" +
      str(int(amountPLN) / int(4.23)))
print("\n")

ValueAsText = '123.45' # pamietac ze jest to wartosc zmiennoprzecinkowa float
factor = 1.23
print("value is " + ValueAsText + " factor is " + str(factor) + " value * factor = " + str(float(ValueAsText) * factor))
