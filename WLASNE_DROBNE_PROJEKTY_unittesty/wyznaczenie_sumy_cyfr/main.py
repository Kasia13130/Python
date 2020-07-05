number = 20730906
i = 0

while 0 < number:
    i = i + number % 10
    number = number // 10

print("Sum of 20730906 is: ", i)