import random

number1 = random.randint(1, 100)
print("First number is %d" % (number1))
counter = 1
number2 = random.randint(1, 100)

while number1 != number2:
    counter += 1
    number2 = random.randint(1, 100)
    print(counter, number2)

print("\n")
print("Number of attempts", counter, number1)