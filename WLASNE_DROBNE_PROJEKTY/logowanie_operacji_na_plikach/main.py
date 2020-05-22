# zapis do jednego  pliku
'''
import os
import functools
from datetime import datetime as dt

log_file_path = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\test.txt"


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(log_file_path, "a")
            file.write("-" * 15 + "\n")
            file.write("Action {} in file: {} on: {}\n".format(logged_action, path, dt.now().strftime("%Y-%m-%d%H:%M:%S")))
            file.close()
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file


import os


@wrapper_with_log_file("FILE_CREATE", log_file_path)
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file("FILE_DELETE", log_file_path)
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')
delete_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')
create_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')
delete_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')
'''

# zapis do dwoch osobnych plikow
import os
import functools
from datetime import datetime as dt


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(log_file_path, "a")
            file.write("-" * 15 + "\n")
            file.write("Action {} in file: {} on: {}\n".format(logged_action, path, dt.now().strftime("%Y-%m-%d%H:%M:%S")))
            file.close()
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file


import os


@wrapper_with_log_file("FILE_CREATE", r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\create_file.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file("FILE_DELETE", r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\delete_file.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')
delete_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')
create_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')
delete_file(r'D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz4_2_funkcja_wrappera_z_parametrem\cwiczenie\dummy_file.txt')

