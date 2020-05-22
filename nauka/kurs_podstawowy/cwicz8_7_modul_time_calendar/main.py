import time

print("Current time is... unix epoch", time.time())     # zwraca czas wyrazony w unix, czyli liczba sekund ktore minely
# od 1 stycznia 1970 roku
#Current time is... unix epoch 1582143391.3755977
print("\n")

print("Current time is... tuple", time.localtime(time.time()))      # czas unix, przedstawiony w tuple czyli krotce
# Current time is... tuple time.struct_time(tm_year=2020, tm_mon=2, tm_mday=19, tm_hour=21, tm_min=16, tm_sec=31,
# tm_wday=2, tm_yday=50, tm_isdst=0)
print("\n")

print("Current time is... for human", time.asctime(time.localtime(time.time())))        # w nawiasach sa parametry
# tych funkcji
#Current time is... for human Wed Feb 19 21:16:31 2020
print("\n")

#print("Current time is... for human", time.localtime(time.clock()))    # bardzo dokładne podanie czasu
print("\n")
print("Current time is... for human", time.perf_counter())
print("\n\n\n\n")


import calendar
print(calendar.month(2017, 9, w=5, l=2))       # wyswietlenie kalendarza na konkretny miesiac, na kazdy dzien
# przeznaczone jest 5 znakow, a odstepy miedzy znakami wynosza 2
print("\n")
print(calendar.month(2017, 9))      # wyswietlenie kalendarza bez dodatkowych parametrow
print("\n")
print("week day is", calendar.weekday(2017, 9, 29))     # ktory dzien tygodnia byl okreslonego dnia
print("\n")
calendar.setfirstweekday(6)     # funkcja, ktora ustala ktory dzien tygodnia ma sie jako pierwszy wyswietlic, w tym
# przypadku niedziela
print(calendar.month(2017, 9))
print("\n")
print("week day is", calendar.weekday(2017, 9, 29))     # nadal bedzie wyswietlany czwarty dzien
print("\n")
print("is 2020 a leap year", calendar.isleap(2020))     # sprawdza czy dany rok jest przystepny
print("\n")
print("Leap days 2000-2017", calendar.leapdays(2000, 2017))     # ile bylo dni przystepnych w tych latach, ale bez
# roku 2017
print("Leap days 2000-2020", calendar.leapdays(2000, 2020))     # to samo ale bez roku 2020
print("Leap days 2000-2021", calendar.leapdays(2000, 2021))     # to samo ale 2020 juz sie liczy, ale bez 2021
print("\n")

print(calendar.calendar(2018))      # parametrem jest rok, zwroci caly kalendarz na dany rok

print("\n")

# cwiczenie 1
print("Czas w postaci Unix Epoche", time.time())
print("Wersja dla człowieka", time.localtime(time.time()))

print("\n")

print(calendar.month(2020, 2))
calendar.setfirstweekday(6)
print(calendar.month(2020, 2))
print(calendar.isleap(2000))
print(calendar.calendar(2019))