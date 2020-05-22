message1 = "Procesing file %s"
print(message1 % ("file1.txt"))

message2 = "File %s has size %d KB"
print(message2 % ("file1.txt", 100))

message3 = "File %20s has size %10d KB"
print(message3 % ("file.txt", 100))

message4 = "Processing file {0:s}"
print(message4.format("file1.txt"))

message5 = "File {0:s} has size {1:d}"
print(message5.format("file1.txt", 100))

message5 = "File {1:s} has size {0:d}"
print(message5.format(100, "file1.txt"))

message6 = "File {0:20s} has size {1:10d}"
print(message6.format("file1.txt", 100))
print("\n")


helloMessage = "Hello %s !"
print(helloMessage % ("helloMessage"))
print("\n")

helloMessage = "Hello %s! Hello %s!"
print(helloMessage % ("Kate", "Chris"))
print("\n")

helloMessage = "Hello {0:s}! Hello {1:s}!"
print(helloMessage.format("Kate", "Chris"))
print("\n")

helloMessage = "%s has %d %s"
print(helloMessage % ("Kate", 1, "animal"))
print("\n")

helloMessage = "%s has %d %s"
print(helloMessage % ("Chris", 100000, "$"))
print("\n")

helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format("Kate", 1, "animal"))
print("\n")

helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format("Chris", 100000, "$"))
print("\n")

line = "%20s %20s %6d %s"
print(line % ("ICE CREAM", "costs", 3, "€"))
print(line % ("TRIP TO VENICE", "costs", 119, "€"))
print(line % ("PIZZA HAWAII", "costs", 6, "€"))
print("\n")

# inny zapis
line = "{0:20s} costs {1:6d} €"
print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAWAII", 6))
print("\n")

line = "%s %d"
print(line % ("ICE CREAM", 3))
print(line % ("TRIP TO VENICE", 119))
print(line % ("PIZZA HAWAII", 6))

