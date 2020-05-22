listaA = list(range(6))
listaB = list(range(6))

print(listaA, listaB)
print("\n")

product = []
for a in listaA:
    for b in listaB:
        product.append((a, b))
print(product)
print("\n")


product = [(a, b) for a in listaA for b in listaB]
print(product)
print("\n")


product = [(a, b) for a in listaA for b in listaB if a % 2 == 1 if b % 2 == 0]
print(product)
print("\n")

product = {a: b for a in listaA for b in listaB if a % 2 == 1 if b % 2 == 0}
print(product)
print("\n")