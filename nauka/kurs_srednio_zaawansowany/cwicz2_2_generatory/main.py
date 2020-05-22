listaA = list(range(6))
listaB = list(range(6))

product = [(a, b) for a in listaA for b in listaB if a % 2 == 1 if b % 2 == 0]
print(product)
print("\n")


gen = ((a, b) for a in listaA for b in listaB if a % 2 == 1 if b % 2 == 0)
print(gen)
print("\n")

print(next(gen))
print(next(gen))
print("-" * 20)

for x in gen:
    print(x)
print("-" * 20)

for x in gen:
    print(x)
print("\n")
print("^" * 20)

gen = ((a, b) for a in listaA for b in listaB if a % 2 == 1 if b % 2 == 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("all value have been generated")
        break