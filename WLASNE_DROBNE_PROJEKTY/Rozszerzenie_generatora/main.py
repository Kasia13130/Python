def gen():
    x = 0
    while True:
        y = yield x
        if y is None:
            x = x + 1
        else:
            x = y


g = gen()

print(next(g))
print(next(g))
print(next(g))

print(g.send(12))
print(next(g))
print(next(g))

print(g.send(20))
print(next(g))
g.close()


def gen():
    while True:
        try:
            yield 1
        except GeneratorExit:
            print("wyjatek zostal rzucony")
            return


g = gen()
next(g)

g.throw(GeneratorExit)
g2 = gen()
next(g2)
g2.close()

# dowiedziec sie czemu jest blad !!!
