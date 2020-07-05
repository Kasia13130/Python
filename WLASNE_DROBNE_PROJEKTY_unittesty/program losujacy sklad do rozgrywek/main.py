import random

countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark',
             'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland', 'Serbia',
             'Costa Rica', 'Sweden', 'Mexico', 'Korea Republic', 'Germany',  'Belgium', 'England', 'Tunisia', 'Panama',
             'Colombia', 'Japan', 'Senegal', 'Poland']

random.shuffle(countries)
groupNumber = 0
x = 0


while x < len(countries):

    if x % 4 == 0:
        groupNumber += 1
        print("----Grupa X----")
    print((countries[(x)]))
    x += 1