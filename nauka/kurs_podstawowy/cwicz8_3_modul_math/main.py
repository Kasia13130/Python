f_smaller = 3.141592653589793
f_bigger = 3.87756392764

import math

print(math.ceil(f_smaller), math.ceil(f_bigger))    # zwraca dla argumentu najmniejsza liczbe calkowita,
# ktora jest wieksza od wskazanego argumentu
print("\n")

print(math.floor(f_smaller), math.floor(f_bigger))  # zwraca najwieksza liczbe ktora jest mniejsza od podanego argumentu
print("\n")

print(math.ceil(- f_smaller), math.ceil(- f_bigger))    # najmniejsza liczba, wieksza od podanego argumentu
print("\n")

print(math.floor(- f_smaller), math.floor(- f_bigger))   # najwieksza liczba, ktora jest mniejsza od wskazanego argumentu
print("\n")

print(pow(2, 8), pow(9, 0.5))   # funkcja power, pierwszy argument to tenktory chcemy podniesc do potegi a druga to potega do ktorej chcemy podniesc,
# lub w drugim przypadku mozna wyliczyc pierwiastek czyli liczbe do poteki 0.5
print("\n")

print(math.sqrt(16))    # pierwiastek z 16
print("\n")

print(math.pi, math.e)  # stale pi oraz e
print("\n")

print(math.sin(math.pi/2), " ", math.cos(math.pi/4))    # funkcje trygonometryczne
print("\n")

# cwiczenie 3
degree = 360

print("Radiany: ", (math.pi * degree) / 180)

degree = 45

print("Radiany: ", (math.pi * degree/ 180))

print("inny zapis cwiczenia")
degree = 360
radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree, radian))

degree = 45
radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree, radian))
print('')

print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')

# cwiczenie 5
print(math.radians(360))
print(math.radians(45))

print("\n")

# cwiczenie 6
small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

print("Size of a small pizza in m^2: ", int(math.pi * small_pizza_r ** 2) / 1000)
print("Size of a big pizza in m^2: ", int(math.pi * big_pizza_r ** 2) / 1000)
print("Size of family pizza in m^2: ", int(math.pi * family_pizza_r ** 2) / 1000)

print("Price for m^2 small pizza: ", int((small_pizza_price * 1000) / int(math.pi * small_pizza_r ** 2)))
print("Price for m^2 big pizza: ", int((big_pizza_price * 1000) / int(math.pi * big_pizza_r ** 2)))
print("Price for m^2 family pizza: ", int((family_pizza_price * 1000) / int(math.pi * family_pizza_r ** 2)))

print("\n")

# inny zapis cwiczenia
small_area = math.pi * small_pizza_r ** 2
big_area = math.pi * big_pizza_r ** 2
family_area = math.pi * family_pizza_r ** 2

print('small', small_pizza_r, small_pizza_price, small_area)
print('big', big_pizza_r, big_pizza_price, big_area)
print('family', family_pizza_r, family_pizza_price, family_area)
print('')
print('small', small_pizza_price / small_area)
print('big', big_pizza_price / big_area)
print('family', family_pizza_price / family_area)

print("\n")

# cwiczenie 9
math_ls = dir(math)
print(math_ls)