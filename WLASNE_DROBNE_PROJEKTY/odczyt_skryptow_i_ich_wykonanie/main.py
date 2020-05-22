files_to_process = [
    r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz2_4_funkcja_exec\cwiczenie\script1.txt",
    r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz2_4_funkcja_exec\cwiczenie\script2.txt"
    ]

import os

print(os.path.basename("script1.txt"))
print(os.path.basename("script2.txt"))

source = """
with open("script1.txt", "r")
with open("script2.txt", "r")  
"""
print("For script1: "), exec(open("script1.txt").read())
print("For script2: "), exec(open("script2.txt").read())
