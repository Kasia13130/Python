var_x = 10      # 1
password = "My super secret password"       # 1, 2

#source = "var_x + 2"
#source = "password"
#source = "var_x + 3"
source = "__import__('os').getcwd()"

#globals = globals().copy()
#del globals["password"]
globals = {}


#result = eval(source)
result = eval(source, globals)
print(result)
#print(globals())   