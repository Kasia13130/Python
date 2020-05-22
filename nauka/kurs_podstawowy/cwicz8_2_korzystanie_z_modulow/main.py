import math         # importowanie modulu (calego), utworzenie nowego podkatalogu w ktorym znajduja sie wszystkie
# funkcje, ale trzeba podac sciezke dlatego przed wpisaniem funkcji nalezy wpisac math.; mozliwosc pracowania i innymi
# modulami o tej samej nazwie
print(math.pi)

print(math.floor(math.pi))

from math import *  # importowanie calego modulu, przyczytanie modulu math ale wszystkie funckje umiescic w glownym
# katalog z wszystkimi funkcjami; jesli chcemy korzystac z dwoch modulow o tej samej nazwie to te funkcje sie przykryja
print(pi)

print(floor(pi))

# importowanie konkretnej funkcji z modulu math
from math import pi
print(pi)
from math import floor
print(floor(pi))

# metody import math najlepiej uzywac w skryptach bo wtedy nie ma mozliwosci by funkcje sie pokrywaly
# metody from math import * najlepiej uzywac w sesjach interaktywnych kiedy chcemu na szybko/na juz uzyc danej funkcji
print("\n")

# cwiczenie
import statistics
percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,

           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,

           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,

           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,

           8.740978348, 6.174819567]

percent.sort()
print(percent)
print("Obliczenie mediany: ", statistics.median(percent), "najnizsza mediana: ", statistics.median_low(percent),
      "najwyzsza mediana: ", statistics.median_high(percent))

print("\n")
from statistics import *
print(median(percent), median_low(percent), median_high(percent))
