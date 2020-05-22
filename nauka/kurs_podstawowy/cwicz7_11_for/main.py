# cwiczenie 1
fibobaciIterations = 20
a1 = 0 #wynik poprzedni poprzedni
a2 = 1 #wynik poprzedni
a3 = 0 #wynik obecny
i = 0

print(str(a1))
print(str(a2))

for i in range(0, 20):
    a3 = a1 + a2
    print(str(a1) + " + " + str(a2) + " = " + str(a3))
    a1 = a2
    a2 = a3

    if a1 == 20:
        break

print("\n")
# inny zapis cwiczenia
fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(0,20):
    print('Step',i,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2

print("\n")


# cwiczenie 2
text = '''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
'''
listOftext = text.replace("\n", " ").split(" ")
print(listOftext)
print("\n")
i = 0
words = []

for text in listOftext:
    for x in text:
        if x == "p":
            words.append(text)
            continue
        elif x == "P":
            words.append(text)

print("Words witch have 'p' or 'P' is: ", words)

print("\n")

# inny zapis cwiczenia
text='''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn't do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it's an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can't.
'''
listOfWords = text.replace("\n"," ").split(' ')
for word in listOfWords:
    if word.lower().find('p')>=0:
        print(word)

print("\n")

# cwiczenie 3
dictionary = {"A": "80%-100%", "B": "60%-80%", "C": "50%-60%", "D": "less then 50%"}

for key, value in dictionary.items():
    print(key + " - " + value)

print("\n")
# inny zapis cwiczenia
dictionary={'A':'80%-10%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
for word in dictionary.keys():
    print(word,'-',dictionary[word])

print("\n")

# cwiczenie 4
text = '''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
'''
wordDictionary = {}
listOfWords = text.replace("\n", "").replace(",", "").replace(":", "").lower().split(" ")

for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] += 1
    if word not in wordDictionary.keys():
        wordDictionary[word] = 1


print(wordDictionary)
print(wordDictionary.values())
print(wordDictionary.keys())

print("\n")

# inny zapis cwiczenia
wordDictionary = {}
for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word] + 1
    else:
        wordDictionary.setdefault(word, 1)

print(wordDictionary)