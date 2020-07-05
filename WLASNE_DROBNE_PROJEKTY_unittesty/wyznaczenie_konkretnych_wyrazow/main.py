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