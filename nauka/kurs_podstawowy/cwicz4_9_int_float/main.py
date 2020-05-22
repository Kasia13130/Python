name = "Kasia"
age = 26
daysinYear = 365
message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name, age, daysinYear * age))
print("\n")

message = "%s is %d years old, so is about %d days old"
print(message % (name, age, daysinYear))
print("\n")

name = "Jan"
age = 26
daysinYear = 365
message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name, age, daysinYear * age))
print("\n")

name = "Mateusz"
age = 27
daysinYear = 7584
message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name, age, daysinYear *age))
print("\n")

name = "Chris"
age = 17
daysinYear = 365
message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name, age, daysinYear * age))
print("\n")

one = 1234567890
two = 12345
three = one / two
four = one % two
message = "{0:d} divided by {1:d} is {2:d} and the rest is {3:d}"
print(message.format(one, two, int(three), four))


