'''
def Calculate(kind="+", *args):
    result = 0
    if kind == "+":
        for a in args:
            result += a
    elif kind == "-":
        for a in args:
            result -= a
    return result


print(Calculate("+", 1, 2, 3))
print(Calculate("-", 1, 2, 3))
'''


def CreateFunction(kind="+"):
    source = """    
def f(*args):       
    result = 0
    for a in args:
        result {}= a    
    return result
""".format(kind)
    exec(source, globals())

    return f


f_add = CreateFunction("+")
print(f_add(1, 2, 3, 4))

f_subs = CreateFunction("-")
print(f_subs(10, 20, 30))

