import os
import time

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