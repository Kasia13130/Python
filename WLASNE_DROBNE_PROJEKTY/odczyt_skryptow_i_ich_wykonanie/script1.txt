import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(math.sin(x) * x**2))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))