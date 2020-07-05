
import math

argument_list = []
i = 0

while len(argument_list) < 100:
    argument_list.append(i/10)
    i += 1

formula = input("Enter equation with x: ")
for x in argument_list:
    print("{0:3.1f}  {1:6.2f}".format(x, eval(formula)))
