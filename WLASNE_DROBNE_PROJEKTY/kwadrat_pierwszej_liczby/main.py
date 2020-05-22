numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
maxx = len(numbers) - 1

while i < maxx:
    print(i, numbers[i], numbers[i+1])
    if numbers[i+1] is (numbers[i] * numbers[i]):
        print("\tFound:", numbers[i], numbers[i+1])
    i += 1

# modernizacja skryptu dla trzech liczb
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
maxx = len(numbers) - 2

while i < maxx:
    print(i, numbers[i], numbers[i+1], numbers[i+2])
    if numbers[i+1] is (numbers[i] * numbers[i]) and numbers[i+2] is (numbers[i+1] * numbers[i+1]):
        print("\tFound:", numbers[i], numbers[i+1], numbers[i+2])
    i += 1

