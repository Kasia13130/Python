a = b = c = 10
print("Is value the same?", a == b == c)
print(id(a), id(b), id(c))

print("\n")
a = 20
print("Is value the same?", a == b == c)
print(id(a), id(b), id(c))

print("\n")
a = b = c = [1, 2, 3]
a.append(4)
print("Is value the same?", a == b == c)
print(id(a), id(b), id(c))
print(a, b, c)

print("\n")
x = 10
y = 10
print(id(x), id(y))
print("\n")
y = y + 1 - 1
print(id(x), id(y))
print("\n")
y = y + 1234567890 - 1234567890
print(id(x), id(y))
