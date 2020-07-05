diskSize = 100
diskSizeUsed = 90
fileSize = 15

if fileSize <= (diskSize - diskSizeUsed):
    print("File can be downoladed")
else:
    print("No space on disk")