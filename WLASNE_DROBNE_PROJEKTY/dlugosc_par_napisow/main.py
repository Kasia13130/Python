texts = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

i = 0
text = len(texts) -1

while i < text:
    print(texts[i], texts[i+1])
    if len(texts[i]) == len(texts[i+1]):
        print("\tFound", texts[i], texts[i+1])
    i += 1
