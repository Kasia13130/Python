import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
argument_list = []
for i in range(1000):
    argument_list.append(i/10)

for formula in formulas_list:
    result_list = []
    print("Calculated formula: {}".format(formula))
    start = time.time()

    for argument in argument_list:
        x = argument
        result_list.append((x, eval(formula)))
        print("Minimal calculated value is: {} Maximal calculated value is: {}".format(min(result_list), max(result_list)))

        stop = time.time()
        calculated_not_compiled = stop - start
        print("Time of end program: {}".format(calculated_not_compiled))


# kompilacja
import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
argument_list = []
for i in range(1000):
    argument_list.append(i/10)

for formula in formulas_list:
    result_list = []
    print("Calculated formula: {}".format(formula))
    start = time.time()

    compiled_formula = compile(formula, "equation", "eval")

    for argument in argument_list:
        x = argument
        result_list.append((x, eval(compiled_formula)))
        print("Minimal calculated value is: {} Maximal calculated value is: {}".format(min(result_list), max(result_list)))

    stop = time.time()
    calculated_compiled = stop - start
    print("Time of end program: {}".format(calculated_compiled))


