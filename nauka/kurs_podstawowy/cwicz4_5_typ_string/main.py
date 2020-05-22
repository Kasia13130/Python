atext = "This is a text."

print(atext.endswith("ext"))
print(atext.endswith("ext."))
print(atext.islower())
print(atext.upper())
print(atext.upper().isupper())
print(atext.find('is'))
print(atext.find('is', 3))
print(atext.replace('t', '5'))
print(atext.replace('s', '2'))
print(atext.replace('e', '1').replace('a', '8').replace('h', '0'))
print(atext.split(' '))

somethingLikeNumber = '1000'

print(somethingLikeNumber + '1')
print(somethingLikeNumber.isdigit())
print(somethingLikeNumber.isdigit())
print(somethingLikeNumber.isalpha())
print(somethingLikeNumber.isalnum())
print("\n")

quote = "A good programmer is someone who always looks both ways before crossing a one-way street"
print(quote.upper())
print(quote.lower())
print(quote.endswith("street"))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find("one"))
print(quote.replace("one", "1"))
print(quote.replace("one", "1").replace("both", "2"))
print(quote.split(" "))
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())