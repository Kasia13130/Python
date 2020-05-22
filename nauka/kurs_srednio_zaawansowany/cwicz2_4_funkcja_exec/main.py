var_x = 10

source = "var_x + 4"

result = eval(source)
print(result)

source = "var_x = 4"

result = eval(source)
print(result)

print(var_x)

#var_x = 10
source = """
var_x = 4       
"""

result = exec(source)
print(result)
print(var_x)


var_x = 10
source = """
for i in range(var_x):      
    print("-" * i)
"""

result = exec(source)
print(result)

print(var_x)


var_x = 10
source = """
new_var = 1             
for i in range(var_x):
    print("-" * i)
    new_var += i        
"""

result = exec(source)
print(result)

print(var_x)
print(new_var)

source = input("Enter your expression: ")
print(eval(source))     