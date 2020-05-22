# sposob wyswietlenia liczb przy danym parametrze
for number in range(20):
    print(number)           # wyswietli liczby od 0 do 19

print("\n")


for number in range(1, 21):
    print(number)           # wyswietlenie liczb tak jak chcemy czyli od 1 do 20

print("\n")


for number in range(1, 21, 2):
    print(number)           # wyswietlenie liczb nieparzystych z zakresu 1, 21

print("\n")


for number in range(1, 21):     # wyswietlenie liczb parzystyczh i nieparzystych
    if number % 2 == 0:
        print("Number %2d is %s" % (number, "even"))
    else:
        print("Number %2d is %s" % (number, "odd"))

print("\n")

# cwiczenie 1
string_A = "+---+---+---+---+"
string_B = "|   |   |   |   |"

for i in range(10):
    print(string_A)

print("\n")

# cwiczenie 2
for i in range(1, 10):
    if i % 2 == 0:
        print(string_B)
    else:
        print(string_A)

print("\n")

# cwiczenie 3
text = "x"

for i in range(1, 10):
    print("x" * i)

print("\n")

# cwiczenie 4
a = "x"
b = "o"

for i in range(1, 10):
    if i % 2 == 0:
        print("x" * i)
    else:
        print("o" * i)