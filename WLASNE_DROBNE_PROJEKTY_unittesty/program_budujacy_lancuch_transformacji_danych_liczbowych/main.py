
def double(x):
    return 2 * x

def root(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2


transformation = [double, root, div2, negative]
transformation2 = [root, root, div2, double]
number = 6

tmp_return_value = number

for tran in transformation:
    print("{}: transformation value is {}".format(tran.__name__, tran(tmp_return_value)))
print("\n")

for tran in transformation2:
    print("{}: transformation value is {}".format(tran.__name__, tran(tmp_return_value)))
