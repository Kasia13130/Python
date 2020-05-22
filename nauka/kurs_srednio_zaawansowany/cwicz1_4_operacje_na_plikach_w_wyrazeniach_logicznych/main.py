# badamy czy plik istnieje, a jesli nie to go tworzymy

import os

path = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz1_4_operacje_na_plikach_w_wyrazeniach_logicznych\mydata.txt"

os.remove(path)
if os.path.isfile(path):
    print("File %s exist" % path)
else:
    print("Creating a file: %s" % path)
    open(path, "x").close()
    print("File: %s created" % path)


# inny zapis
'''
path = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz1_4_operacje_na_plikach_w_wyrazeniach_logicznych\mydata.txt"

#os.remove(path)

#result = os.path.isfile(path)    
result = os.path.isfile(path) or open(path, "x").close()    

print(result)


# kolejny zapis
path = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz1_4_operacje_na_plikach_w_wyrazeniach_logicznych\mydata.txt"

#os.remove(path)

result = os.path.isfile(path) or open(path, "x").close()    
print(result)


# kolejny zapis
path = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz1_4_operacje_na_plikach_w_wyrazeniach_logicznych\mydata.txt"

#os.remove(path)

result = os.path.isfile(path) and open(path, "x").close()

print(result)


# kolejny zapis
path = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz1_4_operacje_na_plikach_w_wyrazeniach_logicznych\mydata.txt"

os.remove(path)

result = os.path.isfile(path) and open(path, "x").close()

print(result)
'''
