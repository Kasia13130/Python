import datetime     # pozwala na korzystanie z funkcji dotyczacych daty i czasu
'''
print("Minimum and maximum", datetime.MINYEAR, datetime.MAXYEAR)        # minimalna i maksymalna wartosc dopuszczalna
# dla roku

# from datetime import timedelta
d1 = datetime.timedelta(days=1, hours=2, minutes=-30)   # mozna to zastosowac jako wektor czasu
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2, minutes=-3)
print(d2)

print("timedelta sum:", d1 + d2)

# from datetime import date

print("Today is", datetime.date.today())        # wywolanie dzisiejszej daty
print("\n")

today = datetime.date.today()           # wyznaczenie np. terminu zaplaty
daysToPay = datetime.timedelta(days=7)
print("Today is ", today)
print("Bills should be paid within:", daysToPay.days, "days")
print("The bill should be paid till:", today + daysToPay)
print("\n")

endOfTheWorld = datetime.date.max       # kiedy bedzie np. koniec swiata
print("The final end of world will happen (by Python) :", endOfTheWorld)
print(endOfTheWorld.weekday())          # jaki to bedzie dzien tygodnia
print("\n")

bornDate = datetime.date(2000, 8, 15)       # ile zyje dni ktos kto urodzil sie 15 sierpnia 2000r
today = datetime.date.today()
print(today - bornDate)
print("\n")

from datetime import datetime

print("now()\t", datetime.now())        # zwraca date i godzine
print("today()\t", datetime.today())        # czas lokalny obowiazujacy w biezacej strefie czasowej,
print("utcnow()\t", datetime.utcnow())          # roznica czasowa 1-2 w zaleznosci od czasu letniego a zimowego
print("weekday()\t", datetime.today().weekday())        # numer dnia tygodnia
print("\n")


print("%a", datetime.now().strftime("%a"))      # funkcja strftime konwertujaca czas do napisu, skrocona nazwa
# dnia tygodnia
print("%A", datetime.now().strftime("%A"))      # pelna nazwa dnia tygodnia
print("%w", datetime.now().strftime("%w"))      # numer dnia tygodnia
print("%a %A %w ", datetime.now().strftime("%a %A %w"))
print("%Y-%m-%d_%H_%M_%S_%f", datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))      # %f to milisekundy

# more details:
# https://docs.python.org/3/library/datetime.html#module-datetime
'''


print("\n")
# cwiczenie 1
inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
factortable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]

import math
print(len(inputdata))
print(len(factortable))

if len(inputdata) == len(factortable):
    for i in range(len(inputdata)):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print("minvalue:", minvalue, "\t", "maxvalue:", maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, "\t", inputdata[i], "\t", round(maxvalue))

elif len(inputdata) != len(factortable):
    print("inputdata and factortable need to have equal number of elements")

print("\n")

# inny zapis
inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
factortable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]
print('input data has  ', len(inputdata), 'elements')
print('factor table has', len(factortable), 'elements')
if len(inputdata) == len(factortable):
    i = 0
    while i < len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print('minvalue=', minvalue, 'maxvalue=', maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, "\t", inputdata[i], "\t", maxinteger)
        i += 1
else:
    print("inputdata and factortable need to have equal number of elements")

print("\n")


# cwiczenie 2
import random

inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(len(inputdata))

for i in range(len(inputdata)):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]
    print("minvalue:", minvalue, "\t", "maxvalue:", maxvalue)

    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger, "\t", inputdata[i], "\t", round(maxvalue))


print("\n")
# inny zapis
i = 0
while i < len(inputdata):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]
    print('minvalue=', minvalue, 'maxvalue=', maxvalue)

    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger, "\t", inputdata[i], "\t", maxinteger)
    i += 1


print("\n")
# cwiczenie 3

import datetime
print("Today is: ", datetime.date.today())
print("Today is:", datetime.date.today().strftime("%Y-%m-%d"))

from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d"))
print("Today is:", datetime.today().strftime("%Y-%m-%d"))

print("\n")

# inny zapis
from datetime import datetime

print('results generated', datetime.today())
print('results generated:', datetime.today().strftime("%Y-%m-%d"))

import datetime
print('results generated', datetime.date.today())
print('results generated:', datetime.date.today().strftime("%Y-%m-%d"))