values = [10, 43, 13, 48, 12, 11, 18, 98, 57, 28, 19, 27, 49, 19, 74]

i = 0
max = len(values) - 2

while i < max:
    print(i, values[i], values[i+1], values[i+2])
    if values[i] < values[i + 1] and values[i+1] < values[i+2]:
        print("\tFound:", values[i], values[i+1], values[i+2])
    i += 1

print("\n")

# cwiczenie
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
maxx = len(numbers) - 1

while i < maxx:
    print(i, numbers[i], numbers[i+1])
    if numbers[i+1] is (numbers[i] * numbers[i]):
        print("\tFound:", numbers[i], numbers[i+1])
    i += 1


print("\n")

# cwiczenie 2
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
maxx = len(numbers) - 2

while i < maxx:
    print(i, numbers[i], numbers[i+1], numbers[i+2])
    if numbers[i+1] is (numbers[i] * numbers[i]) and numbers[i+2] is (numbers[i+1] * numbers[i+1]):
        print("\tFound:", numbers[i], numbers[i+1], numbers[i+2])
    i += 1

print("\n")

# cwiczenie 3
texts = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

i = 0
text = len(texts) -1

while i < text:
    print(texts[i], texts[i+1])
    if len(texts[i]) == len(texts[i+1]):
        print("\tFound", texts[i], texts[i+1])
    i += 1