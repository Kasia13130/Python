import os
import time
'''
print("Current directory is:", os.getcwd())


currentDir = os.getcwd()
filename = "results.txt"
fullpath = os.path.join(currentDir, filename)
print("\nThe constructed file path is: ", fullpath)

reletivePath = "output.txt"
print("\nThe absolute path is: ", os.path.abspath(reletivePath))


filepath = r'c:\temp\results.txt'
print("\nThe file name part is: ", os.path.basename(filepath))
print("The directory part is: ", os.path.dirname(filepath))


print("\nIs file existing? ", os.path.exists(filepath))

if os.path.exists(filepath):
    print("\nLast modify date is:", os.path.getmtime(filepath))
    print("Last modify date is:", time.localtime(os.path.getmtime(filepath)))

    print("\nFile size is:", os.path.getsize(filepath))

    print("\nIs it a file?", os.path.isfile(filepath))
    print("Is it a dir? ", os.path.isdir(filepath))

    print("\nPath splitted:", os.path.split(filepath))
    print("only file name part:", os.path.split(filepath)[1])

    print("\nPath splitted into drive:", os.path.splitdrive(filepath))
    print("Only drive:", os.path.splitdrive(filepath)[0])
'''
print("\n")

# cwiczenie

dir = input("Enter the path: ")

if not os.path.isdir(dir):
    print("A dir not exists")
else:
    file = input("Enter the file name: ")
    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print("A path not exists")
    else:
        print("Path file properties")
        print("Last modify date of path is", time.localtime(os.path.getmtime(path)))
        print("File size is: ", os.path.getsize(path))
        print("Current directory is: ", os.getcwd())
        print("The absolute path is: ", os.path.realpath(path))


print("\n")
'''
# inny zapis

import os
import time

dir = input('enter directory name: ')

if not os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:

    file = input('enter filename saved in directory %s: ' % dir)

    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print('File %s does not exist!' % path)

    else:

        print('displaying properties of file %s' % path)

        print('Last modified date', time.localtime(os.path.getmtime(path)))
        print('Size in bytes', os.path.getsize(path))

        print('Current directory is: ', os.getcwd())
        print('Relative path to the file is', os.path.relpath(path))
'''