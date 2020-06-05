text_list = ["x", "xxx", "xxxxx", "xxxxxxx", ""]

f = lambda text: len(text)

print(f("Ala ma kota"))

print(f(text_list[0]))
print(list(map(f, text_list)))

print(list(map(lambda text: len(text), text_list)))