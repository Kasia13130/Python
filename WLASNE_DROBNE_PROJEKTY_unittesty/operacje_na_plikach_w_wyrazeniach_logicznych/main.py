
import os

def readingFile(path_txt):

    with open(path_txt, "r") as file:
        file = file.read().replace(",", " ").split()
        print(file)
        file = len(file)

    return file


path_txt = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz1_4_operacje_na_plikach_w_wyrazeniach_logicznych\cwiczenie\path.txt"


if os.path.isfile(path_txt):
    print("There are: ", readingFile(path_txt), "words")

result = os.path.isfile(path_txt)
print("There are: ", readingFile(path_txt), "words")


'''Jest sloneczna pogoda,
na niebie jest kilka bialych chmurek,
ptaki cwierkaja.'''
