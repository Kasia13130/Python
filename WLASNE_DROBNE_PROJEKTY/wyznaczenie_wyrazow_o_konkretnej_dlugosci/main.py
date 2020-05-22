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