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