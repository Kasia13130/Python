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

