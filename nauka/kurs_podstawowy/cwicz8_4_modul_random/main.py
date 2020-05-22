import random

print("One random number:", random.randint(1, 100))     # losowanie liczby calkowitej z zakresu od 1 do 100
# w pelnym zakresie
print("\n")

print("Choosing rundon number from a range", random.choice(range(1, 100)))      # zakres od 1 do 99, wybierze jedna
# dostepna wartosc
print("\n")

print("Choosing rundon number from a range - easier", random.randrange(1, 100))     # nakladka poprzedniej funkcji,
# krotszy zapis
print("\n")

list = ["John", "Anna", "Peter", "Susan", "Emily", "Greg", "Chris"]     # losowanie z listy, lista zostanie losowo
# wymieszana w miejscu
random.shuffle(list)
print("Reorgered list:", list)
print("\n")

print("Just a random float", random.random)     # losowanie liczby typu float od 0 do 1
print("\n")

# cwiczenie 2
for i in range(1, 11):
    number = random.randint(1, 100)
    print("Choosing %d number: %d" % (i, number))
print("\n")

# inny zapis
for i in range(10):
    print(random.randint(1,100))

print("\n")

# cwiczenie 3
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
print("\n")

# inny zapis
number1 = random.randint(1, 100)
print("The first generated number is %d" % (number1))

counter = 1
number2 = random.randint(1, 100)

while number1 != number2:
    counter += 1
    number2 = random.randint(1, 100)
    print(counter, number2)

print("I needed %d attempts to generate %d again" % (counter, number1))


# cwiczenie 4
countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark',
             'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland', 'Serbia',
             'Costa Rica', 'Sweden', 'Mexico', 'Korea Republic', 'Germany',  'Belgium', 'England', 'Tunisia', 'Panama',
             'Colombia', 'Japan', 'Senegal', 'Poland']

random.shuffle(countries)
#print(countries)
groupNumber = 0
x = 0


while x < len(countries):

    if x % 4 == 0:
        groupNumber += 1
        print("----Grupa X----")
    print((countries[(x)]))
    x += 1

print("\n")

countries = ['Uruguay',
             'Russia',
             'Saudi Arabia',
             'Egypt',
             'Spain',
             'Portugal',
             'Iran',
             'Morocco',
             'France',
             'Denmark',
             'Peru',
             'Australia',
             'Croatia',
             'Argentina',
             'Nigeria',
             'Iceland',
             'Brazil',
             'Switzerland',
             'Serbia',
             'Costa Rica',
             'Sweden',
             'Mexico',
             'Korea Republic',
             'Germany',
             'Belgium',
             'England',
             'Tunisia',
             'Panama',
             'Colombia',
             'Japan',
             'Senegal',
             'Poland'
             ]

random.shuffle(countries)
groupNumber = 0
countrieNumber = 1

for countrie in countries:
    random.shuffle(countries)
    countrieNumber += 1

    if countrieNumber % 4 == 0:
        groupNumber += 1
        print("----Grupa X----")
    print(random.sample(countries, groupNumber))

print("\n")

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland']

random.shuffle(countries)

groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])
