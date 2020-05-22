import random

for i in range(32, 127):
   print(i, chr(i))

print("\n")

ints = range(33, 127)       # zakres dla tablicy ASCII
password = ""

for i in range(16):         # haslo bedzie losowane dla 16 znakow
    password += chr(random.choice(ints))        # chr oznacza tablice ASCII, a choice oznacza wybor ze zmiennej
                                                # wczesniej utworzonej
print("Password is:", password)

print("\n")

# cwiczenie 1
min = 1
max = 6
dice = random.choice(range(min, max))

if dice == 1:
    print("%3s" % ("o"))
elif dice == 2:
    print("%3s \n \n%s" % ("o", "o"))
elif dice == 3:
    print("%3s \n%2s \no" % ("o", "o"))
elif dice == 4:
    print("o %3s \n \no %3s" % ("o", "o"))
elif dice == 5:
    print("o %3s \n%3s \no %3s" % ("o", "o", "o"))
else:
    print("o %3s \no %3s \no %3s" % ("o", "o", "o"))

print("\n")

# inny zapis
min = 1
max = 6

dice = random.randint(min, max)

if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')

print("\n")

# cwiczenie 2
dices = []
for i in range(5):
    dice = random.choice(range(min, max))

    dices.append(dice)
    dices.sort()
print(dices)


print("\n")
# inny zapis
dices = []
for i in range(5):
    dices.append(random.randint(min, max))

dices.sort()
print(dices)