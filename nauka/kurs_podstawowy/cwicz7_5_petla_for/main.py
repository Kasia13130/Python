persons = ["Elizabeth", "Steven", "Sebastian", "Margareth", "Svetlana", "Raphael"]

domain = "mycompany.com"

for person in persons:
    email = person + "@" + domain
    print("Email for\t", person, "\tis\t", email)
# mozna dodac else
else:
    print("-- end the list --")

print("\n")

# cwiczenie 1
data = ["Error:File cannot be open",
        "Error:No free space on disk",
        "Error:File missing",
        "Warning:Internet connection lost",
        "Error:Access denied"]

for text in data:
    print(text.upper())

print("\n")

# cwiczenie 2
data = ["Error:File cannot be open",
        "Error:No free space on disk",
        "Error:File missing",
        "Warning:Internet connection lost",
        "Error:Access denied"]

for text in data:
    elements = text.split(":")
    print(elements[0].upper())
    print(elements[1])


print("\n")

# cwiczenie 3
data = ["Error:File cannot be open",
        "Error:No free space on disk",
        "Error:File missing",
        "Warning:Internet connection lost",
        "Error:Access denied"]

for text in data:
    elements = text.split(":")
    if "Error" in elements[0]:
        print(elements[1].upper())
    else:
        print(elements[1])

print("\n")

# inny zapis kodu
for text in data:
    elements = text.split(":")
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])